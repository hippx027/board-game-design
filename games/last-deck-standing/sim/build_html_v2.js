// Pre-render rulebook-v2-draft.md into a standalone rulebook-v2.html (styles copied from rulebook.html).
// Usage: node sim/build_html_v2.js   (needs `npm install marked@12`)
const fs = require("fs");
const { marked } = require("marked");
const md = fs.readFileSync("rulebook-v2-draft.md", "utf8").split("\n").slice(1).join("\n");
let body = marked.parse(md);
body = body.replace(/<table>/g, '<div class="tbl"><table>').replace(/<\/table>/g, "</table></div>");
body = body.replace(/<h2>([^<]*)<\/h2>/g, (m, t) => `<h2 id="${t.toLowerCase().replace(/[^a-z0-9]+/g, "-")}">${t}</h2>`);
// everything from "Playtest options still to run" onward is designer notes
body = body.replace(/(<h2 id="playtest-options-still-to-run">)/, '<hr>\n<section class="designer">\n$1') + "</section>";
const css = fs.readFileSync("rulebook.html", "utf8").match(/<style>[\s\S]*?<\/style>/)[0];
let page = `<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Last Deck Standing Rules v2</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@700&family=IBM+Plex+Sans:wght@400;600&family=IBM+Plex+Mono:wght@500&display=swap">
${css}</head><body><div class="wrap">
<header><div class="eyebrow">Realtime rules &#183; v2 draft &#183; 2026-10-13</div><h1>Last Deck Standing</h1>
<div class="meta"><span class="chip">2&#8211;10 players</span><span class="chip">No rounds</span><span class="chip">Battle royale deck builder</span></div></header>
<main id="rules">
${body}</main></div></body></html>`;
page = page.replace(/[^\x00-\x7F]/g, c => `&#${c.codePointAt(0)};`);
fs.writeFileSync("rulebook-v2.html", page);
console.log("ok", page.length);
