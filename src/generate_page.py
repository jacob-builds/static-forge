import os
from extract_title import extract_title
from block_to_html import markdown_to_html_node

def generate_page(from_path, template_path, dest_path, basepath="/"):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r", encoding="utf-8") as f:
        markdown_content = f.read()

    with open(template_path, "r", encoding="utf-8") as f:
        template_content = f.read()

    html_node = markdown_to_html_node(markdown_content)
    html_content = html_node.to_html()
    title = extract_title(markdown_content)
    full_html = template_content.replace("{{ Title }}", title)
    full_html = full_html.replace("{{ Content }}", html_content)
    full_html = full_html.replace('href="/', f'href="{basepath}')
    full_html = full_html.replace('src="/', f'src="{basepath}')
    dest_dir_path = os.path.dirname(dest_path)

    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)

    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(full_html)
