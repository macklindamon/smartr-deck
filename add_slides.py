#!/usr/bin/env python3
"""Insert 7 new operational-depth slides into the ECA deck."""

import re

DECK = "/Users/damonmacklin/smartr-deck/deck.html"

# ── Logo used on every slide ──────────────────────────
LOGO = '<div class="slide-logo"><svg width="80" height="31" viewBox="0 0 80 31" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M64.375 24.18C59.55 24.18 55.625 20.2864 55.625 15.5C55.625 10.7136 59.55 6.82 64.375 6.82C69.2 6.82 73.125 10.7136 73.125 15.5C73.125 20.2864 69.2 24.18 64.375 24.18ZM7.39375 12.555C8.6125 9.2132 11.8417 6.82 15.625 6.82C16.7542 6.82 17.8312 7.03493 18.8229 7.42347C21.1542 8.33487 23 10.2114 23.8563 12.555H7.39375ZM80 0.628267H74.8104L73.1417 2.66807C71.8146 1.77527 70.3438 1.0788 68.7687 0.622067C67.375 0.217 65.9021 0 64.375 0C62.8479 0 61.375 0.217 59.9833 0.622067C56.875 1.52313 54.1667 3.35833 52.1896 5.80113C50.0396 8.4568 48.7521 11.8296 48.7521 15.5C48.7521 20.2864 44.8271 24.18 40.0021 24.18C35.1771 24.18 31.2521 20.2864 31.2521 15.5C31.2521 10.7136 35.1771 6.82 40.0021 6.82C42.0917 6.82 44.0125 7.5516 45.5187 8.76887L49.8583 3.47407C48.2667 2.1886 46.4167 1.209 44.3937 0.622067C43 0.217 41.5271 0 40.0021 0C38.4771 0 37.0021 0.217 35.6104 0.622067C32.5 1.52313 29.7938 3.35833 27.8167 5.80113C25.8396 3.35833 23.1312 1.52313 20.0208 0.622067C19.6292 0.5084 19.2313 0.4092 18.8271 0.326533C17.7938 0.113667 16.725 0.00206667 15.6292 0.00206667C14.1042 0.00206667 12.6292 0.219067 11.2375 0.624133C4.74167 2.5048 0 8.45267 0 15.5C0 22.5473 4.78333 28.5469 11.3167 30.4027C12.6854 30.7913 14.1292 31 15.625 31C16.7208 31 17.7896 30.8884 18.8229 30.6755C19.1979 30.597 19.5687 30.5081 19.9312 30.4048C21.9812 29.822 23.8583 28.8362 25.4688 27.5363L21.1333 22.2373C20.4417 22.7953 19.6625 23.25 18.8208 23.5786C17.8292 23.9671 16.7521 24.1821 15.6229 24.1821C11.8396 24.1821 8.61042 21.7889 7.39167 18.4471H24.6542C25.1437 20.9705 26.2479 23.2748 27.8083 25.2009C27.8083 25.203 27.8125 25.2051 27.8146 25.2071C29.8104 27.6685 32.5458 29.512 35.6896 30.4048C37.0583 30.7933 38.5021 31.0021 39.9979 31.0021C41.4938 31.0021 42.9375 30.7933 44.3062 30.4048C47.4521 29.512 50.1896 27.6644 52.1854 25.2009C54.1813 27.6665 56.9208 29.512 60.0646 30.4048C61.4333 30.7933 62.8771 31.0021 64.3729 31.0021C65.8687 31.0021 67.3125 30.7933 68.6813 30.4048C70.2812 29.9501 71.7771 29.2495 73.1229 28.3443L74.8083 30.4048H79.9979V15.7521V0.628267H80Z" fill="#E5004D"/></svg></div>'

