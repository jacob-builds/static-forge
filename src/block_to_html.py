from markdown_to_block import markdown_to_block
from textnode import *
from htmlnode import *
from parentnode import *
from leafnode import *
from blocktype import *
from text_to_textnodes import *

def text_to_children(text):
    """Converts a raw string with inline markdown into a list of HTMLNodes."""
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        children.append(text_node_to_html_node(text_node))
    return children


def markdown_to_html_node(markdown):
    blocks = markdown_to_block(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children)


def block_to_html_node(block):
    block_type = block_to_block_type(block)

    # Note: Handle both String literals and Enum members depending on your blocktype implementation
    if block_type in (BlockType.PARAGRAPH, "paragraph"):
        return paragraph_to_html_node(block)
    if block_type in (BlockType.HEADING, "heading"):
        return heading_to_html_node(block)
    if block_type in (BlockType.CODE, "code"):
        return code_to_html_node(block)
    if block_type in (BlockType.QUOTE, "quote"):
        return quote_to_html_node(block)
    if block_type in (BlockType.UNORDERED_LIST, "unordered_list"):
        return ulist_to_html_node(block)
    if block_type in (BlockType.ORDERED_LIST, "ordered_list"):
        return olist_to_html_node(block)

    raise ValueError(f"Invalid block type: {block_type}")


# --- Block Converters ---

def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph_text = " ".join(lines)
    children = text_to_children(paragraph_text)
    return ParentNode("p", children)


def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break

    # Strip the leading '#... ' characters
    text = block[level + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)


def code_to_html_node(block):
    # Strip opening and closing ``` tags
    text = block[3:-3].lstrip("\n")

    # Do NOT parse inline markdown for code blocks
    text_node = TextNode(text, TextType.TEXT)
    code_leaf = text_node_to_html_node(text_node)
    code_parent = ParentNode("code", [code_leaf])
    return ParentNode("pre", [code_parent])


def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if line.startswith(">"):
            new_lines.append(line[1:].strip())
        else:
            new_lines.append(line.strip())

    quote_text = " ".join(new_lines)
    children = text_to_children(quote_text)
    return ParentNode("blockquote", children)


def ulist_to_html_node(block):
    lines = block.split("\n")
    li_nodes = []
    for line in lines:
        # Strip '- ' or '* '
        text = line[2:]
        children = text_to_children(text)
        li_nodes.append(ParentNode("li", children))
    return ParentNode("ul", li_nodes)


def olist_to_html_node(block):
    lines = block.split("\n")
    li_nodes = []
    for line in lines:
        # Strip '1. ', '2. ', etc.
        text = line.split(". ", 1)[1]
        children = text_to_children(text)
        li_nodes.append(ParentNode("li", children))
    return ParentNode("ol", li_nodes)




