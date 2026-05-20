import os
import markdown

INPUT = "content"
OUTPUT = "build_html"

os.makedirs(OUTPUT, exist_ok=True)

index_items = []

for root, _, files in os.walk(INPUT):
    for file in files:
        if file.endswith(".md"):
            md_path = os.path.join(root, file)

            with open(md_path, "r", encoding="utf-8") as f:
                text = f.read()

            # تبدیل به HTML
            body = markdown.markdown(text)

            title = file.replace(".md", "")

            # ساخت HTML کامل (خیلی مهم برای doc2dash)
            full_html = f"""<!DOCTYPE html>
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

            out_name = file.replace(".md", ".html")
            out_path = os.path.join(OUTPUT, out_name)

            with open(out_path, "w", encoding="utf-8") as f:
                f.write(full_html)

            index_items.append((title, out_name))

# ساخت index.html (ضروری برای Zeal)
index_html = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Documentation Index</title>
</head>
<body>
<h1>Documentation</h1>
<ul>
"""

for title, link in index_items:
    index_html += f'<li><a href="{link}">{title}</a></li>\n'

index_html += """
</ul>
</body>
</html>
"""

with open(os.path.join(OUTPUT, "index.html"), "w", encoding="utf-8") as f:
    f.write(index_html)

print("✅ HTML files + index ساخته شد")
