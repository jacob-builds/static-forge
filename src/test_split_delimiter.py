import unittest
from textnode import TextNode, TextType
from split_delimiter import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_bold(self):
        node = TextNode("Hello **world**!", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)

        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text, "Hello ")
        self.assertEqual(result[0].text_type, TextType.TEXT)

        self.assertEqual(result[1].text, "world")
        self.assertEqual(result[1].text_type, TextType.BOLD)

        self.assertEqual(result[2].text, "!")
        self.assertEqual(result[2].text_type, TextType.TEXT)

    def test_split_code(self):
        node = TextNode("Use `print()` here", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(result[1].text_type, TextType.CODE)
        self.assertEqual(result[1].text, "print()")

    def test_split_italic(self):
        node = TextNode("This is _cool_ stuff", TextType.TEXT)
        result = split_nodes_delimiter([node], "_", TextType.ITALIC)

        self.assertEqual(result[1].text_type, TextType.ITALIC)
        self.assertEqual(result[1].text, "cool")

    def test_no_split_non_text(self):
        node = TextNode("bold", TextType.BOLD)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(result[0], node)

    def test_missing_closing_delimiter(self):
        node = TextNode("This is **broken text", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "**", TextType.BOLD)
