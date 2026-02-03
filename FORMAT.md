# Remote Jobs Briefing – Page Format (MUST KEEP CONSISTENT)

All daily pages (`YYYY-MM-DD.html`) must match the **same layout, sections, and styling** as `2026-02-02.html`.

## Required structure

- `<head>` includes:
  - Umami script (website id: `cec8b016-3089-457e-9695-5c7cb7fa9d21`)
  - Inline CSS identical (or functionally identical) to `2026-02-02.html`
  - Meta description
- Body layout:
  - Container wrapper `.container`
  - Back link: `← Back to Archives`
  - Header with:
    - Title `💼 Remote Jobs Briefing`
    - `.issue-info` as: `Issue #N · <Weekday>, <Month> <D>, <YYYY>`
  - **Stats bar** (`.stats-bar`) with 4 stats (Jobs Today, DevOps Roles, Worldwide, Top Hourly or similar)
  - **Market Insight** box (`.insight-box`) with short paragraph
  - **Featured Opportunity** section with one `.featured-job` (badge `TOP PICK`)
  - Multiple **job category sections** (`h2.section-title`) with multiple `.job-card`
  - **Tips box** (`.tips-box`) with a short list
  - **Quote** section (`blockquote.quote` with `p` + `cite`)
  - Footer matches `2026-02-02.html`.

## Content rules

- Every job card includes: company, title (link opens in new tab), a highlight line, and tag chips.
- Prefer categories: Programming / DevOps / Product.
- Issue number increments daily starting from `2026-02-01` as Issue #1.

If the format drifts, **fix the generator/prompt before publishing**.
