from openpack.basepack import Part

class HeaderPart(Part):
	content_type = "application/vnd.openxmlformats-officedocument.wordprocessingml.header+xml"
	rel_type = "http://schemas.openxmlformats.org/officeDocument/2006/relationships/header"
	default_name = '/word/header.xml'

	def __init__(self, package, name=None, growth_hint=None, data=None):
		Part.__init__(self, package, name or self.default_name, growth_hint, data)

class FooterPart(Part):
	content_type = "application/vnd.openxmlformats-officedocument.wordprocessingml.footer+xml"
	rel_type = "http://schemas.openxmlformats.org/officeDocument/2006/relationships/footer"
	default_name = '/word/footer.xml'

	def __init__(self, package, name=None, growth_hint=None, data=None):
		Part.__init__(self, package, name or self.default_name, growth_hint, data)

