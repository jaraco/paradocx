from lxml import etree

from openpack.basepack import DefaultNamed, Part

style_ns = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
STYLES = '{%s}' % style_ns

class StylesPart(DefaultNamed, Part):
	content_type = "application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"
	rel_type = "http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles"
	default_name = '/word/styles.xml'

	def load(self, xml):
		lookup = etree.ElementNamespaceClassLookup()
		parser = etree.XMLParser()
		parser.set_element_class_lookup(lookup)
		namespace = lookup.get_namespace(style_ns)
		namespace.update(dict(style=Style))
		self._data = etree.fromstring(xml, parser=parser)
	data = property(lambda self: self._data, load)

class Style(etree.ElementBase):
	@property
	def id(self):
		return self.attrib[STYLES+'styleId']

	@property
	def name(self):
		return self.find(STYLES+'name').attrib[STYLES+'val']