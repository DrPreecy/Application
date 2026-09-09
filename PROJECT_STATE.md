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

## Current validation state

G-001 was answered under D-005: process quality, structured evaluation, traceability, visible steps and targeted intervention are part of value. Equal document quality is not assumed.

The user authorized private historical inputs and clarified that they were to serve as data for an independently agent-authored application/CV package.

EXP-004–007 produced useful supporting technical/research evidence. EXP-008 produced new native application/CV artifacts and a narrow scoped-edit check.

### G-003 user review

**G-003 FAILED.**

The user rejected the generated package on substantive quality grounds:

- the application letter was judged too derivative of the accepted historical final application rather than independently derived from the intended process;
- the CV was judged visually and editorially inadequate, with weak information hierarchy/design and poor photo integration;
- technical PDF validity did not compensate for the missing design/process quality.

This failure is preserved as validation evidence, not treated as a request to cosmetically repair the two PDFs.

New failure classes F-026–F-030 cover gold-reference leakage, process bypass, design collapse, reference-as-template misuse and output-only optimization.

See `docs/validation/experiments/g003-failure-and-retest.md` for the corrected retest protocol.

### Evidence still retained from EXP-008

- Native editable document/PDF generation is technically feasible in this environment.
- One local heading edit was isolated without unrelated pixel/media changes.
- Reference inputs remained unchanged.
- These facts are narrow technical evidence only and do not establish successful application/CV quality.

### Hypothesis state

- All H0–H8 remain TESTING; none PASS.
- H4 now has negative user evidence for the EXP-008 package.
- H5 has narrow technical evidence but negative design-quality evidence for the candidate CV.
- H6 retains narrow scoped-edit evidence.
- No production runtime, independent reviewer or sustained quality claim exists.

## Current gate

Walking Skeleton remains **HOLD**.

The next private reference-case run must use the retest protocol: separate neutral data/process/voice evidence from hidden gold artifacts, preserve the mandatory intermediate chain, perform real design exploration before rendering, and reintroduce final historical artifacts only after the candidate package is frozen for comparison.

While private Work/Astra quota is unavailable, safe repository work may continue; do not launch a compromised substitute generation run or choose a final stack.
