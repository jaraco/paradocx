from lxml.etree import Element
from lxml import builder
import re

from openpack.basepack import ooxml_namespaces

docx_namespaces = {
	'w' : "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
	'r' : 'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
	've' : 'http://schemas.openxmlformats.org/markup-compatibility/2006',
	'wp' : 'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing',
	'v' : 'urn:schemas-microsoft-com:vml',
}
docx_namespaces.update(ooxml_namespaces)

class ElementMaker(builder.ElementMaker):
	def __getitem__(self, name):
		return "%s%s" % (self._namespace, name)

w = ElementMaker(namespace=docx_namespaces['w'], nsmap=docx_namespaces)
dcterms = ElementMaker(namespace=docx_namespaces['dcterms'], nsmap=docx_namespaces)

