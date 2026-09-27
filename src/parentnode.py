from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if tag is None:
            raise ValueError("ParentNode must have a tag")
        if children is None:
            raise ValueError("ParentNode must have children")

        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        if self.children is None:
            raise ValueError("ParentNode must have children")
        inner_html = "".join(child.to_html() for child in self.children)
        props_str = self.props_to_html()
        return f"<{self.tag}{props_str}>{inner_html}</{self.tag}>"

    def __repr__(self):
        return (
            f"ParentNode(tag={self.tag}, "
            f"children={self.children}, "
            f"props={self.props})"
        )
