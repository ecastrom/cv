# SESSION_NOTES — personal website / CV (ecastrom.github.io/cv)

Internal notes for Claude. Not published (excluded in `_config.yml`).

## Structure

GitHub Pages site (Jekyll, built by GitHub; no local Ruby/Jekyll on this machine).
Since 2026-10-20 there is no theme: a custom layout plus a stylesheet.
Restyled 2026-11-08 (see "Design" below).

| File | Role |
|---|---|
| `_config.yml` | site title, email, address (footer); `exclude` list |
| `_layouts/default.html` | (2026-11-09) navy top bar with name + nav; home (`home: true`) gets a light "cover" (name large, second line italic green; one-sentence statement; `lede`; underlined text links; rectangular portrait with an offset thin gold frame and caption (an arched top was rejected: "looks tombstone")), then the campus photo as a full-colour `.panorama` strip; other pages get a navy hero with `eyebrow`, `heading`/`title`, `lede`, and a background photo if `hero:` is set; navy footer |
| `assets/css/site.css` | all styling. Deep green `#0f3324` (bands), `#1d5a3a` (links) + gold `#c19a4b` (PI 2026-11-09: "not blue, make it green shade"); Source Serif 4 (text, headings) + Inter (labels, nav, buttons); 72rem wide; breakpoints 860/640px; light only (no dark mode: PI 2026-11-09 "I don't like it changes to dark theme"); print |
| `assets/img/` | web photos (EXIF stripped): campus.jpg (home hero), portrait.jpg (office selfie, 4:5), beer-lab-prizes.jpg, lab-session.jpg (Projects hero), lab-teams.jpg, lab-room.jpg (Teaching hero). `photo.jpg` (suit headshot) no longer used |
| `assets/photo/` | the PI's raw WhatsApp photos (63); git-ignored, never publish them directly |
| `main.md` | home page (URL `/cv/main`, linked from elsewhere, so keep that URL) |
| `index.html` | redirects `/cv/` to `/cv/main` |
| `cv.md` | web CV **and the single source for the PDF** |
| `research.md`, `teaching.md` | papers (HTML `<p class="paper">` blocks), courses |
| `projects.md` | Projects page: one `<div class="project">` per project (side label + role, title, text, links) |
| `.claude/launch.json` | local preview config (git-ignored); the script it points to lived in a session scratchpad and has to be recreated |
| `tools/build_cv.py` | cv.md → `latex/cv_body.tex` → XeLaTeX → `assets/Castro_CV.pdf` |
| `latex/cv.tex` | PDF template: header with phones (phones appear ONLY in the PDF), XCharter font |
| `assets/img/photo.jpg` | 480px web photo made from `PhotoID.png` (the original, kept but excluded from the build) |
| `assets/Hoarding_price_distortions.pdf`, `assets/pdf/Edgar_Castro_JMP_2023.pdf` | old paper PDFs, not linked; left untouched |

### Conventions in cv.md (the build script depends on them)
- `## Section` → section heading.
- `- <span class="date">YEARS</span> text` → dated entry (date flush right on the web and in the PDF).
- `- text` → undated entry. `**Bold line**` alone → group heading (e.g. an institution).
- Links `[text](url)`, `*italic*`, `"quoted titles"`. A trailing double space is a line break.
- After editing cv.md, run `python tools/build_cv.py` and commit the new PDF.

