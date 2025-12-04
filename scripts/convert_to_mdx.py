#!/usr/bin/env python3
"""
Convert Sphinx-Gallery generated markdown files to MDX with pre-computed TOC.

This script:
1. Parses headings from markdown files (ignoring those inside code blocks)
2. Generates a TOC array for Docusaurus
3. Converts .md to .mdx with the exported TOC
"""

import re
import sys
from pathlib import Path

# Files to convert (Sphinx-Gallery generated)
SPHINX_GALLERY_FILES = [
    "0010_housing_classification",
    "0020_selecting_sampling_context",
    "0030_two_moon_classification",
    "0040_categorization",
    "0050_on_premise_classifier",
]

DOCS_DIR = Path(__file__).parent.parent / "docs"


def fix_api_links(content: str) -> str:
    """
    Fix Sphinx-generated API links to match Docusaurus structure.

    Sphinx generates: ../api/generated/neuralk.Classifier.md#neuralk.Classifier
    Docusaurus expects: /api-reference/generated/neuralk.Classifier
    """
    # Fix relative api links to absolute api-reference links
    content = re.sub(
        r'\.\./api/generated/([^)#\s]+)\.md(?:#[^)]*)?',
        r'/api-reference/generated/\1',
        content
    )
    # Also fix any ../api-reference links (just in case)
    content = re.sub(
        r'\.\./api-reference/generated/([^)#\s]+)\.md(?:#[^)]*)?',
        r'/api-reference/generated/\1',
        content
    )
    return content


def slugify(text: str) -> str:
    """Convert heading text to a URL-friendly slug."""
    # Lowercase
    slug = text.lower()
    # Remove markdown links, keep text
    slug = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', slug)
    # Remove backticks
    slug = slug.replace('`', '')
    # Replace spaces and special chars with hyphens
    slug = re.sub(r'[^\w\s-]', '', slug)
    slug = re.sub(r'[\s_]+', '-', slug)
    # Remove leading/trailing hyphens
    slug = slug.strip('-')
    return slug


def extract_headings(content: str) -> list[dict]:
    """
    Extract markdown headings, ignoring those inside code blocks or HTML.
    Returns list of {value, id, level} dicts.
    """
    headings = []
    in_code_block = False
    in_html_block = False

    for line in content.split('\n'):
        # Track code blocks
        if line.startswith('```'):
            in_code_block = not in_code_block
            continue

        # Track HTML style blocks (common in Sphinx output)
        if '<style' in line.lower():
            in_html_block = True
        if '</style>' in line.lower():
            in_html_block = False
            continue

        # Skip if inside code or HTML
        if in_code_block or in_html_block:
            continue

        # Match markdown headings (# ## ### etc.)
        match = re.match(r'^(#{1,6})\s+(.+)$', line)
        if match:
            level = len(match.group(1))
            value = match.group(2).strip()

            # Skip headings that look like code comments or CSS
            if value.startswith(('report', 'Note:', 'Silence')):
                continue
            # Skip very short headings that are likely noise
            if len(value) < 3:
                continue

            heading_id = slugify(value)
            headings.append({
                'value': value,
                'id': heading_id,
                'level': level,
            })

    return headings


def generate_toc_export(headings: list[dict]) -> str:
    """Generate the MDX export statement for TOC."""
    if not headings:
        return ""

    lines = ["export const toc = ["]
    for h in headings:
        # Escape quotes in value
        value = h['value'].replace("'", "\\'").replace('"', '\\"')
        lines.append(f"  {{value: '{value}', id: '{h['id']}', level: {h['level']}}},")
    lines.append("];")

    return '\n'.join(lines)


def convert_file(basename: str) -> None:
    """Convert a single .md file to .mdx with TOC."""
    md_path = DOCS_DIR / f"{basename}.md"
    mdx_path = DOCS_DIR / f"{basename}.mdx"

    if not md_path.exists():
        print(f"⚠️  Skipping {basename}: .md file not found")
        return

    content = md_path.read_text(encoding='utf-8')

    # Fix API links from Sphinx format to Docusaurus format
    content = fix_api_links(content)

    # Extract headings
    headings = extract_headings(content)
    print(f"📑 {basename}: found {len(headings)} headings")

    # Generate TOC export
    toc_export = generate_toc_export(headings)

    # Check if file already has frontmatter
    if content.startswith('---'):
        # Insert TOC export after frontmatter
        parts = content.split('---', 2)
        if len(parts) >= 3:
            new_content = f"---{parts[1]}---\n\n{toc_export}\n\n{parts[2].lstrip()}"
        else:
            new_content = f"{toc_export}\n\n{content}"
    else:
        # Add frontmatter and TOC export
        new_content = f"{toc_export}\n\n{content}"

    # Write .mdx file
    mdx_path.write_text(new_content, encoding='utf-8')
    print(f"✅ Created {mdx_path.name}")

    # Remove .md file to avoid duplicate doc IDs
    md_path.unlink()
    print(f"🗑️  Removed {md_path.name}")


def main():
    print("Converting Sphinx-Gallery markdown to MDX with TOC...\n")

    for basename in SPHINX_GALLERY_FILES:
        try:
            convert_file(basename)
        except Exception as e:
            print(f"❌ Error converting {basename}: {e}")
            sys.exit(1)
        print()

    print("Done! Don't forget to update sidebars.js if needed.")


if __name__ == "__main__":
    main()
