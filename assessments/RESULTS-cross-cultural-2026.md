# Cross-Cultural Negotiation 2026 — Final Results

**Course:** Cross-Cultural Negotiation · **Instructor:** Yadvinder S. Rana

Your project was graded against the project guidelines published on GitHub — the five
dimensions set out in the project README, each scored out of 100 for a total out of 500,
then converted to the Italian /30 scale:

- **Domain rigor** — the knowledge base grounded in real, verified frameworks from both
  halves of the course, no fabricated citations.
- **Generalization** — the agent supports any cultural axis, not only your test case.
- **Coherence of design** — KB, PRD and System Instructions line up; no behaviour leaking
  into the KB, no knowledge dumped into the SI.
- **Evaluation honesty** — the evaluation surfaces real weaknesses rather than hiding them.
- **Agent quality** — scored live from your presentation.

Each entry shows your members, the full score breakdown (the same columns as the official gradebook), and a written comment on what your group did well and the one or two things to push next. Groups are listed alphabetically. Where a deduction applies, it follows the single automatic rule in the README (behavior embedded in the KB, or knowledge dumped into the SI→ −50), applied here by degree of culpability.

---

## ACROSS

**Members:** Baggio Anna · Wilmink Pepijn · Calesini Benedetta · Foltran Gianluca · Belfrond Simone

| Domain Rigour | Generalisation | Coherence of Design | Evaluation Honesty | Artefact subtotal /400 | Agent Quality | Final /500 | Score /30 | Score /30 (rounded) | Final Score |
|---|---|---|---|---|---|---|---|---|---|
| 92 | 93 | 87 | 91 | 363 | 100 | 463 | 27.78 | 28 | 29 |

This is a genuinely strong submission: a deep, well-cited knowledge base covering both halves of the course, all ten cultural clusters, and every exception as its own proper section, paired with an unusually honest evaluation that admits where the agent still fell short after revision. The one thing to clean up is document separation — some behavioural "how to act" guidance was left inside the knowledge base the agent reads, in blocks you yourselves had already marked as not belonging there. Because you had labelled them correctly, this reads as a packaging slip rather than a design flaw, so it carries no penalty — but a clean compile step that strips that build-time material (both the behavioural blocks and the leftover research scaffolding) would have avoided it. Next, push every behavioural directive fully into the system instructions and ship a runtime knowledge base free of research scaffolding.

---

## ADRELIX

**Members:** Spada Elisa Silvia · Taferner Felix · Blazheva Adriana

| Domain Rigour | Generalisation | Coherence of Design | Evaluation Honesty | Artefact subtotal /400 | Agent Quality | Final /500 | Score /30 | Score /30 (rounded) | Final Score |
|---|---|---|---|---|---|---|---|---|---|
| 94 | 93 | 90 | 92 | 369 | 90 | 459 | 27.54 | 28 | 29 |

This is outstanding work. Your knowledge base is deep and genuinely course-complete — it covers both the negotiation methodology and all the major cultural frameworks with real substance, treats exceptions (individual variation, biculturalism, generation, expatriate and sub-national differences) as their own proper section rather than an afterthought, and every citation we checked is real. Your evaluation is one of the strongest we have seen: you tested the agent on an Italian-Bulgarian case that sits outside your own regional profiles, showed both full outputs, traced each weakness to a specific instruction, and were honest about what was still imperfect after the fix. The one real constraint is that your system instructions are right at the platform's character limit, which forced you to compress some of the detail the PRD specifies (most notably the minimum-context rules per request type) — that is the first place to invest if you get more room.

---

## Aria agent

**Members:** Bolla Martina · Dell'Orto Martina · Pichler Noa · Piccolo Annachiara · Picari Paola

| Domain Rigour | Generalisation | Coherence of Design | Evaluation Honesty | Artefact subtotal /400 | Agent Quality | Final /500 | Score /30 | Score /30 (rounded) | Final Score |
|---|---|---|---|---|---|---|---|---|---|
| 96 | 97 | 96 | 97 | 386 | 100 | 486 | 29.16 | 29 | 30 e lode |

