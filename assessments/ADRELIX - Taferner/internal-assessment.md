# Internal Assessment — ADRELIX (folder: `ADRELIX - Taferner`)

- **Group name:** ADRELIX
- **Namesake last name (folder):** Taferner
- **Drive folder:** `1pN7vy-qLTbnhSUAgpuZC21JfAZDfOqke` (parent: "CCN Project Submission")
- **Assessment date:** 2026-06-22
- **Skill version:** cross-cultural-2026-assessment (4 document dimensions /400; Agent Quality left for live instructor score)
- **Members (from GROUP MANIFEST.pdf):** Elisa Silvia Spada; Felix Taferner; Adriana Blazheva

## File-mapping log

| Detected file | Mapped artefact | Confidence | Note |
|---|---|---|---|
| `KB.md` (186 KB) | Knowledge Base | High | "How to Use This Knowledge Base"; Parts 1–3; principle/explanation/example chunks throughout |
| `PRD.md` (44 KB) | PRD | High | 7-section structure: Identity, Target Users, Core Capabilities, Interaction Guidelines, Output Format, Boundaries, Definition of Success |
| `SI.md` (8,006 chars) | System Instructions | High | "You are ADRELIX…"; 7 sections: Role, Context/Boundaries, KB Usage, Criteria, Workflow/Edge Cases, Output Format, Example. At the 8,000-char platform ceiling |
| `evaluation_report.md` (112 KB) | Evaluation Report | High | Part A (4 checks + findings table) + Part B (case, full first output, diagnosis, SI patch, full second output, comparison) |
| `GROUP MANIFEST.pdf` | group.md equivalent | High | Members + per-step contributions. Submitted as PDF, not `.md` |
| `agent-link.md` | (not graded) | — | Public ChatGPT custom-GPT link + platform rationale. Not penalised (agent shown live; link no longer required) |
| `ADRELIX Presentation.mp4` | recorded presentation | — | Ignored per rubric |

All five graded artefacts present and read in full. No missing artefacts.

---

