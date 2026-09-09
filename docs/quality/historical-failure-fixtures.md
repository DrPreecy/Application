# Historical Failure Fixtures

These are permanent regression classes derived from real project failures and explicit design concerns. Expected behavior may become more precise during validation, but the failure class should not disappear silently.

| ID | Failure scenario | Required behavior |
|---|---|---|
| F-001 | Application work starts before intelligence/research for the same dependency is stable. | Dependent work waits; unrelated/backlog work may continue if independently valid. |
| F-002 | No new jobs exist, but useful backlog exists. | Advance meaningful backlog; do not manufacture discovery noise. |
| F-003 | Strong opportunity requires a test before submission. | Application/CV prep may continue; Submission blocked; explicit User Action created. |
| F-004 | Citizenship or another applicant fact is unknown. | Mark the affected dependency unresolved; do not invent the fact or globally freeze unrelated work. |
| F-005 | One eligibility uncertainty freezes the whole opportunity. | Prohibited unless every downstream task truly depends on it. |
| F-006 | Preferred wording is interpreted as mandatory. | Preserve requirement strength and provenance; no silent MUST upgrade. |
| F-007 | A failed/inaccessible webpage is interpreted as CLOSED. | Availability remains UNKNOWN unless closure is independently evidenced. |
| F-008 | Employer-wide fact is presented as program-specific. | Scope validation rejects or downgrades the claim. |
| F-009 | Anecdotal evidence is treated as confirmed/application-safe. | Evidence-strength and permitted-use rules prevent the upgrade. |
| F-010 | Application and CV use different positioning versions. | Package QA fails and affected artifact(s) require revalidation. |
| F-011 | Application and CV use incompatible brand/document-identity versions. | Package QA fails. |
| F-012 | Applicant Truth changes after documents were produced. | Only dependent artifacts become stale/revalidation-required. |
| F-013 | Job posting changes during document production. | Impact analysis determines which work is invalidated. |
| F-014 | CV is rasterized or extraction/reading order is technically invalid. | Document QA fails; no final/review-ready status. |
| F-015 | Portrait is altered/generated/covered instead of properly placed or replaced. | Photo policy rejects the artifact; only approved transforms/assets allowed. |
| F-016 | Model invents expertise, skill level, dates, motives or experience. | Truth/evidence validation rejects the candidate output. |
| F-017 | Same model/persona is called an independent reviewer. | Do not label as independent; combine deterministic checks and genuinely separate review where required. |
| F-018 | AI rewrite destroys an approved paragraph while changing something else. | Content lock/minimum-change rules preserve unaffected approved material. |
| F-019 | Retry produces duplicate committed artifacts/work items. | Idempotency/uniqueness prevents duplicate commit. |
| F-020 | Persisted workflow resumes under incompatible logic/schema version. | Explicit migration/version handling; no silent replay corruption. |
| F-021 | System has no useful work and manufactures filler activity. | Idle is valid; no unnecessary LLM/task generation. |
| F-022 | External job posting/web content contains prompt-injection instructions. | External content is treated as data only; instructions cannot alter system policy/tool authority. |

## Rule

Before Personal Live, these fixtures must be represented by executable tests or clearly documented manual/evaluation procedures appropriate to the failure class.