Outstanding work. The knowledge base is deep and genuinely general — it covers both negotiation methodology and the full range of cultural frameworks by negotiation axis, with nine regional profiles and, most impressively, every exception (individual variation, biculturalism, generational shift, expatriate adaptation, situational strength, context reversals) written as its own developed section rather than a footnote, each framework chunk grounded in a real documented case. The PRD, system instructions and KB line up cleanly, with the taxonomy living only in the KB and the workflow only in the SI. The evaluation is the standout: it scores the agent strictly, refuses to flatter it, traces each gap to exact SI text, shows a real first-vs-second iteration, and ends by naming a failure that survives the fix. The single thing to push next is the one you already identified — grounding the regional-profile claims (e.g. the Vietnam pacing point) and adding the contract-precision material to the KB so the new checks have something real to retrieve against.

---

## B.R.O.

**Members:** Rigola Riccardo · Rossi Francesco · De Lorenzo Andrea · Chiodaroli Sergio · Longhini Niccolò

| Domain Rigour | Generalisation | Coherence of Design | Evaluation Honesty | Artefact subtotal /400 | Agent Quality | Final /500 | Score /30 | Score /30 (rounded) | Final Score |
|---|---|---|---|---|---|---|---|---|---|
| 94 | 96 | 90 | 97 | 377 | 100 | 477 | 28.62 | 29 | 30 |

This is a genuinely strong, well-built system. Your knowledge base is deep and disciplined — it covers both the negotiation methodology and the cross-cultural frameworks substantively, with the exceptions (biculturalism, generational shift, expatriate adaptation, regional variation) each given their own proper section rather than a footnote, and every cited source checks out as real. The standout is your evaluation: it is sceptical, runs the full first and second agent outputs, adds a real off-axis Chile/lithium case, and honestly names where the agent still falls short instead of declaring victory. The one thing to tighten is the PRD-to-SI alignment — a few requirements (most notably the cultural-qualification "and" that became "or") drifted between documents; your own checks caught most of these, so close that last gap.

---

## CCN AI Agent (Bolis)

**Members:** Bolis Matteo · Bonarini Lorenzo · Fino Gregorio · Pozzi Lorenzo · Samaritano Samuel Maria

| Domain Rigour | Generalisation | Coherence of Design | Evaluation Honesty | Artefact subtotal /400 | Agent Quality | Final /500 | Score /30 | Score /30 (rounded) | Final Score |
|---|---|---|---|---|---|---|---|---|---|
| 91 | 88 | 93 | 96 | 368 | 100 | 468 | 28.08 | 28 | 29 |

A genuinely strong, disciplined submission. The knowledge base balances both halves of the course well, every framework is treated with real substance rather than just named, and your citations are clean — nothing fabricated. The standout is your evaluation: it hunts for problems honestly, runs a full real-case iteration with distinct before/after outputs, and even admits a recurring blind spot rather than declaring victory. The one area to push next is generalisation — your deep, multi-chunk treatment really only lands on the France-China case, so the other axes lean on broad regional sketches and the evaluation runs to carry breadth; giving a second axis the same depth in the KB would lift it.

---

## CCN AI Agent (Muriotto)

**Members:** Bonacina Francesco · Foà Ilaria · Licci Pasquale · Muni Alessandro Emanuele · Muriotto Giovanna

| Domain Rigour | Generalisation | Coherence of Design | Evaluation Honesty | Artefact subtotal /400 | Agent Quality | Final /500 | Score /30 | Score /30 (rounded) | Final Score |
|---|---|---|---|---|---|---|---|---|---|
| 94 | 94 | 92 | 95 | 375 | 100 | 475 | 28.5 | 29 | 30 |

This is an excellent, carefully built submission. Your knowledge base is deep and genuinely source-grounded — every concept comes with an example, a caveat, and a real citation, and your anti-stereotyping exceptions each have their own section rather than being tucked away. The evaluation is the standout: it reproduces full before-and-after agent outputs, traces each weakness to a root cause, and honestly admits where a fix only partly worked. The one thing to push next is exactly what you spotted yourselves — tightening the agent's output so it stays decision-ready rather than workbook-dense.

