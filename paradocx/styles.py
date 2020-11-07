from lxml import etree

from openpack.basepack import DefaultNamed, Part
from .util import docx_namespaces

style_ns = docx_namespaces['w']
STYLES = '{%s}' % style_ns


class StylesPart(DefaultNamed, Part):
    content_type = (
        "application/" "vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"
    )
    rel_type = (
        "http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles"
    )
    default_name = '/word/styles.xml'

    def load(self, xml):
        lookup = etree.ElementNamespaceClassLookup()
        parser = etree.XMLParser()
        parser.set_element_class_lookup(lookup)
        namespace = lookup.get_namespace(style_ns)
        namespace.update(dict(style=Style))
        self._data = etree.fromstring(xml, parser=parser)

    data = property(lambda self: self._data, load)

    def get_styles(self):
        return self._data.findall(STYLES + 'style')

    def replace_style_id(self, orig, repl):
        # replace all instances of a style id with another
        for style in self.get_styles():
            if style.id == orig:
                style.id = repl
            if style.based_on_id == orig:
                style.based_on_id = repl
            if style.next_id == orig:
                style.next_id = repl

    def replace_styles(self, other):
        """
        Replace all of the styles in self with all of the styles in
        the other StylesPart, but reuse style IDs from the self for any
        styles with the same name.
        """
        self_style_ids = dict((style.name, style.id) for style in self.get_styles())
        for style in other.get_styles():
            if style.name in self_style_ids:
                orig_style_id = style.id
                repl_style_id = self_style_ids[style.name]
                other.replace_style_id(orig_style_id, repl_style_id)
        self._data = other._data
        # todo: make sure there are no duplicate IDs

    def get_style_by_id(self, id):
        styles = dict((style.id, style) for style in self.get_styles())
        return styles[id]


class Style(etree.ElementBase):
    def _get_id(self):
        return self.attrib[STYLES + 'styleId']

    def _set_id(self, id):
        self.attrib[STYLES + 'styleId'] = id

    id = property(_get_id, _set_id)

    @property
    def name(self):
        return self.find(STYLES + 'name').attrib[STYLES + 'val']

    def _get_based_on_id(self):
        node = self.find(STYLES + 'basedOn')
        if node is not None:
            return node.attrib[STYLES + 'val']

    def _set_based_on_id(self, id):
        self.find(STYLES + 'basedOn').attrib[STYLES + 'val'] = id

    based_on_id = property(_get_based_on_id, _set_based_on_id)

    def _get_next_id(self):
        node = self.find(STYLES + 'next')
        if node is not None:
            return node.attrib[STYLES + 'val']

    def _set_next_id(self, id):
        self.find(STYLES + 'next').attrib[STYLES + 'val'] = id

    next_id = property(_get_next_id, _set_next_id)
