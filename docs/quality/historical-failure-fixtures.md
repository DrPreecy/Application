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

## Validation coverage

See [explicit procedures and execution status](validation-procedures.md). Synthetic model evidence is marked separately from unexecuted product checks; no historical failure class is removed.

## Failure classes discovered during validation

| ID | Failure scenario | Required behavior |
|---|---|---|
| F-023 | Native CV text extracts in conflicting reading orders across readers. | Record extractor/ordering evidence; native text alone cannot certify semantic readability. |
| F-024 | An authoritative program page contradicts its own heading or the precise job posting. | Preserve conflict and source scope; do not overwrite a well-supported field from an incidental conflicting paragraph. |
| F-025 | An inherited document style adds an unintended title border. | Inspect actual native export and remove style residue before delivery. |
| F-026 | Gold-reference leakage: an accepted final application is supplied as reference and the agent reproduces its structure/arguments instead of independently executing the intended process. | Separate process/voice evidence from hidden gold output; do not expose the final accepted artifact until after independent generation when the purpose is reconstruction validation. |
| F-027 | Process bypass: a final artifact is generated without preserving the intermediate Source Lock, Evidence Map, Positioning, Application Concept, CV relevance decisions, design reasoning and QA state needed to explain how it was produced. | Required intermediate artifacts must exist and be reviewable before the final package can support a process-validation claim. |
| F-028 | Design collapse: a technically native PDF is produced but the information-design system, hierarchy, grid, spacing and photo integration are materially weaker than established design requirements. | Technical PDF checks and design-quality checks are separate gates; native/selectable text alone cannot qualify a CV as successful. |
| F-029 | Reference-as-template misuse: a voice/process reference is used as wording/layout source rather than as calibration evidence. | References must carry permitted-use metadata; voice references calibrate style/reasoning and may not silently become paragraph/layout templates. |
| F-030 | Output-only optimization: the agent focuses on producing something that looks complete instead of validating whether upstream research, positioning, voice, design and dependency logic actually worked. | Validation success requires evidence from the required subprocesses, not only existence of final PDFs. |
| F-031 | Profile compression loss: a richer applicant/motivation profile is reduced to a short generic summary, causing distinctive high-value signals to disappear before writing. | Maintain a coverage map from high-value profile evidence to positioning/content decisions; omission of a material signal requires an explicit reason rather than silent loss. |
| F-032 | Template equivalence: after customization, most of the application could still be reused for another employer by replacing the company/program name and one or two details. | Run an employer-swap/template-baseline test; the application must contain load-bearing employer/opportunity reasoning that materially changes the narrative. |
| F-033 | Design without semantic rationale: major visual decisions such as name placement, photo position, column structure or header hierarchy exist because they look acceptable rather than because they solve an information/reading problem. | Major design decisions must map to an information role, reading priority or document constraint and be explainable before rendering. |
| F-034 | Narrative flattening: compression/restructuring removes the layered causal story and 'between-the-lines' evidence that made the candidate's path convincing, even though the remaining sentences are individually correct. | Preserve a narrative coverage/causality map and evaluate information density, transition logic and candidate distinctiveness before approving a shorter draft. |

F-026–F-030 were discovered at G-003 after direct user review of EXP-008. F-031–F-034 were added after the subsequent controlled pre-version runner improved technical/visual quality but still received only a 5/10 user rating because profile richness, narrative specificity and semantic design rationale remained insufficient. These are validation-discovered classes, not retroactively claimed historical incidents.