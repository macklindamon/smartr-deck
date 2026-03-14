#!/usr/bin/env node
// ── Smartr Deck · Local Relay Server ──────────────────────
// Zero-dependency Node server that:
//   • Serves static files (deck.html, presenter.html, remote.html, etc.)
//   • Relays slide commands between phone remote ↔ laptop deck via SSE
//
// Usage:
//   node server.js            → starts on port 8000
//   PORT=3000 node server.js  → custom port

const http = require('http');
const fs   = require('fs');
const path = require('path');

const PORT = parseInt(process.env.PORT || '8000', 10);
const ROOT = __dirname;

// ── Local IP detection ─────────────────────────────────────
const nets = require('os').networkInterfaces();
let localIP = 'localhost';
for (const iface of Object.values(nets)) {
  for (const addr of iface) {
    if (addr.family === 'IPv4' && !addr.internal) {
      localIP = addr.address;
      break;
    }
  }
  if (localIP !== 'localhost') break;
}

// ── MIME types ────────────────────────────────────────────
const MIME = {
  '.html': 'text/html; charset=utf-8',
  '.css':  'text/css; charset=utf-8',
  '.js':   'application/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.svg':  'image/svg+xml',
  '.png':  'image/png',
  '.jpg':  'image/jpeg',
  '.gif':  'image/gif',
  '.ico':  'image/x-icon',
  '.woff': 'font/woff',
  '.woff2':'font/woff2',
  '.ttf':  'font/ttf',
  '.txt':  'text/plain; charset=utf-8',
};

// ── SSE clients ───────────────────────────────────────────
const sseClients = new Set();
let deckState = { current: 0, total: 16 };

// ── Notes persistence ─────────────────────────────────────
const NOTES_FILE = path.join(ROOT, 'notes-saved.json');

function loadSavedNotes() {
  try {
    return JSON.parse(fs.readFileSync(NOTES_FILE, 'utf8'));
  } catch (_) {
    return null;
  }
}

function saveSavedNotes(notes) {
  fs.writeFileSync(NOTES_FILE, JSON.stringify(notes, null, 2), 'utf8');
}

function broadcast(data) {
  const msg = `data: ${JSON.stringify(data)}\n\n`;
  for (const res of sseClients) {
    try { res.write(msg); } catch (_) { sseClients.delete(res); }
  }
}

