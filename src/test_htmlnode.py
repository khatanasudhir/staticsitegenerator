# test_htmlnode.py

import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_props_to_html_with_props(self):
        # Test with props
        node = HTMLNode(tag="a", props={"href": "https://www.google.com", "target": "_blank"})
        expected_props = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected_props)

    def test_props_to_html_without_props(self):
        # Test without props (should return an empty string)
        node = HTMLNode(tag="p", value="Some text")
        expected_props = ""
        self.assertEqual(node.props_to_html(), expected_props)

    def test_props_to_html_with_empty_props(self):
        # Test with empty props dictionary
        node = HTMLNode(tag="div", props={})
        expected_props = ""
        self.assertEqual(node.props_to_html(), expected_props)

    def test_repr_method(self):
        # Test __repr__ method
        node = HTMLNode(tag="a", value="Click here", props={"href": "https://www.google.com"})
        expected_repr = "HTMLNode(tag='a', value='Click here', children=[], props={'href': 'https://www.google.com'})"
        self.assertEqual(repr(node), expected_repr)

if __name__ == "__main__":
    unittest.main()
