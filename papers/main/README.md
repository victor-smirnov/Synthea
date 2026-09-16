# paper_v2

- `plan.md` — the working plan; dated decisions and notes.
- `frames.md` — the argument in frames (iteration 2); the text of the paper is written from it.
- `argument.hybrid.md` — the frames as Gellish facts (iteration 2; history, out of sync with the paper).
- `paper.hybrid.md` — the current paper's prose with one Gellish fact block per section (604 facts); the
  logical check of the paper. Rebuild with `tools/extract_prose.py` (LaTeX → `paper-prose.md`) and
  `tools/build_hybrid.py` (prose + fact blocks → hybrid), check with
  `nous gellish check docs/paper_v2/paper.hybrid.md -o REPORT.md` from the repo root; the last report is
  `verification/logic-check.md` (0 contradictions, 0 tensions, 0 violations, psychophysical coverage 10/10).
- `SOURCES.md` — every citation with the claim it has to support and its verification status.
- `verification/` — per-batch tasks for the source verification; `remaining.md` lists what is left.
- `notes-future.md` — dated notes for later versions and for the experimental work (not part of the paper).
- `removed-for-ka-paper.tex` — paragraphs cut from Section 4.8 (need, emotion, consolidation, the Field), material for the separate paper on the cognitive architecture.
- `sources/` — obtained copies of sources (not committed; see `.gitignore`).
- `main.tex` — preamble, title, abstract; the sections are separate files, one per part of the reduction:
  introduction, background, functional account, the Synthea framework (computational curvature),
  generalization of the functions in Transformers (the learner, the machine, the frame, localization, the mechanisms of generalization, the profile, falsification), discussion, conclusion. Frame ids are kept in comments.
- `refs.bib` — the bibliography, keyed by surname and year.

Build: `tectonic -X compile main.tex` (tectonic 0.17 in `~/.local/bin`, no system TeX needed).
Current draft: 49 pages, 155 cited keys over 156 rows in `SOURCES.md`, 149 of them verified against the source; seven section files `sec1-intro.tex` … `sec8-conclusion.tex` (no sec6) plus `sec-appendix.tex`.
