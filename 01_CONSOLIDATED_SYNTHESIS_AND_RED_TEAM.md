# Application Operations System
## Consolidated Architecture, Validation & Red-Team Report — v1.1

**Status:** Post-concept synthesis after internal redesign, Gemini review/blueprint, Grok blueprint, public-source research, and historical workflow evidence.

**Purpose:** Preserve how the project got here, separate established product decisions from attractive but premature implementation ideas, attack the concept as if it were wrong, and define the corrected development baseline before GPT-6 Astra/Codex begins implementation work.

## 1. Executive verdict

The project should continue, but **not** by converting the current concept directly into a production-grade “event-driven DDD platform.”

The strongest idea is not any specific workflow engine, database, agent framework, or “aggregate root.” The strongest idea is the product behavior that emerged from the real failures:

1. application work is one persistent system, not three isolated scheduled prompts;
2. each opportunity carries a traceable state across research, eligibility, fit, positioning, documents and user actions;
3. unknowns block only the work that actually depends on them;
4. truth, evidence, positioning and brand must be shared across application and CV work;
5. LLMs perform bounded semantic work; deterministic software owns authoritative state, transitions, validation and artifacts;
6. user approval is reserved for real human decisions, especially personal truth and submission;
7. accepted work must not be silently rewritten;
8. changes invalidate only dependent work;
9. research and document generation are useful only when they advance a real application;
10. the system must be able to sit idle without manufacturing tasks.

Those are the **validated-by-experience design pressures**. The proposed software architecture is still a hypothesis.

The next stage should therefore be a **browser-first, GitHub-native validation and walking-skeleton project**, not a large infrastructure build.

## 2. How we got here

### 2.1 Initial operating model

The system began as three scheduled activities:

- Opportunity Intelligence / job discovery and analysis
- Application Writer
- CV Compiler

This was initially convenient because each task was understandable in isolation.

### 2.2 Quality work inside the three modules

The modules were progressively improved.

Opportunity work gained:

- opportunity normalization;
- separate Fit and Eligibility;
- primary-source verification;
- evidence strength and provenance;
- program-quality analysis;
- positioning;
- application branding;
- research queues;
- “preferred is not mandatory” safeguards.

Application writing gained:

- truth lock;
- employer specificity;
- raw argumentation before polished prose;
- voice-first drafting;
- professionalization after voice;
- authenticity checks;
- content locking;
- “why me” and employer counterfactual checks.

CV work gained:

- applicant/career truth before layout;
- relevance selection separate from factual history;
- native document generation;
- ATS/text-extraction checks;
- photo immutability;
- geometry/layout locks;
- minimum-change behavior;
- content, layout, photo and export locks.

### 2.3 First structural failure: clocks were pretending to be dependencies

The three Dailies were scheduled at different times. This looked like a pipeline, but it was only three clocks.

A real failure demonstrated the problem:

- Intelligence was still researching.
- Application Writer started because its time had arrived.
- It observed no completed handoff.
- It concluded that there was no useful application work.

The architecture could not distinguish:

- “nothing useful exists” from
- “upstream work is still running” from
- “there is older backlog work” from
- “the current opportunity is partly ready.”

### 2.4 Second structural failure: readiness was too global

Formal uncertainties such as a required test or an unresolved citizenship fact caused excessive blocking.

The correct behavior is dependency-scoped:

- a test may block submission;
- it does not necessarily block fit analysis, positioning, application drafting or CV preparation;
- an unknown user fact should block only the decisions that depend on that fact.

This led to multi-axis readiness and explicit user-action items.

### 2.5 Intermediate workaround: shared handoff files and condition watches

A shared-state workaround was created between the three scheduled automations.

This solved some immediate problems:

- explicit run state;
- stable opportunity IDs;
- positioning/brand version references;
- downstream conditional execution;
- fewer false “nothing to do” conclusions.

But it exposed the deeper issue: the system was spending architecture on coordinating three prompts that were conceptually parts of one application workflow.

### 2.6 Paradigm shift

The system was reframed as an **Application Operations System** with:

- persistent shared state;
- opportunity-centered work;
- a work queue;
- bounded specialist heads;
- package-level QA;
- explicit user actions;
- dependency-aware invalidation.

