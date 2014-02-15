import sys, os

__pyver = sys.version_info[0] * 10 + sys.version_info[1]

if __pyver <= 26:
    import unittest2 as unittest
else:
    import unittest

if __pyver < 33: 
    import mock
else:
    from unittest import mock

from docutils.nodes import emphasis, reference
from sphinxtrap.ext.rawtoc import Link, ParseLinks, icon_role, btn_role
from sphinxtrap.ext.rawtoc import build_raw_toctree, html_page_context


def resolve_doctree(*args, **kwargs):
    '''Emulates sphinx/docutils render_partial'''

    path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(path, "test.html")) as fp:
        html = fp.read()
    return html


#Mocking sphinx's stuff
doctree = mock.Mock()
doctree.traverse.side_effect = lambda x: ['index']

builder = mock.Mock()
builder.env.get_doctree.side_effect = lambda x: doctree
builder.env.resolve_doctree.side_effect = resolve_doctree
builder.render_partial.side_effect = lambda x: {'fragment':resolve_doctree()}


inliner = mock.Mock()
inliner.problematic= mock.Mock()
inliner.reporter= mock.Mock()
inliner.reporter.error = mock.Mock()

class TestSphinxtrap(unittest.TestCase):

    def test_node(self):
        lk = Link(text="gabbagabbahey", href="https://foo.com")
        lk2 = Link(text="gabbagabbahey", href="https://foo.com", depth=1)
        lk["childs"].append(lk2)
        self.assertEqual(lk['childs'][0].get("current"), False)
        self.assertEqual(lk['href'], "https://foo.com")

    def test_parser(self):
        pl = ParseLinks()
        path = os.path.dirname(os.path.realpath(__file__))
        with open(os.path.join(path, "test.html")) as fp:
            pl.feed(fp.read())
        self.assertEqual(pl.links[7]['childs'][0]['href'],
                "#compression-algorithms")
    
    def test_build_raw_toctree(self):
        links = build_raw_toctree(builder, "test", False, False)
        self.assertEqual(links[7]['childs'][0]['href'],
                "#compression-algorithms")

    def test_icon_role(self):
        icon = icon_role("foo", ":icon:`foo`", "foo", 100,
                inliner, options={'classes':[]}, content=[])
        self.assertTrue(isinstance(icon[0][0], emphasis ))

    def test_btn_role(self):
        l_str = ":btn:`Foo <http://foo.org/>,btn-success,icon-globe`"
        btn = btn_role("foo", l_str, l_str, 100, inliner,
                options={'classes':[]}) 
        self.assertTrue(isinstance(btn[0][0], reference))


    def test_html_page_context(self):
        global context
        context = {}
        app = mock.Mock()
        app.builder = builder
        html_page_context(app, 'index', 'foo', context, None)
        local = context['raw_toctree']()
        toc = context['raw_localtoc']()
        self.assertFalse(toc[0]['current'])
        self.assertFalse(local[0]['current'])
