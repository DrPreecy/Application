export type ReadinessState = 'READY' | 'IN_PROGRESS' | 'CONDITIONAL' | 'BLOCKED' | 'PENDING';

export type ReadinessAxis = {
  label: string;
  state: ReadinessState;
  note: string;
};

export type UserAction = {
  id: string;
  title: string;
  reason: string;
  blocks: string[];
};

export type Opportunity = {
  id: string;
  employer: string;
  program: string;
  intake: string;
  location: string;
  studyPartner: string;
  jobId: string;
  stage: string;
  summary: string;
  readiness: ReadinessAxis[];
  actions: UserAction[];
};

export const demoOpportunity: Opportunity = {
  id: 'DZBANK-SOFTWARETECH-2027',
  employer: 'DZ BANK',
  program: 'Duales Studium Softwaretechnologie (B.Sc.)',
  intake: '2027',
  location: 'Frankfurt am Main',
  studyPartner: 'THM',
  jobId: '7952',
  stage: 'Application preparation',
  summary:
    'Prototype case used to make the future workflow tangible. Status values are demo state, not a live production assessment.',
  readiness: [
    { label: 'Identity', state: 'READY', note: 'Core opportunity identity captured.' },
    { label: 'Research', state: 'IN_PROGRESS', note: 'Evidence and source mapping are still being developed.' },
    { label: 'Eligibility', state: 'CONDITIONAL', note: 'Requirements are modeled independently from fit.' },
    { label: 'Fit', state: 'IN_PROGRESS', note: 'Qualitative fit analysis belongs here.' },
    { label: 'Positioning', state: 'PENDING', note: 'Starts after enough evidence is available.' },
    { label: 'Application', state: 'PENDING', note: 'No document should be generated before positioning is stable.' },
    { label: 'CV', state: 'PENDING', note: 'Content relevance and design are separate stages.' },
    { label: 'Submission', state: 'BLOCKED', note: 'Submission is always user-owned.' }
  ],
  actions: [
    {
      id: 'demo-review-profile',
      title: 'Review applicant profile coverage',
      reason: 'The last validation run showed that compressing the applicant profile removes distinctiveness.',
      blocks: ['Positioning quality', 'Application quality']
    }
  ]
};
