import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_multiple_children(self):
        children = [
            LeafNode("b", "Bold"),
            LeafNode(None, " text "),
            LeafNode("i", "italic"),
        ]
        parent = ParentNode("p", children)
        self.assertEqual(
            parent.to_html(),
            "<p><b>Bold</b> text <i>italic</i></p>"
        )

    def test_nested_parents(self):
        inner = ParentNode("section", [
            LeafNode("h1", "Title"),
            LeafNode("p", "Paragraph")
        ])
        outer = ParentNode("div", [inner])
        self.assertEqual(
            outer.to_html(),
            "<div><section><h1>Title</h1><p>Paragraph</p></section></div>"
        )

    def test_missing_tag(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("p", "hi")])

    def test_missing_children(self):
        with self.assertRaises(ValueError):
            ParentNode("div", None)
