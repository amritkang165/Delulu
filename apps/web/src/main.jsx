import React, { useEffect, useState } from 'react';
import { createRoot } from 'react-dom/client';
import './styles.css';

const initialIdea = { startupName: '', ideaDescription: '', targetCustomer: '', problem: '', solution: '', industry: 'SaaS', businessModel: 'Subscription' };
const dimensions = [
  { key: 'problemClarity', label: 'Problem clarity', note: 'Can a real person recognize the pain?' },
  { key: 'customerUrgency', label: 'Customer urgency', note: 'Does this need solving right now?' },
  { key: 'technicalComplexity', label: 'Technical complexity', note: 'How much machinery does version one need?' },
  { key: 'monetizationClarity', label: 'Monetization clarity', note: 'Is there a believable path to payment?' },
  { key: 'acquisitionDifficulty', label: 'Acquisition difficulty', note: 'How hard is it to consistently reach buyers?' },
  { key: 'competitionLevel', label: 'Competition level', note: 'How crowded is the alternative set?' },
];

function scoreText(text, fallback = 4) {
  const words = text.trim().split(/\s+/).filter(Boolean).length;
  return Math.min(9, Math.max(2, fallback + Math.round(words / 18)));
}

function evaluateIdea(idea) {
  const combined = Object.values(idea).join(' ').toLowerCase();
  const hasEvidence = /(user|customer|interview|pilot|paying|revenue|waitlist|prototype|validated)/.test(combined);
  const complexityBoost = /(marketplace|hardware|blockchain|delivery|network|platform|real-time|integration)/.test(combined) ? 2 : 0;
  const competitionBoost = /(ai|invoice|tutor|resume|delivery|productivity|analytics|marketplace)/.test(combined) ? 2 : 0;
  const scores = {
    problemClarity: scoreText(idea.problem, 4),
    customerUrgency: scoreText(`${idea.problem} ${idea.targetCustomer}`, 3),
    technicalComplexity: Math.min(10, 3 + complexityBoost + Math.round(idea.solution.length / 140)),
    monetizationClarity: idea.businessModel === 'No clear model yet' ? 3 : idea.businessModel === 'Subscription' ? 6 : 5,
    acquisitionDifficulty: Math.min(10, 4 + Math.round(idea.targetCustomer.length / 40)),
    competitionLevel: Math.min(10, 3 + competitionBoost),
  };
  const uncertainty = Math.round(Object.values(scores).reduce((sum, score) => sum + score, 0) / Object.keys(scores).length + (hasEvidence ? -1 : 1));
  const risks = [];
  if (!hasEvidence) risks.push('No customer evidence is visible yet. The idea is still carrying its assumptions in a backpack.');
  if (scores.technicalComplexity >= 6) risks.push('The first version may be overbuilt before the core demand is proven.');
  if (scores.acquisitionDifficulty >= 6) risks.push('Distribution looks harder than the product pitch makes it sound.');
  if (scores.competitionLevel >= 6) risks.push('Existing alternatives will make differentiation and retention do real work.');
  return {
    scores,
    uncertainty: Math.min(10, Math.max(1, uncertainty)),
    risks,
    recommendation: hasEvidence ? 'Run a narrow paid pilot with the exact customer segment you named. Measure repeat use before adding features.' : 'Interview five people in the target segment this week. Ask about the last time this problem cost them time, money, or patience.',
    roast: scores.technicalComplexity >= 7 ? 'The architecture is already wearing a tiny graduation cap. Make sure it has met a customer before it starts giving a thesis defense.' : `You have a ${uncertainty}/10 uncertainty problem, which is healthier than a 10/10 confidence problem. Go find the receipts.`,
  };
}

function ScoreBar({ score }) { return <div className="score-track"><span style={{ width: `${score * 10}%` }} /></div>; }

function Header({ page, setPage }) {
  return <header className="topbar shell">
    <button className="brand" onClick={() => setPage('evaluate')} aria-label="Go to evaluator"><span className="brand-mark">DS</span><span>DeluluScore</span></button>
    <nav className="main-nav" aria-label="Main navigation">
      <button className={page === 'evaluate' ? 'active' : ''} onClick={() => setPage('evaluate')}>Evaluate</button>
      <button className={page === 'method' ? 'active' : ''} onClick={() => setPage('method')}>How it works</button>
      <button className={page === 'about' ? 'active' : ''} onClick={() => setPage('about')}>About</button>
    </nav>
    <span className="topbar-note"><span className="status-dot" /> v0.1 / illustrative</span>
  </header>;
}

