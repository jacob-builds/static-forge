from textnode import TextNode, TextType
from extract_markdown import extract_markdown_images, extract_markdown_links

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
             new_nodes.append(node)
             continue

        text = node.text
        images = extract_markdown_images(text)

        if not images:
            new_nodes.append(node)
            continue
        for alt, url in images:
            markdown = f"![{alt}]({url})"
            before, after = text.split(markdown, 1)
            if before:
                new_nodes.append(TextNode(before, TextType.TEXT))
            new_nodes.append(TextNode(alt, TextType.IMAGE, url))
            text = after
        if text:
            new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        links = extract_markdown_links(text)

        if not links:
            new_nodes.append(node)
            continue

        for anchor, url in links:
            markdown = f"[{anchor}]({url})"
            before, after = text.split(markdown, 1)
            if before:
                new_nodes.append(TextNode(before, TextType.LINK))
            new_nodes.append(TextNode(anchor, TextType.LINK, url))
            text = after
        if text:
            new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes


