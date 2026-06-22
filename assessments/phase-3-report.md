# Cross-Cultural Negotiation 2026 — Phase 3 Review (post-decision consistency pass)

- **Date:** 2026-06-22 (after lunch)
- **Trigger:** instructor decisions on the four bottom groups — (1) accept Negocierge's corrected PRD; (2) recharacterise the KB/SI behavioural leak as a forgivable packaging slip for ACROSS and HomeGround, waiving the −50; (3) keep a reduced **−10** for CCNA because it diagnosed the leak itself and shipped it unfixed.
- **Scope:** This is a **ripple/consistency audit of the four changed groups against Phase 2's still-current deep recalibration**, not a third full re-read of all 19. Phase 2 re-graded the whole cohort against absolute bands earlier today and nothing about the 15 unchanged groups has changed; re-reading them from Drive again would be redundant. What *can* drift is whether the four new numbers still sit correctly relative to those 15 — that is what this pass checks.

---

## 1. The four changes

| Group (namesake) | Phase 2 /400 | Phase 3 /400 | What changed |
|---|---|---|---|
| Negocierge (Caruso) | 319 | **343** | Corrected PRD now on Drive (Negocierge, 5 capabilities, seniority calibration, §7 incl. the 2-minute-scan criterion). All four PRD↔SI coherence FAILs flip to PASS → Coherence 66→90. DR/Gen/EvH unchanged. |
| ACROSS (Belfrond) | 308 | **358** | −50 behavioural-leak penalty waived (blocks were self-labelled "not for KB"; pure un-stripped-compile-step). |
| CCNA (Manno) | 288 | **328** | −50 reduced to −10 (KB-embedded workflow + output-selection logic; diagnosed in their own Part A and shipped unfixed). |
| HomeGround (Uysal) | 208 | **258** | −50 behavioural-leak penalty waived. |

These changes revise one of Phase 2's promote-ready band rules: refinement **#3(b)** ("behavioural directives that ship inside the runtime KB DO trigger −50 even if quarantined and self-labelled — judge runtime impact, not authoring intent"). The instructor's call softens this to: **a labelled/packaging leak is forgiven; a *known and unremediated* leak is penalised, but lightly (−10).** That is a deliberate, consistent override, applied the same way to all three penalised groups. Recommend updating the assessment skill's rule #3(b) to match, so a future cohort is graded on the same principle.

The discriminator now in force, stated cleanly for the record:
- **ACROSS** — intent correct (every behavioural block labelled "belongs in SI"), failed only at the compile/strip step → **no penalty** (packaging slip).
- **HomeGround** — did not catch it, but the KB's weakness (no citations, behavioural tables, no chunking) is **already priced into its low dimension scores** (DR 66 / Gen 60 / Coh 64); a separate −50 double-counts → **no penalty**.
- **CCNA** — **diagnosed the exact leak in its own Part A** (finding #9: "remove behavioural instructions from the KB") and submitted without fixing it; its dimension scores are high (88/90/74/86) so nothing else reflects the defect → **−10**, the one case a penalty does real, non-duplicative work.

This rule holds together: it penalises *known-and-ignored* leakage specifically, not honest mistakes.

---

## 2. The one genuine consistency question the changes expose — ACROSS Coherence 82

**This is the headline Phase 3 finding and it needs an instructor decision.**

Phase 2 deliberately split ACROSS's two build-hygiene failures (recalibration report §1, Coherence anchor + §4 refinement #3a):
- **Behavioural blocks** in the KB (10 "Notes for System Instructions") → the **−50** (now waived as a packaging slip).
- **Research scaffolding** in the KB (31 "Gaps identified" + 30 "Coverage note" + 26 "Content-for-other-sections" blocks) → an **~8-point Coherence ding**, landing ACROSS at **82** instead of the ~90 its strong PRD↔SI logic would earn.

Both failures have the **same root cause**: ACROSS shipped a runtime KB without running a clean compile/strip step. We have now decided that root cause is a forgivable packaging slip for the *behavioural* half. The question: **is it consistent to keep docking ~8 Coherence points for the *research-scaffolding* half of the very same slip?**

- **Argument to lift it** (recommend ~82→~88, ACROSS → ~364): one packaging miss, one leniency. Having forgiven the more serious behavioural leak, penalising the milder cosmetic clutter from the same un-run compile step is internally inconsistent. ACROSS's DR 92 / Gen 93 are genuinely top-band (its exceptions layer is model-grade); only this hygiene ding holds it below the main cluster.
- **Argument to hold 82:** the research scaffolding is a real document-cleanliness defect that a deployed agent reads, and Phase 2 always treated it as a *separate, legitimate* Coherence matter (not part of the −50). Forgiving the behavioural penalty doesn't oblige forgiving every cosmetic flaw. Document cleanliness is a fair quality bar.

**My recommendation: a partial lift, 82 → 87 (ACROSS → 363).** It applies the same leniency that drove the waiver without pretending the KB shipped clean. Either way is defensible — your call. (If you lift it, I re-run; nothing else moves.)

No other group has this double-exposure: CCNA's Coherence 74 is for a *distinct* defect (the SI's self-contradicting governance patch, 6-vs-7 tier counts), unrelated to its KB leak, so its 74 stands and is not double-counting the −10.

---

## 3. Did any changed group's *other* dimensions need revisiting? (checked — no)

