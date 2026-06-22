# Internal Assessment — CCN AI Agent Culturae (Amendola)

**Group name:** CCN AI Agent Culturae
**Agent name:** Culturae
**Drive folder:** `CCN AI Agent Culturae - Amendola` (`1uRPCxz2qPjYISKM9MtShVrAFkyHwrL3l`), parent "CCN Project Submission"
**Owner:** saraamendola175@gmail.com
**Assessment date:** 2026-06-22
**Skill version:** cross-cultural-2026-assessment (4 document dimensions /400; Agent Quality scored live by instructor)

## File-mapping log

| Detected filename | Mapped artefact | Confidence |
|---|---|---|
| `2-knowledge-base-guide.md` (171 KB / ~2000 lines) | Knowledge Base | High — "How to Use This KB", 3 Parts, principle/explanation/example chunks, framework sections with substance |
| `3-prd-reference-structure.md` | PRD | High — full 7-section structure (Identity, Target Users, Capabilities, Interaction, Output Format, Boundaries, Definition of Success) + appendix |
| `4-system-instructions-reference-structure istruction.md` | System Instructions | High — second-person "You are Culturae…", 7 sections (Role, Context, KB Usage, Criteria, Instructions, Output Format, Examples) |
| `5-evaluation.md` | Evaluation Report | High — Part A self-eval + Part B real-case loop, full outputs, diagnosis/scoring tables |
| `README.md` | group.md | High — 5 members with first+last names + per-step contribution lines |
| `1-brainstorming.md` | Supporting scoping doc (not separately graded) | High — Step-1 scoping; informs but is not one of the five graded artefacts |

All five graded artefacts present. No `.mp4` in folder (agent shown live — not penalised). No missing artefacts.

---

## Dimension 1 — Domain Rigour — 94/100

**Confidence: Medium-High.** Citation verification, both-halves coverage, and chunk structure are textual checks (high); final judgement of chunk substance is partly the instructor's read (medium).

