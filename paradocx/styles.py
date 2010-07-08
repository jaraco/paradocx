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

	def get_styles(self):
		return self._data.findall(STYLES+'style')

	

	def replace_styles(self, other):
		"""
		Replace all of the styles in self with all of the styles in
		the other StylesPart, but reuse style IDs from the self for any
		styles with the same name.
		"""
		self_style_ids = dict((style.name, style.id) for style in self.get_styles())
		for style in other.get_styles():
			style.id = self_style_ids.get(style.name, style.id)
		self._data = other._data
		# todo: make sure there are no duplicate IDs

	def get_style_by_id(self, id):
		styles = dict((style.id, style) for style in self.get_styles())
		return styles[id]

class Style(etree.ElementBase):
	def _get_id(self):
		return self.attrib[STYLES+'styleId']
	def _set_id(self, id):
		self.attrib[STYLES+'styleId'] = id
	id = property(_get_id, _set_id)

	@property
	def name(self):
		return self.find(STYLES+'name').attrib[STYLES+'val']
