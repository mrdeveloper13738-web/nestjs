import os
import markdown

input_dir = "content"
output_dir = "build_html"

os.makedirs(output_dir, exist_ok=True)

for root, _, files in os.walk(input_dir):
    for file in files:
        if file.endswith(".md"):
            full_path = os.path.join(root, file)

            with open(full_path, "r", encoding="utf-8") as f:
                text = f.read()

            html = markdown.markdown(text)

            output_file = os.path.join(
                output_dir,
                file.replace(".md", ".html")
            )

            with open(output_file, "w", encoding="utf-8") as f:
                f.write(html)

print("Markdown conversion done")
