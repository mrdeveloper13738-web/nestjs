import os
import markdown
import sys

sys.stdout.reconfigure(encoding='utf-8')

INPUT_DIR = "content"
OUTPUT_DIR = "build_html"

os.makedirs(OUTPUT_DIR, exist_ok=True)

index_items = []

for root, _, files in os.walk(INPUT_DIR):
    for file in files:
        if file.endswith(".md"):
            path = os.path.join(root, file)

            with open(path, "r", encoding="utf-8") as f:
                text = f.read()

            body = markdown.markdown(text)
            title = file.replace(".md", "")

            html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>{title}</title>
</head>
<body>
<h1>{title}</h1>
{body}
</body>
</html>
"""

            out_file = file.replace(".md", ".html")
            out_path = os.path.join(OUTPUT_DIR, out_file)

            with open(out_path, "w", encoding="utf-8") as f:
                f.write(html)

            index_items.append((title, out_file))

# index.html
index_html = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Docs</title>
</head>
<body>
<h1>Documentation</h1>
<ul>
"""

for title, link in index_items:
    index_html += f'<li><a href="{link}">{title}</a></li>\n'

index_html += "</ul></body></html>"

with open(os.path.join(OUTPUT_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(index_html)

print("Build complete")
