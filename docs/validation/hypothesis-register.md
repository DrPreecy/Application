# Hypothesis Register

Status values: `UNKNOWN`, `TESTING`, `PASS`, `FAIL`, `DEFERRED_WITH_MITIGATION`.

| ID | Hypothesis | Why it matters | Current status | First validation direction |
|---|---|---|---|---|
| H0 | A custom Application Operations System creates enough value beyond GitHub + agents to justify custom software. | Prevents building infrastructure that reproduces existing tools. | TESTING | Run one high-fidelity application workflow using the repo/agents operating model and record unresolved friction. |
| H1 | The current domain can be modeled cleanly around Opportunity without awkward identity/version exceptions. | Wrong domain center would infect persistence, workflow and UI. | TESTING | Compare Opportunity-only vs SourcePosting+Opportunity vs Opportunity+ApplicationCase with repost/reopen/version scenarios. |
| H2 | Dependency-scoped blocking can let useful work continue while only true prerequisites pause. | Core correction to previous over-blocking. | TESTING | Test required test, unknown citizenship/user fact, and preferred-vs-mandatory requirement fixtures. |
| H3 | Research can produce sufficiently reliable evidence/provenance for decision and application use. | Weak evidence would contaminate eligibility and documents. | UNKNOWN | Test official, conflicting, inaccessible, secondary and anecdotal source cases. |
| H4 | Automated writing can preserve authentic user voice while remaining employer-specific and professional. | A factually correct but alien application still fails. | UNKNOWN | Evaluate approved/rejected historical application fragments and adversarial rewrites. |
| H5 | CV/application documents can be generated reliably as native, inspectable artifacts. | Raster/geometry/photo failures were real historical failures. | UNKNOWN | Native-text extraction, reading order, clipping, photo immutability and minimum-change tests. |
| H6 | Material-change invalidation can be scoped to true dependencies. | Prevents expensive unnecessary rebuilds and stale artifacts. | TESTING | Change benefit, program title, positioning fact and applicant-skill fact separately. |
| H7 | Workflow execution can be made idempotent, resumable and safe under concurrent/versioned changes. | Required before autonomous long-running operation. | UNKNOWN | Retry, partial failure, concurrent edit and persisted-state migration experiments. |
| H8 | Complex internal state can be translated into a simple user-facing experience. | Internal rigor is useless if the user cannot understand state/action. | TESTING | Prototype ready/uncertain/action/continue states without engineering jargon. |

## Required experiment record

Every experiment must record:

`Question → Hypothesis → Method → Evidence → Result → Decision / No Decision → Affected artifacts → Retest condition`

No hypothesis is considered proven because another LLM agrees with it.

## Initial validation update — 2026-09-09

See [experiment report](experiments/initial-validation.md) and [procedures](../quality/validation-procedures.md).

- H0/H8 TESTING: partial synthetic repo/agent rehearsal recorded; user-value criterion G-001 pending. No high-fidelity trial or usability pass.
- H1 TESTING: identity counterexamples compared manually; no schema/aggregate choice.
- H2/H6 TESTING: 11 synthetic graph checks passed; eight historical-mutant rejections. Correct graph edges were supplied manually; no production proof.
- H3/H4/H5/H7 remain UNKNOWN: no extraction evaluation, authentic-voice trial, native-document trial or durable runtime test executed.
- Hypothesis wording is unchanged: evidence does not justify replacing the questions. PASS is withheld for all hypotheses.
