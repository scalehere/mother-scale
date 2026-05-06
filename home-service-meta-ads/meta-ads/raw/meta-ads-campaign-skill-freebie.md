---
title: "PDF to Markdown"
source: "https://pdf2md.morethan.io/"
author:
published:
created: 2026-04-12
description: "Converts PDF files to Markdown."
tags:
  - "clippings"
---
## The Meta Ads Campaign Deployment

## Guide

## Deploy Facebook & Instagram Ad Campaigns With One

## Claude Code Command

Most people spend 45 minutes clicking through Meta Ads Manager every time they launch a campaign.  
Video uploads, ad copy, UTMs, pixel setup, targeting. The same 20 clicks, every time.

This guide walks you through building a Claude Code skill that does the entire pipeline with one  
command. From "I have video ads ready" to "campaign is live on Meta" without ever opening Ads  
Manager.

Everything deploys PAUSED. You review in Ads Manager, then activate when you are ready.

This guide assumes you have never set up Claude Code or a Meta Developer App before. We start  
from zero.

## 1\. Set Up Claude Code (If You Haven't Already)

If you already have Claude Code running in VS Code, skip to Section 2.

### 1\. 1 Install VS Code

Download Visual Studio Code from code.visualstudio.com. It is free and works on Mac, Windows, and  
Linux. Install it and open it.

### 1\. 2 Install the Claude Code Extension

```
1. Open VS Code
2. Click the Extensions icon on the left sidebar (it looks like four squares)
```
```
3. Search for "Claude Code"
4. Find the one published by Anthropic and click Install
```

### 1\. 3 Sign In

```
1. Click the Claude Code icon in the top-right toolbar (the spark icon)
2. Sign in with your Anthropic account
3. If you do not have an account, create one at claude.ai
```

### 1\. 4 Verify It Works

Open the Claude Code panel and type:

```
What files are in this project?
```

If Claude responds with a list of your files, you are set up. Claude Code can now read your project,  
write code, run terminal commands, and execute skills.

### 1\. 5 What Are Skills?

Skills are custom commands you build inside Claude Code. They live in a folder called

#### .claude/skills/ in your project. Each skill has a SKILL.md file that tells Claude exactly

what to do when you type the command.

#### For this guide, the skill is /meta-ads-campaign. When you type it, Claude Code runs a 6 - phase

pipeline that deploys an entire Meta ad campaign from your terminal.

Section 3 of this guide walks you through creating the skill file step by step. You will paste the full skill  
definition into a file on your machine. After that, you set up the prerequisites and run your first  
campaign.

## 2\. Set Up the Meta Developer App

Before Claude Code can talk to Meta's advertising API, you need three things:

```
1. A Meta Developer App (this is how Meta authenticates API requests)
2. An access token (the key that lets your app manage ads)
3. The right permissions granted to that token
```

This section walks you through all three.

### 2\. 1 Create a Meta Developer Account

```
1. Go to developers.facebook.com
2. Click Get Started in the top right
3. Log in with the Facebook account that manages your business's ad account
4. Accept the developer terms
5. You now have a Meta Developer account
```

### 2\. 2 Create a New App

```
1. From the developer dashboard, click Create App
2. Choose Other as the use case
3. Select Business as the app type
4. Give it a name like "My Ad Deployer" or "Claude Code Ads"
5. Select the Business Portfolio that contains your ad account
6. Click Create App
```

Your app is now created. You will land on the app dashboard.

### 2\. 3 Add the Marketing API Product

```
1. On your app dashboard, scroll down to Add Products to Your App
2. Find Marketing API and click Set Up
```
```
3. This enables your app to manage ad campaigns, upload videos, and create ads
```

### 2\. 4 Create a System User

System users are special accounts designed for API access. Unlike personal tokens that expire in 60  
days, system user tokens can be long-lived.

```
1. Go to business.facebook.com/settings
2. In the left menu, click Users then System Users
3. Click Add to create a new system user
4. Name it something like "Claude Code Deployer"
5. Set the role to Admin (needs full access to create campaigns)
6. Click Create System User
```

### 2\. 5 Assign the Ad Account

