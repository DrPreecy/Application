# Initial validation — 2026-09-09

## Audit and evidence boundary

Baseline commit: `215db7f461efca6bc4606e83071d7b179a1c6a44`.
All 12 repository files were read, including the complete start instructions, agent rules and evidence register. The recursive GitHub tree was not truncated. GitHub issue search returned no issues. The local checkout matched this commit and was clean before work.

Established behavior remains in the concept baseline and PROJECT_STATE. This report adds experiments and proposals, not new accepted product requirements. No personal memories, applicant dossier, employer facts or approved documents were imported. All scenario data below are synthetic. Existing historical evidence is a summarized account, not original artifacts sufficient for voice or document evaluation.

Missing at baseline: runnable fixtures, experiment results, explicit hypothesis exit criteria, original approved/rejected writing samples, native artifact samples, a measured H0 workflow, runtime/concurrency implementation and user comprehension evidence. All H0–H8 were UNKNOWN; that was accurate. No application code, nested AGENTS files or Actions workflows existed.

## EXP-001 — Dependency feasibility (H2, H6)

**Question:** Can explicit dependencies avoid global blocking and broad invalidation in the historical scenarios?

**Hypothesis:** H2/H6, limited to a fully specified synthetic dependency graph.

**Method:** Before execution, encode explicit expected task/artifact sets in `validation/cases.json`, derived from F-001–006, F-010, F-012–013 and F-021. Run the disposable standard-library model in `validation/experiment.py`. Compare two intentionally faulty alternatives: global blocking and invalidate-everything. The language is an experiment convenience, not a product stack choice.

**Evidence:** `validation/results.json`, produced by actual command `python3 validation/experiment.py > validation/results.json` (exit 0). 11/11 expected-set checks passed; 8 cases reject the applicable historical mutant. Three control cases do not distinguish the mutants, explicitly recorded. This is same-agent authored testing, not independent review.

**Result:** Narrow feasibility supported. An unresolved test/fact need not block unrelated document preparation. Invalidation must follow actual use: a benefit change only affects fit in one graph, but also the application/package when the letter uses that benefit. A fixed list based only on field names would be wrong.

**Limits:** Correct edges are supplied by hand. No dependency discovery, requirement extraction, user-action generation, persistence, locking, security, graph schema validation or concurrent execution is tested. F-006 demonstrates only the downstream effect of correctly interpreted preferred wording; it does not test NLP. F-010 exercises dependency propagation, not package version comparison. F-021 checks an empty task set, not model-call suppression. Synthetic checks are not production regression passes.

**Decision / no decision:** Keep H2/H6 TESTING, not PASS. Continue validation; no walking-skeleton approval or technology choice.

**Affected artifacts:** cases, runner, raw results, hypothesis/evidence registers, fixture procedures, PROJECT_STATE.

**Retest:** Whenever dependency semantics change; repeat against real artifact dependencies and independently specified expectations before claiming general reliability.

## EXP-002 — Identity counterexample review (H1)

**Question:** Does an Opportunity-only identity suffice across reposts and repeat applications?

**Hypothesis:** H1.

**Method:** Manually compare candidate models against three synthetic identity scenarios. This is a structural thought experiment, not an implemented model trial.

| Scenario | Opportunity only | SourcePosting + Opportunity | Opportunity + ApplicationCase |
|---|---|---|---|
| Two URLs advertise one intake | Can work with source identities embedded; one URL as opportunity ID fails | Explicit source identities fit | Needs source identities within opportunity |
| Same URL changes intake/title | URL alone loses history; explicit versions can work | Needs posting revisions and intake mapping | Still needs source revisions/intake mapping |
| User applies again after withdrawal | Single mutable status loses first attempt unless attempt history is embedded | Source separation alone does not solve attempts | Separate case identities express attempts; not proof they need separate storage |

**Evidence:** The scenario matrix above, inspected against the concept's required IDs, versions and history.

**Result:** Labels alone do not determine correctness. Source revisions and application attempts must remain distinguishable for these scenarios; embedding versus separating them remains open. This does not establish a formal aggregate boundary.

**Decision / no decision:** H1 TESTING. No preferred schema accepted. No model agreement counted as evidence.

**Affected artifacts:** this matrix and hypothesis/evidence registers.

**Retest:** Execute all three models against persisted repost/reopen fixtures during a justified identity spike; reject any that overwrite prior evidence or attempt history.

## EXP-003 — Repo + agent workflow rehearsal (H0, H8)

**Question:** What can already be coordinated in repository artifacts, and what requires a user evaluation?

**Hypothesis:** H0/H8. This is a synthetic, partial rehearsal, not the required high-fidelity application trial.

**Method:** Carry one synthetic case through a hand-authored state handoff; apply the EXP-001 changes. Use no applicant facts or external employer claims.

