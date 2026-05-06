"""
Cleanup pass on mobile-leads-enriched.csv:
- Strip URL-encoding artifacts (%20, %3A, etc.) from email strings
- Detect emails appearing on 3+ businesses (likely web devs / shared infra) and remove
- Prefer domain-matched emails (owner@theirbusiness.com) as primary
- Output mobile-leads-clean.csv with a clean single email + quality tier
"""

import csv
import re
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlparse

INPUT_CSV = Path(__file__).parent / "raw" / "mobile-leads-enriched.csv"
OUTPUT_CSV = Path(__file__).parent / "raw" / "mobile-leads-clean.csv"


def url_decode_email(e):
    """Strip %20 and other URL-encoding artifacts."""
    return unquote(e).strip().lower()


def extract_domain_from_website(website):
    """Get base domain from a website URL."""
    if not website:
        return None
    website = website.strip().lower()
    if not website.startswith(("http://", "https://")):
        website = "http://" + website
    try:
        netloc = urlparse(website).netloc
        return netloc.replace("www.", "")
    except Exception:
        return None


def main():
    # Load
    with open(INPUT_CSV, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        fieldnames = reader.fieldnames

    # --- Pass 1: clean URL encoding, split, recombine ---
    for row in rows:
        raw = row.get("emails_found", "")
        if not raw:
            row["_emails_list"] = []
            continue
        emails = [url_decode_email(e) for e in raw.split(";") if e.strip()]
        # dedupe while preserving order
        seen = set()
        deduped = []
        for e in emails:
            if e and e not in seen:
                seen.add(e)
                deduped.append(e)
        row["_emails_list"] = deduped

    # --- Pass 2: find cross-site contamination ---
    # Count how many distinct businesses each email appears on
    email_business_count = Counter()
    for row in rows:
        for e in set(row["_emails_list"]):
            email_business_count[e] += 1

    # Emails on 3+ businesses = likely shared/dev/agency emails
    contaminated = {e for e, c in email_business_count.items() if c >= 3}
    print(f"Found {len(contaminated)} cross-site emails (appearing on 3+ businesses):")
    for e in sorted(contaminated, key=lambda x: -email_business_count[x])[:15]:
        print(f"  {e} — on {email_business_count[e]} businesses")

    # --- Pass 3: pick best email per row ---
    # Priority:
    #   1. Email whose domain matches the business's own website domain (highest trust)
    #   2. Any non-contaminated, non-generic email
    #   3. Generic (info@, contact@) emails
    #   4. Gmail/Yahoo/etc personal emails
    GENERIC_PREFIXES = ("info@", "contact@", "hello@", "admin@", "office@",
                        "service@", "sales@", "support@")
    FREE_MAIL_DOMAINS = ("@gmail.com", "@yahoo.com", "@hotmail.com", "@outlook.com",
                          "@aol.com", "@icloud.com", "@comcast.net", "@msn.com")

    def score_email(e, site_domain):
        """Lower is better."""
        if e in contaminated:
            return 1000  # disqualify
        # Domain match = best (e.g., owner@theirbusiness.com)
        if site_domain and f"@{site_domain}" in e:
            # Named email on own domain = best
            if not e.startswith(GENERIC_PREFIXES):
                return 1
            # Generic on own domain = good
            return 2
        # Named email on a free mail provider (e.g. john@gmail.com) — plausible owner
        if any(d in e for d in FREE_MAIL_DOMAINS) and not e.startswith(GENERIC_PREFIXES):
            return 3
        # Generic on free mail
        if e.startswith(GENERIC_PREFIXES):
            return 4
        # Anything else
        return 5

    hit_count = 0
    domain_match_count = 0
    for row in rows:
        emails = [e for e in row["_emails_list"] if e not in contaminated]
        site_domain = extract_domain_from_website(row.get("website", ""))
        if emails:
            scored = sorted(emails, key=lambda e: score_email(e, site_domain))
            best = scored[0]
            row["primary_email"] = best
            row["emails_found"] = "; ".join(scored)
            if site_domain and f"@{site_domain}" in best:
                row["email_quality"] = "domain-match"
                domain_match_count += 1
            elif best.startswith(GENERIC_PREFIXES):
                row["email_quality"] = "generic"
            else:
                row["email_quality"] = "personal-freemail"
            hit_count += 1
        else:
            row["primary_email"] = ""
            row["emails_found"] = ""
            row["email_quality"] = ""
        del row["_emails_list"]

    # --- Write output ---
    new_fields = fieldnames + (["email_quality"] if "email_quality" not in fieldnames else [])
    with open(OUTPUT_CSV, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=new_fields)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)

    # --- Report ---
    quality_counts = Counter(r["email_quality"] for r in rows if r["email_quality"])
    total = len(rows)
    print()
    print(f"✓ Cleaned output: {OUTPUT_CSV}")
    print(f"  Total leads:               {total}")
    print(f"  With valid email:          {hit_count} ({hit_count * 100 // total}%)")
    print(f"  Domain-matched (best):     {quality_counts['domain-match']}")
    print(f"  Personal freemail:         {quality_counts['personal-freemail']}")
    print(f"  Generic (info@/contact@):  {quality_counts['generic']}")
    print(f"  Removed contaminated emails: dropped from {len(contaminated)} unique addresses")


if __name__ == "__main__":
    main()
