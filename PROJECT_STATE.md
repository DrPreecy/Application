# Project State

## Current phase

**Validation / Bootstrap**

## Current objective

Establish a minimal, browser-first GitHub project system and validate the highest-risk assumptions before large implementation work.

## Current source-of-truth hierarchy

1. Explicit current user instruction
2. Accepted concept / consolidated project baseline
3. Accepted decision records
4. Validated product baseline
5. Approved requirements
6. Accepted architecture decisions
7. Repository code/tests
8. Historical reports and old Daily prompts as evidence/history
9. New agent proposals

## Current established product behaviors

- One coherent application lifecycle; not three mutually ignorant timer-driven Dailies.
- Applicant truth must not be invented or silently upgraded.
- Fit and Eligibility are separate.
- Missing information blocks only dependent work.
- Research claims require provenance and correct scope.
- Application and CV share positioning/document-identity inputs.
- Approved work should not be broadly regenerated for local changes.
- Material upstream changes invalidate only dependent outputs.
- User actions must be explicit.
- Submission remains user-owned.
- Final documents must be technically valid native artifacts rather than whole-page raster images.

## Important non-decisions

Not yet selected:
- final database
- workflow/orchestration framework
- final domain aggregate boundaries
- event sourcing / CQRS
- final programming language
- frontend framework
- PDF renderer
- deployment platform
- final model-provider set
- runtime PII storage

## Next gate

Initial validation executed; see `docs/validation/experiments/initial-validation.md`.

- H2/H6: 11 synthetic graph checks passed; 8 historical-mutant rejections. Production behavior remains unvalidated.
- H1: manual identity counterexamples recorded; architecture remains open.
- H0/H8: partial synthetic repo/agent rehearsal only; no full application or user evaluation.
- All F-001–F-022 now have explicit procedures and honest execution status in `docs/quality/validation-procedures.md`.
- H3/H4/H5/H7 remain UNKNOWN. No hypothesis is PASS.

**Current user decision gate G-001:** establish what residual coordination burden makes GitHub + agents insufficient, even at equal document quality. This personal value criterion cannot be inferred by an agent. After the answer, run one authorized high-fidelity case with personal artifacts outside GitHub; measure the relevant burden and quality failures.

Walking-skeleton gate remains HOLD pending evidence. No broad implementation, stack or runtime PII decision has been made.
