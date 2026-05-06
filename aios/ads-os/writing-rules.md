# Scale SD — Anti-AI-Slop Writing Rules

> The slop filter. Run every script through this BEFORE publishing.
> Source: Wikipedia "Signs of AI writing" (https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) + Eddie pattern + Scale SD voice.

## Why this exists

Default AI writing is generic, hedged, polished, dead. It reads like a marketing blog. Contractors smell it instantly and scroll. This file forbids the patterns that make AI writing detectable.

## The hard ban list — never appear in our copy

### Banned individual words (zero tolerance)

```
delve, leverage, robust, seamless, holistic, navigate, embark, foster,
empower, unlock, elevate, unleash, harness, propel, streamline, optimize,
synergy, paradigm, ecosystem, landscape (figurative), tapestry, vibrant,
intricate, multifaceted, comprehensive, cutting-edge, state-of-the-art,
revolutionary, game-changer, game-changing, transformative, dynamic,
innovative, pivotal, paramount, crucial, vital, essential, profound,
ever-evolving, fast-paced, rapidly-changing, in-depth, deep-dive,
methodology, framework (in copy), solution (as in "our solution"),
offering (noun), platform (when we mean ads), suite, end-to-end,
white-glove, world-class, best-in-class, next-level, mission-critical
```

### Banned phrases (zero tolerance)

```
"In today's [adjective] world"
"Imagine a world where"
"In the realm of"
"At the forefront of"
"Stay ahead of the curve"
"In an ever-evolving landscape"
"It's important to note"
"It's worth mentioning"
"It is crucial to understand"
"By leveraging X, you can"
"Take your business to the next level"
"Unlock the power of"
"Drive meaningful results"
"Empower your business"
"Revolutionize the way you"
"A holistic approach to"
"Comprehensive solution"
"Tailored to your needs" (we say "fits your trade" instead)
"Seamlessly integrate"
"Harness the power of"
"At [Company], we believe"
"As a [trade] professional"
"Whether you are X or Y"
```

### Banned structural patterns

1. **Em dashes.** Period. We use commas, semicolons, or new sentences.
2. **Bulleted lists in ad copy.** Sentences only. Bullets allowed in internal docs and lead-form questions, never in body copy.
3. **Three-part parallel constructions.** "Powerful, scalable, and reliable." Pick one adjective, drop the others. Never three.
4. **Rhetorical questions stacked.** One per script max, in the hook only.
5. **Hedged claims.** "May help you" / "could potentially" / "designed to assist." If we can't claim it firmly, don't claim it.
6. **Vague qualifiers.** "Various," "numerous," "a range of," "a variety of." Use specific numbers or drop the word.
7. **Closing with a summary.** AI loves to recap. Don't. End with the CTA, not "in conclusion."
8. **Setup-payoff balance.** AI weights every section equally. Real writing front-loads. Hook gets the most energy. Body trims fast.
9. **Title-case headlines that read like a blog.** Static ads use sentence case. Lowercase punchy lines beat title-case marketing lines.
10. **Adverbs for emphasis.** "Truly," "really," "absolutely," "literally." Cut them all.

## The Wikipedia AI-signs reference

Per https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing — these are the highest-signal AI tells:

| Sign | Why it screams AI | What we do instead |
|---|---|---|
| Excessive use of "—" (em dash) | LLMs default to it constantly | Periods. Or commas. |
| Overuse of "delve," "tapestry," "robust" | Ranked by Wikipedia as top AI tells | Banned (see list above) |
| Vague boosting language | "It's an exciting time for X" | Skip. Get to the pain. |
| Unwarranted hedging | "It's important to consider" | Just say it. |
| Title-case in mid-sentence | "Our Innovative Approach" | Lowercase. Always. |
| Filler transitional phrases | "Furthermore," "Moreover," "Additionally" | Just continue. |
| Closing summary paragraphs | Restating what was already said | End on the CTA. Cut everything after. |
| Editorializing about importance | "This is a crucial topic" | If it's crucial, prove it, don't claim it. |
| Promotional puffery | "Cutting-edge," "world-class" | Banned. |
| Symmetrical structure | Three points, three paragraphs, three takeaways | Asymmetric. Front-load. |

## Positive rules (what TO do)

1. **Open with a real sentence.** First word should not be a generic call-out ("Attention contractors!"). Open with a thought a contractor would actually say.
2. **Specifics beat abstractions.** "$85,000 pool" beats "high-ticket project."
3. **Concrete nouns beat abstract ones.** "Job site," "phone," "calendar," "form" beat "engagement," "experience," "journey."
4. **Active voice, present tense.** "We film your ads" not "Your ads are filmed by us."
5. **Short clauses, hard stops.** Periods earlier than feels natural for AI.
6. **One idea per sentence.** If you can split it, split it.
7. **Tell, don't tease.** Contractors don't have time for "wait until you see this." Just say it.
8. **Use contractions.** "We're," "you're," "we'll," "won't." AI under-uses contractions. We over-use them on purpose.
9. **Allow disfluencies in spoken scripts.** "Look, the thing is..." "Real talk." "Here's the deal." These are voice markers Register C demands.
10. **Numbers must be exact and verified.** "90 leads" beats "lots of leads." "$85k pool" beats "huge project."

## The 5-pass slop check (run on every script before publishing)

### Pass 1: Banned-words scan
Ctrl-F every word in the banned list. Zero allowed.

### Pass 2: Em-dash scan
Ctrl-F "—". Zero allowed. Replace with periods.

### Pass 3: Read-aloud test
Read the script out loud at contractor pace. Strike any line:
- You wouldn't say to a contractor in person
- That makes you sound like a marketer
- That you trip over

### Pass 4: First-three-words test
Look at the first 3 words of every sentence. If 3+ sentences start with a generic AI opener ("In today's," "By leveraging," "It's important," "When it comes to"), rewrite.

### Pass 5: Specificity audit
Highlight every adjective and number. Each one must be either (a) verifiable from `product.md` proof table or (b) cuttable. If neither, cut.

## The Eddie test

Ask: "would Eddie ship this?" Eddie ships scripts that sound like a contractor saying it to another contractor at a job site. Eddie does NOT ship scripts that sound like a marketing agency talking about contractors.

If your script sounds like the second thing, rewrite from the hook.

## Reference

- https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing (full list, updated periodically)
- `voice.md` for register-specific rules
- `product.md` for verified claim sourcing
- `icp.md` for verbatim pain language by trade

## Update log

- 2026-05-05: Initial. Banned list compiled from Wikipedia AI signs + agency-jargon list + observed AI tells.
