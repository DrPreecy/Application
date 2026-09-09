# GitHub Browser-First Bootstrap Plan
## Application Operations System

## 1. Core principle

GitHub is the **development workspace**, not automatically the production personal-data store.

The user should be able to:
- review issues;
- review/approve PRs;
- inspect CI;
- upload screenshots/references;
- steer agents;
- read product decisions;
from GitHub.com and ChatGPT Work.

## 2. Minimal initial files

```text
README.md
AGENTS.md
PROJECT_STATE.md
.github/copilot-instructions.md

docs/concept/concept-baseline.md
docs/concept/history-and-lessons.md
docs/validation/hypothesis-register.md
docs/validation/evidence-register.md
docs/validation/experiments/
docs/decisions/decision-log.md
docs/quality/historical-failure-fixtures.md
docs/risks/risk-register.md
```

Do not pre-create empty SRS, deployment docs, dozens of ADRs or agent profiles.

## 3. Work hierarchy

Use a parent GitHub Issue for each project phase only when needed.

Sub-issues should be executable units:
- one validation experiment;
- one architecture spike;
- one vertical-slice change;
- one regression group.

An issue assigned to an agent must have stable acceptance criteria before assignment.

## 4. PR policy

Agent-authored implementation changes should normally land through PRs.

Each PR:
- links issue;
- explains scope;
- states source requirement/decision;
- records tests/checks actually run;
- includes screenshots/artifacts when visual;
- names unresolved risks;
- avoids unrelated cleanup.

## 5. Browser-verifiable quality

Use GitHub Actions once code exists.

At minimum:
- formatting/lint where relevant;
- unit tests;
- integration tests;
- artifact/document QA tests;
- fixture/eval jobs as they become stable.

The user should never need to run a command locally merely to know whether a PR passes.

## 6. Agent instructions

### `AGENTS.md`
Cross-agent rules only.

### `.github/copilot-instructions.md`
Copilot-specific repo context.

### `.github/instructions/*.instructions.md`
Only when a path has genuinely different working rules.

### `.github/agents/*.agent.md`
Create custom agents only after recurring task patterns exist.

## 7. Copilot cloud-agent constraints

Design issues around cloud-agent reality:
- tasks are asynchronous and PR-oriented;
- one task/branch/PR at a time;
- sessions are time-bounded;
- large phases must be decomposed;
- acceptance criteria should be in the issue at assignment time;
- steer follow-up work from the PR.

## 8. Proposed agent routing

Routine:
- GitHub Copilot for bounded implementation/tests/docs.
- GPT-5.6-class work for ordinary product/research/review.

Escalate:
- GPT-6 Astra for cross-cutting, adversarial or high-risk work.

Do not turn routing into a rigid ritual. If routine work repeatedly fails, escalate.

## 9. Development vs runtime state

Repository state:
- requirements;
- decisions;
- schemas;
- sanitized fixtures;
- code/tests.

Runtime state:
- applicant truth;
- PII;
- live opportunity records;
- documents;
- secrets.

Runtime storage is decided later after deployment/privacy validation.

## 10. First milestone objective

Not “build the app.”

Objective:
- repository is understandable to a new agent;
- H0–H8 are registered;
- historical failures exist as fixtures;
- first validation experiments executed;
- walking-skeleton criteria agreed;
- first software slice is justified by evidence.
