# Decision Log

This file records accepted material project decisions. Proposals do not become decisions merely because an agent recommends them.

## Accepted decisions

### D-001 — Validation before broad implementation
**Status:** Accepted

The project will validate high-risk assumptions and prove a walking skeleton before building a broad autonomous platform.

### D-002 — Browser-first development workflow
**Status:** Accepted

The user should be able to operate the project primarily through GitHub.com and ChatGPT Work. Local VS Code/terminal work is not assumed.

### D-003 — GitHub is development source of truth, not default PII vault
**Status:** Accepted

Code, project docs, decisions, sanitized fixtures and tests live in GitHub. Runtime storage for personal application data is a later architecture/privacy decision.

### D-004 — Old three-Daily timer architecture is historical, not target architecture
**Status:** Accepted

The useful domain/process logic from the Dailies is preserved, but clocks are not used as the primary dependency model.

## Explicitly unresolved

- final domain aggregate boundaries
- final persistence technology
- final workflow/orchestration technology
- final programming language/framework
- final renderer
- final deployment environment
- final runtime PII storage
- final model-provider routing implementation

When one of these is decided, add a traceable decision/ADR with evidence rather than editing history retroactively.

## Validation checkpoint — 2026-09-09 (no new accepted decision)

EXP-001–003 and E-005 retain D-001 through D-004. All architecture non-decisions remain open. G-001 awaits the user-owned value criterion for H0. The walking-skeleton gate is HOLD; synthetic feasibility is insufficient for a go decision. Proposed experiment criteria are not promoted to accepted requirements.

## D-005 — Process quality and visibility are part of product value
**Status:** Accepted user direction, 2026-09-09 (response to G-001)

The user rejects holding document quality constant when assessing H0. The system must be evaluated on repeatable quality throughout connected subprocesses, structured data processing/sorting/evaluation, traceable relationships between variables, visible intermediate steps and targeted intervention. Application/CV outputs alone do not represent the product's value. GitHub remains the development workspace under D-002/D-003; its suitability as the user's operational interface is a separate question.

The user reports existing prompt-based failures and believes GitHub + agents alone cannot meet the desired consistency and visibility. Record that as user experience and a product hypothesis, not an experimentally proven impossibility. No particular UI, rating formula, stack or architecture is chosen. No commercial/multi-user scope is inferred from the business analogy.

G-001 is answered; no need to ask the user to justify the same preference again. This decision supersedes the pending-G-001 checkpoint above. Walking-skeleton approval still requires appropriate evidence.

## Validation scope clarification — 2026-09-09

Current user instruction authorizes the supplied historical case as private data for generating the agent's own application/CV. Auditing the supplied final documents alone is insufficient. EXP-008 follows this clarification. No reference file is overwritten and no personal inputs/outputs are committed. G-003 is review of the new drafts; the proposed G-002 sentence-only gate is superseded. No architecture decision or walking-skeleton approval is added.
