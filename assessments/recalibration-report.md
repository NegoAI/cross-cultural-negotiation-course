# Cross-Cultural Negotiation 2026 — Re-calibration & Self-Audit Report (Phase 2)

- **Date:** 2026-06-22
- **Cohort:** 19 groups / 89 students, all with a Phase-1 internal report and a first-pass gradebook row.
- **Scope:** the four document dimensions (Domain Rigour, Generalisation, Coherence of Design, Evaluation Honesty). Agent Quality is the instructor's, scored live, and is left empty.
- **Headline:** no major changes; one minor adjustment (Muriotto Domain Rigour 93→94). See `changes-summary.md`.
- **Method note:** the cohort was graded by ~19 **parallel** agents, not one sequential grader. So this pass re-levels **inter-agent variance** against common absolute bands — it is not correcting one grader's drift over time. Drift guard enforced throughout: bands are absolute; a genuinely strong cohort stays strong; exemplars locate the bands, they do not become a curve.

---

## 1. Calibration anchors (per dimension)

For each dimension, the clearest cohort exemplar at each band the cohort actually reaches, with the evidence that places it.

### Domain Rigour
- **96 — Exemplary (Aria/ARIA; Cross-Cultural AI Agent/NEXA).** Zero fabricated citations across a dense, precise reference set (NEXA web-verified 18 distinct non-canonical citations with matching DOIs/case numbers; ARIA grounds every methodology chunk in a real documented negotiation), both course halves cross-wired, frameworks taught *with their limits*.
- **94 — Strong (ADRELIX, Amendola, Antonucci, Biondi, Malerba, Rossi, NegotiaTe; now Muriotto).** Disciplined principle/explanation/example chunks, both halves deep, zero fabricated citations; held off 96 by minor unevenness, lighter secondary cites, or thinner regional sub-profiles.
- **88–90 — Strong-minus (Berto 90, Manno 88).** Well-sourced and chunked, but loose in-chunk attribution ("Source notes:" author-only — Berto) or governance/operating material diluting the KB as a knowledge document (Manno).
- **84 — Adequate (Negocierge/Caruso).** Content rich and correctly, even precisely sourced (archive numbers right), but the KB is a **raw concatenation of full-text sources** with no chunk architecture — the engineering, not the content, caps it.
- **66 — Failing-band (HomeGround).** No citations at all; frameworks named, not grounded; no chunk structure.

### Generalisation
- **97 — Exemplary (Aria, NEXA).** Exceptions as their own full sections (Aria: ten distinct exception types as developed chunks), multi-axis far beyond the test case.
- **88–96 — Strong (most of the cohort).** Exceptions present as their own sections (the hardest test, met); held below ceiling where axis *depth* concentrates on the anchor case or two exception types share one chunk (Bolis 88, NegotiaTe 88).
- **76 — Adequate (Negocierge/Caruso).** Genuinely multi-axis content, but with no section architecture at all in the KB there is no exceptions layer as a retrievable structure.
- **60 — Weak (HomeGround).** Exceptions only as scattered caveats; coverage is rental-practice-by-country, not cultural-axis generalisation.

### Coherence of Design
- **96 — Exemplary (Aria).** Separation explicitly architected ("the KB owns the taxonomy; the SI owns the procedural rule"), PRD↔SI near-complete, every worked example obeys the rules above it.
- **90–95 — Strong (Geroldi 94, Kira 93, Malerba 93, Bolis 93, Muriotto 92, Biondi/Antonucci/BRIDGE 91, Rossi/ADRELIX/Amendola 90).** PRD↔SI clean; only minor self-flagged residual seams (a "five capabilities" header that lists six; an "and"→"or" criterion drift; version-string drift).
- **82 — Adequate (ACROSS).** PRD↔SI logic strong, but the compiled runtime KB still carries pervasive build-time scaffolding (31 "Gaps" + 30 "Coverage" + 26 "Content-for-other-sections" blocks) — a hygiene defect *separate* from the behavioural −50.
- **74 — Adequate-minus (CCNA).** Appended "Governance Integration Patch" duplicates the Evidence Hierarchy with divergent tier counts (6 vs 7) and a stray "Claude ha risposto:" artefact ships in the SI.
- **64–66 — Weak (HomeGround 64, Negocierge 66).** Orphaned cross-document references: HomeGround's PRD/SI cite a "KB Part 1/2/3" structure the KB does not have and the PRD/SI output skeletons differ (9 vs 14 items); Negocierge's PRD describes a different agent than the SI builds.