```
1. On the system user you just created, click Add Assets
2. Select Ad Accounts
3. Find your client's ad account and check the box
4. Grant Full Control (the deploy pipeline needs to create campaigns, ad sets, and ads)
5. Click Save Changes
```

### 2\. 6 Generate an Access Token

```
1. Still on the system user page, click Generate New Token
2. Select the app you created in Step 2. 2
3. Check these permissions:
```

#### ads\_management (create and manage campaigns)

#### ads\_read (read campaign data)

#### pages\_read\_engagement^ (access^ Facebook^ Pages)

#### pages\_manage\_ads (publish ads through Pages)

```
4. Click Generate Token
5. Copy the token immediately. You will not see it again.
```

### 2\. 7 Add the Token to Your Project

#### Open your project's.env file (create one if it does not exist) and add:

```
META_ACCESS_TOKEN=paste_your_long_token_string_here
```

This is the only secret you need. Claude Code reads this token from your environment when deploying  
campaigns.

### 2\. 8 Find Your Ad Account ID

#### Your Meta ad account ID looks like act\_123456789. Find it in:

```
1. Meta Ads Manager - it is in the URL when you open any campaign
2. Or in Business Settings under Ad Accounts
```

Write this down. You will need it when setting up the database.

### 2\. 9 Find Your Facebook Page ID

Every Meta ad is published through a Facebook Page. Find the Page ID:

```
1. Go to your Facebook Page
2. Click About (or Page Transparency on newer layouts)
3. Scroll to the bottom where it says Page ID
```

Or use the API:

```
GET https://graph.facebook.com/v21.0/me/accounts?access_token={your_token}
```

#### This returns all Pages your system user can access. The id field is the Page ID.

### Quick Test

Verify your token works by running this in your terminal:

```
curl "https://graph.facebook.com/v21.0/me?access_token=YOUR_TOKEN_HERE"
```

If you get back a JSON object with your system user's name and ID, the token is working. If you get an  
error, double-check that you copied the full token and that the app is set up correctly.

## 3\. Create the Skill File

Now you will create the skill file that tells Claude Code how to deploy Meta ad campaigns. This is the

#### command definition that runs when you type /meta-ads-campaign.

### 3\. 1 Create the Skill Folder

Open your VS Code terminal and run:

```
mkdir -p ~/.claude/skills/meta-ads-campaign
```

Then create and open the skill file:

**On Mac:**

```
touch ~/.claude/skills/meta-ads-campaign/SKILL.md
code ~/.claude/skills/meta-ads-campaign/SKILL.md
```

**On Windows:**

```
touch $HOME/.claude/skills/meta-ads-campaign/SKILL.md
code $HOME/.claude/skills/meta-ads-campaign/SKILL.md
```

### 3\. 2 Paste the Skill Definition

#### Copy everything below and paste it into the SKILL.md file you just opened:

---

name: meta-ads-campaign  
description: Create and deploy a Meta (Facebook/Instagram) ad campaign end-to-end  
**trigger: /meta-ads-campaign  
\---**

**\# Meta Ads Campaign Deployer**

When the user triggers this skill with a client slug and objective, run this 6-phase  
pipeline:

**\## Phase 1: Gather Context**

- Look up the client in the database by slug
- Find their Meta ad account mapping (platform = 'meta **ads', is** active = true)
- Ask the user about: campaign objective, target audience (geo, age), daily budget,  
	landing page URL, funnel structure, and which video assets to include
- Read the META **ACCESS** TOKEN from.env

**\## Phase 2: Create Campaign Record**

- Insert a campaign row into the database with status 'draft'
- Register video assets with file paths, dimensions (vertical 1080x1920, feed 1080x1080,  
	landscape 1920x1080), and format labels
- If multiple formats exist for the same ad, group them for multi-format creative

**\## Phase 3: Generate Ad Copy**

- For each video ad, generate: primary text, headline (25 char limit), description, and  
	CTA type (LEARN **MORE, SIGN** UP, GET \_\_QUOTE, etc.)
- Present all copy to the user for review before saving
- Allow rewrites on any piece until the user approves\_

*\## Phase 4: Generate UTMs*

*\- Build UTM parameters per ad: utm* \_ source=facebook, utm **medium=paid** social, utm **campaign=  
{client-slug}-{month}-{year}-{objective}, utm** content={ad-slug}

