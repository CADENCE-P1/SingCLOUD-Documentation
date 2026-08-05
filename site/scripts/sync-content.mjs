#!/usr/bin/env node
/**
 * Sync the repo's canonical markdown (docs/, datasets/) into the Starlight
 * content directory (src/content/docs/).
 *
 * The repo markdown stays plain GitHub-flavoured markdown with no frontmatter,
 * so it remains readable on GitHub. This script runs before `astro dev` and
 * `astro build` and, for each page:
 *
 *   1. lifts the first `# heading` into `title:` frontmatter (Starlight
 *      renders the title itself, so the heading is removed from the body);
 *   2. reads the status emoji (✅ / 🟡 / ⚪) from the page's status table and
 *      turns it into a sidebar badge;
 *   3. rewrites relative `.md` links to site routes, and links to files that
 *      are not part of the site (tools/, source_material/, …) to GitHub URLs;
 *   4. sets `editUrl` so every page's "Edit page" link points at the real
 *      source file in the repo.
 *
 * Never edit files in src/content/docs/guides/ or src/content/docs/datasets/
 * by hand — they are overwritten on every sync.
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
const repoRoot = path.resolve(here, '..', '..');
const contentRoot = path.resolve(here, '..', 'src', 'content', 'docs');

const REPO_URL = 'https://github.com/CADENCE-P1/SingCLOUD-Documentation';
const RAW_URL = 'https://raw.githubusercontent.com/CADENCE-P1/SingCLOUD-Documentation/main';
const IMAGE_EXTS = new Set(['.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp']);

/** Repo directory → site section. */
const SECTIONS = [
  { src: 'docs', out: 'guides' },
  { src: 'catalog_pages', out: 'catalog' },
  { src: 'datasets', out: 'datasets' },
];

/** Pages pinned to the top of their auto-generated sidebar group. */
const PINNED = {
  'catalog_pages/index.md': { order: 0, label: 'Page index' },
  'catalog_pages/template_intro.md': { order: 1, label: 'How to read a page' },
  'catalog_pages/template.md': { order: 2, label: 'Page template' },
  'datasets/index.md': { order: 0, label: 'Notes index' },
  'datasets/full_inventory.md': { order: 1, label: 'Full inventory (OCR)' },
};

const STATUS_BADGES = {
  '✅': { text: 'Verified', variant: 'success' },
  '🟡': { text: 'Draft', variant: 'caution' },
  '⚪': { text: 'Stub', variant: 'note' },
};

/** Site route (no trailing slash) for a repo-relative .md path, or null. */
function routeFor(repoPath) {
  for (const { src, out } of SECTIONS) {
    if (repoPath.startsWith(`${src}/`)) {
      const base = path.posix.basename(repoPath, '.md');
      return base === 'index' ? `/${out}` : `/${out}/${base}`;
    }
  }
  return null;
}

function rewriteLinks(body, srcDir, pageRoute) {
  return body.replace(/(!?)\[([^\]]*)\]\(([^)\s]+)\)/g, (full, bang, label, target) => {
    if (/^(https?:|mailto:|#)/.test(target)) return full;
    const [file, anchor] = target.split('#');
    const repoPath = path.posix.normalize(path.posix.join(srcDir, file));
    const route = file.endsWith('.md') ? routeFor(repoPath) : null;
    if (route) {
      const rel = path.posix.relative(pageRoute, route);
      const href = (rel === '' ? '.' : rel) + '/' + (anchor ? `#${anchor}` : '');
      return `${bang}[${label}](${href})`;
    }
    // File that is not part of the site → link to it on GitHub.
    const ext = path.posix.extname(repoPath).toLowerCase();
    const base = bang || IMAGE_EXTS.has(ext) ? RAW_URL : `${REPO_URL}/blob/main`;
    return `${bang}[${label}](${base}/${repoPath}${anchor ? `#${anchor}` : ''})`;
  });
}

function toYaml(value, indent = '') {
  return Object.entries(value)
    .map(([k, v]) =>
      typeof v === 'object'
        ? `${indent}${k}:\n${toYaml(v, indent + '  ')}`
        : `${indent}${k}: ${JSON.stringify(v)}`
    )
    .join('\n');
}

let count = 0;
for (const { src, out } of SECTIONS) {
  const outDir = path.join(contentRoot, out);
  fs.rmSync(outDir, { recursive: true, force: true });
  fs.mkdirSync(outDir, { recursive: true });

  for (const name of fs.readdirSync(path.join(repoRoot, src)).sort()) {
    if (!name.endsWith('.md') || name.startsWith('_')) continue;
    const repoPath = `${src}/${name}`;
    let md = fs.readFileSync(path.join(repoRoot, repoPath), 'utf8');

    const titleMatch = md.match(/^#\s+(.+?)\s*$/m);
    const title = titleMatch ? titleMatch[1] : path.basename(name, '.md');
    if (titleMatch) md = md.replace(titleMatch[0], '').replace(/^\s+/, '');

    const frontmatter = { title, editUrl: `${REPO_URL}/edit/main/${repoPath}` };

    const sidebar = { ...(PINNED[repoPath] ?? {}) };
    // Structural pages (indexes, templates) carry no status of their own.
    const status = PINNED[repoPath]
      ? null
      : md.match(/\|\s*\*\*Status\*\*\s*\|\s*(✅|🟡|⚪)/);
    if (status) sidebar.badge = STATUS_BADGES[status[1]];
    if (Object.keys(sidebar).length > 0) frontmatter.sidebar = sidebar;

    const pageRoute = routeFor(repoPath);
    md = rewriteLinks(md, src, pageRoute);

    fs.writeFileSync(
      path.join(outDir, name),
      `---\n${toYaml(frontmatter)}\n---\n\n${md}`
    );
    count++;
  }
}
console.log(`[sync-content] ${count} pages synced into src/content/docs/`);
