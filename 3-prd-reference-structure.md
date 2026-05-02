# 3. PRD — Product Requirements Document

> Step 3 of 5. The PRD is the bridge between what your agent **knows** (the KB you built in Step 2) and what your agent **does** (the System Instructions you write in Step 4). It is a specification: a written commitment to what this agent is, who it is for, what it does, and how you will know it is working.

## Why the PRD exists

Without a PRD, the System Instructions are guesswork. You will write a directive, then second-guess it, then revise, then forget what you decided last week. The PRD forces the decisions out of your head and onto a page. Once it is written, the SI becomes a translation job rather than a design job.

This is the rule of **specification before construction**: define *what* before *how*. It is non-negotiable in production AI work, and it is the reason the methodology runs in this exact order — Knowledge Base (what the agent knows), PRD (what the agent does), System Instructions (how the agent behaves). Skipping the PRD or writing it after the SI flips the dependency and the SI ends up encoding decisions you have not actually made.

## What this file is and is not

This file is a **reference structure**, not a template. It tells you what each section of the PRD is for and what good looks like. It does not give you a fill-in-the-blanks form. You write the PRD in whatever shape works for you, but it must answer everything below.

## The seven sections of the PRD

### 1. Agent Identity & Role

Who is this agent? Give it a name. Write a one-paragraph description that explains both what it does and how it approaches its work — not just a restatement of the name. Define its core domain expertise (negotiation; cross-cultural intelligence; both, in your case) and two or three defining personality traits.

A reader who has never heard of your project should be able to picture the agent after reading this section.

### 2. Target Users

Who uses this agent? Their role, their seniority, their negotiation experience, their cross-cultural experience. The primary use cases — when and why a user opens the agent. What the user expects from the interaction.

You scoped this in Step 1. Sharpen it here. Be specific enough that the SI can calibrate vocabulary, depth, and assumption levels.

### 3. Core Capabilities

The specific things the agent can do. Each capability needs:

- **Trigger** — what user input or situation activates it
- **Process** — what the agent does internally (which KB sections it consults, which frameworks it applies, what reasoning it runs)
- **Output** — what the user gets (format, structure, depth)

List capabilities in priority order — most important first. "Helps the user prepare for a negotiation" is a non-capability. "Builds a stakeholder map of the counterpart side from the user's input, surfaces three to five likely cultural risks with the framework that explains each, and proposes opening moves the user can pressure-test" is a capability.

### 4. Interaction Guidelines

How a typical interaction flows from start to end. The agent's tone and communication style. How it handles ambiguity — does it ask clarifying questions, or interpret and proceed with a note? How it handles requests outside its scope.

This is where you commit to whether the agent is a sparring partner who pushes back, an advisor who lays out options, or a coach who asks questions. Pick one.

### 5. Output Format

The default structure of the agent's responses. Length norms. Required elements that appear in every response (e.g., "every recommendation cites the KB section it came from"). Any response template or skeleton the agent should follow for its main use case.

The SI in Step 4 will translate this into formatting rules. The clearer this section is, the cleaner that translation will be.

### 6. Boundaries & Constraints

What the agent does NOT do. Topics it declines or redirects. Limitations it should be transparent about. Domain-specific guardrails that matter for cross-cultural negotiation:

- The agent must not stereotype — when it generalises, it qualifies (see Step 2 on the exceptions).
- The agent should not give legal, HR, or compliance advice.
- Anything else specific to your scope.

If you cannot name what the agent will not do, you have not finished defining what it does.

### 7. Definition of Success

Three parts:

- **Success criteria** — three to five specific, observable indicators of a "good" response. Not "the response is helpful" but "the response surfaces at least one cultural risk the user had not raised, names the framework that explains it, and proposes one concrete move".
- **Failure modes** — two or three descriptions of what a "bad" response looks like. The mistakes the agent must avoid. Stereotyping is one. Generic culture-talk with no negotiation move is another. Add the ones specific to your agent.
- **Self-check vs external** — for each criterion, mark whether the agent can verify it in its own output (structural completeness, presence of required elements, length) or whether it requires user judgement (the user feels understood). Only the self-checkable ones become Criteria in the SI in Step 4. Flag the external ones — they are for your evaluation in Step 5, not for the agent.

## How to do the work

- Build the PRD section by section. Do not draft it all in one pass.
- Use the model as a sounding board: after each section, paste it back and ask "is this specific enough to drive a system instruction, or is it still vague?"
- Cross-check at the end. Every capability in Section 3 should appear somewhere in Section 4 (interaction) or Section 6 (boundaries) — a capability that exists nowhere in the flow is a gap. Section 5 (output) must accommodate everything Section 3 promises.
- Reference your KB explicitly in Section 3. When a capability requires the agent to consult specific Parts of the KB, name them.

## Common failure modes

- **Aspirational success criteria.** "The agent helps the user feel prepared." Replace with observable behaviour.
- **Capabilities without triggers, processes, or outputs.** All three are required for each one.
- **Contradictions between sections.** Section 3 says the agent asks clarifying questions; Section 4 describes a single-pass workflow with no question step. Resolve before moving on.
- **No failure modes.** Section 7 with only success criteria and no failure modes leaves the SI without negative checks. The agent only knows what good looks like and cannot recognise its own mistakes.
- **Drifting from Step 1.** Compare this PRD against the scoping document from Step 1. If the agent has quietly become a different agent, decide which version is correct and update the other.

## Reference back to the methodology

The PRD step compresses what the eight-stage methodology calls Phase 4 — the full version uses fifteen sections including a PRD-to-SI mapping table. The seven sections above cover the same ground at student weight. If you want the full version after the project, ask.

## When you are done with this step

Move to `4-system-instructions-reference-structure.md` when the PRD covers all seven sections, every capability has a trigger/process/output, success criteria are observable, failure modes are named, and the document is internally consistent.
