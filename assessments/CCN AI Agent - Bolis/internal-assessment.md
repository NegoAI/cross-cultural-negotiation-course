# Internal Assessment — CCN AI Agent / Cross-Cultural Negotiation Strategist (Bolis)

- **Group name:** CCN AI Agent (generic cohort name; namesake **Bolis** disambiguates)
- **Project title in docs:** Cross-Cultural Negotiation Strategist
- **Drive folder:** `CCN AI Agent - Bolis` (`1z2LDIpOWTAzO4lY9eD2gSQkcuv1WWOUo`, parent "CCN Project Submission")
- **Assessment date:** 2026-06-22
- **Skill version:** cross-cultural-2026-assessment (four-dimension /400)
- **Members (from `group.md`):** Matteo Bolis, Lorenzo Bonarini, Gregorio Fino, Lorenzo Pozzi, Samuel Maria Samaritano

## File-mapping log

| Detected file | Mapped to | Confidence |
|---|---|---|
| `01_knowledge_base_cross_cultural_negotiation_agent.md` | Knowledge Base | high |
| `02_prd_cross_cultural_negotiation_strategist.md` | PRD | high |
| `03_system_instructions_v1_2_final.md` | System Instructions | high |
| `04_evaluation_report.md` | Evaluation Report (Phase 5) | high |
| `group.md` | Group manifest | high |

All five graded artefacts present. No missing files. No `.mp4` present in the folder (agent shown live; not penalised).

---

## Score summary

| Dimension | Score | Confidence |
|---|---|---|
| Domain Rigour | 91 / 100 | high |
| Generalisation | 88 / 100 | medium-high |
| Coherence of Design | 93 / 100 | high |
| Evaluation Honesty | 96 / 100 | high-medium |
| **Artefact subtotal** | **368 / 400** | — |
| Agent Quality | *instructor — live* | — |
| KB/SI separation −50 | **not triggered** | high |

---

## Domain Rigour — 91 / 100

**Confidence:** high — citation existence verified (canonical on sight; four non-canonical scholarly cites web-verified); both-halves coverage and chunk structure verified textually. Substantive accuracy of domain claims deferred to instructor.

**Evidence:**
- **Both halves of the course present and roughly balanced.** Part 1 (negotiation methodology, 5 sub-sections): positions/interests, issues & tradeable variables, objective criteria, "BATNA, reservation value, and ZOPA" (defined together), power/leverage (legal/economic/relational/informational/symbolic), individual-vs-organizational BATNA, sunk costs, integrative/distributive, logrolling, contingent agreements, anchors, table design & stakeholder mapping, sequencing, agreement architecture, disputes/escalation, and "Post-round review turns cultural hypotheses into evidence." Part 2 (cross-cultural, 6 sub-sections) covers the frameworks below.
- **Every named framework has real substance, not just a name.** Hofstede — all six dimensions named *plus the McSweeney critique*. Trompenaars — all seven dilemmas named and applied. Meyer — all eight Culture Map scales. GLOBE — includes the "as is" practices vs "should be" values distinction. Hall — high/low context plus monochronic/polychronic time. Bonus substantive frameworks beyond the rubric: World Values Survey and Ting-Toomey face-negotiation theory (own chunks).
- **Chunk discipline is strong.** Stated up front in "How to Use", every chunk carries **Principle / Explanation / Negotiation example / Source anchors / Strategic links** (the expected triad plus per-chunk anchors and cross-links), followed near-uniformly across 60+ chunks. Example (§2.5 "Ecological fallacy"): *"Principle. The ecological fallacy occurs when group-level averages are applied as if they predict individual behavior… Negotiation example. A negotiator from a country often described as indirect may communicate bluntly because of legal training, organizational culture, personal style, or frustration. Treating the national pattern as a script would produce a false diagnosis."*
- **Citation integrity high: every citation Verified, zero fabricated.** Formal Source Register (A–E) of ~30 references plus per-chunk anchors. Four non-canonical scholarly cites web-verified to exact volume/page/DOI (Ting-Toomey & Kurogi 1998 IJIR 22(2):187–225; Kirkman, Lowe & Gibson 2006 JIBS 37(3):285–320; Au 1999 JIBS 30(4):799–812; McSweeney 2002 Human Relations 55(1)).

**Why not higher:** Four canonical-list sources the course expects are **absent** — Schwartz, Earley & Ang (Cultural Intelligence), Salacuse, and the instructor's own **Rana (2015)** are not cited anywhere. Worked examples are deliberately generic/illustrative ("A supplier says…"), so the KB teaches the *pattern* rather than supplying hard case data outside Danone–Wahaha. Two anchors are effectively uncitable ("Danone Group (2007). Public statements"; "Public French convention material on Euro Disneyland"), and PON value-creation/dispute/cross-cultural sub-topics are anchored without a matching Register entry — minor traceability gaps, not fabrications.