- Bake full UTM URLs into the ad creative link (do not rely on url \_ *tags)*

*\## Phase 5: Pre-Deploy Checklist*

\_- Present a 10-point verification checklist: video files exist, copy approved, UTMs  
clean, geo targeting validated, pixel connected, Instagram actor connected, budget  
confirmed, landing page live, ad account active, Page ID valid

- Do not proceed until the user explicitly approves\_

*\## Phase 6: Deploy to Meta*

\_- Upload videos via the Meta Graph API

- Create campaign (PAUSED), ad set with Advantage+ audience, ads with pixel tracking
- Enable the pixel with custom\_\_ event \_\_type LEAD on the ad set
- Set targeting\_\_ automation advantage \_\_audience on every ad set
- Log every API call and response
- Return the Ads Manager URL for the new campaign\_

*\## Usage*

```
/meta-ads-campaign {client-slug} {objective}
Objectives: leads, traffic, awareness, conversions
```

Save the file. Your folder should look like this:

```
~/.claude/skills/
meta-ads-campaign/
SKILL.md
```

### 3\. 3 What the Skill Does (Summary)

The 6 phases handle the full lifecycle of a Meta ad campaign:

```
1. Gather Context - - pulls client data, ad account, and asks you about scope
2. Create Campaign Record - - saves a draft campaign with video assets to your database
3. Generate Ad Copy - - writes headlines, descriptions, and CTAs for each ad (you review before
saving)
4. Generate UTMs - - builds tracking URLs with consistent naming
5. Pre-Deploy Checklist - - 10 - point verification before anything touches Meta
6. Deploy to Meta - - uploads videos, creates the campaign, ad set, and ads via the API (all
PAUSED)
```

The pipeline never loses work. If a deploy fails halfway, re-running picks up where it left off.

## 4\. Database Prerequisites

The skill needs a few database records to know which client, which ad account, and which videos to  
deploy. If you are using Supabase (like this project), you can run these queries in the SQL Editor.

### 4\. 1 Your Client Record

#### Your client needs a row in the clients table. Check if it exists:

```
SELECT id, name, slug FROM clients WHERE slug = 'your-client-slug';
```

If nothing comes back, add the client through your admin dashboard or insert directly:

```
INSERT INTO clients (name, slug)
VALUES ('Your Client Name', 'your-client-slug')
RETURNING id;
```

#### Save the id (UUID). You will need it for the next steps.

### 4\. 2 Ad Account Mapping

This tells the deploy pipeline which Meta ad account to use for this client:

```
INSERT INTO ad_account_mappings (client_id, platform, account_id, account_name,
is_active)
VALUES (
'your-client-uuid',
'meta_ads',
'act_123456789', -- your Meta ad account ID from Section 2.
'Client Ad Account', -- a friendly name
true
);
```

### 4\. 3 Video Assets

Your video ads need to be rendered MP 4 files accessible from your machine. Supported formats:

```
Vertical (Stories/Reels): 1080 x 1920 ( 9 : 16 )
Feed (Square): 1080 x 1080 ( 1 : 1 )
Landscape : 1920 x 1080 ( 16 : 9 )
```

If you render all three formats for the same ad, the pipeline creates a multi-format creative that serves  
the best format per placement automatically.

### Quick Prerequisite Check

Run this single query to verify everything is ready:

```
SELECT
c.slug,
c.name,
aam.account_id,
aam.is_active
FROM clients c
LEFT JOIN ad_account_mappings aam
ON aam.client_id = c.id AND aam.platform = 'meta_ads' AND aam.is_active = true
WHERE c.slug = 'your-client-slug';
```

#### You should see is\_active = true and a valid account\_id.

## 5\. Your First Campaign: Step by Step

### 5\. 1 Run the Skill

Open Claude Code in your project and type:

```
/meta-ads-campaign your-client-slug leads
```

The first argument is the client slug from your database. The second is the campaign objective.  
Options:

```
Objective When to Use
leads Lead generation campaigns (most common)
traffic Drive visitors to a landing page
awareness Brand awareness and reach
conversions Website conversion events
```

### 5\. 2 Claude Code Asks Questions

Claude will ask you about six things:

