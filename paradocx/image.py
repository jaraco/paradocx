from openpack.basepack import Part

class ImagePart(Part):
	content_type = 'image/jpeg'
	rel_type = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships/image'
	default_name = '/word/media/image.jpeg'

	def __init__(self, package, name=None, growth_hint=None, fp=None):
		Part.__init__(self, package, name or self.default_name, growth_hint, fp)


