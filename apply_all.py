#!/usr/bin/env python3
"""Comprehensive deck update: Lucide icons, plane icon, slide 1 overhaul, perpetual animations."""
import re

html_path = 'deck.html'

with open(html_path, 'r') as f:
    html = f.read()

# ─── 1. Fix duplicate dot comment ───────────────────────────────────────────
html = html.replace(
    '<!-- Dot-grid world map (2989 dots) -->\n<!-- Dot-grid world map (2989 dots) -->',
    '<!-- Dot-grid world map (2989 dots) -->'
)

# ─── 2. Replace plane icon in SVG defs with Lucide-inspired plane ────────
old_plane = '''        <g id="plane-icon">
          <path d="M-6,0 L-2,-2 L6,0 L-2,2 Z" fill="#fff"/>
          <path d="M-1,-4 L1,-4 L1,-1 L-1,-1 Z" fill="#fff" opacity=".7"/>
          <path d="M-1,1 L1,1 L1,4 L-1,4 Z" fill="#fff" opacity=".7"/>
        </g>'''
new_plane = '''        <g id="plane-icon">
          <g transform="translate(-10,-10) scale(0.85)">
            <path d="M17.8 19.2 16 11l3.5-3.5C21 6 21.5 4 21 3c-1-.5-3 0-4.5 1.5L13 8 4.8 6.2c-.5-.1-.9.1-1.1.5l-.3.5c-.2.4-.1.9.3 1.1L10.1 12l-3.6 3.5-2.8-.7c-.3-.1-.7 0-.9.3l2.8 2.1 2.1 2.8c.3.3.7.1.9-.3l-.7-2.8L13.2 14l2.3 6.4c.2.4.7.5 1.1.3l.5-.3c.4-.2.6-.6.5-1.1z" fill="#fff" stroke="rgba(255,255,255,.5)" stroke-width=".5"/>
          </g>
        </g>'''
html = html.replace(old_plane, new_plane)

# ─── 3. Add Lucide CDN before the <script> block ────────────────────
html = html.replace(
    '<script>\n(function(){',
    '<script src="https://unpkg.com/lucide@latest"></script>\n<script>\n(function(){'
)

# ─── 4. Add lucide.createIcons() call at start of IIFE ──────────────────
html = html.replace(
    "const slides=document.querySelectorAll('.slide'),total=slides.length;",
    "const slides=document.querySelectorAll('.slide'),total=slides.length;\n  lucide.createIcons();"
)

# ─── 5. Replace inline SVG icons with Lucide data-lucide throughout ──────

# Slide 4 icons (lines ~913-928)
html = html.replace(
    '<div class="icon purple-bg"><svg viewBox="0 0 24 24"><path d="M9 12l2 2 4-4"/><path d="M12 22c5.523 0 10-4.477 10-10S17.523 2 12 2 2 6.477 2 12s4.477 10 10 10z"/></svg></div>',
    '<div class="icon purple-bg"><i data-lucide="circle-check-big"></i></div>'
)
html = html.replace(
    '<div class="icon purple-bg"><svg viewBox="0 0 24 24"><path d="M20 21v-2a4 4 0 00-4-4H8a4 4 0 00-4 4v2"/><circle cx="12" cy="7" r="4"/></svg></div>',
    '<div class="icon purple-bg"><i data-lucide="user"></i></div>'
)
html = html.replace(
    '<div class="icon purple-bg"><svg viewBox="0 0 24 24"><line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 000 7h5a3.5 3.5 0 010 7H6"/></svg></div>',
    '<div class="icon purple-bg"><i data-lucide="dollar-sign"></i></div>'
)
# Globe icons (multiple)
html = html.replace(
    '<div class="icon purple-bg"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 014 10 15.3 15.3 0 01-4 10 15.3 15.3 0 01-4-10A15.3 15.3 0 0112 2z"/></svg></div>',
    '<div class="icon purple-bg"><i data-lucide="globe"></i></div>'
)

