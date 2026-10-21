# SESSION_NOTES — personal website / CV (ecastrom.github.io/cv)

Internal notes for Claude. Not published (excluded in `_config.yml`).

## Structure

GitHub Pages site (Jekyll, built by GitHub; no local Ruby/Jekyll on this machine).
Since 2026-10-20 there is no theme: a custom layout plus a stylesheet.

| File | Role |
|---|---|
| `_config.yml` | site title, email, address (footer); `exclude` list |
| `_layouts/default.html` | header nav (Research · Teaching · CV), home intro with photo when `home: true`, footer |
| `assets/css/site.css` | all styling. Serif (Source Serif 4), one column 44rem, light and dark, phone breakpoint 600px, print |
| `main.md` | home page (URL `/cv/main`, linked from elsewhere, so keep that URL) |
| `index.html` | redirects `/cv/` to `/cv/main` |
| `cv.md` | web CV **and the single source for the PDF** |
| `research.md`, `teaching.md` | papers (HTML `<p class="paper">` blocks), courses |
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

## Decisions / constraints from the PI
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
7. Fall 2026 courses added without codes ("De micro incentivos a macro resultados", "Economía conductual"); the English CV names are my translations. Need: codes, level, and whether EO 4024 continues. Experiencia21 (Canvas) needs the PI's own login; never enter credentials.
8. US phone +1 (202) still in the PDF; is it still in use?

## Pending
- PI to answer the questions above. The site has been live since 2026-10-20 (commit ab7abe3 and later).

## Resuming
Read this file and CHANGELOG.md. Preview without Jekyll: a rough Python renderer (python-markdown + layout substitution) served over http works in the browser pane; GitHub's kramdown adds curly quotes that the preview lacks.

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
