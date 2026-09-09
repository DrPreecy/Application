# Evidence Register

This register records evidence used to validate product or architecture claims.

## Rules

- Prefer primary/authoritative sources where possible.
- Separate external source evidence from empirical project evidence.
- Another LLM's agreement is not validation by itself.
- Technical spikes count as evidence only for the exact question they test.
- Every important design claim should eventually link to evidence or remain explicitly `PROPOSAL` / `UNKNOWN`.

## Initial evidence classes

### E-001 — Historical application-writing process
**Type:** Empirical project evidence

Observed across multiple application iterations:
- corporate/buzzword-heavy professionalization caused character drift;
- authentic wording improved when real user language and reasoning were used as source material;
- employer specificity improved when employer facts changed the personal argument rather than acting as praise;
- approved segments needed locking to prevent later regressions.

### E-002 — Historical CV-production process
**Type:** Empirical project evidence

Observed across repeated CV iterations:
- content/design changes performed together created instability;
- whole-page raster/image workflows caused technical and layout problems;
- native text rebuild, stable grid, photo asset handling and minimum-change behavior produced the strongest final result;
- one successful manual/native rebuild proves feasibility, not an automated production pipeline.

### E-003 — Three-Daily race condition
**Type:** Empirical system evidence

Observed behavior:
- downstream Application Writer could execute while Opportunity Intelligence remained incomplete;
- clock time therefore did not represent dependency readiness.

Supports testing a persistent dependency/state model.

### E-004 — Eligibility over-blocking
**Type:** Empirical system/design evidence

Required tests and unknown user facts showed that global readiness caused unnecessary blocking. This supports the dependency-scoped-blocking hypothesis but does not yet prove the final state-machine design.

## To add during validation

Each experiment should link evidence here or in its own experiment record and include source/date/method/scope.
