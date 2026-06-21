# CLAUDE_CONTEXT — CCN 2026 final-project grading

> **Last updated:** 2026-06-21 (evening, by Brama) · **For:** the grading run on **Monday 22 June 2026**.

---

## ⚡ TRIGGER — what to do tomorrow

When Yadvinder points you at this repo (`cross-cultural-negotiation-course`), **run the full grading pipeline autonomously**: go into Google Drive, read every group's submission, grade all of them (Phase 1), re-grade the cohort for consistency (Phase 2), and report back. Do not re-brief or re-ask the settled decisions below — they're locked. Just confirm the group count, then run.

---

## THE RUN — step by step

1. **Pre-flight: confirm the cohort is complete.**
   - Google Drive folder: **"CCN Project Submission"**, ID `1UG2_YNSnqylMtkebS89j3HF38ChMFAC4` (owned by yrana@neglob.com).
   - List its subfolders (one per group, named `Project Name – Lastname`) with `search_files` → `parentId = '1UG2_YNSnqylMtkebS89j3HF38ChMFAC4'`.
   - Expect ~12–13 groups (class ~100, groups of ~4). **Report the count to Yadvinder and confirm it looks complete before grading** — a half-uploaded cohort produces bad re-grade anchors. The folder locks at 7:30 a.m.; after that the set is final.

2. **Phase 1 — grade each group.** For every group folder, invoke the **`cross-cultural-2026-assessment`** skill (installed at `~/.claude/skills/`). It reads the 5 artefacts from Drive, scores the four document dimensions /400, and appends per-student rows to the gradebook + writes a per-group evidence report. (The Ferrandino group was a dry run — re-grade it fresh with the rest, since groups may have edited before the lock; the CSV is idempotent and replaces a group's rows on re-run.)

3. **Phase 2 — re-grade the cohort.** Once all groups have a first-pass assessment, invoke **`cross-cultural-2026-recalibrate`**. It re-grades the four dimensions against absolute bands calibrated by the cohort's own exemplars (drift-guarded), and writes the three final outputs.

4. **Report back** with the Phase-2 headline (did any scores move materially, and why), then hand off: the final gradebook awaits Yadvinder's **Agent Quality** column.

5. **Sync** both repos after (course repo for outputs; nothing changes in Skills-repository during a run).

---

## OUTPUTS (all local, never written to the student Drive folder)

Under `cross-cultural-negotiation-course/assessments/`:
- `cohort-gradebook.csv` — Phase-1 first-pass scores (kept as history).
- `<group>/internal-assessment.md` — per-group evidence behind the scores.
- `cohort-gradebook-final.csv` — **the final** (Phase 2), 14 columns incl. Italian /30 + rounded /30.
- `changes-summary.md` — Phase 2: did anything major move, and why (read this first).
- `recalibration-report.md` — Phase 2: anchors, self-audit, promote-ready band fixes.

---

## SETTLED DECISIONS — do not re-litigate

- **Five rubric dimensions, /500.** Brama scores **four from the documents (/400)**: Domain Rigour, Generalisation, Coherence of Design, Evaluation Honesty.
- **Agent Quality (/100) is Yadvinder's**, scored **live** from the presentations, added end of day. Brama never scores it — column left empty. Final = subtotal + Agent Quality.
- **No `agent-link.md`** — agents shown live, not submitted. Don't expect or penalise it.
- **Graded artefacts (5):** Knowledge Base, PRD, System Instructions, Evaluation Report, `group.md`. Identify by **content, not filename**. **Ignore `*.mp4`** (recorded presentation).
- **−50 deduction** (behaviour in KB / knowledge in SI) fires on ≥3 distinct violations OR ≥1 structural violation. *(Threshold is a Brama design choice softening the README's binary wording — Yadvinder to confirm if he disagrees; default stands.)*
- **Contribution flag** is exceptional only (explicit non-contribution, or a member with no role at all). Flag, never deduct — Yadvinder decides the −2.
- **Comments column** = short student-facing comment, group-level, repeated across members.
- **Italian /30** = linear `Final/500×30`; rounded column = `ROUND(...)`. (500/500 = 30/30; 480 ≈ 29; 400 = 24/30.) *(Confirm if faculty uses a floor at 18 or 30 e lode.)*
- **Marks aren't released** until the final is assembled, so re-grading early groups in Phase 2 causes no "moving number" problem.

---

## DRIVE ACCESS — proven working (2026-06-21)

- Read with the Google Drive MCP tools. No OAuth blocker; folder reachable.
- `read_file_content` returns full text but **escapes** markdown (`\#`, `\*\*`) — fine, read past it.
- **Large files (KB, evaluation reports) don't return inline** — they save to a `tool-results/…txt` file (JSON `{fileContent}`). Extract with a one-line python step writing `fileContent` to a local `.md`, then Read it. Never grade from a preview snippet.

---

## DRY-RUN REFERENCE (Ferrandino group, 2026-06-21)

Cross-Cultural Neg Advisor (Ferrandino): Domain Rigour 93, Generalisation 95, Coherence 94, Evaluation Honesty 96 → **378/400**, no −50, zero fabricated citations, no contribution flag. Strong submission; use it as a rough top-band reference point, but re-grade it fresh tomorrow within the real cohort.

---

## STATUS

Both skills built, installed, and pushed (Skills-repository `ae260ef`). Dry run committed (course repo `a02371f`). Ready to run on Yadvinder's go tomorrow.
