from openpack.basepack import Part

class StylesPart(Part):
	content_type = "application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"
	rel_type = "http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles"
	default_name = '/word/styles.xml'

	def __init__(self, package, name=None, growth_hint=None, data=None):
		Part.__init__(self, package, name or self.default_name, growth_hint, data)

