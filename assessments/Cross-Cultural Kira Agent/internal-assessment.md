# Internal Assessment — Cross-Cultural Kira Agent (KIRA)

**Group name:** Cross-Cultural Kira Agent *(folder-name parsing flag — see below)*
**Drive folder:** `Cross-Cultural Kira Agent` — ID `1wS9JClPcrNpSH6_Nbs64sTo_2adzvu8y` (parent "CCN Project Submission")
**Members:** Edoardo Monaco · Francesco Accarino · Beatrice Vanda Ruggeri · Gabriele Redaelli
**Assessment date:** 2026-06-22
**Skill version:** cross-cultural-2026-assessment (v1)
**Assessor:** grading assistant (four document dimensions only; Agent Quality scored live by instructor)

> **Folder-name parsing flag:** The folder `Cross-Cultural Kira Agent` has **no spaced separator** (` - ` / ` – ` / ` — `). Per the col-C rule, the whole folder name is used as the group name and the namesake-lastname split is not applied. There is no namesake last name to extract; member names are taken from `group.md`.

---

## File-mapping log

| Detected filename | Mapped artefact | Confidence | Notes |
|---|---|---|---|
| `KB Cross Cultural Negotiation v1 2.md` | Knowledge Base (v1.2) | High | "How to Use This KB", 3 Parts, chunked frameworks, evidence tiers. 847 lines. |
| `PRD definitivo.md` | PRD (v2.0) | High | 7 sections + worked examples; KIRA identity. |
| `system-instructions v3_1.md` | System Instructions (v3.1) | High | "You are KIRA…"; 7 sections (Role, Context, KB Usage, Criteria, Instructions, Output Format, Examples). |
| `5-evaluation-report-EN.md` | Evaluation Report | High | Part A (4 checks) + Part B (real-case, deployed-agent output). |
| `group.md` | Group manifest | High | 4 members + per-step contributions. |
| `link KIRA Lars.pdf` | Agent link (claude.ai/share) | n/a | Not a graded artefact; agent shown live. Not penalised. |
| `VIDEO Cross.mp4` | Recorded presentation | n/a | Ignored per skill. |

All five graded artefacts present. No missing artefacts. Read in full.

---

## Dimension 1 — Domain Rigour — **95 / 100**

