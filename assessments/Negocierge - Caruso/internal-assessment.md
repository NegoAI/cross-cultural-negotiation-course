# Internal Assessment — Negocierge (folder: `Negocierge - Caruso`)

**Group name:** Negocierge
**Drive folder:** `1LSSTQZRZ-itiQOGtlTB_539huaW8JIB4` (parent: CCN Project Submission)
**Assessment date:** 2026-06-22
**Skill version:** cross-cultural-2026-assessment (4 document dimensions /400; Agent Quality left to instructor)
**Assessor:** grading assistant (documents only)

> **Note — this supersedes an earlier draft of this file.** A previous pass graded an *earlier version* of this submission (KB ≈1.0 MB / 9 sources with Meyer, Voss, Gesteland, Salacuse absent; a Negocierge-titled "advisor" PRD with an embedded second evaluation). The files currently on Drive have been **revised**: the KB is now 3.85 MB / 19 sources and **does** contain Meyer, Voss, Gesteland, Salacuse, Sebenius, Wasta; the PRD has been **replaced** by a different document titled *ARIA* (see cross-cutting flag). This assessment grades the **current** files. Score movement vs the earlier draft is a consequence of the changed submission, not of regrading the same artefacts.

---

## File-mapping log

| Detected file | Mapped artefact | Confidence | Note |
|---|---|---|---|
| `PRD.md` (53.7 KB; 68.8 KB decoded) | **PRD** | High (structure) / **see flag** | 7-section PRD, but it describes a *different agent* — **ARIA** (7 capabilities, advisor model). 181 "ARIA" mentions, 0 "Negocierge". NOT the Negocierge described everywhere else. Ends cleanly at §7; no embedded evaluation. |
| `System-Instructions.md` (38.7 KB) | **SI** | High | "You are **Negocierge**…", 7 sections (Role, Context, KB Usage, Criteria, Instructions, Output Format, Examples). v1.1. |
| `5-evaluation.md` (29.3 KB) | **Evaluation** | High | Part A (4 checks) + Part B (case, two full outputs, diagnosis, fixes). For *Negocierge*. |
| `Knowledge-Base.md` (3.85 MB) | **KB** | High | Raw concatenated full-text source documents with 130 `[[KB-FONTE:…]]` source tags (19 unique sources). |
| `group.md` (728 B) | **group.md** | High | 5 members + step leads. |
| `VideoGuidato.mov`, `VideoFree.mov` | presentation | — | Ignored per rubric (treated as `.mp4` equivalents). |

**No artefact missing.** All five graded artefacts present. The PRD↔rest identity mismatch is treated as a coherence defect, not a missing-file deduction.

### Cross-cutting flag — the submitted PRD is for a different agent (ARIA, not Negocierge)

This is the single most consequential finding and it drives the Coherence score.

- The **PRD** (`PRD.md`) is titled *"Cross-Cultural Negotiation Agent — ARIA"* ("AI Advisor for Relational and Intercultural Analysis"). It specifies **seven** capabilities (Position Analysis, Cultural Context, Stakeholder/Decision Structure, Pre-Session Plan, Cultural Risk, Value Creation, Post-Negotiation Debrief), an **advisor** model that explicitly *"does not adopt a counterposition or argue for the sake of stress-testing"*, **no seniority calibration**, and a §7 built from `SC-1…SC-7` / `FM-1…FM-6`.
- The **SI**, **Evaluation**, and **group.md** all describe **Negocierge**: **five** capabilities (Cultural Profile & Levers, Stakeholder Map, Cultural Risks, Pressure-Testing, Offer Letter), a **sparring-partner / challenger** register, and a **senior/junior seniority calibration** (50/50 vs 60/40 content split) that is the spine of the design.
- The Evaluation's Part A maps against a *Negocierge* PRD that does not exist in this folder: it cites *"PRD §3.1–§3.5"* capabilities, *"PRD §4.0 Seniority-Based Calibration"*, and *"PRD §7 Criterion 4 … scannable in under 2 minutes / no explanations of BATNA, ZOPA, etc."* — **none of which appear in the submitted ARIA PRD** (ARIA §7 is SC/FM, has no seniority requirement, no 2-minute-scan criterion).