| Step | Stored rehearsal state | Outcome / boundary |
|---|---|---|
| Intake | Case DEMO-001; research v1 stable; truth v1 synthetic | Preparation may begin |
| Eligibility | Required test open; fit assessed separately | Submission blocked; task: complete test |
| Positioning | Positioning p1 references truth v1 | Shared basis for application/CV |
| Document preparation | Application draft a1 and CV draft c1 reference p1; no actual document exports | Content/native-artifact QA remains unexecuted; package is not review-ready |
| Local change | Benefit changes; a1 does not cite benefit | Only fit stale in this fixture; documents retained |
| Material change | Positioning changes to p2 | a1/c1/package require revalidation |
| Resume | Agent can read this persisted table | Human-readable handoff demonstrated; no runtime resume/retry proof |

**Evidence:** This persisted handoff and the actual dependency results. No user task timings, intervention counts or document-quality scores have been measured. No custom application or native documents were produced in this rehearsal.

**Result:** Repository + agent coordination is feasible at this small manual scale. It does not establish whether its user burden is acceptable or custom software adds sufficient value. The missing full workflow is material, not a reason to infer H0 PASS.

**Decision / no decision:** H0/H8 TESTING. Hold the walking-skeleton gate. Ask for the user-owned success criterion below before treating automation savings as sufficient. H4 authentic voice also awaits user-approved evidence; no agent can approve the user's voice.

**Affected artifacts:** report, hypothesis/evidence registers, PROJECT_STATE.

**Retest:** Run a full, consented application case with actual native documents, record user interventions, corrections and duration, and compare against the user's success criterion. Keep personal data outside GitHub.

## G-001 — User value criterion, now ready for a decision

ASTRA_START_HERE explicitly reserves true personal preference and mixed go/no-go evidence to the user. The technical prototype cannot answer whether manual repository coordination is acceptable to them. This is a validation decision, not merge approval.

Concrete contrast for the test case: GitHub + agent can preserve the table, but the user still opens a conversation to resume/review it. A possible custom-system benefit is carrying the case forward without these repeated handoffs and showing one coherent review/action view. That benefit has not been measured and is not an accepted UX requirement.

**Question:** In a real application trial, which remaining work would make GitHub + agents insufficient for you, even if document quality is equally good?

Proposed measurement after the answer: count those interventions and their time, retain quality failures separately, and record user judgment after one full case. Do not invent a numeric threshold or claim user acceptance from model preference.

Next executable work after this decision: establish that H0 success criterion, select a user-authorized reference case outside GitHub, then execute the native-document/voice/workflow trial. Synthetic cases cannot settle user value or authenticity. More infrastructure now would evade the gate rather than resolve it.

## G-001 resolution — user response, 2026-09-09

**Status:** Answered. The preceding question/history is retained, but its equal-quality premise and narrow coordination-only framing are superseded by D-005.

The user describes a specialized process with substantial internal steps, interconnected variables, structured data processing and rating/sorting. They report unreliable prompt-driven execution and insufficient ability to inspect/intervene. Visible intermediate steps and repeatable, traceable quality are explicit goals. This is preference/experience evidence, not a pass for any implementation.

### Corrected validation matrix (proposed test design)

| User criterion | Coupled test scenario | Observable evidence to collect |
|---|---|---|
| Consistent process quality | A high-fit case has missing eligibility data and a weak research claim | Claim cannot silently enter approved text; only dependent work pauses; fit remains separate |
| Structured evaluation | Several factors conflict and one source changes | Preserve inputs, source/version and the existing rating rule; affected assessment changes are explainable; missing weight stays unknown |
| Traceable connections | An applicant fact changes after positioning and documents were approved | Show which conclusions and document parts depend on it; flag those for review; retain unrelated approved material |
| Visible intermediate steps | Research complete, assessment uncertain, CV prepared, application needs review | User can inspect the actual intermediate work, its basis, uncertainty and next action; a final green/red badge is insufficient |
| Targeted intervention | User corrects one source interpretation while other work is ready | Correction applies to its dependent results; no unrelated rewrite; before/after evidence and user review remain available |
| Recovery and consistency | Interrupt, retry, then resume after an upstream correction | No duplicate authoritative result; stale results do not appear current; user sees what happened |

These are proposed combined tests grounded in accepted behavior and D-005, not results. EXP-001 supplies only narrow dependency-set evidence. The missing end-to-end controls, ratings, UI and document production remain untested. More synthetic passes cannot demonstrate user authenticity or sustained quality.

**Next work:** use this matrix for a coupled validation scenario, keeping exact rating tests dependent on the actual existing rules. Do not invent their factors or weights. Any UI used for evaluation is provisional; no final design approval is implied. Evaluate existing tools and a minimal custom approach against the same criteria without presuming either can maintain quality.