# ── New CSS ───────────────────────────────────────────
NEW_CSS = """
/* ── ICP Concentric Rings ──────────────────────────── */
.icp-rings{position:relative;width:420px;height:420px;margin:0 auto}
.icp-ring{position:absolute;border-radius:50%;display:flex;align-items:center;justify-content:center;text-align:center;transition:all .7s var(--ease);opacity:0;transform:scale(.7)}
.slide.active .icp-ring.visible{opacity:1;transform:scale(1)}
.icp-ring.r1{inset:0;background:rgba(94,36,194,.04);border:2px dashed rgba(94,36,194,.15)}
.icp-ring.r2{inset:70px;background:rgba(94,36,194,.1);border:2px solid rgba(94,36,194,.25)}
.icp-ring.r3{inset:145px;background:linear-gradient(135deg,var(--purple),var(--purple-bright));border:none;box-shadow:0 0 40px rgba(94,36,194,.4)}
.icp-ring .ring-label{position:absolute;font-weight:700}
.icp-ring.r3 .ring-label{color:#fff;font-size:15px;line-height:1.3}
.icp-ring.r2 .ring-label{top:16px;font-size:13px;color:var(--purple);letter-spacing:.06em;text-transform:uppercase}
.icp-ring.r1 .ring-label{top:20px;font-size:13px;color:var(--text-muted);letter-spacing:.06em;text-transform:uppercase}
@keyframes ringPulse{0%,100%{box-shadow:0 0 40px rgba(94,36,194,.4)}50%{box-shadow:0 0 70px rgba(94,36,194,.6)}}
.icp-ring.r3{animation:ringPulse 3s ease-in-out infinite}

/* ── Dual-track lanes ──────────────────────────────── */
.dual-track{display:flex;gap:48px;margin-top:44px;width:100%;max-width:1680px}
.track-lane{flex:1;position:relative}
.track-header{display:flex;align-items:center;gap:12px;margin-bottom:24px}
.track-header .track-dot{width:14px;height:14px;border-radius:50%;flex-shrink:0}
.track-header h3{font-size:24px;font-weight:700}
.track-items{display:flex;flex-direction:column;gap:12px}
.track-item{border-radius:14px;padding:22px 24px;display:flex;gap:14px;align-items:flex-start;transition:transform .4s var(--ease)}
.track-item:hover{transform:translateX(4px)}
.theme-dark .track-item{background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.08)}
.theme-dark .track-item:hover{background:rgba(255,255,255,.12)}
.track-item .ti-icon{width:44px;height:44px;border-radius:10px;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.track-item .ti-icon svg{width:22px;height:22px;fill:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
.track-item h4{font-size:18px;font-weight:700;margin-bottom:3px}
.track-item p{font-size:15px;font-weight:500;line-height:1.4}
.theme-dark .track-item h4{color:#fff}
.theme-dark .track-item p{color:rgba(255,255,255,.5)}
.theme-white .track-item{background:#fff;border:1px solid rgba(0,0,0,.05);box-shadow:0 4px 20px rgba(0,0,0,.04)}
.track-divider{position:absolute;right:-24px;top:60px;bottom:0;width:0;display:flex;flex-direction:column;align-items:center;gap:10px}
.track-divider-line{width:2px;flex:1;background:linear-gradient(180deg,var(--purple-light),transparent);border-radius:1px}
@keyframes pulseSync{0%,100%{opacity:.3;transform:scale(.9)}50%{opacity:1;transform:scale(1.1)}}
.track-sync-dot{width:12px;height:12px;border-radius:50%;background:var(--purple-light);animation:pulseSync 2s ease-in-out infinite;flex-shrink:0}

/* ── Prioritisation matrix ─────────────────────────── */
.matrix-wrap{position:relative;width:640px;flex-shrink:0}
.matrix-2x2{display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:3px;width:100%;aspect-ratio:1.3;border-radius:20px;overflow:hidden}
.matrix-cell{display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:28px 20px;transition:all .5s var(--ease)}
.matrix-cell h4{font-size:18px;font-weight:700;margin-bottom:6px}
.matrix-cell p{font-size:14px;font-weight:500;line-height:1.4}
.matrix-axes{display:flex;justify-content:space-between;margin-top:12px;padding:0 8px}
.matrix-axes span{font-size:12px;font-weight:700;color:var(--text-muted);text-transform:uppercase;letter-spacing:.1em}

/* ── Metric gauge cards ────────────────────────────── */
.metric-row{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-top:44px;width:100%;max-width:1680px}
.metric-card{background:var(--card-bg);border-radius:18px;padding:36px 24px;text-align:center;border:1px solid rgba(0,0,0,.04);transition:all .4s var(--ease)}
.metric-card:hover{transform:translateY(-4px);box-shadow:0 16px 48px rgba(94,36,194,.1)}
.metric-card .metric-val{font-size:44px;font-weight:800;margin-bottom:4px}
.metric-card .metric-name{font-size:17px;font-weight:700;margin-bottom:4px}
.metric-card .metric-desc{font-size:14px;font-weight:500;color:var(--text-body);line-height:1.4}
.metric-card .metric-mini{display:flex;align-items:flex-end;justify-content:center;gap:4px;height:36px;margin-top:14px}
.metric-card .metric-mini span{display:block;width:8px;border-radius:4px;transition:height .5s var(--ease)}

/* ── Cadence timeline ──────────────────────────────── */
.cadence-row{display:flex;align-items:flex-start;gap:0;margin-top:48px;width:100%;max-width:1680px;position:relative}
.cadence-row::before{content:'';position:absolute;top:18px;left:60px;right:60px;height:3px;background:var(--divider);border-radius:2px}
.theme-dark .cadence-row::before{background:rgba(255,255,255,.1)}
.cadence-item{flex:1;display:flex;flex-direction:column;align-items:center;text-align:center;position:relative;z-index:1;padding:0 12px}
.cadence-dot{width:16px;height:16px;border-radius:50%;margin-bottom:14px;transition:all .5s var(--ease);opacity:.3}
.cadence-item.lit .cadence-dot{opacity:1;box-shadow:0 0 16px currentColor}
.cadence-item h4{font-size:17px;font-weight:700;margin-bottom:6px}
.cadence-item p{font-size:14px;font-weight:500;max-width:200px;line-height:1.4}
.theme-dark .cadence-item h4{color:#fff}
.theme-dark .cadence-item p{color:rgba(255,255,255,.45)}

/* ── Trade-off grid ────────────────────────────────── */
.tradeoff-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:24px;margin-top:44px;width:100%;max-width:1680px}
.tradeoff-card{border-radius:18px;padding:32px 28px;display:flex;gap:16px;align-items:flex-start}
.tradeoff-card .tf-marker{width:5px;border-radius:3px;flex-shrink:0;min-height:60px;align-self:stretch}
.tradeoff-card h4{font-size:19px;font-weight:700;margin-bottom:6px}
.tradeoff-card p{font-size:16px;font-weight:500;line-height:1.5}
.theme-dark .tradeoff-card{background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.08)}
.theme-dark .tradeoff-card:hover{background:rgba(255,255,255,.1)}
.theme-dark .tradeoff-card h4{color:#fff}
.theme-dark .tradeoff-card p{color:rgba(255,255,255,.5)}

/* ── Escalation flow ───────────────────────────────── */
.esc-flow{display:flex;align-items:center;gap:0;margin-top:28px;flex-wrap:wrap}
.esc-step{display:flex;flex-direction:column;align-items:center;text-align:center;padding:16px 20px}
.esc-step .esc-num{width:40px;height:40px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:16px;font-weight:800;color:#fff;margin-bottom:10px}
.esc-step h4{font-size:15px;font-weight:700;margin-bottom:4px}
.esc-step p{font-size:13px;font-weight:500;max-width:140px;line-height:1.35}
.theme-dark .esc-step h4{color:#fff}
.theme-dark .esc-step p{color:rgba(255,255,255,.45)}
.esc-arrow{font-size:20px;color:var(--purple-light);margin:0 6px;padding-top:0}

/* ── Kill / stop items ─────────────────────────────── */
.stop-item{position:relative;padding:16px 20px;border-radius:12px;display:flex;align-items:center;gap:12px}
.stop-item::after{content:'';position:absolute;left:20px;right:20px;top:50%;height:2px;background:var(--pink);border-radius:1px}
.stop-item h4{font-size:17px;font-weight:600;opacity:.5}
.theme-white .stop-item{background:rgba(229,0,77,.04);border:1px solid rgba(229,0,77,.1)}
.theme-dark .stop-item{background:rgba(229,0,77,.08);border:1px solid rgba(229,0,77,.15)}
.theme-dark .stop-item h4{color:rgba(255,255,255,.4)}
.stop-icon{width:28px;height:28px;border-radius:50%;background:var(--pink);display:flex;align-items:center;justify-content:center;flex-shrink:0;position:relative;z-index:2}
.stop-icon svg{width:14px;height:14px;stroke:#fff;fill:none;stroke-width:3;stroke-linecap:round}

/* ── Venn diagram ──────────────────────────────────── */
.venn-wrap{position:relative;width:380px;height:340px;margin:0 auto;flex-shrink:0}
.venn-circle{position:absolute;width:200px;height:200px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:15px;font-weight:700;text-align:center;line-height:1.3;transition:all .6s var(--ease)}
.venn-circle.vc1{top:0;left:30px;background:rgba(94,36,194,.15);border:2px solid var(--purple-light);color:var(--purple-light)}
.venn-circle.vc2{top:0;right:30px;background:rgba(229,0,77,.1);border:2px solid rgba(229,0,77,.5);color:var(--pink)}
.venn-circle.vc3{bottom:0;left:50%;transform:translateX(-50%);background:rgba(0,207,186,.1);border:2px solid rgba(0,207,186,.5);color:var(--teal)}
.venn-center{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:56px;height:56px;border-radius:50%;background:var(--purple);display:flex;align-items:center;justify-content:center;box-shadow:0 0 30px rgba(94,36,194,.5);z-index:3}
.venn-center svg{width:24px;height:24px;stroke:#fff;fill:none;stroke-width:2;stroke-linecap:round}
"""

