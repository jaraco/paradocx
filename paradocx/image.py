from openpack.basepack import DefaultNamed, Part

class ImagePart(DefaultNamed, Part):
	content_type = 'image/jpeg'
	rel_type = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships/image'
	default_name = '/word/media/image.jpeg'
