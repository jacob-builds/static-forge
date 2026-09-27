from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if value is None:
            raise ValueError("LeafNode musst have a value")
        super().__init__(tag=tag, value=value, children=None, props=props)
    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode musst have a value")
        if self.tag is None:
            return self.value
        props_str = self.props_to_html()
        return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"
    def __repr__(self):
        return (
            f"LeafNode(tag={self.tag}, "
            f"value={self.value}, "
            f"props={self.props})"
        )