# ── SLIDE 8: ICP & Market Segmentation ────────────────
SLIDE_8 = f'''
<!-- ═══════════════════════════════════════════════════ -->
<!-- SLIDE 8 — ICP & Market Segmentation                -->
<!-- ═══════════════════════════════════════════════════ -->
<section class="slide theme-white" data-slide="8">
  <div class="deco purple" style="width:450px;height:450px;top:-180px;right:-120px"></div>
  <div class="deco pink" style="width:250px;height:250px;bottom:-80px;left:-60px"></div>
  <div class="slide-split">
    <div class="slide-left" style="flex:.55">
      <div class="label-tag anim" data-delay="50">Market Focus</div>
      <h2 class="slide-heading anim" data-delay="100" style="text-align:left">Who we <span class="accent-purple">target first</span> and why</h2>
      <p class="body-text anim" data-delay="250" style="margin-top:16px;max-width:520px">In a PE cycle, focus beats breadth. We concentrate on segments with highest LTV and fastest path to NRR growth.</p>
      <div style="margin-top:36px;display:flex;flex-direction:column;gap:14px">
        <div class="card accent-top anim" data-delay="400" style="display:flex;gap:16px;align-items:flex-start;padding:22px 24px">
          <div class="icon purple-bg" style="flex-shrink:0;width:48px;height:48px"><svg viewBox="0 0 24 24"><path d="M21 16V8a2 2 0 00-1-1.73l-7-4a2 2 0 00-2 0l-7 4A2 2 0 003 8v8a2 2 0 001 1.73l7 4a2 2 0 002 0l7-4A2 2 0 0021 16z"/></svg></div>
          <div><h3 style="font-size:20px">Enterprise Multinationals</h3><p style="font-size:15px">500+ assignees, complex corridors, highest ARPA. They need intelligence, not just admin.</p></div>
        </div>
        <div class="card anim" data-delay="550" style="display:flex;gap:16px;align-items:flex-start;padding:22px 24px;border-left:3px solid var(--teal)">
          <div class="icon teal-bg" style="flex-shrink:0;width:48px;height:48px"><svg viewBox="0 0 24 24"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 00-3-3.87"/><path d="M16 3.13a4 4 0 010 7.75"/></svg></div>
          <div><h3 style="font-size:20px">Mid-Market Growth</h3><p style="font-size:15px">50–500 assignees. Scaling internationally, price-sensitive but high-growth potential.</p></div>
        </div>
        <div class="card anim" data-delay="700" style="display:flex;gap:16px;align-items:flex-start;padding:22px 24px;border-left:3px solid var(--pink)">
          <div class="icon pink-bg" style="flex-shrink:0;width:48px;height:48px"><svg viewBox="0 0 24 24"><path d="M2 3h6a4 4 0 014 4v14a3 3 0 00-3-3H2z"/><path d="M22 3h-6a4 4 0 00-4 4v14a3 3 0 013-3h7z"/></svg></div>
          <div><h3 style="font-size:20px">RMCs & Consultancies</h3><p style="font-size:15px">Channel partners who embed our data into their services. Extends reach without direct sales cost.</p></div>
        </div>
      </div>
    </div>
    <div class="slide-right" style="flex:.45;display:flex;align-items:center;justify-content:center">
      <div class="icp-rings anim scale-in" data-delay="300">
        <div class="icp-ring r1"><span class="ring-label">Consultancies &amp; RMCs</span></div>
        <div class="icp-ring r2"><span class="ring-label">Mid-Market 50–500</span></div>
        <div class="icp-ring r3"><span class="ring-label">Enterprise<br>500+</span></div>
      </div>
    </div>
  </div>
  {LOGO}
</section>
'''

