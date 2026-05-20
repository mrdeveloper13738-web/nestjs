import os
import markdown
from bs4 import BeautifulSoup

INPUT = "content"
OUTPUT = "build_html"

os.makedirs(OUTPUT, exist_ok=True)

index_page = ""

for root, _, files in os.walk(INPUT):
    for file in files:
        if file.endswith(".md"):
            md_path = os.path.join(root, file)

            with open(md_path, "r", encoding="utf-8") as f:
                text = f.read()

            html = markdown.markdown(text)

            name = file.replace(".md", ".html")
            out_path = os.path.join(OUTPUT, name)

            with open(out_path, "w", encoding="utf-8") as f:
                f.write(html)

            # برای index صفحه
            index_page += f'<li><a href="{name}">{file}</a></li>\n'

# ساخت index.html (خیلی مهم برای docset)
index_html = f"""
<html>
<head><title>Docs Index</title></head>
<body>
<h1>Documentation</h1>
<ul>
{index_page}
</ul>
</body>
</html>
"""

with open(os.path.join(OUTPUT, "index.html"), "w", encoding="utf-8") as f:
    f.write(index_html)

print("HTML + index generated")
