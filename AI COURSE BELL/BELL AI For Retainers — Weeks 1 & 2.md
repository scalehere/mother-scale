# AI For Marketing Agencies — Retainer Understanding
## WEEK 1 + WEEK 2 COURSE HANDOUT
### Session 1A & 1B (Foundation) + Session 2A & 2B (Discovery)

**Internet Connection:** xxxxxxxxxxxxxx  **Make a copy of this sheet so you can edit your prompts as you go.**

---

## MASTER SCHEDULE AT A GLANCE

| Week | Client Stage | Primary Tool(s) | Gem/Asset Built | Output |
|------|-------------|-----------------|-----------------|--------|
| **1** | Foundation | Gemini Gems | Client Capability Architect | Master Capability Statement v3 |
| **2** | Discovery | Gemini Gems + Deep Research + NotebookLM | Opportunity Scout + Evidence Base | Shortlist of 3-5 real prospects you're qualified for |
| **3** | Qualification | NotebookLM + Gemini Gems | Prospect Qualifier + Client Intelligence Profile | Go/No-Go score on top prospect + client dossier |
| **4** | Proposal Drafting | Gemini Gems + Nano Banana + Pomelli + Veo | Proposal Architect + Brand Credibility Pack + 60-sec Video CS | Full proposal draft + visual collateral + video pitch |
| **5** | Outreach + Scale | Gemini Gems + Opal | Outreach Checklist Agent + No-Code Pitch App | Real sent pitch + reusable team app |

---

## THE GOOGLE TOOL STACK — WHEN EACH ONE EARNS ITS PLACE

| Tool | What it does | Why it matters for retainers | Introduced in |
|------|-------------|------------------------------|---------------|
| **Gemini Gems** | Reusable AI assistants with custom instructions | Every Gem is a saved playbook for a specific client acquisition task. Build once, run forever. | Week 1 |
| **Deep Research** | Multi-step autonomous research mode | Pulls company news, social proof, competitor landscape, ad spend signals, and review history — the "prospect intelligence" that elite agencies pay $5K/month for | Week 2 |
| **NotebookLM** | Upload 50+ documents, AI synthesizes patterns across all of them | Reads multiple client briefs from the same vertical at once, finds language patterns, builds Client Intelligence Profiles. Also stores your case study evidence base. | Week 2 + 3 |
| **Nano Banana** | High-quality image generation and editing | Cover pages, process diagrams, before/after visuals, case study graphics that make small agencies look enterprise | Week 4 |
| **Pomelli** | AI-powered branded marketing campaigns | One-pagers, capability sheets, branded collateral that match client aesthetic standards | Week 4 |
| **Veo** | AI video generation | 60-second video Capability Statements, pitch meeting intros, client case study videos | Week 4 |
| **Opal** | No-code AI app builder | Turns your chained Gems into actual mini-apps your team can use without prompting knowledge. Train-the-trainer + scaling moment. | Week 5 |
| **Antigravity** | Agentic IDE for automation builds | Optional advanced path for participants who want to automate lead monitoring and inbound tracking | Week 5 (optional) |

---

## THE PROMPTING SKILL LADDER

Each week teaches new prompting skills that compound on the last week's. By Week 5, participants have a full prompting toolkit — not just a set of tools.

| Week | New Skill Taught | Total Skills in Their Toolkit |
|------|-----------------|-------------------------------|
| **1** | Interview-first prompting, Critique-Rewrite loop, Persona stacking, Frame shifting, Collaborative prompting | 5 skills |
| **2** | Multi-source synthesis (Deep Research), Document grounding (NotebookLM), Filter chaining | 8 skills |
| **3** | Pattern extraction across documents, Comparative analysis, Compliance matrix building | 11 skills |
| **4** | Visual prompt engineering, Multi-modal chaining (text→image→video), Brand consistency prompting | 14 skills |
| **5** | App-level prompt design (Opal), System-level orchestration, Self-critiquing meta-prompts | 17 skills |

---

---

# SESSION 1A — IN-PERSON
## "Build Your Client Capability Architect"

**Duration:** 90 minutes  **Tool:** Google Gemini (free version)  **Prompt Budget:** 7 prompts  
**Outcome:** A working Gem called the Client Capability Architect, plus a Capability Statement that has been built, critiqued, and refined.

---

### THE FRAME (what you'll learn today)

Today is not really about building a Capability Statement. Today is about learning how to prompt.

The Capability Statement is the deliverable. The skill is the prompting pattern: ask the AI to interview you, answer carefully, generate a draft, have the AI critique its own draft, then rewrite. That's the loop. You'll use this loop for the rest of your life with any AI tool.

We'll do it 7 times today, in 7 different ways. Watch the pattern.

---

## PART 1 — INTRODUCTION + THE 5-PART FRAMEWORK
**(0:00 – 0:20 | 20 minutes)**

### Why we're here

Marketing agencies in every city leave thousands of dollars on the table every month — not because their work isn't good, but because they can't clearly explain what they do, who it's for, and why it works. Most of those retainers go to the same handful of agencies — not because they're the best, but because they know how to write the pitch.

Over five weeks, you're going to build five AI tools that handle the four stages of winning retainer clients: finding opportunities, qualifying them, writing the proposal, and closing it. Today we build the foundation everything else stands on. That foundation is your **Capability Statement.**

### What a Capability Statement actually is

A Capability Statement is a one-to-two page document that tells a prospective client, in 30 seconds, who you are, what you do, what you've done before, and why you can be trusted with their marketing budget. Every pitch you send gets backed by one. If yours is generic, your pitch is dead before it's read.

By the end of today, you'll have one that's been worked over by an AI playing the role of a skeptical business owner who's been burned by agencies before.

### The 5-Part Prompt Framework

Every good prompt has five parts. Pull out the Prompting 101 Cheatsheet.

| Part | What it does | Quick example |
|------|-------------|---------------|
| **ROLE** | Who the AI should be | "You are an expert in marketing agency positioning..." |
| **TASK** | What you want done | "Help me build a Capability Statement..." |
| **CONTEXT** | Background it needs | "I run a small agency in San Diego that does..." |
| **FORMAT** | How the output should look | "Format as a two-page document with these sections..." |
| **REFERENCES** | Examples or source materials | "Use the standards a skeptical business owner would score against..." |

You don't need to memorize this. You need to recognize it. Every one of the 7 prompts today uses this pattern. Watch for it.

### About Gemini's prompt limits

Free Gemini gives you a limited number of prompts per day. I am giving you exactly 7 today. Each one earns its place. Don't experiment off-script during class. If you want to play, save it for after.

---

## PART 2 — THE INTERVIEW + DRAFT
**(0:20 – 1:00 | 40 minutes)**

### Get into Gemini

Open your browser. Go to **gemini.google.com**. Make sure you're logged into your Google account. The text box at the bottom is where everything happens.

---

### PROMPT 1 — THE INTERVIEW STARTER

**Why this prompt matters:** Most people waste their first prompt by trying to tell the AI everything. We're flipping it. We're going to make Gemini ASK US the right questions. This works because Gemini knows what business owners look for when evaluating agencies. You know your business. We're putting them together.

**Type this exactly:**

```
You are an expert in marketing agency positioning and client acquisition,
with deep experience in helping small agencies win retainer clients across
industries including home services, local business, e-commerce, and
professional services.

I am a marketing agency owner. I want to build a professional Capability
Statement — the foundation document I will use for every retainer pitch
and inbound response.

Before you write anything, INTERVIEW ME. Ask me the 7 questions below, all
at once, in a single message. Do not write the Capability Statement yet.

When you ask the questions, frame them like this:

---

Before I write anything, I need to interview you. Read all 7 questions
first, then answer them in order. Take your time.

A heads up: I am going to push you toward uncomfortable specificity. Most
Capability Statements lose because they sound like every other agency in
the stack. Generic answers here produce generic statements that get deleted
after one sentence. If you catch yourself writing "we provide quality
service" or "experienced team," scratch it and dig deeper.

QUESTION 1: What do you actually do, and what do you walk away from?

Do not give me a service list. Tell me what someone would see if they
followed you around for a week. What problem are you the obvious answer to
for your ideal client? Then flip it: what kind of work do you turn down or
refer out, and why? Your "no" tells me more about your positioning than your
"yes." Also list your primary and secondary service categories — for example:
Meta Ads, Google Ads, SEO, Social Media Management, Email, Video Production,
Funnel Building. If you're not sure how to categorize yourself, describe the
work and I'll suggest categories back.

QUESTION 2: Give me your three Gold Nuggets, with the receipts.

Business owners do not trust adjectives. They trust numbers, dates, and
dollar amounts. Pick the three client results you are proudest of. For each
one, tell me: What type of business was the client? What was the monthly
retainer value? When did the engagement run? What specific outcome can you
prove — leads generated, cost per lead, ROAS, revenue driven, conversion
rate improvement, ad spend managed? If you cannot put a number on it, it
does not go in the statement. If your best work is from a previous job or
a side project, give me those wins with the same level of detail. We will
translate them into agency-friendly language.

QUESTION 3: What is in your credential stack, and what is the gap?

Three parts:
1. List every credential you currently hold (Meta Business Partner,
   Google Partner, HubSpot certified, TikTok for Business, industry
   associations, platform certifications, anything you can put a logo on).
2. List every credential you are eligible for but have not completed.
   Be honest about why — paperwork fatigue, didn't know it existed,
   started and stalled, didn't seem worth it.
3. Tell me your business structure (LLC, sole prop, S-corp) and how
   long you've been operating. This determines how you position your
   credibility to larger clients.

QUESTION 4: Which client types are your "dream three," and where have
you been losing?

Name the three client verticals or business types you most want to serve
(home service, e-commerce, med spa, restaurant, real estate, legal, etc.).
For each one: have you ever pitched one? If yes, did you win or lose, and
do you know why? If no, what has been stopping you? Then give me your
retainer range — the smallest retainer that is actually worth your time,
and the largest you could execute without dropping the ball. Be honest
about both ends.

QUESTION 5: Who can you put on the field tomorrow?

Capacity is where most small agency statements quietly lie. I need the
truth. How many people are on your team full-time? How many reliable
contractors or specialists can you call on within a week? What is the
biggest single client engagement you have managed end-to-end (in monthly
budget and in scope)? If a $10,000/month client signed on Monday, what
would you have to do by Friday to be ready to deliver? Geographic or
industry service area: what is the actual type of client you can serve
without your results collapsing?

QUESTION 6: What do your competitors do that you would refuse to do,
and what do you do that they will not?

This is the differentiator question, and it is the one most agency owners
answer wrong. "Quality work" and "great communication" are not
differentiators. Every competitor says that. Try this instead: When a
happy client refers you to someone new, what story do they tell about your
work? What is the thing you do that you have watched other agencies skip
or cheap out on? What is the thing competitors do — a sales tactic, a
corner cut, a way of treating client budgets — that you have decided you
will not do, even when it costs you a deal? If nothing comes to mind,
talk to your last three happy clients before you answer this. Their words
are gold.

QUESTION 7: Who is already in your corner?

List every real referral relationship, white-label partnership, or
strategic alliance you have. For each one: how did the relationship start,
what work have you actually done together, and would they refer you a
client tomorrow if you asked? Then tell me who is missing. If you could
partner with one complementary agency or specialist firm to unlock a
class of clients you cannot serve alone, who would it be? We may use the
Capability Statement to attract them.

---

Once I have all 7 answers, I will build your Capability Statement. After
the draft, I will run it through a skeptical business-owner critique mode
and tell you exactly what would get questioned, what is missing, and what
to tighten before any client sees it.
```

**Send it. Read what comes back. Don't answer yet.**

---

**Quick group check (3 minutes)**

Look up. Three volunteers — read me your first question out loud. Notice how Gemini's questions are slightly different per person but always cover the same ground. **That's the pattern of a good intake interview.** Most consultants charge two grand for this conversation.

---

### PROMPT 2 — THE ANSWER DUMP

**Why this prompt matters:** Every separate message uses one of your daily prompts. So we answer ALL 7 questions in ONE message. This is a habit worth building — batching context-heavy responses saves prompts and gives the AI a richer single picture.

**The voice trick:** Use the microphone button on your keyboard. Just talk. Ramble. Tell stories. Gemini doesn't care if it's grammatically perfect. Gemini WANTS your voice. The way you actually talk about your agency is more useful than a polished sentence.

**The number rule:** When Gemini asks about past results, give NUMBERS. "Generated 47 leads in 60 days." "Cut cost per lead from $85 to $22." "Managed $40,000 in monthly ad spend." Numbers are gold. Business owners look for numbers.

**The differentiator rule:** Don't say "great client communication" or "we care about results." Everybody says that. Be specific. "I'm the only agency in San Diego that exclusively serves home service businesses." "My team built a 10-agent AI production pipeline that creates ad creative in 48 hours instead of two weeks." Specific beats impressive.

**Now type:**

```
Here are my answers to all 7 questions:

1. [YOUR ANSWER — voice-typed if you can]
2. [YOUR ANSWER]
3. [YOUR ANSWER]
4. [YOUR ANSWER]
5. [YOUR ANSWER]
6. [YOUR ANSWER]
7. [YOUR ANSWER]

Confirm you have what you need. If you have any clarifying questions,
ask them now in the same message before we move forward.
```

**Take 12 minutes. Send it.**

---

**Group share (3 minutes)**

Anyone get a clarifying question back from Gemini? Share one. This tells us what most people leave out — and that gap is usually the same thing they'd leave out of a real pitch.

---

### PROMPT 3 — THE FIRST DRAFT

**Why this prompt matters:** Now we ask for the actual document. The first draft is never the final draft. The point of this prompt is to get something on the page so we have something to critique. **Bad drafts are easier to fix than blank pages.**

**Type:**

```
Now write my Capability Statement.

Format it as a clean, two-page document with these sections:
- Company Overview (one paragraph)
- Core Services (bulleted, with service categories alongside)
- Client Results (2-3 highlights with measurable outcomes)
- Credentials and Certifications
- Target Clients and Service Area
- Differentiators (what makes me different, in plain language)
- Contact Information (placeholder)

Tone: professional but human. No corporate buzzwords. No
"transformative" or "innovative." Real language a business owner
would respect.
```

**Send. Read it. Don't get attached. We're about to break it.**

---

## PART 3 — THE CRITIQUE LOOP
**(1:00 – 1:30 | 30 minutes)**

### The most important skill in this whole program

Watch what happens next. We're going to use AI to critique AI. Then we're going to use the critique to make the original better. **This loop — generate, critique, rewrite — is the entire skill.** You'll use it in every Gem you build for the next four weeks.

---

### PROMPT 4 — THE SKEPTICAL BUSINESS OWNER CRITIQUE

**Why this prompt matters:** Right now Gemini is on your side. It wrote you a draft and it likes the draft. We need an adversary. So we're going to ask Gemini to put on a different hat — a skeptical business owner who has evaluated 500 agency pitches this year. The goal is to find what's weak BEFORE a real client does.

**Type:**