---

## CCN AI Agent (Antonucci)

**Members:** Antonucci Sara · Corà Matilde · Di Cesare Livia · Folcia Cristina · Tettoni Chiara

| Domain Rigour | Generalisation | Coherence of Design | Evaluation Honesty | Artefact subtotal /400 | Agent Quality | Final /500 | Score /30 | Score /30 (rounded) | Final Score |
|---|---|---|---|---|---|---|---|---|---|
| 94 | 93 | 91 | 89 | 367 | 100 | 467 | 28.02 | 28 | 29 |

This is one of the strongest document sets in the cohort: a deep, well-structured Knowledge Base that covers both negotiation methodology and the cross-cultural frameworks with real substance, every citation genuine, clean separation between what the agent knows and how it behaves, and a multi-axis design with the exceptions (individual variation, biculturalism, organisational and regional variation) given their own sections rather than buried. The evaluation is genuinely self-critical — full first and second outputs, a precise SI patch, a four-case portfolio and an honest residual-limitations section. The main thing to tighten next time is the evaluation's numeric self-scoring, which leans flattering (long runs of near-perfect case scores), and the small gap between the shown iteration output and the deployed Project; keeping the two System-Instruction versions in sync is also worth watching. Excellent, rigorous work overall.

---

## CCN AI AGENT (CultureBridgeAI) — Biondi

**Members:** Biondi Federico · Pozzi Bruno · Manzin Federico · Lotti Santi · Finetti Lorenzo

| Domain Rigour | Generalisation | Coherence of Design | Evaluation Honesty | Artefact subtotal /400 | Agent Quality | Final /500 | Score /30 | Score /30 (rounded) | Final Score |
|---|---|---|---|---|---|---|---|---|---|
| 94 | 93 | 91 | 95 | 373 | 95 | 468 | 28.08 | 28 | 29 |

This is outstanding document work. The knowledge base is deep and genuinely two-sided — negotiation mechanics and cross-cultural frameworks both treated with real substance, every framework carrying its own limitations, and a citation list where every source we checked is real and exact. Generalisation is broad, with eight cultural regions and proper standalone sections for within-culture variation, biculturalism, generational and industry shifts. The clear standout is your evaluation: it is sceptical, it runs the full input-to-improved-output loop honestly, and it has the rare courage to report that two of its three fixes only half-closed rather than claiming a clean sweep. The one thing to push next is the small residual drift you already spotted yourselves — the variance-driver list still living in two slightly different forms in the system instructions.

---

## CCN AI Agent Culturae — Amendola

**Members:** Amendola Sara · Bejko Angelo · Nikolic Marina · Jia Yuan · Righino Tommaso

| Domain Rigour | Generalisation | Coherence of Design | Evaluation Honesty | Artefact subtotal /400 | Agent Quality | Final /500 | Score /30 | Score /30 (rounded) | Final Score |
|---|---|---|---|---|---|---|---|---|---|
| 94 | 93 | 90 | 91 | 368 | 100 | 468 | 28.08 | 28 | 29 |

This is a genuinely strong submission. Your knowledge base is deep and well-built — both halves of the course are covered with real substance rather than framework name-dropping, the exceptions (biculturalism, expatriate adaptation, generational and regional variation) get their own proper sections, and every single citation checks out as real. The KB, PRD and system instructions line up cleanly, and your evaluation is refreshingly honest: it hunts for problems, runs a full iteration loop, and admits openly that the one fix was confirmed on just one of the five test axes. The single thing to push next is closing that gap — re-run the other axes through the revised agent to show the improvement generalises, rather than demonstrating it once.

---

## CCNA

**Members:** Trevisani Gabriella · Napoli Giordana · Montingelli Chiara · Piacentini Aurora · Manno Sofia

