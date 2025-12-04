// @ts-check
// `@type` JSDoc annotations allow editor autocompletion and type checking
// (when paired with `@ts-check`).
// There are various equivalent ways to declare your Docusaurus config.
// See: https://docusaurus.io/docs/api/docusaurus-config

import {themes as prismThemes} from 'prism-react-renderer';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Neuralk AI',
  tagline: 'Dinosaurs are coool',
  favicon: 'img/favicon.jpg',

  // Future flags, see https://docusaurus.io/docs/api/docusaurus-config#future
  future: {
    v4: true, // Improve compatibility with the upcoming Docusaurus v4
  },

  // Set the production url of your site here
  url: 'https://your-docusaurus-site.example.com',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: '/',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'facebook', // Usually your GitHub org/user name.
  projectName: 'docusaurus', // Usually your repo name.

  onBrokenLinks: 'throw',

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  // Use 'detect' to parse .md files as plain markdown (not MDX)
  // This prevents MDX from misinterpreting HTML in Sphinx-generated docs
  markdown: {
    format: 'detect',
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: './sidebars.js',
          // Exclude original Sphinx files (we use .processed.md versions)
          exclude: ['**/00[0-9][0-9]_*.md'],
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          // editUrl:
            // 'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
        },
        blog: {
          showReadingTime: true,
          feedOptions: {
            type: ['rss', 'atom'],
            xslt: true,
          },
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          // editUrl:
            // 'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
          // Useful options to enforce blogging best practices
          onInlineTags: 'warn',
          onInlineAuthors: 'warn',
          onUntruncatedBlogPosts: 'warn',
        },
        
        theme: {
          customCss: './src/css/custom.css',
        },
      }),
    ],
    
  ],
  
  plugins: [
    [
      '@docusaurus/plugin-content-docs',
      {
        id: 'api-reference',                      // unique ID
        path: 'api-reference',                    // folder for the second docs
        routeBasePath: 'api-reference',           // URL prefix
        sidebarPath: require.resolve('./sidebarsGuides.js'), // separate sidebar
      },
    ],
    // Docusaurus search plugin
    [
      require.resolve('@cmfcmf/docusaurus-search-local'),
      {
        indexDocs: true,    // include docs in search
        indexBlog: false,   // exclude blog if you have one
        indexPages: false,  // exclude standalone pages
        language: 'en',
      },
    ],
  ],


  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      // Replace with your project's social card
      image: 'img/docusaurus-social-card.jpg',
      colorMode: {
        defaultMode: 'light', // fallback if browser preference not detected
        disableSwitch: false,
        respectPrefersColorScheme: false,
      },
      navbar: {
        // title: 'Neuralk AI',
        logo: {
          alt: 'Neuralk AI Logo',
          src: 'img/neuralk_logo.svg',
          srcDark: 'img/neuralk_logo_dark.svg',
          href: '/docs/intro', // <- your custom link here
        },
        items: [
          {
            type: 'docSidebar',
            sidebarId: 'tutorialSidebar',
            position: 'right',
            label: 'Docs',
          },
          {
            type: 'doc',        // for second docs plugin
            docId: 'index',     // first page in guides
            docsPluginId: 'api-reference', // important! use the plugin ID of the second docs
            position: 'right',
            label: 'API reference',
          },
          // // {to: '/api', label: 'API reference', position: 'right'},
          // {
          //   href: 'https://github.com/Neuralk-AI/',
          //   label: 'GitHub',
          //   position: 'right',
          // },
          {
            href: 'https://dashboard.neuralk-ai.com/',
            label: 'Benchmark',
            position: 'right',
          },
          {
            type: 'search',       // adds the search bar
            position: 'right',     // left side of the navbar
          },
          {
            href: 'https://www.neuralk-ai.com/contact',      // link to your page or external URL
            label: 'Contact us',
            position: 'right',
            className: 'button button--primary', // makes it look like a button
          },
          {
            href: 'https://www.neuralk-ai.com/request-credentials?utm_source=documentation&utm_medium=nav-button&utm_campaign=friendly-launch',      // link to your page or external URL
            label: 'Get access',
            position: 'right',
            className: 'button button--secondary', // makes it look like a button
          },
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'NEURALK AI',
            items: [
              {
                label: 'Company',
                to: 'https://www.neuralk-ai.com',
              },
              {
                label: 'Contact us',
                to: 'https://www.neuralk-ai.com/contact',
              },
             {
                label: 'Webinars',
                to: 'https://www.neuralk-ai.com/webinars',
              },
              {
                label: 'Careers',
                to: 'https://www.neuralk-ai.com/careers',
              },
            ],
          },
          {
            title: 'Documentation',
            items: [
              {
                label: 'Prediction Models',
                href: '/docs/models',
              },
              {
                label: 'Expert AI Modules',
                href: '/docs/expert-modules',
              },
            ],
          },
          {
            title: 'More',
            items: [
              {               
                label: 'Blog',
                to: 'https://www.neuralk-ai.com/blog',
              },
              {
                label: 'Linkedin',
                href: 'https://www.linkedin.com/company/neuralk-ai/',
              },
              {
                label: 'TabBench',
                href: 'https://dashboard.neuralk-ai.com/',
              },
              {
                label: 'GitHub',
                href: 'https://github.com/Neuralk-AI/',
              },
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} Neuralk AI.`,
      },
      prism: {
        theme: prismThemes.github,
        darkTheme: prismThemes.dracula,
      },
    }),
};

export default config;
