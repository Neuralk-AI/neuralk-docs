#!/usr/bin/env python3
"""
Process Sphinx-Gallery generated markdown files for Docusaurus.

This script:
1. Strips HTML output (sklearn estimators, pandas DataFrames, etc.)
2. Fixes API links from Sphinx format to Docusaurus format
3. Keeps code blocks and text content
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


def strip_html(content: str) -> str:
    """
    Strip HTML blocks from content while preserving markdown and code blocks.
    """
    lines = content.split('\n')
    result = []
    in_code_block = False
    in_html_block = False
    html_tag_stack = []

    i = 0
    while i < len(lines):
        line = lines[i]

        # Track code blocks (preserve these)
        if line.startswith('```'):
            in_code_block = not in_code_block
            result.append(line)
            i += 1
            continue

        # Inside code block - keep everything
        if in_code_block:
            result.append(line)
            i += 1
            continue

        # Detect start of HTML blocks we want to remove
        # Style blocks
        if re.match(r'^\s*<style', line, re.IGNORECASE):
            in_html_block = True
            i += 1
            continue

        if in_html_block and re.search(r'</style>', line, re.IGNORECASE):
            in_html_block = False
            i += 1
            continue

        # Skip lines that are purely HTML div/span blocks (sklearn output)
        if re.match(r'^\s*<div\s+[^>]*(?:sk-|sklearn|class=)[^>]*>', line, re.IGNORECASE):
            # Find closing tag - could be multi-line
            depth = 1
            i += 1
            while i < len(lines) and depth > 0:
                if '<div' in lines[i].lower():
                    depth += lines[i].lower().count('<div')
                if '</div>' in lines[i].lower():
                    depth -= lines[i].lower().count('</div>')
                i += 1
            continue

        # Skip raw HTML table blocks (pandas output)
        if re.match(r'^\s*<div[^>]*>\s*$', line) or re.match(r'^\s*<table', line, re.IGNORECASE):
            depth = 1
            tag = 'div' if '<div' in line.lower() else 'table'
            i += 1
            while i < len(lines) and depth > 0:
                if f'<{tag}' in lines[i].lower():
                    depth += lines[i].lower().count(f'<{tag}')
                if f'</{tag}>' in lines[i].lower():
                    depth -= lines[i].lower().count(f'</{tag}>')
                i += 1
            continue

        # Skip standalone HTML tags and CSS
        if re.match(r'^\s*</?(?:style|div|span|table|tr|td|th|thead|tbody|iframe|script)[^>]*>?\s*$', line, re.IGNORECASE):
            i += 1
            continue

        # Skip lines that look like CSS rules
        if re.match(r'^\s*[#.@]?[\w-]+\s*\{', line) or re.match(r'^\s*[\w-]+\s*:', line) and not line.strip().startswith('#'):
            i += 1
            continue

        # Skip raw CSS property lines
        if re.match(r'^\s*--[\w-]+:', line):
            i += 1
            continue

        # Skip closing braces from CSS
        if re.match(r'^\s*\}\s*$', line):
            i += 1
            continue

        if in_html_block:
            i += 1
            continue

        # Keep this line
        result.append(line)
        i += 1

    # Clean up multiple blank lines
    cleaned = []
    prev_blank = False
    for line in result:
        is_blank = line.strip() == ''
        if is_blank and prev_blank:
            continue
        cleaned.append(line)
        prev_blank = is_blank

    return '\n'.join(cleaned)


def fix_links(content: str) -> str:
    """
    Fix Sphinx-generated links to match Docusaurus structure.
    """
    # Fix relative api links to absolute api-reference links
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
    """Process a .md file in place: strip HTML, fix links."""
    md_path = DOCS_DIR / f"{basename}.md"

    if not md_path.exists():
        print(f"⚠️  Skipping {basename}: file not found")
        return

    content = md_path.read_text(encoding='utf-8')
    original_lines = len(content.split('\n'))

    # Strip HTML
    content = strip_html(content)

    # Fix links
    content = fix_links(content)

    new_lines = len(content.split('\n'))
    print(f"📑 {basename}: {original_lines} -> {new_lines} lines")

    # Write back to same file
    md_path.write_text(content, encoding='utf-8')
    print(f"✅ Updated {md_path.name}")


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