The Dailies became potential triggers, not the system architecture.

### 2.7 External review stage

Two large independent model reviews were then gathered.

Gemini strongly supported:

- validation-first development;
- requirements traceability;
- architecture decision records;
- walking-skeleton development;
- schema and semantic validation;
- security/privacy;
- persistent workflow and versioning.

Grok independently converged on:

- preserving the concept while validating assumptions;
- proportional requirements engineering;
- domain/data/workflow modeling;
- ADRs and technical spikes;
- real-failure regression fixtures;
- browser-independent agent work;
- security from the beginning;
- avoiding enterprise process theatre.

That convergence is meaningful, but **agreement between models is not product validation**. Both can share the same software-engineering priors and make the same wrong assumption.

## 3. What is established vs. still only proposed

### 3.1 Established from the project history and concept

- One coherent application lifecycle is preferable to three mutually ignorant prompt runs.
- Applicant truth must never be invented or silently upgraded.
- Fit and eligibility are separate dimensions.
- Missing information does not automatically make an opportunity unusable.
- Blocking must be scoped to dependencies.
- Research claims require provenance and correct scope.
- Application and CV must share a positioning basis.
- Application and CV should share a coherent document identity without being identical.
- User actions such as tests, documents or factual clarifications must be explicit.
- Submission is user-owned.
- Approved content/assets require controlled change, not broad regeneration.
- PDFs must be technically valid documents rather than whole-page raster images.
- No-op runs should not manufacture work.
- Material changes should invalidate only dependent outputs.
- The system should support persistent work rather than “today-only” thinking.

### 3.2 Derived but not yet proven

- Opportunity should be the primary domain anchor.
- A central work queue will outperform simpler per-opportunity processes.
- Positioning Contract and Brand Contract should be first-class persisted objects.
- Application and CV can often be generated independently once shared contracts are stable.
- A durable workflow runtime will be needed for the personal-live product.
- autonomous daily operation is worth its complexity and ongoing model cost.

### 3.3 Proposals that must NOT become requirements yet

These appeared in one or both external reviews but are not settled:

- “Opportunity” as a DDD Aggregate Root.
- Event Sourcing.
- CQRS.
- Temporal.
- Azure Durable Functions.
- AWS Step Functions.
- SQLite.
- PostgreSQL.
- SQLCipher.
- Pydantic.
- TypeScript.
- Typst as mandatory renderer.
- ReportLab as mandatory fallback.
- maximum exactly three retries.
- a specific 50-posting benchmark size.
- a commercial ATS parser requirement.
- a fixed seven-day Alpha.
- exactly ten Beta packages.
- 100% statistical guarantees for probabilistic model behavior.
- “0 second” idle execution.
- any specific deployment provider.

All may be evaluated. None is the current truth.

## 4. Critical attack: assume the whole idea is bad

### Attack A — A custom application may not be necessary

A private GitHub repository, structured Markdown/JSON records, ChatGPT Work, GitHub Issues and cloud coding agents may already solve most of the operational pain.

If so, a custom web application could become a months-long engineering project whose only purpose is to reproduce capabilities already available in the tools used to build it.

**Required validation:** run the workflow using a repo-based operating system first. Measure what friction remains. Only implement software where the repo/agent workflow genuinely fails.

### Attack B — “Opportunity” may be the wrong central object

One job posting is not necessarily one opportunity:

- the same program can appear on several pages;
- an employer can publish several location variants;
- one opportunity may later support multiple application versions;
- an application campaign may outlive a specific source posting;
- a program can close and reopen under a new posting ID.

A better domain may eventually distinguish:

- SourcePosting
- Opportunity
- ApplicationCase / Candidacy
- Employer / Program
- ArtifactPackage

**Response:** preserve “Opportunity” as the current conceptual center, but do not freeze DDD aggregate semantics before domain modeling and real examples.

### Attack C — Full workflow orchestration may be premature

A long-running durable orchestration system is valuable only if the actual workflow needs resumable multi-step processes often enough to justify it.

A much simpler early system might be:

- database records;
- stateless workers;
- a deterministic task table;
- scheduled/event checks.

