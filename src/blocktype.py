from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    #heading
    for i in range(1, 7):
        if block.startswith("#" * i + " "):
            return BlockType.HEADING

    #code
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE

    lines = block.split("\n")

    #quote
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE

    #unordered list
    if all(line.startswith("- ") or line.startswith("* ") for line in lines):
        return BlockType.UNORDERED_LIST

    #ordered list
    ordered = True

    for i, line in enumerate(lines, start=1):
        if not line.startswith(f"{i}. "):
            ordered = False
            break

    if ordered:
        return BlockType.ORDERED_LIST

    #default
    return BlockType.PARAGRAPH

