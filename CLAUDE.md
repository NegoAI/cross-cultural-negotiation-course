<!-- repo-standard v1 -->
> Shared rules are in the global files, loaded here too. This file holds only this repo: what it
> is for, where things live, its own limits and procedures. Under 100 lines and 8 KB. A change
> replaces or deletes a line, never adds a second one on the same point. Stories and finished
> items are deleted, not archived: git keeps them. Standard: `claude-config/REPO-STANDARD.md`.

# cross-cultural-negotiation-course

## What this repo is

The Cross-Cultural Negotiation 2026 student project (instructor Yadvinder S. Rana): the five-step brief students followed to build an AI negotiation agent, plus the grading outputs for the cohort. Remote: `NegoAI/cross-cultural-negotiation-course`.

## Where things live

- `README.md`, `1-brainstorming.md` to `5-evaluation.md`: the student-facing brief and methodology. Open to see what students were asked to do.
- `final-submission/README.md`: what students submit.
- `assessments/`: per-group evidence reports, gradebooks (`cohort-gradebook-final.v2.csv`, `final-results-project70-test30.csv`), `RESULTS-cross-cultural-2026.md`, `recalibration-report.md`, `phase-3-report.md`, and the generator scripts `_build_gradebook.py` and `_build_gradebook_final.py`.
- `single assessment route/`: exam questions and feedback for the two single-exam students.

## This repo's limits

- Student names, marks and group evidence are confidential: never paste them outside this repo or its grading skills.
- A score is changed in the generator script and the file regenerated, or in column I (Agent Quality) of the gradebook only; do not hand-edit other gradebook cells.

## Procedures

- Grading skills: `cross-cultural-2026-assessment` (one group), then `cross-cultural-2026-recalibrate` (whole cohort), in `C:/Users/yrana/repos/Skills-repository/`. They are switched off between cohorts; read each `SKILL.md` there directly, or relink with the command in `Skills-repository/CLAUDE.md`.
- Regenerate a gradebook: run the matching `assessments/_build_gradebook*.py` by absolute path.
