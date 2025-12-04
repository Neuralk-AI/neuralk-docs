#!/usr/bin/env python3
"""
Process Sphinx-Gallery generated markdown files for Docusaurus.

This script:
1. Fixes API links from Sphinx format to Docusaurus format
2. Adds frontmatter to disable TOC (which crashes on large HTML content)
3. Injects an inline TOC as markdown
"""

import re
import sys
from pathlib import Path

# Files to process (Sphinx-Gallery generated)
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
    slug = text.lower()
    # Remove markdown links, keep text
    slug = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', slug)
    # Remove backticks
    slug = slug.replace('`', '')
    # Replace spaces and special chars with hyphens
    slug = re.sub(r'[^\w\s-]', '', slug)
    slug = re.sub(r'[\s_]+', '-', slug)
    slug = slug.strip('-')
    return slug


def extract_headings(content: str) -> list[dict]:
    """
    Extract markdown headings, ignoring those inside code blocks or HTML.
    """
    headings = []
    in_code_block = False
    in_html_block = False

    for line in content.split('\n'):
        if line.startswith('```'):
            in_code_block = not in_code_block
            continue

        if '<style' in line.lower():
            in_html_block = True
        if '</style>' in line.lower():
            in_html_block = False
            continue

        if in_code_block or in_html_block:
            continue

        match = re.match(r'^(#{1,6})\s+(.+)$', line)
        if match:
            level = len(match.group(1))
            value = match.group(2).strip()

            # Skip headings that look like code comments or CSS
            if value.startswith(('report', 'Note:', 'Silence')):
                continue
            if len(value) < 3:
                continue

            headings.append({
                'value': value,
                'id': slugify(value),
                'level': level,
            })

    return headings


def generate_inline_toc(headings: list[dict]) -> str:
    """Generate an inline TOC as markdown."""
    if not headings:
        return ""

    lines = ["## Contents", ""]
    min_level = min(h['level'] for h in headings)

    for h in headings:
        indent = "  " * (h['level'] - min_level)
        # Remove markdown formatting from display text
        display = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', h['value'])
        display = display.replace('`', '')
        lines.append(f"{indent}- [{display}](#{h['id']})")

    lines.append("")
    return '\n'.join(lines)


def process_file(basename: str) -> None:
    """Process a .md file: fix links, add frontmatter, inject TOC, write to .processed.md."""
    src_path = DOCS_DIR / f"{basename}.md"
    dst_path = DOCS_DIR / f"{basename}.processed.md"

    if not src_path.exists():
        print(f"⚠️  Skipping {basename}: file not found")
        return

    content = src_path.read_text(encoding='utf-8')

    # Fix API links
    content = fix_api_links(content)

    # Extract headings for inline TOC
    headings = extract_headings(content)
    print(f"📑 {basename}: found {len(headings)} headings")

    # Generate inline TOC
    inline_toc = generate_inline_toc(headings)

    # Build new content with frontmatter
    # Use explicit id to match sidebar references
    doc_id = basename.lstrip('0123456789_')
    frontmatter = f"---\nid: {doc_id}\nhide_table_of_contents: true\n---\n\n"

    # Find where to insert TOC (after first heading)
    first_heading_match = re.search(r'^#\s+.+$', content, re.MULTILINE)
    if first_heading_match:
        insert_pos = first_heading_match.end()
        new_content = (
            frontmatter +
            content[:insert_pos] +
            "\n\n" + inline_toc + "\n" +
            content[insert_pos:]
        )
    else:
        new_content = frontmatter + inline_toc + "\n" + content

    # Write to processed file
    dst_path.write_text(new_content, encoding='utf-8')
    print(f"✅ Created {dst_path.name}")


def main():
    print("Processing Sphinx-Gallery markdown files...\n")

    for basename in SPHINX_GALLERY_FILES:
        try:
            process_file(basename)
        except Exception as e:
            print(f"❌ Error processing {basename}: {e}")
            sys.exit(1)

    print("\nDone!")


if __name__ == "__main__":
    main()
