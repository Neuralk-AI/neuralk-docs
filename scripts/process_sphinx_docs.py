#!/usr/bin/env python3
"""
Process Sphinx-Gallery generated markdown files for Docusaurus.

This script:
1. Extracts HTML output blocks (sklearn estimators, skrub TableReport, etc.) to separate HTML files
2. Replaces them with iframes in the markdown
3. Fixes API links and unescapes Sphinx-escaped characters
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
STATIC_DIR = Path(__file__).parent.parent / "static" / "html_outputs"


def unescape_sphinx(content: str) -> str:
    """Unescape characters that Sphinx escaped in the markdown."""
    # Unescape: \* -> *, \_ -> _, \{ -> {, \} -> }, \` -> `
    content = content.replace(r'\*', '*')
    content = content.replace(r'\_', '_')
    content = content.replace(r'\{', '{')
    content = content.replace(r'\}', '}')
    content = content.replace(r'\[', '[')
    content = content.replace(r'\]', ']')
    content = content.replace(r'\`', '`')
    return content


def extract_html_blocks(content: str, basename: str) -> tuple[str, list[Path]]:
    """
    Extract HTML output blocks from content, save to files, replace with iframes.

    Sphinx-Gallery output blocks start with <div class="output_subarea ...">
    and end right before <br /> tags.
    """
    STATIC_DIR.mkdir(parents=True, exist_ok=True)
    html_files = []
    html_block_count = 0

    # Unescape Sphinx escapes first
    content = unescape_sphinx(content)

    # Find all <div class="output_subarea ..."> blocks
    # These end right before <br /> tags
    pattern = r'<div\s+class="output_subarea[^"]*"[^>]*>'
    result_parts = []
    last_end = 0

    for match in re.finditer(pattern, content):
        start = match.start()
        result_parts.append(content[last_end:start])

        # Find the end - look for <br /> which follows output blocks
        remaining = content[start:]
        br_match = re.search(r'\n<br />', remaining)

        if br_match:
            end_offset = br_match.start()
            html_block = remaining[:end_offset].rstrip()
            html_block_count += 1

            # Determine iframe height based on content type
            if 'report_' in html_block and '-wrapper' in html_block:
                height = 500  # TableReport - taller
            else:
                height = 150  # sklearn estimator - shorter

            # Save to file
            html_filename = f"{basename}_output_{html_block_count}.html"
            html_path = STATIC_DIR / html_filename
            full_html = f'''<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
</head>
<body>
{html_block}
</body>
</html>'''
            html_path.write_text(full_html, encoding='utf-8')
            html_files.append(html_path)

            # Replace with iframe
            result_parts.append(
                f'<iframe src="/html_outputs/{html_filename}" width="100%" '
                f'height="{height}" style="border:1px solid #ddd; border-radius: 4px;"></iframe>\n'
            )
            last_end = start + end_offset
        else:
            # No <br /> found, keep original
            result_parts.append(match.group(0))
            last_end = match.end()

    result_parts.append(content[last_end:])
    return ''.join(result_parts), html_files


def fix_links(content: str) -> str:
    """Fix Sphinx-generated links to match Docusaurus structure."""
    # Fix relative api links
    content = re.sub(
        r'\.\./api/generated/([^)#\s]+)\.md(?:#[^)]*)?',
        r'/api-reference/generated/\1',
        content
    )
    content = re.sub(
        r'\.\./api-reference/generated/([^)#\s]+)\.md(?:#[^)]*)?',
        r'/api-reference/generated/\1',
        content
    )

    # Fix internal links to other Sphinx docs
    content = re.sub(
        r'00\d{2}_([^)#\s]+)\.md(#[^)]*)?',
        r'/docs/\1\2',
        content
    )

    return content


def process_file(basename: str) -> None:
    """Process a .md file: extract HTML, fix links, write to .processed.md."""
    src_path = DOCS_DIR / f"{basename}.md"
    dst_path = DOCS_DIR / f"{basename}.processed.md"

    if not src_path.exists():
        print(f"⚠️  Skipping {basename}: file not found")
        return

    content = src_path.read_text(encoding='utf-8')
    original_lines = len(content.split('\n'))

    # Extract HTML blocks to separate files
    content, html_files = extract_html_blocks(content, basename)

    # Fix links
    content = fix_links(content)

    # Add frontmatter with explicit id to match sidebar
    doc_id = basename.lstrip('0123456789_')
    frontmatter = f"---\nid: {doc_id}\n---\n\n"
    content = frontmatter + content

    new_lines = len(content.split('\n'))
    print(f"📑 {basename}: {original_lines} -> {new_lines} lines, {len(html_files)} HTML files")

    # Write to .processed.md
    dst_path.write_text(content, encoding='utf-8')
    print(f"✅ Created {dst_path.name}")

    # Remove original to avoid duplicate doc IDs
    src_path.unlink()
    print(f"🗑️  Removed {src_path.name}")


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
