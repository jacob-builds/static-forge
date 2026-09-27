import unittest
from extract_markdown import extract_markdown_images, extract_markdown_links

class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual(
            [("image", "https://i.imgur.com/zjjcJKZ.png")],
            matches
        )

    def test_extract_multiple_images(self):
        text = (
            "![one](url1) and ![two](url2)"
        )
        matches = extract_markdown_images(text)
        self.assertListEqual(
            [("one", "url1"), ("two", "url2")],
            matches
        )

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "Go to [Boot.dev](https://www.boot.dev)"
        )
        self.assertListEqual(
            [("Boot.dev", "https://www.boot.dev")],
            matches
        )

    def test_extract_multiple_links(self):
        text = (
            "[one](url1) and [two](url2)"
        )
        matches = extract_markdown_links(text)
        self.assertListEqual(
            [("one", "url1"), ("two", "url2")],
            matches
        )

    def test_links_do_not_match_images(self):
        text = "![img](url) and [link](url2)"
        matches = extract_markdown_links(text)
        self.assertListEqual(
            [("link", "url2")],
            matches
        )