# Slide 3 icons (lines ~954-969)
html = html.replace(
    '<div class="icon purple-bg"><svg viewBox="0 0 24 24"><path d="M22 11.08V12a10 10 0 11-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg></div>',
    '<div class="icon purple-bg"><i data-lucide="circle-check"></i></div>'
)
html = html.replace(
    '<div class="icon pink-bg"><svg viewBox="0 0 24 24"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0110 0v4"/></svg></div>',
    '<div class="icon pink-bg"><i data-lucide="lock"></i></div>'
)
html = html.replace(
    '<div class="icon teal-bg"><svg viewBox="0 0 24 24"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg></div>',
    '<div class="icon teal-bg"><i data-lucide="eye"></i></div>'
)
html = html.replace(
    '<div class="icon lime-bg"><svg viewBox="0 0 24 24"><polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/><polyline points="17 6 23 6 23 12"/></svg></div>',
    '<div class="icon lime-bg"><i data-lucide="trending-up"></i></div>'
)

# Slide 5 icons (lines ~989-997)
html = html.replace(
    '<div class="icon purple-bg" style="flex-shrink:0"><svg viewBox="0 0 24 24"><path d="M21 16V8a2 2 0 00-1-1.73l-7-4a2 2 0 00-2 0l-7 4A2 2 0 003 8v8a2 2 0 001 1.73l7 4a2 2 0 002 0l7-4A2 2 0 0021 16z"/><polyline points="3.27 6.96 12 12.01 20.73 6.96"/><line x1="12" y1="22.08" x2="12" y2="12"/></svg></div>',
    '<div class="icon purple-bg" style="flex-shrink:0"><i data-lucide="box"></i></div>'
)
html = html.replace(
    '<div class="icon pink-bg" style="flex-shrink:0"><svg viewBox="0 0 24 24"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 00-3-3.87"/><path d="M16 3.13a4 4 0 010 7.75"/></svg></div>',
    '<div class="icon pink-bg" style="flex-shrink:0"><i data-lucide="users"></i></div>'
)
html = html.replace(
    '<div class="icon teal-bg" style="flex-shrink:0"><svg viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg></div>',
    '<div class="icon teal-bg" style="flex-shrink:0"><i data-lucide="star"></i></div>'
)

# Sparkline slide icons (lines ~1052-1067)
html = html.replace(
    '<div class="icon pink-bg" style="margin:0 auto 20px;width:72px;height:72px;border-radius:50%"><svg viewBox="0 0 24 24"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z"/><circle cx="12" cy="10" r="3"/></svg></div>',
    '<div class="icon pink-bg" style="margin:0 auto 20px;width:72px;height:72px;border-radius:50%"><i data-lucide="map-pin"></i></div>'
)
html = html.replace(
    '<div class="icon teal-bg" style="margin:0 auto 20px;width:72px;height:72px;border-radius:50%"><svg viewBox="0 0 24 24"><line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 000 7h5a3.5 3.5 0 010 7H6"/></svg></div>',
    '<div class="icon teal-bg" style="margin:0 auto 20px;width:72px;height:72px;border-radius:50%"><i data-lucide="dollar-sign"></i></div>'
)
html = html.replace(
    '<div class="icon purple-bg" style="margin:0 auto 20px;width:72px;height:72px;border-radius:50%"><svg viewBox="0 0 24 24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg></div>',
    '<div class="icon purple-bg" style="margin:0 auto 20px;width:72px;height:72px;border-radius:50%"><i data-lucide="shield"></i></div>'
)
html = html.replace(
    '<div class="icon lime-bg" style="margin:0 auto 20px;width:72px;height:72px;border-radius:50%"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 014 10 15.3 15.3 0 01-4 10 15.3 15.3 0 01-4-10A15.3 15.3 0 0112 2z"/></svg></div>',
    '<div class="icon lime-bg" style="margin:0 auto 20px;width:72px;height:72px;border-radius:50%"><i data-lucide="globe"></i></div>'
)

