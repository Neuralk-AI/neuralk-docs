// Automatically generates sidebar for API reference docs

const fs = require('fs');
const path = require('path');

const GENERATED_DIR = path.join(__dirname, 'api-reference/generated');

// Define API categories and their overview docs (in the root folder)
const categories = [
  { prefix: 'neuralk.Neuralk.analysis.', label: 'Analysis', overview: 'analysis' },
  { prefix: 'neuralk.Neuralk.projects.', label: 'Projects', overview: 'projects' },
  { prefix: 'neuralk.Neuralk.users.', label: 'Users', overview: 'users' },
  { prefix: 'neuralk.Neuralk.datasets.', label: 'Datasets', overview: 'datasets' },
  { prefix: 'neuralk.Neuralk.project_files.', label: 'Project Files', overview: 'project_files' },
  { prefix: 'neuralk.Neuralk.organization.', label: 'Organization', overview: 'organization' },
];

// Helper to make readable labels
function makeLabel(filename, prefix) {
  return filename
    .replace(prefix, '')
    .replace(/_/g, ' ')
    .replace(/\b\w/g, (l) => l.toUpperCase());
}

// Generate sidebar items for each category
const sidebarCategories = categories.map(({ prefix, label, overview }) => {
  const items = fs.readdirSync(GENERATED_DIR)
    .filter(f => f.startsWith(prefix) && f.endsWith('.md'))
    .map(f => ({
      type: 'doc',
      id: `generated/${f.replace('.md', '')}`,
      label: f.replace('.md', ''), 
    }));

  return {
    type: 'category',
    label,
    link: { type: 'doc', id: overview }, // 👈 links to e.g. api-reference/analysis.md
    items,
  };
});

// Export the sidebar
module.exports = {
  guidesSidebar: [
    {
      type: 'html',
      value: 'Explore the API',
      className: 'sidebar-getting-started',
      defaultStyle: true,
    },
    {
      type: 'doc',
      id: 'index',
      label: 'Introduction',
    },
    {
      type: 'doc',
      id: 'generated/neuralk.Neuralk',
      label: 'Neuralk',
    },
    ...sidebarCategories,
  ],
};
