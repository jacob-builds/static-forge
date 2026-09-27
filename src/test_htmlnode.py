import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_basic(self):
        node = HTMLNode(
            tag="a",
            value="Click me",
            props={"href": "https://google.com", "target": "_blank"}
        )
        self.assertEqual(
            node.props_to_html(),
            ' href="https://google.com" target="_blank"'
        )

    def test_props_to_html_empty(self):
        node = HTMLNode(tag="p", value="Hello", props=None)
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_single(self):
        node = HTMLNode(tag="img", props={"src": "image.png"})
        self.assertEqual(node.props_to_html(), ' src="image.png"')