# ── SLIDE 9: Differentiation & Kill List ──────────────
SLIDE_9 = f'''
<!-- ═══════════════════════════════════════════════════ -->
<!-- SLIDE 9 — Differentiation & What to Stop           -->
<!-- ═══════════════════════════════════════════════════ -->
<section class="slide theme-dark" data-slide="9">
  <div class="deco purple" style="width:500px;height:500px;bottom:-200px;left:-180px"></div>
  <div class="particle" style="width:5px;height:5px;background:var(--pink);top:20%;right:15%;animation-delay:2s"></div>
  <div class="particle" style="width:4px;height:4px;background:var(--lime);top:60%;left:10%;animation-delay:5s"></div>
  <div class="slide-inner">
    <div class="label-tag anim" data-delay="50">Differentiation</div>
    <h2 class="slide-heading anim" data-delay="100" style="color:#fff">Double down on strengths.<br><span style="color:var(--pink)">Stop what doesn't compound.</span></h2>
    <div style="display:flex;gap:56px;margin-top:48px;width:100%;max-width:1680px">
      <!-- Double Down column -->
      <div style="flex:1">
        <div class="anim" data-delay="300" style="display:flex;align-items:center;gap:10px;margin-bottom:20px">
          <div style="width:12px;height:12px;border-radius:50%;background:var(--lime)"></div>
          <h3 style="font-size:22px;font-weight:700;color:var(--lime)">Double Down</h3>
        </div>
        <div style="display:flex;flex-direction:column;gap:12px">
          <div class="card anim" data-delay="400" style="padding:22px 24px;display:flex;gap:14px;align-items:center">
            <div style="width:8px;height:8px;border-radius:50%;background:var(--lime);flex-shrink:0"></div>
            <div><h3 style="font-size:17px;margin:0">Proprietary data moat</h3><p style="font-size:14px;margin-top:2px">No competitor has 40 years of global cost-of-living data</p></div>
          </div>
          <div class="card anim" data-delay="500" style="padding:22px 24px;display:flex;gap:14px;align-items:center">
            <div style="width:8px;height:8px;border-radius:50%;background:var(--lime);flex-shrink:0"></div>
            <div><h3 style="font-size:17px;margin:0">Compliance intelligence</h3><p style="font-size:14px;margin-top:2px">Embed regulatory logic into the workflow — not bolted on</p></div>
          </div>
          <div class="card anim" data-delay="600" style="padding:22px 24px;display:flex;gap:14px;align-items:center">
            <div style="width:8px;height:8px;border-radius:50%;background:var(--lime);flex-shrink:0"></div>
            <div><h3 style="font-size:17px;margin:0">AI on top of real data</h3><p style="font-size:14px;margin-top:2px">Models trained on actual mobility outcomes, not generic LLMs</p></div>
          </div>
          <div class="card anim" data-delay="700" style="padding:22px 24px;display:flex;gap:14px;align-items:center">
            <div style="width:8px;height:8px;border-radius:50%;background:var(--lime);flex-shrink:0"></div>
            <div><h3 style="font-size:17px;margin:0">API-first platform</h3><p style="font-size:14px;margin-top:2px">Let HRIS & relocation tools consume our intelligence layer</p></div>
          </div>
        </div>
      </div>
      <!-- Stop Doing column -->
      <div style="flex:1">
        <div class="anim" data-delay="350" style="display:flex;align-items:center;gap:10px;margin-bottom:20px">
          <div style="width:12px;height:12px;border-radius:50%;background:var(--pink)"></div>
          <h3 style="font-size:22px;font-weight:700;color:var(--pink)">Stop Doing</h3>
        </div>
        <div style="display:flex;flex-direction:column;gap:12px">
          <div class="stop-item anim" data-delay="500">
            <div class="stop-icon"><svg viewBox="0 0 24 24"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg></div>
            <h4>Bespoke client builds that don't scale</h4>
          </div>
          <div class="stop-item anim" data-delay="600">
            <div class="stop-icon"><svg viewBox="0 0 24 24"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg></div>
            <h4>Replicating generic HRIS features</h4>
          </div>
          <div class="stop-item anim" data-delay="700">
            <div class="stop-icon"><svg viewBox="0 0 24 24"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg></div>
            <h4>Manual report generation for each client</h4>
          </div>
          <div class="stop-item anim" data-delay="800">
            <div class="stop-icon"><svg viewBox="0 0 24 24"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg></div>
            <h4>Maintaining legacy on-prem deployments</h4>
          </div>
          <div class="stop-item anim" data-delay="900">
            <div class="stop-icon"><svg viewBox="0 0 24 24"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg></div>
            <h4>Feature parity with broad HR platforms</h4>
          </div>
        </div>
      </div>
    </div>
  </div>
  {LOGO}
</section>
'''

# ── SLIDE 10: Discovery & Validation ──────────────────
SLIDE_10 = f'''
<!-- ═══════════════════════════════════════════════════ -->
<!-- SLIDE 10 — Discovery Without Slowing Delivery      -->
<!-- ═══════════════════════════════════════════════════ -->
<section class="slide theme-white" data-slide="10">
  <div class="deco purple" style="width:400px;height:400px;top:-160px;left:-120px"></div>
  <div class="deco teal" style="width:200px;height:200px;bottom:-60px;right:-50px;background:var(--teal);opacity:.04"></div>
  <div class="slide-inner">
    <div class="label-tag anim" data-delay="50">Dual-Track</div>
    <h2 class="slide-heading anim" data-delay="100">Discovery and delivery run <span class="accent-purple">in parallel</span></h2>
    <p class="body-text anim" data-delay="200" style="text-align:center;margin-top:12px;max-width:720px">Validation doesn't slow us down — it prevents us building the wrong thing. Time-boxed discovery feeds a continuous delivery engine.</p>
    <div class="dual-track">
      <!-- Discovery track -->
      <div class="track-lane">
        <div class="track-header anim" data-delay="300">
          <div class="track-dot" style="background:var(--purple)"></div>
          <h3 style="color:var(--purple)">Continuous Discovery</h3>
        </div>
        <div class="track-items">
          <div class="track-item anim" data-delay="400">
            <div class="ti-icon" style="background:var(--purple-pale)"><svg viewBox="0 0 24 24" stroke="var(--purple)"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 00-3-3.87"/><path d="M16 3.13a4 4 0 010 7.75"/></svg></div>
            <div><h4>Weekly user interviews</h4><p>2–3 sessions/week with enterprise mobility managers</p></div>
          </div>
          <div class="track-item anim" data-delay="500">
            <div class="ti-icon" style="background:var(--purple-pale)"><svg viewBox="0 0 24 24" stroke="var(--purple)"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18"/><path d="M9 21V9"/></svg></div>
            <div><h4>Prototype &rarr; test in 5 days</h4><p>Figma prototypes validated before a single line of code</p></div>
          </div>
          <div class="track-item anim" data-delay="600">
            <div class="ti-icon" style="background:var(--purple-pale)"><svg viewBox="0 0 24 24" stroke="var(--purple)"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg></div>
            <div><h4>Usage analytics &amp; signals</h4><p>Behavioural data reveals what users do, not just what they say</p></div>
          </div>
        </div>
        <!-- Divider -->
        <div class="track-divider">
          <div class="track-sync-dot anim" data-delay="350"></div>
          <div class="track-divider-line anim" data-delay="400"></div>
          <div class="track-sync-dot anim" data-delay="450"></div>
          <div class="track-divider-line anim" data-delay="500"></div>
          <div class="track-sync-dot anim" data-delay="550"></div>
        </div>
      </div>
      <!-- Delivery track -->
      <div class="track-lane">
        <div class="track-header anim" data-delay="350">
          <div class="track-dot" style="background:var(--teal)"></div>
          <h3 style="color:var(--teal)">Continuous Delivery</h3>
        </div>
        <div class="track-items">
          <div class="track-item anim" data-delay="450">
            <div class="ti-icon" style="background:rgba(0,207,186,.12)"><svg viewBox="0 0 24 24" stroke="var(--teal)"><polyline points="20 6 9 17 4 12"/></svg></div>
            <div><h4>2-week sprint cycles</h4><p>Ship incremental value every sprint — no 6-month bets</p></div>
          </div>
          <div class="track-item anim" data-delay="550">
            <div class="ti-icon" style="background:rgba(0,207,186,.12)"><svg viewBox="0 0 24 24" stroke="var(--teal)"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg></div>
            <div><h4>Feature flags &amp; gradual rollout</h4><p>De-risk releases with controlled exposure to real users</p></div>
          </div>
          <div class="track-item anim" data-delay="650">
            <div class="ti-icon" style="background:rgba(0,207,186,.12)"><svg viewBox="0 0 24 24" stroke="var(--teal)"><polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/><polyline points="17 6 23 6 23 12"/></svg></div>
            <div><h4>Outcome reviews every 6 weeks</h4><p>Measure impact against hypothesis — kill or scale features</p></div>
          </div>
        </div>
      </div>
    </div>
  </div>
  {LOGO}
</section>
'''

