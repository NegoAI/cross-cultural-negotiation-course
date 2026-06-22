#!/usr/bin/env python3
# Phase-2 FINAL gradebook. Re-graded four document dimensions against absolute
# bands (cohort-exemplar calibrated, drift-guarded). Adds Italian /30 columns.
# One row per student; Excel formulas re-indexed per row. Agent Quality left empty.
import csv, os

# (groupName, [DR,Gen,Coh,EvH], minus50, flag, comment, [(last,first),...])
# Re-graded vs Phase 1: ONLY change = Muriotto Domain Rigour 93->94 (inter-agent
# consistency: equal chunk discipline + more non-canonical cites verified than 94-peers;
# the 93 had penalised responsible anti-stereotyping hedging the rubric rewards).
groups = [
    ("Cross-Cultural Neg Advisor", [93,95,94,96], False, "",
     "Outstanding work. Your knowledge base is grounded in real, verified sources across both halves of the course, with the anti-stereotyping exceptions built out as their own sections — exactly what lets the agent generalise beyond one culture. The KB, PRD and System Instructions line up cleanly, with no behaviour leaking into the KB and no theory dumped into the SI. Your evaluation is the standout: it closes the iteration loop honestly and even flags where your own fix only partly worked, which counts for more than a polished evaluation that hides its weaknesses. To push higher: tighten the agreement-space reasoning (avoid merging non-comparable figures such as authority ceilings and informal signals into a single numerical range), and test the agent on a cultural axis well outside the German–Mexican case. Final mark pending the live agent-quality score from your presentation.",
     [("Levante","Giuseppe"),("Ferrandino","Nunzia"),("Bonadio","Riccardo"),("Franciolini","Beatrice"),("Safcencu","Ruxandra")]),

    ("HomeGround", [66,60,64,68], False, "",
     "Your strongest work is the real-case evaluation: you ran the Bologna case through two genuine rounds and showed concrete, distinct improvements between them, which is exactly the kind of honest iteration the project rewards, and the housing-negotiation focus is practical and well-targeted. The biggest issue is that a lot of operating instructions live in the wrong place — your knowledge base carries the output structure, the Before-You-Sign scoring rubric, message templates and 'the agent should…' rules that belong in the system instructions, while the frameworks you name (Hofstede, Hall, Meyer and others) are not grounded in any cited sources. To push this higher, move all the behavioural and output rules out of the knowledge base into the system instructions, cite the real sources behind each framework, align the output list between the PRD and the instructions, and add the anti-stereotyping exceptions (individual variation, biculturalism, generational and regional difference) as their own sections rather than scattered caveats. Final mark pending the live agent-quality score from your presentation.",
     [("Uysal","Baris"),("Alpdogan","Elif Reda"),("Alparslan","Poyraz")]),

    ("NegotiaTe", [94,88,89,91], False, "",
     "This is a genuinely strong submission — the knowledge base is deep and disciplined, every academic citation checks out (including the recent HBR 2025 piece), frameworks are taught with their limits, and the exceptions are built in as their own sections rather than footnotes. The evaluation is a real highlight: you stress-tested the agent on Germany, an axis you deliberately under-built, found a precise citation gap, fixed it, and showed the improvement in full. The main thing to tighten is consistency between your documents: you submitted two system-instruction files with no marker of which is canonical, and the evaluation's list of applied fixes doesn't fully match what's actually in those files. Next, push the regional depth onto a fourth, genuinely different culture (China or the Middle East) so generalisation matches the quality of your exception architecture. Final mark pending the live agent-quality score.",
     [("Rosso","Filippo"),("Celeste","Mattia"),("Seghezzi","Davide"),("Palermo","Mattia"),("Gualdrini","Francesca")]),

    ("Negocierge", [84,76,90,93], False, "",
     "This is strong, conscientious work. Your sourcing is excellent — every framework and regional pattern is tied to a real, correctly-cited source (you even got the archive numbers right), and your evaluation is genuinely honest: it hunts down its own residual failures after fixing the agent and explains why two of the three fixes did not land, which is exactly the right instinct. The PRD, system instructions and evaluation now line up cleanly around the same five-capability, seniority-calibrated Negocierge — the earlier file mismatch is resolved. The main thing left to build is the knowledge base itself: it is currently a raw dump of full source texts rather than a structured, chunked KB with its own sections and a dedicated exceptions layer, even though your SI addresses it as if those sections exist; giving it that structure would lift both rigour and generalisation. Next, push the evaluation to a second iteration on the governance deadlock you flagged. Final mark pending the live agent-quality score.",
     [("Caruso","Lorenzo"),("Cesari","Samuele"),("Ronzino","Matteo"),("Schiantarelli","Gianmarco"),("Vecchiarelli","Lorenzo")]),

    ("Cross-Cultural Kira Agent", [95,96,93,96], False, "",
     "This is outstanding work — the knowledge base is deep and genuinely two-sided, pairing real negotiation methodology with a full set of cross-cultural frameworks, and every citation we checked is real and accurately used. The exceptions section (individual variation, biculturalism, generational and regional shift, expatriate and corporate override) is a model of how to make an agent generalise beyond one test case, and your evaluation is refreshingly honest: you ran the agent live on a brand-new Denmark–Korea axis with no Korea card in the KB and openly surfaced where it fell short. The one thing to push next is tightening the routing rule you flagged yourselves (what happens when a single message triggers debrief and stress-test together) and the small version-string drift between the SI and the report. KB/SI separation is clean, so no deduction applies. Final mark pending the live agent-quality score.",
     [("Monaco","Edoardo"),("Accarino","Francesco"),("Ruggeri","Beatrice Vanda"),("Redaelli","Gabriele")]),

    ("CCN AI Agent", [91,88,93,96], False, "",
     "A genuinely strong, disciplined submission. The knowledge base balances both halves of the course well, every framework is treated with real substance rather than just named, and your citations are clean — nothing fabricated. The standout is your evaluation: it hunts for problems honestly, runs a full real-case iteration with distinct before/after outputs, and even admits a recurring blind spot rather than declaring victory. The one area to push next is generalisation — your deep, multi-chunk treatment really only lands on the France-China case, so the other axes lean on broad regional sketches and the evaluation runs to carry breadth; giving a second axis the same depth in the KB would lift it. Final mark pending the live agent-quality score.",
     [("Bolis","Matteo"),("Bonarini","Lorenzo"),("Fino","Gregorio"),("Pozzi","Lorenzo"),("Samaritano","Samuel Maria")]),

    ("Cross-Cultural AI Agent", [96,97,88,90], False, "",
     "This is a genuinely strong submission. The knowledge base is deep and exceptionally well-sourced — both negotiation methodology and the cross-cultural frameworks are covered in real depth, ten regional clusters are each treated substantively, and the exceptions (individual variation, biculturalism, generational and expatriate adaptation) sit in their own section rather than as afterthoughts; every citation we checked is real. The evaluation is honest in the best way, surfacing a residual structural gap rather than declaring victory. The main things to tidy are small: a couple of copy-paste slips (a 'Brazilian' baseline inside a Japanese example, a 'five capabilities' header that defines six), one mis-attributed journal venue, and a leftover build note in the KB; reproducing the full second-round output would also have strengthened the eval. Polish these and it is excellent work — final mark pending the live agent-quality score.",
     [("Digirolamo","Annalisa"),("Viscione","Silvia"),("Mongodi","Francesco"),("Longo","Davide")]),

    ("the BRIDGE", [90,92,91,88], False, "",
     "This is a genuinely strong submission. The knowledge base is deep and exceptionally well-sourced — both halves of the course (negotiation methodology and cross-cultural frameworks) are covered with real substance, every citation we checked is real, and the work generalises properly: exceptions, biculturalism, generational and expatriate variation each get their own section rather than a footnote, so the agent isn't built around a single test case. The PRD, system instructions and evaluation line up cleanly with no behaviour leaking into the knowledge base. The one place to push next is the evaluation's verification layer — it rightly spots that the agent keeps uncertainty and evidence-tracking too implicit, and showing that fix demonstrated against the success criteria would lift the work further. Final mark pending the live agent-quality score.",
     [("Berto","Greta"),("de Souza Basso","Valentina"),("Monsurrò","Martina"),("Rizzato","Chiara"),("Scazza","Vittoria")]),

    ("Kairos", [94,95,93,93], False, "",
     "This is a standout submission. The knowledge base is genuinely deep on both negotiation mechanics and the cultural frameworks, every source checks out, and the exception layer (biculturalism, cultural intelligence, company type, generation) is built as its own full section rather than a footnote - exactly what makes the agent general-purpose rather than single-case. The evaluation is honest and self-critical: it runs a real before-and-after on a deliberately hard Saudi/Gulf case and even flags a weakness that survived the fix. The one thing to tighten is a single mis-named journal in the bibliography and slightly lighter sourcing on a couple of regional profiles. Final mark pending the live agent-quality score.",
     [("Malerba","Arianna"),("Mastrogiacomo","Chiara"),("Codoni","Tommaso"),("Commodaro","Riccardo"),("Cairoli","Filippo")]),

    ("B.R.O.", [94,96,90,97], False, "",
     "This is a genuinely strong, well-built system. Your knowledge base is deep and disciplined — it covers both the negotiation methodology and the cross-cultural frameworks substantively, with the exceptions (biculturalism, generational shift, expatriate adaptation, regional variation) each given their own proper section rather than a footnote, and every cited source checks out as real. The standout is your evaluation: it is sceptical, runs the full first and second agent outputs, adds a real off-axis Chile/lithium case, and honestly names where the agent still falls short instead of declaring victory. The one thing to tighten is the PRD-to-SI alignment — a few requirements (most notably the cultural-qualification 'and' that became 'or') drifted between documents; your own checks caught most of these, so close that last gap. Final mark pending the live agent-quality score.",
     [("Rigola","Riccardo"),("Rossi","Francesco"),("De Lorenzo","Andrea"),("Chiodaroli","Sergio"),("Longhini","Niccolò")]),

    ("ACROSS", [92,93,87,91], False, "",
     "This is a genuinely strong submission: a deep, well-cited knowledge base covering both halves of the course, all ten cultural clusters, and every exception as its own proper section, paired with an unusually honest evaluation that admits where the agent still fell short after revision. The one thing to clean up is document separation — some behavioural 'how to act' guidance was left inside the knowledge base the agent reads, in blocks you yourselves had already marked as not belonging there. Because you had labelled them correctly, this reads as a packaging slip rather than a design flaw, so it carries no penalty — but a clean compile step that strips that build-time material (both the behavioural blocks and the leftover research scaffolding) would have avoided it. Next, push every behavioural directive fully into the system instructions and ship a runtime knowledge base free of research scaffolding. Final mark pending the live agent-quality score.",
     [("Baggio","Anna"),("Wilmink","Pepijn"),("Calesini","Benedetta"),("Foltran","Gianluca"),("Belfrond","Simone")]),

    ("CCNA", [88,90,74,86], 10, "−10 KB/SI separation (self-diagnosed, unremediated)",
     "This is a strong submission built on an excellent knowledge base: both negotiation methodology and the cross-cultural frameworks are covered with real substance, your citations all check out, and — best of all — the anti-stereotyping exceptions (within-country variation, biculturalism, generational and regional difference) appear as their own proper sections, which is exactly what makes the agent general rather than a single-case tool. The evaluation is genuinely self-critical, which we value. The one real problem — and the reason for a small 10-point deduction — is document separation: operating rules and output-selection logic that belong in the System Instructions are embedded inside the Knowledge Base, where the agent reads them at runtime. What makes it count is that you diagnosed this exact issue yourselves in Part A and still submitted without fixing it; a known, unremediated leak earns the deduction. Tidying that, plus removing the leftover editing notes pasted into the SI, is the highest-value next step. Final mark pending the live agent-quality score.",
     [("Trevisani","Gabriella"),("Napoli","Giordana"),("Montingelli","Chiara"),("Piacentini","Aurora"),("Manno","Sofia")]),

    ("CROSSBRIDGE AI", [96,96,94,95], False, "",
     "This is outstanding, genuinely top-band work. Your knowledge base is rich and well-built — both halves of the course are covered in real depth, every chunk follows the principle/explanation/example shape, the regional patterns refuse to treat any region as one bloc, and all five exception types (individual variation, biculturalism, generational shift, expatriate adaptation, within-country variation) stand as their own full sections rather than footnotes. Your citation discipline is exemplary: we found zero fabrications, and the documents line up cleanly with no behaviour leaking into the KB or domain knowledge dumped into the instructions. The single thing that would have pushed the evaluation to perfect is the one your own report honestly names — you identify but do not run the hardest test, a case where the leading cultural hypothesis turns out to be wrong; running that round next is the obvious next push. Final mark pending the live agent-quality score.",
     [("Rozzi","Caterina"),("Geroldi","Filippo"),("Giacobone","Alessandro"),("D'Alterio","Paolo"),("Solomon","Cosmina")]),

    ("ADRELIX", [94,93,90,92], False, "",
     "This is outstanding work. Your knowledge base is deep and genuinely course-complete — it covers both the negotiation methodology and all the major cultural frameworks with real substance, treats exceptions (individual variation, biculturalism, generation, expatriate and sub-national differences) as their own proper section rather than an afterthought, and every citation we checked is real. Your evaluation is one of the strongest we have seen: you tested the agent on an Italian-Bulgarian case that sits outside your own regional profiles, showed both full outputs, traced each weakness to a specific instruction, and were honest about what was still imperfect after the fix. The one real constraint is that your system instructions are right at the platform's character limit, which forced you to compress some of the detail the PRD specifies (most notably the minimum-context rules per request type) — that is the first place to invest if you get more room. Final mark pending the live agent-quality score.",
     [("Spada","Elisa Silvia"),("Taferner","Felix"),("Blazheva","Adriana")]),

    ("CCN AI AGENT (CultureBridgeAI)", [94,93,91,95], False, "",
     "This is outstanding document work. The knowledge base is deep and genuinely two-sided — negotiation mechanics and cross-cultural frameworks both treated with real substance, every framework carrying its own limitations, and a citation list where every source we checked is real and exact. Generalisation is broad, with eight cultural regions and proper standalone sections for within-culture variation, biculturalism, generational and industry shifts. The clear standout is your evaluation: it is sceptical, it runs the full input-to-improved-output loop honestly, and it has the rare courage to report that two of its three fixes only half-closed rather than claiming a clean sweep. The one thing to push next is the small residual drift you already spotted yourselves — the variance-driver list still living in two slightly different forms in the system instructions. Final mark pending the live agent-quality score.",
     [("Biondi","Federico"),("Pozzi","Bruno"),("Manzin","Federico"),("Lotti","Santi"),("Finetti","Lorenzo")]),

    ("CCN AI Agent Culturae", [94,93,90,91], False, "",
     "This is a genuinely strong submission. Your knowledge base is deep and well-built — both halves of the course are covered with real substance rather than framework name-dropping, the exceptions (biculturalism, expatriate adaptation, generational and regional variation) get their own proper sections, and every single citation checks out as real. The KB, PRD and system instructions line up cleanly, and your evaluation is refreshingly honest: it hunts for problems, runs a full iteration loop, and admits openly that the one fix was confirmed on just one of the five test axes. The single thing to push next is closing that gap — re-run the other axes through the revised agent to show the improvement generalises, rather than demonstrating it once. Final mark pending the live agent-quality score.",
     [("Amendola","Sara"),("Bejko","Angelo"),("Nikolic","Marina"),("Jia","Yuan"),("Righino","Tommaso")]),

    ("CCN AI Agent", [94,94,92,95], False, "",
     "This is an excellent, carefully built submission. Your knowledge base is deep and genuinely source-grounded — every concept comes with an example, a caveat, and a real citation, and your anti-stereotyping exceptions each have their own section rather than being tucked away. The evaluation is the standout: it reproduces full before-and-after agent outputs, traces each weakness to a root cause, and honestly admits where a fix only partly worked. The one thing to push next is exactly what you spotted yourselves — tightening the agent's output so it stays decision-ready rather than workbook-dense. Final mark pending the live agent-quality score.",
     [("Bonacina","Francesco"),("Foà","Ilaria"),("Licci","Pasquale"),("Muni","Alessandro Emanuele"),("Muriotto","Giovanna")]),

    ("Aria agent", [96,97,96,97], False, "",
     "This is outstanding work. Your knowledge base is deep and genuinely general — it covers both negotiation methodology and the full range of cultural frameworks by negotiation axis, with nine regional profiles and, most impressively, every exception (individual variation, biculturalism, generational shift, expatriate adaptation, situational strength, context reversals) written as its own developed section rather than a footnote, and every framework chunk grounded in a real documented case. The PRD, system instructions and KB line up cleanly, with the taxonomy living only in the KB and the workflow only in the SI. Your evaluation is the standout: it scores your own agent strictly, refuses to flatter it, traces each gap to exact SI text, shows a real first-vs-second iteration, and ends by naming a failure that survives the fix. The single thing to push next is the one you already identified — grounding the regional-profile claims (e.g. the Vietnam pacing point) and adding the contract-precision material to the KB so the new checks have something real to retrieve against. Final mark pending the live agent-quality score.",
     [("Bolla","Martina"),("Dell'Orto","Martina"),("Pichler","Noa"),("Piccolo","Annachiara"),("Picari","Paola")]),

    ("CCN AI Agent", [94,93,91,89], False, "",
     "This is one of the strongest document sets in the cohort: a deep, well-structured Knowledge Base that covers both negotiation methodology and the cross-cultural frameworks with real substance, every citation genuine, clean separation between what the agent knows and how it behaves, and a multi-axis design with the exceptions (individual variation, biculturalism, organisational and regional variation) given their own sections rather than buried. The evaluation is genuinely self-critical — full first and second outputs, a precise SI patch, a four-case portfolio and an honest residual-limitations section. The main thing to tighten next time is the evaluation's numeric self-scoring, which leans flattering (long runs of near-perfect case scores), and the small gap between the shown iteration output and the deployed Project; keeping the two System-Instruction versions in sync is also worth watching. Excellent, rigorous work overall — final mark pending the live agent-quality score.",
     [("Antonucci","Sara"),("Corà","Matilde"),("Di Cesare","Livia"),("Folcia","Cristina"),("Tettoni","Chiara")]),
]

