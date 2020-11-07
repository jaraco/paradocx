from lxml.etree import fromstring, tostring
from lxml import builder

from openpack.basepack import ooxml_namespaces

docx_namespaces = {
    'w': "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
    'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
    've': 'http://schemas.openxmlformats.org/markup-compatibility/2006',
    'wp': ('http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing'),
    'v': 'urn:schemas-microsoft-com:vml',
}
docx_namespaces.update(ooxml_namespaces)


def expand_namespace(tag):
    """
    >>> expand_namespace('w:document')
    '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}document'
    """
    namespace, sep, tag = tag.rpartition(':')
    fmt = '{%(namespace)s}%(tag)s' if namespace else '%(tag)s'
    namespace = docx_namespaces[namespace]
    return fmt % vars()


class ElementMaker(builder.ElementMaker):
    def __getitem__(self, name):
        return "%s%s" % (self._namespace, name)


w = ElementMaker(namespace=docx_namespaces['w'], nsmap=docx_namespaces)
dcterms = ElementMaker(namespace=docx_namespaces['dcterms'], nsmap=docx_namespaces)


class TemplateSource(object):
    template = None

    def __init__(self, variables, encoding='utf-8'):
        self.variables = variables
        self.xml = self._from_template()
        self.element = self._to_element()

    def _from_template(self):
        """Use self.template and self.variables to generate XML content."""
        raise NotImplementedError

    def _to_element(self):
        return fromstring(self.xml)

    def __str__(self):
        return tostring(self.element, encoding=self.encoding)
