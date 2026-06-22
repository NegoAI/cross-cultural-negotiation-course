# Internal Assessment — CultureDeal Strategist (Antonucci group)

**Group name:** CCN AI Agent (namesake: Antonucci)
**Project / product:** CultureDeal Strategist
**Drive folder:** `CCN AI Agent - Antonucci` (`1C3Yf2SkznU7hy6SJXKTElgon-4ptQwN3`)
**Assessment date:** 2026-06-22
**Skill version:** cross-cultural-2026-assessment (four document dimensions /400; Agent Quality scored live by instructor)
**Grader role:** instructor's grading assistant — document dimensions only; no Agent Quality, no /500, no verdict.

## File-mapping log

| Detected filename | Mapped artefact | Confidence |
|---|---|---|
| `Group.md` | group.md (members + step leads) | High |
| `01_Knowledge_Base_Final.md` | Knowledge Base | High |
| `02_PRD_Final.md` | PRD | High |
| `03_System_Instructions_v2.3_Full.md` | System Instructions (canonical/academic full) | High |
| `03A_System_Instructions_v2.3_Deployed.md` | System Instructions (compact deployed variant) | High |
| `04_Evaluation_Report_v4_Final.md` | Evaluation Report (Part A + Part B + 4-case portfolio) | High |
| `CultureDeal_link.pdf` | agent access link (not graded; agent shown live) | n/a |
| `CultureDeal.mp4` | recorded presentation | ignored per skill |

All five graded artefacts present. Two SI files submitted: a 43 KB "Full" academic SI and a 7 KB "Compact Deployed" SI. Both are operational instruction text (no domain dumping); the Full is treated as the canonical SI and the Deployed as a disclosed character-limited subset. Both were read in full.

---

## Dimension 1 — Domain Rigour — 94/100 (confidence: Medium)

Exemplary band. KB is deep, both halves of the course are covered substantively, and every citation is real (including the three non-canonical ones).