# ── SLIDE 11: Prioritisation & Governance ─────────────
SLIDE_11 = f'''
<!-- ═══════════════════════════════════════════════════ -->
<!-- SLIDE 11 — Prioritisation & Roadmap Governance     -->
<!-- ═══════════════════════════════════════════════════ -->
<section class="slide theme-dark" data-slide="11">
  <div class="deco pink" style="width:350px;height:350px;top:-120px;right:-100px;opacity:.05"></div>
  <div class="particle" style="width:5px;height:5px;background:var(--purple-light);top:25%;left:8%;animation-delay:1s"></div>
  <div class="particle" style="width:3px;height:3px;background:var(--teal);top:75%;right:12%;animation-delay:4s"></div>
  <div class="slide-inner">
    <div class="label-tag anim" data-delay="50">Governance</div>
    <h2 class="slide-heading anim" data-delay="100" style="color:#fff">How we prioritise — and handle <span class="accent-purple">urgent requests</span></h2>
    <div style="display:flex;gap:56px;align-items:flex-start;margin-top:40px;width:100%;max-width:1680px">
      <!-- Matrix -->
      <div class="matrix-wrap anim scale-in" data-delay="300">
        <div class="matrix-2x2">
          <div class="matrix-cell" style="background:rgba(163,245,199,.12)">
            <h4 style="color:var(--lime)">Quick Wins</h4>
            <p style="color:rgba(255,255,255,.6)">High value, low effort.<br>Ship immediately.</p>
          </div>
          <div class="matrix-cell" style="background:rgba(94,36,194,.2)">
            <h4 style="color:var(--purple-light)">Strategic Bets</h4>
            <p style="color:rgba(255,255,255,.6)">High value, high effort.<br>Plan &amp; resource carefully.</p>
          </div>
          <div class="matrix-cell" style="background:rgba(255,255,255,.04)">
            <h4 style="color:rgba(255,255,255,.4)">Fill-ins</h4>
            <p style="color:rgba(255,255,255,.35)">Low value, low effort.<br>Only if spare capacity.</p>
          </div>
          <div class="matrix-cell" style="background:rgba(229,0,77,.1)">
            <h4 style="color:var(--pink)">Say No</h4>
            <p style="color:rgba(255,255,255,.5)">Low value, high effort.<br>Decline with data.</p>
          </div>
        </div>
        <div class="matrix-axes" style="margin-top:14px">
          <span style="color:rgba(255,255,255,.3)">Low Effort</span>
          <span style="color:rgba(255,255,255,.3)">High Effort</span>
        </div>
        <div style="position:absolute;left:-24px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:space-between;padding:10px 0">
          <span style="font-size:12px;font-weight:700;color:rgba(255,255,255,.3);text-transform:uppercase;letter-spacing:.1em;writing-mode:vertical-lr;transform:rotate(180deg)">High Value</span>
          <span style="font-size:12px;font-weight:700;color:rgba(255,255,255,.3);text-transform:uppercase;letter-spacing:.1em;writing-mode:vertical-lr;transform:rotate(180deg)">Low Value</span>
        </div>
      </div>
      <!-- Escalation flow -->
      <div style="flex:1">
        <h3 class="anim" data-delay="400" style="font-size:22px;font-weight:700;color:#fff;margin-bottom:6px">Urgent Client Requests</h3>
        <p class="anim" data-delay="450" style="font-size:16px;color:rgba(255,255,255,.5);margin-bottom:24px">"Our biggest customer needs X by Friday" — here's how we handle it:</p>
        <div class="esc-flow">
          <div class="esc-step anim" data-delay="550">
            <div class="esc-num" style="background:var(--purple)">1</div>
            <h4>Classify</h4>
            <p>Revenue impact? Churn risk? Scope?</p>
          </div>
          <div class="esc-arrow anim" data-delay="600">&rarr;</div>
          <div class="esc-step anim" data-delay="650">
            <div class="esc-num" style="background:var(--teal)">2</div>
            <h4>Size</h4>
            <p>Can we solve with config, not code?</p>
          </div>
          <div class="esc-arrow anim" data-delay="700">&rarr;</div>
          <div class="esc-step anim" data-delay="750">
            <div class="esc-num" style="background:var(--pink)">3</div>
            <h4>Trade-off</h4>
            <p>What gets displaced? Make it visible.</p>
          </div>
          <div class="esc-arrow anim" data-delay="800">&rarr;</div>
          <div class="esc-step anim" data-delay="850">
            <div class="esc-num" style="background:var(--lime);color:var(--navy)">4</div>
            <h4>Commit</h4>
            <p>If yes: time-box it. If no: propose alternative.</p>
          </div>
        </div>
        <div class="card anim" data-delay="950" style="margin-top:28px;padding:20px 24px;display:flex;gap:12px;align-items:center">
          <div style="width:8px;height:8px;border-radius:50%;background:var(--purple-light);flex-shrink:0"></div>
          <p style="font-size:15px;color:rgba(255,255,255,.6)"><strong style="color:#fff">Rule:</strong> No unscored work enters a sprint. Every request goes through the same lens — regardless of who asks.</p>
        </div>
      </div>
    </div>
  </div>
  {LOGO}
</section>
'''

