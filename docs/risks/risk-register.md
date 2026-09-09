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