```
Now act as a skeptical, experienced business owner who runs a
$2M/year home service company. You've evaluated pitches from 500
marketing agencies this year. You've seen every kind of fluff
and exaggeration.

Read the Capability Statement you just wrote. Tell me:

1. The 3 weakest claims — places where the language sounds
   generic or unsupported.
2. The 2 most critical pieces of evidence that are missing —
   things I should add to be more credible.
3. The 1 thing in this statement that would actually make you
   pick up the phone and call this agency.

Be direct. Don't soften the feedback. Treat me like an agency
owner you want to help, not a friend you don't want to hurt.
```

**Send. Read the critique. Don't be defensive. This is the most expensive consulting you'll never pay for.**

---

**Pair work (8 minutes)**

Pair up with the person next to you.
- Read your Skeptical Business Owner Critique to your partner — out loud, the whole thing.
- After each person reads, the partner asks ONE question: **"Which piece of feedback hits hardest? Which one are you going to fix right now?"**
- Both partners should be able to name their TOP fix before the 8 minutes are up.

This pair work matters. Reading your AI critique to another human forces you to actually hear it.

---

### PROMPT 5 — THE REWRITE

**Why this prompt matters:** Critique without action is therapy. We're going to take what Gemini just told us and feed it RIGHT BACK to fix the document. This is the move that separates people who use AI well from people who just play with AI. **Output → Critique → Rewrite. Always.**

**Type:**

```
Now rewrite the Capability Statement using the business owner's
feedback above. Specifically:

- Strengthen or remove the 3 weakest claims you identified.
- Add the 2 missing pieces of evidence (use placeholders like
  [INSERT METRIC] if I haven't given you the number yet — I'll
  fill it in).
- Lead with the ONE thing the business owner said would make
  them pick up the phone.

Keep all my facts the same. Only change the framing, language,
and structure. Return the full revised Capability Statement.
```

**Send. Compare side-by-side with the first draft. Same agency, sharper presentation.**

---

## PART 4 — TURN IT INTO A REUSABLE GEM
**(1:30 – 1:55 | 25 minutes)**

We've built a great Capability Statement. Now we save the process that built it, so it's reusable forever. This is what makes it a Gem instead of a one-time chat.

---

### PROMPT 6 — THE GEM PACKAGER

**Why this prompt matters:** A Gem is just a saved set of instructions Gemini follows every time you open it. Right now, the instructions for building YOUR Capability Statement are scattered across 5 prompts. We're going to ask Gemini to bundle them into one clean instruction set we can paste into the Gem Builder.

**Type:**

```
Act as a master prompt engineer. Look at our entire conversation
above.

Write a single, comprehensive set of "Custom Instructions" for a
Google Gem called "Client Capability Architect."

The Gem's job: take any client brief, inbound inquiry, or prospect
profile I give it, and produce a tailored Capability Statement that
is optimized for that specific opportunity.

The instructions must:
- Use the 5-Part Framework (Role, Task, Context, Format,
  References)
- Embed everything you've learned about my agency in this
  conversation
- Always lead with how I solve the CLIENT'S problem, not how
  great my agency is
- Always include measurable client results
- Always surface my credentials and certifications prominently
- Always run a skeptical business owner critique BEFORE
  producing the final version
- Stay under 2 pages

Output: just the instructions, ready to paste into the Gem
Builder. No commentary, no labels, no preamble.
```

**Send. Copy the entire output. Don't read it yet — we'll save it first.**

---

### Build the Gem (8 minutes)

1. In Gemini's left sidebar, click **"Gems."**
2. Click **"New Gem"** (or the create button — Gemini's UI shifts).
3. Name it: **Client Capability Architect**
4. In the Instructions box, paste the entire output from Prompt 6.
5. Click **Save.**

If you don't save the Gem, none of this carries forward. Save it now.

---

### PROMPT 7 — THE TEST DRIVE

**Why this prompt matters:** A Gem you haven't tested is a Gem you don't trust. We're going to run it on something real to make sure it works. This also gives you your FINAL Capability Statement for the week.

**Open your new Gem in a fresh chat. Type:**

```
Generate my optimized Capability Statement now. Treat this as my
master baseline — the version I'll customize for every future
opportunity.

Run your built-in business owner critique first, then deliver
the final version. Show me the critique notes briefly so I can
see what you fixed.
```

**Send. This is your Capability Statement v1 — the one you save, the one we use in Week 2.**

---

## PART 5 — REFLECTION + SAVE YOUR WORK
**(1:55 – 2:00 | 5 minutes)**

### Save everything

Right now, before you forget:
1. Copy the final Capability Statement into a Google Doc. Title it: **Agency Capability Statement — v1**
2. Open the Prompt Library Template. Add today's Gem as your first entry.
3. Verify the Gem is saved in your Gemini sidebar.

If you skip this, you'll be rebuilding it next week.

### The pattern you just learned (memorize this)

**Interview → Answer → Draft → Critique → Rewrite → Package → Test.**

That's the loop. You used it once today. You'll use it every week from here. Every Gem you build for the rest of this program follows this same shape.

### Reflection question

Sit with this one. You don't have to answer out loud:

> What did the AI write about your agency that you've been thinking but never put into words?

### Homework before Session 1B

1. Read your final Capability Statement out loud one time at home. If anything sounds wrong, fix it directly in the Doc.
2. Identify ONE service category that best describes your primary offer. Google a few agencies that use that category on their websites. Write down how they describe themselves. Bring it.
3. Pull up one competitor agency's website. Just look around. Notice how they describe their services and who they target.

**See you on [day] at [time]. Bring your laptop charged.**

---

---

# SESSION 1B — VIRTUAL
## Review work before Session 1B

1. Read your final Capability Statement out loud one time at home. If anything sounds wrong, fix it directly in the Doc.
2. Identify ONE service category that best describes your primary offer. Google a few agencies that use that category on their websites. Write down how they describe themselves. Bring it.
3. Pull up one competitor agency's website. Just look around. Notice how they describe their services and who they target.

**Start off with a reflection question:**

Sit with this one. You don't have to answer out loud:

> What did the AI write about your agency that you've been thinking but never put into words?

---

## "Stress-Test Your Statement Until It's Client-Ready"

**Duration:** 90 minutes  **Tool:** Google Gemini (free version) + your Client Capability Architect Gem  
**Prompt Budget:** 7 prompts  **Outcome:** A service-category-locked, client-aligned, multi-perspective-reviewed, client-focused, keyword-optimized Capability Statement ready to drop into any pitch.

---

### THE FRAME (what you'll learn today)

Last session you learned the basic loop: Generate → Critique → Rewrite.

Today we go deeper. Today you learn three more advanced prompting skills:

1. **Persona stacking** — running the same critique through multiple expert lenses at once
2. **Frame shifting** — taking the same content and reframing it from a totally different angle (self-focused vs. client-focused is the big one)
3. **Collaborative prompting** — running prompts on someone else's work and letting them run prompts on yours

By the end you'll have a Capability Statement that's been pressure-tested from five different angles.

---

## PART 1 — WARMUP + WIN SHARING
**(0:00 – 0:15 | 15 minutes)**

### Drop in chat

In one word: how does your Capability Statement feel right now? Read a few aloud.

### Show the wins from Session 1A

I'll share 2-3 strong Capability Statements (with permission) on screen. As I show each one, I'll point out:
- One that nailed measurable client results
- One that nailed differentiation
- One that nailed client alignment

You'll see one of these strengths in your own statement. Today's job is to add ALL three.

### Today's prompt budget

Seven prompts. Same as last session. Here's the map so you know where we're going:

| Prompt | What it does |
|--------|-------------|
| 1 | Service Category Deep Match — find your best categories |
| 2 | Client Mission Alignment — pull a real client vertical's goal, align your statement to it |
| 3 | The Three-Persona Review — critique through 3 expert lenses simultaneously |
| 4 | The Client-Focused Rewrite — flip from "we" to "you" |
| 5 | Keyword Optimization — bake in client decision-making terms |
| 6 | The Partner Stress Test — pair work, you run a Gem on someone else's statement |
| 7 | The Lock-In — produce the final v3 baseline |

---

## PART 2 — SERVICE CATEGORIES + CLIENT ALIGNMENT
**(0:15 – 0:35 | 20 minutes)**

### Why service categories matter

Service categories are how clients and platforms describe what your agency does. Every inbound inquiry, every directory listing, every LinkedIn search uses these labels. If your Capability Statement doesn't speak the same language as the categories your clients are searching, you won't surface when they're looking.

**Drop in chat**

The service category you identified in your homework. Just the label. I'll validate live.

---

### PROMPT 1 — SERVICE CATEGORY DEEP MATCH

**Why this prompt matters:** You identified ONE category in your homework. Most agencies fit 2 to 4 categories, not just one. Missing the others means missing 50-75% of the opportunities you could be pitching. We're going to ask Gemini to look at your whole agency and find ALL the categories that fit.

**Open your Client Capability Architect Gem. Type:**

```
Look at my Capability Statement and look at the services I
described in our last conversation.

Find me 2-4 service categories that genuinely fit my agency. For
each category, give me:
- The category name (e.g. "Meta Advertising," "Paid Social,"
  "Lead Generation," "Full-Service Digital")
- One sentence on why it matches my agency
- Whether it's a "primary" or "secondary" category for me

Then update my Capability Statement to:
- Add a section called "Service Categories" listing all 2-4
- Use language from how clients in my niche actually describe
  what they're looking for in my Core Services section
- Keep my actual facts unchanged

Return the updated Capability Statement.
```

**Send. Read the new categories carefully. These are the labels you'll use on Clutch, LinkedIn, and in every pitch going forward.**

---

### PROMPT 2 — CLIENT MISSION ALIGNMENT

**Why this prompt matters:** Business owners care about ONE thing more than anything else: how you help them accomplish their goal. Most agencies lead with "we are a great agency." Winning agencies lead with "your business is trying to do X — here's how we help you do X."

We're going to pick ONE client vertical you want to target and align your statement to their actual business reality.

**Pick a client type. Examples:**
- Home service company — "Generate consistent, qualified leads during peak seasons so their crews stay booked"
- Med spa — "Build a steady stream of new patient bookings without relying on word-of-mouth alone"
- Local restaurant — "Drive consistent foot traffic and online orders without a massive marketing budget"
- Real estate agent — "Stay top-of-mind in their farm area so listings come to them before hitting the market"
- Roofing company — "Dominate their service area after every storm before competitors flood the market"

**Type:**

```
I want to target [CLIENT TYPE] for retainer clients. Their primary
business goal is [PASTE OR PARAPHRASE THEIR GOAL — 1-2 sentences].

Take my current Capability Statement and rewrite the Company
Overview paragraph and the Differentiators section so they
directly connect my services to this client type's goal.

The Company Overview should open by referencing what this client
type is trying to accomplish, then position my agency as a partner
in accomplishing it.

The Differentiators should explicitly tie each of my strengths
to a problem this client type cares about.

Do not change my Client Results, Credentials, or Service
Categories sections. Only the Overview and Differentiators.

Return the updated Capability Statement.
```

**Send. Notice the difference. Your statement no longer sounds like it's about you. It sounds like it's about how you help them.**

---

## PART 3 — THE THREE-PERSONA REVIEW
**(0:35 – 1:00 | 25 minutes)**

### Why we critique through multiple lenses

Last session, one persona (the skeptical business owner) reviewed your statement. That's good. But agency deals rarely get decided by one person. An owner cares about ROI. Their operations manager cares about whether you'll actually show up. Their CFO or spouse cares about whether this is a sound financial decision. Each one has different priorities.

We're going to run all three reviews at once.

---

### PROMPT 3 — THE THREE-PERSONA REVIEW

**Why this prompt matters:** This is persona stacking. You'll use this pattern any time you need 360-degree feedback fast. Real evaluation happens across multiple conversations — simulating the panel surfaces those gaps before you pitch.

**Type:**

```
Now critique my Capability Statement through THREE different
expert lenses at the same time. Give me each review separately.

PERSONA 1 — The Business Owner
You care about ROI, credibility, and proof that this agency has
done this before. What in this statement would make you skeptical
or score it lower? Name 3 specific issues.

PERSONA 2 — The CFO or Spouse (the financial decision-maker)
You care about whether this agency will deliver on time, on
budget, and without hidden costs or scope creep. What raises your
eyebrows in this statement? Name 3 specific concerns.

PERSONA 3 — The Operations Manager (the person who will actually
work with the agency day-to-day)
You care about whether this agency will make your life easier or
harder, whether they'll communicate well, deliver on time, and
handle problems without drama. What's missing from this statement
that would make you want to get on a call with them? Name 3
specific gaps.

For each persona, end with the ONE change you'd most want to see.
```

**Send. Read all three reviews carefully. You're about to see 9 issues — most of them you wouldn't have spotted alone.**

---

**Breakout rooms (10 minutes)**

Pairs. 10 minutes.
- Read your three-persona review to your partner.
- Compare: which persona gave the toughest feedback for YOU? Which gave the toughest feedback for THEM? Are they the same persona?
- Each person picks the TOP 2 issues to fix. Write them down.

When you come back, drop in chat: which persona was hardest on you?

---

## PART 4 — REFRAMING + KEYWORD OPTIMIZATION
**(1:00 – 1:25 | 25 minutes)**

### The biggest mistake in agency pitching

Most losing pitches start with "We are a results-driven agency with years of experience..." Most winning pitches start with "Home service companies in your market are leaving leads on the table every month because..."

Same agency. Same experience. Different frame. The first one talks about itself. The second one talks about the customer. **Client-focused beats self-focused 9 times out of 10.**

We're going to flip your statement.

---

### PROMPT 4 — THE CLIENT-FOCUSED REWRITE

**Why this prompt matters:** This is frame shifting. It's the same prompt skill as the persona work, but applied to YOUR voice instead of an external reviewer. You're rewriting from "we" to "you" without losing your facts or credibility.

**Type:**

```
Take my Capability Statement and apply the "client-focused vs.
self-focused" rewrite test.

For every sentence, ask: does this lead with what WE do, or
what the CLIENT needs?

Rewrite every self-focused sentence as client-focused.

Examples of the shift:

SELF-FOCUSED (losing): "We have 3 years of experience running
Meta campaigns for home service businesses."

CLIENT-FOCUSED (winning): "Home service companies need ad
campaigns that generate booked jobs — not just clicks. That's
what we've built our entire process around for 3 years."

Keep all my facts. Only change the framing direction.

Return the full rewritten Capability Statement. Add a brief note
at the end summarizing the top 3 framing shifts you made.
```

**Send. Read the new version carefully. The sentences should feel like they were written FOR a client, not about your agency.**

---

### PROMPT 5 — KEYWORD OPTIMIZATION

**Why this prompt matters:** Business owners and marketing directors searching for agencies — on Clutch, LinkedIn, or even Google — use specific language. Your Capability Statement needs to match how clients describe what they're looking for, not how agencies describe what they offer. We're going to bake the most common client-decision language into your statement now, so when you send a pitch or update your profile next week you start from a strong base.

**Type:**

```
Business owners evaluating marketing agencies use specific
language when deciding who to trust with their budget.

Take my current Capability Statement and rewrite it to naturally
incorporate the most relevant of these client-decision keywords
for my service area: lead generation, cost per lead, return on
ad spend, ROAS, conversion rate, qualified leads, booked
appointments, ad spend management, campaign optimization,
transparent reporting, consistent results, proven process,
dedicated account management, creative testing, audience
targeting, performance tracking, scalable campaigns.

Rules:
- Only use keywords that are TRUTHFUL for my agency. If I don't
  actually do dedicated account management, don't add it.
- Do not turn this into keyword stuffing. The statement must
  still read like a real agency.
- Show me which keywords you added and where, in a brief note
  at the end.

Return the final, optimized Capability Statement.
```

**Send. Save this output — it's the closest thing to a "final" version we'll have today.**

---

## PART 5 — PEER STRESS TEST + LOCK-IN
**(1:25 – 1:55 | 30 minutes)**

### Why peer stress-testing matters

You can critique your own work for hours and miss things. Another set of eyes — even another participant who's only one week in — sees what you miss. We're going to use AI to help.

---

### PROMPT 6 — THE PARTNER STRESS TEST

**Why this prompt matters:** This teaches collaborative prompting. You're going to run the business owner critique on someone ELSE'S Capability Statement, then they'll do the same to yours. Reading another person's AI feedback teaches you to read your own feedback better.

**In breakout rooms — pairs — 12 minutes total:**

1. Each person posts their current Capability Statement in the chat.
2. The partner copies it and runs THIS prompt in their own Gemini:

```
You are a skeptical business owner who runs a home service
company. You've been burned by agencies before who overpromised
and underdelivered.

Below is a Capability Statement from an agency owner I'm
mentoring. I want you to give them honest, useful feedback.

[PASTE PARTNER'S CAPABILITY STATEMENT HERE]

Tell them:
1. The single strongest sentence in this statement and why.
2. The single weakest sentence in this statement and why.
3. One specific addition that would make this 10x more
   convincing to a skeptical business owner.
4. One thing they should remove or shorten.

Be direct. Be specific. Pretend you actually want this agency
to win.
```

3. Send the AI's feedback back to your partner in chat.
4. Both of you read the feedback you received.
5. Quick verbal exchange: "Was the AI right? What are you actually going to fix?"

**Come back to main room (3 minutes)**

Drop in chat: ONE thing your partner's AI feedback caught that surprised you.

Read 3-4 aloud. Pattern usually emerges: the things AI catches in OTHER people's statements are often the same things it would catch in yours.

---

### PROMPT 7 — THE LOCK-IN

**Why this prompt matters:** You now have feedback from 5 different sources: the original business owner critique (Session 1A), the three-persona review, the client-focus reframe, the keyword optimization, and your partner's AI critique. Time to fold everything into one final master version.

**Type:**

```
This is the lock-in. Look at our entire conversation today plus
last session.

Produce the final, master version of my Capability Statement,
incorporating EVERY refinement we've made:
- Service categories integrated throughout (Prompt 1)
- Client mission alignment in the Overview and Differentiators
  (Prompt 2)
- Issues raised by all three personas resolved (Prompt 3)
- Client-focused framing throughout (Prompt 4)
- Client decision-making keywords baked in naturally (Prompt 5)
- Any specific feedback I shared from my partner's review
  (Prompt 6 — I'll paste it below if needed)

This is my master baseline. I will customize it for each
specific opportunity going forward, but THIS is the version I
build from every time.

Format: clean, two pages, ready to attach to a real pitch.
```

**Send. Save the output. This is your Capability Statement v3 — and it's the document Week 2 builds on.**

---

## PART 6 — REFLECTION + WEEK 2 SETUP
**(1:55 – 2:00 | 5 minutes)**

### What you actually learned today

Three new prompting skills, on top of last session's loop:

1. **Persona stacking** — multiple expert lenses in one prompt
2. **Frame shifting** — same facts, different angle (self-focused → client-focused)
3. **Collaborative prompting** — running prompts on someone else's work

You'll use all three in every Gem we build going forward.

### Save your work

1. Replace your old Google Doc with this new master version. Rename it: **Agency Capability Statement — MASTER v3**
2. In your Prompt Library, add the 7 prompts from today. Note which ones felt most useful.
3. Verify your Gem is still saved.

### Reflection question

> Two weeks ago, most of you wouldn't have known where to start with a Capability Statement. Right now, you have one that's been worked over by 14 different prompts across two sessions. What does it feel like to have something this sharp ready to go?

### Setup for Week 2

Next week we go from "I have a Capability Statement" to "I know where the clients are."

We'll build a Gem called the **Opportunity Scout**. It searches LinkedIn, Clutch, local business directories, and referral networks — and filters prospects down to the ones YOUR agency is actually qualified for, using the service categories we locked in today.

### Homework before Session 2A

1. Read your master Capability Statement out loud once. If anything sounds off, fix it directly in your Doc.
2. Go to Clutch.co. Find the category that fits your agency. Count how many agencies are listed. Bring that number.
3. Same exercise on LinkedIn. Search for businesses in your target vertical in your city. Just count how many are active. Bring that number.

**See you [day].**

---

---

# SIDEBAR 3: AGENCY BOTTLENECK BRAINSTORM WORKSHEET
## "Find the Pain That's Actually Costing You Retainers"

This worksheet is not a checklist. It is an interview with yourself.

The clearer and more uncomfortable you are with these answers, the better the Gems you build over the next 5 weeks will be. Generic answers here produce generic Gems that produce generic Capability Statements that get deleted after one sentence.

A few ground rules before you start:

Nobody is reading this but you. There is no right answer. If you find yourself writing "I just need to be more organized" or "I need more time" — scratch it. Those are not bottlenecks. Those are excuses we all use. Dig until you find the specific moment, the specific email you never sent, the specific prospect that ghosted you and why.

---

## STEP 1: AUDIT YOUR ACTUAL CLIENT ACQUISITION BEHAVIOR

Answer each question in **complete sentences**, not bullet points. The act of writing the sentence is where the insight lives.

### 1. Discovery — Where are you not looking, and why?

Most agency owners say they "don't have time" to find new clients. That is rarely the real answer.

Walk me through the last time you sat down to actively look for a new client opportunity. When was it? Where did you look? How long did you spend before you closed the tab?

Now the harder question: which platforms or client types have you been *avoiding* — not because you don't know about them, but because something about them intimidates you or feels out of reach? (Cold outreach? LinkedIn DMs? Reaching out to bigger businesses? A specific industry that intimidates you?)

What story have you been telling yourself about why those opportunities are not for you?

**Write your answer here:**

---

### 2. Qualification — What do you do in the first 10 minutes after receiving an inbound inquiry?

Be honest about your actual behavior, not what a "good agency owner" would do.

When an inbound inquiry lands in your inbox, what is the first thing you do? Do you reply immediately? Do you let it sit? Do you look up their business before responding? Do you check their ad account or social media?

What is the thing you keep meaning to do before a sales call but somehow never do until it's too late? (For most agency owners, it is one of these: researching the prospect's current ads, reviewing their reviews and reputation, understanding their peak season, or qualifying their budget range.)

