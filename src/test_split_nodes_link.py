from split_nodes import split_nodes_link
from textnode import TextNode, TextType

def test_split_links(self):
    node = TextNode(
        "Go [here](https://a.com) or [there](https://b.com)",
        TextType.TEXT,
    )
    new_nodes = split_nodes_link([node])
    self.assertListEqual(
        [
            TextNode("Go ", TextType.TEXT),
            TextNode("here", TextType.LINK, "https://a.com"),
            TextNode(" or ", TextType.TEXT),
            TextNode("there", TextType.LINK, "https://b.com"),
        ],
        new_nodes,
    )

