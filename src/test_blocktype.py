import unittest
import blocktype

def test_heading_block(self):
    self.assertEqual(
        block_to_block_type("# Heading"),
        BlockType.HEADING,
    )

def test_code_block(self):
    block = "```\nprint('hello')\n```"

    self.assertEqual(
        block_to_block_type(block),
        BlockType.CODE,
    )

def test_quote_block(self):
    block = "> line one\n> line two"

    self.assertEqual(
        block_to_block_type(block),
        BlockType.QUOTE,
    )

def test_unordered_list_block(self):
    block = "- item 1\n- item 2\n- item 3"

    self.assertEqual(
        block_to_block_type(block),
        BlockType.UNORDERED_LIST,
    )

def test_ordered_list_block(self):
    block = "1. first\n2. second\n3. third"

    self.assertEqual(
        block_to_block_type(block),
        BlockType.ORDERED_LIST,
    )

def test_paragraph_block(self):
    block = "Just a normal paragraph."

    self.assertEqual(
        block_to_block_type(block),
        BlockType.PARAGRAPH,
    )


