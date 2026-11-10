"""Build the PDF CVs from cv.md (English) and es/cv.md (Spanish).

Each Markdown page is the single source for its PDF. This script converts it
to LaTeX (latex/cv_body.tex or latex/cv_es_body.tex), which the matching
template (latex/cv.tex or latex/cv_es.tex) includes, then runs latexmk and
copies the result to assets/Castro_CV.pdf or assets/Castro_CV_es.pdf.

Usage (from the repository root):  python tools/build_cv.py
"""
import re
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LATEX = ROOT / "latex"
# (Markdown source, generated body, template, PDF written to assets/)
JOBS = [
    ("cv.md", "cv_body.tex", "cv.tex", "Castro_CV.pdf"),
    ("es/cv.md", "cv_es_body.tex", "cv_es.tex", "Castro_CV_es.pdf"),
]

DATE = re.compile(r'^<span class="date">(.*?)</span>\s*(.*)$')


def inline(s):
    links = []

    def keep_link(m):
        links.append((m.group(1), m.group(2)))
        return f"\x00{len(links) - 1}\x00"

    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", keep_link, s)
    for ch, rep in (("\\", r"\textbackslash{}"), ("&", r"\&"), ("%", r"\%"),
                    ("#", r"\#"), ("_", r"\_"), ("$", r"\$")):
        s = s.replace(ch, rep)
    s = re.sub(r"\*\*(.+?)\*\*", r"\\textbf{\1}", s)
    s = re.sub(r"\*(.+?)\*", r"\\emph{\1}", s)
    s = re.sub(r'"(.+?)"', r"``\1''", s)

    def put_link(m):
        text, url = links[int(m.group(1))]
        url = url.replace("%", "\\%").replace("#", "\\#")
        return "\\href{" + url + "}{" + inline(text) + "}"

    return re.sub(r"\x00(\d+)\x00", put_link, s)


def convert(md):
    md = re.sub(r"\A---\n.*?\n---\n", "", md, flags=re.S)
    out = []
    in_list = False
    for raw in md.splitlines():
        line = raw.rstrip()
        hard_break = raw.endswith("  ")
        if line.startswith("- "):
            if not in_list:
                out.append(r"\begin{entries}")
                in_list = True
            item = line[2:]
            m = DATE.match(item)
            if m:
                out.append(rf"\entry{{{inline(m.group(1))}}}{{{inline(m.group(2))}}}")
            else:
                out.append(rf"\entry{{}}{{{inline(item)}}}")
            continue
        if in_list:
            out.append(r"\end{entries}")
            in_list = False
        if not line or line.startswith("# ") or line.startswith("<p"):
            out.append("")
        elif line.startswith("## "):
            out.append(rf"\section{{{inline(line[3:])}}}")
        elif re.fullmatch(r"\*\*[^*]+\*\*( \(.*\))?", line):
            out.append(rf"\group{{{inline(line)}}}")
        else:
            out.append(inline(line) + (r"\\" if hard_break else ""))
    if in_list:
        out.append(r"\end{entries}")
    return "\n".join(out) + "\n"


def main():
    for src, body, template, pdf in JOBS:
        (LATEX / body).write_text(f"% Generated from {src} by tools/build_cv.py. Do not edit.\n"
                                  + convert((ROOT / src).read_text(encoding="utf-8")), encoding="utf-8")
        subprocess.run(["latexmk", "-xelatex", "-interaction=nonstopmode", "-quiet", template],
                       cwd=LATEX, check=True)
        shutil.copyfile(LATEX / template.replace(".tex", ".pdf"), ROOT / "assets" / pdf)
        print(f"Wrote assets/{pdf}")


if __name__ == "__main__":
    main()