**Response:** validate the required semantics first: persistence, idempotency, dependency resolution, human pauses, version migration. Choose the simplest mechanism that proves them.

### Attack D — Research automation may be the weakest part

Web research is unstable:

- source pages change;
- job portals block automation;
- snippets are stale;
- employer claims can be vague;
- secondary sources copy each other;
- indirect prompt injection is possible;
- heavy research is expensive.

**Response:** initially restrict deep research to high-value opportunities and prefer primary sources / structured public job data. Treat external text as untrusted evidence, never as instructions.

### Attack E — Brand Contracts may create fake precision

A structured “Brand Contract” can look rigorous while encoding subjective guesses.

**Response:** keep the contract small, operational and testable. Use design tokens/rules only if downstream document generation truly consumes them. Avoid aesthetic pseudo-metrics.

### Attack F — Voice automation can become a sophisticated impersonation failure

Even a truth-safe letter can sound unlike the user.

Historical application work demonstrated that corporate vocabulary, abstract “professional” wording and repeated motives produced a technically polished but inauthentic result.

**Response:** voice is evidence, not personality fiction. Approved/rejected examples, argument provenance, locked paragraphs and user review remain necessary.

### Attack G — ATS “compliance” is not a universal property

A PDF can be native-text and logically ordered yet behave differently across real employer portals.

**Response:** use an **ATS Safety Proxy**:
- real text extraction;
- predictable reading order;
- no hidden raster page;
- stable fonts/layout;
- selected real portal testing when feasible.

Never claim universal ATS compatibility.

### Attack H — Zero hallucinations is not a measurable universal guarantee

A test set with zero observed errors does not prove the true error rate is zero.

**Response:** separate hard invariants that deterministic software can guarantee from probabilistic quality goals measured over evaluation sets.

### Attack I — “Daily autonomy” could be a cost machine

If the system wakes daily and researches widely, it can consume model credits without improving application outcomes.

**Response:** daily is a trigger option, not an entitlement to spend. Perform cheap deterministic change checks first. Only invoke expensive reasoning when a material work item exists.

### Attack J — GitHub cannot be both development repository and personal-data vault

A private repository is an excellent source of truth for code, architecture, requirements and project decisions. It is a poor default location for full applicant PII, photos, credentials and live application artifacts.

**Response:** explicitly separate:
- **Development Truth in GitHub**
- **Runtime Personal Data in a dedicated protected store chosen later**

Never commit secrets, full personal dossiers, production CVs with contact details, or identity documents merely because the repo is private.

## 5. Corrected target architecture

Do not lock the implementation shape yet. Lock the responsibilities.

### Product core

**System of record**
- applicant/career claims and versions;
- external opportunity evidence and snapshots;
- application cases;
- user actions;
- artifact metadata;
- state/history.

**Deterministic policy layer**
- allowed state transitions;
- dependency checks;
- version checks;
- invalidation;
- idempotency;
- schema validation;
- artifact locks;
- permission boundaries.

**Semantic workers**
- opportunity research interpretation;
- requirement extraction;
- qualitative fit;
- evidence synthesis;
- positioning;
- application concept and writing;
- CV relevance;
- semantic package QA.

**Artifact services**
- application document generation;
- CV generation;
- text extraction / geometry / technical QA.

**User control**
- truth corrections;
- preference decisions;
- high-impact ambiguities;
- final review;
- submission.

### Important correction

The product is **state/dependency-driven**.

It is **not yet established** that the implementation must be fully event-driven, DDD, CQRS, event-sourced, or based on a dedicated durable-workflow framework.

## 6. Walking Skeleton: the first software proof

Before broad discovery, advanced scheduling, provider gateways, sophisticated UI or a durable workflow engine, prove one vertical slice.

### Input

One manually selected real or historical opportunity and a sanitized applicant-truth fixture.

### Slice

1. Create canonical opportunity record and source snapshot.
2. Extract requirements with provenance.
3. Represent one conditional eligibility case.
4. Create one user action that blocks submission only.
5. Build evidence-safe positioning.
6. Build a minimal operational document-identity contract.
7. Produce application concept and draft.
8. Produce a CV content selection.
9. Render native application + CV.
10. Run deterministic document QA.
11. Run package-level semantic checks.
12. Present a review-ready package with explicit remaining action.
13. Modify one upstream fact and prove targeted invalidation.
14. Retry one work item and prove no duplicate artifact is committed.

