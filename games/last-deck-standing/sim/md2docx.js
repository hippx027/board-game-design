// Convert the Last Deck Standing rulebook Markdown into an editable .docx
const fs = require("fs");
const d = require("docx");
const { Document, Packer, Paragraph, TextRun, HeadingLevel, Table, TableRow, TableCell,
  WidthType, ShadingType, LevelFormat, BorderStyle, ExternalHyperlink, AlignmentType } = d;

const [, , src, out] = process.argv;
const lines = fs.readFileSync(src, "utf8").split("\n");

const ACCENT = "5B3FA0";
const CONTENT_W = 9360; // US Letter, 1" margins

function runs(text, base = {}) {
  const out = [];
  const re = /(\*\*[^*]+\*\*|`[^`]+`|\[[^\]]+\]\([^)]+\))/g;
  let last = 0, m;
  while ((m = re.exec(text))) {
    if (m.index > last) out.push(new TextRun({ text: text.slice(last, m.index), ...base }));
    const t = m[0];
    if (t.startsWith("**")) out.push(new TextRun({ text: t.slice(2, -2), bold: true, ...base }));
    else if (t.startsWith("`")) out.push(new TextRun({ text: t.slice(1, -1), font: "Consolas", ...base }));
    else {
      const [, label, url] = t.match(/\[([^\]]+)\]\(([^)]+)\)/);
      out.push(new ExternalHyperlink({ link: url, children: [new TextRun({ text: label, style: "Hyperlink", ...base })] }));
    }
    last = m.index + t.length;
  }
  if (last < text.length) out.push(new TextRun({ text: text.slice(last), ...base }));
  return out;
}

function table(rows) {
  const cells = rows.map(r => r.replace(/^\||\|$/g, "").split("|").map(c => c.trim()));
  const header = cells[0], body = cells.slice(2);
  const n = header.length;
  // width by content length, clamped
  const len = header.map((_, i) => Math.max(...[header, ...body].map(r => (r[i] || "").length)));
  const weights = len.map(l => Math.min(Math.max(l, 6), 60));
  const sum = weights.reduce((a, b) => a + b, 0);
  const widths = weights.map(w => Math.floor(CONTENT_W * w / sum));
  widths[n - 1] += CONTENT_W - widths.reduce((a, b) => a + b, 0);
  const border = { style: BorderStyle.SINGLE, size: 4, color: "C9CCD6" };
  const borders = { top: border, bottom: border, left: border, right: border };
  const mk = (r, head) => new TableRow({
    tableHeader: head,
    children: widths.map((w, i) => new TableCell({
      width: { size: w, type: WidthType.DXA },
      borders,
      shading: head ? { type: ShadingType.CLEAR, fill: "ECE7F7", color: "auto" } : undefined,
      margins: { top: 60, bottom: 60, left: 100, right: 100 },
      children: [new Paragraph({ children: runs(r[i] || "", { bold: head || undefined, size: 20 }) })],
    })),
  });
  return new Table({
    width: { size: CONTENT_W, type: WidthType.DXA },
    columnWidths: widths,
    rows: [mk(header, true), ...body.map(r => mk(r, false))],
  });
}

const children = [];
let listInstance = 0;
let i = 0;
let inNumbered = false;
while (i < lines.length) {
  const line = lines[i];
  if (!line.trim()) { i++; continue; }
  if (line.startsWith("|")) {
    const rows = [];
    while (i < lines.length && lines[i].startsWith("|")) rows.push(lines[i++]);
    children.push(table(rows), new Paragraph({ spacing: { after: 60 }, children: [] }));
    inNumbered = false;
    continue;
  }
  let m;
  if ((m = line.match(/^(#{1,3}) (.*)/))) {
    const lvl = m[1].length;
    if (lvl === 1) {
      children.push(new Paragraph({ heading: HeadingLevel.TITLE, children: runs(m[2]) }));
    } else {
      children.push(new Paragraph({ heading: lvl === 2 ? HeadingLevel.HEADING_1 : HeadingLevel.HEADING_2, children: runs(m[2]) }));
    }
    inNumbered = false; i++; continue;
  }
  if (line.trim() === "---") {
    children.push(new Paragraph({ border: { bottom: { style: BorderStyle.SINGLE, size: 8, color: "C9CCD6", space: 1 } }, spacing: { before: 240, after: 240 }, children: [] }));
    inNumbered = false; i++; continue;
  }
  if ((m = line.match(/^(\s*)(\d+)\. (.*)/))) {
    if (!inNumbered) { listInstance++; inNumbered = true; }
    const level = m[1].length >= 3 ? 1 : 0;
    children.push(new Paragraph({ numbering: { reference: "num", level, instance: listInstance }, children: runs(m[3]) }));
    i++; continue;
  }
  if ((m = line.match(/^(\s*)- (.*)/))) {
    const indent = m[1].length;
    const level = indent === 0 ? 0 : 1;
    children.push(new Paragraph({ numbering: { reference: "bullet", level: inNumbered && indent > 0 ? 1 : level }, children: runs(m[2]) }));
    i++; continue;
  }
  if ((m = line.match(/^(\s{3,})(\S.*)/)) && inNumbered) {
    // continuation paragraph inside a numbered item
    children.push(new Paragraph({ indent: { left: 720 }, children: runs(m[2]) }));
    i++; continue;
  }
  // plain paragraph (each line its own paragraph so reference lines stay separate)
  children.push(new Paragraph({ spacing: { after: 120 }, children: runs(line.trim()) }));
  if (!line.startsWith("**")) inNumbered = false;
  i++;
}

const doc = new Document({
  creator: "Brandon and Chris",
  title: "Last Deck Standing — Playtest Rules v1",
  styles: {
    default: { document: { run: { font: "Calibri", size: 22 } } },
    paragraphStyles: [
      { id: "Title", name: "Title", basedOn: "Normal", run: { size: 48, bold: true, color: "1B1F2A" }, paragraph: { spacing: { after: 120 } } },
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", run: { size: 32, bold: true, color: ACCENT }, paragraph: { spacing: { before: 360, after: 120 }, outlineLevel: 0 } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", run: { size: 26, bold: true, color: "1B1F2A" }, paragraph: { spacing: { before: 240, after: 80 }, outlineLevel: 1 } },
    ],
  },
  numbering: {
    config: [
      { reference: "bullet", levels: [
        { level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 720, hanging: 360 } } } },
        { level: 1, format: LevelFormat.BULLET, text: "◦", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 1440, hanging: 360 } } } },
      ] },
      { reference: "num", levels: [
        { level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 720, hanging: 360 } } } },
        { level: 1, format: LevelFormat.BULLET, text: "◦", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 1440, hanging: 360 } } } },
      ] },
    ],
  },
  sections: [{
    properties: { page: { size: { width: 12240, height: 15840 }, margin: { top: 1440, bottom: 1440, left: 1440, right: 1440 } } },
    children,
  }],
});

Packer.toBuffer(doc).then(b => { fs.writeFileSync(out, b); console.log("wrote", out); });
