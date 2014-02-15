import sys

try:
    from html.parser import HTMLParser, HTMLParseError
except ImportError:
    from  HTMLParser import HTMLParser, HTMLParseError
import logging
import re

from sphinx import addnodes
from docutils.nodes import emphasis, reference, Text
from docutils.parsers.rst.roles import set_classes


class Link(dict):

    '''Minimal nested link representation.'''

    def __init__(self, *args, **kwds):
        default = {'href': None, 'text': None, 'current': False,
                   'depth': None, 'childs': []}
        default.update(kwds)
        self.update(*args, **default)


class ParseLinks(HTMLParser):

    '''Parses sphinx's toctree html output into a list of nested Link
    objects, to simplify the bootstrap stuff inside Jinja templates.'''

    def __init__(self):
        self.logger = logging.getLogger("%s.%s" %
                (__name__, self.__class__.__name__))
        HTMLParser.__init__(self)

        self.depth = 0
        self.tag_stack = []
        self.links = []
        self.current = False
        self._tag = None
        self._tmp = None
        self._dataq = ""

    def handle_starttag(self, tag, attrs):
        if tag == 'ul':
            self.logger.debug("adding %s to tag_stack" % tag)
            self.tag_stack.append(tag)
            self.depth += 1

        if tag == 'li':
            self.logger.debug("adding %s to tag_stack" % tag)
            self.tag_stack.append(tag)
            for name, value in attrs:
                if name == 'class' and 'toctree-l' in value:
                    classes = value.split()
                    self.depth = int(classes[0].replace('toctree-l', ''))
                    if 'current' in classes:
                        self.current = True
                    else:
                        self.current = False
        if tag == 'a':
            self.logger.debug("adding %s to tag_stack" % tag)
            self.tag_stack.append(tag)
            self._tag = tag
            for name, value in attrs:
                if name == 'href':
                    href = value
            self._tmp = (Link(href=href, depth=self.depth,
                              current=self.current))

    def handle_data(self, data):
        if self._tag == 'a':
            data = " ".join(data.split())
            self.logger.debug("handle 'a tag' data: %s" % data)
            if self._tmp['text'] is None:
                seen = False
                self._tmp['text'] = data
            else:
                seen = True
                self._tmp['text'] += " " + data
            if not seen:
                if self._tmp['depth'] > 1:
                    links = self.links
                    loop = 0

                    for pos in range(self._tmp['depth']):
                        if loop == 0:
                            links = links[-1:]
                        else:
                            links = links[-1:][0]['childs']
                        loop += 1
                    links.append(self._tmp)
                else:
                    self.links.append(self._tmp)

    def handle_endtag(self, tag):
        try:
            if tag in ["li", "a"] and tag == self.tag_stack[-1:][0]:
                self.logger.debug("poping %s from stack" % tag)
                self.tag_stack.pop()
            self._tag = None
            if tag == 'ul' and tag == self.tag_stack[-1:][0]:
                self.tag_stack.pop()
                self.depth -= 1
        except IndexError:
            raise HTMLParseError('Unbalanced html tags.')


def html_page_context(app, pagename, templatename, context, doctree):
    """ Handler for the html-page-context signal, adds a raw_toctree function
    to the context."""

    def raw_toctree(collapse=False):
        return build_raw_toctree(app.builder, pagename, prune=False,
                                 collapse=collapse)

    def raw_localtoc(collapse=False):
        self_toc = app.builder.env.get_toc_for(pagename, app.builder)
        toc = app.builder.render_partial(self_toc)['fragment']
        pl = ParseLinks()
        pl.feed(toc)
        try:
            index = pl.links[0]
            childs = list(index['childs'])
            index['childs'] = []
            childs.insert(0, index)
            return childs
        except IndexError:
            return []

    context['raw_toctree'] = raw_toctree
    context['raw_localtoc'] = raw_localtoc


def build_raw_toctree(builder, docname, prune, collapse):
    """ Returns a list of nested Link objects representing the toctree."""
    env = builder.env
    doctree = env.get_doctree(env.config.master_doc)
    toctrees = []
    for toctreenode in doctree.traverse(addnodes.toctree):
        toctree = env.resolve_toctree(docname, builder, toctreenode,
                                      prune=prune, collapse=collapse, 
                                      includehidden=True)
        toctrees.append(toctree)
    if not toctrees:
        return None
    retv = toctrees[0]
    for toctree in toctrees[1:]:
        if toctree:
            retv.extend(toctree.children)
    pl = ParseLinks()
    pl.feed(builder.render_partial(retv)['fragment'])

    return pl.links


def icon_role(role, rawtext, text, lineno, inliner, options={}, content=[]):

    options.update({'classes': ["icon-" + x for x in text.split(",")]})
    options['classes'].append('icon-holder')
    set_classes(options)
    node = emphasis(**options)
    return [node], []


def btn_role(role, rawtext, text, lineno, inliner, options={}, content=[]):

    m = re.match(r'(.*)\<(.*)\>(,.*){0,}', text)
    if m:
        name, ref, classes = m.groups()
        if ref is '':
            msg = inliner.reporter.error('The ref portion of the btn role'
                                         ' cannot be none')
            prb = inliner.problematic(rawtext, rawtext, msg)
            return [prb], [msg]

        ref_cls = []
        em_cls = []
        if classes:
            cls = classes.strip(',').split(',')
            em_cls = [x for x in cls if x.startswith("icon-")]
            ref_cls = [x for x in cls if not x.startswith("icon-")]
            if 'btn' not in ref_cls:
                ref_cls.append('btn')
            options.update({'classes': ref_cls})


        set_classes(options)
        node = reference(rawtext, name, refuri=ref, **options)
        if len(em_cls) > 0:
            em_cls.append('icon-holder')
            em_opts = {'classes': em_cls}
            set_classes(em_opts)
            node.insert(0, emphasis(**em_opts))
            node.insert(1, Text(" "))

        return [node], []


def setup(app): # pragma: no cover
    app.info('Adding the icon role')
    app.add_role('icon', icon_role)
    app.info('Adding the btn role')
    app.add_role('btn', btn_role)
    app.info('Adding the raw_toctree Jinja function.')
    app.connect('html-page-context', html_page_context)
    return
