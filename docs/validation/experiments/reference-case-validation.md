# Authorized reference case: coupled validation

Date: 2026-09-09. Starting PR head: `48a3b47af1c2003d8e4d05fc9793e4c297b768b0`.
Phase: Validation. Same-agent analysis and execution; no independent review or production certification.

## User correction and actual deliverable

During this session the user clarified that the attachments are data sources for **new agent-authored application/CV outputs**, not the primary artifacts to validate. The initial reference inspection below was useful preparation but did not fulfill that intent on its own. EXP-008 completes the requested creation and tests the new outputs. No reference file was edited. The earlier sentence-level gate G-002 was superseded before asking it; current gate G-003 concerns the actual new package.

## Authorization and evidence handling

The user authorized the historical application case as a private validation reference and supplied two PDFs and two supporting document images directly in Work. All four files were readable despite initial attachment-preview errors. Input files, extracted text, renders, private candidate wording and full-file integrity hashes remained outside the repository. They were not uploaded to public search, GitHub, a review bot or a model-provider integration. Only public employer/education-source queries were sent to search.

References below use aliases `reference-letter`, `reference-cv`, `support-image-A/B`. No personal facts, contact details, grades, photos, private filenames, private file hashes or application quotations are included. The user authorized reference use, not automatic promotion of every statement to independently verified Applicant Truth. Original files are frozen, read-only reference inputs; this is not a new content/identity approval.

Private input identity and full output are retained in the Work session's private working records. The sanitized repository alone cannot reproduce the private-file measurements; reruns require re-supplying the authorized inputs. Do not retrieve them from unrelated personal history or reconstruct them from memory.

## EXP-004 — Native artifact quality and extraction disagreement (H5)

**Question:** Do the real reference PDFs support native inspection, and is native text enough to establish reliable reading order?

**Method:** Open both PDFs with PyMuPDF, render all pages at 1.4x, inspect both renders visually, independently extract with pdfplumber, inspect font embedding and span bounds. Inspect the two supporting images directly. Execute `validation/audit_pdf.py` with the private paths, emitting metrics only. Compare the CV's primary content sequence with geometry-based extraction; then execute `validation/reading_order_probe.py` with a reference-specific column boundary.

**Evidence:** `validation/reference-pdf-metrics.json` and `validation/reading-order-results.json`. Both PDFs have one A4 page, embedded referenced fonts, native text and zero text spans outside page bounds. Both visual renders were inspected: no obvious clipped/overlapping text or whole-page rasterization. Visual QA does not establish subjective brand approval. Source and result texts remain private.

**Result:** Real extraction disagreement found. PyMuPDF's content order keeps the main CV narrative together; default pdfplumber geometry extraction inserts six sidebar headings within the education span. A reference-specific split at x=175 points reduces that count to zero and retains all character objects. This repairs our extraction for this reference; it does not repair every external reader or establish ATS compatibility. Bounding-box checks do not detect all clipping/occlusion. Embedded portrait comparison against an independently approved original is unavailable; visual plausibility is not identity verification.

**Decision / no decision:** H5 becomes TESTING, not PASS or a proven generation pipeline. Native text alone cannot be a package-ready gate. Retain both raw extraction results and a declared reading-order procedure privately; no automatic PDF rewrite or design change. Add F-023.

**Affected artifacts:** metric scripts/results, fixture procedures, evidence/hypothesis/project state.

**Retest:** After any export/layout change, use both extractors and visual QA again. The fixed split is valid only for this reference geometry; reject or re-derive it for other layouts. A later export solution requires a bounded renderer spike and user design constraints.

## EXP-005 — Evidence reconciliation across real inputs and live sources (H3, H2)

**Question:** Can supporting evidence, document assertions and conflicting authoritative sources remain distinguishable while useful review continues?

**Method:** Manually compare the private education entries to visible supporting pages, locate the precise public job posting using public identifiers, and inspect the official program/profile sources. Check disputed qualification interpretation against official education guidance. Keep source statements, inference and missing proof separate. No private employer contact or application action.

