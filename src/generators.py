from converters import markdown_to_html_node
from htmlnode import HTMLNode
from extractors import extract_title
from os import path, makedirs

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as f:
        from_content = f.read()
    with open(template_path, "r") as f:
        dest_html = f.read()
    from_html = markdown_to_html_node(from_content).to_html()
    from_title = extract_title(from_content)
    dest_html = dest_html.replace(r"{{ Title }}", from_title)
    dest_html = dest_html.replace(r"{{ Content }}", from_html)
    makedirs(path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(dest_html)