# ── SLIDE 12: Sales/CS Partnership ────────────────────
SLIDE_12 = f'''
<!-- ═══════════════════════════════════════════════════ -->
<!-- SLIDE 12 — Sales/CS Partnership                    -->
<!-- ═══════════════════════════════════════════════════ -->
<section class="slide theme-purple" data-slide="12">
  <div class="deco pink" style="width:350px;height:350px;bottom:-150px;left:-100px;opacity:.08"></div>
  <div class="particle" style="width:5px;height:5px;background:var(--lime);top:15%;right:20%;animation-delay:1s"></div>
  <div class="particle" style="width:4px;height:4px;background:var(--purple-light);top:70%;left:15%;animation-delay:3s"></div>
  <div class="slide-inner">
    <div class="label-tag anim" data-delay="50" style="background:rgba(255,255,255,.15);color:#fff">Partnering Model</div>
    <h2 class="slide-heading anim" data-delay="100" style="color:#fff">Partner with Sales &amp; CS — without becoming an <span style="color:var(--lime)">order-taker</span></h2>
    <div style="display:flex;gap:64px;align-items:center;margin-top:44px;width:100%;max-width:1680px;flex-wrap:wrap;justify-content:center">
      <!-- Venn diagram -->
      <div class="venn-wrap anim scale-in" data-delay="300">
        <div class="venn-circle vc1">Product</div>
        <div class="venn-circle vc2">Sales</div>
        <div class="venn-circle vc3">CS</div>
        <div class="venn-center"><svg viewBox="0 0 24 24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg></div>
      </div>
      <!-- Principles -->
      <div style="flex:1;min-width:500px;display:flex;flex-direction:column;gap:14px;max-width:680px">
        <div class="card anim" data-delay="400" style="padding:22px 24px;display:flex;gap:14px;align-items:center">
          <div style="width:44px;height:44px;border-radius:12px;background:rgba(163,245,199,.15);display:flex;align-items:center;justify-content:center;flex-shrink:0">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="var(--lime)" stroke-width="2" stroke-linecap="round"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 00-3-3.87"/><path d="M16 3.13a4 4 0 010 7.75"/></svg>
          </div>
          <div><h3 style="font-size:17px;margin:0">Customer Advisory Board</h3><p style="font-size:14px;margin-top:2px">8–10 enterprise customers, quarterly sessions. Structured input, not ad-hoc asks.</p></div>
        </div>
        <div class="card anim" data-delay="500" style="padding:22px 24px;display:flex;gap:14px;align-items:center">
          <div style="width:44px;height:44px;border-radius:12px;background:rgba(229,0,77,.12);display:flex;align-items:center;justify-content:center;flex-shrink:0">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="var(--pink)" stroke-width="2" stroke-linecap="round"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>
          </div>
          <div><h3 style="font-size:17px;margin:0">Shared Feedback Taxonomy</h3><p style="font-size:14px;margin-top:2px">Every request tagged: revenue at risk, frequency, segment, effort. No "CS said so" prioritisation.</p></div>
        </div>
        <div class="card anim" data-delay="600" style="padding:22px 24px;display:flex;gap:14px;align-items:center">
          <div style="width:44px;height:44px;border-radius:12px;background:rgba(0,207,186,.12);display:flex;align-items:center;justify-content:center;flex-shrink:0">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="var(--teal)" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
          </div>
          <div><h3 style="font-size:17px;margin:0">Monthly Roadmap Review</h3><p style="font-size:14px;margin-top:2px">Sales &amp; CS see what's coming, why, and what's been deprioritised — with the reasoning.</p></div>
        </div>
        <div class="card anim" data-delay="700" style="padding:22px 24px;display:flex;gap:14px;align-items:center">
          <div style="width:44px;height:44px;border-radius:12px;background:rgba(94,36,194,.15);display:flex;align-items:center;justify-content:center;flex-shrink:0">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="var(--purple-light)" stroke-width="2" stroke-linecap="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
          </div>
          <div><h3 style="font-size:17px;margin:0">"Say No" with Evidence</h3><p style="font-size:14px;margin-top:2px">Every declined request paired with data: segment fit, strategic alignment, opportunity cost.</p></div>
        </div>
      </div>
    </div>
  </div>
  {LOGO}
</section>
'''