function EvaluatePage({ idea, update, submit, isEvaluating }) {
  return <section className="page-shell evaluate-page">
    <div className="page-intro"><div><p className="eyebrow">01 / The evaluator</p><h1>Is it a <em>business</em>,<br />or a very elaborate hobby?</h1></div><p className="intro-note">Give us the plain-language version. We will return the questions your pitch is quietly avoiding.</p></div>
    <form className="idea-form" onSubmit={submit}>
      <div className="form-ribbon"><span>Founder intake form</span><span>takes about 90 seconds</span></div>
      <div className="form-grid">
        <label className="field"><span>Startup name</span><input required value={idea.startupName} onChange={update('startupName')} placeholder="e.g. LaundryLoop" /></label>
        <label className="field"><span>Industry</span><select value={idea.industry} onChange={update('industry')}><option>SaaS</option><option>AI Application</option><option>Marketplace</option><option>Consumer App</option><option>Hardware</option><option>Other</option></select></label>
        <label className="field field-wide"><span>One-sentence idea <small>Keep the pitch human-sized.</small></span><textarea required rows="3" value={idea.ideaDescription} onChange={update('ideaDescription')} placeholder="We help [customer] solve [pain] by [solution]." /></label>
        <label className="field"><span>Who is it for?</span><input required value={idea.targetCustomer} onChange={update('targetCustomer')} placeholder="College students living in hostels" /></label>
        <label className="field"><span>How will it make money?</span><select value={idea.businessModel} onChange={update('businessModel')}><option>Subscription</option><option>Commission per transaction</option><option>Freemium</option><option>One-time purchase</option><option>No clear model yet</option></select></label>
        <label className="field field-wide"><span>What problem are they living with?</span><textarea required rows="4" value={idea.problem} onChange={update('problem')} placeholder="Describe the frustrating, expensive, recurring thing." /></label>
        <label className="field field-wide"><span>What will you build first?</span><textarea required rows="4" value={idea.solution} onChange={update('solution')} placeholder="Describe the smallest useful version, not the cinematic universe." /></label>
      </div>
      <div className="form-footer"><p><span className="asterisk">*</span> Vibes are charming. Evidence is more useful.</p><button className="primary-button" type="submit" disabled={isEvaluating}>{isEvaluating ? 'Interrogating the idea...' : 'Run the reality check'} <span>↗</span></button></div>
    </form>
  </section>;
}

function MethodPage() {
  return <section className="page-shell content-page"><div className="page-intro"><div><p className="eyebrow">02 / The method</p><h1>No crystal ball.<br /><em>Just better questions.</em></h1></div><p className="intro-note">The score is a conversation starter, not a prophecy with a logo.</p></div><div className="method-grid"><article className="method-card method-dark"><span className="card-number">01</span><h2>Describe the reality.</h2><p>We ask about the person, the pain, the smallest useful solution, and who is supposed to pay for this whole adventure.</p></article><article className="method-card method-mint"><span className="card-number">02</span><h2>Surface the assumptions.</h2><p>Six dimensions turn the pitch into a readable set of risks: demand, complexity, money, distribution, and competition.</p></article><article className="method-card method-blue"><span className="card-number">03</span><h2>Leave with a next move.</h2><p>A score without an action is just decorative anxiety. Each report points you toward the next useful validation step.</p></article></div><div className="method-footer"><span>Important distinction</span><strong>We measure uncertainty, not startup destiny.</strong><p>A high DeluluScore means more evidence is needed. It does not mean the idea is bad, and it definitely does not mean we have met your customers.</p></div></section>;
}