- **Negocierge Generalisation 76.** Phase 2 partly justified this by "the strongest exceptions articulation lives in the PRD that does not match this agent." With the PRD now matching, does Gen rise? **No.** The binding constraint on Gen 76 was always the KB itself — a raw source-text dump with *no section architecture*, hence no retrievable exceptions layer. The corrected PRD adds a cultural-generalisation guardrail in *its own* §6, but it does not add an exceptions layer to the KB the agent retrieves. Gen 76 holds. (DR 84 likewise — the raw-dump-KB cap is independent of the PRD.)
- **Negocierge Coherence 90.** Sits correctly against peers at the same band — B.R.O. 90 (and→or drift), ADRELIX 90, Rossi 90 — and is held off higher by one real residual: the SI addresses the KB as if it has named sections ("the Power Distance section of the KB") that don't exist as retrieval units in the raw dump. Consistent.
- **ACROSS / CCNA / HomeGround dimension scores** were never tied to the penalty; they are unchanged and remain correctly placed.

---

## 4. New cohort ranking (document side /400, pre–Agent Quality)

| Rank | Group (namesake) | DR | Gen | Coh | EvH | Penalty | /400 |
|---|---|---|---|---|---|---|---|
| 1 | Aria agent (Dell'Orto) | 96 | 97 | 96 | 97 | — | 386 |
| 2 | CROSSBRIDGE AI (Geroldi) | 96 | 96 | 94 | 95 | — | 381 |
| 3 | Cross-Cultural Kira Agent (Monaco) | 95 | 96 | 93 | 96 | — | 380 |
| 4 | Cross-Cultural Neg Advisor (Ferrandino) | 93 | 95 | 94 | 96 | — | 378 |
| 5 | B.R.O. (Rossi) | 94 | 96 | 90 | 97 | — | 377 |
| 6= | Kairos (Malerba) | 94 | 95 | 93 | 93 | — | 375 |
| 6= | CCN AI Agent (Muriotto) | 94 | 94 | 92 | 95 | — | 375 |
| 8 | CultureBridgeAI (Biondi) | 94 | 93 | 91 | 95 | — | 373 |
| 9 | Cross-Cultural AI Agent / NEXA (Longo) | 96 | 97 | 88 | 90 | — | 371 |
| 10 | ADRELIX (Taferner) | 94 | 93 | 90 | 92 | — | 369 |
| 11= | CCN AI Agent (Bolis) | 91 | 88 | 93 | 96 | — | 368 |
| 11= | CCN AI Agent Culturae (Amendola) | 94 | 93 | 90 | 91 | — | 368 |
| 13 | CCN AI Agent (Antonucci) | 94 | 93 | 91 | 89 | — | 367 |
| 14 | NegotiaTe (Seghezzi) | 94 | 88 | 89 | 91 | — | 362 |
| 15 | the BRIDGE (Berto) | 90 | 92 | 91 | 88 | — | 361 |
| 16 | ACROSS (Belfrond) | 92 | 93 | 82 | 91 | — | 358 *(→363 if Coh lifted to 87)* |
| 17 | Negocierge (Caruso) | 84 | 76 | 90 | 93 | — | 343 |
| 18 | CCNA (Manno) | 88 | 90 | 74 | 86 | −10 | 328 |
| 19 | HomeGround (Uysal) | 66 | 60 | 64 | 68 | — | 258 |

**Distribution read:** 15 groups in a tight 361–386 band; ACROSS just under it at 358 (held only by the Coherence hygiene ding in §2); Negocierge at 343 (raw-dump KB); CCNA at 328; HomeGround the sole genuine outlier at 258 (no citations — qualitatively weaker, not just penalised). The ranking is monotonic with the documented evidence at every step. The document-side compression is real and expected for a strong cohort; **Agent Quality (the instructor's live /100) is what will spread the final /500.**

---

## 5. Self-audit

- **Did the penalty changes break monotonicity?** No. Each group's place tracks its evidence; the three formerly-penalised groups now sit on raw quality (ACROSS strong, CCNA strong-with-a-real-coherence-mess, HomeGround weak), which matches their reports.
- **Is the −10-only-for-CCNA rule applied consistently?** Yes — it keys on *known-and-unremediated* (self-diagnosed in their own eval), a property ACROSS and HomeGround do not share.
- **One open inconsistency surfaced and flagged, not silently resolved:** ACROSS Coherence 82 (§2) — left for instructor decision rather than auto-adjusted, because it is a judgement about how far the packaging-slip leniency extends, not a clerical error.
- **Drift guard held:** no score was moved to smooth the distribution; the only proposed change beyond the instructor's four is the §2 ACROSS Coherence question, and it is argued from consistency, not from curving.
- **Not re-verified (unchanged from Phase 2 limitations):** substantive accuracy of domain claims; Agent Quality; the /30 mapping floor/lode question.

---

## 6. Actions

1. **Done:** Negocierge 343 (Coherence 66→90, flag cleared, comment rewritten); ACROSS −50 waived; HomeGround −50 waived; CCNA −50→−10 with the deduction named in its comment. Build script `_build_gradebook_final.py` updated (penalty field now numeric); CSV regenerates on next run.
2. **Needs instructor decision:** ACROSS Coherence 82 → ~87 (§2). Recommended.
3. **Recommended skill update:** revise `cross-cultural-2026-assessment` band rule #3(b) to the new leniency principle (§1) so a future cohort is graded the same way.
