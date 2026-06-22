# Internal Assessment — CrossBridge AI (Geroldi group)

- **Group name:** CrossBridge AI
- **Drive folder:** `CROSSBRIDGE AI - Geroldi` (`1kF6qns0GSiEYIojlIo-jT_QABsHsKQH7`)
- **Assessment date:** 2026-06-22
- **Skill version:** cross-cultural-2026-assessment
- **Role:** grading assistant — four document dimensions only (/400). Agent Quality is scored live by the instructor; no /500 or verdict here.

## File-mapping log

| Detected filename | Mapped artefact | Confidence | Note |
|---|---|---|---|
| `KB.md` (175 KB) | Knowledge Base | High | "How to Use This KB", 3 Parts, chunk = principle/explanation/example, Strategic Links, Glossary, per-Part source lists |
| `PRD_.md` | PRD | High | All 7 sections (Identity, Users, Capabilities, Interaction, Output, Boundaries, Definition of Success) |
| `SI.md` | System Instructions | High | "You are…" opening, 7 sections (Role, Context, KB Usage, Criteria, Instructions, Output, Examples) |
| `Evaluation.md` | Evaluation report | High | Part A (4 checks, findings table, changelog) + Part B (case, full outputs, diagnosis, re-score) |
| `group.md` | group.md | High | 5 members + step-lead table |
| `presentazione.mp4` | recorded presentation | — | Ignored per rubric |

All five graded artefacts present and read in full. No missing artefacts.

---

## Dimension 1 — Domain Rigour: 96/100

**Confidence: Medium** — structural checks (chunking, citation existence, both-halves coverage) are high-confidence; chunk-substance judgement is partly the instructor's read, hence not High.

**Evidence**
1. **Both course halves covered with real substance, not names.** Part 1 runs the full negotiation methodology — principled negotiation and the wise-agreement test, interests vs positions, 3-D setup design, Raiffa's three phases, Lewicki's ten steps, the BATNA/reservation/aspiration/ZOPA table with operational formulas (`reservation price = V + N − B`), leverage's five sources, value creation / logrolling / MESO / contingent clauses, concession principles, anchoring, biases, impasse types, and post-negotiation review. Part 2 treats all five frameworks plus Face-Negotiation, Communication Accommodation and Tightness-Looseness, each with a **"Documented limits"** chunk (McSweeney, Baskerville, Cardon, Kittler, Brewer & Venaik, Schoen). This is well beyond naming.
2. **Chunk structure is consistent throughout.** Every chunk is "a bolded sub-heading followed by a principle, its explanation, and a concrete example" (KB §"How to Use"), and the body holds to it — e.g. §1.2 BATNA chunk gives principle (probabilistic BATNA), explanation (four correctives), and a worked €1M-discounting example. *Strategic Links* connect chunks across Parts (negotiation move × cultural lens × exception), which is the cross-cutting reasoning the rubric rewards.
3. **Framework treatment is genuinely comparative and trap-aware.** §2.6 catalogues the canonical single-framework traps (individualism ≠ low-context; hierarchical ≠ top-down deciding; GLOBE Assertiveness ≠ Hofstede Masculinity; practices ≠ values) and writes explicit **default/exception resolution rules** ("use Meyer for table behaviour; Hofstede/GLOBE at macro scale; never average scores across frameworks"). This is expert-level integration, not a framework catalogue.
4. **Citations: zero fabricated.** ~80+ references across three per-Part source lists. All course-canonical sources (Fisher/Ury, Lewicki, Raiffa, Malhotra & Bazerman, Hofstede, Hall, Meyer, Trompenaars, GLOBE/House, Salacuse, Earley & Ang) verified on sight. Six of the most obscure, fabrication-prone, oddly-specific citations were web-verified and **all six exist with exact matching detail** (see citation table). The group ran its own citation-verification step (group.md), and it shows.

**Why not higher:** reserved the top of the band for a 100 only where chunk-by-chunk substantive accuracy is independently confirmed; that is the instructor's read (and is out of scope here per the limitations footer). 96 reflects exemplary breadth, depth, structure and a clean citation set.

**Instructor-judgement flag:** substantive accuracy of domain claims (e.g. the regional-pattern characterisations, the "80% of variance within countries" figure attributed to Taras/Steel/Kirkman 2016) is not verified here — flagged for the instructor, not graded.