function AboutPage() {
  return <section className="page-shell content-page about-page"><div className="page-intro"><div><p className="eyebrow">03 / About the project</p><h1>Comedy for the<br /><em>confirmation bias.</em></h1></div><p className="intro-note">Built for founders who want the truth, but would prefer it with a little seasoning.</p></div><div className="about-layout"><div className="about-quote">“The infrastructure is ready.<br /><span>The customers remain theoretical.</span>”</div><div className="about-copy"><p>DeluluScore is an open-source experiment in making startup evaluation more transparent, more useful, and less likely to arrive wearing a black turtleneck.</p><p>The long-term product combines structured labeling, classical ML, recommendations, and grounded roasts. For now, this prototype is a local illustrative assessment. It is honest about that because the first validation test is not lying to ourselves.</p><button className="primary-button" onClick={() => window.location.hash = '#evaluate'}>Evaluate an idea <span>↗</span></button></div></div></section>;
}

function ReportPage({ idea, report, reset, setPage }) {
  return <section className="page-shell report-page" aria-live="polite"><div className="report-header"><div><p className="eyebrow">Report / {idea.startupName}</p><h1>Here is where<br /><em>the idea gets real.</em></h1></div><div className="report-actions"><button className="text-button" onClick={reset}>← Edit idea</button><button className="text-button" onClick={() => setPage('method')}>Read the method →</button></div></div><div className="report-grid"><div className="uncertainty-panel"><p className="panel-kicker">Overall uncertainty</p><div className="big-score">{report.uncertainty}<span>/10</span></div><p className="score-verdict">{report.uncertainty >= 8 ? 'The vibes are doing unpaid labour.' : report.uncertainty >= 6 ? 'Promising, but assumption-heavy.' : 'A reasonably testable starting point.'}</p><div className="dial"><span style={{ transform: `rotate(${report.uncertainty * 18 - 90}deg)` }} /></div></div><div className="findings-panel"><p className="panel-kicker">What the first pass sees</p><div className="dimension-list">{dimensions.map((dimension) => <div className="dimension" key={dimension.key}><div className="dimension-top"><span>{dimension.label}</span><strong>{report.scores[dimension.key]}<small>/10</small></strong></div><ScoreBar score={report.scores[dimension.key]} /><p>{dimension.note}</p></div>)}</div></div></div><div className="insight-grid"><article className="insight-card risk-card"><p className="panel-kicker">Risk signals</p><ul>{report.risks.map((risk) => <li key={risk}>{risk}</li>)}</ul></article><article className="insight-card recommendation-card"><p className="panel-kicker">Next move</p><p className="recommendation">{report.recommendation}</p><span className="arrow-badge">↗</span></article><article className="insight-card roast-card"><p className="panel-kicker">A constructive roast</p><p className="roast">“{report.roast}”</p><span className="roast-signoff">With affection, mostly.</span></article></div><p className="report-disclaimer">Local illustrative assessment. Not a trained-model prediction, investment advice, or a prophecy.</p></section>;
}

function App() {
  const [page, setPageState] = useState(window.location.hash.replace('#', '') || 'evaluate');
  const [idea, setIdea] = useState(initialIdea);
  const [report, setReport] = useState(null);
  const [isEvaluating, setIsEvaluating] = useState(false);
  useEffect(() => { const onHash = () => setPageState(window.location.hash.replace('#', '') || 'evaluate'); window.addEventListener('hashchange', onHash); return () => window.removeEventListener('hashchange', onHash); }, []);
  const setPage = (nextPage) => { window.location.hash = `#${nextPage}`; };
  const update = (field) => (event) => setIdea((current) => ({ ...current, [field]: event.target.value }));
  const submit = (event) => { event.preventDefault(); setIsEvaluating(true); window.setTimeout(() => { setReport(evaluateIdea(idea)); setIsEvaluating(false); setPage('report'); }, 450); };
  const reset = () => { setReport(null); setIdea(initialIdea); setPage('evaluate'); };
  const visiblePage = report && page === 'report' ? <ReportPage idea={idea} report={report} reset={reset} setPage={setPage} /> : page === 'method' ? <MethodPage /> : page === 'about' ? <AboutPage /> : <EvaluatePage idea={idea} update={update} submit={submit} isEvaluating={isEvaluating} />;
  return <main><Header page={page} setPage={setPage} />{visiblePage}<footer className="footer shell"><span>DeluluScore / research before rocket fuel</span><span>Made for better questions.</span></footer></main>;
}

createRoot(document.getElementById('root')).render(<App />);
