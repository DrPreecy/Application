# Application Operations System

Browser-first personal software project for managing the application lifecycle from opportunity research to review-ready application packages.

## Current phase

**Validation / project bootstrap.**

This repository intentionally does **not** start with application code. The current goal is to preserve the concept, real failure history, validation hypotheses, decisions, risks, and regression fixtures before choosing a final architecture or stack.

## Core product direction

- One coherent application lifecycle instead of three independent timer-driven automations.
- Persistent state and dependency-scoped blocking.
- Applicant facts are authoritative and must never be invented or silently upgraded.
- Fit and eligibility are separate.
- Research claims require provenance and correct scope.
- Application and CV share positioning and document-identity inputs.
- Approved work changes only when a relevant dependency changes.
- The user owns personal truth, review, and final submission.
- Models perform bounded semantic work; deterministic software owns authoritative state, validation, workflow rules, and artifact integrity.

## Important non-decisions

The following are intentionally **not yet chosen**: final database, workflow/orchestration technology, frontend framework, programming language, renderer, model-provider set, deployment platform, event-sourcing/CQRS, or formal DDD aggregate boundaries.

## Repository usage

GitHub is the development source of truth for code, sanitized fixtures, requirements, decisions, tests, and project documentation. It is **not** the production vault for personal application data, credentials, identity documents, or other sensitive PII.

See `PROJECT_STATE.md` for current status and `docs/validation/hypothesis-register.md` for the first validation work.