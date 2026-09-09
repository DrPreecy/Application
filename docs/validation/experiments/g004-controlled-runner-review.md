# G-004 User Review — Controlled Pre-Version Runner v0.1

Date: 2026-09-09
Phase: Validation
Status: **PARTIAL IMPROVEMENT / QUALITY GATE NOT PASSED**
User rating: **5/10**

## Scope

A second controlled reference run was executed outside Work using a pre-version workflow that explicitly separated Applicant Truth, Opportunity Intelligence, Evidence, Eligibility/Fit, Positioning, Document Identity, Application Concept, Voice, CV Relevance, Information Architecture, Design Exploration, Build and QA.

The candidate application and CV are private and are not committed to GitHub. This record preserves sanitized review findings only.

## User verdict

The run was clearly better than the previous failed EXP-008 package, but it still did not demonstrate that the proposed system produces enough quality advantage over a conventional template/manual workflow.

### CV / visual design

The user considered the visual result acceptable but questioned the semantic purpose of major layout decisions. In particular, the placement/emphasis of the name at the top and the overall composition felt insufficiently motivated by the information structure. The document looked cleaner than the prior failed CV, but the design did not yet feel like a coherent system in which every major element had a reason to be where it was.

This distinguishes **visual acceptability** from **semantic information design**. A layout can be clean without having a strong information architecture.

### Application letter

The user judged the structure and opening/ending logic insufficiently distinctive. The letter contained correct and relevant material, but too much of it could plausibly survive an employer swap. The result therefore did not yet justify a complex custom system over a reusable Word template with marked replacement zones.

The accepted historical application contained more layered signals and more 'between-the-lines' information: the reasoning behind the career change, the applicant's way of thinking, employer-specific context and long-term motivation reinforced each other. The new run compressed this richer profile into a smaller set of generic points.

### Applicant profile / source model

The Applicant Data / Motivation & Voice pack used for the runner was too thin. It retained some factual and motivational signals but lost a larger set of requirements, preferences, reasoning patterns and approved/rejected tendencies accumulated during the original application process.

This means the system can fail before writing begins: if the input profile compresses the person too aggressively, later stages cannot recover the missing distinctiveness without inventing it.

## Core product implication

The product goal is not merely to replace labor.

It must produce **quality** that materially exceeds, or is at least demonstrably more reliable than, a much simpler baseline such as:

`Word template + manual employer-specific replacements + human editing`

If the custom system produces a letter that is largely reusable across employers, or a CV whose major visual decisions are arbitrary, the system has not justified its complexity even if the workflow is traceable and technically correct.

This is now accepted as D-006.

## Newly identified failure classes

- F-031 Profile compression loss
- F-032 Template equivalence
- F-033 Design without semantic rationale
- F-034 Narrative flattening

See `docs/quality/historical-failure-fixtures.md`.

## Required corrections before the next serious quality run

### 1. Applicant Profile must become a rich source model

Do not use a small 'motivation pack' as the complete person model.

The next run needs a versioned Applicant Profile that distinguishes at least:

- verified facts;
- current skills/learning stage;
- work-pattern preferences;
- genuine motivations;
- career-change reasoning;
- approved/rejected wording tendencies;
- evidence/examples supporting self-descriptions;
- employer/program preferences;
- constraints and avoid-claims;
- prior user corrections;
- open/uncertain facts.

High-value profile signals must not disappear silently. Maintain a coverage/omission map.

### 2. Positioning must be opportunity-specific enough to change the document

Before writing, identify which opportunity facts are load-bearing for this candidate's decision.

Run a template-swap test:

> If DZ BANK is replaced with another software employer, which paragraphs/arguments must materially change?

If only names and one paragraph change, positioning is insufficient.

### 3. Application needs Narrative Architecture, not only paragraph functions

The system must preserve the causal chain between:

`personal context → way of thinking → prior exploration → current-study learning → reason for transition → why this exact opportunity → why invest in this applicant → future direction`

Shortening is allowed only if the causal information survives. Compare narrative coverage before/after compression.

### 4. Design decisions require semantic traceability

Before rendering, every major visual decision must answer:

- What information role does this solve?
- What should the reader notice first/second/third?
- Why is the name/photo/header placed there?
- What relationship exists between identity, target role, sidebar/main content and chronology?
- What trade-off does this layout make versus another candidate direction?

A design direction is not valid merely because it looks professional.

### 5. H0 needs a real baseline competitor

Future product-value tests must compare the custom process against a simple baseline workflow, not against 'doing nothing'.

Compare at least:

- employer specificity;
- applicant distinctiveness;
- narrative coherence;
- information preservation;
- document design rationale;
- technical quality;
- user correction burden;
- time/effort;
- repeatability.

## Gate status

- G-004: **NOT PASSED**
- Result: partial improvement over G-003, but quality advantage not demonstrated
- H0: TESTING, now requires template-baseline comparison
- H4: TESTING; richer profile and narrative preservation required
- H5: TESTING; visual cleanliness observed but semantic design quality not proven
- Walking Skeleton: HOLD

## Next experiment direction

Do not merely 'improve the wording' or 'make the CV prettier'.

The next run should first rebuild the information foundation:

1. richer Applicant Profile / User Truth + preference/voice evidence;
2. profile coverage map;
3. opportunity-specific value/fit map;
4. narrative architecture;
5. semantic design rationale;
6. only then generation and comparison against the simple-template baseline and hidden historical gold reference.