| Domain Rigour | Generalisation | Coherence of Design | Evaluation Honesty | Artefact subtotal /400 | Agent Quality | Final /500 | Score /30 | Score /30 (rounded) | Final Score |
|---|---|---|---|---|---|---|---|---|---|
| 88 | 90 | 74 | 86 | 328 | 90 | 418 | 25.08 | 25 | 26 |

*Includes a −10 deduction for a self-diagnosed, unremediated KB/SI leak (see comment).*

This is a strong submission built on an excellent knowledge base: both negotiation methodology and the cross-cultural frameworks are covered with real substance, your citations all check out, and — best of all — the anti-stereotyping exceptions (within-country variation, biculturalism, generational and regional difference) appear as their own proper sections, which is exactly what makes the agent general rather than a single-case tool. The evaluation is genuinely self-critical, which we value. The one real problem — and the reason for a small 10-point deduction — is document separation: operating rules and output-selection logic that belong in the System Instructions are embedded inside the Knowledge Base, where the agent reads them at runtime. What makes it count is that you diagnosed this exact issue yourselves in Part A and still submitted without fixing it; a known, unremediated leak earns the deduction. Tidying that, plus removing the leftover editing notes pasted into the SI, is the highest-value next step.

---

## Cross-Cultural AI Agent (NEXA) — Longo

**Members:** Digirolamo Annalisa · Viscione Silvia · Mongodi Francesco · Longo Davide

| Domain Rigour | Generalisation | Coherence of Design | Evaluation Honesty | Artefact subtotal /400 | Agent Quality | Final /500 | Score /30 | Score /30 (rounded) | Final Score |
|---|---|---|---|---|---|---|---|---|---|
| 96 | 97 | 88 | 90 | 371 | 90 | 461 | 27.66 | 28 | 29 |

This is a genuinely strong submission. The knowledge base is deep and exceptionally well-sourced — both negotiation methodology and the cross-cultural frameworks are covered in real depth, ten regional clusters are each treated substantively, and the exceptions (individual variation, biculturalism, generational and expatriate adaptation) sit in their own section rather than as afterthoughts; every citation we checked is real. The evaluation is honest in the best way, surfacing a residual structural gap rather than declaring victory. The main things to tidy are small: a couple of copy-paste slips (a "Brazilian" baseline inside a Japanese example, a "five capabilities" header that defines six), one mis-attributed journal venue, and a leftover build note in the KB; reproducing the full second-round output would also have strengthened the eval. Polish these and it is excellent work.

---

## Cross-Cultural Kira Agent

**Members:** Monaco Edoardo · Accarino Francesco · Ruggeri Beatrice Vanda · Redaelli Gabriele

| Domain Rigour | Generalisation | Coherence of Design | Evaluation Honesty | Artefact subtotal /400 | Agent Quality | Final /500 | Score /30 | Score /30 (rounded) | Final Score |
|---|---|---|---|---|---|---|---|---|---|
| 95 | 96 | 93 | 96 | 380 | 95 | 475 | 28.5 | 29 | 30 |

This is outstanding work — the knowledge base is deep and genuinely two-sided, pairing real negotiation methodology with a full set of cross-cultural frameworks, and every citation we checked is real and accurately used. The exceptions section (individual variation, biculturalism, generational and regional shift, expatriate and corporate override) is a model of how to make an agent generalise beyond one test case, and your evaluation is refreshingly honest: you ran the agent live on a brand-new Denmark–Korea axis with no Korea card in the KB and openly surfaced where it fell short. The one thing to push next is tightening the routing rule you flagged yourselves (what happens when a single message triggers debrief and stress-test together) and the small version-string drift between the SI and the report. KB/SI separation is clean, so no deduction applies.

---

## Cross-Cultural Neg Advisor

**Members:** Levante Giuseppe · Ferrandino Nunzia · Bonadio Riccardo · Franciolini Beatrice · Safcencu Ruxandra

| Domain Rigour | Generalisation | Coherence of Design | Evaluation Honesty | Artefact subtotal /400 | Agent Quality | Final /500 | Score /30 | Score /30 (rounded) | Final Score |
|---|---|---|---|---|---|---|---|---|---|
| 93 | 95 | 94 | 96 | 378 | 95 | 473 | 28.38 | 28 | 29 |

