# from pathlib import Path
# from bs4 import BeautifulSoup

# SRC_DIR = Path("static/auto_examples")
# DST_DIR = Path("docs")
# DST_DIR.mkdir(exist_ok=True, parents=True)

# for html_file in SRC_DIR.glob("*.html"):
#     title = html_file.stem.replace("_", " ").title()

#     with open(html_file, "r", encoding="utf-8") as f:
#         soup = BeautifulSoup(f, "html.parser")

#     # Extract headings
#     headings_md = ""
#     for tag in soup.find_all(["h1", "h2", "h3"]):
#         level = int(tag.name[1])
#         text = tag.get_text()
#         headings_md += f'{"#"*level} {text}\n\n'

#     # MDX with iframe
#     mdx_content = f"""---
# title: "{title}"
# sidebar_position: 4
# ---

# import React from 'react';

# {headings_md}

# <div style={{ width: '100%', height: '100vh', border: 'none' }}>
#   <iframe
#     src="/auto_examples/{html_file.name}"
#     title="{title}"
#     style={{ width: '100%', height: '100%', border: 'none' }}
#   />
# </div>
# """

#     dst_file = DST_DIR / f"{html_file.stem}.mdx"
#     with open(dst_file, "w", encoding="utf-8") as f:
#         f.write(mdx_content)

#     print(f"✅ Generated {dst_file}")