**Evidence and result:**

| Observation | Classification and allowed consequence |
|---|---|
| Visible education fields match their corresponding CV entries | Supports these fields only; does not verify all career facts or document authenticity |
| Some qualification labels require an interpretation beyond the photographed pages | Official guidance supports a reasoned interpretation; direct individual certificate wording remains distinct from inference. Do not silently downgrade the CV or label the claim false |
| Specific job identity/program/intake matches the document package | Identity consistency supported for the inspected fields; full historical posting snapshot was not supplied |
| Specific posting and program heading name B.Sc.; an incidental rewards paragraph on the program page names B.A. | Record an internal official-source contradiction. Use the specific posting and consistent heading for this field; do not rewrite the package from the incidental paragraph. The origin of the inconsistency is unknown |
| Employer-level role is supported by the official bank profile | Supports employer-role framing, not a guarantee of an individual's future assignment |
| Desired academic performance is expressed without a numerical rejection threshold | Record the stated expectation; invent neither a hard cutoff nor an acceptance probability |
| No rating formula/weights or authoritative positioning/document-identity version records were supplied | Exact scoring and version certification remain unavailable. Do not backfill invented versions or score the real applicant using synthetic labels |

Public source register (retrieved 2026-09-09; current pages are not historical snapshots):

- S-01: [specific job posting](https://jobs.dzbank.de/job/Frankfurt-am-Main-Duales-Studium-zum-Bachelor-of-Science-(THM),-Studiengang-Softwaretechnologie-(mwd),-Start-2027/1406803233/). Relevant locations: title, requirements, reference date and job identifier. Employer-published, program-specific. Short paraphrase only; no contact details retained.
- S-02: [program information](https://karriere.dzbank.de/content/karriere/de/homepage/schueler/thm_softwaretechnologie.html). Compare heading with the degree mentioned in the pay/rewards paragraph. Employer-published; internally inconsistent on that field. Also distinguishes program opportunities from guarantees.
- S-03: [bank profile](https://www.dzbank.de/content/dzbank/de/home/die-dz-bank/profil.html). Employer-wide institutional role only.
- S-04: [official certificate guidance](https://www.schulministerium.nrw/sites/default/files/documents/Merkblatt-zum-Zeugnis-der-allgemeinen-Hochschulreife.pdf), language-reference section and table. Guidance predates the historical case; applicability is considered separately from directly seeing an individual's certification.
- S-05: [official upper-secondary guide, 2019](https://www.schulministerium.nrw/system/files/media/document/file/Die-gymnasiale-Oberstufe-Druckfassung-2019.pdf), printed page 22, qualification conditions. Used as contextual guidance, not a new certificate issued by this agent.

**Decision / no decision:** H3 becomes TESTING. One real reconciliation demonstrates a useful source-scope rule; it does not validate automated research. Add F-024. Continue document inspection and unaffected content review while exact scoring, certification and photo provenance remain unresolved. No invented mandatory test, citizenship rule or blanket opportunity rejection is applied to the real case. Synthetic prerequisite examples from EXP-001 do not become actual employer requirements.

**Affected artifacts:** this source/observation register, new fixtures, hypothesis/evidence register.

**Retest:** Source changes, additional certificate pages, actual rating rules or historical posting snapshots arrive. Reconcile only affected assertions; rerun the coupled holds rather than marking the whole case complete.

## EXP-006 — Coupled controls and interruption rehearsal (H2, H6, H7)

**Question:** Can multiple holds, a local correction, an upstream change and a retried write be handled without treating one fix as universal completion?

**Method:** Translate the private review's failure classes into wholly synthetic state. Supply explicit expected outcomes before running `validation/coupled_experiment.py`. Exercise a candidate result against allowlisted sections, expected revisions and operation IDs; persist a synthetic checkpoint in a temporary file, simulate lost acknowledgement after saving, reopen and retry. Compare deliberately faulty alternative outputs with the expected results. No private PDF is edited.

**Evidence:** `validation/coupled-results.json`: 14/14 checks passed and five deliberately faulty alternative decisions disagree with the oracles. These are output comparisons, not a general mutation-testing framework. Original EXP-001 still passes its 11 checks. Local commands executed, not GitHub Actions.

**Result:** Within this small model:

- several independent review holds coexist; correcting one does not clear the others;
- inspection/unaffected preparation remains available; synthetic fit is separate from eligibility and submission;
- a local qualification change affects only its CV section and package, while a career fact affects positioning and both dependent document sections;
- mismatched positioning and document-identity versions are rejected;
- retry after a saved result and lost acknowledgement does not create a second operation;
- outdated revisions, unrelated locked-section edits, changed payloads reusing an operation ID and incompatible schemas are rejected;
- synthetic authoritative truth and the unrelated locked section remain unchanged.

**Limits:** Explicit dependencies and state labels were supplied manually. No real Applicant Truth store exists. Sequential stale-worker simulation is not simultaneous-writer safety. The file save is not a power-loss-durable transaction (no fsync/locking); no distributed retry, actual schema migration, LLM tool integration or prompt-injection defense was validated. The dummy version compatibility rule does not settle the eventual document-identity contract. Temporary JSON and Python remain disposable experiment tools, not architecture decisions.

**Decision / no decision:** H7 becomes TESTING; H2/H6 remain TESTING. No broad implementation. The next persistence spike must test simultaneous writers, crash points before/after durable commit and schema evolution if a walking skeleton is justified.

**Affected artifacts:** coupled script/results and register/status updates.

**Retest:** Any change to dependencies, candidate acceptance policy, operation identity or persistence implementation; test against actual artifact versions when available.

## EXP-007 — Voice-preserving versus expertise-upgrading edit (H4)

**Question:** Can a local wording change preserve the reference's learning-stage meaning and authentic voice?

**Method:** Locate one exact sentence in the private letter. Prepare one minimal candidate preserving its aspiration to learn, and one deliberately adversarial candidate claiming established professional expertise. Compare meaning manually to the supplied reference. Store wording privately, not in GitHub. Do not apply either candidate to the PDF.

**Evidence:** Exact source sentence found in extracted private text. Same-agent semantic review rejects the expertise upgrade as unsupported by the available reference. The minimal candidate retains the learning aspiration; its authenticity remains unjudged by the user. No rejected historical drafts were supplied, so no invented historical label is used.

**Result:** Semantic claim-strength comparison completed; no automated authenticity performance demonstrated. This also shows why a truthful-looking rewrite needs a user voice benchmark and cannot be approved solely by the authoring model.

**Decision / no decision:** H4 becomes TESTING. G-002 was a proposed gate, subsequently superseded by the user correction and EXP-008: judge the presented minimal rewrite as authentic, or retain the original. This is a calibration label for future writing tests, not authorization to rewrite the whole letter. ASTRA_START_HERE reserves personal preference and identity/content judgment to the user.

**Affected artifacts:** this sanitized record; private candidate record. Original documents unchanged.

**Retest:** After the user supplies the label, use further local examples and approved/rejected historical fragments to test generalization; one accepted sentence is not H4 PASS.

## Current operational picture (H8 stimulus, not final UX)

| Work area | Actual state | What can happen next |
|---|---|---|
| Input inspection | Four authorized private inputs read | Retain originals; inspect additional evidence if supplied |
| Document structure | Native text confirmed; extraction disagreement found | Use reference-specific column reading for this review; do not claim external-reader compatibility |
| Evidence | Selected fields corroborated; some inference/provenance remains | Keep assertion-level provenance; exact scoring awaits the existing rules |
| Source reconciliation | Public source inconsistency recorded; specific degree field reconciled | Retain current package field; do not regenerate from weaker conflicting paragraph |
| Local wording | One conservative candidate prepared privately | User labels authenticity at G-002 |
| Package release | Not certified by this validation | No submission; full truth/photo/version/quality checks remain open |

This table is available for comprehension feedback; no H8 user test has passed. H0 remains TESTING: the real reference exposed process failures that final-looking documents alone conceal, but no controlled custom-versus-existing-workflow trial or repeated production run has been completed.

## Phase gate and next action

**Superseded checkpoint:** G-001 answered under D-005. The proposed G-002 was replaced by G-003 in EXP-008. Walking skeleton remains HOLD.

The authorized independent work in this increment is complete: real artifact/source inspection, a column-reading probe, coupled synthetic controls, private local-edit calibration, sanitized repository records. The user redirected the work to generating the full package before asking for review; see EXP-008. Exact rating rules, original approved photo and authoring/version history are missing inputs to their dependent experiments, not a demand to rebuild the dossier or globally stop useful work.


## EXP-008 — New application package and real scoped-edit test (H4, H5, H6)

**Question:** Can the agent produce its own coherent application/CV from the private reference data and change one local element without corrupting the rest?

**Method:** Use the supplied personal statements and career data as attributed private candidate inputs; reconcile employer/program context with S-01–03. Write a new, shorter letter with its own sequence and phrasing and create a new chronological CV. Use one candidate positioning/identity basis, recorded privately, for both documents. Build two editable DOCX files, render them using the document skill's LibreOffice workflow and export two native PDFs. A4 is inherited from the supplied application-document context. These tools are bounded experiment apparatus, not a production stack decision.

The private fact/positioning basis preserves the applicant's learning stage, administrative experience and career-change reasoning; no technical expertise, new employer requirement or numeric fit score is invented. Some facts remain user-supplied rather than independently certified. The CV portrait is extracted directly from the provided PDF; its image bytes are inserted unchanged. No generative portrait editing occurs. The new layout is an experiment candidate, not a final product UI/brand choice.

**Evidence:** `validation/own-package-results.json`, private DOCX/PDF outputs and inspected render images. Each document is one A4 page, with native text, embedded referenced fonts and zero out-of-bounds text spans. Final renders of both documents were inspected with no obvious clipping/overlap. Both extractors preserve the new CV section order. This is not universal ATS certification.

A temporary copy of the new CV changes only one section heading. After rendering that copy, the image comparison finds **zero changed pixels outside the heading band**. Canonical document XML differs only by the intended text replacement; the embedded image bytes are unchanged. The test variation is not the delivered CV. All four reference input hashes still match their pre-experiment values; hashes themselves remain private.

**Observed process failures and fixes:** The first attempt focused too much on inspecting the supplied final documents; the user corrected the scope. The first native render inherited an unwanted colored title border; the builder removed the inherited style border and both documents were rendered and inspected again. Neither issue is hidden by reporting only successful checks. The creation required human steering once in this session, so autonomous end-to-end success is not claimed.

**Result:** A newly authored two-document package was produced, and one actual local-edit case preserved unaffected output. Content has been reviewed by the same authoring agent for source consistency, but authenticity, photo framing and visual preference are not user-approved. This is one successful native generation/edit trial, not sustained production reliability.

**Decision / no decision:** H4/H5/H6 remain TESTING. G-003 is the user review of these concrete new drafts: does the new letter preserve the applicant's voice and does the new document/photo presentation fit the user? The user may identify scoped corrections; freeze accepted regions only after their verdict. No final submission, broad implementation or final stack choice.

**Affected artifacts:** private deliverables, sanitized result JSON, registers, project state and PR description. No personal document or generator containing personal data is committed.

**Retest:** Apply any user-requested local corrections to these new drafts, repeat scoped diff/export checks and retain unrelated accepted material. Multiple representative cases and actual runtime tests are still needed before H0/H4/H5/H7 can be considered proven.

**Current gate:** G-003, new-package content/visual review. Exact rating rules and original authoring history remain missing only for their dependent experiments. G-001 is not reopened. G-002 is superseded. Walking skeleton remains HOLD.