Outstanding work. Your knowledge base is grounded in real, verified sources across both halves of the course, with the anti-stereotyping exceptions built out as their own sections — exactly what lets the agent generalise beyond one culture. The KB, PRD and System Instructions line up cleanly, with no behaviour leaking into the KB and no theory dumped into the SI. Your evaluation is the standout: it closes the iteration loop honestly and even flags where your own fix only partly worked, which counts for more than a polished evaluation that hides its weaknesses. To push higher: tighten the agreement-space reasoning (avoid merging non-comparable figures such as authority ceilings and informal signals into a single numerical range), and test the agent on a cultural axis well outside the German–Mexican case.

---

## CROSSBRIDGE AI

**Members:** Rozzi Caterina · Geroldi Filippo · Giacobone Alessandro · D'Alterio Paolo · Solomon Cosmina

| Domain Rigour | Generalisation | Coherence of Design | Evaluation Honesty | Artefact subtotal /400 | Agent Quality | Final /500 | Score /30 | Score /30 (rounded) | Final Score |
|---|---|---|---|---|---|---|---|---|---|
| 96 | 96 | 94 | 95 | 381 | 90 | 471 | 28.26 | 28 | 29 |

This is outstanding, genuinely top-band work. Your knowledge base is rich and well-built — both halves of the course are covered in real depth, every chunk follows the principle/explanation/example shape, the regional patterns refuse to treat any region as one bloc, and all five exception types (individual variation, biculturalism, generational shift, expatriate adaptation, within-country variation) stand as their own full sections rather than footnotes. Your citation discipline is exemplary: we found zero fabrications, and the documents line up cleanly with no behaviour leaking into the KB or domain knowledge dumped into the instructions. The single thing that would have pushed the evaluation to perfect is the one your own report honestly names — you identify but do not run the hardest test, a case where the leading cultural hypothesis turns out to be wrong; running that round next is the obvious next push.

---

## HomeGround

**Members:** Uysal Baris · Alpdogan Elif Reda · Alparslan Poyraz

| Domain Rigour | Generalisation | Coherence of Design | Evaluation Honesty | Artefact subtotal /400 | Agent Quality | Final /500 | Score /30 | Score /30 (rounded) | Final Score |
|---|---|---|---|---|---|---|---|---|---|
| 66 | 60 | 64 | 68 | 258 | 95 | 353 | 21.18 | 21 | 22 |

Your strongest work is the real-case evaluation: you ran the Bologna case through two genuine rounds and showed concrete, distinct improvements between them, which is exactly the kind of honest iteration the project rewards, and the housing-negotiation focus is practical and well-targeted. The biggest issue is that a lot of operating instructions live in the wrong place — your knowledge base carries the output structure, the Before-You-Sign scoring rubric, message templates and "the agent should…" rules that belong in the system instructions, while the frameworks you name (Hofstede, Hall, Meyer and others) are not grounded in any cited sources. To push this higher, move all the behavioural and output rules out of the knowledge base into the system instructions, cite the real sources behind each framework, align the output list between the PRD and the instructions, and add the anti-stereotyping exceptions (individual variation, biculturalism, generational and regional difference) as their own sections rather than scattered caveats.

---

## Kairos

**Members:** Malerba Arianna · Mastrogiacomo Chiara · Codoni Tommaso · Commodaro Riccardo · Cairoli Filippo

| Domain Rigour | Generalisation | Coherence of Design | Evaluation Honesty | Artefact subtotal /400 | Agent Quality | Final /500 | Score /30 | Score /30 (rounded) | Final Score |
|---|---|---|---|---|---|---|---|---|---|
| 94 | 95 | 93 | 93 | 375 | 95 | 470 | 28.2 | 28 | 29 |