### Explicitly out of scope for Skeleton 1

- autonomous web-wide job discovery;
- daily scheduling;
- complex priority queues;
- multiple providers;
- production secrets;
- full user dashboard;
- durable runtime technology;
- commercial ATS integrations;
- automatic submission.

## 7. Validation program

### H0 — Do we need a custom app?

**Test:** run one real application case using only the GitHub project operating system and agents. Document remaining manual friction.

**Pass for app build:** several high-value pains remain that software can remove without creating greater complexity.

### H1 — Domain center

Test real examples against candidate domain objects:
- Opportunity-only;
- SourcePosting + Opportunity;
- Opportunity + ApplicationCase.

### H2 — Dependency-scoped blocking

Fixture: required test pending.

Expected:
- application preparation continues;
- CV preparation continues;
- submission blocked;
- explicit user action created.

### H3 — Evidence reliability

Evaluation dataset contains:
- official vacancy pages;
- university requirements;
- vague “preferred” wording;
- inaccessible source;
- conflicting sources;
- employer-wide vs program-specific claims;
- anecdotal secondary evidence.

### H4 — Voice integrity

Use known approved and rejected application fragments.

Test:
- truth preservation;
- employer specificity;
- character drift;
- duplicate arguments;
- why-me clarity.

### H5 — Document production

Verify:
- real selectable text;
- logical extraction order;
- A4/page count;
- no clipping;
- immutable portrait source handling;
- targeted layout changes do not alter locked areas.

### H6 — Invalidation

Change:
- minor benefit;
- program title;
- positioning fact;
- applicant skill status.

Expected dependent artifacts differ by case.

### H7 — Workflow reliability

Prove:
- retries are idempotent;
- partial failures resume safely;
- user action can pause only the dependent branch;
- a workflow/schema version change is handled deliberately.

### H8 — User experience

The user should be able to answer:
- What is happening?
- What is ready?
- What is uncertain?
- What do I need to do?
- What can the system continue doing without me?

without seeing internal engineering vocabulary.

## 8. GitHub-native browser-first development model

The user is not expected to run VS Code, Docker or terminal commands locally.

GitHub is the development workspace.

### Source of truth

Git repository:
- concept;
- validation evidence;
- requirements;
- decisions;
- architecture;
- code;
- tests;
- agent instructions;
- CI workflows.

### Work management

GitHub Issues:
- one bounded work item each;
- acceptance criteria;
- source references;
- explicit dependencies;
- phase/gate label.

GitHub Projects:
- optional lightweight portfolio view;
- phase;
- status;
- priority;
- decision-needed;
- agent/owner.

Pull Requests:
- only reviewable change boundary;
- issue link;
- tests/checks;
- decision/requirement impact;
- screenshots/artifacts where relevant.

### Browser-first verification

Every implementation PR should provide:
- GitHub Actions check status;
- relevant test output;
- preview/screenshot or artifact where useful;
- exact unresolved items;
- no claim of success if CI was not executed.

## 9. Agent architecture for development

### Shared rules: `AGENTS.md`

Keep cross-agent standing rules here:
- inspect before modify;
- respect source hierarchy;
- do not invent requirements;
- no personal production data in repo;
- small reversible increments;
- tests appropriate to change;
- update relevant docs in same PR;
- never claim checks passed unless executed.

Keep this file concise. Large conflicting instruction forests are themselves an agent reliability risk.

### Copilot-specific rules: `.github/copilot-instructions.md`

Only rules that materially help Copilot work in this repo.

### Path-specific rules

Use sparingly for:
- tests;
- docs/validation;
- renderer;
- migrations.

### Custom agents

Do not create ten personas on day one.

Initial candidates only if repeated work justifies them:
- implementation
- verification
- research-spike

A “reviewer agent” is not automatically independent merely because it has a different prompt.

### Issue sizing

Cloud-agent sessions are bounded; issues must be independently finishable and reviewable rather than “build Phase 4.”

## 10. Model-use policy