**Flagged for instructor (substantive accuracy):** Part 2 framework characterisations (Hofstede dimensions, Meyer scales, GLOBE practices/values) are dense and accurate-looking; worth a spot read.

---

## Generalisation — 88 / 100

**Confidence:** medium-high — structural checks (exceptions as sections; framework vs axis design) reliable; "substantive multi-axis" judgement partly qualitative and partly answered by the evaluation runs.

**Evidence:**
- **The KB is framework- and region-based, not single-axis-optimised.** Cross-cultural material is organised by framework (§2.2–2.6) and by nine broad world regions (§3.2 North America, W/N Europe, S Europe, C/E Europe, East Asia, South Asia, MENA, Latin America, Sub-Saharan Africa), each with an explicit "these are not country guides" disclaimer. This is the right shape for an agent meant to handle *any* axis.
- **Exceptions are genuinely strong and mostly stand as their own sections** (the rubric's explicit test). Standalone chunks: "Culture is a distribution, not a destiny" (individual variation, §2.1); "Ecological fallacy" (§2.5); "Biculturalism and cultural frame-switching" (§2.5); "Expatriate adaptation and global professional norms" (§2.5). Generational shift and regional-within-country variation are substantive but **share one combined chunk** ("Generational, class, regional, and sector variation") rather than each having a standalone heading.
- **The evaluation demonstrates real cross-axis breadth that the KB alone understates.** Part B runs seven distinct axes/tests — Danone–Wahaha (France/China), Renault–Nissan (France/Japan), Brazil/South Korea, Canada/Tanzania, US/Indonesia, an edge-case test, and a multi-turn coherence test — showing the design is not bolted to its own test case.

**Why not higher:** Only **one** cultural axis (France/China, §3.3, 5 chunks) gets deep multi-chunk treatment inside the KB; the other two case axes are single one-chunk mentions and all country-level content otherwise lives as one-to-three-line entries inside regional palettes. Two of the six required exception types (generational, regional-within-country) are folded into a shared chunk rather than standing alone. The framework-based generalisation is real but the KB's own depth is concentrated on the anchor axis; breadth is carried more by the eval than by the KB.

---

## Coherence of Design — 93 / 100

**Confidence:** high — coherence map and KB/SI separation are reliable textual checks.

**Evidence:**

| Check | Result |
|---|---|
| PRD §3 (9 capabilities) ↔ SI §5 (workflow) | All nine capabilities (intake, fundamentals, cultural-hypothesis, stakeholder mapping, strategy/sequencing, message design, agreement architecture, post-round review, real-case simulation) traceable to SI §5 workflow steps 1–13 (+12a/b/c). ✅ |
| PRD §5 ↔ SI §6 (Output Format) | Strategy Brief, Quick tactical, Message draft, Post-round review carried across identically; SI §6 adds Real-case strategy memo (E). ✅ |
| PRD §7 ↔ SI §4 (Criteria) | PRD §7.4 self-checkable criteria carried into SI §4 positive/negative checks (concrete move, facts/assumptions split, BATNA/ZOPA, hypothesis framing, anti-stereotyping, learning loop). ✅ |
| PRD §1 ↔ SI §1 (Role) | Consistent: "Cross-Cultural Negotiation Strategist", negotiation-first, structured strategic advisor and sparring partner. ✅ |
| SI §7 examples ↔ SI §1–6 | Both worked examples obey the output formats above them, qualify cultural claims as hypotheses with caveats/tests, and avoid stereotyping (Example 2 explicitly reframes "Germans only care about rules"). ✅ |
- **KB/SI separation is clean both directions** (see scan). The SI consults the KB "by category, not by brittle section references" — exactly what the PRD §B translation note asked for.
- **Documented revision discipline.** SI carries explicit v1.1 (eval-driven rule additions) and v1.2 (Example 1 brought into compliance with the §6E format the rules mandate) notes — the change log is honest and self-consistent, and the eval's diagnosis maps one-to-one to the SI §4/§5/§6E edits applied.

**Why not higher:** Minor redundancy — the same forcing functions (fact discipline, formal-vs-practical leverage, parallel tracks) are restated across SI §4, §5 (12a/b/c), and §6E. Defensible as reinforcement, but it is mild duplication rather than perfectly factored design. The PRD declares nine capabilities mapped to its own §A traceability table; the density is high enough that a couple of capabilities (intake vs framing) overlap.

---

## Evaluation Honesty — 96 / 100

**Confidence:** high-medium — structural checks reliable; tone judgement qualitative.

**Evidence:**
- **Part A performs all four required checks as their own sections** (A1 Completeness mapping, A2 Consistency, A3 Specificity, A4 KB/SI separation) and surfaces **6 located, fix-paired findings** (table A5; rubric floor is 3). Each names a PRD/SI location and an exact fix — e.g. A1 (Medium): *"Real-case output format did not explicitly require case fact provenance"* → SI §6E add "Case fact discipline"; A4 self-catches the one separation risk (*"The Danone example includes case-specific content… the SI should remind the agent not to treat example-specific facts as general facts"*). Tone is sceptical, not self-flattering: *"They are not defective, but the real-case memo format needs a few more explicit requirements to prevent good-but-incomplete strategic outputs."*
- **Part B is a complete real-case loop.** Clear case input (B1, a fresh Danone prompt deliberately different from the SI example "because the evaluation should test the agent rather than reproduce the example"); **full** first output (~1,300 words, 13 sections — not a summary); **5-gap root-cause diagnosis** (B5) each tagged "SI gap / SI specificity gap" and tied to a named SI section's absence; **6 paste-ready SI changes** (B6) with exact rule text and target section; **full** second output (~1,500 words, 12 sections).
- **The two outputs are textually distinct — real iteration.** Output 2 adds a "Case fact discipline" section (absent in O1), splits the leverage table into "Formal" and "Practical" columns, promotes private diagnostic questions to a standalone section, and renders the learning loop as a signal→meaning→update matrix — each change implementing a specific diagnosed gap.
- **The clincher for honesty: it surfaces residual and recurring weaknesses after iteration and refuses to soften them.** Across the extra runs (B-2 to B-7) it records, verbatim, residual weaknesses *"recorded for honesty (do not soften)"* — and identifies a **cross-run recurring blind spot** found independently in B-6 and B-7 (low-cost-concession mispricing + under-worked community/local-legitimacy track). It does not conclude the agent is now perfect; its "Remaining limits" note concedes all runs share one build and KB, "so they test consistency of method, not robustness across alternative builds."

**Why not higher:** The runs are openly self-reported "development/verification-session" outputs, not a deployed-agent log (disclosed honestly, but the grader cannot confirm provenance). Appendix F asserts its citation log is fully verified; that is the group's claim, not independently re-checked here. These are honesty-of-provenance caveats, not failures — the eval is the strongest of the four dimensions.

---

## KB/SI separation scan — no violations; −50 NOT triggered

- **KB scanned for behaviour:** none found. The KB opens by policing itself — *"It is not a workflow, prompt script, tone guide, or response template… The examples are illustrative, not universal scripts."* No "the agent should…", no persona/tone directives, no response templates or decision trees. The few prescriptive sentences are negotiation-domain normativity ("a strong anchor is tied to objective criteria"), which belongs in a methodology KB.
- **SI scanned for domain knowledge:** none found. Frameworks are referenced by category as instructions to consult the KB ("Use framework names lightly and practically"), never defined inline. No country-pattern explanations, no BATNA/ZOPA definitions expanded inline, no academic citations in the SI. The two SI §7 examples are agent outputs demonstrating behaviour, explicitly framed as illustration, not standalone theory.

**Result:** 0 distinct violations, 0 structural violations → deduction not applied. Separation is model-clean, and the group caught and fixed the single example-leak risk themselves (Part A4).

---

## Citation verification (existence)

Canonical course texts marked Verified on sight. Non-canonical scholarly cites web-verified (≥1 confirming index each, exact vol/page/DOI matched).

| Citation | Status |
|---|---|
| Fisher, Ury & Patton, *Getting to Yes* (2011 ed.) | Verified (canonical) |
| Program on Negotiation (PON) — "Welcome to PON"; "BATNA 101" | Verified (canonical institution) |
| Mnookin, Peppet & Tulumello, *Beyond Winning* (2004) | Verified (canonical) |
| Raiffa, *The Art and Science of Negotiation* (1982) | Verified (canonical) |
| Raiffa, Richardson & Metcalfe, *Negotiation Analysis* (2002) | Verified (canonical) |
| Lax & Sebenius, *The Manager as Negotiator* (1986); *3-D Negotiation* (2006) | Verified (canonical) |
| Malhotra & Bazerman, *Negotiation Genius* (2007) | Verified (canonical) |
| Lewicki, Barry & Saunders, *Negotiation* | Verified (canonical) |
| Hofstede (2011), "Dimensionalizing Cultures," *ORPC* 2(1), DOI 10.9707/2307-0919.1014 | Verified (canonical) |
| House et al. (2004), *Culture, Leadership, and Organizations: The GLOBE Study* | Verified (canonical) |
| GLOBE Project — "About the Studies" | Verified (canonical institution) |
| World Values Survey Association — "What We Do" | Verified (institutional) |
| Trompenaars & Hampden-Turner, *Riding the Waves of Culture* | Verified (canonical) |
| Hall, *Beyond Culture* (1976); *The Dance of Life* (1983) | Verified (canonical) |
| Meyer, *The Culture Map* (2014) | Verified (canonical) |
| Ting-Toomey & Kurogi (1998), "Facework competence in intercultural conflict," *IJIR* 22(2), 187–225 | **Verified (web — ScienceDirect/PsycNet; pages match)** |
| McSweeney (2002), "A triumph of faith — a failure of analysis," *Human Relations* 55(1) | **Verified (web — SAGE)** |
| Kirkman, Lowe & Gibson (2006), *JIBS* 37(3), 285–320, DOI 10.1057/palgrave.jibs.8400202 | **Verified (web — Springer/RePEc; vol/issue/pages match)** |
| Benet-Martínez, Leu, Lee & Morris (2002), *J. Cross-Cultural Psychology* 33(5) | Verified (acculturation canon) |
| Berry (1997), "Immigration, Acculturation, and Adaptation," *Applied Psychology* 46(1) | Verified (acculturation canon) |
| Au (1999), "Intra-cultural Variation…," *JIBS* 30(4), 799–812 | **Verified (web — Springer/RePEc; pages match)** |
| Barboza (2009), *NYT* — Danone exits China venture | Verified (press, case context) |
| Flannery (2007), *Forbes* — "How To Lose In China" | Verified (press, case context) |
| Kurtenbach (2007), *Forbes/AP* — Wahaha-Danone feud | Verified (press, case context) |
| South China Morning Post (2007) — Danone and Wahaha | Verified (press, case context) |
| Associated Press (2023) — Renault/Nissan 15% cross-shareholdings | Verified (press, case context) |
| Le Monde (2025) — Zong Qinghou inheritance; Disneyland Paris | Unable-to-verify (recent press; case-orientation only, KB flags as "high-level chronology") |
| "Danone Group (2007). Public statements" | Unable-to-verify (no title/URL; case context only) |
| "Public French convention material on Euro Disneyland / Marne-la-Vallée" | Unable-to-verify (no author/date/title; case context only) |

**Fabricated: 0.** Unable-to-verify items are case-context press/primary anchors the KB itself flags as orientation-only, not scholarly claims. Existence checked only; attribution accuracy not assessed.

**Absent from the canonical list (noted, not penalised as fabrication):** Schwartz, Earley & Ang, Salacuse, and the instructor's own **Rana (2015)** are not cited anywhere in the KB.

---

## Coherence map (PRD ↔ SI)

| Check | Verify | Result |
|---|---|---|
| PRD §3 ↔ SI §5 | every capability → workflow step | ✅ all 9 capabilities traceable to SI §5 steps 1–13 |
| PRD §5 ↔ SI §6 | output format aligned | ✅ four PRD formats carried across; SI adds real-case memo (E) |
| PRD §7 ↔ SI §4 | self-check criteria carried into SI | ✅ §7.4 criteria → SI §4 positive/negative checks |
| PRD §1 ↔ SI §1 | role consistent | ✅ identical identity and posture |
| SI §7 ↔ SI §1–6 | examples obey the rules | ✅ both examples follow format, hypothesis-frame, anti-stereotyping |

No contradictions, no orphaned requirements, no behaviour-in-KB, no domain-in-SI.

---

## Artefact subtotal: 368 / 400

Domain Rigour 91 + Generalisation 88 + Coherence 93 + Evaluation Honesty 96. No −50 deduction.

---

## Items requiring instructor judgement

1. **Agent Quality (/100)** — score live from the presentation/demo; the grader cannot run the deployed agent. The documents promise expert-level behaviour and the eval's seven captured runs read as strong; the live run is your call.
2. **Substantive accuracy** — Part 2 framework characterisations (Hofstede/Meyer/GLOBE) are dense and accurate-looking; worth a spot read if you want to confirm.
3. **Provenance** — Part B outputs are self-reported development/verification runs, disclosed openly, not a deployed-agent log. Appendix F's citation-verification claim is the group's own; the grader independently confirmed the four highest-value non-canonical scholarly cites only.
4. **Contribution flag** — none. All five members have real, distinct described step-lead roles in `group.md`, with an explicit "all five took part in every step" note.
5. **Verdict** — deferred. Final = 368 + your Agent Quality score.

---

## Limitations

- Agent Quality is not assessed here — the instructor scores it live.
- Substantive accuracy of domain claims is not verified — only flagged.
- Citation verification is existence-only, not claim-attribution.
- Provenance of artefacts is not verified.
- Confidence ratings are heuristic, not statistical.
- Scores are set against the rubric in absolute terms; the cohort-wide recalibration pass may shift this row slightly once all groups are in.