Think about the last prospect you decided not to pursue or who fell off after an initial call. What was the real reason — not the reason you told yourself, but the real one?

**Write your answer here:**

---

### 3. Pitching — Where does the proposal die on your desk?

Every lost deal dies somewhere specific. Most of the time it is the same spot every time.

Pull up the last proposal you wrote — even if you sent it. Which section took you the longest? Which section did you write last, in a panic, the night before you needed to send it? Which section, if you are honest, was mostly recycled from a previous proposal without really being rewritten for this client?

What is the section that you secretly believe is weak, but you send anyway because you have run out of time? (For most agency owners, it is either the Pricing & ROI section, the Case Studies section, or the Process section.)

If a client told you, "Your pitch lost on one specific thing," which thing would you bet they meant?

**Write your answer here:**

---

### 4. Follow-Up — Have you ever lost a deal on a process failure, and what really happened?

This is the question most agency owners skip. Don't.

Have you ever sent a proposal and then gone silent? Followed up once and never heard back and never followed up again? Scheduled a second call and let it fall off the calendar? If yes — what was it? Got busy? Assumed they weren't interested? Didn't want to seem desperate?

What is your current follow-up routine? Walk me through it from the moment you send a proposal to the moment you either close or move on. Where in that timeline does the deal die?

**Write your answer here:**

---

### 5. Tracking and Learning — What do you actually know about why you win and lose?