# Pillars slide icons (lines ~1346-1364)
html = html.replace(
    '<div class="icon purple-bg"><svg viewBox="0 0 24 24"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg></div>',
    '<div class="icon purple-bg"><i data-lucide="zap"></i></div>'
)
html = html.replace(
    '<div class="icon pink-bg"><svg viewBox="0 0 24 24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg></div>',
    '<div class="icon pink-bg"><i data-lucide="shield"></i></div>'
)
html = html.replace(
    '<div class="icon teal-bg"><svg viewBox="0 0 24 24"><line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 000 7h5a3.5 3.5 0 010 7H6"/></svg></div>',
    '<div class="icon teal-bg"><i data-lucide="dollar-sign"></i></div>'
)
html = html.replace(
    '<div class="icon lime-bg"><svg viewBox="0 0 24 24"><path d="M20.84 4.61a5.5 5.5 0 00-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 00-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 000-7.78z"/></svg></div>',
    '<div class="icon lime-bg"><i data-lucide="heart"></i></div>'
)

# Nav buttons
html = html.replace(
    '<button id="prevBtn" aria-label="Previous slide"><svg viewBox="0 0 24 24"><polyline points="15 18 9 12 15 6"/></svg></button>',
    '<button id="prevBtn" aria-label="Previous slide"><i data-lucide="chevron-left"></i></button>'
)
html = html.replace(
    '<button id="nextBtn" aria-label="Next slide"><svg viewBox="0 0 24 24"><polyline points="9 18 15 12 9 6"/></svg></button>',
    '<button id="nextBtn" aria-label="Next slide"><i data-lucide="chevron-right"></i></button>'
)
html = html.replace(
    '<button id="fsBtn" class="fs-btn" aria-label="Fullscreen" title="Present (F5)"><svg viewBox="0 0 24 24"><polyline points="15 3 21 3 21 9"/><polyline points="9 21 3 21 3 15"/><line x1="21" y1="3" x2="14" y2="10"/><line x1="3" y1="21" x2="10" y2="14"/></svg></button>',
    '<button id="fsBtn" class="fs-btn" aria-label="Fullscreen" title="Present (F5)"><i data-lucide="maximize"></i></button>'
)