# ── SLIDE 13: Metrics & Operating Cadence ─────────────
SLIDE_13 = f'''
<!-- ═══════════════════════════════════════════════════ -->
<!-- SLIDE 13 — Metrics & Operating Cadence             -->
<!-- ═══════════════════════════════════════════════════ -->
<section class="slide theme-light" data-slide="13">
  <div class="deco purple" style="width:500px;height:500px;bottom:-200px;right:-160px"></div>
  <div class="slide-inner">
    <div class="label-tag anim" data-delay="50">Measurement</div>
    <h2 class="slide-heading anim" data-delay="100">Six metrics that prove <span class="accent-purple">product value</span></h2>
    <div class="metric-row">
      <div class="metric-card anim" data-delay="300">
        <div class="metric-val" style="color:var(--purple)">NRR</div>
        <div class="metric-name">Net Revenue Retention</div>
        <div class="metric-desc">Target: 115%+. Expansion from data tiers &amp; AI upsell.</div>
        <div class="metric-mini" data-spark="300"><span style="height:0;background:var(--purple)"></span><span style="height:0;background:var(--purple-light)"></span><span style="height:0;background:var(--purple)"></span><span style="height:0;background:var(--purple-light)"></span><span style="height:0;background:var(--purple)"></span><span style="height:0;background:var(--purple-light)"></span><span style="height:0;background:var(--purple)"></span></div>
      </div>
      <div class="metric-card anim" data-delay="400">
        <div class="metric-val" style="color:var(--teal)">DAU/MAU</div>
        <div class="metric-name">Adoption Depth</div>
        <div class="metric-desc">Target: 40%+. Users returning daily means real value.</div>
        <div class="metric-mini" data-spark="400"><span style="height:0;background:var(--teal)"></span><span style="height:0;background:rgba(0,207,186,.5)"></span><span style="height:0;background:var(--teal)"></span><span style="height:0;background:rgba(0,207,186,.5)"></span><span style="height:0;background:var(--teal)"></span><span style="height:0;background:rgba(0,207,186,.5)"></span><span style="height:0;background:var(--teal)"></span></div>
      </div>
      <div class="metric-card anim" data-delay="500">
        <div class="metric-val" style="color:var(--pink)">TTV</div>
        <div class="metric-name">Time to Value</div>
        <div class="metric-desc">Target: &lt;14 days. From signup to first meaningful insight.</div>
        <div class="metric-mini" data-spark="500"><span style="height:0;background:var(--pink)"></span><span style="height:0;background:rgba(229,0,77,.4)"></span><span style="height:0;background:var(--pink)"></span><span style="height:0;background:rgba(229,0,77,.4)"></span><span style="height:0;background:var(--pink)"></span><span style="height:0;background:rgba(229,0,77,.4)"></span><span style="height:0;background:var(--pink)"></span></div>
      </div>
    </div>
    <div class="metric-row" style="margin-top:24px">
      <div class="metric-card anim" data-delay="600">
        <div class="metric-val" style="color:#1a9e5c">&lt;8%</div>
        <div class="metric-name">Logo Churn</div>
        <div class="metric-desc">Stickiness through embedded workflows + data dependency.</div>
        <div class="metric-mini" data-spark="600"><span style="height:0;background:#1a9e5c"></span><span style="height:0;background:var(--lime)"></span><span style="height:0;background:#1a9e5c"></span><span style="height:0;background:var(--lime)"></span><span style="height:0;background:#1a9e5c"></span><span style="height:0;background:var(--lime)"></span><span style="height:0;background:#1a9e5c"></span></div>
      </div>
      <div class="metric-card anim" data-delay="700">
        <div class="metric-val" style="color:var(--purple)">CTS</div>
        <div class="metric-name">Cost to Serve</div>
        <div class="metric-desc">Target: -20% YoY. Automation reduces manual support burden.</div>
        <div class="metric-mini" data-spark="700"><span style="height:0;background:var(--purple)"></span><span style="height:0;background:var(--purple-light)"></span><span style="height:0;background:var(--purple)"></span><span style="height:0;background:var(--purple-light)"></span><span style="height:0;background:var(--purple)"></span><span style="height:0;background:var(--purple-light)"></span><span style="height:0;background:var(--purple)"></span></div>
      </div>
      <div class="metric-card anim" data-delay="800">
        <div class="metric-val" style="color:var(--teal)">FVR</div>
        <div class="metric-name">Feature Value Ratio</div>
        <div class="metric-desc">% of shipped features with &gt;10% adoption after 30 days.</div>
        <div class="metric-mini" data-spark="800"><span style="height:0;background:var(--teal)"></span><span style="height:0;background:rgba(0,207,186,.5)"></span><span style="height:0;background:var(--teal)"></span><span style="height:0;background:rgba(0,207,186,.5)"></span><span style="height:0;background:var(--teal)"></span><span style="height:0;background:rgba(0,207,186,.5)"></span><span style="height:0;background:var(--teal)"></span></div>
      </div>
    </div>
    <div class="cadence-row" style="margin-top:48px">
      <div class="cadence-item anim" data-delay="900" data-lit="1200">
        <div class="cadence-dot" style="background:var(--purple);color:var(--purple)"></div>
        <h4>Daily</h4>
        <p>Team standup, incident triage, deploy review</p>
      </div>
      <div class="cadence-item anim" data-delay="950" data-lit="1400">
        <div class="cadence-dot" style="background:var(--teal);color:var(--teal)"></div>
        <h4>Weekly</h4>
        <p>Discovery sync, metric check-in, sprint planning</p>
      </div>
      <div class="cadence-item anim" data-delay="1000" data-lit="1600">
        <div class="cadence-dot" style="background:var(--pink);color:var(--pink)"></div>
        <h4>Bi-weekly</h4>
        <p>Sprint demo, stakeholder review, retrospective</p>
      </div>
      <div class="cadence-item anim" data-delay="1050" data-lit="1800">
        <div class="cadence-dot" style="background:var(--lime);color:var(--lime)"></div>
        <h4>Monthly</h4>
        <p>Roadmap review with Sales/CS, board metric pack</p>
      </div>
      <div class="cadence-item anim" data-delay="1100" data-lit="2000">
        <div class="cadence-dot" style="background:var(--purple-bright);color:var(--purple-bright)"></div>
        <h4>Quarterly</h4>
        <p>OKR reset, strategy review, advisory board session</p>
      </div>
    </div>
  </div>
  {LOGO}
</section>
'''

# ── SLIDE 14: PE Risks & Trade-offs ───────────────────
SLIDE_14 = f'''
<!-- ═══════════════════════════════════════════════════ -->
<!-- SLIDE 14 — PE Risks & Trade-offs                   -->
<!-- ═══════════════════════════════════════════════════ -->
<section class="slide theme-dark" data-slide="14">
  <div class="deco purple" style="width:500px;height:500px;top:-200px;left:-150px"></div>
  <div class="deco pink" style="width:250px;height:250px;bottom:-80px;right:-80px;opacity:.05"></div>
  <div class="particle" style="width:6px;height:6px;background:var(--purple-light);top:10%;right:25%;animation-delay:0s"></div>
  <div class="particle" style="width:4px;height:4px;background:var(--pink);top:70%;left:20%;animation-delay:3s"></div>
  <div class="slide-inner">
    <div class="label-tag anim" data-delay="50">PE Context</div>
    <h2 class="slide-heading anim" data-delay="100" style="color:#fff">Key risks &amp; trade-offs in a <span style="color:var(--pink)">fast PE cycle</span></h2>
    <div class="tradeoff-grid">
      <div class="tradeoff-card anim" data-delay="300">
        <div class="tf-marker" style="background:var(--purple-light)"></div>
        <div>
          <h4>Speed vs Quality</h4>
          <p>I bias toward shipping fast with feature flags. But never compromise on data integrity — for ECA, wrong data costs trust permanently.</p>
        </div>
      </div>
      <div class="tradeoff-card anim" data-delay="400">
        <div class="tf-marker" style="background:var(--pink)"></div>
        <div>
          <h4>Platform vs Bespoke</h4>
          <p>Every custom client build creates tech debt that slows the whole platform. I'll ring-fence 80%+ of engineering for scalable features.</p>
        </div>
      </div>
      <div class="tradeoff-card anim" data-delay="500">
        <div class="tf-marker" style="background:var(--teal)"></div>
        <div>
          <h4>Growth vs Margin</h4>
          <p>AI and data services improve both. Invest in self-serve and automation early to drive revenue while reducing cost-to-serve.</p>
        </div>
      </div>
      <div class="tradeoff-card anim" data-delay="600">
        <div class="tf-marker" style="background:var(--lime)"></div>
        <div>
          <h4>New vs Existing</h4>
          <p>NRR is the PE metric. I'll protect expansion revenue from existing accounts over net-new feature development in Year 1.</p>
        </div>
      </div>
      <div class="tradeoff-card anim" data-delay="700">
        <div class="tf-marker" style="background:var(--purple-bright)"></div>
        <div>
          <h4>Build vs Buy vs Partner</h4>
          <p>Build the intelligence layer — it's the moat. Buy/partner for commodity features (auth, notifications, integrations).</p>
        </div>
      </div>
      <div class="tradeoff-card anim" data-delay="800">
        <div class="tf-marker" style="background:rgba(255,180,0,.8)"></div>
        <div>
          <h4>Migration Risk</h4>
          <p>Moving from legacy to the new platform will cause friction. I'll run parallel for key accounts and migrate in cohorts, not a big bang.</p>
        </div>
      </div>
    </div>
    <p class="anim" data-delay="1000" style="text-align:center;margin-top:40px;font-size:22px;font-weight:600;color:#fff">Every trade-off is <span style="color:var(--purple-light)">documented, visible, and reversible</span>.</p>
  </div>
  {LOGO}
</section>
'''