## Dimension 1 — Domain Rigour: **94 / 100**
**Confidence: Medium** (textual checks — structure, both-halves coverage, citation existence — are reliable; final chunk-substance judgement is the instructor's, hence not High.)

Exemplary, deep KB. It is the strongest of the four artefacts.

- **Both halves of the course covered substantively, not just named.** Part 1 (Negotiation Methodology) runs five sections with full treatment of preparation, BATNA/reservation value/ZOPA, leverage (structural/situational/behavioural), value creation (logrolling, agenda expansion, contingent contracts, MESOs, PSS), and concession strategy + post-negotiation review (three-tier debrief, bias audit). Part 2 gives substantive treatment of Hall, Meyer, Hofstede, GLOBE, and Trompenaars & Hampden-Turner — each with multiple dimensions worked out, not labelled. Example, Section 2.1: *"Meyer separates the communicating scale from the evaluating scale … a culture can be high-context in general communication but still direct in negative feedback"* (KB.md, Section 2.1) — this is framework-as-hypothesis depth, not naming.
- **Chunk discipline is consistent.** Almost every chunk follows bold-principle → explanation → "For example…" → "See also Section X" cross-reference. E.g. ZOPA chunk (Section 1.2): principle (*"the range between the parties' reservation values…"*), worked €10–14m example, and cross-link to Section 1.4 on agenda expansion.
- **Real cases as diagnostic pattern tests.** Section 3.5 carries DaimlerChrysler, Renault-Nissan, Danone-Wahaha, Kraft-Cadbury, GE-Honeywell, each tied to a recurring failure pattern (universalist contract in particularist market; cultural due diligence after signing; identity/face threats; home-culture imposition).
- **Citations: ~40 distinct sources, all verified, zero fabricated.** Canonical course texts (Fisher/Ury, Lewicki, Malhotra & Bazerman, Raiffa, Hofstede, Hall, Trompenaars, Meyer, GLOBE/House, Earley & Ang) verified on sight. Eight non-canonical/oddly-specific citations web-verified (table below) — all exist and match.

*Why 94 not higher:* substantive-accuracy of the domain claims is not graded here (flagged for instructor); a couple of cases (Hollmann et al. 2010, Sakyi 2019) rest on secondary case literature rather than the primary deal record. These are minor against an otherwise top-band KB.

*Instructor-judgement flag:* none of the domain claims were checked for accuracy of attribution — existence only.

---

## Dimension 2 — Generalisation: **93 / 100**
**Confidence: Medium** (axis-counting is reliable; depth-of-treatment is partly judgement.)

Genuinely axis-agnostic. Hardest test (exceptions as their own sections) is met.

- **Four cultural axes covered as their own substantive sections**, each well beyond a one-line mention: Section 3.1 East Asia (China/Japan/Korea, distinguished — guanxi/mianzi vs nemawashi/ringi/wa vs kibun/nunchi/jeong); Section 3.2 Western Europe (Germany/France/UK/Netherlands/Scandinavia, each differentiated); Section 3.3 Latin America + Middle East (personalismo/confianza/simpatía vs wasta/wajh/honour); Section 3.4 Cross-Regional Comparison (communication, trust type/speed, decision structure, time, face, first-offer patterns as a comparison map).
- **Exceptions are a dedicated section, not a footnote.** Section 2.5 carries ~9 distinct exception chunks: individual variation, tight-loose cultures (Gelfand), cultural intelligence, personality, **biculturalism + cultural frame-switching**, **generational change**, **expatriate adaptation**, third-culture/hybrid profiles, and **sub-national variation** (worked China Beijing/Shanghai/Shenzhen example). Closes with "exception analysis as a required final check before advice." This is the feature that earns the top band.
- The SI carries the same discipline at runtime: SI §3 step 4 forces an exceptions check *(organisation, industry, role, seniority, individual background, generation, bicultural or expatriate experience, international exposure, sub-national)* before advising from culture, and SI §6 boundary 9 is an explicit anti-stereotyping constraint.

*Why 93 not higher:* coverage is regional/European-Asian-Latin-Arab; South Asia and Sub-Saharan Africa are not given their own profiles. The frameworks plus exception logic make the agent genuinely transferable beyond the covered regions (demonstrated by the eval running an out-of-profile Italian-Bulgarian case successfully), so this is a minor breadth gap, not a single-axis failure.

---

## Dimension 3 — Coherence of Design: **90 / 100**
**Confidence: High** (coherence map + KB/SI separation scan are textual checks.)

PRD, SI, and KB line up tightly; no orphaned requirements; separation is clean.

- PRD's 7 capabilities each map to an SI workflow + an SI capability-specific output format (see coherence map). PRD §7 self-checkable success criteria are carried verbatim into SI §4 Criteria; PRD's external-only criterion ("user finds it useful") is correctly excluded from the SI.
- Role consistent across PRD §1 and SI §1. Output formats align (PRD §5 ↔ SI §6), with length norms deliberately compressed in the SI due to the 8,000-char limit (group documents this as a conscious trade-off in the eval).
- **KB/SI separation is clean — no −50 trigger.** The SI holds behaviour (role, scope, workflow, criteria, output structure, edge cases). The KB holds domain knowledge. No framework *definitions*, country-pattern explanations, or expanded BATNA/ZOPA academic content leak into the SI. The only separation tension is the SI §7 worked example, which carries some Japan-specific content — but a worked example legitimately needs domain content, and the group itself flagged this (Part A Check 4 / finding #7). KB has only mild "a negotiator should…" methodological phrasing, which is methodology, not agent runtime behaviour.

*Why 90 not higher:* the deliberate SI compression means several PRD specifics (minimum-context-by-request-type, framework-selection logic, per-format length norms) are weaker in the SI than in the PRD — the group's own Part A rates this the highest-priority gap. It is a specificity loss, not a contradiction, so it sits at the top of the band rather than above it.

---

## Dimension 4 — Evaluation Honesty: **92 / 100**
**Confidence: Medium** (structural checks reliable; tone/sharpness judgement is partly subjective.)

One of the strongest evals in the cohort. Sceptical, hunts problems, closes the loop on a hard case.

- **Part A surfaces 12 findings** (minimum is 3), each with location (PRD/SI/KB), severity (High → Low), and a concrete recommended fix — e.g. finding #1 "missing minimum-context rule by request type" (High, with exact replacement wording), #7 "Japan-case over-anchoring in SI example."
- **Part B uses a genuinely out-of-axis case.** AgroSense Italia × DanubeFresh Logistics (Italian-Bulgarian) is *not* one of the KB's regional profiles (East Asia / Western Europe / LatAm / Middle East). Testing on an axis the KB doesn't directly cover is a real generalisation stress-test, not a softball.
- **Full first output present** (not summarised — ~600 lines: facts/assumptions, cultural context, 5 risks, 7-stakeholder map, BATNA/RV/ZOPA, leverage, value creation, concession rules, opening approach, 18 verification questions).
- **Diagnosis traces each gap to an SI root cause** (gap / ambiguity / tension) with an **exact combined SI patch** shown, then redeploys.
- **Full second output present and textually distinct** — measurably shorter, KB references removed, framework grounding integrated, fewer questions. Real iteration, not a re-run.
- **Honest residual weaknesses after retest:** still slightly above the 900–1,400-word norm; 8 verification questions vs the new 5–7 target ("Partially worked"); stakeholder map less detailed than run 1. The group does not declare victory.

*Why 92 not higher:* the residual failure is presentation-discipline (length, question count), not a residual *analytical* failure — the very top of the band is reserved for an eval that surfaces a substantive reasoning gap that survives iteration. Self-scoring (8.5 → 9 / 10) is mildly generous and uses the group's own scale rather than an external rubric. Both are minor against an otherwise rigorous, loop-closing evaluation.

---

## KB / SI separation scan

| Direction | Location | Excerpt | Belongs | Severity |
|---|---|---|---|---|
| Domain → SI | SI §7 Example | Japan-specific cultural content (Hall/Meyer high-context, nemawashi consensus) inside the worked example | KB (regional patterns) — but legitimate in a worked example | Low (flagged by group, finding #7) |
| Behaviour → KB | KB methodology chunks | Occasional *"a negotiator should…"* phrasing | Acceptable as methodological advice (about the negotiator, not the agent) | Negligible |

**Violations counted toward −50:** 0 structural, 0 of "≥3 distinct" magnitude. **−50 NOT triggered.** The SI carries no framework definitions, no country-pattern explanations, no expanded academic citations; the KB carries no agent workflows, response templates, or "ADRELIX must…" runtime commands.

---

## Citation table (KB)

Canonical course texts — **Verified on sight** (recur throughout): Fisher, Ury & Patton 2011; Raiffa 1982/1985; Malhotra & Bazerman 2007/2008; Lewicki, Barry & Saunders 2015; Hall 1976/1983; Meyer 2014/2015; Hofstede 1980/2001 & Hofstede, Hofstede & Minkov 2010; House et al. 2004 (GLOBE); Trompenaars & Hampden-Turner 1997/2012; Earley & Ang 2003.

Non-canonical / oddly-specific — **web-verified (≥2 query variations)**:

| Citation | Status | Evidence |
|---|---|---|
| Tey, Schaerer, Madan & Swaab, 2021 | Verified | "The Impact of Concession Patterns on Negotiations," *OBHDP* 165:153-166 (PsycNet / Elsevier / RePEc) |
| Khakhar & Rammal, 2013 | Verified | "Culture and business networks: International business negotiations with Arab managers," *Int. Business Review* 22(3):578-590 (ScienceDirect / RePEc) |
| Anwar, 2019 | Verified | "Kraft's acquisition of Cadbury…," *Thunderbird Int. Business Review* (Wiley tie.21995) |
| Buttery & Leung, 1998 | Verified | "The difference between Chinese and Western negotiations," *European Journal of Marketing* 32(3-4):374 (Emerald) |
| Berger et al., 2021 | Verified | B2B wasta scale development/validation, *JBIM* 36(12):2201 (Emerald) |
| Hollmann et al., 2010 | Verified | "The DaimlerChrysler merger — a cultural mismatch?" (journal vol. 2010, Redalyc 273419412010 / ResearchGate) |

Remaining non-canonical citations (Kim & Fragale 2005; Roth, Murnighan & Schoumaker 1988; Galinsky & Mussweiler 2001; Kahneman & Tversky 1979; Lax & Sebenius 1986; Pruitt 1981; Bazerman & Gillespie 1999; Chhokar, Brodbeck & House 2007; McSweeney 2002; Singelis et al. 1995; Gelfand et al. 2011; Imai & Gelfand 2010; Groves, Feyerherm & Gu 2015; Elfenbein 2015; Benét-Martínez et al. 2002; Minkov 2011; Berry 2005; Adair, Okumura & Brett 2001; Yeung & Tung 1996; Brett, Gunia & Teucher 2017; Graham & Sano 1989; Brett & Gelfand 2006; Hooker 2012; Moran, Abramson & Moran 2014; Shaalan et al. 2013; Sakyi 2019; INCAE Business School 2024) are all well-established works in the negotiation / cross-cultural literature. The most obscure ones were sampled and all verified cleanly.

**Fabricated citations: 0.**

---

## Coherence map (PRD ↔ SI)

| Check | Result |
|---|---|
| PRD §3 capabilities ↔ SI §5 workflows | Pass — all 7 capabilities (full plan, cultural briefing, risk scan, stakeholder map, strategy, opening, previous-negotiation) have matching SI workflow lines |
| PRD §5 output format ↔ SI §6 | Pass — 7 capability-specific formats carried over; length norms compressed (documented trade-off) |
| PRD §7 success criteria ↔ SI §4 Criteria | Pass — 4 self-checkable criteria operationalised; external "usefulness" criterion correctly excluded from SI |
| PRD §1 role ↔ SI §1 role | Pass — consistent ADRELIX identity, strategic-advisor stance, culture-as-hypothesis |
| SI §7 example ↔ SI §1–6 rules | Pass — Germany-SaaS/Japan-distributor example obeys the workflow (context → culture-as-hypothesis → risks → stakeholders → strategy → opening); compressed but consistent |

No contradictions or orphaned requirements found.

---

## Artefact subtotal

| Dimension | Score |
|---|---|
| Domain Rigour | 94 |
| Generalisation | 93 |
| Coherence of Design | 90 |
| Evaluation Honesty | 92 |
| −50 KB/SI separation | Not triggered |
| **Subtotal** | **369 / 400** |

---

## Items requiring instructor judgement

1. **Agent Quality (/100) is scored live** by the instructor from the presentation/demo. Not assessed here. The /400 above is the document subtotal only; no /500 or verdict is asserted.
2. **Substantive accuracy** of the domain claims and case interpretations (e.g. the nemawashi/ringi description, the Danone-Wahaha and GE-Honeywell analyses) is **not** graded — existence-only on citations.
3. **Contribution flag: none.** All three members (Spada, Taferner, Blazheva) have a described role in the manifest; no member is shown as non-contributing or blank. No deduction recommended.
4. **Minor format note (no deduction):** the group/members file was submitted as `GROUP MANIFEST.pdf` rather than `group.md`; all members carry first + last name. The KB/PRD/SI/eval are all `.md`.

---

## Limitations footer

- Agent Quality is not assessed here — the instructor scores it live from the demo.
- Substantive accuracy of domain claims is not verified — existence-only on citations, attribution accuracy not checked.
- Citation verification is existence-only, not claim-attribution.
- Provenance of artefacts is not verified.
- Confidence ratings are heuristic, not statistical.