# ─── 6. NEW CSS for perpetual slide 1 animations ────────────────────────
new_css = '''
/* ── Slide-1 perpetual animated dashboard ──────────── */
.hero-dash{position:absolute;inset:0;pointer-events:none;z-index:5}
.hero-dash .ui-card{
  position:absolute;
  background:rgba(29,37,45,.72);backdrop-filter:blur(18px);
  border:1px solid rgba(212,186,250,.15);border-radius:16px;
  padding:14px 18px;color:#fff;font-size:12px;
  box-shadow:0 8px 32px rgba(0,0,0,.25);
  transition:opacity .6s,transform .6s;opacity:0;transform:translateY(16px);
}
.hero-dash .ui-card.visible{opacity:1;transform:translateY(0)}
.hero-dash .ui-card .card-label{font-size:10px;text-transform:uppercase;letter-spacing:.08em;color:rgba(255,255,255,.45);margin-bottom:4px}
.hero-dash .ui-card .card-value{font-size:22px;font-weight:800;line-height:1.1}
.hero-dash .ui-card .card-sub{font-size:10px;color:rgba(255,255,255,.4);margin-top:3px}

/* Mini bar chart animation */
.mini-bars{display:flex;gap:3px;align-items:flex-end;height:32px}
.mini-bars span{display:block;width:5px;border-radius:2px;transition:height .5s cubic-bezier(.4,0,.2,1)}

/* Perpetual donut */
.mini-donut{width:44px;height:44px;border-radius:50%;position:relative}
.mini-donut svg{width:44px;height:44px;transform:rotate(-90deg)}
.mini-donut circle{fill:none;stroke-width:5}
.mini-donut .donut-track{stroke:rgba(212,186,250,.15)}
.mini-donut .donut-fill{stroke:var(--teal);stroke-linecap:round;transition:stroke-dashoffset .8s ease}

/* Notification toast cycle */
.toast-cycle{
  position:absolute;padding:10px 14px;border-radius:12px;
  background:rgba(94,36,194,.35);border:1px solid rgba(212,186,250,.2);
  backdrop-filter:blur(12px);
  font-size:11px;color:rgba(255,255,255,.8);
  display:flex;align-items:center;gap:8px;
  opacity:0;transform:translateX(20px);
  transition:all .4s cubic-bezier(.4,0,.2,1);
}
.toast-cycle.show{opacity:1;transform:translateX(0)}
.toast-cycle .toast-dot{width:8px;height:8px;border-radius:50%;flex-shrink:0}

/* Live pulse indicator */
.live-pulse{display:inline-flex;align-items:center;gap:6px;font-size:11px;color:rgba(255,255,255,.5)}
.live-pulse::before{content:'';width:7px;height:7px;border-radius:50%;background:var(--lime);animation:liveBlink 2s ease infinite}
@keyframes liveBlink{0%,100%{opacity:1}50%{opacity:.3}}

/* Mini sparkline animation */
.mini-spark{display:flex;gap:2px;align-items:flex-end;height:24px}
.mini-spark span{display:block;width:3px;border-radius:1px;background:var(--purple-light)}

/* Float animation variants */
@keyframes floatSlow{0%,100%{transform:translateY(0)}50%{transform:translateY(-8px)}}
@keyframes floatMed{0%,100%{transform:translateY(0)}50%{transform:translateY(-12px)}}
@keyframes floatFast{0%,100%{transform:translateY(0)}50%{transform:translateY(-6px)}}
.float-s{animation:floatSlow 5s ease-in-out infinite}
.float-m{animation:floatMed 4s ease-in-out infinite}
.float-f{animation:floatFast 3.2s ease-in-out infinite}

/* Lucide icon sizing inside .icon */
.card .icon i[data-lucide],.card .icon svg[data-lucide]{width:32px;height:32px}
.icon i[data-lucide],.icon svg[class^="lucide"]{width:32px;height:32px}
#prevBtn i,#prevBtn svg.lucide,#nextBtn i,#nextBtn svg.lucide{width:28px;height:28px}
#fsBtn i,#fsBtn svg.lucide{width:20px;height:20px}
'''

# Insert before closing </style>
html = html.replace('</style>', new_css + '</style>')

# ─── 7. Replace entire Slide 1 HTML ─────────────────────────────────────
# Find old slide 1
old_slide1_start = '<!-- ═══════════════════════════════════════════════════ -->\n<section class="slide theme-dark active" data-slide="1">'
old_slide1_end = '</section>\n\n<!-- ═══════════════════════════════════════════════════ -->\n<!-- SLIDE 2'

slide1_start_pos = html.find(old_slide1_start)
slide1_end_pos = html.find(old_slide1_end)

if slide1_start_pos == -1 or slide1_end_pos == -1:
    print("ERROR: Could not find slide 1 boundaries!")
    print(f"  start: {slide1_start_pos}, end: {slide1_end_pos}")
    exit(1)

