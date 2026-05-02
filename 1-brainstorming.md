# 1. Brainstorming

> Step 1 of 5. By the end of this step you have two things: a clear scope for your agent, and the body of source material you will turn into a Knowledge Base in Step 2.

## Why brainstorming first

Most agent projects fail at this step, not at the technical ones. A vague scope produces a vague KB, a vague PRD, a vague SI, and an agent that pretends to be useful without ever actually being useful. And without source material, the KB you build in Step 2 is just whatever the model happened to remember — which is exactly what we are trying to avoid.

In the eight-stage methodology this project is drawn from, this single student step combines three early stages: **deep research** on the domain, **comprehension** of the frameworks, and **clarifying questions** that surface the requirements. We collapse them because at student scale the boundary is blurry. What matters is that by the end of this step, you have both halves done.

## What you produce

### Output A — A scoping document

Short. Call it whatever you want, store it however you want. It must answer each of these questions specifically:

- **What is this agent?** One sentence. If you cannot say it in one sentence, the scope is still fuzzy.
- **Who is the typical user?** A specific role, with specific knowledge and specific gaps. "An executive" is not specific. "A senior commercial manager negotiating cross-border supply contracts, fluent in negotiation but not in cultural frameworks" is.
- **When does the user open the agent?** Before a negotiation? Mid-negotiation? Post-mortem? In preparation week? Each moment shapes the agent differently.
- **What does the agent do?** Three to six concrete capabilities. "Helps the user prepare" is a non-answer. "Builds a stakeholder map of the counterpart side, surfaces likely cultural risks, and proposes opening moves the user can pressure-test" is an answer.
- **What does the agent NOT do?** This matters as much as what it does. Does it write opening offers? Roleplay the counterpart? Predict outcomes? Coach soft skills? Give legal advice? Decide.
- **What does expert-level performance look like?** If your agent did its job perfectly, what would the user notice that they would not notice with a competent-but-not-expert agent? Be concrete. "Surfaces three cultural risks the user had not considered, with the framework that explains each" is concrete. "Helps the user feel prepared" is not.

### Output B — Source material for the Knowledge Base

A curated corpus of documentation that your agent will need to know from. **The KB you build in Step 2 will be drawn from this material — it is not built from the model's general training.** If you skip this work, the model will fill the KB with plausible-sounding generalities and your agent will hallucinate confidently.

The corpus must cover both halves of the course:

- **Negotiation methodology** — preparation frameworks, BATNA/ZOPA, leverage analysis, value creation, integrative vs. distributive moves, concession strategy, post-negotiation review. Use the negotiation frameworks taught in this course as your spine; supplement with classics (Fisher & Ury, Lewicki, Raiffa, Malhotra) where useful.
- **Cross-cultural frameworks** — Hofstede, Trompenaars, Meyer (Culture Map), GLOBE, Hall (high/low context, monochronic/polychronic), and any others you cover in class. For each, you need enough source material to write the framework's *core dimensions, how to apply them, and where they fail* — not just the names of the dimensions.
- **Country and regional patterns relevant to negotiation** — communication style, hierarchy, decision-making processes, time orientation, trust-building, conflict handling. The agent has to be general (any cultural axis), so the corpus has to span more than one region.
- **The exceptions to the frameworks** — individual variation, biculturalism, generational shifts, expatriate adaptation, regional variation within a country. As important as the frameworks themselves. Without this material, your agent will stereotype.
- **Real cases** — at least a few documented cross-cultural negotiation cases (M&A, supply, joint venture, diplomatic). Cases ground the frameworks in behaviour.

## How to do the work

You have access to paid Claude or ChatGPT. Use the **deep research** feature of either tool — that is what it is for. A few practical notes:

- **Run deep research on each major area separately.** One research run on negotiation methodology, one on cross-cultural frameworks, one on the regional patterns you want covered, one on the exceptions and individual variation. Trying to research everything at once produces shallow output.
- **Save what you get.** Keep the research outputs as files you can later feed into Step 2. Do not just read them and move on — Step 2 needs them in writing.
- **Verify citations as you go.** Deep research outputs cite sources; not all citations are real — models will produce plausible-looking citations to books or papers that do not exist. Before putting any cited fact in your KB, search the citation on Google Scholar or in a library catalogue. If you cannot find the source, treat the citation as fabricated and remove the fact. Doing this while the context is fresh is far faster than chasing the problem during the evaluation.
- **Use your course material first.** The frameworks taught in class are the spine. Deep research fills in around them — it does not replace them.
- **Use the model as a thinking partner for the scoping document.** Have it interrogate your scoping decisions, push back on vagueness, surface the questions you have not yet asked yourself. Do not let it just confirm your first idea.

## Common failure modes

- **Scope sprawl.** The agent ends up doing five different jobs. Pick one.
- **Generic user.** "A manager." Be specific.
- **Aspirational success.** "Helps the user feel prepared." Replace with observable behaviour.
- **No out-of-scope.** If you cannot name what the agent will not do, you have not scoped it.
- **Skipping the source material.** Easy to fall into because the model "already knows this stuff." It does not — not at the depth your agent needs, and not with citations you can defend.
- **Cultural side without negotiation side, or vice versa.** Both halves of the course must be in the corpus.
- **One region only.** The agent is general. Your corpus must be too.

## When you are done with this step

Move to `2-knowledge-base-guide.md` only when both outputs are in good shape: the six scoping questions are answered specifically in writing, and you have a folder of research material covering negotiation methodology, cross-cultural frameworks, regional patterns, exceptions, and at least a few real cases — enough that someone could open it and start building a Knowledge Base from what is in there.