### Evaluation Honesty
- **95–97 — Exemplary (Rossi 97, Aria 97, Kira 96, Bolis 96, Ferrandino 96, Muriotto 95, Biondi 95, Geroldi 95).** Surface a **named residual failure that survives iteration** (the hardest test) — e.g. Aria's "the fixes are verification checks bolted on after the reasoning, not a change to how it is generated"; Muriotto's self-reported density *regression* introduced by its own fix — plus full, textually-distinct first/second outputs.
- **86–93 — Strong (Caruso 93, Malerba 93, ADRELIX 92, ACROSS 91, Amendola 91, NegotiaTe 91, NEXA 90, Antonucci 89, Berto 88, Manno 86).** Real iteration and a residual surfaced, but undercut by the full second output not being reproduced (NEXA), self-flattering numeric case-scoring (Antonucci's wall of 9.6–10.0), or "done" fixes not re-tested (Berto).
- **68 — Adequate (HomeGround).** A genuine two-round iteration (its real strength) dragged by a thin Part A that does not perform the four required self-checks.

---

## 2. Net movement per dimension

| Dimension | Scores moved | Net movement | Direction |
|---|---|---|---|
| Domain Rigour | 1 of 19 (Muriotto) | +1 | flat (one upward nudge) |
| Generalisation | 0 of 19 | 0 | flat |
| Coherence of Design | 0 of 19 | 0 | flat |
| Evaluation Honesty | 0 of 19 | 0 | flat |

Total: **1 dimension-score changed across 76 dimension-scores (1.3%)**, by 1 point. One artefact subtotal moved (374→375). No −50/flag changes, no band crossings.

---

## 3. Grader self-audit — inter-agent consistency

Because grading was parallel, the audit question is not "did the grader drift early-to-late?" but "did the ~19 agents apply the same bands to the same evidence?" Finding: **yes, to a high degree.**

- **−50 trigger was applied uniformly.** Three fires, all for genuine *structural* behaviour-in-KB (HomeGround, ACROSS, CCNA). About ten near-threshold cases were all correctly held below the line, and the held-below rationale is consistent across agents: behaviour *shipped in the runtime KB* deducts; behaviour *cleaned up pre-submission* or confined to *illustrative SI examples* does not. No agent over- or under-fired relative to the others.
- **Citation discipline was uniform.** Every agent verified canonical texts on sight and web-checked the oddly-specific non-canonical ones; the result is a striking cohort-wide signal — **zero fabricated citations in 19 submissions** — reached by the same method in each report, not by one lenient or one strict reader.
- **Rankings track evidence monotonically.** Across all four dimensions, score order matches documented-evidence order; the fine 1–2 point gaps inside the 90–96 band are individually justified in each report (citation density, exception depth, residual-failure sharpness).
- **The one detectable inconsistency** was the weighting of **canonical-source absence** in Domain Rigour: the NEXA agent treated the absence of Salacuse/Schwartz/Earley & Ang/Rana as "does not hurt the score," while the Bolis agent listed the *same* four absences under "why not higher." Net materiality ≤1 point (Bolis had independent reasons — generic examples, one-axis depth — so its 91 holds). The principle is corrected in §4 and the lone +1 (Muriotto, whose 93 leaned on the mirror error of penalising responsible hedging) is applied.
- **No systematic generous/harsh agent**, and **no dimension ran hot or cold** across the cohort. Correction size: 1 point, 1 dimension. The parallel grading held together.

---

## 4. Promote-ready band refinements (paste-ready into `cross-cultural-2026-assessment`)

1. **Domain Rigour — canonical-source absence is not a deduction.** Replace any heuristic that docks for missing specific texts with: *"Do not lower Domain Rigour merely because a canonical text (Salacuse, Schwartz, Earley & Ang, Rana, etc.) is absent. Score the sourcing that IS present — citation density, precision, and whether each chunk is grounded — provided both course halves are substantively covered by other real, verified frameworks. Roster completeness is not the test."*

2. **Domain Rigour — chunk architecture is a structural requirement, not a citation by-product.** Add: *"A content-rich but UN-chunked KB (raw source-text dump with no 'How to Use', no Parts/Sections, no principle/explanation/example structure) caps Domain Rigour in the low-80s even with zero fabricated citations. 'Chunks have substance' presupposes chunks exist; verify the architecture before crediting the content."*

3. **KB/SI separation (−50) — distinguish behaviour from scaffolding, and intent from runtime impact.** Add: *"(a) Build-time scaffolding / research-process metadata left in the runtime KB ('Gaps identified', 'Coverage note', editing changelogs) is a COHERENCE/hygiene deduction, NOT a −50 separation trigger. (b) Behavioural directives that ship inside the runtime KB DO trigger −50 even if quarantined and self-labelled 'not for KB inclusion' — judge runtime impact, not authoring intent. (c) Behaviour that was leaked in an earlier draft but removed before submission does NOT trigger −50 — grade the submitted artefact."*

4. **Evaluation Honesty — 90+ requires a named, surviving residual failure.** Replace the band note with: *"Evaluation Honesty 90+ requires the eval to surface a NAMED residual failure that survives its own iteration (or a self-introduced regression) — not merely ≥3 located issues or a completed first→second loop. Self-flattering numeric case-scoring (walls of 9.5–10.0 with little downside) caps the dimension below 90 even when the prose reasoning is honest."*

---

## 5. The portable pattern (reusable asset)

**Grade each item against absolute rubric bands as it arrives → once the full set is in, re-grade against real cohort exemplars under a drift guard (exemplars locate the bands; they never become a curve) → audit the graders' own divergence (here, inter-agent variance, since grading ran in parallel) → feed exact band-text fixes back into the first-pass rubric.** The cohort's own best work calibrates the scale; the drift guard stops the mean from pulling scores in either direction. This is the generalisable grading harness — applicable to any rubric-scored fan-out where Phase 1 must commit before the comparison set exists.

---

## 6. Limitations

- Re-grading on a 19-group cohort is **judgement applied consistently, not statistics**; confidence ratings are heuristic.
- **Substantive accuracy of domain claims is still the instructor's** — citation checks were existence-only, not claim-attribution; specific framework values (Hofstede scores, within-country-variance percentages) and case figures were not verified.
- **Agent Quality is not assessed here.** The final /500 and the /30 grade cannot be computed until the instructor enters col I; the gradebook formulas complete automatically when he does (500/500 → 30/30).
- The Negocierge (Caruso) PRD-mismatch is a **data-integrity** issue requiring the instructor's confirmation of the canonical PRD, not a calibration judgement.
