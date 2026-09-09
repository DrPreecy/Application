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