Reading: the group iterated through an earlier design (an advisor PRD, then ARIA) to the delivered agent (Negocierge) and, in the revision that expanded the KB, **left a non-matching PRD attached** — most likely ARIA was a parallel/earlier concept and the correct Negocierge PRD was never re-uploaded. The SI and Evaluation are internally consistent with each other and are clearly the live design; the PRD is an orphan. This breaks the PRD↔SI traceability the rubric scores under Coherence. The instructor should confirm which PRD is canonical before the live score — if a matching Negocierge PRD exists and was simply not uploaded, the Coherence score here is conservative.

---

## Dimension 1 — Domain Rigour — **84 / 100**

**Confidence:** Medium (citation existence is High; KB-architecture and chunk-substance judgement needs the instructor's read).

**Evidence**

1. **Both halves of the course are covered, with real depth.** Negotiation methodology: *Getting to Yes* (Fisher/Ury/Patton) in full, Lewicki *Essentials* (TOC + chapters), Wheeler's HBS *Negotiation Analysis* note, Voss *Never Split the Difference*, Foo/Elfenbein/Tan/Aik on EI and the create/claim-value tension. Cross-cultural: Hofstede (272 mentions, via the Kirkman/Lowe/Gibson 25-year review), Trompenaars *Riding the Waves* (256), Meyer *Culture Map* 8 scales (FONTE-tagged; "Culture Map" ×18, "Meyer" ×30), Hall mono/polychronic (204), Salacuse's ten factors (62), Sebenius *Assess, Don't Assume* (47) with the four cross-cultural fallacies, Gesteland country profiles (21).
2. **Every citation is real and verifiable — zero fabricated (see citation table).** The non-canonical sources are not only real but precisely cited: Musso's guanxi paper carries the correct archive number (MPRA 31642), the Bălan Trompenaars/Romanian-students paper matches the 7th International Management Conference (Bucharest 2013), Darley/Luethge/Blankson matches *Journal of Global Marketing* 26:4 (2013). Unusually careful sourcing.
3. **Regional negotiation coverage is substantive, not nominal:** Arab world via *wasta* (178+51 mentions; Weir/Sultan/Van de Bunt); China via *guanxi* (Musso); Japan via *ringi/nemawashi* (Adair/Brett/Okumura US–Japan study); Sub-Saharan Africa (Darley; Dieng ADR); Latin America and Northern Europe (Gesteland).
4. **The one custom-authored chunk is well-built.** The `Nego Agent — addendum interno` deal-design insertion ("Decouple bundled issues through structural separation…") is a clean principle → explanation → worked-example (IP ring-fencing vs governance) chunk — exactly the structure the rubric rewards.

**What holds the score below the top band:** the KB is **not a designed, chunked KB** — it is raw full-text source documents concatenated, with `[[KB-FONTE]]` attribution tags marking the seams. There is **no "How to Use This Knowledge Base" section, no Parts/Sections scaffolding, and no principle/explanation/example chunk architecture** across the body (only 14 markdown headings in 3.85 MB, all from a single source document; the apparent "How to Use" hit is the phrase "When and How to Use Third-Party Help" inside Lewicki's TOC). The SI repeatedly addresses the KB as if it were structured — "the Power Distance section of the KB", "Meyer's Trusting scale section of the KB", "the KB's conflict-resolution guidance", "regional negotiation patterns in the KB" — but those addressable sections do not exist as labelled retrieval units; the agent must find them inside book-length raw text. The domain *content* is rich, complete, and correctly sourced (strong band); the domain *engineering* of the KB is thin (raw dump), which is what keeps this out of 90+.

**Instructor-judgement flag:** substantive accuracy of the regional/framework claims is not verified here (existence-only on citations). The raw-dump KB is heavy (~3.8 MB) and may strain retrieval — worth probing live.

---

## Dimension 2 — Generalisation — **76 / 100**

**Confidence:** Medium (axis-counting is structural; "exceptions as their own sections" is partly judgement against a non-sectioned KB).

**Evidence**

1. **Multiple cultural axes covered substantively**, each with its own sourced regional/framework treatment: East Asia (China guanxi; Japan ringi/nemawashi), Arab world (wasta), Sub-Saharan Africa (Darley; Dieng), Latin America and Northern Europe (Gesteland), plus the framework axes themselves (Hofstede dimensions, Trompenaars' 7, Meyer's 8, Hall mono/polychronic). Comfortably multi-axis — it does not collapse to the group's own test case.
2. **The design treats culture probabilistically, not deterministically.** SI §4 negative check: *"Never produce absolute or deterministic statements ('the Chinese always…', 'Arabs never…'). Cultural tendencies are probabilistic patterns… Every generalisation must be qualified with context."* SI Example 2 is a dedicated anti-stereotype turn. The (orphaned) ARIA PRD also carries a full "Cultural Boundaries" section (ecological fallacy, biculturalism, frame-switching, situational strength) — the group understands the exceptions deeply.
3. **The live Part B case actively stress-tests biculturalism** (Tanaka: Stanford MBA + traditional hierarchy) and the agent handles it well — "calibrate to the man, not the country average."

**What holds it down:** the rubric wants the **exceptions present as their own KB sections** — individual variation, biculturalism, generational shift, expatriate adaptation, regional variation within a country. In this KB they exist only as **scattered mentions inside source texts** (bicultural ×5, generational ×6, expatriate ×17; the ecological fallacy is present conceptually via Sebenius's four fallacies but not as a labelled exceptions layer). Because the KB has no section architecture at all, there is no dedicated "Exceptions / Contextual Modifiers" unit the agent can retrieve — the strongest articulation of the exceptions lives in the SI (behavioural rules) and in the *PRD that does not match this agent*. Strong, genuinely multi-axis generalisation; held below the top band by the absence of an exceptions layer as a first-class KB structure.

---

## Dimension 3 — Coherence of Design — **66 / 100**

**Confidence:** High (the mismatch is a hard, textual finding).

**Evidence**

1. **PRD ↔ SI is broken at the document-identity level.** The PRD is ARIA (7 capabilities, advisor-not-sparring, no seniority calibration); the SI is Negocierge (5 capabilities, sparring partner, seniority-calibrated). Capability counts, interaction model, and the central seniority mechanic **do not line up**. PRD §3 capabilities (Position Analysis, Value Creation, Debrief…) have **no** SI workflow steps; SI capabilities (Offer Letter, Pressure-Testing, Stakeholder Map) trace to a *Negocierge* PRD that is absent. This is the core coherence failure.
2. **SI internal coherence is strong.** SI §7 examples obey §5/§6: Example 1 delivers the fixed block sequence in one turn (consistent with the `[CRITICAL BOUNDARY]` no-gatekeeping directive at §5 Steps 4/8); the Working-Hypothesis stakeholder map obeys the §6 ≤300-word / labelling rule; the offer letter obeys §5 Step 8 (terms verbatim + stylistic note). No internal SI contradictions found.
3. **SI ↔ Evaluation coherence is strong** — the Evaluation maps cleanly onto the *actual* SI sections (§1–§7) and even surfaces the residual PRD mismatch (it references a Negocierge-PRD "2-minute scan" criterion not in the submitted PRD — itself further evidence the wrong PRD is attached).
4. **KB/SI separation is clean** (see scan): no behaviour embedded in the KB, no domain knowledge dumped into the SI. This *helps* coherence and is why the score is not lower.

**Net:** internal SI quality and clean KB/SI separation are genuinely good, but the headline PRD↔SI traceability — the spine of this dimension — fails because two different agents are described. Adequate band, not weak, because the failure is a wrong-file/version error over an otherwise coherent SI+Eval pair, not incoherent thinking. (Note: the −50 applies to KB/SI *separation*, which is clean and does **not** fire; this Coherence deduction is for the orphaned PRD, a separate check.)

---

## Dimension 4 — Evaluation Honesty — **93 / 100**

**Confidence:** Medium (tone/honesty is partly judgement; structure is High).

**Evidence**

1. **Part A finds ≥3 located issues with fixes**, in a 5-row Findings Log with severity + status. Two High-severity issues are documented *and fixed* (shadow-KB leak in §7 Examples; duplicated hardcoded deadlock rule across §3 Rules 2/3); three remain **Open** (seniority spread across 4 sections; missing 2-minute-scan bound; PRD/SI ambiguity-handling divergence). It explicitly separates "MET" from "⚠️ PARTIAL".
2. **Part B contains the full first and second outputs**, textually distinct — not a re-run. Round 1 is the gatekeeping non-answer ("Want me to draft… in a follow-up turn"); Round 2 is a long, substantive mid-negotiation rescue.
3. **Diagnosis traces each gap to a root cause in the SI** ("this is an SI *gap*, not a contradiction: §5 Steps 4 and 8 did not yet contain any directive forbidding…") and the fixes are quoted verbatim (the `[CRITICAL BOUNDARY]` injection; the §6 script mandate; the §3 deal-design rule).
4. **The standout: it surfaces *residual* failures after the fix and refuses to flatter.** The Round 2 scoring table marks Criterion 3 (verbatim scripts) and Governance-Deadlock handling as **STILL NOT MET despite the injected fixes**, and the write-up names *why* — "two of the three injected fixes did not produce the intended behaviour, and we are reporting that directly rather than smoothing it over… the governance gap is the more serious… the agent dropped it silently instead of flagging it… a silent omission is worse than a declined request." It diagnoses the mechanism (directive-strength vs placement; the `[CRITICAL BOUNDARY]` constrains the opening but not the closing move) and specifies what a further round would change. A self-eval that lands its own agent at NOT-MET on two of three fixes *after* iterating is exactly the top-band behaviour the rubric reserves 90+ for.

**Minor gap (why not higher):** Part B addresses one real case; the governance deadlock (one of two named crunch points) is correctly flagged unresolved but not driven to a second iteration (the group cites the one-round assignment limit — legitimate). Honesty is exemplary; breadth of iteration is the only thing left on the table.

---

## KB/SI Separation Scan — **−50 NOT triggered**

| Direction | Finding | Location | Verdict |
|---|---|---|---|
| KB → behaviour? | No agent-behaviour directives authored into the KB. "you must" (×12), "the agent must" (×1), "step 1" (×16) are all **inside source book text** (Voss second-person prose; Lewicki chapter steps) — not Negocierge instructions. No "You are Negocierge", no output-format/persona/decision-tree authored for the agent. | KB body | Clean |
| KB → behaviour? | The one custom insertion (`addendum interno`, deal-design decoupling) is **domain technique** (principle/example), not agent behaviour. | KB ~char 143k | Clean (correct placement) |
| SI → domain dump? | SI names frameworks but **does not define them** ("Hofstede defined power distance as…" absent); no country-pattern explanations dumped inline; academic citations **explicitly omitted by default** (§6 Sources). §7 example cultural content carries an explicit *illustrative-only* disclaimer requiring runtime KB verification. | SI §3, §6, §7 | Clean |

**Distinct violations: 0. Structural violations: 0.** The −50 does **not** apply. (Clean separation is also one of the group's own documented strengths — Part A Check 4.)

---

## Citation table (existence-only)

Canonical course texts Verified on sight per the rubric. 19 unique `[[KB-FONTE]]` sources; 130 tag instances.

| # | Citation (as tagged) | Status | Basis |
|---|---|---|---|
| 1 | Fisher, Ury & Patton — *Getting to Yes* | Verified | Canonical |
| 2 | Lewicki et al. — *Essentials of Negotiation* (full TOC/chapters present) | Verified | Canonical |
| 3 | Erin Meyer — *The Culture Map* (8 scales) | Verified | Canonical |
| 4 | Trompenaars & Hampden-Turner (with Woolliams) — *Riding the Waves of Culture*, 4th ed. | Verified | Canonical |
| 5 | Kirkman, Lowe & Gibson — *A Quarter Century of Culture's Consequences* (JIBS 2006, Hofstede review) | Verified | Canonical source family |
| 6 | Salacuse — *Ten Ways that Culture Affects Negotiating Style* (Negotiation Journal 1998) | Verified | Canonical |
| 7 | Sebenius — *Assess, Don't Assume* (HBS WP 10-048; four fallacies) | Verified | Canonical |
| 8 | Chris Voss (with Tahl Raz) — *Never Split the Difference* (2016) | Verified | Canonical |
| 9 | Michael Wheeler — *Negotiation Analysis: An Introduction* (HBS Note 801-156) | Verified | Real HBS note |
| 10 | Adair, Brett & Okumura — *Negotiation Behavior When Cultures Collide: US & Japan* (JAP 2001, 86:3) | Verified | Real, canonical research family |
| 11 | Adair, Brett, Lempereur, Okumura, Shikhirev, Tinsley & Lytle — *Culture and Negotiation Strategy* (Negotiation Journal 2004) | Verified | Real |
| 12 | Gesteland — *Cross-Cultural Business Behavior* | Verified | Canonical |
| 13 | Sergiu Bălan — *The Trompenaars' Seven-Dimension Cultural Model… Romanian Students* (7th Int'l Mgmt Conf., Bucharest 2013) | **Verified (web)** | Exact title match; conference archive PDF found |
| 14 | Fabio Musso — *Guanxi… Chinese Business Network* (MPRA Paper No. 31642, 2005) | **Verified (web)** | MPRA 31642 number confirmed |
| 15 | Darley, Luethge & Blankson — *Culture and International Marketing: A Sub-Saharan African Context* (J. Global Marketing 26:4, 2013) | **Verified (web)** | Exact title/journal match |
| 16 | Foo, Elfenbein, Tan & Aik — *Emotional Intelligence and Negotiation…* (Int'l J. Conflict Management 15:4, 2004) | **Verified (web)** | PsycNet/SMU records found |
| 17 | Amadou Dieng — *ADR in Sub-Saharan African Countries* | **Verified (web)** | OHADA chapter PDF + Harvard cite found |
| 18 | Roberta Rio — *Breve Decalogo di Comunicazione Cross-Culturale* | Unable-to-verify | Italian practitioner handout; not a fabrication signal, but not independently locatable. Likely course/practitioner material — flag for instructor. |
| 19 | Weir / Sultan / Van de Bunt — *Wasta* + thesis on negotiation phases | Verified | Wasta literature (Weir is the canonical wasta scholar) |
| — | `Nego Agent — addendum interno` (deal-design decoupling) | N/A | Self-authored KB chunk, correctly labelled internal — not an external citation. |

**Fabricated citations: 0.** One Unable-to-verify (Roberta Rio handout) — likely real Italian course/practitioner material, not a fabrication red flag.

---

## Coherence map (PRD ↔ SI)

| Check | Result |
|---|---|
| PRD §1 ↔ SI §1 (role) | **FAIL** — PRD: ARIA, advisor, "does not adopt a counterposition." SI: Negocierge, sparring partner / challenger. Different agents. |
| PRD §3 ↔ SI §5 (capabilities → workflow) | **FAIL** — PRD lists 7 capabilities (Position Analysis, Value Creation, Debrief…); SI implements 5 (Cultural Profile, Stakeholder Map, Risks, Pressure-Testing, Offer Letter). No traceability between the two sets. |
| PRD §5 ↔ SI §6 (output format) | **FAIL** — PRD: Stage-1/2/3 Analytical Report with 11 numbered sections. SI: five fixed capability blocks with word ceilings. Unrelated output models. |
| PRD §7 ↔ SI §4 (success criteria → Criteria) | **FAIL** — PRD §7 is SC-1…SC-7 / FM-1…FM-6 (no seniority, no 2-min scan). SI §4 implements seniority checks + scan structuring that trace to a *Negocierge* PRD not in this folder. |
| SI §7 ↔ SI §1–6 (examples obey rules) | **PASS** — examples consistent with the SI's own §4/§5/§6. |
| SI ↔ Evaluation | **PASS** — eval maps to the real SI sections; even flags the missing Negocierge-PRD criterion. |

The PRD↔SI rows fail because of the wrong-PRD submission, not because the SI is internally incoherent. Internal SI and SI↔Eval coherence are sound.

---

## Artefact subtotal

| Dimension | Score |
|---|---|
| Domain Rigour | 84 |
| Generalisation | 76 |
| Coherence of Design | 66 |
| Evaluation Honesty | 93 |
| KB/SI separation −50 | **Not triggered** |
| **Subtotal /400** | **319** |

---

## Items requiring instructor judgement

1. **Agent Quality is not scored here** — scored live by the instructor from the demo. Final /500 and verdict pending.
2. **Wrong PRD submitted (decisive coherence item).** The folder's PRD is **ARIA** (a different/earlier design); the delivered agent, SI, and Evaluation are **Negocierge**. Confirm with the group which PRD is canonical — if a correct Negocierge PRD exists and was simply not uploaded, the Coherence score is conservative. As submitted, PRD↔SI traceability fails.
3. **KB is a raw-text dump, not a chunked KB.** Rich, correctly-sourced, complete content, but no "How to Use", no Parts/Sections, no principle/explanation/example architecture, and no dedicated exceptions layer — yet the SI addresses the KB as if those sections exist. Worth probing whether retrieval actually works live against a 3.85 MB raw corpus.
4. **Substantive accuracy** of regional/framework claims not verified (existence-only on citations).
5. **One Unable-to-verify citation** (Roberta Rio, *Decalogo*) — confirm it is course/practitioner material.
6. **Submission was revised after an earlier grading pass** (KB tripled in size and gained the cross-cultural framework sources; PRD swapped). This report grades the current state.
7. **Contribution flag: none.** All five members have a described role in `group.md`. No deduction recommended; the instructor decides.

### group.md contribution check
Five members, each with a real described role:
- Caruso Lorenzo — KB, **major PRD**, SI, Part A eval, presentation, final video
- Cesari Samuele — **major KB**, PRD check, SI modification, eval, presentation
- Ronzino Matteo — **major KB**, PRD, SI check, **Part B + final wrap-up of eval**, final video
- Schiantarelli Gianmarco — **major KB**, PRD check, SI, **Part B eval**, final video
- Vecchiarelli Lorenzo — KB+SI modification, PRD, Part A eval, **major final video**

No blank or "did not contribute" line. **No flag fires.**

---

## Limitations footer

- Agent Quality is not assessed here — the instructor scores it live from the demo.
- Substantive accuracy of domain claims is not verified; citation checks are existence-only, not claim-attribution.
- Provenance of artefacts is not verified.
- Confidence ratings are heuristic, not statistical.
- The KB was read from the full decoded source (3.85 MB) via structural probing and targeted reads, not a linear front-to-back read of all 3.8 MB; quoted evidence and counts are exact.
