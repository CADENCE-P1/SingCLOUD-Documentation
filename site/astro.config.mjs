// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// Deployed as a GitHub Pages *project* site, so all URLs live under the
// repository-name base path.
export default defineConfig({
  site: 'https://cadence-p1.github.io',
  base: '/SingCLOUD-Documentation',
  integrations: [
    starlight({
      title: 'SingCLOUD Data Catalogue',
      description:
        'Standardised documentation for the datasets available through SingCLOUD: contents, provenance, linkage, quality and governance.',
      logo: { src: './src/assets/logo.svg' },
      favicon: '/favicon.svg',
      social: [
        {
          icon: 'github',
          label: 'GitHub',
          href: 'https://github.com/CADENCE-P1/SingCLOUD-Documentation',
        },
      ],
      customCss: ['./src/styles/custom.css'],
      sidebar: [
        {
          label: 'Guides',
          items: [
            { label: 'Why this catalogue exists', slug: 'guides/00_rationale' },
            { label: 'Documentation standard', slug: 'guides/01_documentation_standard' },
            { label: 'Access & governance', slug: 'guides/02_access_and_governance' },
            { label: 'Linkage guide', slug: 'guides/03_linkage_guide' },
          ],
        },
        {
          label: 'Datasets',
          items: [{ autogenerate: { directory: 'datasets' } }],
        },
      ],
    }),
  ],
});