out = r"C:\Users\yrana\repos\cross-cultural-negotiation-course\assessments\cohort-gradebook-final.csv"

# Preserve any Agent Quality (col I, index 8) the instructor has already typed into
# the existing CSV — that column is HIS, scored live, and must survive a regenerate.
existing_aq = {}
if os.path.exists(out):
    with open(out, newline="", encoding="utf-8") as f:
        r = csv.reader(f)
        next(r, None)  # skip header
        for row in r:
            if len(row) > 8 and row[8].strip():
                existing_aq[(row[0], row[1])] = row[8]

rows = [["Last name","First name","Group name","Domain Rigour","Generalisation",
         "Coherence of Design","Evaluation Honesty","Artefact subtotal /400",
         "Agent Quality","Final /500","Score /30","Score /30 (rounded)","Flag","Comments"]]

n = 1  # header is row 1
for gname, sc, penalty, flag, comment, students in groups:
    for last, first in students:
        n += 1
        h = f"=SUM(D{n}:G{n})-{int(penalty)}" if penalty else f"=SUM(D{n}:G{n})"
        i = existing_aq.get((last, first), "")  # keep instructor's live Agent Quality
        j = f"=H{n}+I{n}"
        k = f"=J{n}/500*30"
        l = f"=ROUND(K{n},0)"
        rows.append([last, first, gname, sc[0], sc[1], sc[2], sc[3], h, i, j, k, l, flag, comment])

if existing_aq:
    print(f"Preserved Agent Quality for {len(existing_aq)} existing rows.")
with open(out, "w", newline="", encoding="utf-8") as f:
    csv.writer(f).writerows(rows)

print(f"Wrote {len(rows)-1} student rows across {len(groups)} groups to {out}")