// ── HTTP server ───────────────────────────────────────────
const server = http.createServer((req, res) => {
  const parsed = new URL(req.url, `http://localhost:${PORT}`);
  const pathname = parsed.pathname;

  // ── SSE endpoint ──
  if (pathname === '/sse') {
    res.writeHead(200, {
      'Content-Type':  'text/event-stream',
      'Cache-Control': 'no-cache',
      'Connection':    'keep-alive',
      'Access-Control-Allow-Origin': '*',
    });
    res.write(`data: ${JSON.stringify({ type: 'state', ...deckState })}\n\n`);
    sseClients.add(res);
    req.on('close', () => sseClients.delete(res));
    return;
  }

  // ── Command endpoint (phone → server → deck) ──
  if (pathname === '/cmd' && req.method === 'POST') {
    let body = '';
    req.on('data', chunk => { body += chunk; });
    req.on('end', () => {
      try {
        const cmd = JSON.parse(body);
        console.log('[cmd]', cmd.action, cmd.index ?? '', cmd.value ?? '', '→', sseClients.size, 'clients');
        // Update deckState so all clients stay in sync
        if (cmd.action === 'goto' && cmd.index != null) {
          deckState.current = cmd.index;
        } else if (cmd.action === 'next') {
          deckState.current = Math.min(deckState.current + 1, (deckState.total || 16) - 1);
        } else if (cmd.action === 'prev') {
          deckState.current = Math.max(deckState.current - 1, 0);
        }
        // Relay command to all SSE listeners (deck + presenter + script)
        broadcast({ type: 'cmd', action: cmd.action, index: cmd.index, value: cmd.value });
        // Broadcast updated state so all clients sync slide position
        if (cmd.action === 'next' || cmd.action === 'prev' || cmd.action === 'goto') {
          broadcast({ type: 'state', ...deckState });
        }
        res.writeHead(200, {
          'Content-Type': 'application/json',
          'Access-Control-Allow-Origin': '*',
        });
        res.end('{"ok":true}');
      } catch (_) {
        res.writeHead(400, { 'Content-Type': 'application/json' });
        res.end('{"error":"bad json"}');
      }
    });
    return;
  }

  // ── State update (deck → server → remotes) ──
  if (pathname === '/state' && req.method === 'POST') {
    let body = '';
    req.on('data', chunk => { body += chunk; });
    req.on('end', () => {
      try {
        const state = JSON.parse(body);
        deckState = { current: state.current ?? 0, total: state.total ?? 18 };
        broadcast({ type: 'state', ...deckState });
        res.writeHead(200, {
          'Content-Type': 'application/json',
          'Access-Control-Allow-Origin': '*',
        });
        res.end('{"ok":true}');
      } catch (_) {
        res.writeHead(400, { 'Content-Type': 'application/json' });
        res.end('{"error":"bad json"}');
      }
    });
    return;
  }

  // ── CORS preflight ──
  if (req.method === 'OPTIONS') {
    res.writeHead(204, {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type',
    });
    res.end();
    return;
  }

  // ── Server info (for hub.html) ──
  if (pathname === '/info') {
    res.writeHead(200, {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*',
      'Cache-Control': 'no-cache',
    });
    res.end(JSON.stringify({ ip: localIP, port: PORT }));
    return;
  }

  // ── GET /notes — return saved notes (or empty) ──
  if (pathname === '/notes' && req.method === 'GET') {
    const saved = loadSavedNotes();
    res.writeHead(200, {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*',
      'Cache-Control': 'no-cache',
    });
    res.end(JSON.stringify(saved || {}));
    return;
  }

  // ── POST /notes — save notes and broadcast to SSE clients ──
  if (pathname === '/notes' && req.method === 'POST') {
    let body = '';
    req.on('data', chunk => { body += chunk; });
    req.on('end', () => {
      try {
        const notes = JSON.parse(body);
        saveSavedNotes(notes);
        broadcast({ type: 'notes', notes });
        res.writeHead(200, {
          'Content-Type': 'application/json',
          'Access-Control-Allow-Origin': '*',
        });
        res.end('{"ok":true}');
      } catch (_) {
        res.writeHead(400, { 'Content-Type': 'application/json' });
        res.end('{"error":"bad json"}');
      }
    });
    return;
  }

  // ── Static files ──
  let filePath = pathname === '/' ? '/hub.html' : pathname;
  // Prevent directory traversal
  const safePath = path.normalize(filePath).replace(/^(\.\.[\/\\])+/, '');
  const fullPath = path.join(ROOT, safePath);
  if (!fullPath.startsWith(ROOT)) {
    res.writeHead(403); res.end('Forbidden'); return;
  }

  const ext = path.extname(fullPath).toLowerCase();
  const contentType = MIME[ext] || 'application/octet-stream';

  fs.readFile(fullPath, (err, data) => {
    if (err) {
      res.writeHead(404, { 'Content-Type': 'text/plain' });
      res.end('Not found');
      return;
    }
    res.writeHead(200, {
      'Content-Type': contentType,
      'Cache-Control': 'no-cache',
    });
    res.end(data);
  });
});

server.listen(PORT, '0.0.0.0', () => {
  console.log(`\n  ┌─────────────────────────────────────────────┐`);
  console.log(`  │  Smartr Deck Server                          │`);
  console.log(`  ├─────────────────────────────────────────────┤`);
  console.log(`  │  Hub    → http://localhost:${PORT}              │`);
  console.log(`  │  Phone  → http://${localIP}:${PORT}/remote-notes  │`);
  console.log(`  └─────────────────────────────────────────────┘\n`);
});
