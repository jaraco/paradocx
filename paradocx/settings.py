from openpack.basepack import Part

class SettingsPart(Part):
	content_type = 'application/vnd.openxmlformats-officedocument.wordprocessingml.settings+xml'
	rel_type = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships/settings'
	default_name = '/word/settings.xml'

	def __init__(self, package, name=None, growth_hint=None, fp=None):
		Part.__init__(self, package, name or self.default_name, growth_hint, fp)