Interpretation of the user’s preferred operating model:

**Default:** GPT-5.6-class reasoning for routine planning, documentation, analysis and ordinary implementation/review.

**Escalate to GPT-6 Astra when the task has one or more of these characteristics:**
- cross-cutting architecture change;
- validation synthesis with conflicting evidence;
- difficult debugging after ordinary agent failure;
- phase-gate decision;
- security/privacy boundary;
- model/eval design;
- complex multi-file integration;
- adversarial review/red-team;
- migration of persistent workflow semantics;
- final release audit.

**GitHub Copilot cloud agent:** bounded issue implementation, tests, repo maintenance, straightforward refactors, documentation updates and selected spikes.

**Astra/Codex:** project-level coordinator / high-complexity implementer/reviewer, especially when multiple concerns must remain coherent.

Model capability is not a security boundary. Critical invariants remain enforced in code/tests/permissions.

## 11. Security correction

The system ingests hostile external text: job postings, websites, PDFs and employer content.

Treat all external content as **data, never instructions**.

Required controls:
- source tagging;
- prompt-injection fixture tests;
- least-privilege tools;
- model cannot commit authoritative truth directly;
- outputs validated before state mutation;
- personal-data exposure minimized;
- secrets never supplied through prompts;
- external content never allowed to modify system policies.

## 12. Evaluation policy: remove fake “100%” language

### Hard invariants

These may use absolute gates:
- no automatic submission;
- no direct model write to authoritative Applicant Truth;
- unique work-item/idempotency constraints;
- schema validation on persisted structured records;
- no successful build status without actual build;
- no “native PDF pass” when extraction is empty;
- no secret committed to repository.

### Statistical / semantic objectives

These require evaluation metrics rather than universal guarantees:
- eligibility extraction accuracy;
- claim-scope classification;
- employer specificity;
- voice similarity/authenticity;
- semantic package consistency;
- research usefulness.

## 13. Project-management skeleton that can later inform the larger planning-tool idea

The Application Operations System should be the first serious project run through the user’s broader product-planning logic.

Recommended project lifecycle:

1. **Idea Creation / Existing Concept Origin**
2. **Idea Exploration**
3. **Conceptation**
4. **Validation**
5. **Validated Product Baseline**
6. **Idea to Production**
   - requirements;
   - domain/workflow design;
   - UX;
   - architecture decisions;
   - engineering plan.
7. **Production**
   - walking skeleton;
   - vertical slices;
   - integration;
   - alpha/beta.
8. **After Production**
   - operations;
   - learning;
   - revisions.

The exact stage taxonomy for the future planning tool remains a separate design problem.

Each experiment should preserve:

`Question → Hypothesis → Method → Evidence → Result → Decision / No Decision → Affected artifacts → Retest condition`

## 14. Minimal repository skeleton

```text
/
├── README.md
├── AGENTS.md
├── PROJECT_STATE.md
│
├── .github/
│   ├── copilot-instructions.md
│   ├── ISSUE_TEMPLATE/
│   └── instructions/             # only as needed
│
├── docs/
│   ├── concept/
│   │   ├── concept-baseline.md
│   │   └── history-and-lessons.md
│   ├── validation/
│   │   ├── hypothesis-register.md
│   │   ├── evidence-register.md
│   │   └── experiments/
│   ├── decisions/
│   │   ├── decision-log.md
│   │   └── adr/                  # created when architecture begins
│   ├── quality/
│   │   └── historical-failure-fixtures.md
│   └── risks/
│       └── risk-register.md
│
└── src/                          # created only when a validated slice starts
```

Do not create empty SRS, architecture, operations and deployment directories merely to look professional. Create them when their phase begins.

## 15. Final recommendation

Proceed.

But the first GPT-6 Astra task is **not “build the Application Operations System.”**

It is:

1. create/inspect the GitHub repository;
2. install the minimal source-of-truth skeleton;
3. import this concept/history;
4. create the validation backlog;
5. design and execute H0 and the first high-risk experiments;
6. stop at the first real decision gate;
7. only then define the first walking-skeleton implementation issue set.

This keeps the project capable of becoming real software without allowing process documents or infrastructure to become the project itself.