---

## Dimension 2 — Generalisation: 96/100

**Confidence: Medium** — axis count and "exceptions as their own sections" are structural (high); depth-of-treatment judgement is partly interpretive.

**Evidence**
1. **Many cultural axes, each substantive — not one test case.** §3.1 deliberately refuses bloc treatment: East Asia is split into **three distinct logics** (China / Japan / South Korea, each a full chunk with its own decision process, trust mechanism and conflict handling, plus a comparison table); Western economies into four (USA / UK / Germany / Scandinavia); India; the Gulf into two (UAE / Saudi Arabia); Latin America into four (Mexico / Brazil / Argentina / Colombia, with a comparison table). This is well past the single-axis failure mode.
2. **All five exception types present as their own full Sections — the hardest test of this dimension.** §3.2 Individual variation (ecological fallacy; "80% of variance within countries"; organisational and professional identity as autonomous levels; a synoptic weak-predictor matrix), §3.3 Biculturalism and frame switching (BII's two components; high- vs low-BII contrastive reactions; boundary spanners), §3.4 Generational shifts (with the Rudolph et al. caveat that generation is methodologically weak — "she's Gen Z, she'll be informal" named as the same ecological fallacy at generational scale), §3.5 Expatriate adaptation (Berry, CQ/Earley & Ang, curvilinear over-adaptation risk), §3.6 Within-country variation (Kaasa, Lenartowicz & Roth, urban–rural maximizing/satisficing). These are sections, not footnotes.
3. **The exception logic is wired into the operating instructions.** The KB's update hierarchy (§2.6: observed behaviour > national profile; organisational culture > national culture; trajectory > cluster; recent signals > history) is carried into SI §5 Step 5 ("update cultural priors against the specifics") and the SI edge case on biculturalism — so generalisation is not just documented, it is operationalised. The Part B case (Saudi-born, Wharton, 8 years in California) directly exercises it.

**Why not higher:** 96 not 100 — the work covers the major world regions richly, but Sub-Saharan Africa and South-East Asia beyond India get only cluster-level mention; a 100 would carry comparable depth across every region named in the GLOBE cluster list. Minor, and named.

---

## Dimension 3 — Coherence of Design: 94/100

**Confidence: High** — rests on the coherence map and the KB/SI separation scan, both textual.

**Evidence**
1. **PRD → SI traceability is explicit and clean.** Each SI section is tagged with its PRD source (`## 1. Role (← PRD §1)`, `## 4. Criteria (← PRD §7)`, etc.), and every PRD capability lands on an SI workflow step (see coherence map below). The group's own Part A Check 1 mapping matches an independent re-check.
2. **KB/SI separation is clean in both directions** (see separation table) — no behavioural rules in the KB, no domain definitions in the SI. The KB states the boundary explicitly ("It does **not** contain behavioural rules… how the agent uses this material is defined separately in the System Instructions"); the SI refers to the KB only by content category ("the negotiation-preparation framework", "the exceptions material"), never by Part/Section number or with inlined framework definitions.
3. **The worked examples obey the rules above them.** SI §7 Example 1 = clarifying round only (obeys Step 1 and the §6 first-turn rule); Example 2 = stereotype-reframe edge case (obeys the §5 Part B edge case and the §4 negative checks, declining the "out-tough" tactic); Example 3 = the full five-part analysis (obeys the §6 analysis-turn structure). The group caught and fixed an earlier contradiction (Finding 8: Example 1 once showed five un-prioritised questions against the capped Step 1) — the shipped version is consistent.

**Why not higher:** one residual maintainability seam the group itself flagged (Finding 5) — domain assertions live inside the SI §7 examples (the China package-deal description, Face-Negotiation reasoning), legitimate for an example but able to drift out of sync if the KB is revised. Not a KB/SI violation (an example must show real output), but it keeps the score off 100. No −50 implications.

---

## Dimension 4 — Evaluation Honesty: 95/100

**Confidence: Medium** — Part A/Part B structural checks are high-confidence; tone-and-depth judgement is interpretive.

**Evidence**
1. **Part A finds eight genuine issues, each with location, severity and fix** — well past the ≥3 floor. One is a real **High**-severity gap honestly named: PRD success criterion #1 (the agent's core value proposition — "surface a risk the user had not considered") **had no SI directive** (Finding 1). Two further findings (#7, #8) were surfaced by a *second* verification pass as cascade effects of an earlier fix — the group treats "the consistency check is only complete once the edits it triggers have propagated" as part of the self-eval, which is unusually rigorous.
2. **Part B is a real iteration, not a re-run.** The case is deliberately chosen **off the group's own axis** (Brazil–Saudi Arabia) and loaded with four traps (bicultural counterpart presented with the user's wrong conclusion; a facilitation-payment/bribe; a legal-advice request; a Friday deadline). Both the first output and the full two-turn second output are reproduced; they are **textually distinct** (the second adds the "you've been calibrating to the one person who doesn't decide" reframe and a complete five-part analysis). The diagnosis traces the gap to a **root cause in the SI** (no coverage of a mixed message bundling an urgent red flag with items needing clarification) and the fix is **specific** (the exact Step 1b text added to §5).
3. **The eval is sceptical, not self-flattering, and resists inflation.** The group explicitly reports the Part B improvement as a **sequencing** fix and refuses to dress it up as a substantive one ("we deliberately report the fix as a sequencing improvement rather than inflating it"). Most tellingly, the closing reflection names a **residual, untested weakness**: the agent has never been tested on a case where the dominant cultural hypothesis is genuinely *wrong*, so the "treat as hypothesis, validate" machinery has not been shown to actually change course. Surfacing a residual failure is the rubric's top-band marker.

