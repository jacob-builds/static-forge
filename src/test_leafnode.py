import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://google.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://google.com">Click me!</a>'
        )

    def test_leaf_raw_text(self):
        node = LeafNode(None, "Just text")
        self.assertEqual(node.to_html(), "Just text")

    def test_leaf_missing_value(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None)

    def test_leaf_repr(self):
        node = LeafNode("span", "hi", {"class": "bold"})
        self.assertEqual(
            repr(node),
            "LeafNode(tag=span, value=hi, props={'class': 'bold'})"
        )
