
def markdown_to_block(markdown):
    blocks = markdown.split("\n\n")
    return [block.strip() for block in blocks if block.strip() != ""]