## Design (2026-11-09, replaces the 2026-11-08 design below)
- The PI found the green design "too minimalistic" and asked for something richer, like stanislaomaldonado.org. He sent the photos for the home page (office selfie, prize group photo, campus with Cerro de la Silla) and for Projects (two lab-session photos). Colours were not chosen: navy + gold by default.
- Home: photo hero, framed portrait (slightly rotated card), fields strip, About + News side by side (`.split`), "Selected papers" rows, BEER Lab feature band with the prize photo.
- Research: `<article class="paper">` rows: `.paper-meta` (year, kind) | title, authors, venue | `.paper-links` (first link is the "Read paper" button). Work in progress uses `.paper compact`.
- News items on the home page are hand-written in main.md; keep them factual (sourced from research.md/cv.md).
- Home cover redone 2026-11-09 because the PI found the photo-hero version "too obvious copycat from Stan's": no dark overlay, no framed tilted card, no boxed buttons, no numbered fields strip (fields now a line in About). Keep the home page visibly different from stanislaomaldonado.org.
- Captions: do not name the mountain or say the office is at Tec (the cork-board notes look like GMU Korea students').
- Student photos: the PI chose the prize photo (identifiable students). I flagged consent; still unconfirmed.

## Design (2026-11-08, superseded)
- The PI asked for something like stanislaomaldonado.org (his coauthor's site) "but not an obvious copy", in GMU colors, whole site, and **no search bar** (his output is small).
- Taken from the reference: a coloured band with the page title, a wider page, a side column of labels. Deliberately different: one band instead of white header + photo banner, no breadcrumb, no numerals, no logo, no boxed buttons, labels on the left rather than role on the right, all serif.
- Colors: Mason green `#006633` (masthead, links) and gold `#ffcc33` (rule under the masthead, current nav item). Dark mode: deeper green band, gold links.
- Pages no longer start with `# Title`; the title is in the masthead. Section `##` headings sit in a left column: the `h2` has zero height and a right padding of `100% - var(--side)`, so the entries start on its line. If a section's content is shorter than its (wrapped) heading, the next heading would collide; check after adding short sections.
- A first-child paragraph in `main` (research intro, `cv-meta`) runs from the left edge.

## Decisions / constraints from the PI
- Projects page (PI, 2026-11-08): BEER Lab (co-founder and deputy director, as on beer-lab.org/en/team) and the BEER Lab classroom games. The PI said he coded 20 of the games and is correcting Stan's, but wants the public wording soft: the page says only "I am one of the contributors to the collection" with the side label "Contributor" (PI, 2026-11-09; do not put the count or "correcting" on the site). The "about 185" count was read from teaching.beer-lab.org on 2026-11-08 and will go stale. Pukllay and WEBEAS were offered and not chosen.
- "Tackling Biased Beliefs…" (with Maldonado, Naranjo, Chapa; version Oct 31, 2026) added as a working paper at the PI's request. Title and authors checked on the PDF title page. The AEA registry entry AEARCTR-0017053 lists Maldonado, Naranjo and Chapa only (not the PI); told the PI.
- Must NOT look AI-generated: no cards, icons, emoji, gradients, marketing copy, or third-person voice.
- **Job title:** Tec has no tenure. Its classification puts "Profesor de Economía" as the first level and "Assistant Professor" as the SECOND. The PI is at the first level, so never write "Assistant Professor" or "tenure-track" for the current post. In use: "Faculty Member in Economics (Profesor de planta)"; home page: "full-time economics faculty member". The PI said it is hard to translate; they may still choose another wording.
- Summary and Methods sections dropped from the CV (PI agreed by silence).
- Phone numbers only in the PDF, not on the web.
- PDF compiles with XeLaTeX because MiKTeX's pdfLaTeX font maps are broken for XCharter/Charter. Don't run `initexmf` without asking.

## Open questions flagged to the PI (2026-10-20)
1. Coauthors of "Beliefs About Price Controls…": the June 2026 CV edit lists Maldonado and Sautua; research.md (Feb 2026) also had Joana Chapa and Lianet Farfán. Used the June list; **confirm**.
2. Colombia procurement WIP title: used the June title "Discretionality of Public Procurement and Efficiency: Colombia" (the old one was "How Does Flexibilization…").
3. CESED pre-doc (2018–2019) overlaps the GMU PhD. Is that correct?
4. ICFES wording "ranked 1/1000 nationwide" kept verbatim; meaning unclear.
5. "University of Pacific" changed to "Universidad del Pacífico"; Matias → Matías. Confirm.
6. EO 4024: "(for graduates)" dropped from the teaching page. Restore if it is a graduate course.
7. Fall 2026 courses: EC1025 De microincentivos a macroresultados (2 groups) and EC1015 Economía conductual (2 groups, last 5 weeks). The English CV names are my translations. Codes came from the Experiencia21 Canvas API (`/api/v1/courses?enrollment_state=active`) in the PI's signed-in Chrome; never enter credentials. The PI has a teacher role on the seed course P3018 "Experimentos e inferencia causal" but does NOT teach it; keep it off the CV (PI, 2026-10-20).
8. US phone +1 (202) still in the PDF; is it still in use?

## Pending
- PI to answer the questions above. The site has been live since 2026-10-20 (commit ab7abe3 and later).

## Resuming
Read this file and CHANGELOG.md. Preview without Jekyll: a small Python server that renders the layout with `python-liquid` (installed with `pip --target` into the scratchpad, plus a `relative_url` filter that prefixes `/cv`) and the pages with python-markdown, serving `/cv/<page>`; started through `.claude/launch.json` in the browser pane. It is not kramdown, so check the live site after pushing.

## Working Maxims (copy from global CLAUDE.md)
1. Do not touch raw source data. Work on copies. Worked products are not raw data and need no backups.
2. Do not force results.
3. Academic honesty is a categorical imperative. Never fabricate or misrepresent.
4. Highlight epistemic risks.
5. Verify all references twice; flag UNVERIFIED if unable.
6. Make assumptions explicit.
7. Protect user data wisely; proportionate, not paranoid.
8. Respect user edits; touch only the broken part. No .bak/-old/_backup files.
9. Read before overwrite, but don't hoard versions.
10. Test after writing (compile LaTeX, run code).