- **Both halves covered substantively, in depth.** Part 1 (Negotiation Methodology) runs 16 sections — BATNA/Reservation/ZOPA/Target (1.1), Interests vs Positions (1.2), Power & Leverage (1.3), Stakeholder Mapping (1.4), Integrative/Distributive (1.5), Anchoring & Concession (1.6), Trust (1.7), Deadlock (1.8), Post-Neg Review (1.9), 4Ps (1.10), Communication/Listening (1.11), Emotions (1.12), Multi-Issue/Logrolling (1.13), Objective Criteria (1.14), Team Negotiation (1.15), Agreement/Implementation (1.16). Part 2 (Cross-Cultural) covers all major frameworks named in the rubric with real content, not labels: Hofstede (2.1, all six dimensions with national scores), Hall (2.2, context + time + proxemics), Trompenaars (2.3, all seven dimensions), Meyer (2.4, all eight scales), GLOBE (2.5), CQ (2.6), Schwartz (2.7).
- **Chunks have real structure.** Sections follow Principle → explanation → Example → Cross-cultural note → Strategic Link. E.g. 1.1: "BATNA is the best realistic alternative available if the current negotiation fails… Introduced by Fisher and Ury" + a strong-BATNA and weak-BATNA worked example + cross-cultural signalling note. This is substance, not naming.
- **Every citation verified real — zero fabrications.** The canonical course texts recur (Fisher/Ury/Patton, Raiffa, Lewicki, Malhotra & Bazerman, Hofstede/Minkov, Hall, Trompenaars, Meyer, House/GLOBE, Schwartz, Earley & Ang). The non-canonical, oddly-specific ones were web-verified individually and all exist with the exact attributions used: Sebenius (2002) "The Hidden Challenge of Cross-Border Negotiations," *HBR*; Weiss (1994) Sloan Mgmt Review cross-cultural negotiation; Brannen & Thomas (2010) "Bicultural Individuals in Organizations," *Int. J. Cross Cultural Management*; Hong et al. (2000) "Multicultural Minds," *American Psychologist*. See citation table.
- **Country/case layer adds applied depth.** Part 3: 10 country/regional profiles + a comparison matrix + 8 documented cases (Daimler-Chrysler, Renault-Nissan, Walmart Germany, Lenovo-IBM, Camp David, US-Japan trade, Dutch-Chinese SOE, composite supplier case), each with frameworks and a key lesson. Glossary + Concept Index close it.
- **Why not 90+→ higher:** the KB is genuinely top-band. Held just below the ceiling because some Part 3 country profiles lean on a single national-score sweep (e.g. 3.10 Latin America) where the framework treatment is thinner than the flagship sections — a minor unevenness, not a gap. *(Instructor judgement: substantive accuracy of the Hofstede scores quoted, e.g. "Slovakia 110 MAS", is not verified here — flagged for the instructor's read, not graded.)*

---

## Dimension 2 — Generalisation — 93/100

**Confidence: Medium-High.** Axis-count and exceptions-as-sections are structural (high); depth judgement is partly interpretive (medium).

- **Genuinely multi-axis, not a single test case.** 10 country/regional profiles (US, Germany, France, UK, Italy, China, Japan, India, Middle East, Latin America), each its own section ≥ several chunks. The evaluation then exercises five distinct axes (US-Japan, Germany-Brazil, France-India, China-Italy, UAE-Sweden) — directness, time-orientation, compound-hierarchy, trust-sequence, power-distance. The agent is clearly not optimised to one axis.
- **Exceptions are present as their own sections — the hardest test, met.** Section 2.11 (Individual Variation, Bicultural Negotiators, Third-Culture Individuals, Expatriate Adaptation); 2.12 (Organizational, Industry, Generational, Regional Variation Within Countries); 2.13 (Convergence and Mediated Communication); 2.14 (Stereotyping / Cultural Bias / Ethnocentrism + Three-Step Validation + Misinterpretation Checklist); 2.15 (Red-Flags table). Biculturalism and code-switching get a dedicated framework section (2.8 Yin & Yang / Code-Switching) plus Dynamic Culture Theory (2.9). These are framed explicitly as "structural corrections, not footnotes" and the KB's reading instructions force validation against them before any framework is applied.
- **The exceptions are operationalised, not decorative.** The SI's §5 Step 2 modifier check (industry / region / international exposure → confidence level) and Part B non-standard-profile handling pull the 2.11–2.12 material into the live workflow.
- **Why not higher:** the evaluation itself (honestly) shows the non-standard-profile criterion landing only "Partial" on first output across all five axes — i.e. the breadth is in the KB but the agent's *use* of it was the recurring weak spot. That is a fair, self-surfaced limit on demonstrated generalisation, and it caps this just below the ceiling.

---

## Dimension 3 — Coherence of Design — 90/100

**Confidence: High.** Rests on the coherence map and KB/SI separation scan.

- **Clean labour-division across the three docs.** The SI states up front: "All substantive domain content … lives in the Knowledge Base — this document tells the agent how to behave, not what to know." That promise holds in practice (see separation scan: no −50).
- **PRD capabilities trace to SI workflow steps.** PRD §3 Cap 1 (Cultural Profile) → SI §5 Step 2; Cap 2 (Preparation) → Step 3; Cap 3 (Friction Diagnosis) → Steps 2–4 incl. the mandatory non-cultural-cause test; Cap 4 (Strategy/Move) → Step 4; Cap 5 (Exception Flagging) → Step 2 + Part B; Cap 6 (Debrief) → Step 1. No orphaned capability.
- **Output format aligned.** PRD §5 five-section structure (Situation Diagnosis / Cultural Analysis / Negotiation Assessment / Recommended Moves / Immediate Next Step) matches SI §6 exactly, including the required Confidence Calibration line and the four optional blocks.
- **Success criteria carried through.** PRD §7's seven self-checkable criteria map onto SI §4 positive checks; the six PRD failure modes map onto SI §4 negative checks. SI §7's five worked examples obey §§4–6 (each names framework+dimension, distinguishes cultural/commercial, names the 4Ps level, ends on an Immediate Next Step).
- **Why not higher:** one dangling cross-reference — the KB (Section 2.3, and PRD §3.6-equivalent appendix note) points to "PRD §8" for an annotated case example, but the PRD's case material is an *unnumbered* Appendix, not a §8. Harmless to the agent but a real internal-reference inconsistency. Minor and isolated; does not rise to a contradiction.

---

## Dimension 4 — Evaluation Honesty — 91/100

**Confidence: Medium-High.** Part A/B structural completeness is a textual check (high); tone/scepticism judgement is interpretive (medium).

- **Part A finds 6 issues, 2 high-severity, each located with a fix.** Not cosmetic: debrief trigger missing from SI (Medium); length guideline contradicting worked examples — "300–500 vs 700–1500 words" (Medium); "2–3 cultural risks" not required in workflow (Low); non-cultural-cause check only negative not positive (Medium); applied "Execution Layer" domain content sitting *inside* the SI, breaking separation (High); hard-coded KB section numbers in the SI, some numerically wrong (High). The report explicitly states a self-eval finding only "low" issues "has not looked hard enough" — the right sceptical stance.
- **Part B runs the full iteration loop on Case 1.** Full first output (verbatim) → diagnosis tracing the gap to a named SI root cause ("SI gap — Step 2's non-standard-profile handling was an optional flag, not a mandatory worked step") → specific SI change (exact rule: "state which scores are unreliable and why, estimate adaptability, identify which cultural code is active") → full second output (verbatim) → rescore against the same seven criteria. First and second outputs are textually distinct — the second adds a worked split-profile reading (adaptable individual vs non-adaptable nemawashi institution) that the first lacked. Real iteration, not a re-run.
- **It surfaces a *residual* limitation honestly — the top-band test.** The "Where the agent still falls short" section concedes the loop was closed on only one of five axes, that one confirmed fix "does not prove it fires everywhere," and that deeper generalisation is "untestable from this set." It then names exactly what another round would do (re-run the other four cases through the redeployed agent; add a Step-2 framework-checklist self-check; test an unfamiliar axis to pressure generalisation). This is an evaluation hunting problems, not flattering the agent.
- **Why not higher:** the residual gap is named but not *closed* — four of five axes were re-scored on first output only, so the fix is demonstrated once rather than across the board. The report is candid about this, which is why it still scores high; but a fully top-band eval would have re-run at least one more axis to show the fix generalises.

---

## KB / SI separation scan (−50 trigger)

| Direction | Finding | Verdict |
|---|---|---|
| Behaviour in the KB? | KB is pure domain knowledge — principles, framework definitions, country patterns, cases, glossary. Navigation guidance ("Navigate by counterpart →") is reading instruction for the doc, not agent response-templating or decision-trees. No "the agent should…", no persona/tone rules, no response templates. | Clean |
| Domain knowledge in the SI? | SI references the KB *by category* ("the cross-cultural material", "the exceptions and qualifications material") — no framework definitions, no country-pattern explanations, no BATNA/ZOPA expanded inline, no academic citations. The five §7 worked examples *name* frameworks (Meyer Trusting, Hofstede LTO, Hall High-Context) but do not *define* them — names, not definitions, so the boundary holds. | Clean |

The team explicitly fixed an earlier violation (Part A finding #5: an "Execution Layer" of domain content was removed from the SI and relocated to the KB; finding #6: hard-coded KB section numbers replaced with category references). The submitted SI reflects those fixes.

**−50 deduction: NOT triggered.** No structural violation, fewer than three distinct violations (zero, in fact). Residual watch-item (self-flagged by the group): if dimension *descriptions* ever creep into the SI §6 output template, they'd belong in the KB — but currently it lists names only.

---

## Citation table (existence-only verification)

| Citation | In KB | Status |
|---|---|---|
| Fisher, Ury & Patton (2011), *Getting to Yes* | 1.1, 1.2, 1.5, 1.11, 1.14, 1.16 | Verified (canonical) |
| Raiffa (1982), *The Art and Science of Negotiation* | 1.1, 1.2, 1.5, 1.13, 1.14, 1.16 | Verified (canonical) |
| Lewicki, Barry & Saunders, *Negotiation* | throughout Part 1 | Verified (canonical) |
| Malhotra & Bazerman (2007), *Negotiation Genius* | 1.1, 1.2, 1.5, 1.13, 1.14, 1.16 | Verified (canonical) |
| Lax & Sebenius (1986), *The Manager as Negotiator* | 1.5, 1.13 | Verified |
| Voss (2016), *Never Split the Difference* | 1.11, 1.12 | Verified |
| Mnookin, Peppet & Tulumello (2000), *Beyond Winning* | 1.11 | Verified |
| Fisher & Shapiro (2005), *Beyond Reason* | 1.12 | Verified |
| Thompson (2015), *The Mind and Heart of the Negotiator* | 1.12, 1.13, 1.15 | Verified |
| Brett (2014), *Negotiating Globally* | 1.15 | Verified |
| Weiss (1994) [Sloan Mgmt Review, cross-cultural negotiation] | 1.10 | **Verified by web search** — Weiss, *Negotiating with "Romans"*, SMR 35(2), 1994 |
| Sebenius (2002), "The Hidden Challenge of Cross-Border Negotiations," *HBR* | 1.16 | **Verified by web search** — HBR March 2002 |
| Hofstede, Hofstede & Minkov (2010), *Cultures and Organizations* | 1.3, 1.4, 2.1 | Verified (canonical) |
| Hall (1976), *Beyond Culture*; (1983), *The Dance of Life* | 2.2 | Verified (canonical) |
| Trompenaars & Hampden-Turner (2012), *Riding the Waves of Culture* | 2.3 | Verified (canonical) |
| Meyer (2014), *The Culture Map* | 2.2, 2.3, 2.4 | Verified (canonical) |
| House et al. (2004), GLOBE Study; Chhokar, Brodbeck & House (2007) | 1.4, 2.1, 2.5 | Verified (canonical) |
| Earley & Ang (2003), *Cultural Intelligence*; Ang & Van Dyne (2015) | 2.6 | Verified (canonical) |
| Schwartz (1992 onwards), *J. Cross-Cultural Psychology* | 2.7 | Verified (canonical) |
| Brannen & Thomas (2010), *Bicultural Individuals in Organizations* | 2.8, 2.9, 2.14 | **Verified by web search** — *Int. J. Cross Cultural Management* 10(1), 2010 |
| Hong et al. (2000), *Multicultural Minds* | 2.8, 2.9 | **Verified by web search** — *American Psychologist*, July 2000 |
| Thomas & Peterson (2017), *Cross-Cultural Management* | 2.7, 2.9, 2.14 | Verified |

**Fabricated citations: none.** Every citation in the KB corresponds to a real, locatable source. (Existence only — accuracy of each *claim's attribution* to its source is not assessed here; flagged for instructor.)

---

## Coherence map (PRD ↔ SI)

| Check | Result |
|---|---|
| PRD §3 capabilities ↔ SI §5 workflow steps | Pass — all six capabilities trace to a workflow step (Cap1→Step2, Cap2→Step3, Cap3→Steps2–4, Cap4→Step4, Cap5→Step2+PartB, Cap6→Step1) |
| PRD §5 output format ↔ SI §6 output format | Pass — identical five-section structure + Confidence Calibration line + four optional blocks |
| PRD §7 success criteria ↔ SI §4 Criteria | Pass — 7 self-checkable criteria → positive checks; 6 failure modes → negative checks |
| PRD §1 role ↔ SI §1 role | Pass — "Culturae, general-purpose cross-cultural negotiation advisor" consistent; three traits carried as behaviour |
| SI §7 examples ↔ SI §1–6 rules | Pass — all five worked examples obey the format and criteria above them |
| KB internal cross-reference | Minor gap — KB points to "PRD §8" for a case example; PRD case material is an unnumbered Appendix, not §8 |

---

## Artefact subtotal /400

| Dimension | Score |
|---|---|
| Domain Rigour | 94 |
| Generalisation | 93 |
| Coherence of Design | 90 |
| Evaluation Honesty | 91 |
| −50 KB/SI separation | Not triggered |
| **Subtotal** | **368 / 400** |

---

## Items requiring instructor judgement

- **Agent Quality (/100) is scored live by the instructor** — not assessed here. This report covers only the four document dimensions (/400). No /500 total or verdict is asserted.
- **Substantive accuracy of domain claims** is not graded. Flag for the instructor's read: the KB quotes many specific Hofstede national scores (e.g. "Slovakia MAS 110", "Pakistan LTO 0", "France PDI 68") — these are stated as fact; verify against current Hofstede data if precision matters for the live demo.
- **Contribution flag: none.** `README.md` lists all five members (Sara Amendola, Angelo Bejko, Marina Nikolic, Yuan Jia, Tommaso Righino) each with a described role (agent build; module-I research + evaluation cases; module-IV research + KB improvement; module-III research + evaluation cases; module-II research + brainstorming). Every member has a real contribution line — Step-10's narrow trigger does not fire. Note for the instructor: roles are research/module-based, with Amendola credited as sole agent-builder (KB, PRD, SI, evaluation coding) — within normal range, not a flag.

---

## Limitations footer

- Agent Quality is not assessed here — the instructor scores it live from the demo.
- Substantive accuracy of domain claims (e.g. specific Hofstede scores) is not verified — flagged, not graded.
- Citation verification is existence-only, not claim-attribution.
- Provenance of the artefacts is not verified.
- Confidence ratings are heuristic, not statistical.