This is a standout submission. The knowledge base is genuinely deep on both negotiation mechanics and the cultural frameworks, every source checks out, and the exception layer (biculturalism, cultural intelligence, company type, generation) is built as its own full section rather than a footnote — exactly what makes the agent general-purpose rather than single-case. The evaluation is honest and self-critical: it runs a real before-and-after on a deliberately hard Saudi/Gulf case and even flags a weakness that survived the fix. The one thing to tighten is a single mis-named journal in the bibliography and slightly lighter sourcing on a couple of regional profiles.

---

## Negocierge

**Members:** Caruso Lorenzo · Cesari Samuele · Ronzino Matteo · Schiantarelli Gianmarco · Vecchiarelli Lorenzo

| Domain Rigour | Generalisation | Coherence of Design | Evaluation Honesty | Artefact subtotal /400 | Agent Quality | Final /500 | Score /30 | Score /30 (rounded) | Final Score |
|---|---|---|---|---|---|---|---|---|---|
| 84 | 76 | 90 | 93 | 343 | 90 | 433 | 25.98 | 26 | 27 |

This is strong, conscientious work. Your sourcing is excellent — every framework and regional pattern is tied to a real, correctly-cited source (you even got the archive numbers right), and your evaluation is genuinely honest: it hunts down its own residual failures after fixing the agent and explains why two of the three fixes did not land, which is exactly the right instinct. The PRD, system instructions and evaluation now line up cleanly around the same five-capability, seniority-calibrated Negocierge — the earlier file mismatch is resolved. The main thing left to build is the knowledge base itself: it is currently a raw dump of full source texts rather than a structured, chunked KB with its own sections and a dedicated exceptions layer, even though your SI addresses it as if those sections exist; giving it that structure would lift both rigour and generalisation. Next, push the evaluation to a second iteration on the governance deadlock you flagged.

---

## NegotiaTe

**Members:** Rosso Filippo · Celeste Mattia · Seghezzi Davide · Palermo Mattia · Gualdrini Francesca

| Domain Rigour | Generalisation | Coherence of Design | Evaluation Honesty | Artefact subtotal /400 | Agent Quality | Final /500 | Score /30 | Score /30 (rounded) | Final Score |
|---|---|---|---|---|---|---|---|---|---|
| 94 | 88 | 89 | 91 | 362 | 90 | 452 | 27.12 | 27 | 28 |

This is a genuinely strong submission — the knowledge base is deep and disciplined, every academic citation checks out (including the recent HBR 2025 piece), frameworks are taught with their limits, and the exceptions are built in as their own sections rather than footnotes. The evaluation is a real highlight: you stress-tested the agent on Germany, an axis you deliberately under-built, found a precise citation gap, fixed it, and showed the improvement in full. The main thing to tighten is consistency between your documents: you submitted two system-instruction files with no marker of which is canonical, and the evaluation's list of applied fixes doesn't fully match what's actually in those files. Next, push the regional depth onto a fourth, genuinely different culture (China or the Middle East) so generalisation matches the quality of your exception architecture.

---

## the BRIDGE

**Members:** Berto Greta · de Souza Basso Valentina · Monsurrò Martina · Rizzato Chiara · Scazza Vittoria

| Domain Rigour | Generalisation | Coherence of Design | Evaluation Honesty | Artefact subtotal /400 | Agent Quality | Final /500 | Score /30 | Score /30 (rounded) | Final Score |
|---|---|---|---|---|---|---|---|---|---|
| 90 | 92 | 91 | 88 | 361 | 90 | 451 | 27.06 | 27 | 28 |

This is a genuinely strong submission. The knowledge base is deep and exceptionally well-sourced — both halves of the course (negotiation methodology and cross-cultural frameworks) are covered with real substance, every citation we checked is real, and the work generalises properly: exceptions, biculturalism, generational and expatriate variation each get their own section rather than a footnote, so the agent isn't built around a single test case. The PRD, system instructions and evaluation line up cleanly with no behaviour leaking into the knowledge base. The one place to push next is the evaluation's verification layer — it rightly spots that the agent keeps uncertainty and evidence-tracking too implicit, and showing that fix demonstrated against the success criteria would lift the work further.
