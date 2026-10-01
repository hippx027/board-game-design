// Pre-render rulebook-draft.md into rulebook.html (no runtime Markdown, ASCII-safe entities)
const fs = require("fs");
const { marked } = require("marked");
const [, , md, html] = process.argv;
const src = fs.readFileSync(md, "utf8").split("\n").slice(3).join("\n");
let body = marked.parse(src);
body = body.replace(/<table>/g, '<div class="tbl"><table>').replace(/<\/table>/g, "</table></div>");
body = body.replace(/<h2>([^<]*)<\/h2>/g, (m, t) => `<h2 id="${t.toLowerCase().replace(/[^a-z0-9]+/g, "-")}">${t}</h2>`);
// quick reference: one paragraph, keep line breaks
body = body.replace(/(<h2 id="quick-reference">Quick Reference<\/h2>\s*)<p>([\s\S]*?)<\/p>/, (m, h, p) => `${h}<p class="qr">${p.replace(/\n/g, "<br>\n")}</p>`);
// designer notes box
body = body.replace(/<hr>\s*([\s\S]*)$/, '<hr>\n<section class="designer">\n$1</section>');
body = body.replace("value 1 gray", '<span class="v1">value 1 gray</span>').replace("2 blue", '<span class="v2">2 blue</span>').replace("3 purple", '<span class="v3">3 purple</span>');
let page = fs.readFileSync(html, "utf8");
page = page.replace(/<main id="rules">[\s\S]*<\/main>/, "<main id=\"rules\">\n" + body + "</main>");
page = page.replace(/<script type="text\/markdown"[\s\S]*$/, "");
if (!page.startsWith("<meta charset")) page = '<meta charset="utf-8">\n' + page;
// encode every non-ASCII character as a numeric entity so the page renders the same under any charset
page = page.replace(/[^\x00-\x7F]/g, c => `&#${c.codePointAt(0)};`);
fs.writeFileSync(html, page);
console.log("ok", page.length);
