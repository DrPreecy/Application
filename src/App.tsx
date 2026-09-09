import { useMemo, useState } from 'react';
import { demoOpportunity, ReadinessState } from './domain';

type Section = 'dashboard' | 'opportunity' | 'profile' | 'packages';

const stateLabels: Record<ReadinessState, string> = {
  READY: 'Ready',
  IN_PROGRESS: 'In progress',
  CONDITIONAL: 'Conditional',
  BLOCKED: 'Blocked',
  PENDING: 'Pending'
};

function App() {
  const [section, setSection] = useState<Section>('dashboard');
  const opportunity = demoOpportunity;

  const readyCount = useMemo(
    () => opportunity.readiness.filter((item) => item.state === 'READY').length,
    [opportunity]
  );

  return (
    <div className="app-shell">
      <aside className="sidebar">
        <div className="brand-block">
          <span className="eyebrow">Prototype v0.1</span>
          <strong>Application Operations</strong>
        </div>

        <nav className="nav-list" aria-label="Main navigation">
          <button className={section === 'dashboard' ? 'active' : ''} onClick={() => setSection('dashboard')}>Dashboard</button>
          <button className={section === 'opportunity' ? 'active' : ''} onClick={() => setSection('opportunity')}>Opportunities</button>
          <button className={section === 'packages' ? 'active' : ''} onClick={() => setSection('packages')}>Packages</button>
          <button className={section === 'profile' ? 'active' : ''} onClick={() => setSection('profile')}>Applicant Profile</button>
        </nav>

        <div className="sidebar-note">
          <span className="eyebrow">Current mode</span>
          <p>Working prototype. Data shown here is demo state, not a production assessment.</p>
        </div>
      </aside>

      <main className="main-content">
        {section === 'dashboard' && (
          <>
            <header className="page-header">
              <div>
                <span className="eyebrow">Today</span>
                <h1>Move one application case forward.</h1>
                <p>See what is ready, what is uncertain and what actually needs your input.</p>
              </div>
              <div className="summary-chip">{readyCount}/{opportunity.readiness.length} axes ready</div>
            </header>

            <section className="hero-card">
              <div className="hero-meta">
                <span>{opportunity.employer}</span>
                <span>{opportunity.location}</span>
                <span>{opportunity.studyPartner}</span>
              </div>
              <h2>{opportunity.program}</h2>
              <p>{opportunity.summary}</p>
              <div className="hero-footer">
                <span>Stage: {opportunity.stage}</span>
                <button onClick={() => setSection('opportunity')}>Open case</button>
              </div>
            </section>

            <section className="grid-two">
              <div className="panel">
                <div className="panel-heading">
                  <div>
                    <span className="eyebrow">Readiness</span>
                    <h3>What can move now?</h3>
                  </div>
                </div>
                <div className="readiness-list">
                  {opportunity.readiness.slice(0, 5).map((item) => (
                    <div className="readiness-row" key={item.label}>
                      <div>
                        <strong>{item.label}</strong>
                        <p>{item.note}</p>
                      </div>
                      <span className={`status status-${item.state.toLowerCase()}`}>{stateLabels[item.state]}</span>
                    </div>
                  ))}
                </div>
              </div>

              <div className="panel">
                <span className="eyebrow">Your actions</span>
                <h3>Only interrupt when it matters.</h3>
                {opportunity.actions.map((action) => (
                  <article className="action-card" key={action.id}>
                    <strong>{action.title}</strong>
                    <p>{action.reason}</p>
                    <small>Blocks: {action.blocks.join(', ')}</small>
                  </article>
                ))}
              </div>
            </section>
          </>
        )}

        {section === 'opportunity' && (
          <>
            <header className="page-header compact">
              <div>
                <span className="eyebrow">Opportunity detail</span>
                <h1>{opportunity.employer}</h1>
                <p>{opportunity.program} · {opportunity.intake} · Job ID {opportunity.jobId}</p>
              </div>
            </header>

            <section className="panel">
              <div className="detail-grid">
                {opportunity.readiness.map((item) => (
                  <article className="axis-card" key={item.label}>
                    <div className="axis-topline">
                      <strong>{item.label}</strong>
                      <span className={`status status-${item.state.toLowerCase()}`}>{stateLabels[item.state]}</span>
                    </div>
                    <p>{item.note}</p>
                  </article>
                ))}
              </div>
            </section>
          </>
        )}

        {section === 'profile' && (
          <>
            <header className="page-header compact">
              <div>
                <span className="eyebrow">Applicant Profile</span>
                <h1>Rich source model, not a short bio.</h1>
                <p>The next implementation slice will make facts, motivations, preferences, evidence and corrections explicit.</p>
              </div>
            </header>
            <section className="panel empty-state">
              <h3>Next build target</h3>
              <p>Create the first structured Applicant Profile editor and coverage map. This is intentionally not filled with private production data yet.</p>
            </section>
          </>
        )}

        {section === 'packages' && (
          <>
            <header className="page-header compact">
              <div>
                <span className="eyebrow">Packages</span>
                <h1>Application + CV belong to one case.</h1>
                <p>Package QA will eventually verify truth, positioning, design identity and unresolved user actions together.</p>
              </div>
            </header>
            <section className="panel empty-state">
              <h3>No review-ready package yet</h3>
              <p>This prototype deliberately shows workflow state before document generation.</p>
            </section>
          </>
        )}
      </main>
    </div>
  );
}

export default App;
