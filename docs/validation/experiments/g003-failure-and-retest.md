# G-003 User Review — EXP-008 Failed

Date: 2026-09-09
Phase: Validation
Status: **FAILED USER QUALITY GATE**

## Why this record exists

EXP-008 produced a new application letter and CV from authorized private reference inputs. Technical checks on native PDF generation and one scoped-edit diff succeeded, but the actual user review rejected the package. Therefore EXP-008 must not be described as a successful end-to-end application-production validation.

The private files remain outside GitHub. This record preserves only sanitized findings.

## User verdict

The user rejected both generated documents.

### Application letter

The user judged the letter to be largely a rewritten/reordered version of the already accepted historical application rather than an independently derived result from Applicant Truth + Opportunity Evidence + Positioning + Voice Evidence.

This exposes a methodological problem: the accepted final artifact was visible during a test whose purpose was to learn whether the system could reconstruct a strong application process. The target answer contaminated the generation step.

### CV

The user rejected the visual result as materially below the established CV/design process. The output was perceived as a plain content dump with weak hierarchy and an inadequately integrated photo rather than a deliberately designed information system.

Technical properties such as native text, one-page A4 output, embedded fonts, extraction order and absence of clipping are necessary checks, but they did not establish design quality.

## Corrected interpretation of EXP-008

EXP-008 demonstrated only narrow technical facts:

- native editable documents can be generated;
- the generated PDFs can contain real text;
- one local heading edit can be isolated technically;
- reference inputs can remain unchanged;
- a portrait image can be transferred without generative alteration.

EXP-008 **did not demonstrate**:

- independent application reasoning;
- authentic voice generation;
- successful employer-specific positioning;
- a reliable Application Concept process;
- successful CV relevance/editorial design;
- a valid Brand/Document Identity Contract;
- package-level user quality;
- autonomous end-to-end production.

The earlier wording “one successful native generation/edit trial” remains true only at the narrow technical artifact level. It must not be interpreted as successful product/document quality.

## Newly discovered failure classes

See `docs/quality/historical-failure-fixtures.md`:

- F-026 Gold-reference leakage
- F-027 Process bypass
- F-028 Design collapse
- F-029 Reference-as-template misuse
- F-030 Output-only optimization

## Root causes

### RC-1 — Gold answer contamination

The final accepted historical application was available during generation. Even when instructed to create a new version, the agent could reuse its argument order, causal structure and phrasing patterns. A similar problem exists for design when a final CV is treated as both data source and design/process reference without explicit permitted-use boundaries.

### RC-2 — Missing mandatory intermediate artifacts

The experiment did not force a reviewable chain such as:

`Source Lock → Evidence Map → Eligibility/Fit → Positioning → Application Concept → Voice Draft → Professionalization → Document Identity → CV Relevance Model → Design Exploration → Selected Design → Native Build → Package QA`

Without those artifacts, a final PDF can appear even when the intended process was bypassed.

### RC-3 — Technical QA was mistaken for quality evidence

Native text, fonts, extraction and geometry checks are technical QA. They do not prove hierarchy, information design, visual coherence, employer fit or user preference.

### RC-4 — Design reasoning was under-specified

The CV production step did not establish and compare serious layout directions before implementation. As a result, the renderer solved “put the information on one page” rather than “derive and execute a coherent information-design system.”

## Corrected retest design

The next real reference-case experiment must prevent answer leakage.

### Phase A — Allowed inputs before generation

The agent may receive:

- verified Applicant Truth / factual career data;
- supporting evidence/zeugnis data;
- the target Opportunity and public employer/program evidence;
- historical process lessons;
- Voice Evidence consisting of approved/rejected tendencies and selected fragments where needed;
- CV/design process lessons and design constraints.

The agent must **not** use the accepted final application or final CV as a wording/layout template.

If a final gold artifact must be supplied because some facts exist only there, those facts must first be extracted into a neutral fact record and the artifact removed from generation context where technically possible.

### Phase B — Mandatory intermediate outputs

Before final document generation, preserve:

1. Source Lock
2. Evidence Map with provenance/scope/permitted use
3. Eligibility and Fit state
4. Positioning Contract
5. Application Concept / Argument Map
6. Voice-First Draft
7. Professionalization diff/pass
8. Document Identity / Brand Contract
9. CV relevance/content model
10. at least two meaningfully different design explorations with rationale
11. selected design and reason for selection
12. native artifacts
13. technical QA
14. package semantic/design QA

A final PDF without this chain is a process-validation failure even if visually acceptable.

### Phase C — Gold comparison only after independent generation

Only after the candidate package is frozen may the historical final application/CV be reintroduced as a **gold comparison**, not a generation source.

Compare:

- which strong arguments were independently rediscovered;
- which were missed;
- where the candidate is better/worse;
- whether wording appears derivative;
- whether the candidate preserves authentic voice;
- whether design quality matches the established process rather than copying a final template.

### Phase D — User gate

The user judges:

- “Das bin ich” / interview-continuability;
- employer specificity;
- application argument quality;
- CV information hierarchy;
- visual coherence;
- photo integration;
- whether intermediate reasoning is understandable and useful.

No same-agent review may substitute for this gate.

## Gate status

- G-003: **FAIL**
- Walking Skeleton: **HOLD**
- H4 authentic voice: remains TESTING with negative evidence from this package
- H5 document generation: technical sub-capability observed; design-quality hypothesis remains unresolved/negative for this candidate
- H6 scoped invalidation/editing: narrow technical evidence retained; does not rescue package quality
- H0 custom-system value: still TESTING

## Next action while Work/Astra quota is unavailable

Do not start another private-file generation run in a context that cannot preserve the required private inputs and process controls.

Repository work may continue safely on:

- codifying F-026–F-030;
- preparing the retest protocol;
- reviewing the validation PR for overclaims;
- creating bounded GitHub/Copilot tasks that do not require private applicant data.

When a suitable private Work session is available again, resume from this retest protocol rather than asking the agent to “improve the PDFs.”
