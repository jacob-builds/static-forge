import os
from pathlib import Path
from generate_page import generate_page

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath="/"):
    for entry in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, entry)
        dest_path = os.path.join(dest_dir_path, entry)

        if os.path.isfile(from_path):
            if entry.endswith(".md"):
                dest_html_path = Path(dest_path).with_suffix(".html")
                generate_page(from_path, template_path, dest_html_path, basepath)

        else:
            os.makedirs(dest_path, exist_ok=True)
            generate_pages_recursive(from_path, template_path, dest_path, basepath)