Pull up your pitch history for the last 12 months. (If you don't have one written down, that itself is the answer to this question.)

How many proposals did you send? How many did you win? Of the ones you lost — how many did you follow up with to ask why? How many actually told you?

Here is the harder version: when you lose a deal, what is the story you tell yourself about why? "They went with a cheaper agency." "They weren't serious." "Timing wasn't right." Are those stories actually true, or are they the comfortable story you tell so you don't have to look at the proposal again?

What is the *pattern* across your losses? Same client type? Same deal size? Same objection?

**Write your answer here:**

---

## STEP 2: MAP YOUR BOTTLENECKS TO THE GEMS YOU'LL BUILD

Each Gem in this program is built to dissolve a specific kind of bottleneck. As you read the table, circle or highlight the row that hurts the most for your business.

| Client Stage | The Bottleneck It Solves | The Gem | Week Built |
|-------------|--------------------------|---------|-----------|
| Discovery | "I'm avoiding channels or client types that feel out of reach" | Opportunity Scout | Week 2 |
| Discovery | "I find too many potential clients and freeze" | Opportunity Scout (filter mode) | Week 2 |
| Qualification | "I pitch clients I can't win and waste 10 hours" | Prospect Qualifier | Week 3 |
| Qualification | "I can't read between the lines of what a client actually wants" | Client Intelligence Profile | Week 3 |
| Pitching | "I freeze on the blank page" | Proposal Architect | Week 4 |
| Pitching | "My pitch looks amateur next to bigger agencies" | Brand Credibility Pack | Week 4 |
| Pitching | "I can't compete with agencies who have 20-person teams" | Video Capability Statement | Week 4 |
| Follow-Up | "I lose deals I should close because my follow-up is inconsistent" | Outreach Checklist Agent | Week 5 |
| Scaling | "Only I know how to do any of this" | Train-the-Team workflow | Week 5 |

---

## STEP 3: PUT A REAL DOLLAR FIGURE ON THE PAIN

Vague pain doesn't get fixed. Quantified pain does.

Fill in this table with **specific numbers from your actual business in the last 12 months**. If you don't know the number, write your best guess and circle it — that "I don't know" is itself a bottleneck.

| Your Specific Bottleneck | How Often It Happens | Time Lost Each Time | Dollars Lost (real or opportunity cost) | Priority 1–10 |
|--------------------------|---------------------|---------------------|----------------------------------------|--------------|
| *Example: Spent 15 hrs on a pitch I couldn't win* | *Monthly* | *15 hrs* | *$1,500 in time + $3K/mo retainer I could have won instead* | *10* |
| *Example: Prospect ghosted after proposal — no follow-up* | *Twice last quarter* | *8 hrs* | *$5K/mo retainer gone* | *9* |

Now add up the right column. That is what *not* solving these bottlenecks cost you last year.

**Write the total here: $_______________**

If that number doesn't make you uncomfortable, you didn't fill it out honestly. Go back.

---

## STEP 4: TURN YOUR BOTTLENECK INTO YOUR DIFFERENTIATOR

This is the move most agency owners never make. Pain that you have already overcome is your most credible selling point.

Look back at the bottleneck you marked as your highest priority. Now answer:

What did you have to learn, change, or systematize because of that pain? What process do you now have in place that someone who hasn't been burned the same way wouldn't have? How could that hard-won lesson become a line in your Capability Statement that no competitor could honestly write?

**The formula:**

> "I got burned by [specific failure]. So I built [specific system or habit]. Now I [specific result with a number or timeframe]. Clients need agencies who [the standard your pain forced you to set]."

**Write your version here:**

*My differentiator born from pain:*

Compare the two examples below. Then look at what you wrote.

**Generic answer (don't do this):** "We have great client communication and care about results."

**Bottleneck-as-differentiator (do this):** "I lost two clients in 2023 because I couldn't produce ad creative fast enough to test during their peak season. That pain made me build a 10-agent AI production system that creates full ad concepts in 48 hours instead of two weeks. I have not missed a creative deadline in 18 months across 12 active clients. Businesses need agencies who keep pace with their seasons, not ones who slow them down."

The second one wins because it has a date, a number, a process, and a stake. It cannot be copy-pasted from anyone else's website.

---

## STEP 5: WRITE YOUR ONE-SENTENCE WHY

Finish this sentence in one breath, no clauses, no qualifiers.

> "By the end of this 5-week program, the one bottleneck I want gone forever is _________________________ because right now it costs me _________________________ every _________________________."

**Write it here, in your own words:**

**My Why:**

Tape this to your monitor. Bring it to every session. When you get tired in Week 3 or skeptical in Week 4, this is the sentence that pulls you back.

---

## STEP 6: BRING THIS WORKSHEET TO SESSION 1

When you sit down with your Gem in Session 1A and it asks you to describe your agency, do not paste in your website's About page.

Paste in the answers from this worksheet.

The Gem will produce a Capability Statement that sounds like a real human who has been in the trenches — because you just told it the truth about the trenches. That is the difference between a statement that gets a response and a statement that gets archived.

**One last thing.**

If you finish this worksheet and feel slightly exposed, you did it right. The discomfort is the signal that you finally wrote down what you have been carrying around in your head for years. Now we can build systems that solve it.

See you in Session 1.

---

---

# ALL 14 WEEK 1 PROMPTS — COPY-PASTE READY
## "Week 1 Prompt Pack"

Every prompt for Sessions 1A and 1B in one place. Bookmark this tab. You'll come back to it during the live session.

---

## SESSION 1A — IN-PERSON
### "Build Your Client Capability Architect"

---

### PROMPT 1A.1 — THE INTERVIEW STARTER

```
You are an expert in marketing agency positioning and client
acquisition, with deep experience in helping small agencies win
retainer clients across industries including home services, local
business, e-commerce, and professional services.

I am a marketing agency owner. I want to build a professional
Capability Statement — the foundation document I'll use for every
retainer pitch and inbound response.

Before you write anything, INTERVIEW ME. Ask me exactly 7
questions, one message, all at once, that will give you the
information you need to write a competitive Capability Statement.

Focus your questions on what business owners actually evaluate:
- Service categories and core offer
- Client results with measurable outcomes (the "Gold Nuggets")
- Credentials I have or am eligible for (Meta Partner, Google
  Partner, HubSpot, platform certs, industry associations)
- Target client types and retainer range
- Capacity (team size, contractor network, client load)
- Genuine differentiators
- Any referral partnerships or white-label relationships

Do not write the Capability Statement yet. Just the 7 questions.
```

---

### PROMPT 1A.2 — THE ANSWER DUMP

```
Here are my answers to all 7 questions:

1. [YOUR ANSWER]
2. [YOUR ANSWER]
3. [YOUR ANSWER]
4. [YOUR ANSWER]
5. [YOUR ANSWER]
6. [YOUR ANSWER]
7. [YOUR ANSWER]

Confirm you have what you need. If you have any clarifying
questions, ask them now in the same message before we move
forward.
```

---

### PROMPT 1A.3 — THE FIRST DRAFT

```
Now write my Capability Statement.

Format it as a clean, two-page document with these sections:
- Company Overview (one paragraph)
- Core Services (bulleted, with service categories alongside)
- Client Results (2-3 highlights with measurable outcomes)
- Credentials and Certifications
- Target Clients and Service Area
- Differentiators (what makes me different, in plain language)
- Contact Information (placeholder)

Tone: professional but human. No corporate buzzwords. No
"transformative" or "innovative." Real language a business owner
would respect.
```

---

### PROMPT 1A.4 — THE SKEPTICAL BUSINESS OWNER CRITIQUE

```
Now act as a skeptical, experienced business owner who runs a
$2M/year home service company. You've evaluated pitches from 500
marketing agencies this year. You've seen every kind of fluff
and exaggeration.

Read the Capability Statement you just wrote. Tell me:

1. The 3 weakest claims — places where the language sounds
   generic or unsupported.
2. The 2 most critical pieces of evidence that are missing —
   things I should add to be more credible.
3. The 1 thing in this statement that would actually make you
   pick up the phone and call this agency.

Be direct. Don't soften the feedback. Treat me like an agency
owner you want to help, not a friend you don't want to hurt.
```

---

### PROMPT 1A.5 — THE REWRITE

```
Now rewrite the Capability Statement using the business owner's
feedback above. Specifically:

- Strengthen or remove the 3 weakest claims you identified.
- Add the 2 missing pieces of evidence (use placeholders like
  [INSERT METRIC] if I haven't given you the number yet — I'll
  fill it in).
- Lead with the ONE thing the business owner said would make
  them pick up the phone.

Keep all my facts the same. Only change the framing, language,
and structure. Return the full revised Capability Statement.
```

---

### PROMPT 1A.6 — THE GEM PACKAGER

```
Act as a master prompt engineer. Look at our entire conversation
above.

Write a single, comprehensive set of "Custom Instructions" for a
Google Gem called "Client Capability Architect."

The Gem's job: take any client brief, inbound inquiry, or
prospect profile I give it, and produce a tailored Capability
Statement that is optimized for that specific opportunity.

The instructions must:
- Use the 5-Part Framework (Role, Task, Context, Format,
  References)
- Embed everything you've learned about my agency in this
  conversation
- Always lead with how I solve the CLIENT'S problem, not how
  great my agency is
- Always include measurable client results
- Always surface my credentials and certifications prominently
- Always run a skeptical business owner critique BEFORE
  producing the final version
- Stay under 2 pages

Output: just the instructions, ready to paste into the Gem
Builder. No commentary, no labels, no preamble.
```

---

### PROMPT 1A.7 — THE TEST DRIVE
*(Run this INSIDE your new Gem after saving it)*

```
Generate my optimized Capability Statement now. Treat this as my
master baseline — the version I'll customize for every future
opportunity.

Run your built-in business owner critique first, then deliver
the final version. Show me the critique notes briefly so I can
see what you fixed.
```

---

## SESSION 1B — VIRTUAL
### "Stress-Test Your Statement Until It's Client-Ready"

---

### PROMPT 1B.1 — SERVICE CATEGORY DEEP MATCH

```
Look at my Capability Statement and look at the services I
described in our last conversation.

Find me 2-4 service categories that genuinely fit my agency. For
each category, give me:
- The category name
- One sentence on why it matches my agency
- Whether it's a "primary" or "secondary" category for me

Then update my Capability Statement to:
- Add a section called "Service Categories" listing all 2-4
- Use language from how clients in my niche actually describe
  what they're searching for in my Core Services section
- Keep my actual facts unchanged

Return the updated Capability Statement.
```

---

### PROMPT 1B.2 — CLIENT MISSION ALIGNMENT

```
I want to target [CLIENT TYPE] for retainer clients. Their
primary business goal is [PASTE OR PARAPHRASE THEIR GOAL — 1-2
sentences].

Take my current Capability Statement and rewrite the Company
Overview paragraph and the Differentiators section so they
directly connect my services to this client type's goal.

The Company Overview should open by referencing what this client
type is trying to accomplish, then position my agency as a
partner in accomplishing it.

The Differentiators should explicitly tie each of my strengths
to a problem this client type cares about.

Do not change my Client Results, Credentials, or Service
Categories sections. Only the Overview and Differentiators.

Return the updated Capability Statement.
```

---

### PROMPT 1B.3 — THE THREE-PERSONA REVIEW

```
Now critique my Capability Statement through THREE different
expert lenses at the same time. Give me each review separately.

PERSONA 1 — The Business Owner
You care about ROI, credibility, and proof that this agency has
done this before. What in this statement would make you skeptical
or score it lower? Name 3 specific issues.

PERSONA 2 — The CFO or Spouse (the financial decision-maker)
You care about whether this agency will deliver on time, on
budget, and without hidden costs or scope creep. What raises your
eyebrows in this statement? Name 3 specific concerns.

PERSONA 3 — The Operations Manager (the person who will actually
work with the agency day-to-day)
You care about whether this agency will make your life easier or
harder, whether they'll communicate well, deliver on time, and
handle problems without drama. What's missing from this statement
that would make you want to get on a call with them? Name 3
specific gaps.

For each persona, end with the ONE change you'd most want to see.
```

---

### PROMPT 1B.4 — THE CLIENT-FOCUSED REWRITE

```
Take my Capability Statement and apply the "client-focused vs.
self-focused" rewrite test.

For every sentence, ask: does this lead with what WE do, or
what the CLIENT needs?

Rewrite every self-focused sentence as client-focused.

Examples of the shift:

SELF-FOCUSED (losing): "We have 3 years of experience running
Meta campaigns for home service businesses."

CLIENT-FOCUSED (winning): "Home service companies need ad
campaigns that generate booked jobs — not just clicks. That's
what we've built our entire process around for 3 years."

Keep all my facts. Only change the framing direction.

Return the full rewritten Capability Statement. Add a brief note
at the end summarizing the top 3 framing shifts you made.
```

---

### PROMPT 1B.5 — KEYWORD OPTIMIZATION

```
Business owners evaluating marketing agencies use specific
language when deciding who to trust with their budget.

Take my current Capability Statement and rewrite it to naturally
incorporate the most relevant of these client-decision keywords
for my service area: lead generation, cost per lead, return on
ad spend, ROAS, conversion rate, qualified leads, booked
appointments, ad spend management, campaign optimization,
transparent reporting, consistent results, proven process,
dedicated account management, creative testing, audience
targeting, performance tracking, scalable campaigns.

Rules:
- Only use keywords that are TRUTHFUL for my agency. If I don't
  actually do dedicated account management, don't add it.
- Do not turn this into keyword stuffing. The statement must
  still read like a real agency.
- Show me which keywords you added and where, in a brief note
  at the end.

Return the final, optimized Capability Statement.
```

---

### PROMPT 1B.6 — THE PARTNER STRESS TEST
*(Run this on YOUR PARTNER'S Capability Statement, not your own)*

```
You are a skeptical business owner who runs a home service
company. You've been burned by agencies before who overpromised
and underdelivered.

Below is a Capability Statement from an agency owner I'm
mentoring. I want you to give them honest, useful feedback.

[PASTE PARTNER'S CAPABILITY STATEMENT HERE]

Tell them:
1. The single strongest sentence in this statement and why.
2. The single weakest sentence in this statement and why.
3. One specific addition that would make this 10x more
   convincing to a skeptical business owner.
4. One thing they should remove or shorten.

Be direct. Be specific. Pretend you actually want this agency
to win.
```

---

### PROMPT 1B.7 — THE LOCK-IN

```
This is the lock-in. Look at our entire conversation today plus
last session.

Produce the final, master version of my Capability Statement,
incorporating EVERY refinement we've made:
- Service categories integrated throughout (Prompt 1)
- Client mission alignment in the Overview and Differentiators
  (Prompt 2)
- Issues raised by all three personas resolved (Prompt 3)
- Client-focused framing throughout (Prompt 4)
- Client decision-making keywords baked in naturally (Prompt 5)
- Any specific feedback I shared from my partner's review
  (Prompt 6 — I'll paste it below if needed)

This is my master baseline. I will customize it for each
specific opportunity going forward, but THIS is the version I
build from every time.

Format: clean, two pages, ready to attach to a real pitch.
```

---

---

# BOTTLENECK BRAINSTORM — SESSION 2A
## "Map the Retainers You've Been Telling Yourself Aren't For You"

This worksheet is not about finding clients. You can find clients in 30 seconds on Google.

This worksheet is about finding the retainers your brain has been quietly skipping past for the last two years. The $10K/month accounts. The agencies in verticals you assume are "too sophisticated" for you. The inbound RFP platforms you've never opened. The Black-owned business directories you didn't know existed. Every agency owner has a private list of opportunities they've been treating as "not for me."

That list is your real bottleneck. Not the search itself.

A few ground rules before you start:

Nobody is reading this but you. Write in complete sentences, not bullets. The sentence is where the insight lives. If you find yourself writing "I just need to be more disciplined about prospecting" — scratch it. That is not a bottleneck. That is the comfortable story. Dig until you find the specific platform you opened, looked at, and closed without reading.

---

## STEP 1: AUDIT YOUR ACTUAL DISCOVERY BEHAVIOR

### 1. Walk me through your last hour of prospecting.

Most agency owners say they "don't have time" to look for new clients. The truth is usually that they have looked, recently, and what they saw made them quietly close the tab.

When was the last time you actually opened a prospecting platform? Not "checked email" — actually went to Clutch, LinkedIn Sales Navigator, UpCity, an industry Facebook group, or anywhere else. What date was it? What platform? How long did you spend before you closed it?

What was the specific feeling that made you stop? Overwhelm? Confusion about what you were looking at? A profile that made you feel small? Boredom because nothing seemed to fit? The sense that everyone else has been doing this longer than you?

**Write your answer here:**

---

### 2. Name the platforms and channels you've been avoiding, and tell me why.

This is the one that matters most.

Look at this list:

- **Clutch.co** — the largest agency directory on the internet
- **LinkedIn Sales Navigator** — direct B2B outreach platform
- **UpCity** — small business agency directory
- **Agency Spotter** — vetted-agency directory used by enterprise buyers
- **Inbound RFP platforms** — RFPIO, Loopio, PandaDoc — businesses post their marketing RFPs here
- **Industry trade associations** — NARI (remodeling), ACCA (HVAC), NRCA (roofing), RIA (restoration), IICRC
- **Local networking** — BNI, Chamber of Commerce, Rotary
- **Industry Facebook groups** — home service business owner communities, contractor masterminds
- **Strategic partner referrals** — bookkeepers, accountants, web developers, business coaches who serve your same vertical
- **Podcasts and trade publications** in your vertical
- **Inbound RFPs from school districts, municipalities, and local non-profits** — the "small government" marketing/communications work
- **Black-owned / minority-owned / veteran-owned business directories** — most agency owners eligible never apply

Which of these have you registered for? Which have you visited more than twice? Which do you know exists but have never opened?

Now the harder question: of the ones you have NOT been visiting, which one have you been *actively avoiding* — not "haven't gotten to" — actively avoiding. The one where every time you think about it, your gut tells you "that's not for me yet."

What is the story you have been telling yourself about why that channel is not for you? ("LinkedIn outreach is sleazy." "Clutch is saturated and only big agencies show up." "I need a 5-year track record before I post on Agency Spotter." "RFP platforms are for big firms with proposal teams." "I'm not a real Black-owned business — I'm just a Black guy with a business.")

**Write your answer here:**

---

### 3. What's the retainer size that scares you at the high end?

Every agency owner has a number. Above that number, the engagement feels too big, too risky, too much to deliver. Below that number, you feel comfortable pitching.

What is your number?

Now: when was the last time you actually pitched a client at 2x or 3x bigger than your "comfort ceiling"? What did you tell yourself when you closed the conversation?

The honest answer is usually some version of: "I'd never be able to deliver that" or "they'd never pick me" or "I'd need a team of 20 to do that." Which version is your version?

**Write your answer here:**

---

### 4. What kind of client feels "not for me" even though it technically fits your services?

Med spas hire ad agencies for compliance-heavy creative — not just bigger agencies that specialize in healthcare. Real estate brokerages hire content agencies for community marketing — not just real estate marketing firms. Law firms hire SEO and content agencies — not just legal-only marketing companies. SaaS companies in growth stage hire performance agencies that are vertical-flexible, not just SaaS-specialist firms.

But most agency owners self-filter. They look at a med spa and think "I'm not a healthcare agency." They look at a SaaS company and think "I don't speak SaaS." They look at a $20M home service company and think "they need a real agency, not me." They miss the half of every vertical that needs *exactly* what they offer — generalist paid ads + automation + content with a vertical-relevant lens.

Which industry or client size have you been writing off because of what you assume they buy, without checking what they actually need?

**Write your answer here:**

---

### 5. What certification, partnership, or directory do you assume you don't qualify for?

Most small marketing agencies in San Diego qualify for at least 3 of these and only know about 1: Meta Business Partner, Google Partner, HubSpot Partner, TikTok for Business, the State of California Small Business Enterprise (SBE) certification, the SBA's 8(a) program (if minority-owned), Black-owned business directories like ByBlack and US Black Chambers, women-owned business directories like WBENC, veteran-owned (VOSB), Buy SD's local preference programs.

Which certifications and partnerships do you currently hold? Which have you been meaning to apply for but haven't? Which have you assumed you don't qualify for without ever actually checking the eligibility requirements?

What is the cost to your business each year of not having those certifications? (5% bid preferences on local-government marketing contracts. Set-aside-only contract pools you're locked out of. Pass-through retainers from prime agencies that need to hit MWBE participation goals on enterprise accounts and can't find vendors. Inbound leads from each platform's partner directory.)

**Write your answer here:**

---

## STEP 2: MAP YOUR AVOIDANCE PATTERNS TO YOUR SCOUT CONFIGURATION

In Session 2A you are going to build a Gem called the **Opportunity Scout.** The Scout is only as smart as the configuration you give it.

If you tell the Scout "I'm not interested in inbound RFPs" because RFPs scare you, the Scout will never surface RFP platform opportunities, even the ones you'd win. If you tell the Scout your retainer ceiling is $3K because $5K feels too big, the Scout will filter out the $4K opportunities that are perfect for you.

The Scout will configure itself around your fears unless you make those fears visible.

Use this table to translate the avoidance patterns from Step 1 into Scout configuration decisions:

| Your Avoidance Pattern from Step 1 | What to Tell the Scout | What NOT to Tell the Scout |
|---|---|---|
| *Example: I avoid LinkedIn outreach because it feels sleazy* | Surface LinkedIn-sourced opportunities anyway, flag warm-intro paths first so I can ramp into cold outreach | "Filter out all LinkedIn" |
| *Example: I'm scared of retainers over $5K* | Include opportunities up to $8K, but flag them as "stretch" so I can review carefully | "Cap everything at $5K" |
| *Example: I assume I don't qualify for ByBlack / minority directories* | Surface directory-listed opportunities anyway, so I can see what I'm missing while I get listed | "Skip Black-owned-only contracts" |
| *Example: I avoid med spa clients because compliance feels scary* | Include med spa opportunities but flag them with the compliance check I'd need to pass | "Filter out healthcare/wellness" |
| *Example: I avoid school district / local government RFPs* | Include local-government communications RFPs flagged as "explore" so I can see what's there | "Filter out government work" |

The pattern: the Scout should know what scares you so it can show you those opportunities **with context**, not so it can hide them from you.

---

## STEP 3: PUT A REAL DOLLAR FIGURE ON YOUR AVOIDANCE

Every avoided platform, every imagined size ceiling, every uncertified status has a real dollar cost. We're going to put a number on it.

| Avoidance Pattern | How long you've been avoiding it | Estimated retainer value you've missed each year | Total cost over the avoidance period |
|---|---|---|---|
| *Example: Never registered on Clutch* | 2 years | At least one $3K/mo retainer = $36K/yr | $72,000 |
| *Example: Skipped LinkedIn outreach* | 3 years | One $2K/mo retainer per quarter = $24K/yr first signed, ~$60K cumulative LTV | $180,000 |
| *Example: Never applied to ByBlack directory* | 1 year | One $4K/mo retainer = $48K/yr | $48,000 |

Add up the right column.

This is what your avoidance has cost you to date: **$_______________**

If that number doesn't make you uncomfortable, you didn't fill it out honestly. The point of this number is not to make you feel bad. It's to make sure you take the Avoidance Audit prompt seriously when you build the Scout in Session 2A.

---

## STEP 4: TURN AN AVOIDANCE INTO A POSITIONING THESIS

Pick the avoidance pattern that costs you the most.

Now we flip it.

Most agency owners who finally pursue an opportunity in their avoidance category discover something interesting: the prospect was actively looking for vendors like them, and the absence of vendors like them was the prospect's biggest problem. Your avoidance was the gap. Filling it is your positioning.

**The formula:**

> "I have been avoiding [specific platform or category] because [honest story you've been telling yourself]. But the businesses in that category are actively looking for [your business type] because [real reason businesses need you]. My avoidance has been their problem. The first three opportunities I should evaluate in this category are [best fits from Deep Research]."

**Write your version here:**

*My positioning thesis born from avoidance:*

Compare these two examples. Then look at what you wrote.

**Generic answer (don't do this):** "I'm going to start using LinkedIn."

**Avoidance-as-thesis answer (do this):** "I have been avoiding LinkedIn outreach for 2 years because cold messaging felt sleazy. But home service business owners who hire agencies on LinkedIn are specifically looking for vendors who DM them with a video walkthrough of their existing ad account — they hate generic pitches as much as I do. Black-owned agencies in the Meta ads space are actively recruited because Meta's diversity partner program directs leads from enterprise clients to certified small agencies that have ByBlack listings. The first three opportunities I should evaluate are the local roofing companies that posted "looking for a Meta agency" on LinkedIn in the last 30 days, the ByBlack directory inbound leads, and Meta's Small Business Diversity Partner program."

The second one wins because it has a specific platform, a specific reason your fear was wrong, and three specific next moves. It is not a goal. It is a strategy.

---

## STEP 5: WRITE YOUR ONE-SENTENCE WHY FOR THE SCOUT

Finish this sentence in one breath.

> "By the end of Session 2A, the one avoidance pattern I want my Opportunity Scout to break is _________________________ because pursuing those opportunities would mean _________________________ for my business in the next 90 days."

**Write it here:**

**My Why for the Scout:**

When the Scout asks you the Avoidance Audit questions in Prompt 1, your answers should sound like this sentence. Not vague. Specific.

---

## STEP 6: BRING THIS WORKSHEET TO SESSION 2A

In Session 2A, the very first prompt you run is the **Avoidance Audit** — Gemini will ask you 5 questions about what you've been avoiding.

**Do not answer those questions cold.**

Bring this worksheet. When Gemini asks "Which prospecting platforms or client types have you been avoiding, and what's the real reason?" — paste in your answer from Step 1, Question 2.

When Gemini asks "What retainer size scares you at the high end?" — paste in your answer from Question 3.

The Scout you build will be configured around real avoidance patterns instead of the polite version you would have given on the spot. That is the difference between a Scout that surfaces the same comfortable opportunities you've been finding on your own and a Scout that surfaces the retainers you've been quietly walking past.

**One last thing.**

The Avoidance Audit is the single most important prompt you will run in Week 2. Most participants soften their answers because they are slightly embarrassed to admit what they have been skipping. Don't do that.

The story you have been telling yourself about why a platform isn't for you is almost always wrong, and the cost of that wrong story is measured in retainers you never even saw.

See you in Session 2A.

---

---

# SESSION 2A — IN-PERSON
## "Build the Opportunity Scout"

**Duration:** 1 hour 45 minutes  **Tool:** Google Gemini (free version) + Gemini Deep Research  
**Prompt Budget:** 8 prompts  
**Outcome:** A working Gem called the Opportunity Scout, plus a sourced shortlist of 3 real San Diego-area retainer opportunities you are actually qualified to pursue.

---

### THE FRAME (what you'll learn today)

Last week you built a Capability Statement that says clearly who you are and what you do.

This week we answer the next question: **where are the retainers that match it?**

Most agency owners are not bad at writing pitches. They're bad at finding the right opportunities to pitch on. They check Clutch once a month, get overwhelmed, close the tab, and pitch on whatever lead crosses their desk that week. That's how you end up spending 40 hours on a pitch you were never going to win.

Today we fix that. You're going to build a Gem called the **Opportunity Scout** that knows your business as well as you do, and you're going to point it at the real opportunities being published in San Diego right now. You'll also learn the most important new tool in the program: **Gemini Deep Research.**

The new prompting skill today is **multi-source synthesis** — letting the AI scan many sources at once and report back with patterns, not just hits.

Watch the pattern. Same loop as last week, new fuel.

---

## PART 1 — INTRODUCTION + WHERE RETAINERS LIVE
**(0:00 – 0:20 | 20 minutes)**

### Where retainer opportunities actually get published

Retainer-ready clients don't show up on Indeed. They live across a handful of platforms — and most small agencies only know about one or two of them.

In San Diego, your real hunting ground is:

- **Clutch.co** — the largest agency review and directory site; clients use it to shortlist agencies
- **LinkedIn Sales Navigator** — direct B2B outreach + tracking when companies post they're looking for an agency
- **UpCity** — small business agency directory
- **Agency Spotter** — vetted-agency directory for mid-market and enterprise buyers
- **Inbound RFP platforms** — RFPIO, Loopio, PandaDoc, Bidsketch, Proposify (clients post marketing RFPs)
- **Industry trade associations** — NARI, ACCA, NRCA, RIA, IICRC, NAHB local chapters
- **Industry Facebook + Slack groups** — home service business owner communities
- **Strategic partner networks** — bookkeepers, web developers, accountants, business coaches in your vertical
- **School districts / local government** — small marketing & communications RFPs, especially for grant-funded community programs
- **Have Gemini help you find directories and RFP boards** specific to your niche!

Each one publishes opportunities differently. Each one has different keyword conventions. Each one has different vendor preferences.

The mistake most agencies make is checking ONE platform occasionally. Winners check **multiple platforms consistently** — and they track signal sources that show what's coming **3 to 6 months before a business posts the formal RFP** (LinkedIn complaint posts about their current agency, founder podcast appearances mentioning marketing pain, expiring agency contracts visible in 10-K filings or press releases).

We're going to build a system that does both at once.

### What "Deep Research" actually is

Last week, every prompt was a single back-and-forth with Gemini.

Today we use a different mode: **Gemini Deep Research.** Instead of one search and one answer, Deep Research runs a **multi-step investigation** — it builds a research plan, scans dozens of pages across the open web, verifies findings across sources, and returns a sourced report with links.

This is the tool that elite agency biz dev teams pay $5,000 a month for under names like "capture intelligence" or "ABM platforms." You're getting it free.

When you click the Deep Research button in Gemini, expect it to take 5 to 10 minutes per run. It is not chatting with you in real time — it is working. Use that time to answer questions on this handout while it runs.

### About today's prompt budget

Eight prompts today. Every one earns its place.

| Prompt | What it does |
|--------|-------------|
| 1 | Avoidance Audit — surface the platforms you've been quietly skipping |
| 2 | Opportunity Scout Configuration — tell Gemini who your Scout is |
| 3 | Deep Research Brief — the multi-source scan |
| 4 | Match-Reasoning Audit — Gemini explains every match decision |
| 5 | The Avoidance Lens — re-scan with your blocked categories included |
| 6 | The Shortlist Filter — Scout picks your top 3 |
| 7 | The Gem Packager — bundle the Scout into a saved Gem |
| 8 | The Test Drive — run your saved Scout on a fresh opportunity |

Same loop as last week. New fuel.

---

## PART 2 — CONFIGURE YOUR SCOUT
**(0:20 – 0:50 | 30 minutes)**

### Get into Gemini

Open **gemini.google.com**. Pull up your **Client Capability Architect Gem** from last week — you'll need it open in another tab.

If your Capability Statement v1 is in a Google Doc, open that too. We're going to copy from it.

---

### PROMPT 1 — THE AVOIDANCE AUDIT

**Why this prompt matters:** Before we configure the Scout, we need to know what you've been quietly avoiding. Most agencies don't have a discovery problem. They have an avoidance problem. They skip LinkedIn outreach because cold DMs feel sleazy. They skip Clutch because they assume only big agencies show up. They skip anything over $5K/month because it feels too big.

The Scout needs to know your real fears. Otherwise it will configure itself around opportunities you'd never actually pursue.

**Open your Client Capability Architect Gem (the one you built last week). Type:**

```
You know my business from our last conversation (or my
Capability Statement). Now I want you to interview me
about my AVOIDANCE PATTERNS — the opportunities I have
been quietly skipping.

Ask me 5 questions, all in one message. Push me. Do not
let me say "I don't avoid anything" — every agency owner
does.

Cover at minimum:
1. Which prospecting platforms or client channels have I
   been avoiding, and what's the real reason?
2. What retainer size scares me at the high end? Be
   specific.
3. What kind of client feels "not for me" even though it
   technically fits my services?
4. What certification, partnership, or directory do I
   always assume I don't qualify for, without checking?
5. What do I tell myself about why I haven't pursued more
   inbound RFP work or larger enterprise clients?

Do not write the audit yet. Just the 5 questions.
```

**Send. Read the questions. Don't answer yet.**

---

**Take 8 minutes — answer all 5 questions in ONE message**

Same rule as last week. One message. Voice-type if you can. Be honest about the things you've been telling yourself.

```
Here are my answers:

1. [YOUR ANSWER]
2. [YOUR ANSWER]
3. [YOUR ANSWER]
4. [YOUR ANSWER]
5. [YOUR ANSWER]
```

**Send.** Gemini will respond with what it noticed. Read carefully — it usually catches a pattern you didn't see.

---

### PROMPT 2 — OPPORTUNITY SCOUT CONFIGURATION

**Why this prompt matters:** Now we configure the actual Scout. This prompt does three things at once: it tells Gemini what your business does (from your Capability Statement), what you're avoiding (from Prompt 1), and what to filter for going forward.

**Type:**

```
You are now my Opportunity Scout.

Here's everything you need to know about my business —
pulled from my Capability Statement and our avoidance
audit:

SERVICE CATEGORIES: [PASTE FROM YOUR CAPABILITY STATEMENT
— e.g. Meta Advertising, Paid Social, Lead Generation,
GHL Automation, Social Media Management]

CORE SERVICES: [PASTE 2-3 SENTENCES FROM YOUR CAPABILITY
STATEMENT]

CERTIFICATIONS I HOLD: [LIST — Meta Ads Manager active,
GHL Agency, Google Workspace, etc.]

RETAINER SIZE RANGE: [SMALLEST WORTH MY TIME] to [LARGEST
I COULD DELIVER WITHOUT DROPPING THE BALL]

GEOGRAPHIC SERVICE AREA: [YOUR REAL RADIUS — e.g. San
Diego County primary, remote anywhere in US for the right
client]

DISQUALIFIERS — automatic NO if I see these in an
opportunity:
- [LIST: industries you don't serve, retainer floors you
  can't drop below, contract types you won't sign,
  geographic limits, etc.]

AVOIDANCE NOTES — flag these but don't filter them out
automatically:
- [LIST: things you've been avoiding that you might still
  consider — bigger retainers, LinkedIn outreach,
  unfamiliar verticals]

Going forward, when I give you a list of opportunities,
return a clean table with these columns:
- Company / Source
- Title or context (the role they're hiring for or the
  RFP scope)
- Estimated Retainer Value
- Posted Date / Inquiry Date
- Match Rating: Strong Match / Likely Match / Stretch /
  No
- The single biggest reason for that rating
- A flag if this is one of my "avoidance" categories

Confirm you have everything. If anything is unclear, ask
now.
```

**Send. Read the confirmation carefully. If Gemini asks a clarifying question, answer it before moving on.**

---

## PART 3 — DEEP RESEARCH + REASONING
**(0:50 – 1:25 | 35 minutes)**

### Why we use Deep Research instead of a regular search

A regular Gemini search gives you what's on the first page of Google.

Deep Research builds an actual research plan, then executes it. It scans Clutch, LinkedIn (public posts), agency review sites, industry forums, news about businesses changing agencies, and inbound RFP platforms. Then it cross-references everything and gives you a sourced report.

For client discovery, this is the difference between fishing in a pond and trawling the ocean.

---

### PROMPT 3 — THE DEEP RESEARCH BRIEF

**Why this prompt matters:** This single prompt is the heart of today's session. Run it once well and you have a sourced map of every San Diego retainer opportunity that fits your business in the next 90 days — including the ones nobody else is pitching on yet because the formal RFP hasn't been published.

**In Gemini, click the Deep Research button.** (It looks like a small icon next to the prompt box. If you don't see it, raise your hand.)

**Then paste this prompt:**

```
You are running a Gemini Deep Research investigation for
my business. Use the multi-step research plan to scan,
verify across sources, then report.

RESEARCH SCOPE:
- Clutch.co (San Diego region, my service categories)
- LinkedIn public posts (companies in my target verticals
  posting that they're hiring or looking for an agency)
- UpCity and Agency Spotter (my service area)
- Inbound RFP platforms (RFPIO, Loopio, PandaDoc) for
  marketing/advertising RFPs in San Diego
- Industry association job boards (NARI, ACCA, NRCA, RIA,
  IICRC) for marketing/agency RFPs
- Local government and school district procurement
  portals for communications and marketing RFPs in San
  Diego County
- Industry-specific Facebook groups and Reddit
  communities for "looking for an agency" signals
- Any 6-month switching signals: businesses publicly
  complaining about their current agency, announcing
  funding/expansion that implies marketing scale-up,
  posting RFPs

MY BUSINESS PROFILE:
[PASTE THE CONFIRMATION GEMINI GAVE YOU AT THE END OF
PROMPT 2 — IT HAS YOUR SERVICE CATEGORIES, RETAINER
RANGE, AND DISQUALIFIERS ALREADY]

WHAT I WANT BACK:

Find both ACTIVE opportunities (currently posted RFPs,
LinkedIn-visible "we need an agency" posts, recent
Clutch inquiries) and FORECAST opportunities (businesses
about to need an agency based on switching signals).
Elite biz dev teams track switching signals 3-6 months
before the formal RFP — include those.

For each opportunity you surface, return:
1. Company + role/context + estimated retainer value +
   posted date or signal date
2. The specific phrase or signal that makes this a match
   for my business
3. The likely incumbent agency (if any) and why they
   would beat me
4. A direct source link so I can verify

End with a brief AVOIDANCE AUDIT: of the opportunities
you found, identify the 2-3 I would most likely skip past
based on my avoidance patterns. For each one, name the
story I have probably been telling myself about why it's
not for me.

Cite every source. Do not invent opportunities. I would
rather have 5 real ones with sources than 50 ghost
listings.
```

**Send.** Deep Research will take 5 to 10 minutes. Use that time to flip back to your Capability Statement and read it out loud to yourself once. (You haven't read it out loud since last week. Trust me.)

---

### PROMPT 4 — THE MATCH-REASONING AUDIT

**Why this prompt matters:** Deep Research found you opportunities. Now we make Gemini explain its match decisions out loud, so you can pressure-test them. AI is not always right. The Audit catches the bad calls before you waste time on a pitch that wasn't actually a match.

**When Deep Research finishes, type:**

```
Take the top 5 opportunities from your Deep Research
report above. For each one, do three things:

1. Explain in plain English why you rated it a match.
   Quote the specific phrase from the post, RFP, or
   signal that triggered your rating.

2. Tell me what would have to be true for this match to
   be wrong. (Example: "This is a match if you have a
   home service vertical case study. If you don't, it's
   not.")

3. Name the strongest reason I might still NOT pursue
   this one — even though it matches on paper.

Number every issue. Be direct.
```

**Send. Read carefully.** Sometimes the AI will surface a reason that makes you walk away from an opportunity you would have chased. That's the Audit working.

---

### PROMPT 5 — THE AVOIDANCE LENS

**Why this prompt matters:** So far, the Scout has been filtering out the things you said you avoid. This prompt flips that. We tell Gemini to deliberately surface 2 or 3 opportunities **inside your avoidance categories** so you can decide whether the avoidance is real or just a story.

This is where most agency owners find a client they didn't know they were qualified for.

**Type:**

```
Now do the opposite of what you've been doing.

Look back at your Deep Research report and at my
avoidance notes. Surface 2-3 opportunities I would
normally SKIP because they fall into one of my avoidance
categories (LinkedIn outreach, larger retainer size, an
unfamiliar vertical, a directory I assume I don't
qualify for, an inbound RFP platform).

For each one, tell me:
1. Why a business owner or marketing director would
   consider me qualified despite my avoidance pattern
2. What I would actually need to do to be ready (cert
   application, directory listing, case study draft,
   warm intro path)
3. The single reason I should at least put this one on
   my "explore further" list

The goal is not to push me to pursue these — it's to
make sure I'm not skipping winnable retainers because of
a story I've been telling myself.
```

**Send. Read every word.** This is usually the most important output of the session.

---

## PART 4 — SHORTLIST + SHARE
**(1:25 – 1:40 | 15 minutes)**

### PROMPT 6 — THE SHORTLIST FILTER

**Why this prompt matters:** Your Deep Research report probably has 8 to 15 opportunities. That's too many to actually pursue. We need a top 3 — opportunities you'll actively work on between now and Week 5. The Scout picks them based on real fit, not just whatever caught your eye.

**Type:**

```
Based on everything you know about my business, my
capacity, my avoidance patterns, and the opportunities
you surfaced — pick my TOP 3 to actively pursue over the
next 30-90 days.

For each one in the top 3:
- Company name + source + retainer value + posted date
- The 2-3 reasons it ranked top 3 over the others
- The single biggest risk to a winning pitch
- The first action I should take this week (request a
  discovery call, build a relevant case study, find a
  warm intro, watch their ad library, etc.)

Format as a clean shortlist I can paste into a Google
Doc and reference all program.
```

**Send. Save the output.** This is your shortlist for the next 4 weeks.

---

**Small group share — get up and move (10 min)**

Get into groups of 3 or 4. Move to a different table than where you started.

Each person, in turn:
1. Read your top 1 opportunity to the group — company, source, retainer value, posted date
2. Read the "single biggest risk" Gemini flagged
3. The group asks ONE question: **"What's the first move you'll make this week to address the risk?"**

You should be able to answer that question out loud before the group moves to the next person.

This 10 minutes is where most of the real learning happens. Hearing what other people are pursuing — and why — will reshape what you pursue too.

When you come back to your seat, write down ONE opportunity from someone else's shortlist that surprised you.

---

## PART 5 — TURN THE SCOUT INTO A SAVED GEM
**(1:40 – 1:50 | 10 minutes)**

We've used the Scout effectively today as a one-time conversation. Now we save the process so you can run it weekly without rebuilding.

---

### PROMPT 7 — THE GEM PACKAGER

**Why this prompt matters:** Same skill as last week, new Gem. We're asking Gemini to bundle today's conversation into a clean instruction set you can paste into a saved Gem and run every week from now on.

**Type:**

```
Act as a master prompt engineer. Look at our entire
conversation today.

Write a single, comprehensive set of "Custom Instructions"
for a Google Gem called "Opportunity Scout."

The Gem's job: every time I run a fresh Deep Research
scan and paste the results in, the Scout filters those
opportunities against my business profile, surfaces
matches and stretches, runs the avoidance lens, and
produces a top 3 shortlist with first-action
recommendations.

The instructions must:
- Embed everything you've learned about my business today
  (service categories, certifications, retainer range,
  disqualifiers, avoidance patterns)
- Always run the match-reasoning audit before producing
  rankings
- Always include the avoidance lens — surface 2-3
  opportunities I would normally skip
- Always produce a top 3 shortlist with first actions
- Stay focused on San Diego region businesses unless I
  explicitly broaden the scope

Output: just the instructions, ready to paste into the
Gem Builder. No commentary, no labels, no preamble.
```

**Send. Copy the entire output. Don't read it yet — we'll save it first.**

---

### Build the Gem (5 minutes)

1. In Gemini's left sidebar, click **"Gems."**
2. Click **"New Gem"** (or the create button — Gemini's UI shifts).
3. Name it: **Opportunity Scout**
4. In the Instructions box, paste the entire output from Prompt 7.
5. Click **Save.**

If you don't save the Gem, none of this carries forward. Save it now.

---

### PROMPT 8 — THE TEST DRIVE

**Why this prompt matters:** A Gem you haven't tested is a Gem you don't trust. We run it on a fresh opportunity to confirm it actually works the way today's full conversation worked.

**Open your new Opportunity Scout Gem in a fresh chat. Paste in any 1-2 opportunities from your Deep Research report. Then type:**

```
Run your full process on this opportunity. Match-
reasoning audit, avoidance lens check, and a clear
recommendation: should I pursue, watch, or pass?
```

**Send.** This is the version of the Scout you'll use every week from now on.

---

## PART 6 — REFLECTION + SAVE YOUR WORK
**(1:50 – 2:00 | 5 minutes)**

### Save everything

Right now, before you forget:
1. Copy your top 3 shortlist into a Google Doc. Title it: **Opportunity Shortlist — Week 2**
2. Save the full Deep Research report (copy or download as PDF) into the same folder as your Capability Statement
3. Add the Opportunity Scout Gem to your Prompt Library Template
4. Verify the Gem is saved in your Gemini sidebar

If you skip this, you'll be rebuilding it next session.

### The pattern you just learned (memorize this)

**Last week:** Interview → Answer → Draft → Critique → Rewrite → Package → Test.

**This week:** same loop, plus a new layer — **Multi-Source Synthesis.**

You can now run a Deep Research scan and turn the result into a structured shortlist. You'll use this exact pattern in Week 3 to pull patterns across multiple proposals from the same prospect.

### Reflection question

Sit with this one. You don't have to answer out loud:

> Which opportunity surprised you most today — and what story have you been telling yourself about why you haven't pitched on anything like it before?

### Homework before Session 2B

1. Pick the **#1 opportunity** from your top 3 shortlist. Read every public detail you can find — their website, their reviews, their current ads, their team page, their LinkedIn. Highlight every problem or signal you notice.
2. Pull together **3 to 5 documents** from your business that prove you can deliver on this kind of work — past retainer agreements, screenshots of campaign results, signed client references, project descriptions, before/after metrics, anything. We'll upload them to NotebookLM in 2B.
3. If you can find **the last 1 or 2 ad campaigns or marketing assets** the same prospect has run (their Facebook Ad Library, their Instagram, their YouTube), save them as PDFs or screenshots. We'll use them in Week 3 to read their patterns.

**See you on [day] at [time]. Bring your laptop charged and your evidence documents ready to upload.**

---

---

# SESSION 2B — VIRTUAL
## "Build Your Evidence Base + Cross-Reference Your #1 Opportunity"

**Duration:** 1 hour 45 minutes  **Tool:** NotebookLM + your Opportunity Scout Gem  
**Prompt Budget:** 8 prompts  
**Outcome:** A permanent NotebookLM evidence base that holds your past performance documents, plus a cross-referenced fit score on your #1 opportunity that becomes the input to Week 3's Prospect Qualifier.

---

### Review work before Session 2B

Before we start, confirm you have:

- Your **#1 opportunity** research saved as a PDF or document (their site, ads, reviews, team page)
- **3 to 5 evidence documents** from your business (retainer agreements, campaign screenshots, references, case studies)
- Your **Opportunity Scout Gem** still saved in your Gemini sidebar
- Your **Capability Statement v3** in a Google Doc

If any of these are missing, raise your hand in chat and we'll wait for you.

---

### Start off with a reflection question

**Drop in chat — one sentence:**

> Which opportunity surprised you most from Session 2A, and what story have you been telling yourself about why you haven't pitched on anything like it before?

Read 3 or 4 aloud. The pattern usually emerges quickly: most of the avoidance stories are the same 4 or 5 stories.

---

### THE FRAME (what you'll learn today)

Last session you learned to **find** opportunities.

Today you learn to **prove you can deliver them.**

The new tool today is **NotebookLM.** It's where you upload all your past performance evidence — retainer agreements, campaign screenshots, signed references, case studies — and let an AI synthesize patterns across all of it. Once it's set up, you have a permanent, searchable proof library that any future Gem can pull from.

Two new prompting skills:

1. **Document grounding** — every claim the AI makes must point to a real document in your evidence base
2. **Filter chaining** — feeding the output of one Gem (today, the Scout) into another (today, NotebookLM) to produce something neither could produce alone

By the end you'll have a real fit score on your #1 opportunity — backed by real evidence — that you can take into Week 3.

---

## PART 1 — WARMUP + SET UP NOTEBOOKLM
**(0:00 – 0:25 | 25 minutes)**

### Drop in chat

In one sentence: how confident are you that you could win your #1 opportunity right now? Scale of 1 to 10. We'll come back to this number at the end of class.

### What NotebookLM is and why it matters

NotebookLM is Google's tool for working with your own documents. You upload a set of files — up to 50 sources at a time — and it indexes them. Then you can ask it questions and it answers using **only what's in those documents,** with citations.

For agency biz dev work, this changes the game. Instead of trying to remember which past client showed which capability, you upload all of it once, and the AI cross-references on demand.

**The rule: NotebookLM only knows what you give it.** If your evidence isn't uploaded, it doesn't exist as far as the AI is concerned.

### Set up your notebook

1. Go to **notebooklm.google.com** in a new tab. Sign in with the same Google account you used last week.
2. Click **"New notebook."**
3. Name it: **Agency Evidence Base — [YOUR AGENCY NAME]**
4. You'll see an "Add sources" panel. This is where you upload everything.

### Upload your evidence (8 minutes)

Upload everything you brought:

- Past retainer agreements / signed client contracts
- Campaign screenshots showing CPL, ROAS, leads, ad spend
- Signed reference letters or testimonials
- Case studies or written client wins
- **Capability Statement v3** (yes, upload your own statement — it becomes a source)
- The **#1 opportunity research** you saved as a PDF
- Any past ads or marketing assets from the prospect (their Facebook Ad Library exports, screenshots of their current creative)

**Don't worry if some files feel small or rough.** Even a one-page screenshot of an Ads Manager dashboard with a CPL number is gold. NotebookLM doesn't need polished case studies. It needs real data points.

While files upload, drop in chat: how many evidence documents did you bring? The cohort average will tell us what "ready" looks like.

---

### PROMPT 1 — THE EVIDENCE BASE INVENTORY

**Why this prompt matters:** Before we use NotebookLM to score anything, we need to know what's actually in there. This first prompt makes NotebookLM tell you what evidence you have — and just as importantly, what evidence you DON'T have. The gap is where most pitches fail.

**In NotebookLM, in the chat box at the bottom, type:**

```
Look at every source I have uploaded.

Build me an inventory of my proven capabilities, broken
into these categories:

1. PAST CLIENTS / RETAINERS — for each one, list:
   client, monthly retainer value, year, scope in one
   sentence
2. MEASURABLE OUTCOMES — every specific number,
   percentage, or dollar figure mentioned anywhere in my
   sources (CPL, ROAS, leads generated, ad spend
   managed, conversion rates, revenue driven)
3. CERTIFICATIONS / CREDENTIALS — anything I can prove
   with a document (Meta Ads Manager active, GHL agency
   account, Google Workspace, partnership badges)
4. REFERENCES — anyone named in my sources who could be
   contacted as a reference
5. CAPABILITY GAPS — categories where I have very thin
   or zero documentation. Be honest. If I uploaded 4
   home service campaigns and 0 e-commerce campaigns,
   say so.

For every claim you make, cite the specific source
document it came from.
```

**Send. Read the inventory carefully.** The Capability Gaps section is the most important part. It tells you what you're underclaimed for.

---

## PART 2 — CROSS-REFERENCE YOUR #1 OPPORTUNITY
**(0:25 – 1:00 | 35 minutes)**

### Why this section matters

Last week you found opportunities. Today we answer: **for your #1 opportunity, do you have the receipts to actually win it?**

This is the Prospect Qualifier preview. In Week 3 we'll build a full Go/No-Go agent. Today we get a sourced fit score on one specific opportunity.

---

### PROMPT 2 — THE REQUIREMENTS EXTRACTION

**Why this prompt matters:** Before we score fit, we need to know exactly what the prospect is looking for. This prompt makes NotebookLM read everything you uploaded about your #1 prospect — their site, their current ads, their reviews, their LinkedIn — and pull every single signal of what they need. No skimming. No "I think they probably want lead gen." Every signal of what they're trying to accomplish gets extracted and listed.

**Type:**

```
Look at the documents I uploaded about [PASTE PROSPECT
NAME — e.g., "Acme Roofing"]: their website, ads,
reviews, team page, and any other research.

Extract every signal of what this business needs from a
marketing agency. Group them into these categories:

1. STATED MARKETING NEEDS — anything they've said
   publicly about wanting more leads, better marketing,
   a new agency, etc.
2. INDUSTRY AND CLIENT TYPE — exactly what kind of
   business they are, their average ticket size, their
   service area, their seasonality
3. CURRENT MARKETING POSTURE — what their website looks
   like, what ads they're running, what their social
   presence shows, what reviews say about how customers
   find them
4. PAIN SIGNALS — complaints in reviews about response
   time, missed appointments, capacity issues, marketing
   gaps, current agency dissatisfaction
5. BUDGET AND DECISION-MAKER SIGNALS — company size,
   employee count, who's likely making the marketing
   decision, what retainer level they could comfortably
   afford

Pull every direct quote and screenshot detail you can.
Cite the exact document and section it came from.

Do not summarize. Do not interpret. Just extract.
```

**Send. Read every signal.** This list is what you have to either match, prove, or walk away from.

---

### PROMPT 3 — THE FIT SCORE

**Why this prompt matters:** Now NotebookLM compares your evidence (from Prompt 1) against the prospect's needs (from Prompt 2). This is the first time today you're getting an honest, evidence-backed score on whether you can actually win this client.

**Type:**

```
Now cross-reference my evidence base against the
prospect signals you just extracted.

For each of the 5 signal categories, give me:

1. Score on a 1-10 scale based on what's actually in my
   sources
2. The specific document(s) that support the score —
   "Your 2026 EMSR retainer at $2,500/mo with TikTok and
   Meta active demonstrates ability to deliver
   multi-platform paid for a restoration business"
3. If you cannot cite a real document, the score is
   automatically 5 or below — be strict about this
4. For any score below 7, the specific evidence I would
   need to add to close the gap

Then give me an overall recommendation:
- GO (I have what's needed and should pursue)
- GO IF (I can pursue if I add or partner for X)
- NO-GO (the gap is too large to close before they pick
  someone else)

Do not invent evidence. If a document does not exist in
my base, say so.
```

**Send. Read carefully.** This is the score that decides whether you spend the next 4 weeks pursuing this client or pivot to your #2 opportunity.

---

### PROMPT 4 — THE GAP-CLOSING PLAN

**Why this prompt matters:** A score below 10 isn't a death sentence — it's a list of homework. This prompt turns the gaps into a specific action plan. What can you do in the next 14 days to close the gap? What requires a teaming partner? What's actually fatal?

**Type:**

```
Look at every score below 7 in your fit assessment
above.

For each gap, tell me:

1. Is this gap FATAL (cannot be closed before they pick
   someone), FIXABLE WITH WORK (can be closed in 14
   days on my own), or FIXABLE WITH TEAMING (need a
   partner — white-label specialist, contractor, or
   referral relationship)?

2. If FIXABLE WITH WORK: the specific 14-day action
   plan — case study to write, partnership badge to
   apply for, reference letter to request, screenshot
   to capture from past client work

3. If FIXABLE WITH TEAMING: what kind of partner I need
   (their service speciality, vertical experience,
   credentials) and where I might find one

4. If FATAL: confirm it's fatal so I know to walk away
   from this one and pivot to my #2 opportunity

Be honest. Don't soften the assessment. I'd rather lose
a day to your analysis than 40 hours to a pitch I can't
win.
```

**Send.** This is your roadmap for the next two weeks.

---

## PART 3 — VIRTUAL BREAKOUT GROUPS
**(1:00 – 1:25 | 25 minutes)**

### Get into breakout rooms (groups of 3)

You'll be moved into breakout rooms of 3 people each. Each person gets 7 minutes — about 21 minutes total — plus a 4-minute return to the main room.

### What to do in your group

Each person, in turn:

1. **Share your screen** — show your Fit Score from Prompt 3 (just the overall recommendation and the lowest-scoring category)
2. **Read your Gap-Closing Plan from Prompt 4** — out loud, the whole thing
3. **The other two ask ONE question:** "What's the first action you'll take this week to close your biggest gap?"

You should be able to answer that question out loud before the group moves to the next person.

If your group finishes early, ask the harder question: **"Is your #1 actually still your #1, or has the fit score made you reconsider?"**

### Come back to main room (4 minutes)

Drop in chat: ONE thing your group caught that you missed in your own analysis.

Read 3 or 4 aloud. The pattern is usually the same — gaps are easier to see in someone else's shortlist than in your own.

---

## PART 4 — LOCK IN THE OPPORTUNITY + UPDATE YOUR SCOUT
**(1:25 – 1:50 | 25 minutes)**

### PROMPT 5 — THE OPPORTUNITY DOSSIER

**Why this prompt matters:** Everything we've done today is scattered across multiple chats. We need to consolidate it into a single dossier you can carry into Week 3 — when we build the full Prospect Qualifier and Client Intelligence Profile.

**In NotebookLM, type:**

```
Build me a complete Opportunity Dossier for [PASTE
PROSPECT NAME].

Include in this order:

1. Prospect summary — company, vertical, retainer
   value estimate, decision-maker, contact path
2. Full prospect signals list (from your earlier
   extraction)
3. My fit score per category, with cited evidence
4. My gap-closing plan with 14-day actions
5. The 3 strongest selling points I should lead with
   in any outreach or pitch — pulled directly from my
   evidence base
6. The 2 weakest spots I need to address before
   reaching out
7. A short list of any signals about their current
   agency or marketing partner — name them if I have
   it, and any complaints or switching signals

Format as a clean, single-document dossier I can paste
into a Google Doc.
```

**Send. Save the output.** This dossier is what feeds into Week 3.

---

### PROMPT 6 — UPDATE YOUR OPPORTUNITY SCOUT GEM

**Why this prompt matters:** Your Scout from Session 2A doesn't know what you learned today. We need to teach it what real fit looks like — based on the cross-reference work you just did — so the next time it surfaces opportunities, the rankings are sharper.

**Open your Opportunity Scout Gem (in Gemini, not NotebookLM). Type:**

```
I just ran a deep cross-reference on one of my top 3
opportunities. Here's what I learned about my own
strengths and gaps:

[PASTE THE SHORT VERSION OF YOUR FIT SCORE FROM PROMPT 3]

Update your internal logic going forward:
- When you rate match strength on future opportunities,
  weight the categories where I scored highest in this
  cross-reference
- Be more skeptical of opportunities that fall in
  categories where I scored low — flag them as "stretch"
  rather than "match"
- Keep surfacing avoidance-category opportunities, but
  only the ones that match my strongest evidence
  categories

Confirm you've updated your weighting and summarize the
new logic in 3 lines.
```

**Send.** Your Scout is now sharper than it was yesterday.

---

### PROMPT 7 — THE WEEK 3 BRIEFING

**Why this prompt matters:** Week 3 builds the **Prospect Qualifier** (full Go/No-Go agent) and the **Client Intelligence Profile.** Both of those need today's work as input. This prompt produces a clean briefing document that loads directly into Week 3.

**Type (still in NotebookLM):**

```
Produce a Week 3 Briefing.

This will be the input to two new Gems I'm building next
week — a Prospect Qualifier and a Client Intelligence
Profile.

The briefing should include:
1. My #1 opportunity (full dossier from Prompt 5)
2. The prospect's vertical, with anything you know
   about other businesses in their vertical from my
   sources
3. The 3 strongest categories of evidence in my base
4. The 2 weakest categories where I need to invest
5. My current avoidance patterns, in case the new Gems
   need them

Format as a single-page briefing.
```

**Send. Save.** Bring this to Session 3A.

---

### PROMPT 8 — THE FINAL CONFIDENCE CHECK

**Why this prompt matters:** Last move of the night. Same question we opened with — but now we have data behind the answer.

**In Gemini (not NotebookLM), in your Opportunity Scout Gem, type:**

```
Based on everything I've learned today — the prospect
signal extraction, the fit score, the gap-closing plan,
and the opportunity dossier — give me your honest
answer to one question:

If I committed to pursuing this #1 opportunity over the
next 30 days, what's my realistic probability of
landing a discovery call with the decision-maker? Give
me a percentage and three reasons.

Be direct. I want a number, not a hedge.
```

**Send. Read the answer.** Drop the number in chat. Compare it to your gut answer at the start of class.

---

## PART 5 — REFLECTION + WEEK 3 SETUP
**(1:50 – 2:00 | 10 minutes)**

### What you actually learned today

Two new prompting skills, on top of last week's loop:

1. **Document grounding** — making the AI cite real sources for every claim
2. **Filter chaining** — feeding the Scout's output into NotebookLM so each tool does what it's best at

You'll use both in every Gem we build going forward.

### Save your work

1. Save your **Opportunity Dossier** as a Google Doc — title it: **Dossier — [Prospect Name] — Week 2**
2. Save the **Week 3 Briefing** in the same folder
3. Verify your **NotebookLM evidence base** is named correctly and accessible
4. Verify your **Opportunity Scout Gem** is updated and saved
5. Add today's 8 prompts to your **Prompt Library Template**

### Reflection question

Sit with this one:

> Three weeks ago, you didn't know where the retainers were. Two weeks ago, you didn't have a Capability Statement. Tonight, you have a sourced shortlist of real opportunities, an evidence base full of your own past work, and a fit score backed by actual documents. **What's different in how you see your business right now compared to when you walked in?**

### Setup for Week 3

Next week we go from "I have a fit score" to "I have a full Go/No-Go decision and a client intelligence profile that tells me how this prospect's vertical thinks."

We'll build two Gems:

- **The Prospect Qualifier** — full Shipley-style Go/No-Go on any opportunity you upload
- **The Client Intelligence Profile** — Deep Research + NotebookLM combined, pulling patterns across multiple businesses in the same vertical so you understand what they actually value

By Week 3 you'll know not just whether to pursue, but how to position the pitch based on how the prospect's vertical thinks.

### Homework before Session 3A

1. **Take the first action** from your Gap-Closing Plan. Apply for the Meta Business Partner badge. Request the reference letter from EMSR or CDW. Email the potential teaming partner. Whatever it is — start it this week, before the gap calcifies.
2. **Pull together 3 to 5 examples** from your top target vertical (the same industry as your #1 opportunity) — competitor agency websites, ads from competing businesses in that vertical, RFP examples. Save them as PDFs. We'll upload them to NotebookLM in 3B and let it find patterns across them.
3. **Read your Opportunity Dossier out loud once.** If anything sounds off, fix it directly in your doc.

**See you [day]. Bring your laptop charged and your vertical research ready to upload.**

---

---

# ALL 16 WEEK 2 PROMPTS — COPY-PASTE READY
## "Week 2 Prompt Pack"

Every prompt for Sessions 2A and 2B in one place. Bookmark this tab. You'll come back to it during the live session.

---

## SESSION 2A — IN-PERSON
### "Build the Opportunity Scout"

---

### PROMPT 2A.1 — THE AVOIDANCE AUDIT

```
You know my business from our last conversation (or my
Capability Statement). Now I want you to interview me
about my AVOIDANCE PATTERNS — the opportunities I have
been quietly skipping.

Ask me 5 questions, all in one message. Push me. Do not
let me say "I don't avoid anything" — every agency owner
does.

Cover at minimum:
1. Which prospecting platforms or client channels have I
   been avoiding, and what's the real reason?
2. What retainer size scares me at the high end? Be
   specific.
3. What kind of client feels "not for me" even though it
   technically fits my services?
4. What certification, partnership, or directory do I
   always assume I don't qualify for, without checking?
5. What do I tell myself about why I haven't pursued more
   inbound RFP work or larger enterprise clients?

Do not write the audit yet. Just the 5 questions.
```

---

### PROMPT 2A.2 — OPPORTUNITY SCOUT CONFIGURATION

```
You are now my Opportunity Scout.

SERVICE CATEGORIES: [PASTE]
CORE SERVICES: [PASTE 2-3 SENTENCES]
CERTIFICATIONS I HOLD: [LIST]
RETAINER SIZE RANGE: [SMALLEST] to [LARGEST]
GEOGRAPHIC SERVICE AREA: [REAL RADIUS]

DISQUALIFIERS — automatic NO if I see these:
- [LIST]

AVOIDANCE NOTES — flag but don't filter automatically:
- [LIST]

Going forward, when I give you a list of opportunities,
return a clean table with:
- Company / Source
- Title or context
- Estimated Retainer Value
- Posted / Inquiry Date
- Match Rating: Strong / Likely / Stretch / No
- The single biggest reason for that rating
- A flag if this is one of my "avoidance" categories

Confirm you have everything. Ask if anything's unclear.
```

---

### PROMPT 2A.3 — THE DEEP RESEARCH BRIEF
*(Click the Deep Research button before sending this)*

```
You are running a Gemini Deep Research investigation for
my business. Use the multi-step research plan to scan,
verify across sources, then report.

RESEARCH SCOPE:
- Clutch.co (San Diego, my service categories)
- LinkedIn public posts (target verticals hiring or
  looking for an agency)
- UpCity and Agency Spotter (my service area)
- Inbound RFP platforms (RFPIO, Loopio, PandaDoc) for
  marketing/advertising RFPs in San Diego
- Industry association job boards (NARI, ACCA, NRCA,
  RIA, IICRC)
- Local government and school district procurement for
  marketing/communications RFPs
- Industry Facebook groups and Reddit communities for
  "looking for an agency" signals
- Switching signals: businesses complaining about
  current agencies, announcing scale-up, posting RFPs

MY BUSINESS PROFILE:
[PASTE THE CONFIRMATION FROM PROMPT 2]

WHAT I WANT BACK:
Find both ACTIVE opportunities and FORECAST
opportunities. For each:
1. Company + role/context + estimated retainer +
   posted date
2. The specific phrase or signal that makes this a
   match
3. The likely incumbent agency (if any) and why they'd
   beat me
4. A direct source link

End with an AVOIDANCE AUDIT: surface 2-3 opportunities
I'd most likely skip based on my avoidance patterns,
and name the story I'd be telling myself.

Cite every source. Do not invent opportunities.
```

---

### PROMPT 2A.4 — THE MATCH-REASONING AUDIT

```
Take the top 5 opportunities from your Deep Research
report above. For each one, do three things:

1. Explain in plain English why you rated it a match.
   Quote the specific phrase from the post, RFP, or
   signal.
2. Tell me what would have to be true for this match
   to be wrong.
3. Name the strongest reason I might still NOT pursue
   this one — even though it matches on paper.

Number every issue. Be direct.
```

---

### PROMPT 2A.5 — THE AVOIDANCE LENS

```
Now do the opposite of what you've been doing.

Look back at your Deep Research report and at my
avoidance notes. Surface 2-3 opportunities I would
normally SKIP because they fall into one of my avoidance
categories.

For each one, tell me:
1. Why a business owner would consider me qualified
   despite my avoidance pattern
2. What I would actually need to do to be ready
3. The single reason I should at least put this one
   on my "explore further" list

The goal is not to push me to pursue these — it's to
make sure I'm not skipping winnable retainers because
of a story I've been telling myself.
```

---

### PROMPT 2A.6 — THE SHORTLIST FILTER

```
Based on everything you know about my business, my
capacity, my avoidance patterns, and the opportunities
you surfaced — pick my TOP 3 to actively pursue over
the next 30-90 days.

For each one in the top 3:
- Company + source + retainer value + posted date
- The 2-3 reasons it ranked top 3 over the others
- The single biggest risk to a winning pitch
- The first action I should take this week

Format as a clean shortlist I can paste into a Google
Doc.
```

---

### PROMPT 2A.7 — THE GEM PACKAGER

```
Act as a master prompt engineer. Look at our entire
conversation today.

Write a single, comprehensive set of "Custom Instructions"
for a Google Gem called "Opportunity Scout."

The Gem's job: every time I run a fresh Deep Research
scan and paste results in, the Scout filters those
opportunities against my business profile, surfaces
matches and stretches, runs the avoidance lens, and
produces a top 3 shortlist with first-action
recommendations.

The instructions must:
- Embed everything you've learned about my business today
- Always run the match-reasoning audit before rankings
- Always include the avoidance lens — surface 2-3
  opportunities I'd normally skip
- Always produce a top 3 shortlist with first actions
- Stay focused on San Diego region unless I broaden it

Output: just the instructions, ready to paste into the
Gem Builder. No commentary, no labels, no preamble.
```

---

### PROMPT 2A.8 — THE TEST DRIVE
*(Run this INSIDE your new Opportunity Scout Gem)*

```
Run your full process on this opportunity. Match-
reasoning audit, avoidance lens check, and a clear
recommendation: should I pursue, watch, or pass?

[PASTE 1-2 OPPORTUNITIES FROM YOUR DEEP RESEARCH REPORT]
```

---

## SESSION 2B — VIRTUAL
### "Build Your Evidence Base + Cross-Reference Your #1 Opportunity"

---

### PROMPT 2B.1 — THE EVIDENCE BASE INVENTORY
*(Run this in NotebookLM after uploading all evidence documents)*

```
Look at every source I have uploaded.

Build me an inventory of my proven capabilities, broken
into these categories:

1. PAST CLIENTS / RETAINERS — for each one: client,
   monthly retainer value, year, scope in one sentence
2. MEASURABLE OUTCOMES — every specific number,
   percentage, or dollar figure mentioned anywhere in
   my sources
3. CERTIFICATIONS / CREDENTIALS — anything I can prove
   with a document
4. REFERENCES — anyone named in my sources who could
   be contacted as a reference
5. CAPABILITY GAPS — categories where I have very thin
   or zero documentation. Be honest.

For every claim you make, cite the specific source
document it came from.
```

---

### PROMPT 2B.2 — THE REQUIREMENTS EXTRACTION

```
Look at the documents I uploaded about [PROSPECT NAME]:
their website, ads, reviews, team page, and any other
research.

Extract every signal of what this business needs from a
marketing agency. Group them into these categories:

1. STATED MARKETING NEEDS
2. INDUSTRY AND CLIENT TYPE
3. CURRENT MARKETING POSTURE
4. PAIN SIGNALS
5. BUDGET AND DECISION-MAKER SIGNALS

Pull every direct quote and screenshot detail you can.
Cite the exact document and section.

Do not summarize. Do not interpret. Just extract.
```

---

### PROMPT 2B.3 — THE FIT SCORE

```
Now cross-reference my evidence base against the prospect
signals you just extracted.

For each of the 5 signal categories, give me:
1. Score on a 1-10 scale based on what's actually in my
   sources
2. The specific document(s) that support the score
3. If you cannot cite a real document, the score is
   automatically 5 or below — be strict
4. For any score below 7, the specific evidence I would
   need to add

Then give me an overall recommendation:
- GO / GO IF / NO-GO

Do not invent evidence. If a document does not exist in
my base, say so.
```

---

### PROMPT 2B.4 — THE GAP-CLOSING PLAN

```
Look at every score below 7 in your fit assessment above.

For each gap, tell me:
1. Is this gap FATAL, FIXABLE WITH WORK (14 days), or
   FIXABLE WITH TEAMING?
2. If FIXABLE WITH WORK: the specific 14-day action plan
3. If FIXABLE WITH TEAMING: what kind of partner I need
   and where I might find one
4. If FATAL: confirm so I pivot to my #2 opportunity

Be honest. Don't soften the assessment. I'd rather lose
a day to your analysis than 40 hours to a pitch I can't
win.
```

---

### PROMPT 2B.5 — THE OPPORTUNITY DOSSIER

```
Build me a complete Opportunity Dossier for [PROSPECT
NAME].

Include in this order:
1. Prospect summary — company, vertical, retainer
   estimate, decision-maker, contact path
2. Full prospect signals list
3. My fit score per category, with cited evidence
4. My gap-closing plan with 14-day actions
5. The 3 strongest selling points I should lead with
6. The 2 weakest spots I need to address before
   reaching out
7. Signals about their current agency / partner

Format as a clean, single-document dossier I can paste
into a Google Doc.
```

---

### PROMPT 2B.6 — UPDATE YOUR SCOUT GEM
*(Run in your Opportunity Scout Gem, NOT NotebookLM)*

```
I just ran a deep cross-reference on one of my top 3
opportunities. Here's what I learned:

[PASTE THE SHORT VERSION OF YOUR FIT SCORE FROM PROMPT 3]

Update your internal logic going forward:
- Weight the categories I scored highest in
- Flag opportunities in low-scoring categories as
  "stretch" rather than "match"
- Keep surfacing avoidance-category opportunities, but
  only the ones that match my strongest evidence

Confirm you've updated your weighting and summarize the
new logic in 3 lines.
```

---

### PROMPT 2B.7 — THE WEEK 3 BRIEFING
*(Run in NotebookLM)*

```
Produce a Week 3 Briefing.

This will be the input to two new Gems I'm building next
week — a Prospect Qualifier and a Client Intelligence
Profile.

Include:
1. My #1 opportunity (full dossier from Prompt 5)
2. The prospect's vertical, with anything from my
   sources about other businesses in it
3. The 3 strongest categories of evidence in my base
4. The 2 weakest categories where I need to invest
5. My current avoidance patterns

Format as a single-page briefing.
```

---

### PROMPT 2B.8 — THE FINAL CONFIDENCE CHECK
*(Run in your Opportunity Scout Gem)*

```
Based on everything I've learned today — the prospect
signal extraction, the fit score, the gap-closing plan,
and the opportunity dossier — give me your honest answer
to one question:

If I committed to pursuing this #1 opportunity over the
next 30 days, what's my realistic probability of landing
a discovery call with the decision-maker? Give me a
percentage and three reasons.

Be direct. I want a number, not a hedge.
```

---

---

# PROMPTING FRAMEWORKS CHEATSHEET
## "The Mental Models Behind Great Prompts"

You don't need to memorize these. You need to recognize them. Every prompt in this program uses one or more.

---

## FRAMEWORK 1: THE 5-PART PROMPT

**The foundation. Use it for every prompt.**

| Part | What It Means | Example |
|------|-------------|---------|
| **ROLE** | Who you want the AI to be | "You are an expert in marketing agency positioning..." |
| **TASK** | What you want it to do | "Help me build a Capability Statement..." |
| **CONTEXT** | Background info it needs | "I run a small agency in San Diego that does..." |
| **FORMAT** | How the output should look | "Format as a two-page document with these sections..." |
| **REFERENCES** | Examples or source materials | "Use language a real business owner would respect..." |

**The shortcut:** R-T-C-F-R. Role, Task, Context, Format, References.

---

## FRAMEWORK 2: PACE

**For prompts where you need to solve a specific problem for a specific audience.**

| Part | What It Means | Example |
|------|-------------|---------|
| **P**roblem | The challenge you're solving | "I need to qualify whether to pitch this prospect" |
| **A**udience | Who the output is for | "A business owner evaluating 10 agencies" |
| **C**ontext | The relevant background | "My agency has these strengths and these gaps" |
| **E**xpectation | The format and tone you need | "A 1-10 score with reasoning, in plain language" |

**Use PACE when:** You're solving a specific business problem and the audience matters.

---

## FRAMEWORK 3: STEER

**For content creation where voice and style matter.**

| Part | What It Means | Example |
|------|-------------|---------|
| **S**tatement | The main idea | "How my Capability Statement aligns with the client's goal" |
| **T**ype | The kind of content | "A professional one-pager" |
| **E**xamples | References for style | "In the tone of a top-tier agency but conversational" |
| **E**xplanation | Audience and tone | "For a business owner, professional but human" |
| **R**esults | The outcome you want | "They should feel I understand their business" |

**Use STEER when:** You're creating content that needs a specific voice.

---

## FRAMEWORK 4: THE CRITIQUE LOOP

**The most important pattern in the entire program.**

```
GENERATE → CRITIQUE → REWRITE
```

1. **GENERATE** — Ask the AI for a first draft. Don't get attached.
2. **CRITIQUE** — Have the AI put on a different hat (skeptical client, CFO, competitor) and tear the draft apart.
3. **REWRITE** — Feed the critique back to the AI and ask it to fix what was broken.

You'll use this loop in every Gem. Memorize the shape.

---

## FRAMEWORK 5: PERSONA STACKING

**Get 360-degree feedback in one prompt.**

Instead of asking one expert to review your work, ask 3 experts at once. Each persona has different priorities. Each catches what the others miss.

**Example structure:**

```
Critique my [WORK] through THREE expert lenses simultaneously.

PERSONA 1 — The [Business Owner]
Priority: [What this persona cares about]
Tell me: [Specific feedback you want]

PERSONA 2 — The [Financial Decision-Maker]
Priority: [What this persona cares about]
Tell me: [Specific feedback you want]

PERSONA 3 — The [Day-to-Day Contact]
Priority: [What this persona cares about]
Tell me: [Specific feedback you want]
```

**Use this when:** Your work will be evaluated by multiple people before a decision is made. (Almost every retainer.)

---

## FRAMEWORK 6: FRAME SHIFTING

**Same content, completely different angle.**

The big one for agency pitches is self-focused vs. client-focused:

| Self-Focused (Losing) | Client-Focused (Winning) |
|-----------------------|--------------------------|
| "We are a results-driven agency with 3 years of experience" | "Home service companies in your market are leaving leads on the table every month because..." |
| "Our proprietary system cuts production time" | "To keep pace with your peak season, our system delivers tested ad concepts in 48 hours, not two weeks" |
| "We offer competitive pricing" | "Our approach generates $8–12 in revenue for every $1 clients spend on our retainer" |

**Use frame shifting when:** Your content technically works but doesn't move the reader.

---

## THE ONE RULE THAT MATTERS MOST

> **"If your prompt doesn't tell the AI WHO it should be, WHAT it should do, and WHO the output is for — your prompt will produce average work."**

Average work doesn't win retainers. Specificity wins retainers.

---

---

# RETAINER BEST PRACTICES
### What Works, What Kills Deals, and How to Position an Agency for Consistent Wins

---

## Phase 1: I Am New to Agency Sales

### Step 1: What are service categories?

Service categories are how clients, directories, and platforms describe what your agency does. Unlike government contracting's rigid NAICS system, agency service categories are descriptive labels — but they still matter enormously for how you get found and how clients evaluate you.

- **Why you need them:** They determine which searches surface you, which RFPs you're qualified for, and how confidently you can describe your offer.
- **Where to define them:** Review how top agencies in your space describe their services on Clutch, LinkedIn, and their own websites.

### Step 2: Getting Credentialed

Credentialed agencies receive preference when business owners are comparing options. Apply for every platform certification you are eligible for.

- **Key credentials:** Meta Business Partner, Google Partner, TikTok for Business, HubSpot Partner, industry associations
- **Why it matters:** Credentials create shortcut trust signals for clients who can't evaluate your work directly

### Step 3: Register Your Agency Presence

Get your agency listed in the places clients actually look:
- **Clutch** — the primary B2B agency directory
- **LinkedIn Company Page** — where referrals verify you exist
- **Google Business Profile** — for local visibility
- **UpCity or Agency Spotter** — secondary directories worth listing on

---

## Phase 2: I Am Pitch-Ready

### Step 4: Research Your Market

Understand which client verticals have the most consistent need for your primary service. There are three primary retainer structures:

1. **Performance-based** (tied to leads, ROAS, or revenue)
2. **Managed services** (monthly fee for ongoing management)
3. **Project-based** (one-time or quarterly scope)

### Step 5: Market Yourself

- Develop a **capability statement** using the Gem you built in Session 1A.
- Prepare a targeted outreach plan and a **90-second elevator pitch.**
- Identify 3 referral partners who serve the same client type without competing with you.

---

## Phase 3: I Am Ready to Pitch!

### Step 6: Pitching On a Retainer

- **Capacity:** Only pitch what you can actually deliver.
- **Guidelines:** Follow the prospect's intake process precisely — if they ask for a proposal in a specific format, use it.
- **Differentiation:** Define how your agency stands out from the alternatives they're evaluating.
- **Attendance:** Participate in discovery calls fully — don't send a proposal without a conversation first.
- **Compliance:** Meet all proof requirements (case studies, references, credentials) before you ask for a signature.

### Step 7: If You Are Not Awarded the Retainer

Request feedback from the decision-maker. Frame it as: "I'd love to understand what would have made us a better fit — not to reopen the conversation, just to improve our process." Use this as a learning opportunity.

### Step 8: If You Are Awarded the Retainer

Onboard immediately and professionally. Set expectations clearly in the first week. If you have questions about scope, address them before work begins — not after.

### Step 9: Growing with the Process

- Build case studies from every client win — with their permission and real numbers.
- Stay connected to your client verticals through trade associations, local events, and industry groups.
- Use every closed deal to earn one referral introduction before the engagement ends.

---

### Tips That Actually Close Retainers

- **Get specific early:** The more precisely you describe who you serve and what you produce, the faster good-fit clients recognize themselves.
- **Be realistic:** Only pitch what you can deliver at the level that earns a testimonial.
- **Build referral relationships:** The best clients come from people who've already experienced your work or know someone who has.
- **Persistence with patience:** Most deals take 2-4 touchpoints. Follow up consistently without desperation.

---

*BELL AI For Retainers — Week 1 Packet*  
*tools@scalehere.com*
