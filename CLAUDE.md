# CLAUDE.md — website (Claire's homepage)

Static site, repo `clairehjx/website`, live at **https://claire-hjx.vercel.app**.
Git-connected to Vercel: **push to `main` auto-deploys** (~30–60s). No build step.

## Files
`index.html` (homepage) · `learn.html` (lessons page) · `science-workflow.html` (how the science tool works) · `styles.css` (all CSS) · `script.js` (footer year + `.reveal` IntersectionObserver) · `gate.js` (friends-only password) · `README.md`.

## Deploy / git — IMPORTANT
- **Ask-first:** make edits, show them, **do NOT push until the user says "push it"/"publish"**.
- Push = `git add -A && git commit && git push` (commits authored as `clairehjx`; repo-local credential helper uses her gh token — don't change it).
- After push, verify live with `curl`. This env has **no browser** — can't screenshot; verify via markup/curl + `grep -c '<div'` vs `'</div>'` balance.

## Voice (how Claire writes) — apply to ALL copy
Dry, sarcastic, self-deprecating; **anti-cheerful** (she rejects bubbly AI tone). **Near-zero emoji.** CAPS *sprinkle* on single words ("LIFE", "SO not me") but **no stretched letters** (FARRRR). Parenthetical asides / fourth-wall breaks. Casual: "build **stuff**", "big(ish)", "basically". British/SG spelling (colour, favourite, maths). Inside jokes are wanted ("a certain MOUSY"). Running gag: her **"perpetually cheerful AI 'pet'"**. Full rules: memory `claire-voice.md`.

## Design system — "Dreamy Watercolor Blue"
Tokens in `:root` (`styles.css`): `--ink #1c3a5e --ink-soft #4a6585 --blue #2b6cb0 --blue-deep #1f5290 --blue-bright #4a90d9 --sky #a8d8ea --wash #cfe8ff --mist #e3f2fd --paper #f4f9ff --card #fff --shadow --shadow-sm --radius 22px --maxw 1040px`. Fonts: **Fredoka** (headings/buttons), **Nunito** (body).
Reusable classes: `.wrap .nav .brand .hero`+`.blob`(b1–b3)+`.eyebrow` `.section-head`+`.kicker` `.card .btn`/`.btn-primary`/`.btn-ghost` `.reveal` (add to any block → fades in on scroll) `.chip`/`.chips` `.app-card`/`.app-thumb`/`.app-body`/`.app-actions` `.footer`.

## New standalone page → copy `science-workflow.html`'s pattern
Same `<head>` (fonts, `styles.css`, favicon) + **`<script src="gate.js"></script>` right after the viewport meta** + page-specific `<style>` block; nav brand → `index.html#top`, links back to `index.html#…`; `main>section>.wrap`; every card gets `.reveal`; footer has `<span id="year">`; `<script src="script.js">` last.

## Friends-only gate (`gate.js`)
Soft password overlay on all 3 pages (in `<head>`). Password is base64 in gate.js (`atob('cHVwcHk=')` = "puppy") — **keep it out of plaintext/comments**. Soft only: content is still in page source; fine for "friends", not real security. Unlock persists via `localStorage`.

## index.html layout
`#about` (about-text card + `.toolkit` card in 2-col `.about-grid`; the old fact-cards column was removed) → `#learn` (CTA → learn.html) → `#apps` (`.apps-grid` of `.app-card`s). The old `#journey` section was removed. Apps: **Shophouse Row** (separate repo/deploy `shophouse-row.vercel.app`), **Pokémon Coloring Book**, **Science Tutoring Tool** (links to cheat sheets + `science-workflow.html`), "More coming" placeholder. Linked external sites: `pokemon-coloring-book.vercel.app`, `science-cheatsheets.vercel.app`.

## learn.html
Hero + lessons index + Lesson 1 ("How do AI tools actually work?" — explains LLMs with ONLY PSLE maths: multiply/add weighted scores → percentages → guess-and-check → average → scale). Visuals are **pure CSS bars** (`.bar-model`/`.bar-fill`, width inline %) — no images. Built to append Lesson 2+. If editing the worked example, keep sums consistent: `5×8+5×4=60`, `5×4+5×2=30`, `5×1+5×1=10`, `60+30+10=100`.

See repo-root `../CLAUDE.md` for the multi-repo overview.