new_slide1 = '''<!-- ═══════════════════════════════════════════════════ -->
<section class="slide theme-dark active" data-slide="1">
  <!-- Particles -->
  <div class="particle" style="width:6px;height:6px;background:var(--purple-light);top:15%;left:10%;animation-delay:0s"></div>
  <div class="particle" style="width:4px;height:4px;background:var(--pink);top:70%;left:25%;animation-delay:3s"></div>
  <div class="particle" style="width:5px;height:5px;background:var(--lime);top:30%;left:40%;animation-delay:7s"></div>
  <div class="particle" style="width:3px;height:3px;background:var(--purple-light);top:80%;left:5%;animation-delay:5s"></div>
  <div class="particle" style="width:4px;height:4px;background:var(--teal);top:50%;left:15%;animation-delay:10s"></div>
  <div class="particle" style="width:3px;height:3px;background:var(--pink);top:20%;left:55%;animation-delay:2s"></div>
  <div class="particle" style="width:5px;height:5px;background:var(--purple-light);top:85%;left:70%;animation-delay:8s"></div>

  <div class="deco purple" style="width:500px;height:500px;top:-200px;left:-150px"></div>
  <div class="deco pink" style="width:200px;height:200px;bottom:60px;left:100px"></div>

  <div class="slide-split">
    <div class="slide-left">
      <div class="label-tag anim" data-delay="100">Product Director Discussion</div>
      <h1 class="hero-title anim" data-delay="300" style="color:#fff;max-width:680px">Shaping the Future of <span class="accent-purple">Global Mobility Platforms</span></h1>
      <p class="sub-line anim" data-delay="600" style="max-width:560px">A product vision for turning ECA&#8217;s world-class data into the intelligence platform that global organisations need.</p>
      <p class="anim" data-delay="900" style="margin-top:48px;font-size:22px;font-weight:700;letter-spacing:.03em;color:var(--purple-light)">Damon Macklin</p>
    </div>
    <div class="slide-right" style="position:relative">
      <!-- Bleeding circle image -->
      <div class="hero-circle-wrap anim scale-in" data-delay="200">
        <img src="https://cdn.builder.io/api/v1/image/assets%2Faaf105599c0b4853bf4544d312efc583%2F80f93a047d584c9f98e79c7971864b83" alt="Global mobility"/>
      </div>

      <!-- ═══ HERO DASHBOARD — Perpetually animated UI cards ═══ -->
      <div class="hero-dash" id="heroDash">

        <!-- Card 1: Active Assignments (fluctuating counter) -->
        <div class="ui-card float-s anim from-right" data-delay="700" style="top:55px;left:20px;z-index:6">
          <div style="display:flex;align-items:center;gap:10px">
            <div style="width:36px;height:36px;border-radius:10px;background:rgba(94,36,194,.2);display:flex;align-items:center;justify-content:center">
              <i data-lucide="globe" style="width:18px;height:18px;color:var(--purple-light)"></i>
            </div>
            <div>
              <div class="card-label">Active Assignments</div>
              <div class="card-value" id="heroAssignments" style="color:var(--purple-light)">2,847</div>
            </div>
          </div>
        </div>

        <!-- Card 2: Compliance Score (animated donut) -->
        <div class="ui-card float-m anim from-right" data-delay="900" style="bottom:180px;left:-10px;z-index:6">
          <div style="display:flex;align-items:center;gap:10px">
            <div class="mini-donut">
              <svg viewBox="0 0 44 44">
                <circle class="donut-track" cx="22" cy="22" r="17"/>
                <circle class="donut-fill" id="heroDonut" cx="22" cy="22" r="17"
                  stroke-dasharray="106.8" stroke-dashoffset="6.4"/>
              </svg>
            </div>
            <div>
              <div class="card-label">Compliance Score</div>
              <div class="card-value" style="color:var(--lime)"><span id="heroCompliance">94.2</span>%</div>
            </div>
          </div>
        </div>

        <!-- Card 3: Cost Index chart (looping bar animation) -->
        <div class="ui-card float-f anim from-right" data-delay="1100" style="top:230px;right:20px;z-index:6">
          <div class="card-label">Cost Index — London &rarr; Singapore</div>
          <div class="mini-bars" id="heroBars">
            <span style="height:12px;background:var(--purple-light)"></span>
            <span style="height:20px;background:var(--purple)"></span>
            <span style="height:16px;background:var(--purple-light)"></span>
            <span style="height:28px;background:var(--pink)"></span>
            <span style="height:22px;background:var(--purple)"></span>
            <span style="height:18px;background:var(--purple-light)"></span>
            <span style="height:24px;background:var(--purple)"></span>
            <span style="height:15px;background:var(--teal)"></span>
            <span style="height:26px;background:var(--pink)"></span>
          </div>
        </div>

        <!-- Card 4: Revenue ticker (cycling numbers) -->
        <div class="ui-card float-m anim from-right" data-delay="1300" style="top:410px;right:50px;z-index:6">
          <div style="display:flex;align-items:center;gap:10px">
            <div style="width:36px;height:36px;border-radius:10px;background:rgba(229,0,77,.15);display:flex;align-items:center;justify-content:center">
              <i data-lucide="trending-up" style="width:18px;height:18px;color:var(--pink)"></i>
            </div>
            <div>
              <div class="card-label">Platform Revenue</div>
              <div class="card-value" style="color:var(--pink)">&pound;<span id="heroRevenue">14.2</span>M</div>
              <div class="card-sub">&uarr; 12.6% YoY</div>
            </div>
          </div>
        </div>

        <!-- Card 5: Countries served (incrementing) -->
        <div class="ui-card float-s anim from-right" data-delay="1500" style="bottom:70px;left:100px;z-index:6">
          <div style="display:flex;align-items:center;gap:10px">
            <div style="width:36px;height:36px;border-radius:10px;background:rgba(0,207,186,.15);display:flex;align-items:center;justify-content:center">
              <i data-lucide="map-pin" style="width:18px;height:18px;color:var(--teal)"></i>
            </div>
            <div>
              <div class="card-label">Countries Covered</div>
              <div class="card-value" style="color:var(--teal)"><span id="heroCountries">214</span></div>
            </div>
          </div>
        </div>

        <!-- Card 6: Mini sparkline (live data feel) -->
        <div class="ui-card float-f anim from-right" data-delay="1700" style="top:120px;right:-30px;z-index:6">
          <div class="card-label">Assignment Volume (7d)</div>
          <div class="mini-spark" id="heroSpark">
            <span style="height:12px"></span><span style="height:18px"></span>
            <span style="height:10px"></span><span style="height:22px"></span>
            <span style="height:16px"></span><span style="height:24px"></span>
            <span style="height:14px"></span><span style="height:20px"></span>
            <span style="height:18px"></span><span style="height:22px"></span>
            <span style="height:12px"></span><span style="height:16px"></span>
          </div>
        </div>

        <!-- Card 7: Active users online -->
        <div class="ui-card float-m anim from-right" data-delay="1900" style="bottom:280px;right:-20px;z-index:6">
          <div style="display:flex;align-items:center;gap:8px">
            <div style="width:28px;height:28px;border-radius:8px;background:rgba(163,245,199,.12);display:flex;align-items:center;justify-content:center">
              <i data-lucide="users" style="width:14px;height:14px;color:var(--lime)"></i>
            </div>
            <div>
              <div class="card-label">Users Online</div>
              <div class="card-value" style="font-size:18px;color:var(--lime)"><span id="heroOnline">1,284</span></div>
            </div>
          </div>
        </div>

        <!-- Card 8: Notification toast (cycling messages) -->
        <div class="toast-cycle anim from-right" data-delay="2200" id="heroToast" style="bottom:20px;right:30px;z-index:7">
          <div class="toast-dot" style="background:var(--lime)"></div>
          <span id="heroToastMsg">New assignment: Tokyo &rarr; London</span>
        </div>

        <!-- Live indicator -->
        <div class="anim" data-delay="2400" style="position:absolute;top:20px;right:10px;z-index:6">
          <div class="live-pulse">LIVE DATA</div>
        </div>

      </div><!-- /hero-dash -->
    </div>
  </div>
  <div class="slide-logo"><svg width="80" height="31" viewBox="0 0 80 31" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M64.375 24.18C59.55 24.18 55.625 20.2864 55.625 15.5C55.625 10.7136 59.55 6.82 64.375 6.82C69.2 6.82 73.125 10.7136 73.125 15.5C73.125 20.2864 69.2 24.18 64.375 24.18ZM7.39375 12.555C8.6125 9.2132 11.8417 6.82 15.625 6.82C16.7542 6.82 17.8312 7.03493 18.8229 7.42347C21.1542 8.33487 23 10.2114 23.8563 12.555H7.39375ZM80 0.628267H74.8104L73.1417 2.66807C71.8146 1.77527 70.3438 1.0788 68.7687 0.622067C67.375 0.217 65.9021 0 64.375 0C62.8479 0 61.375 0.217 59.9833 0.622067C56.875 1.52313 54.1667 3.35833 52.1896 5.80113C50.0396 8.4568 48.7521 11.8296 48.7521 15.5C48.7521 20.2864 44.8271 24.18 40.0021 24.18C35.1771 24.18 31.2521 20.2864 31.2521 15.5C31.2521 10.7136 35.1771 6.82 40.0021 6.82C42.0917 6.82 44.0125 7.5516 45.5187 8.76887L49.8583 3.47407C48.2667 2.1886 46.4167 1.209 44.3937 0.622067C43 0.217 41.5271 0 40.0021 0C38.4771 0 37.0021 0.217 35.6104 0.622067C32.5 1.52313 29.7938 3.35833 27.8167 5.80113C25.8396 3.35833 23.1312 1.52313 20.0208 0.622067C19.6292 0.5084 19.2313 0.4092 18.8271 0.326533C17.7938 0.113667 16.725 0.00206667 15.6292 0.00206667C14.1042 0.00206667 12.6292 0.219067 11.2375 0.624133C4.74167 2.5048 0 8.45267 0 15.5C0 22.5473 4.78333 28.5469 11.3167 30.4027C12.6854 30.7913 14.1292 31 15.625 31C16.7208 31 17.7896 30.8884 18.8229 30.6755C19.1979 30.597 19.5687 30.5081 19.9312 30.4048C21.9812 29.822 23.8583 28.8362 25.4688 27.5363L21.1333 22.2373C20.4417 22.7953 19.6625 23.25 18.8208 23.5786C17.8292 23.9671 16.7521 24.1821 15.6229 24.1821C11.8396 24.1821 8.61042 21.7889 7.39167 18.4471H24.6542C25.1437 20.9705 26.2479 23.2748 27.8083 25.2009C27.8083 25.203 27.8125 25.2051 27.8146 25.2071C29.8104 27.6685 32.5458 29.512 35.6896 30.4048C37.0583 30.7933 38.5021 31.0021 39.9979 31.0021C41.4938 31.0021 42.9375 30.7933 44.3062 30.4048C47.4521 29.512 50.1896 27.6644 52.1854 25.2009C54.1813 27.6665 56.9208 29.512 60.0646 30.4048C61.4333 30.7933 62.8771 31.0021 64.3729 31.0021C65.8687 31.0021 67.3125 30.7933 68.6813 30.4048C70.2812 29.9501 71.7771 29.2495 73.1229 28.3443L74.8083 30.4048H79.9979V15.7521V0.628267H80Z" fill="#E5004D"/></svg></div>
'''