```
1. Campaign objective - Already set from your argument, but you can override
2. Target audience - Geographic region, age range
3. Budget - Daily budget in dollars (e.g., "$ 20 /day")
```

**4\. Landing page** - Where clicks go (e.g., (^) https://yourclient.com/free-quote )  
**5\. Funnel structure** - Single ad set or split by funnel stage  
**6\. Video assets** - Which rendered videos to include  
Answer conversationally. Claude handles all the data formatting and database insertions.

### 5\. 3 Review Ad Copy

Claude generates ad copy for each video and presents it for review:

```
Ad 1: "Rate Hikes"
Primary text: Your electricity rate just went up again...
Headline: Stop Paying More Every Year
Description: Free solar savings report
CTA: LEARN_MORE
Approve? (y/n)
```

Nothing is saved until you approve. You can ask Claude to rewrite any piece.

### 5\. 4 Pre-Deploy Checklist

Before anything touches Meta, Claude presents a 10 - point checklist:

```
All video assets exist at their file paths
All ad copy reviewed and approved
UTM URLs are clean
Geographic targeting validated
Landing pages live
Facebook Page ID set
Ad account mapping active
Budget set
Content details accurate
No special ad category violations
```

#### You approve, and Claude sets the campaign status to ready.

### 5\. 5 Deploy

Claude calls the deploy endpoint. You will see output like:

```
Uploading video 1/10: Rate Hikes - Vertical... done
Uploading video 2/10: Rate Hikes - Feed... done
Creating campaign... PAUSED
Discovering pixel... PSS Pixel (123456)
Creating ad set... done
Creating ad 1/10... done
...
All 10 ads deployed successfully. Campaign is PAUSED.
```

Everything is PAUSED. Open Meta Ads Manager to review, then activate when ready.

## 6\. How the Deploy Pipeline Works

When you trigger deployment, here is what happens under the hood:

### Video Upload (with Resume)

Each video file is uploaded to Meta via the Graph API. If a video was already uploaded (has a stored  
Meta video ID), it is skipped. This means a failed deploy can be re-run without re-uploading gigabytes  
of video.

### Campaign Creation

The campaign is created with status PAUSED. Budget is set at the campaign level when using  
Campaign Budget Optimization (CBO), which is the default. The API expects budget in cents. The  
pipeline converts your dollar amount automatically.

### Pixel Auto-Discovery

The pipeline finds the active Meta Pixel on the ad account and attaches it to the ad set. This means  
conversion tracking is set up automatically. If no pixel is found, the deploy continues but logs a  
warning.

### Ad Set with Advantage+ Audience

The ad set is created with your targeting and Advantage+ audience enabled. This lets Meta expand  
beyond your seed audience for better results. It is always enabled.

### UTM Generation

For each ad, tracking URLs are built:

```
https://yourclient.com/free-quote?utm_source=meta&utm_medium=paid_social&utm_campaign=your-
client-march-2026-leads&utm_content=v1-tof-rate-hikes-news
```

### Multi-Format Creatives

If your ad has multiple video formats (vertical, feed, landscape), the pipeline creates a multi-format  
creative. Meta serves the best format per placement automatically. If multi-format fails, it falls back to  
single-video.

### Everything Logged

Every step is logged to the (^) ad\_deploy\_log table with the request, response, status, and any  
errors. Complete audit trail.

## 7\. Geographic Targeting

Getting the region key wrong is the most common deployment mistake. Meta's geolocation keys are  
not intuitive, and a wrong key can target the wrong country entirely.

### Always Validate via the API

Before deploying, look up the correct region key:

```
GET https://graph.facebook.com/v21.0/search?
type=adgeolocation&location_types=region&q=Saskatchewan&access_token={token}
```

The response includes a (^) key field. Verify three things:

#### 1\. The key matches what you expect

**2.** The (^) country\_code is correct (e.g., (^) CA for Canada)

#### 3\. The name is the right region

### Common Mistakes

#### Wrong region key: Region key 3901 looks like it could be Canadian, but it is actually Uruguay.

Always search, never guess.

#### Country + region conflict: If you set both countries: \["CA"\] and regions: \[{"key":

#### "536"}\],^ Meta^ targets^ all^ of^ Canada,^ not^ just^ the^ region.^ Use^ one^ or^ the^ other.

## 8\. Post-Deploy Verification

After the deploy finishes, run these checks:

### Check Meta IDs

```
SELECT video_title, meta_ad_id, meta_campaign_id, meta_adset_id, status
FROM video_ad_units
WHERE campaign_id = 'your-campaign-uuid';
```

Every row should have all Meta IDs populated. If any ID is null, that ad failed. Check the deploy logs.

### Check Deploy Logs

```
SELECT action, status, error_message
FROM ad_deploy_log
WHERE campaign_id = 'your-campaign-uuid'
ORDER BY created_at;
```

Look for any rows with (^) status = 'failed'.

### Verify Pixel

```
GET https://graph.facebook.com/v21.0/{adset_id}?fields=promoted_object&access_token={token}
```

#### Confirm pixel\_id is present in the response.

### Verify Targeting

```
GET https://graph.facebook.com/v21.0/{adset_id}?fields=targeting&access_token={token}
```

Confirm the region key and Advantage+ audience are correct.

## 9\. Troubleshooting Common Issues

### Video Upload Fails

Re-run the deploy. Resume support skips already-uploaded videos. If uploads keep failing:

```
Check the file path exists and is readable
Verify it is a valid MP 4 (H. 264 codec)
Confirm file size is under Meta's 4 GB limit
```

#### Verify your token has ads\_management permission

### Missing Pixel

Deploy continues without a pixel and logs a warning. To fix: create a pixel in Meta Events Manager,  
install it on the landing page, then re-deploy.

### Wrong Region Key

Update targeting directly on Meta:

```
POST https://graph.facebook.com/v21.0/{adset_id}
{
"targeting": {
"geo_locations": { "regions": [{"key": "correct-key"}] },
"targeting_automation": { "advantage_audience": 1 }
}
}
```

### Partial Deploy Failure

Campaign status is set to (^) error. Fix the issue, then reset:  
UPDATE ad\_campaigns SET status = 'ready', deploy\_error = NULL WHERE id = 'your-campaign-  
uuid';  
Re-run the deploy. It picks up where it left off.

### Token Expired or Invalid

If you used a personal token instead of a system user token, it expires after 60 days. Go back to  
Section 2. 6 and generate a new system user token. System user tokens do not expire.

### "App Not Approved" Error

New Meta apps start in Development Mode, which limits API access. For development and testing, this  
is fine. For production:

```
1. Go to your app dashboard at developers.facebook.com
2. Switch from Development to Live mode
3. You may need to complete Meta's App Review for certain permissions
```

For most ad deployment use cases, Development Mode is sufficient if your system user has direct  
access to the ad account.

## 10\. UTM Tracking Reference

### Campaign Slug Format

```
{client-slug}-{month}-{year}-{objective}
```

#### Example: acme-roofing-march-2026-leads

Rules:

```
Lowercase, hyphen-separated
No internal tool names (never "remotion", "claude", etc.)
No redundant date suffixes
```

### Content Tag Format

```
v{version}-{funnel_stage}-{descriptive-slug}
```

Examples:

#### v1-tof-rate-hikes-news (top of funnel)

#### v1-mof-customer-testimonial (mid funnel)

#### v1-bof-free-quote-offer (bottom of funnel)

### Full URL Structure

```
{landing_page}?utm_source=meta&utm_medium=paid_social&utm_campaign={slug}&utm_content=
{content}
```

## 11\. Next Steps

**Monitor your campaigns.** Once you activate ads in Meta Ads Manager, track spend, impressions,  
clicks, and cost per lead. The database stores Meta IDs so you can pull performance data  
programmatically.

**Iterate on creative.** Your first batch gives you baseline data. Use performance numbers to identify  
which hooks and formats work best. Render new variations and deploy with the same skill.

**Scale to multiple clients.** The skill is client-agnostic. Adding another client is just a database row and  
an ad account mapping. Same pipeline handles everything.

**Follow @KyleWhitrow** on Instagram for more Claude Code automation content, including how to build  
custom skills like this one from scratch.

**Visit** nustimulus.com to connect with other builders using AI-powered automation to grow their  
businesses.

Built with Claude Code. Deployed from the terminal.

```
Send an email to kyle@nustimulus.com for inquiries.
nustimulus.com
```