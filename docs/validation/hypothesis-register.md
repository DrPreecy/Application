# Hypothesis Register

Status values: `UNKNOWN`, `TESTING`, `PASS`, `FAIL`, `DEFERRED_WITH_MITIGATION`.

| ID | Hypothesis | Why it matters | Current status | First validation direction |
|---|---|---|---|---|
| H0 | A custom Application Operations System creates enough value beyond GitHub + agents to justify custom software. | Prevents building infrastructure that reproduces existing tools. | TESTING | Compare a full workflow against repeatable process quality, structured evaluation, traceability, visible intermediate states and targeted intervention (D-005); do not assume equal output quality. |
| H1 | The current domain can be modeled cleanly around Opportunity without awkward identity/version exceptions. | Wrong domain center would infect persistence, workflow and UI. | TESTING | Compare Opportunity-only vs SourcePosting+Opportunity vs Opportunity+ApplicationCase with repost/reopen/version scenarios. |
| H2 | Dependency-scoped blocking can let useful work continue while only true prerequisites pause. | Core correction to previous over-blocking. | TESTING | Test required test, unknown citizenship/user fact, and preferred-vs-mandatory requirement fixtures. |
| H3 | Research can produce sufficiently reliable evidence/provenance for decision and application use. | Weak evidence would contaminate eligibility and documents. | TESTING | Test official, conflicting, inaccessible, secondary and anecdotal source cases. |
| H4 | Automated writing can preserve authentic user voice while remaining employer-specific and professional. | A factually correct but alien application still fails. | TESTING | Evaluate approved/rejected historical application fragments and adversarial rewrites. |
| H5 | CV/application documents can be generated reliably as native, inspectable artifacts. | Raster/geometry/photo failures were real historical failures. | TESTING | Native-text extraction, reading order, clipping, photo immutability and minimum-change tests. |
| H6 | Material-change invalidation can be scoped to true dependencies. | Prevents expensive unnecessary rebuilds and stale artifacts. | TESTING | Change benefit, program title, positioning fact and applicant-skill fact separately. |
| H7 | Workflow execution can be made idempotent, resumable and safe under concurrent/versioned changes. | Required before autonomous long-running operation. | TESTING | Retry, partial failure, concurrent edit and persisted-state migration experiments. |
| H8 | Complex internal state can be translated into a simple user-facing experience. | Internal rigor is useless if the user cannot understand state/action. | TESTING | Prototype ready/uncertain/action/continue states without engineering jargon. |

## Required experiment record

Every experiment must record:

`Question → Hypothesis → Method → Evidence → Result → Decision / No Decision → Affected artifacts → Retest condition`

No hypothesis is considered proven because another LLM agrees with it.

## Initial validation update — 2026-09-09

See [experiment report](experiments/initial-validation.md) and [procedures](../quality/validation-procedures.md).

- H0/H8 TESTING: partial synthetic repo/agent rehearsal recorded; G-001 subsequently answered in D-005. No high-fidelity trial or usability pass.
- H1 TESTING: identity counterexamples compared manually; no schema/aggregate choice.
- H2/H6 TESTING: 11 synthetic graph checks passed; eight historical-mutant rejections. Correct graph edges were supplied manually; no production proof.
- H3/H4/H5/H7 remain UNKNOWN: no extraction evaluation, authentic-voice trial, native-document trial or durable runtime test executed.
- Hypothesis wording is unchanged: evidence does not justify replacing the questions. PASS is withheld for all hypotheses.

## User correction after G-001

H0 measures operational capability and sustained quality, not merely coordination time at assumed equal document quality. H8 includes visible intermediate steps and meaningful intervention across connected subprocesses, not just a simplified final status message. Both remain TESTING. The exact existing rating rules are unavailable in the repository; no replacement scoring model is authorized by this clarification.

## Reference-data production trial — 2026-09-09

[EXP-004–008](experiments/reference-case-validation.md) uses authorized private inputs. The user clarified that the agent must generate its own package; EXP-008 does so. All hypotheses are now TESTING, none PASS. H3 has manual live-source reconciliation; H4 has a newly authored letter pending user voice review; H5 has new native exports and real extraction checks; H7 has a limited temporary-file retry experiment, not concurrent production safety. H6 includes a real local document edit with zero pixel changes outside its heading band. G-003 awaits user review of the new drafts; G-002 is superseded.
