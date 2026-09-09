# Application Operations System — Concept Baseline

## Status

Current product concept and validation baseline. This is **not** a final software architecture, final SRS, or approved technology stack.

## Product thesis

The product is one persistent Application Operations System that manages the application lifecycle from opportunity discovery/research to review-ready documents and submission readiness.

The system replaces the old mental model of three independent scheduled Dailies. Scheduling may later trigger work, but clocks do not define dependencies.

## Primary goal

Reduce manual coordination while producing high-quality, truthful, evidence-backed, opportunity-specific application packages that remain under user control.

The user should primarily decide, review and submit — not repeatedly transfer state between chats, rediscover research, or repair generated documents.

## Core responsibilities

### Shared system state

The system needs durable representations for at least:
- Applicant Truth / Career Truth
- opportunity/source evidence
- eligibility and open prerequisites
- fit and program assessment
- positioning
- document identity / brand constraints
- application artifacts
- CV artifacts
- user actions
- workflow/history

The final persistence model is not decided.

### Deterministic responsibilities

Software should own authoritative:
- IDs and versions
- allowed transitions
- dependency checks
- invalidation
- idempotency
- schema validation
- artifact locks
- audit/state history

### Semantic/LLM responsibilities

Models may perform bounded work such as:
- research interpretation
- requirement extraction
- qualitative fit analysis
- evidence synthesis
- positioning
- application concept and writing
- CV relevance judgment
- semantic package review

Model output is a candidate result, not automatically authoritative state.

## Core behavioral principles

### Applicant truth

No experience, date, qualification, skill level, motivation or personal fact may be invented or silently upgraded.

### Fit ≠ Eligibility

A very strong opportunity may still have conditional eligibility.

### Dependency-scoped blocking

Unknowns block only dependent work.

Example:
- Required Test = open
- Application prep = may continue
- CV prep = may continue
- Submission = blocked/pending
- User Action = complete test

### Evidence provenance

Claims must preserve source, scope, strength, freshness and allowed use. Employer-wide evidence must not silently become program-specific. Anecdote must not become confirmed fact.

### Positioning consistency

Application and CV should derive from the same stable positioning basis rather than independently inventing different career narratives.

### Document identity

Application and CV should feel like one coherent application family without being identical documents. The exact persisted contract/schema remains to be validated.

### Controlled change

Approved/locked work should not be broadly regenerated for local changes. Material upstream changes should invalidate only dependent artifacts.

### User action

The system should explicitly surface what the user must do, why, and what the action blocks.

### Submission

No automatic submission or employer contact. Final submission remains user-owned.

### Idle behavior

No useful work is a valid state. The system should not manufacture tasks, research or notifications simply because a scheduled trigger fired.

## Application-writing process baseline

- Source/Truth lock
- raw argumentation before prose
- employer counterfactual/specificity check
- voice-first draft
- professionalization pass
- authenticity/character-drift check
- truth/evidence audit
- why-me check
- content lock
- document production only after content stability

Professionalization improves form, not identity.

## CV process baseline

- verified career truth
- opportunity-specific relevance selection
- content hierarchy before layout
- approved document identity / layout rules
- native document rendering
- photo treated as immutable approved asset unless user requests otherwise
- technical QA and visual QA
- minimum-change behavior after locks

## Package QA

The system eventually needs package-level checks for:
- Applicant Truth consistency
- opportunity identity
- positioning consistency
- document-identity consistency
- application/CV semantic consistency
- artifact integrity
- outstanding user actions
- submission prerequisites

## Current non-goals

- automatic application submission
- automatic employer contact
- mass Easy Apply
- commercial multi-user SaaS
- generative applicant portraits
- automatic LinkedIn outreach
- hidden ATS pseudo-scores
- silently changing Applicant Truth

## Explicit non-decisions

Not yet chosen:
- formal DDD aggregate boundaries
- event sourcing/CQRS
- workflow engine
- database
- language/framework
- renderer
- deployment platform
- model-provider architecture
- runtime PII storage

## Validation direction

Before broad implementation, test H0–H8 in `docs/validation/hypothesis-register.md` and prove one walking skeleton that can carry a single application case through truth/evidence, conditional eligibility, positioning, application, CV, package QA, user action, targeted invalidation, and idempotent retry.