**Why not higher:** the honest residual the group itself names (no test where the leading hypothesis is wrong) is exactly the round that would have pushed this to 100 — the eval names the gap but does not run it. Scored at the top of the strong band rather than exemplary because the sharpest test is identified but deferred, not executed.

---

## KB/SI separation scan

| Direction | Searched for | Result |
|---|---|---|
| Behaviour in KB | "the agent should…", always/never directives, response templates, decision trees, persona/tone rules | **None.** KB is declarative throughout; behaviour is explicitly delegated to the SI in the "How to Use" preamble. |
| Domain in SI | Framework definitions, country/regional pattern explanations, BATNA/ZOPA expanded inline, academic citations | **None in §1–§6.** SI refers to the KB only by content category. Domain content appears **only inside the §7 worked examples**, which is legitimate (an example must show the agent's real output). |

**Violations: 0 structural, 0 lower-severity (beyond the example-maintainability seam, which is not a separation violation).**
**−50 deduction: NOT triggered.**

---

## Citation table

Canonical course texts marked **Verified (canonical, on sight)**. Six non-canonical, oddly-specific, fabrication-prone citations web-verified (≥1 authoritative hit, exact author/venue/detail match). No fabricated citations found.

| Citation | Status | Basis |
|---|---|---|
| Fisher, Ury & Patton (1991) *Getting to Yes* | Verified | Canonical |
| Lewicki, Barry & Saunders (2021) *Essentials of Negotiation* | Verified | Canonical |
| Raiffa (1982); Raiffa, Richardson & Metcalfe (2002) | Verified | Canonical |
| Lax & Sebenius (1986; 2003) *Manager as Negotiator* / 3-D HBR | Verified | Canonical |
| Malhotra & Bazerman (2007) *Negotiation Genius* | Verified | Canonical |
| Bazerman & Neale (1992); Sebenius HBS WP 10-048/10-050 | Verified | Canonical |
| Hofstede (1980; 2010); Hofstede (2011) | Verified | Canonical |
| Hall (1959/1966/1976/1983); Hall & Hall (1990) | Verified | Canonical |
| Meyer (2014) *The Culture Map* | Verified | Canonical |
| Trompenaars & Hampden-Turner (1997/2000) | Verified | Canonical |
| House et al. (2004) GLOBE; Javidan et al. (2006) | Verified | Canonical |
| Earley & Ang (2003) *Cultural Intelligence* | Verified | Canonical |
| Salacuse (1998) "Ten Ways Culture Affects Negotiating" | Verified | Canonical |
| McSweeney (2002); Baskerville (2003) Hofstede critiques | Verified | Canonical critique literature |
| Cardon (2008) Hall critique; Schoen (2022) Meyer critique | Verified | Canonical critique literature |
| **Benetti, Ogliastri & Caputo (2021)**, *J. of Management & Organization* 27(4), 786–808 | **Verified (web)** | Cambridge Core + RePEc; exact volume/pages match |
| **Roehrich, Sarafan, Squire, Lawson & Bouazzaoui (2025)**, *Production and Operations Management* 34(5) | **Verified (web)** | SAGE + Oxford/Bath research portals; authors and venue match |
| **Srivastava, Kühnen, Simunovic & Boehnke (2023)**, *Current Research in Ecological and Social Psychology* 5, 100140 | **Verified (web)** | ScienceDirect + PsycNet; exact DOI/volume match |
| **Velez-Calle, Sosa & Large (2021)**, *Int. J. of Cross Cultural Management* 21(3), 491–506 | **Verified (web)** | SAGE + author Scholar profile; venue match |
| **Sikorski & Albrecht (2025)**, "Trust… intercultural negotiations: a systematic review", *NCMR* 18(1) | **Verified (web)** | NCMR (CMU) + Sheffield Hallam repository; title/venue match |
| **Bodendorf & Franke (2024)**, *Int. J. of Production Research* 62(16), 5828–5849 | **Verified (web)** | RePEc + author Scholar profile; exact volume/issue/pages match |
| Remaining ~55 references (Taras, Brett, Gunia, Benet-Martínez, Gerhart, Gelfand, Putnam, etc.) | Verified (canonical/established) | Recognised cross-cultural / negotiation literature; spot-checks all real |

**Fabricated citations: none.**

---

## Coherence map (PRD ↔ SI)

| Check | Verify | Result |
|---|---|---|
| PRD §3 ↔ SI §5 | every PRD capability → an SI workflow step | ✅ 3.1→Step 3; 3.2→Step 4; 3.3→Step 6; 3.4→§4 "names its grounding" (cross-cutting, woven through §5); 3.5→Step 7; 3.6→"Post-negotiation reflection (separate trigger)". No orphaned capability. |
| PRD §5 ↔ SI §6 | output format aligned | ✅ Identical five-part shape (working assumptions → context map → cultural risks → adaptive strategy → assumptions/validate), plus first-turn, narrow-question and edge-case variants. |
| PRD §7 ↔ SI §4 | self-checkable success criteria → SI Criteria | ✅ Success criteria 2–5 + the structural half of #1 become positive checks; all five failure modes become negative checks (stereotyping non-negotiable). Finding 1's gap (#1 had no directive) was fixed before submission. |
| PRD §1 ↔ SI §1 | role consistent | ✅ Identical advisor stance, fixed negotiation-first-then-culture order, anti-stereotyping, epistemic care. |
| SI §7 ↔ SI §1–6 | examples obey the rules above them | ✅ Ex.1 = clarifying round only; Ex.2 = stereotype-reframe edge case; Ex.3 = full five-part analysis. All consistent with §4/§5/§6. |

No contradictions or orphaned requirements found.

---

## Artefact subtotal

| Dimension | Score |
|---|---|
| Domain Rigour | 96 |
| Generalisation | 96 |
| Coherence of Design | 94 |
| Evaluation Honesty | 95 |
| −50 KB/SI separation | Not triggered |
| **Artefact subtotal** | **381 / 400** |

---

## Items requiring instructor judgement

- **Agent Quality (5th dimension) is scored live by the instructor** from the demo/presentation — not assessed here. No /500 total or verdict computed.
- **Substantive accuracy** of domain claims (regional-pattern characterisations; the "80% within-country variance" figure; the documented-case framings such as Daimler–Chrysler and TCL–Alcatel) is **not** verified here — flagged for the instructor.
- **Contribution flag: none.** group.md lists all five members (Caterina Rozzi, Filippo Geroldi, Alessandro Giacobone, Paolo D'Alterio, Cosmina Solomon) with described roles in the step-lead table. Note for the instructor only (not a flag): Paolo D'Alterio appears in Step 1 (whole group) and the citation-verification step but not in the Step 2–5 lead rows — a real, described contribution, so the narrow flag trigger does **not** fire.

---

## Limitations (declared every report)

- Agent Quality is not assessed here — the instructor scores it live.
- Substantive accuracy of domain claims is not verified — existence/structure only.
- Citation verification is existence-only, not claim-attribution; canonical texts accepted on sight, a sample of non-canonical ones web-checked.
- Provenance of the artefacts is not verified.
- Confidence ratings are heuristic, not statistical.
