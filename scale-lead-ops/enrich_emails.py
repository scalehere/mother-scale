"""
Email enrichment scraper for mobile-leads.csv.

Visits each lead's website (homepage + common contact pages), extracts
emails via mailto: links and regex matching, outputs enriched CSV.

Output: raw/mobile-leads-enriched.csv with new `emails_found` column
(semicolon-separated list of unique emails).
"""

import csv
import re
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

# --------------------------- config ---------------------------

INPUT_CSV = Path(__file__).parent / "raw" / "mobile-leads.csv"
OUTPUT_CSV = Path(__file__).parent / "raw" / "mobile-leads-enriched.csv"

# Paths to check on each domain (homepage + common contact pages)
PATHS_TO_CHECK = ["", "/contact", "/contact-us", "/about", "/about-us", "/contact.html"]

TIMEOUT = 8  # seconds per request
MAX_WORKERS = 15  # parallelism
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0 Safari/537.36"

# Email regex — standard pattern, then we filter junk after
EMAIL_RE = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")

# Emails we never want (stock footer / plugin noise)
JUNK_PATTERNS = [
    "example.com", "domain.com", "yoursite.com", "yourdomain.com",
    "sentry.io", "sentry.wixpress.com", "wixpress.com",
    "godaddy.com", "noreply", "no-reply", "donotreply",
    "@2x.png", "@3x.png",  # retina image filenames that look like emails
    "yourname@", "email@", "name@",
]

# Extensions that aren't emails (image filenames caught by regex)
IMAGE_EXTS = (".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".ico")

# --------------------------- helpers ---------------------------

def clean_emails(raw_emails, domain):
    """Filter junk, dedupe, prefer same-domain emails."""
    cleaned = set()
    for e in raw_emails:
        e = e.lower().strip().rstrip(".,;:")
        if any(j in e for j in JUNK_PATTERNS):
            continue
        if e.endswith(IMAGE_EXTS):
            continue
        if len(e) > 60:  # absurdly long = probably a false match
            continue
        cleaned.add(e)
    # sort: same-domain first, then alphabetical
    if domain:
        return sorted(cleaned, key=lambda e: (not e.endswith("@" + domain), e))
    return sorted(cleaned)


def extract_emails_from_html(html, base_url):
    """Pull emails from mailto: links + page text."""
    emails = set()
    try:
        soup = BeautifulSoup(html, "html.parser")
        # mailto: links are the highest quality signal
        for a in soup.find_all("a", href=True):
            href = a["href"]
            if href.lower().startswith("mailto:"):
                addr = href[7:].split("?")[0].strip()
                if addr:
                    emails.add(addr)
        # regex pass over full text (catches plain-text emails)
        text = soup.get_text(" ", strip=True)
        emails.update(EMAIL_RE.findall(text))
        # also check raw HTML for obfuscated cases
        emails.update(EMAIL_RE.findall(html))
    except Exception:
        pass
    return emails


def normalize_url(raw):
    """Ensure URL has scheme, strip trailing path."""
    if not raw or not isinstance(raw, str):
        return None
    raw = raw.strip()
    if not raw:
        return None
    if not raw.startswith(("http://", "https://")):
        raw = "http://" + raw
    try:
        p = urlparse(raw)
        if not p.netloc:
            return None
        return f"{p.scheme}://{p.netloc}"
    except Exception:
        return None


def scrape_site(website_url):
    """Fetch a few pages on a domain, return set of emails found."""
    base = normalize_url(website_url)
    if not base:
        return set()

    domain = urlparse(base).netloc.lower().replace("www.", "")
    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT})

    emails = set()
    for path in PATHS_TO_CHECK:
        url = urljoin(base, path) if path else base
        try:
            r = session.get(url, timeout=TIMEOUT, allow_redirects=True)
            if r.status_code == 200 and r.text:
                emails.update(extract_emails_from_html(r.text, url))
                # if we got emails from homepage, can stop early
                if path == "" and emails:
                    # still check /contact for completeness
                    continue
        except Exception:
            continue

    return clean_emails(emails, domain)


# --------------------------- main ---------------------------

def main():
    if not INPUT_CSV.exists():
        print(f"ERROR: {INPUT_CSV} not found")
        sys.exit(1)

    # Read input CSV
    with open(INPUT_CSV, "r", encoding="utf-8", errors="replace") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        fieldnames = reader.fieldnames

    total = len(rows)
    print(f"Loaded {total} rows from {INPUT_CSV.name}")
    print(f"Enriching with email scraping ({MAX_WORKERS} workers)...\n")

    # Scrape in parallel
    results = {}
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        future_to_idx = {
            executor.submit(scrape_site, row.get("website", "")): i
            for i, row in enumerate(rows)
        }
        done = 0
        for future in as_completed(future_to_idx):
            idx = future_to_idx[future]
            try:
                emails = future.result()
            except Exception:
                emails = set()
            results[idx] = emails
            done += 1
            if done % 25 == 0 or done == total:
                hits = sum(1 for v in results.values() if v)
                print(f"  {done}/{total} scraped — {hits} with emails ({hits * 100 // max(done, 1)}% hit rate)")

    # Write enriched CSV
    new_fieldnames = fieldnames + ["emails_found", "primary_email"]
    hit_count = 0
    with open(OUTPUT_CSV, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=new_fieldnames)
        writer.writeheader()
        for i, row in enumerate(rows):
            emails = results.get(i, set())
            if emails:
                hit_count += 1
            row["emails_found"] = "; ".join(sorted(emails))
            row["primary_email"] = next(iter(sorted(emails))) if emails else ""
            writer.writerow(row)

    print(f"\n✓ Done. Wrote {OUTPUT_CSV}")
    print(f"  Total leads:        {total}")
    print(f"  With email found:   {hit_count} ({hit_count * 100 // total}%)")
    print(f"  Without email:      {total - hit_count}")


if __name__ == "__main__":
    main()
