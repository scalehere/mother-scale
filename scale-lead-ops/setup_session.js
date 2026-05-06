#!/usr/bin/env node
/**
 * LeadOps Instagram Session Setup
 * ─────────────────────────────────────────────────────────────
 * Run once to log into Instagram and save the session so
 * Agent 1 can navigate profiles without hitting login walls.
 *
 * Usage:  node setup_session.js
 * Re-run: every ~2 weeks when login walls reappear
 * ─────────────────────────────────────────────────────────────
 */

const path     = require('path');
const fs       = require('fs');
const readline = require('readline');

const SESSION_PATH = path.join(__dirname, '.auth', 'session.json');

function waitForEnter(msg) {
  const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
  return new Promise(resolve => rl.question(msg, () => { rl.close(); resolve(); }));
}

async function run() {
  let chromium;
  try {
    ({ chromium } = require('playwright'));
  } catch {
    console.error('\n❌  playwright not found. Run:  npm install playwright && npx playwright install chromium\n');
    process.exit(1);
  }

  console.log('\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
  console.log('  LeadOps — Instagram Session Setup');
  console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n');
  console.log('⚠️  Use a BURNER account — not your personal Instagram.\n');

  const browser = await chromium.launch({
    headless: false,
    slowMo: 50
  });

  const context = await browser.newContext({
    viewport: { width: 1280, height: 800 },
    userAgent: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
  });

  const page = await context.newPage();

  // Navigate — don't wait for networkidle, Instagram never settles
  await page.goto('https://www.instagram.com/accounts/login/', {
    waitUntil: 'load',
    timeout: 60000
  });

  console.log('Browser is open at instagram.com/accounts/login/');
  console.log('\n→ Log into your Instagram burner account');
  console.log('→ Wait until your home feed is showing posts');
  console.log('→ Then come back here and press Enter\n');

  await waitForEnter('Press Enter once you are logged in and see the home feed: ');

  // Verify login state
  const loggedIn = await page.evaluate(() => {
    return window.location.href.includes('instagram.com') &&
           !document.querySelector('input[name="username"]');
  }).catch(() => false);

  if (!loggedIn) {
    console.log('\n⚠️  Could not confirm login — saving anyway.');
    console.log('    If the session does not work, re-run this script.\n');
  } else {
    console.log('\n✅  Login confirmed.\n');
  }

  // Save session
  await context.storageState({ path: SESSION_PATH });
  await browser.close();

  const size = (fs.statSync(SESSION_PATH).size / 1024).toFixed(1);
  console.log(`✅  Session saved → .auth/session.json (${size} KB)`);
  console.log('\n  Done. Restart Claude Code to activate the session.');
  console.log('  Re-run this script in ~2 weeks if login walls return.\n');
}

run().catch(err => {
  console.error('\n❌  Error:', err.message, '\n');
  process.exit(1);
});
