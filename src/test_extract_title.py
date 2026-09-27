import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extract_title_basic(self):
        md = "# Hello"
        self.assertEqual(extract_title(md), "Hello")

    def test_extract_title_with_whitespace(self):
        md = "#    Tolkien Fan Club   "
        self.assertEqual(extract_title(md), "Tolkien Fan Club")

    def test_extract_title_multiline(self):
        md = """
Some introductory text.

# Main Header Title

Some more text.
"""
        self.assertEqual(extract_title(md), "Main Header Title")

    def test_extract_title_no_h1_raises_exception(self):
        md = "## Subheader only\nNo h1 here."
        with self.assertRaises(Exception):
            extract_title(md)

if __name__ == "__main__":
    unittest.main()
