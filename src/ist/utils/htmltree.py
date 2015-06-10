# encoding: utf-8
# author:   Jan Hybs
import cgi

import xml.etree.ElementTree as ET


class htmltree(object):
    def __init__(self, tag_name='div', cls='', *args, **kwargs):
        self.attrib = { 'class': cls } if cls else { }
        self.tag_name = tag_name
        self.root = ET.Element(tag_name, self.attrib)
        self.counter = 0
        self.roots = [self.root]

    def tag(self, tag_name, value='', attrib={ }):
        element = ET.Element(tag_name, attrib)
        element.text = cgi.escape(value)
        self.current().append(element)
        return element

    def current(self):
        return self.roots[self.counter]

    def add(self, element):
        return self.current().append(element)

    def h1(self, value='', attrib={ }):
        return self.tag('h1', value, attrib)

    def h2(self, value='', attrib={ }):
        return self.tag('h2', value, attrib)

    def h3(self, value='', attrib={ }):
        return self.tag('h3', value, attrib)

    def h4(self, value='', attrib={ }):
        return self.tag('h4', value, attrib)

    def h5(self, value='', attrib={ }):
        return self.tag('h5', value, attrib)

    def h6(self, value='', attrib={ }):
        return self.tag('h6', value, attrib)

    def ul(self, value='', attrib={ }):
        return self.tag('ul', value, attrib)

    def ol(self, value='', attrib={ }):
        return self.tag('ol', value, attrib)

    def span(self, value='', attrib={ }):
        return self.tag('span', value, attrib)

    def div(self, value='', attrib={ }):
        return self.tag('div', value, attrib)

    def bold(self, value='', attrib={ }):
        return self.tag('strong', value, attrib)

    def italic(self, value='', attrib={ }):
        return self.tag('em', value, attrib)

    def li(self, value='', attrib={ }):
        return self.tag('li', value, attrib)

    def href(self, href, value=''):
        return self.tag('a', value if value else href, { 'href': href })

    def open(self, tag_name, value='', attrib={ }):
        element = self.tag(tag_name, value, attrib)
        self.roots.append(element)
        return self

    def description(self, value):
        return self.tag('div', value, { 'class': 'description' })

    def __enter__(self):
        self.counter += 1
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        self.counter -= 1
        self.roots.pop()
        return self

    def dump(self):
        return ET.tostring(self.root)

    def __repr__(self):
        return '<htmltree object>'

    def style(self, location):
        self.tag('link', '', { 'rel': 'stylesheet', 'type': 'text/css', 'media': 'screen', 'href': location })


