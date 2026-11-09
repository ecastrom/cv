# CHANGELOG

## 2026-10-20 — Session 1: CV update and redesign

1. Removed clutter from the repository: an old Claude worktree copy of the whole site (`.claude/worktrees/…`), Word lock/temp files, and the 2023 CV files (`CV_EDGAR_CASTRO_2023.*`, `CV_with_Intro_2023.docx`). Added `.gitignore` so they don't come back.
2. Replaced the stock `jekyll-theme-minimal` with a custom layout (`_layouts/default.html`) and stylesheet (`assets/css/site.css`): one serif column, top navigation, photo on the home page only, dates aligned right, dark mode, phone layout, print styles.
3. Smaller web photo (`assets/img/photo.jpg`, 36 KB instead of the 2 MB PNG on every page).
4. `cv.md` rewritten:
   - Dropped Summary and Methods; new order: Positions, Education, Fields, Publications, Working Papers, Work in Progress, Conferences, Grants, Teaching, Experience, Professional Activities.
   - Current post: "Faculty Member in Economics (Profesor de planta)" instead of "Assistant Professor", because at Tec that is the second level.
   - One citation style throughout; hoarding paper now shows "Revise and resubmit, JEBO".
   - Added ECON 495 Policy Impact Evaluation; ECON 306 dated Spring 2024 – Spring 2025, as on the teaching page.
   - Conferences and grants grouped by year; refereeing as one line of journals.
   - "University of Pacific" → "Universidad del Pacífico"; "Cesar" → "César".
   - Phones removed from the web page (they stay in the PDF).
5. `research.md` and `teaching.md` restyled and aligned with the CV (same coauthor lists and titles as the June 2026 CV).
6. `main.md`: wording of the current post, link to the new PDF. New `index.html` sends `/cv/` to the home page.
7. New PDF CV built from `cv.md`: `python tools/build_cv.py` → `assets/Castro_CV.pdf` (XeLaTeX, XCharter, 3 pages). The PDF link now points here instead of Google Drive.

8. Committed and pushed (ab7abe3); verified live on GitHub Pages.
9. Added Fall 2026 Tec courses "De micro incentivos a macro resultados" and "Economía conductual" to the teaching page and the CV (English names on the CV, Spanish in parentheses). Codes taken from Experiencia21 (via the PI's Chrome session): EC1025 (groups 602 and 611, Aug–Dec 2026) and EC1015 (groups 301 and 303, Nov 2–Dec 7, 2026).

## 2026-11-08 — Session 2: restyle in GMU colors and Projects page

10. Whole site restyled after looking at stanislaomaldonado.org, without copying it: a Mason green band at the top holds the name, the navigation and the page title, with a gold rule under it; the page is wider (54rem); section headings sit in a left column beside their entries; links are green (gold in dark mode). No search bar.
11. Home: photo, email and CV link in the left column, text on the right. Removed the line of links at the bottom (the navigation already has them) and added one sentence about the BEER Lab.
12. New `projects.md` and a "Projects" item in the navigation: BEER Lab (co-founder and deputy director) and the BEER Lab classroom experiments (programmed 20 of the games, revising others).
13. Added the working paper "Tackling Biased Beliefs to Foster Women's Entry into Economics: Experimental Evidence from Mexico" (with Stanislao Maldonado, Elvira Naranjo and Joana Chapa) to the research page and the CV; PDF CV rebuilt.
14. Page titles moved from the Markdown (`# Research` etc.) to the masthead; front matter gained `lede` and, for the CV, `heading`.
15. `.claude/` added to `.gitignore` (local preview config).

Checked in a local preview at desktop and phone widths, light and dark. Committed on 2026-11-09; not yet pushed when this entry was written.

### Current state
Site live at ecastrom.github.io/cv (the live site changes only after a push). Open questions are listed in SESSION_NOTES.md.

### TO RESUME WORK
- Edit `cv.md` (conventions are in SESSION_NOTES.md), then run `python tools/build_cv.py` to refresh the PDF.
- Commit and push to `main`; GitHub Pages rebuilds the site within a minute or two.
