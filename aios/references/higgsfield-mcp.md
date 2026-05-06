# Higgsfield MCP — Reference Guide

> Researched-once-saved-forever. Skills that generate ad video/image creative read this first.
> Last updated: 2026-05-05 | Status: REGISTERED — API key needed to activate

## Connection

- **Mechanism:** MCP — `npx -y higgsfield-mcp`
- **Auth:** API key in `.env` → `HF_API_KEY`
- **Get key:** https://cloud.higgsfield.ai → API Keys
- **Status:** ⚠️ Registered but not yet authenticated. Add `HF_API_KEY` to `.env` to activate.

## What Higgsfield Does

Cinematic-grade image and video generation for ad creative. 30+ models including:
- **Video:** Kling 3.0, Veo 3, Sora 2, Seedance 2.0, Wan, DOP Standard
- **Image:** Soul, Flux, Seedream, Reve, GPT Images 2.0
- **Talking head:** Avatar-based video with lip sync

Plugs into the creative → campaign loop:
`reel-script skill → Higgsfield (generate video) → Meta Ads MCP (upload + launch)`

## MCP Tools

| Tool | What it does |
|---|---|
| `generate_image` | Text-to-image with 16+ models |
| `generate_image_seedream` | Seedream-specific image gen |
| `generate_image_reve` | Reve model image gen |
| `edit_image_seedream` | Edit an existing image |
| `generate_video` | Image-to-video (cinematic) |
| `generate_video_kling` | Kling 3.0 video gen |
| `generate_video_seedance` | Seedance 2.0 video gen |
| `generate_video_dop_standard` | DOP Standard video gen |
| `generate_talking_head` | Talking head / avatar video |
| `create_character` | Save a reusable character reference |
| `list_characters` | List saved characters |
| `get_character` | Get a character by ID |
| `delete_character` | Remove a character |
| `upload_image` | Upload a source image |
| `get_generation_status` | Poll job status (async) |
| `get_request_status` | Check request status |
| `cancel_request` | Cancel an in-flight job |
| `list_styles` | List available visual styles |
| `list_motions` | List available motion presets |
| `debug_credentials` | Verify API key is working |

## Common Skill Patterns

### Generate a UGC-style ad video from a reel script
```
1. reel-script skill → approved 30-60s script
2. upload_image(source_image)           ← brand/job photo as starting frame
3. generate_video(
     prompt=script_as_visual_direction,
     model="kling",                      ← or seedance for more cinematic
     image_id=uploaded_image_id
   )
4. get_generation_status(job_id)        ← poll until complete
5. → video URL → pass to Meta Ads MCP for upload
```

### Create a reusable character for a client's owner/crew
```
create_character(
  name="{client_slug}-owner",
  image_url="{headshot_url}"
)
→ saves character_id for reuse across all future videos for this client
```

### Generate a before/after image for Pillar 1 (The Work)
```
generate_image(
  prompt="Before/after {job type} in San Diego neighborhood, contractor quality",
  model="flux"
)
→ use in caption-writer skill as post visual
```

## Async Pattern (important)

All generation calls are async — they return a `job_id`, not the result.

```
generate_video(...) → {job_id: "abc123", status: "processing"}
→ poll get_generation_status(job_id) every 10-15s
→ when status == "completed" → download result_url
```

Never block a skill waiting inline. Queue the job, log the job_id, check in a follow-up step.

## Per-Client Character Library

Once activated, create a character reference for each active client's owner so videos are consistent:

| Client | Character name | Status |
|---|---|---|
| EMSR (Joseph) | emsr-owner | pending — needs headshot |
| California Doors & Windows (Michael) | cdw-owner | pending |
| Tony (pool) | tony-owner | pending |
| VIP General Contractor (Victor) | vip-owner | pending |

## Known Limits

- Generation time: images ~10-30s, videos ~60-180s depending on model
- Kling 3.0 and Veo 3 produce highest quality but take longest
- Seedance 2.0 is fastest for batch content production
- Talking head requires a clean frontal headshot with neutral background
- Output videos are typically 5-10 seconds — chain multiple for longer ads
