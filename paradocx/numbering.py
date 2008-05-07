from openpack.basepack import Part

class NumberingPart(Part):
	content_type = 'application/vnd.openxmlformats-officedocument.wordprocessingml.numbering+xml'
	rel_type = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships/numbering'
	default_name = '/word/numbering.xml'

	def __init__(self, package, name=None, growth_hint=None, fp=None):
		Part.__init__(self, package, name or self.default_name, growth_hint, fp)

class AbstractNumbering(object):
	def __init__(self, id, **props):
		self.id = id
		self.properties = properties

class Numbering(object):
	pass