**Confidence:** Medium (chunk-substance judgement is partly the instructor's read; citation verification is High-confidence and clean).

This is among the strongest KBs the rubric anticipates. Both halves of the course are present **substantively**, not named.

- **Negotiation methodology (Part 1, Sections 1.1–1.10).** Full chunk discipline — each carries source + evidence tier + core concept + key variables + reasoning steps + output pattern + limitations. E.g. §1.2 BATNA: *"BATNA estimates are hypothesis-grade without verified market data. A specific financial reservation value must never be computed without the user confirming the underlying data."* Covers Principled Negotiation, BATNA, ZOPA, leverage (Lax & Sebenius 3-D), value creation / multi-issue trading, anchoring & concession strategy, investigative negotiation, a 13-row failure-mode table, preparation checklist, and post-meeting debrief structure.
- **Cross-cultural frameworks (Part 2, Sections 2.1–2.9).** Hofstede, Trompenaars, Meyer (8 scales), GLOBE (9 dims + 6 CLTs), Hall, two-type Trust theory, Face theory (dignity/face/honor prototypes), Tight/Loose, and a standout Exceptions section. Each framework carries **named critical limitations** — e.g. §2.1: *"Do not use Hofstede UAI interchangeably with GLOBE UAI — they measure different phenomena… r ≈ −0.69, Venaik & Brewer 2010. Choose one."* This is genuine domain command, not labelling.
- **Evidence-tier system [ET]/[BP]/[EI]/[L]** applied throughout — the KB self-grades the strength of each claim. Meyer correctly tiered [EI] "not peer-reviewed"; Trompenaars flagged as statistically contested.
- **Citations: every one checked is real and accurately attributed.** Canonical sources verified on sight (Fisher/Ury/Patton, Lewicki-adjacent Mnookin, Malhotra & Bazerman, Raiffa, Hofstede, Hall, Trompenaars, Meyer, GLOBE/House, Salacuse, Lax & Sebenius). The oddly-specific non-canonical set — exactly where fabrication hides — was web-verified: Aslani et al. 2016, Dheer et al. 2015 (JIBS), Venaik & Brewer 2010, Kittler/Rygl/Mackinnon 2011, Gelfand et al. 2015 (JOB), Kwon 2012, Khakhar & Rammal 2013, Lenartowicz & Roth 2001 — **all exist and match the KB's claims.** Zero fabrication signals (full table below).

**Why 95, not higher:** the hardest-test feature (clean both-halves coverage + zero fabricated citations + tiered evidence) is met, which earns the 90+ band. Held just below exemplary only because substantive *accuracy* of every domain claim is out of scope for me and warrants the instructor's spot-read on a handful of practitioner-tier interpretive chunks (e.g. the Meyer France "confrontational + indirect feedback" reading) — a flag, not a deduction.

---

## Dimension 2 — Generalisation — **96 / 100**

**Confidence:** Medium (axis-count is a textual check; exception-depth quality is partly judgement).

Meets the dimension's hardest test: **the exceptions are their own sections, not footnotes.**

- **Multiple axes covered substantively.** Nine cross-cultural frameworks (each its own section with ≥3 chunks of substance) plus seven country/regional cards (Japan, China, Germany/DACH, US, India, Saudi/GCC, Brazil, France — each with eight sub-dimensions: Communication / Hierarchy / Decision-making / Time / Trust / Conflict / Common risks / What not to assume). This is far beyond a single test-case axis.
- **Exceptions as a dedicated architecture (§2.9).** Individual variation, biculturalism (BII), acculturation strategies (Berry), Cultural Frame Switching, generational shift, expatriate adaptation, regional variation within countries, and corporate/sector override are each a **named, sourced sub-section** — *"National scores explain only 2–4% of variance in individual cultural values (Gerhart & Fang 2005)"*; *"approximately 80% of cultural-value variation resides within countries, not between them (Taras et al. 2016)."* This is the strongest exceptions treatment the rubric describes.
- **Override Warning header** before Part 2 forces the exceptions check on every cultural interpretation — generalisation is wired into the runtime navigation logic, not just documented.
- **Misinterpretation Library (§3.3)** gives each signal four hypothesis types (cultural / organizational / tactical / individual) — structurally prevents single-axis over-reading.
- The KB explicitly disclaims monoliths: *"'China,' 'India,' 'Italy,' and 'Brazil' are not single negotiating cultures."* Every country card closes with a "What not to assume" block naming generational/sector/regional override.

**Why 96, not 100:** coverage and exceptions are exemplary; a perfectly comprehensive set would also card a couple more industrially-relevant axes (the group's own eval honestly notes Korea, Indonesia, Taiwan, Turkey, Poland, South Africa are uncarded) — minor, and they surfaced it themselves.

---

## Dimension 3 — Coherence of Design — **93 / 100**

**Confidence:** High (rests on the PRD↔SI coherence map and the KB/SI separation scan).

PRD, SI and KB line up tightly. The artefacts were built as a chain (SI header: *"Translates: PRD v2.0, KB v1.2"*) and it shows.

- PRD §1 identity ↔ SI §1 role: consistent (KIRA, post-meeting/in-cycle sparring partner, three→five behavioural rules).
- PRD §3 capabilities ↔ SI §5 instructions: all five capabilities (Signal Interpretation, Debrief, Stress-Test, Risk-Surfacing, Prep Brief) carried with matching triggers, processes, and the priority order.
- PRD §5 output ↔ SI §6: identical Cap 2 / Cap 5 templates; identical trigger-based Confidence-Map placement rule.
- PRD §7 success/failure criteria ↔ SI §4: the group's own Part A caught that the SI initially mapped only 5 of 6 success criteria and 5 of 6 failure modes (missing "Calibration to user profile" / "Mis-calibrated depth") and the missing 5th behavioural rule — and **fixed all three in SI v3.1.** The SI I assessed contains C6, N6, and the fifth rule, so the coherence gap is closed in the submitted version.

**Residual, minor (flagged, not −50):**
- Version-string drift: the SI header reads v3.1 and contains the fixes, but the eval report references "SI v3.0" in places — cosmetic, self-acknowledged.
- A genuine routing ambiguity the group surfaced itself: SI §5 Step 1 says "Cap 1 … folds into Cap 2 **or** Cap 3" — undefined when Cap 2 **and** Cap 3 are both triggered. Real, low-severity, honestly documented with a proposed fix.

**KB/SI separation:** clean (see scan below). No −50.

**Why 93:** the chain is coherent and the self-caught gaps were actually repaired; held below exemplary by the small live residuals (version drift + the un-fixed routing "or").

---

## Dimension 4 — Evaluation Honesty — **96 / 100**

**Confidence:** Medium (tone and weakness-surfacing are partly judgement; structural checks are High).

This is the rubric's exemplar case: a sharp eval that surfaces a **residual** failure rather than declaring everything fine.

- **Part A finds 5 issues** (1 high, 3 medium, 1 low), each with location + severity + concrete recommended fix — above the ≥3 threshold. The high-severity finding (missing C6/N6 self-checks for one of the six declared success criteria) is a real architectural gap, not a cosmetic one.
- **Part B runs a real deployed-agent output** (claude.ai share link submitted) on an axis **never tested in the SI examples** — Denmark ↔ South Korea — and the group explicitly notes the KB has **no Korea card**, deliberately stress-testing generalisation rather than replaying a home-axis softball.
- **The full first output is reproduced verbatim** (long, structured, not a summary).
- **The eval surfaces a residual failure on the deployed agent:** "Cap 2 template not applied even though Cap 2 was triggered," diagnosed to a root cause in the SI (the "or" routing ambiguity) — exactly the *"honest evaluation that exposes weakness"* the rubric rewards. It also flags the Korea KB-gap and that "Pragmatist test" was not named.
- **A dedicated "What was NOT tested in this round" section** lists Cap 5, Profile-B-misusing-vocabulary, Cap1+Cap5 collision, and tabular cases — unusually honest scoping of the eval's own limits.
- **Tone is sceptical throughout** — it hunts problems and resists self-congratulation even while the agent performs well.

**Why 96, not 100 / instructor-judgement item:** the Part B methodology is **one** deployed-agent run after the Part A fixes, not the textbook two-output *(first output → diagnosis → SI change → second, textually-distinct output)* iteration. The group justifies this honestly ("one authorized SI iteration per the Professor's instruction"), and the Part A fixes *were* applied before the run — so there is genuine iteration, just not a same-case before/after pair. This is the one place the eval falls short of the strict Part B model; it is explained, not hidden, hence near-exemplary rather than docked hard. **Instructor judgement:** confirm whether the single-run-after-fixes design satisfies the Part B "two outputs" requirement for full marks.

---

## KB / SI separation scan

| Direction | Finding | Location | Verdict |
|---|---|---|---|
| SI → KB (definitions leaking into SI?) | No framework definitions in SI. Frameworks are **named and applied only** (e.g. "Erin Meyer's Culture Map, Deciding dimension") — never defined. | SI §1–§6 | Clean |
| SI → KB (borderline) | Worked examples (§7) contain discursive framework glosses *inside sample outputs* ("in high-context Southeast Asian business cultures… answers are deferred…"). Demonstrative material showing *how the agent writes*, not a glossary entry. | SI §7 Examples | Not a violation (borderline, noted) |
| KB → SI (behaviour leaking into KB?) | KB navigation logic ("when the user raises a cultural signal → go to Part 2") is **retrieval guidance**, KB-appropriate, not agent persona/workflow. Case-9 "agent lesson" phrased descriptively ("diagnose the interaction pattern"). | KB "How to Use", §3.4/3.5 | Clean |
| KB → SI (residue check) | The group's own Part A flagged a behavioural sentence ("the agent should never use the KB to generate country profiles…") in a **source** file and asked to verify it is absent from final KB v1.2. **Verified absent** — I read KB v1.2 in full; the sentence does not appear. | KB v1.2 (whole) | Clean (residue not present) |

**Distinct violations: 0. Structural violations: 0. −50 deduction: NOT triggered.**

---

## Citation table

Canonical course texts marked **Verified (canonical)** on sight per skill. Non-canonical / oddly-specific citations web-verified (≥2 query variations where needed).

| Citation (as in KB) | Status | Note |
|---|---|---|
| Fisher, Ury & Patton (2011), *Getting to Yes* | Verified (canonical) | |
| Mnookin, Peppet & Tulumello (2000) | Verified (canonical-adjacent) | *Beyond Winning*, standard. |
| Raiffa (1982) | Verified (canonical) | |
| Lax & Sebenius (2006), *3-D Negotiation* | Verified (canonical) | |
| Malhotra & Bazerman (2007) | Verified (canonical) | |
| Galinsky & Mussweiler (2001, JPSP) | Verified | Anchoring/first-offer, standard JPSP article. |
| Thompson (2020); Shell (2006) | Verified (canonical-adjacent) | Standard negotiation texts. |
| Hofstede (1980; 2001); Hofstede, Hofstede & Minkov (2010) | Verified (canonical) | |
| McSweeney (2002); Baskerville (2003) | Verified | Standard Hofstede critiques. |
| Trompenaars & Hampden-Turner (1997/2014) | Verified (canonical) | |
| Hofstede (1996); Smith, Dugan & Trompenaars (1996) | Verified | Trompenaars dimension-reduction critiques. |
| Meyer (2014/2016), *The Culture Map* | Verified (canonical) | |
| House et al. (2004); Chhokar et al. (2007) — GLOBE | Verified (canonical) | |
| Hall (1959/1966/1976/1983) | Verified (canonical) | |
| **Kittler, Rygl & Mackinnon (2011)** | **Verified (web)** | Hall HC/LC critique, IJCM — exists, matches. |
| **Venaik & Brewer (2010)** | **Verified (web)** | "Avoiding uncertainty in Hofstede and GLOBE", JIBS; r ≈ −0.69 confirmed. |
| McAllister (1995, AMJ); McKnight et al. (1998); Lewicki & Bunker (1996) | Verified (canonical-adjacent) | Trust typology, standard. |
| Goffman (1959); Brown & Levinson (1987); Ting-Toomey (1988/1994) | Verified (canonical) | Face theory canon. |
| **Leung & Cohen (2011, JPSP)** | Verified (canonical-adjacent) | Dignity/face/honor — well-established. |
| **Aslani et al. (2016)** | **Verified (web)** | "Dignity, face, and honor cultures… negotiation strategy and outcomes" — exists, matches. |
| Gelfand, Raver, Nishii et al. (2011, *Science* 332) | Verified (canonical) | Tight/loose, 33 nations. |
| **Gelfand et al. (2015)** | **Verified (web)** | "Culture and getting to yes", JOB — Egypt honor, rational persuasion backfires. Matches. |
| Gerhart & Fang (2005); Gerhart (2009) | Verified | 2–4% variance claim, standard. |
| Tung & Verbeke (2010); Brewer & Venaik (2014) | Verified | Cross-cultural methodology critiques. |
| Hong, Morris, Chiu & Benet-Martínez (2000) | Verified (canonical-adjacent) | Cultural Frame Switching, foundational. |
| Benet-Martínez & Haritatos (2005); Berry (1997) | Verified | BII / acculturation, standard. |
| Taras, Steel & Kirkman (2011); Taras et al. (2016); Greenfield (2014) | Verified | Generational/within-country variation. |
| **Dheer et al. (2015, JIBS)** | **Verified (web)** | India's nine regional subcultures — exists, matches. |
| **Kwon (2012)** | **Verified (web)** | Shenzhen vs Taiyuan individualism/UA — matches. |
| Graham (1983/1985/1993); Graham & Lam (2003) | Verified | Coded negotiation video studies, standard. |
| **Khakhar & Rammal (2013)** | **Verified (web)** | Arab managers / wasta, Int'l Business Review — matches. |
| Alon & Brett (2007); Brett (2014) | Verified (canonical-adjacent) | |
| **Lenartowicz & Roth (2001, JIBS)** | **Verified (web)** | Four Brazilian regional subcultures — matches. |
| Gunia et al. (2011); Vandello & Cohen (1999); Rodrigues et al. (2011); Campbell, Graham, Jolibert & Meissner (1988); Brodbeck et al. (2000) | Verified | All real, field-standard. |
| Salacuse (1998/2003) | Verified (canonical) | |

**Fabricated citations: NONE.** Citation discipline is exemplary; the KB also self-grades each source's evidence strength via the ET/BP/EI/L tier system.

*Existence-only verification per skill — accuracy of each claim's attribution is for the instructor to spot-check.*

---

## Coherence map (PRD ↔ SI)

| Check | Verify | Result |
|---|---|---|
| PRD §3 ↔ SI §5 | Every capability traceable to an SI workflow step | Pass — all 5 capabilities, matching triggers/processes/priority order |
| PRD §5 ↔ SI §6 | Output format aligned | Pass — identical Cap 2 / Cap 5 templates + Confidence-Map placement rule |
| PRD §7 ↔ SI §4 | Self-checkable success criteria carried into SI Criteria | Pass (in v3.1) — C1–C6 + N1–N6; the missing C6/N6 were caught in Part A and fixed |
| PRD §1 ↔ SI §1 | Role consistent | Pass — KIRA identity, post-meeting/in-cycle sparring partner |
| SI §7 ↔ SI §1–6 | Worked examples obey the rules | Pass (one self-flagged micro-inconsistency: Example B's "inline Confidence Map because Cap 5 frame is partial" introduces a placement case not written into §6 — low severity) |

---

## Artefact subtotal

| Dimension | Score |
|---|---|
| Domain Rigour | 95 |
| Generalisation | 96 |
| Coherence of Design | 93 |
| Evaluation Honesty | 96 |
| **−50 KB/SI separation** | **not triggered** |
| **Subtotal /400** | **380** |

---

## Items requiring instructor judgement

1. **Agent Quality (/100)** — scored live by the instructor from the deployed agent. Not assessed here. The submitted claude.ai share link (`link KIRA Lars.pdf`) points at the deployed KIRA on the Lars/Korea case; the document-side evidence (clean separation, real-case handling, ethics refusal of a fabricated-leverage request, framework-as-hypothesis discipline) reads as a strong agent on paper, but live performance is the instructor's call.
2. **Part B "two outputs" question (Evaluation Honesty)** — the eval runs a single deployed-agent output *after* the Part A SI fixes, rather than a same-case first-output → diagnosis → second-output pair. Honestly justified as the one authorized iteration. Confirm whether this satisfies the Part B requirement for full marks.
3. **Substantive-accuracy spot-check** — a handful of practitioner-tier interpretive chunks (e.g. Meyer's France "confrontational + indirect-feedback" combination; the China holistic-bargaining terms) are plausible and sourced but interpretive; worth a domain spot-read. Existence of citations is confirmed; correctness of attribution is not graded here.
4. **Contribution flag** — none. `group.md` describes a real, specific role for all four members (Monaco: deep research + SI; Accarino: KB + SI; Ruggeri: deep research + PRD; Redaelli: KB + PRD; all four on scoping, evaluation, video). No member is blank or stated as non-contributing. Step 10 does **not** fire.
5. **Folder-name parsing** — folder has no spaced separator; whole name used as the group name (noted in header).

---

## Limitations footer

- **Agent Quality is not assessed here** — the instructor scores it live from the deployed agent.
- **Substantive accuracy of domain claims is not verified** — chunks are flagged for instructor review, not graded for correctness.
- **Citation verification is existence-only**, not claim-attribution accuracy.
- **Provenance of artefacts is not verified.**
- **Confidence ratings are heuristic, not statistical.**
- No /500 total and no pass/distinction verdict is asserted — those require the instructor's Agent Quality score.