# ═══════════════════════════════════════════════════════
# APPLY CHANGES
# ═══════════════════════════════════════════════════════

with open(DECK, "r") as f:
    html = f.read()

# 1. Insert CSS before </style>
css_anchor = "</style>\n</head>"
if css_anchor not in html:
    # Try alternate
    css_anchor = "</style>"
new_css_block = NEW_CSS + "\n</style>"
html = html.replace(css_anchor, new_css_block, 1)

# 2. Insert 7 slides between slide 7 and slide 8
slide_anchor = "<!-- SLIDE 8 \xe2\x80\x94 Customer Value"
if slide_anchor not in html:
    # Try alternate
    slide_anchor = "<!-- SLIDE 8"
    
all_new_slides = SLIDE_8 + SLIDE_9 + SLIDE_10 + SLIDE_11 + SLIDE_12 + SLIDE_13 + SLIDE_14

# Find the exact marker
idx = html.index(slide_anchor)
# Find the <!-- ═══ line before it
line_start = html.rfind("<!-- ═══", 0, idx)
insert_point = line_start

html = html[:insert_point] + all_new_slides + "\n" + html[insert_point:]

# 3. Renumber old slides 8→15, 9→16, 10→17, 11→18
# We need to be careful to only change the ones AFTER our insertions
# Find position after our new slides to only modify the old ones
renumber_map = {
    'data-slide="8"': 'data-slide="15"',
    'data-slide="9"': 'data-slide="16"',
    'data-slide="10"': 'data-slide="17"',
    'data-slide="11"': 'data-slide="18"',
    '<!-- SLIDE 8 \u2014 Customer Value': '<!-- SLIDE 15 \u2014 Customer Value',
    '<!-- SLIDE 9 \u2014 Commercial Impact': '<!-- SLIDE 16 \u2014 Commercial Impact',
    '<!-- SLIDE 10 \u2014 Product Leadership': '<!-- SLIDE 17 \u2014 Product Leadership',
    '<!-- SLIDE 11 \u2014 The Goal': '<!-- SLIDE 18 \u2014 The Goal',
}

# Find where the old slide 8 starts (after our new slides)
# Look for "Customer Value" data-slide="8" after the new content
for old, new in renumber_map.items():
    # Only replace the last occurrence (the old slides)
    # Actually, since our new slides use 8-14 already, the old ones are the second occurrence of 8
    # But safer: replace from the end
    # The old data-slide="8" is the SECOND occurrence now
    pass

# More precise approach: find each old slide by its unique comment+data combo
# Since we have unique comments, let's do targeted replacements
old_slide_markers = [
    ('<!-- SLIDE 8 \u2014 Customer Value', 'data-slide="8"', '<!-- SLIDE 15 \u2014 Customer Value', 'data-slide="15"'),
    ('<!-- SLIDE 9 \u2014 Commercial Impact', 'data-slide="9"', '<!-- SLIDE 16 \u2014 Commercial Impact', 'data-slide="16"'),
    ('<!-- SLIDE 10 \u2014 Product Leadership', 'data-slide="10"', '<!-- SLIDE 17 \u2014 Product Leadership', 'data-slide="17"'),
    ('<!-- SLIDE 11 \u2014 The Goal', 'data-slide="11"', '<!-- SLIDE 18 \u2014 The Goal', 'data-slide="18"'),
]

for comment_old, ds_old, comment_new, ds_new in old_slide_markers:
    # Find the comment
    pos = html.rfind(comment_old)  # rfind = last occurrence
    if pos == -1:
        print(f"WARNING: Could not find '{comment_old}'")
        continue
    # Replace the comment
    html = html[:pos] + html[pos:].replace(comment_old, comment_new, 1)
    # Now find and replace the data-slide near this position
    # Find the next data-slide="N" after this position
    pos2 = html.find(ds_old, pos)
    if pos2 != -1 and pos2 < pos + 500:  # sanity check — should be nearby
        html = html[:pos2] + html[pos2:].replace(ds_old, ds_new, 1)
    else:
        print(f"WARNING: Could not find '{ds_old}' near position {pos}")

# 4. Add cadence-item lit animation to the JS animateSlide function
# Insert after the "Timeline lit" section
cadence_js = """
    // Cadence dots
    slide.querySelectorAll('.cadence-item[data-lit]').forEach(ci=>{
      setTimeout(()=>ci.classList.add('lit'),parseInt(ci.dataset.lit,10));
    });

    // ICP rings
    slide.querySelectorAll('.icp-ring').forEach((r,i)=>{
      setTimeout(()=>r.classList.add('visible'),400+i*250);
    });

    // Metric mini sparklines
    slide.querySelectorAll('.metric-mini[data-spark]').forEach(sl=>{
      const d=parseInt(sl.dataset.spark||0,10);
      sl.querySelectorAll('span').forEach((sp,j)=>{
        const h=12+Math.floor(Math.random()*24);
        sp.style.height='0';sp.style.transition='none';
        setTimeout(()=>{sp.style.transition='height .5s var(--ease)';sp.style.height=h+'px'},d+200+j*60);
      });
    });"""

# Find the right place in JS to insert
js_anchor = "    // Bubbles"
html = html.replace(js_anchor, cadence_js + "\n\n    // Bubbles", 1)

# Also need to reset new elements in the reset section
reset_anchor = "slide.querySelectorAll('.lit').forEach(el=>el.classList.remove('lit'));"
html = html.replace(reset_anchor, 
    reset_anchor + "\n    slide.querySelectorAll('.icp-ring').forEach(r=>r.classList.remove('visible'));",
    1)

with open(DECK, "w") as f:
    f.write(html)

# Verify
with open(DECK, "r") as f:
    content = f.read()

slide_count = content.count('class="slide ')
print(f"✅ Done. Total slides: {slide_count}")
print(f"   File length: {len(content.splitlines())} lines")

# Verify all new slides present
for i in range(8, 15):
    marker = f'data-slide="{i}"'
    if marker in content:
        print(f"   ✓ Slide {i} present")
    else:
        print(f"   ✗ Slide {i} MISSING")
for i in range(15, 19):
    marker = f'data-slide="{i}"'
    if marker in content:
        print(f"   ✓ Old slide renumbered to {i}")
    else:
        print(f"   ✗ Renumbered slide {i} MISSING")