- **Chunk format is disciplined and consistent.** "How to Use This Knowledge Base" declares the chunk schema — *Principle / Explanation / Negotiation implication / Example / Strategic links* — and the chunks honour it. E.g. §1.3 ZOPA: "**Principle.** ZOPA means Zone of Possible Agreement: the range of terms that are better than each side's BATNA… **Negotiation implication.** If no ZOPA exists on price, a ZOPA may still exist through structure: timing, risk-sharing, contingent payments…"
- **Both halves present with substance, not naming.** Part I negotiation methodology is complete: positions/interests (1.2), BATNA/reservation/ZOPA + "Imaginary BATNAs are dangerous" (1.3), multilateral/stakeholder levels (1.4), coalitions (1.5), value creation (1.6), concession strategy + **anchoring** (1.7), post-negotiation review (1.8). Part II treats Hofstede, Trompenaars, Schwartz, Hall, Meyer, GLOBE each with a real explanatory paragraph — Schwartz in particular ("operates one level deeper… a values map, not an interaction checklist") shows genuine understanding rather than a label.
- **Framework–question-fit table (2.1)** maps negotiation questions to a primary lens with a distinct alternative lens — substantive scaffolding that also feeds the coherence story.
- **Two real applied cases with structural analysis:** Tata–Ford–JLR (4.1 Case A, positions/interests, coalition with the Unite union as a level-2 stakeholder weakening Ford's BATNA) and Ericsson–China (4.1 Case B, guanxi, government as level-2 veto, face-saving and table-vs-informal information asymmetry).
- **Citations: all verified.** Canonical sources (Fisher/Ury, Lewicki, Malhotra & Bazerman, Raiffa, Hofstede, Trompenaars, Hall, Meyer, GLOBE/House, Gordon) verified on sight. The three non-canonical citations were web-searched and all exist with exact match: Ghauri & Fang (2001) *Journal of World Business* 36(3):303–325; Benet-Martínez et al. (2002) *J. Cross-Cultural Psychology* 33(5); Brett (2007) *Negotiating Globally* 2nd ed. **Zero fabricated citations.**
- *Instructor-judgement flag:* substantive accuracy of domain claims is not graded here (skill boundary). The Schwartz "seven value orientations / three bipolar dimensions" and the framework-level claims read as accurate, but confirm against the instructor's own course treatment if precision matters.

Why not 90–100 top of band: chunk substance is strong but a handful of Part III dimension chunks (3.8 work orientation, 3.5 uncertainty) are lighter than the Part I/II material; Medium confidence because chunk-depth judgement benefits from the instructor's read.

---

## Dimension 2 — Generalisation — 93/100 (confidence: Medium)

Exemplary band. The KB and product are genuinely multi-axis, and the exceptions appear as their own sections — the hardest test for this dimension.

- **Multiple cultural axes as their own sections (≥3 chunks each):** Part III gives time/polychronic (3.1), universalism–particularism (3.2), affective–neutral (3.3), power distance (3.4), uncertainty tolerance (3.5), individualism–collectivism (3.6), high/low context (3.7), achievement vs quality-of-life (3.8) — eight dimensions, each its own section, plus six named frameworks in Part II. This is not a single-axis KB.
- **Exceptions present as their own sections, not footnotes** (the hard test): §4.2 "Framework Limits and Exceptions" carries four distinct sub-sections — "Frameworks describe distributions, not individuals" (individual variation), "Biculturalism creates code-switching," "Organisations and industries can override national culture," and "Regional and class variation matter." Generational and expatriate adaptation are also named in the exceptions layer and the SI exceptions engine (SI §3 Rule 4 / Step 7: "individual variation, biculturalism, generational differences, regional variation, organisational culture, industry norms, role effects, class/status differences, and expatriate adaptation").
- **Regional starting hypotheses table (4.3)** spans eight world regions and is explicitly framed as "starting hypotheses, not cultural profiles… useful only when connected to observed behaviour and tested against exceptions."
- **Product is built general-purpose:** PRD §1.4 Generalisation principle and §7.4 evaluation portfolio; the evaluation itself tests four different cultural axes AND four different negotiation structures (Italy–UAE distribution, UAE–Sweden procurement, US–Japan alliance, Germany–India distressed implementation).

Why not higher: biculturalism and individual variation are handled properly but each exceptions sub-section is comparatively brief (one chunk each) versus the multi-chunk depth of Part I; the generational/expatriate exceptions live more in lists than in their own developed chunks. Medium confidence (depth judgement).

---

## Dimension 3 — Coherence of Design — 91/100 (confidence: High)

Strong-to-exemplary. KB, PRD and SI line up tightly; clean KB/SI separation; **no −50**.

- **Clean separation (both directions).** KB carries framework knowledge and analytical distinctions but no turn-by-turn behaviour — its own Executive Summary states "It does not tell the final agent how to behave turn by turn. Behavioural rules belong in the System Instructions." The SI carries operational rules, workflow, output contracts and self-checks but **names** frameworks rather than defining them (SI §3/§5.1 Step 7 select a lens; they do not paste "Hofstede defined power distance as…"). No academic citations or country-pattern textbook content in the SI.
- **PRD ↔ SI traceable** (see coherence map below): every PRD capability maps to an SI workflow step; output contracts match; success criteria carried into SI self-checks; role consistent.
- **Worked examples obey the rules above them.** SI §7 Examples 1–3 follow the §6 output format, apply the qualification engine (signal/lens/hypothesis/implication/qualifier/counter-hypothesis/validation/confidence), and respect the single-primary-framework rule and negotiation-first ordering.
- **Internal version-control is coherent:** the Operating Kernel explicitly resolves example-vs-rule conflicts ("If a later example appears to conflict with this Operating Kernel, follow the Operating Kernel").

Minor deduction: two SI artefacts (Full vs Deployed) are "functionally aligned but not textually identical" (the group discloses this in Eval §15/§18). That is a small maintenance/consistency risk — a future edit to one could drift from the other — and the namesake of the dimension is consistency across documents, so it costs a couple of points even though the divergence is disclosed and currently benign.

---

## Dimension 4 — Evaluation Honesty — 89/100 (confidence: Medium)

Strong. The eval surfaces real weaknesses, shows full first and second outputs that are textually distinct, traces gaps to SI root causes, applies an exact SI patch, and closes with a genuinely self-critical residual-limitations section.

- **Part A finds ≥3 located issues with fixes:** six-row findings table (§3) with location + severity + recommended fix, including a correctly-rated **High** ("user-side internal pressure… a structural gap in the stakeholder taxonomy," SI §5.1 Step 4/Step 10).
- **Part B full first output AND full second output, textually distinct** (not a re-run): the first output (§5) lacks an Executive Priority Summary and ranked moves; the second (§8) leads with three priorities, restructures Recommended Moves into ranked phased sections, and adds a CEO-briefing message — real iteration.
- **Diagnosis traces each gap to a root cause in the SI** (§7.1 table: "SI gap — Step 10 says generate strategy but does not require priority ordering").
- **SI changes are specific (exact text):** §7.2 gives the literal v2.1 patch block to add to Step 10, Output Format and Self-Check.
- **Sceptical tone with a sharp residual section:** §17 and §18 name what is *not* proven — "four cases are still a course-scale portfolio, not statistical proof"; no bicultural, public-sector, humanitarian or extreme-asymmetry case tested; the two SI versions "not textually identical." This is the opposite of a self-eval that finds nothing.

Honesty asterisks (why not 90+):
1. **Self-flattering case scoring.** Cases 3 and 4 and the v2.3 retests (§11.5, §12.5, §13.3, §13.4) award the agent a wall of 9.6–10.0 sub-scores with little downside. The Part A/Part B reasoning is honest; the numeric case grading drifts toward self-congratulation.
2. **Part B second output provenance is disclosed but soft.** §8's deployment note states the second output was generated "by applying the SI v2.1 patch to the prompt in a controlled chat session," with the final v2.3 Project equivalence argued in §13 — i.e. the headline iteration output is a controlled-chat simulation rather than a capture from the deployed Project. The group flags this transparently, which is to its credit, but it is a residual gap between "shown" and "deployed" output.

Medium confidence (tone/honesty judgement).

---

## KB / SI separation scan (−50 trigger)

Scanned KB for behavioural content and SI for domain-knowledge dumping.

| Direction | Finding | Location | Verdict |
|---|---|---|---|
| Behaviour in KB? | None. KB explicitly defers turn-by-turn behaviour to SI; chunks are knowledge + negotiation-implication, no response templates / decision trees / "always-never" agent rules. | KB Exec Summary; throughout | Clean |
| Domain dump in SI? | None. SI names frameworks and selects lenses but does not define them; no academic citations; no country-pattern textbook paragraphs; BATNA/ZOPA used as operational triggers, not expanded theory. | SI §3, §5.1 Step 7–8 | Clean |

**Distinct violations: 0. Structural violations: 0. −50 NOT applied.**

---

## Citation table (existence-only)

| Citation | Class | Status |
|---|---|---|
| Course notes (Prof. Rana, Cattolica) | Course | Verified (canonical/instructor) |
| Fisher, Ury & Patton (1981) *Getting to Yes* | Canonical | Verified on sight |
| Raiffa (1982) *The Art and Science of Negotiation* | Canonical | Verified on sight |
| Malhotra & Bazerman (2007) *Negotiation Genius* | Canonical | Verified on sight |
| Lewicki, Saunders & Barry (2015) *Negotiation* 7th ed. | Canonical | Verified on sight |
| Hofstede (1980/2001) *Culture's Consequences* | Canonical | Verified on sight |
| Hofstede (2011) "Dimensionalizing Cultures," *Online Readings in Psychology and Culture* 2(1) | Canonical author | Verified on sight |
| Trompenaars & Hampden-Turner (1997) *Riding the Waves of Culture* | Canonical | Verified on sight |
| Hall (1976) *Beyond Culture* | Canonical | Verified on sight |
| Meyer (2014) *The Culture Map* | Canonical | Verified on sight |
| House et al. (2004) *Culture, Leadership, and Organizations: The GLOBE Study* | Canonical | Verified on sight |
| Gordon (1970) *Parent Effectiveness Training* (Behavior Window) | Canonical | Verified on sight |
| Ghauri & Fang (2001) "Negotiating with the Chinese," *J. World Business* 36(3):303–325 | Non-canonical | **Verified** (ScienceDirect / RePEc / SSRN — exact match) |
| Benet-Martínez et al. (2002) "Negotiating Biculturalism," *J. Cross-Cultural Psychology* 33(5) | Non-canonical | **Verified** (APA PsycNET / Ovid — exact match, DOI 10.1177/0022022102033005005) |
| Brett (2007) *Negotiating Globally* 2nd ed., Jossey-Bass/Wiley | Non-canonical | **Verified** (APA PsycNET / Kellogg / Amazon — exact match) |

**Fabricated citations: none.**

---

## Coherence map (PRD ↔ SI)

| Check | Result |
|---|---|
| PRD §3 capabilities (CAP-01…CAP-13) ↔ SI §5 workflow steps | Aligned. Each CAP traces to a step: CAP-02/04/05 → Steps 4–5/8; CAP-06/07 → Steps 6–7 qualification engine; CAP-08 → Step 9 communication router; CAP-10 → Step 10 internal-alignment rule; CAP-11 → recalibration/review formats. No orphaned capability. |
| PRD §5 output format ↔ SI §6 output format | Aligned. Standard-analysis contract, Executive Priority Summary, quick brief, recalibration, review and roleplay formats match across both. |
| PRD §7 success criteria ↔ SI §4 Criteria / §5.1 Step 12 self-check | Aligned. PRD §7.3 explicitly splits self-checkable vs external criteria; the self-checkable ones appear as SI positive/negative self-checks. |
| PRD §1 role ↔ SI §1 role | Aligned. "Negotiation-first cross-cultural negotiation strategy agent" consistent in both. |
| SI §7 examples ↔ SI §1–6 rules | Aligned. Worked examples obey the output format, qualification engine, single-framework rule and negotiation-first ordering. |

No contradictions or orphaned requirements found.

---

## Artefact subtotal

| Dimension | Score |
|---|---|
| Domain Rigour | 94 |
| Generalisation | 93 |
| Coherence of Design | 91 |
| Evaluation Honesty | 89 |
| −50 KB/SI separation | not applied |
| **Subtotal /400** | **367** |

Agent Quality is **not** scored here. No /500 total and no verdict asserted.

---

## Items requiring instructor judgement

- **Agent Quality (live):** scored by the instructor from the live demo / `CultureDeal_link.pdf`. The documents predict a strong agent (negotiation-first, qualified hypotheses, four-axis transfer) — confirm against a case outside the group's own axes.
- **Substantive accuracy:** not graded here. Spot-check the Schwartz value-orientation description and the framework-fit defaults against the course's own treatment if precise attribution matters.
- **Two SI versions:** Full (academic) vs Deployed (compact). Confirm the deployed Project actually runs the compact v2.3 + KB v3.2 as the report claims; the divergence is disclosed but is a maintenance risk.
- **Part B second-output provenance:** the headline iteration output (§8) is a v2.1 controlled-chat simulation with deployed-Project equivalence argued in §13 — judge whether that meets the "real-case round on the deployed agent" bar.
- **Contribution flag:** none. `Group.md` lists all five members with first + last name and a led-step each ("All members contributed across all five steps").

---

## Limitations footer

- Agent Quality is not assessed here — the instructor scores it live.
- Substantive accuracy of domain claims is not verified — only existence of citations and structural coherence.
- Citation verification is existence-only, not claim-attribution.
- Provenance of artefacts is not verified.
- Confidence ratings are heuristic, not statistical.
