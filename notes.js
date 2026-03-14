// ═══ Shared Speaker Notes & Titles ═══
// Single source of truth — used by presenter.html, remote-notes.html, and script.html.
// Edits made in presenter.html are saved to the server and broadcast to all clients.

var DEFAULT_NOTES = {
  1: `<p><strong>Opening — Title / Dashboard</strong></p>
<p>Good morning / afternoon. I'm Damon Macklin, and I'm here to share a product vision for shaping the future of global mobility platforms.</p>
<p>What you're seeing behind me is a glimpse of what a modern mobility platform should feel like — live data, real-time compliance scores, assignment volumes, cost indices updating as we speak. This is where I believe ECA needs to go: from world-class data to a world-class intelligence platform.</p>
<p><em>Transition:</em> Let me walk you through how.</p>`,

  2: `<p><strong>Global Complexity</strong></p>
<p>Global mobility is becoming more complex every year. Organisations are navigating compliance across 190-plus jurisdictions, trying to control costs, support the employee experience, and maintain visibility across every corridor — from New York to Dubai, London to Singapore, São Paulo to Tokyo.</p>
<p>Yet most systems in this space were designed for administration, not intelligence. That's the gap.</p>
<p><em>Transition:</em> So what do customers actually want?</p>`,

  3: `<p><strong>Customer Insight</strong></p>
<p>They're not buying mobility software. They're buying <em>confidence</em> — confidence in decisions backed by real-time data. They want compliance built into the workflow, not bolted on afterward. They need full cost visibility before they commit to a move. And they want predictable outcomes — forecast-driven planning that turns every assignment into a known quantity.</p>
<p><em>Transition:</em> The good news is ECA already has the foundation.</p>`,

  4: `<p><strong>The Opportunity — ECA's Three Assets</strong></p>
<p>ECA already owns three powerful assets. First: decades of world-class mobility data — cost-of-living, hardship, salary benchmarks — this is a genuine data moat. Second: deep enterprise relationships and trust built over years. Third: domain expertise recognised across 200-plus countries.</p>
<p>The opportunity is to connect these assets into a single platform that turns data into decisions.</p>
<p><em>Transition:</em> Here's how the platform evolves.</p>`,

  5: `<p><strong>Platform Roadmap — Three Stages</strong></p>
<p>The platform evolves in three stages. First, we become a reliable system of record — tracking assignments and compliance accurately. Then we move to a system of insight — using mobility data to actively inform decisions. And ultimately, a system of intelligence — where AI drives recommendations for workforce strategy.</p>
<p>Each stage builds on the last, and each stage delivers standalone value.</p>
<p><em>Transition:</em> Here's the vision for how we bring this together.</p>`,

  6: `<p><strong>Platform Vision</strong></p>
<p>A unified platform for global mobility intelligence. Not just tracking moves — helping organisations answer the critical questions. Where should we relocate talent? What will it actually cost? What compliance risks exist right now? And how do we optimise our workforce strategy globally?</p>
<p>Each of these becomes a core pillar of the platform — location intelligence, cost modelling, risk monitoring, and AI-driven strategy.</p>
<p><em>Transition:</em> And AI runs through all three stages.</p>`,

  7: `<p><strong>AI &amp; Embedded Intelligence</strong></p>
<p>AI should not be a feature you tick off a list. It should be embedded intelligence that runs through the entire platform.</p>
<p>Cost prediction — giving organisations a complete financial picture before any commitment. Risk identification — surfacing compliance issues before they become problems. Recommendations — optimal move strategies drawn from historical data. And insight generation — turning our global data into actionable intelligence automatically.</p>
<p><em>Action:</em> Walk through each popup — the cost predictor modelling a London-to-Singapore senior manager move at £142K with 94% confidence, the risk monitor tracking 847 assignments and flagging critical visa and tax issues in real time.</p>
<p><em>Transition:</em> Here's the 12-month execution plan.</p>`,

  8: `<p><strong>12-Month Execution Roadmap</strong></p>
<p>Four quarters, each with a clear theme and measurable outcomes. Q1: Foundation and quick wins — data consolidation, compliance engine v1, UX parity. Focus is on retaining enterprise customers and getting churn below 8% with time-to-value under 14 days.</p>
<p>Q2: Insight layer — cost prediction engine, compliance alerts, analytics dashboard v2. Expanding within enterprise accounts, targeting NRR plus 8 percentage points and AI upsell live.</p>
<p>Q3: Platform expansion — self-serve mid-market tier, public API and partner integrations, recommendation engine beta. Landing mid-market logos and building the partner pipeline.</p>
<p>Q4: Intelligence suite — AI recommendations GA, predictive modelling, RMC and consultancy channel. Targeting LTV up 35% and NRR above 115% across all segments.</p>
<p><em>Key calls:</em> Platform over bespoke in Q1–Q2. Retention over acquisition until Q3. Each quarter ships demonstrable value.</p>
<p><em>Transition:</em> Focus means saying no. Here's what we double down on — and what we stop.</p>`,

  9: `<p><strong>Dual-Track — Discovery &amp; Delivery</strong></p>
<p>Discovery and delivery run in parallel. Validation doesn't slow us down — it prevents us building the wrong thing.</p>
<p>On the discovery side: weekly user interviews, rapid prototype testing in five days, and usage analytics that reveal what users actually do. On the delivery side: two-week sprint cycles shipping incremental value, feature flags for controlled rollout, and outcome reviews every six weeks where we measure impact against our hypotheses and decide to kill or scale.</p>
<p><em>Transition:</em> But how do we decide what gets built?</p>`,

  10: `<p><strong>Differentiation</strong></p>
<p>Differentiation means doubling down on what compounds and stopping what doesn't. We double down on our proprietary data moat — no competitor has 40 years of global cost-of-living data. We embed compliance intelligence into the workflow. We build AI on top of real mobility outcomes, not generic models. And we go API-first so HRIS and relocation tools can consume our intelligence layer.</p>
<p>Equally important is what we <em>stop</em> doing: bespoke client builds that don't scale, replicating generic HRIS features, manual report generation, and maintaining legacy on-prem deployments.</p>
<p><em>Transition:</em> Sales and CS have a big voice. Here's how we partner.</p>`,

  11: `<p><strong>Partnering with Sales &amp; CS</strong></p>
<p>I believe in partnering closely with Sales and CS — without becoming an order-taker. That means structured input through a Customer Advisory Board with 8–10 enterprise customers meeting quarterly. A shared feedback taxonomy where every request is tagged by revenue at risk, frequency, segment, and effort. Monthly roadmap reviews so Sales and CS see what's coming, why, and what's been deprioritised — with the reasoning. And every declined request is paired with data: segment fit, strategic alignment, opportunity cost.</p>
<p><em>Transition:</em> How do we run discovery while keeping delivery on track?</p>`,

  12: `<p><strong>Prioritisation &amp; Roadmap Governance</strong></p>
<p>Prioritisation follows a clear framework. High value, low effort — ship immediately. High value, high effort — plan and resource carefully. Low value, low effort — fill-ins only if there's spare capacity. Low value, high effort — we say no, with data.</p>
<p><em>Key message:</em> No unscored work enters a sprint, regardless of who asks.</p>
<p><em>Transition:</em> And when that urgent request lands…</p>`,

  13: `<p><strong>Handling Urgent Requests</strong></p>
<p>When that urgent client request lands — "our biggest customer needs X by Friday" — we run it through the same four-step lens. Step 1: Classify — revenue impact, churn risk, scope. Step 2: Size — can we solve with config, not code? Step 3: Trade-off — what gets displaced, and make it visible. Step 4: Commit — if yes, timebox it; if no, propose an alternative.</p>
<p><em>Key message:</em> No unscored work enters a sprint. Every request goes through the same lens. Regardless of who asks.</p>
<p><em>Transition:</em> To know if this is all working, we need the right metrics.</p>`,

  14: `<p><strong>Measurement — Six Key Metrics</strong></p>
<p>Six metrics prove product value. Net Revenue Retention targeting 115-plus percent through data tier and AI upsell expansion. Adoption depth — DAU over MAU above 40%, meaning users are coming back daily. Time to Value under 14 days from signup to first meaningful insight. Logo churn below 8%. Cost to Serve declining 20% year on year through automation. And Feature Value Ratio — the percentage of shipped features with more than 10% adoption after 30 days.</p>
<p>These aren't just reported quarterly. There's a clear cadence — daily standups, weekly discovery syncs, bi-weekly sprint demos, monthly roadmap reviews, and quarterly OKR resets.</p>
<p><em>Transition:</em> There are also risks we need to be honest about.</p>`,

  15: `<p><strong>PE Context — Risks &amp; Trade-offs</strong></p>
<p>Let me be direct about the key risks and trade-offs in a PE-backed cycle. Speed versus quality — I bias toward shipping fast with feature flags, but never compromise on data integrity. For ECA, wrong data costs trust permanently. Platform versus bespoke — I'll ring-fence 80% or more of engineering for scalable features. Growth versus margin — AI and data services improve both; invest in self-serve early. New versus existing — NRR is the PE metric, so I'll protect expansion revenue over net-new development in year one. Build versus buy — build the intelligence layer, it's the moat; buy commodity features. And migration risk — we run parallel for key accounts and migrate in cohorts, not a big bang.</p>
<p><em>Key message:</em> Every trade-off is documented, visible, and reversible.</p>
<p><em>Transition:</em> Let me close with the mission.</p>`,

  16: `<p><strong>Close</strong></p>
<p>The mission is clear: build the platform that organisations rely on to manage global mobility in an increasingly complex world.</p>
<p>Thank you. I'm happy to take questions.</p>`
};

var TITLES = {
  1: 'Shaping the Future of Global Mobility Platforms',
  2: 'Global Mobility is Becoming More Complex',
  3: 'What Customers Really Want',
  4: "ECA's Three Powerful Assets",
  5: 'The Platform Evolves in Three Stages',
  6: 'A Unified Platform for Global Mobility Intelligence',
  7: 'AI: Embedded Intelligence, Not a Feature',
  8: '12-Month Execution Roadmap',
  9: 'Discovery and Delivery Run in Parallel',
  10: 'Double Down on Strengths, Stop What Doesn\'t Compound',
  11: 'Partner with Sales & CS',
  12: 'Prioritisation & Roadmap Governance',
  13: 'Handling Urgent Requests',
  14: 'Six Metrics That Prove Product Value',
  15: 'Key Risks & Trade-offs in a Fast PE Cycle',
  16: 'The Goal'
};
