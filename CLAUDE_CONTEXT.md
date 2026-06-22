# CLAUDE_CONTEXT — Cross-Cultural Negotiation 2026 grading

> **Snapshot saved:** 2026-06-22 (after lunch, by Brama). Phase 3 complete.
> **One-line state:** All 19 groups graded (Phase 1), re-leveled (Phase 2), and a **Phase 3** post-decision pass applied four instructor-approved changes to the bottom groups. The gradebook still awaits ONLY Yadvinder's live **Agent Quality** column. The Phase-2 OPEN decisions are now resolved (see PHASE 3 below).

---

## What this task is

Grading the end-of-term **Cross-Cultural Negotiation 2026** final project. Each group built an AI negotiation agent (Knowledge Base + PRD + System Instructions + Evaluation report + `group.md`) submitted to the shared Google Drive folder **"CCN Project Submission"** (`1UG2_YNSnqylMtkebS89j3HF38ChMFAC4`, owned by yrana@neglob.com), one subfolder per group.

**Rubric:** five dimensions × /100 = /500. Brama scores the **four document dimensions** → /400; **Yadvinder scores the fifth, Agent Quality, live from each demo** and adds it. /500 maps to the Italian /30 scale (500→30).

Two skills (installed at `C:\Users\yrana\.claude\skills\`):
- `cross-cultural-2026-assessment` (Phase 1 — one group at a time)
- `cross-cultural-2026-recalibrate` (Phase 2 — whole-cohort re-leveling once all groups are in)

---

## STATUS: complete through the document side

- **Cohort = 19 groups** (more than the ~12–13 expected). All graded.
- **Phase 1 complete** — 19 `assessments/<group>/internal-assessment.md` evidence reports + first-pass `assessments/cohort-gradebook.csv` (kept as audit trail).
- **Phase 2 complete** — re-leveled against absolute bands (drift-guarded). Outputs under `assessments/`:
  - `cohort-gradebook-final.csv` ← **THE final document-side gradebook.** 89 student rows, 4 re-graded dimensions, Italian /30 columns (`=J/500*30`, `=ROUND(K,0)`), formulas re-indexed, **Agent Quality (col I) left empty for Yadvinder.**
  - `changes-summary.md` — Yes/No headline (No major changes).
  - `recalibration-report.md` — anchors, inter-agent self-audit, band refinements, portable pattern.
  - `_build_gradebook.py` — the generator script (holds all scores/comments/names; re-run to regenerate the CSV if any score changes).
- **Phase-2 result:** scores HELD. Only one change cohort-wide: **Muriotto Domain Rigour 93→94** (subtotal 374→375). Three −50 KB/SI-separation deductions confirmed uniform (HomeGround, ACROSS, CCNA). **Zero fabricated citations across all 19 groups.**
- **Skill refinements applied** (2026-06-22) to `cross-cultural-2026-assessment` SKILL.md — the 4 calibration fixes the recalibration report produced are now live: (1) −50 behaviour-vs-scaffolding rule; (2) DR canonical-absence is not a deduction; (3) DR un-chunked raw-dump KB caps in low-80s; (4) EvalHon 90+ needs a *named surviving residual failure*.

---

## Final document-side scores (/400, post-recalibration)

| Group (namesake) | DR | Gen | Coh | EvH | /400 | Flag |
|---|---|---|---|---|---|---|
| Aria agent (Dell'Orto) | 96 | 97 | 96 | 97 | 386 | |
| CROSSBRIDGE AI (Geroldi) | 96 | 96 | 94 | 95 | 381 | |
| Cross-Cultural Kira Agent (Monaco) | 95 | 96 | 93 | 96 | 380 | |
| Cross-Cultural Neg Advisor (Ferrandino) | 93 | 95 | 94 | 96 | 378 | |
| B.R.O. (Rossi) | 94 | 96 | 90 | 97 | 377 | |
| Kairos (Malerba) | 94 | 95 | 93 | 93 | 375 | |
| CCN AI Agent (Muriotto) | 94 | 94 | 92 | 95 | 375 | |
| CultureBridgeAI (Biondi) | 94 | 93 | 91 | 95 | 373 | |
| Cross-Cultural AI Agent / "NEXA" (Longo) | 96 | 97 | 88 | 90 | 371 | |
| ADRELIX (Taferner) | 94 | 93 | 90 | 92 | 369 | |
| CCN AI Agent (Bolis) | 91 | 88 | 93 | 96 | 368 | |
| CCN AI Agent Culturae (Amendola) | 94 | 93 | 90 | 91 | 368 | |
| CCN AI Agent (Antonucci) | 94 | 93 | 91 | 89 | 367 | |
| NegotiaTe (Seghezzi) | 94 | 88 | 89 | 91 | 362 | |
| the BRIDGE (Berto) | 90 | 92 | 91 | 88 | 361 | |
| Negocierge (Caruso) | 84 | 76 | 90 | 93 | 343 | PRD corrected (Phase 3) |
| ACROSS (Belfrond) | 92 | 93 | 87 | 91 | 363 | −50 waived; Coh 82→87 (Phase 3) |
| CCNA (Manno) | 88 | 90 | 74 | 86 | 328 | −10 self-diagnosed leak (Phase 3) |
| HomeGround (Uysal) | 66 | 60 | 64 | 68 | 258 | −50 waived (Phase 3) |

Cohort is genuinely strong on documents — 15 of 19 in the 361–386 band; after Phase 3, ACROSS sits at 363, Negocierge 343, CCNA 328, and HomeGround (258) is the sole genuine outlier.

---

## PHASE 3 — post-decision pass (2026-06-22, after lunch) — see `assessments/phase-3-report.md`

The Phase-2 OPEN decisions were resolved by the instructor and applied:

1. **Negocierge PRD — RESOLVED.** Re-checked Drive: `PRD.md` is now the correct **Negocierge** (5 capabilities, seniority calibration, §7 incl. the 2-minute-scan criterion). The ARIA mismatch is gone. Coherence 66→90; subtotal **319→343**; flag cleared.
2. **KB/SI −50, recharacterised by culpability** (instructor override of Phase-2 rule 3b):
   - **ACROSS** −50 **waived** (blocks were self-labelled "not for KB" — packaging slip). Also Coherence **82→87** (same leniency applied to the leftover research-scaffolding hygiene ding). Subtotal **308→363**.
   - **HomeGround** −50 **waived** (KB weakness already priced into low dimension scores; −50 double-counted). Subtotal **208→258**.
   - **CCNA** −50 → **−10** (they diagnosed the exact leak in their own Part A and shipped it unfixed — a known, unremediated defect). Subtotal **288→328**.
3. **Skill rule updated** in both `cross-cultural-2026-assessment/SKILL.md` copies (installed + Skills-repo): rule 3(b) now scales the deduction by culpability (self-labelled→0; self-diagnosed-unfixed→−10; unlabelled heavy→−50 unless double-counted).
4. **Gradebook generator hardened:** `_build_gradebook_final.py` now **preserves any Agent Quality already typed into the CSV** on regenerate (col I is the instructor's and must survive a rebuild).

**Build-artifact note:** at snapshot time the CSV was locked open in Excel, so `cohort-gradebook-final.csv` on disk may still show pre–Phase-3 numbers until `_build_gradebook_final.py` is re-run. The script + this file + the Phase-3 report carry the authoritative Phase-3 scores.

---

## OPEN — needs Yadvinder's decision (resume here)

1. **Enter Agent Quality (col I) in `cohort-gradebook-final.csv`** from the live demos. This is the only thing between now and final /500 + /30 marks — the /30 columns auto-compute once col I is filled (500/500 → 30/30). One score per group, repeated across its member rows.
2. **[RESOLVED in Phase 3 — accepted the corrected PRD → 343.]** ~~Caruso (Negocierge) — PRD mismatch, his call.~~ The group **revised their Drive files mid-grading**; the submitted PRD now describes a *different* agent ("ARIA", 7 capabilities, advisor model) than the **Negocierge** the SI + evaluation + group.md build (5 capabilities, sparring partner). Graded **as-submitted at 319** (Coherence dragged to 66 by the mismatch), flagged. **Decide:** accept 319 as-is, OR ask the group to confirm the canonical PRD (Coherence and subtotal would likely rise if a matching Negocierge PRD exists). Data-integrity issue, not a calibration one.
3. **HomeGround roster (minor).** `group.md` lists **3 members** (Uysal, Alpdogan, Alparslan), each with a step lead, but a footer says "all **five** members." Possibly 2 students omitted — confirm true membership before finalising those rows. Not a contribution flag.

### Carry-over clarifications (low priority, from the 2026-06-21 briefing — still open)
- **−50 threshold** (≥3 distinct violations OR ≥1 structural) is a Brama design choice softening the README's binary wording. Confirm if you disagree; default stands and was applied uniformly.
- **Italian /30 mapping** is linear `Final/500×30` with a `ROUND()` column. Confirm whether faculty uses a floor at 18 or a "30 e lode" top — currently neither is applied.

---

## How to resume in the new thread

1. Read this file, then `assessments/changes-summary.md` and `assessments/recalibration-report.md` for the full picture.
2. Working file is `assessments/cohort-gradebook-final.csv`. To change a score or add Agent Quality: either edit the data in `assessments/_build_gradebook.py` and re-run it (regenerates the CSV with correct formula indices), OR — for Agent Quality only — type col-I values straight into the CSV/Excel.
3. Skills live at `C:\Users\yrana\.claude\skills\cross-cultural-2026-assessment\` and `...\cross-cultural-2026-recalibrate\`.

## Why we did it this way (decisions this session)

- **Architecture:** graded the 17 fan-out groups with one subagent each (HomeGround + Ferrandino done separately); each subagent wrote only its own per-group report and *returned* score data; **the master CSV was assembled centrally** to avoid parallel write races. Reusable pattern.
- **Rate-limit lesson:** launching ~18 agents at once tripped a server-side rate limit. Fix = waves of 4–6 + retry-on-rate-limit instruction. Logged to global memory (`agent-fanout-concurrency-limit`).
- **Recalibration philosophy:** drift guard — bands absolute, no curving to the mean. The cohort was genuinely strong, so scores held; the report says so plainly rather than manufacturing movement.
- **Unrelated, now closed:** the session-start vault ingest (16 files) finished — all filed/deduped, `.ingest.lock` released, obsidian-vault synced. Nothing pending there.

## Repo sync note
The course-repo outputs (gradebooks, reports, this context file) and the skill edits are on disk but **not yet committed/pushed** — do that when ready (course repo for outputs; the two skills live in the Skills repo). Nothing has been pushed this session.
