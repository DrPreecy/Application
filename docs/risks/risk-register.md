# Risk Register

| ID | Risk | Likelihood | Impact | Current mitigation |
|---|---|---|---|---|
| R-001 | Scope expands into a platform before core value is proven. | High | High | Validation first; H0; walking skeleton before broad implementation. |
| R-002 | Research produces weak, stale or incorrectly scoped evidence. | High | High | Provenance, source hierarchy, permitted-use rules, evidence fixtures. |
| R-003 | LLM output invents or upgrades applicant facts. | Medium | Critical | Applicant Truth authority; candidate-output validation; no direct model-to-truth writes. |
| R-004 | Architecture is prematurely locked to fashionable infrastructure. | Medium | High | Non-decisions list; ADRs and spikes for high-cost choices. |
| R-005 | Voice becomes polished but inauthentic. | High | High | Historical voice fixtures, authenticity checks, approved-content locks, user review. |
| R-006 | CV/application generation regresses into raster/geometry/photo failures. | Medium | High | Native artifact tests, extraction checks, minimum-change and asset locks. |
| R-007 | Long-running workflow duplicates or loses work under retry/version change. | Medium | High | H7 validation; idempotency/versioning before autonomous live use. |
| R-008 | Internal state model becomes too complex for normal user interaction. | Medium | High | H8 UX validation and plain-language state translation. |
| R-009 | Personal data leaks through repository, logs, tools or model providers. | Medium | Critical | GitHub/PII boundary, data classification before live data, least privilege. |
| R-010 | External job/web content causes indirect prompt injection. | Medium | High | Treat external content as untrusted data; policy/tool boundary tests. |
| R-011 | Daily automation consumes model budget without meaningful progress. | Medium | Medium | Idle is valid; cheap checks before expensive model work; meaningful-progress metrics. |
| R-012 | Process/documentation becomes the product and delays usable software. | Medium | High | Minimal artifacts; phase exit criteria; vertical walking skeleton. |

## Initial validation evidence — 2026-09-09

E-005 supports narrow dependency feasibility but does not retire R-001, R-007 or other production risks. R-001/R-012: stop at user-value criterion G-001 before creating speculative infrastructure. R-003/R-009/R-010: no live applicant data used; authority and injection integration checks remain unexecuted. R-006: native document reliability remains UNKNOWN. See the initial experiment report for limitations.

## E-006 follow-up

R-002: a real authoritative-source contradiction was found and reconciled by field scope; authority alone is insufficient. R-006: one new native package and local-edit test succeeded, but reference extraction disagreement demonstrates why export QA is separate. R-005/R-008: new-draft user review G-003 is pending. R-007: temporary-file tests do not mitigate simultaneous-writer/power-loss risk. R-009: all personal inputs/outputs remain outside GitHub; only sanitized records are committed. R-012: user corrected an inspection-only interpretation, and actual new deliverables were then produced.