html = html[:slide1_start_pos] + new_slide1 + '</section>\n\n<!-- ═══════════════════════════════════════════════════ -->\n<!-- SLIDE 2' + html[slide1_end_pos + len(old_slide1_end):]

# ─── 8. Add perpetual animation JS before closing IIFE ───────────────────
perpetual_js = '''
  // ═══ SLIDE 1 PERPETUAL ANIMATIONS ═══
  let heroTimers=[];
  function startHeroAnimations(){
    stopHeroAnimations();

    // Fluctuating assignments counter
    const assignEl=document.getElementById('heroAssignments');
    let assignVal=2847;
    heroTimers.push(setInterval(()=>{
      assignVal+=Math.floor(Math.random()*7)-3;
      assignVal=Math.max(2820,Math.min(2870,assignVal));
      if(assignEl)assignEl.textContent=assignVal.toLocaleString();
    },1200));

    // Fluctuating compliance
    const compEl=document.getElementById('heroCompliance');
    let compVal=94.2;
    heroTimers.push(setInterval(()=>{
      compVal+=(Math.random()-.5)*.4;
      compVal=Math.max(92.5,Math.min(96.8,compVal));
      if(compEl)compEl.textContent=compVal.toFixed(1);
      // Update donut
      const donut=document.getElementById('heroDonut');
      if(donut){const circ=2*Math.PI*17;donut.setAttribute('stroke-dashoffset',(circ*(1-compVal/100)).toFixed(1))}
    },1800));

    // Looping bar chart
    const bars=document.querySelectorAll('#heroBars span');
    heroTimers.push(setInterval(()=>{
      bars.forEach(b=>{
        const h=8+Math.floor(Math.random()*24);
        b.style.height=h+'px';
      });
    },1500));

    // Revenue ticker
    const revEl=document.getElementById('heroRevenue');
    let revVal=14.2;
    heroTimers.push(setInterval(()=>{
      revVal+=(Math.random()-.4)*.15;
      revVal=Math.max(13.8,Math.min(15.1,revVal));
      if(revEl)revEl.textContent=revVal.toFixed(1);
    },2200));

    // Countries incrementing
    const countEl=document.getElementById('heroCountries');
    let countVal=214;
    heroTimers.push(setInterval(()=>{
      if(Math.random()>.6){countVal++;if(countVal>220)countVal=214}
      if(countEl)countEl.textContent=countVal;
    },3000));

    // Online users fluctuating
    const onlineEl=document.getElementById('heroOnline');
    let onlineVal=1284;
    heroTimers.push(setInterval(()=>{
      onlineVal+=Math.floor(Math.random()*21)-10;
      onlineVal=Math.max(1200,Math.min(1400,onlineVal));
      if(onlineEl)onlineEl.textContent=onlineVal.toLocaleString();
    },1400));

    // Mini sparkline looping
    const sparkBars=document.querySelectorAll('#heroSpark span');
    heroTimers.push(setInterval(()=>{
      sparkBars.forEach(b=>{
        const h=6+Math.floor(Math.random()*20);
        b.style.height=h+'px';
      });
    },800));

    // Toast notifications cycling
    const toastMsgs=[
      {msg:'New assignment: Tokyo \\u2192 London',color:'var(--lime)'},
      {msg:'Compliance alert: Singapore updated',color:'var(--pink)'},
      {msg:'Cost report generated \\u2014 Q4 2024',color:'var(--purple-light)'},
      {msg:'3 policies expiring this week',color:'var(--pink)'},
      {msg:'New user: Sarah Chen joined',color:'var(--teal)'},
      {msg:'Data sync complete \\u2014 214 countries',color:'var(--lime)'},
      {msg:'Tax threshold update: UAE',color:'var(--purple-light)'},
      {msg:'Assignment complete: Dubai \\u2192 NYC',color:'var(--teal)'},
    ];
    let toastIdx=0;
    const toastEl=document.getElementById('heroToast');
    const toastMsg=document.getElementById('heroToastMsg');
    const toastDot=toastEl?toastEl.querySelector('.toast-dot'):null;
    function cycleToast(){
      if(!toastEl)return;
      toastEl.classList.remove('show');
      setTimeout(()=>{
        const t=toastMsgs[toastIdx%toastMsgs.length];
        if(toastMsg)toastMsg.textContent=t.msg;
        if(toastDot)toastDot.style.background=t.color;
        toastEl.classList.add('show');
        toastIdx++;
      },400);
    }
    // Initial show
    setTimeout(()=>{if(toastEl)toastEl.classList.add('show')},2400);
    heroTimers.push(setInterval(cycleToast,3500));
  }

  function stopHeroAnimations(){
    heroTimers.forEach(t=>clearInterval(t));
    heroTimers=[];
  }

'''

# Insert before the goTo function
html = html.replace(
    "  function goTo(index){",
    perpetual_js + "  function goTo(index){"
)

# Modify goTo to start/stop hero animations
html = html.replace(
    "    updateUI();\n    animateSlide(slides[current]);\n  }",
    "    updateUI();\n    animateSlide(slides[current]);\n    if(current===0){setTimeout(startHeroAnimations,2000)}else{stopHeroAnimations()}\n  }"
)

# Start hero animations on initial load
html = html.replace(
    "  setTimeout(()=>animateSlide(slides[0]),100);",
    "  setTimeout(()=>animateSlide(slides[0]),100);\n  setTimeout(startHeroAnimations,2200);"
)

with open(html_path, 'w') as f:
    f.write(html)

print("All changes applied!")
print(f"New file size: {len(html)} chars")
