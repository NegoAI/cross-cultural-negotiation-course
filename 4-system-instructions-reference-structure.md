# 4. System Instructions

> Step 4 of 5. The System Instructions are the operational text you paste into your Claude Project or ChatGPT Project. They tell the agent **how to behave**, drawing on what it **knows** (the KB from Step 2) to deliver what the PRD said it would do (Step 3).

## Why the SI is the last design step

The KB and the PRD are decisions on paper. The SI is the executable contract. By the time you write it, all the design questions should already be answered — the SI is a translation, not an invention. If you find yourself making new design decisions while writing the SI, stop and update the PRD first.

## What this file is and is not

A **reference structure**, not a template. Names the sections, explains what each one is for, and points to the corresponding PRD section. You write the SI in whatever shape works for you, but it must cover everything below.

## What the SI looks like in practice

The SI is a single markdown document — anywhere from one to a few pages — that you paste into the configuration field of your Claude Project or ChatGPT Project. The agent reads it on every turn before reading the user's input. Markdown headings, bullet lists, tables, and brief examples all work.

You do not need XML tags or any special syntax for this project. The production methodology this is drawn from uses an XML structure for very large agents; at student weight, clean markdown is enough.

## The seven sections of the SI

### 1. Role  ←  PRD §1

A clear role definition in the second person: "You are [Name], a [role]…". One focused paragraph. Personality traits expressed as behavioural directives, not as adjectives — not "you are direct and challenging" but "you push back when the user's reasoning skips a step, and you name the assumption you are challenging".

### 2. Context  ←  PRD §2, §6

Who the agent serves and in what situations. What the agent has access to (a Knowledge Base of negotiation methodology and cross-cultural frameworks). Operating constraints. What the agent does not do.

A subtle but important rule: this section refers to the KB by **category** of content, not by specific document names or section numbers. Do not write "consult Part 1 Section 3 of the KB"; write "consult the negotiation preparation framework in your KB". Specific document references belong inside the agent's runtime — not hard-coded into the SI text.

### 3. Knowledge Base Usage

Three to five rules for how the agent consults its KB. When to reference it, how to combine sections when a question spans topics, what to do when the KB does not cover something (acknowledge the gap; do not improvise domain facts).

This section tells the agent how to **use** the KB. It does not contain KB content. If you find yourself writing a Hofstede dimension or a BATNA definition here, that line belongs in the KB, not the SI.

### 4. Criteria  ←  PRD §7 (self-checkable success criteria + failure modes)

The quality standards the agent applies to its own output before responding. Each criterion specific and observable: not "be helpful" but "every cultural recommendation names the framework it came from and qualifies it with at least one exception".

Include both **positive checks** ("every response includes…") and **negative checks** ("never produce…"). Negative checks come from the failure modes you wrote in PRD §7. Stereotyping is a non-negotiable negative check for this agent.

### 5. Instructions (Workflow + Edge Cases)  ←  PRD §3, §4

The most substantial section. Two parts.

**Part A — Core Workflow.** The step-by-step process the agent follows on its primary task. Start from the capabilities in PRD §3 and sequence them: what does the agent do first when it receives input, what depends on what, where are the decision points. Imperative language: "When [trigger], do [action]". Not "you might consider".

Each step should be specific enough that another LLM reading only the SI could execute it without guessing. "Analyse the situation" is not a step. "Identify the cultural axis from the user's description; if more than one axis is in play, ask which the user wants prioritised" is a step.

**Part B — Edge Cases.** Explicit directives for boundary conditions. The pattern: "If [situation], then [specific action]". At minimum, cover:

- Out-of-scope requests
- Ambiguous input
- Missing information
- Contradictions in what the user has said
- Stereotyping risk — when the user offers a cultural generalisation as fact, the agent qualifies before acting

### 6. Output Format  ←  PRD §5

Response structure and formatting rules. Required elements that appear in every response and the order they appear in. Length guidance. A response template if the agent has a primary structured output.

### 7. Examples  ←  All PRD sections

One or two worked examples that show the agent in action. For each:

- **A realistic user input** — a real-looking message, not a perfect one
- **The full ideal agent response** — not an excerpt or summary; the complete response, following every rule in Sections 1–6

The example must comply with the rules. If Section 4 says "every recommendation names its framework", the example response names the framework. If Section 6 says "responses include a stakeholder map", the example response includes a stakeholder map. **Examples that contradict the rules teach the agent to ignore the rules** — they override written instructions in practice.

The first example covers the core workflow (the most common use case). If you write a second, pick an edge case — stereotyping risk, ambiguous cultural axis, out-of-scope request.

## How to do the work

- **Write section by section.** Do not draft the whole SI in one pass.
- **Use the PRD as your source.** When you write a section of the SI, name which PRD section(s) it draws from. If a directive does not trace to the PRD, either the PRD is missing something (go back) or the directive does not belong in the SI.
- **Use the model to translate, not to design.** The model can turn PRD prose into SI directives quickly. It cannot replace your design decisions.
- **Police the KB / SI line every section.** When domain knowledge — a framework, a fact, a definition — surfaces in your SI draft, flag it for the KB and remove it from the SI.

## Common failure modes

- **Vagueness.** "Be culturally sensitive." Not a directive. Replace with specific actions.
- **Domain knowledge in the SI.** Hofstede explanations, BATNA definitions, country patterns. All of it belongs in the KB, not here.
- **No examples.** The example is where amateur SIs fall apart. Write at least one.
- **Examples that contradict the rules.** If the rule says "always cite the framework" and the example response does not cite the framework, the agent learns to skip the citation. Verify every rule against the example before finalising.
- **Edge cases ignored.** Part B of Section 5 is where the agent fails gracefully or falls apart. Take it seriously.
- **Specific KB references hard-coded.** "Consult Part 1 Section 3" is brittle and does not survive KB revisions. Refer by category instead.

## Deploying the SI

When the SI is finished:

1. Open your Claude Project or ChatGPT Project
2. Paste the SI into the instructions / system prompt field
3. Attach your KB as a file (Claude Project: project knowledge; ChatGPT Project: knowledge files)
4. Run a test message and verify the agent boots correctly — it knows its role, it consults the KB, it follows the output format

If anything is off, fix it in the SI document and redeploy. Do not edit only inside the platform — keep your SI document as the source of truth.

## Reference back to the methodology

The SI step compresses what the eight-stage methodology calls Phase 5. The full version uses a nine-tag XML structure with three layers of instructions and a self-improvement section. The seven sections above cover the same ground in plain markdown at student weight.

## When you are done with this step

Move to `5-evaluation.md` when the SI covers all seven sections, every PRD capability has corresponding SI text, the KB / SI separation is clean, at least one full worked example is present, and the agent boots correctly when deployed.
