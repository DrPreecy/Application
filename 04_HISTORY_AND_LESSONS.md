# History & Lessons Report
## Application Operations System

### Purpose

This document preserves the real development path rather than presenting the current architecture as if it had been obvious from the beginning.

### Stage 1 — Application production as separate tasks

Initial work treated opportunity discovery, cover-letter production and CV production as separate activities. This was practical for experimentation but produced no shared durable model of an application case.

### Stage 2 — Quality failures revealed missing process

Application writing initially became too corporate and abstract. Iteration showed that truth, argument, voice and professionalization had to be solved in sequence. Approved content needed locking.

CV production initially mixed content and design. Image-based whole-page work caused stretching, weak text semantics, photo replacement problems and repeated redesign. The process evolved toward source truth, content selection, stable grids, native rendering and targeted changes.

### Stage 3 — Daily automation

The workflows were converted into three daily automations.

This created useful discipline but hid a structural flaw: scheduled times were acting as if they were dependencies.

### Stage 4 — Real race condition

Opportunity Intelligence could still be researching when Application Writer ran. Application Writer then concluded that there was no work. A daily “pipeline” had been created without an actual workflow state.

### Stage 5 — Eligibility over-blocking

Required tests and unknown personal facts demonstrated that one unresolved eligibility item could freeze unrelated work.

The corrected rule became:

> Block the dependency, not the opportunity.

Application/CV preparation can continue when the unresolved item affects only submission.

### Stage 6 — Shared-state workaround

Explicit handoff JSON and condition watches were introduced.

This improved reliability but made the architecture smell obvious: increasingly complex coordination existed only because one logical workflow had been split into several independent automations.

### Stage 7 — Application Operations System

The problem was reframed:

- persistent application lifecycle;
- shared truth;
- opportunity-centered state;
- bounded semantic workers;
- deterministic workflow/policy;
- package-level QA;
- user action queue.

### Stage 8 — External model review

Gemini and Grok independently recommended validation-first development, requirements traceability, architecture decisions, security, technical spikes and regression fixtures.

Their convergence strengthened the direction but did not validate the architecture.

### Stage 9 — Meta-red-team correction

The concept itself was attacked.

Key corrections:
- do not assume a custom app is necessary before H0;
- do not prematurely call Opportunity a DDD Aggregate Root;
- do not equate state-driven behavior with a mandatory event-driven/durable-workflow framework;
- avoid universal ATS claims;
- avoid fake 100% guarantees for probabilistic model quality;
- keep GitHub as development source of truth, not production PII vault;
- design around browser-first cloud agents and their limits;
- use the Application Operations System as a real test case for the user's broader product-planning method.

### Durable lessons from the real application-writing work

- Truth before presentation.
- Real reasoning before polished prose.
- Professionalization may improve form but must not invent a more impressive person.
- Employer-specific facts matter only when they change the applicant's reasoning.
- One strong argument should not be repeated under new wording.
- The application must show both “why this employer” and “why invest in this applicant.”
- Approved paragraphs should be preserved when facts/strategy do not change.

### Durable lessons from the real CV work

- Data, content selection and design are separate layers.
- The document generator must not fill truth gaps with guesses.
- Layout follows content stability.
- The grid matters more than decorative objects.
- Photo is a layout asset, not a generative identity task.
- Final PDF should come from structured/native source.
- Local changes should not trigger broad regeneration.
- Content, layout, photo and export require explicit lock semantics.
- A successful one-off native rebuild is evidence of feasibility, not proof of a production pipeline.

### Current position

The project is now ready for **empirical validation and a walking skeleton**, not for immediate full-platform implementation.
