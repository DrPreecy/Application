# History & Lessons

This document preserves the real development path so the current architecture is not treated as if it had been obvious from the beginning.

## 1. Separate application tasks

The system began as three separate activities:

- Opportunity Intelligence
- Application Writer
- CV Compiler

This separation was useful for improving each craft area, but there was no shared durable model of an application case.

## 2. Application-writing lessons

Early application drafts became too corporate and abstract. The reliable process became:

- truth before presentation;
- raw argumentation before polished prose;
- employer specificity through personal logic, not employer praise;
- voice-first drafting;
- professionalization after the reasoning and voice are correct;
- no invented expertise or motivation;
- explicit “why this employer?” and “why invest in this applicant?”;
- preserve approved paragraphs rather than rewriting everything.

A final application is only credible if the same person could continue the reasoning in an interview.

## 3. CV-production lessons

Early CV work mixed content and design and sometimes relied on image-style whole-page output. This caused recurring failures:

- weak/native-text semantics;
- photo placement and replacement problems;
- geometry drift;
- unrelated areas changing during local fixes;
- over-compression instead of editorial shortening.

The reliable direction became:

- verified applicant data first;
- job-specific content selection second;
- layout/branding third;
- native document rendering;
- immutable/approved photo asset handling;
- content, layout, photo and export locks;
- minimum-change principle after approval;
- technical and visual QA as separate checks.

## 4. Daily automation stage

The three workflows were turned into separate daily automations. This introduced structure but created a false pipeline: scheduled times were acting as if they were dependencies.

A real failure exposed it:

- Intelligence was still researching;
- Application Writer started because its timer fired;
- no stable handoff existed yet;
- it concluded there was no useful application work.

This was a workflow-state problem, not merely a scheduling problem.

## 5. Eligibility over-blocking

Required tests and unresolved user facts showed that one uncertainty could freeze unrelated work.

The corrected rule became:

> **Block the dependency, not the opportunity.**

For example, a required test may block Submission while Positioning, Application and CV preparation continue.

## 6. Shared-state workaround

Explicit handoff JSON and condition-watch polling were introduced between the Dailies. This improved reliability but also revealed the deeper architecture problem: increasing complexity existed only to coordinate three prompts that were parts of one coherent workflow.

## 7. Application Operations System concept

The work was reframed as one persistent system with:

- shared applicant truth;
- opportunity-centered state;
- evidence/provenance;
- dependency-scoped blocking;
- positioning and document-identity contracts;
- bounded semantic workers;
- deterministic state/policy;
- package-level QA;
- explicit user actions;
- dependency-aware invalidation.

The Dailies became possible triggers rather than the system architecture.

## 8. External model review

Gemini and Grok independently recommended validation-first development, traceable requirements, architecture decisions, technical spikes, security/privacy workstreams and historical regression fixtures.

Their agreement is useful evidence about engineering practice, but it is **not product validation**. Shared model priors can converge on the same wrong architecture.

## 9. Meta-red-team correction

The concept itself was attacked before implementation.

Important corrections:

- do not assume a custom app is necessary before validating H0;
- do not prematurely declare Opportunity a formal DDD Aggregate Root;
- do not equate state/dependency-driven behavior with mandatory event sourcing or a dedicated durable-workflow platform;
- do not claim universal ATS compatibility;
- do not use fake 100% guarantees for probabilistic model quality;
- do not use a private GitHub repository as the default personal-data vault;
- design the development process around browser-first GitHub/ChatGPT Work usage;
- use the Application Operations System as a real test case for the user's broader product-planning workflow.

## Current position

The project is ready for **empirical validation**, followed by a deliberately small **walking skeleton** if the evidence supports it. It is not yet ready for a speculative full-platform implementation.
