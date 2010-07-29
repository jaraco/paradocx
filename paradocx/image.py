from openpack.basepack import DefaultNamed, Part
import mimetypes

class ImagePart(DefaultNamed, Part):
	rel_type = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships/image'
	default_name = '/word/media/image.jpeg'

	def _set_name(self, name):
		super(ImagePart, self)._set_name(name)
		self._guess_mime_type(name)
	name = property(Part._get_name, _set_name)

	def _guess_mime_type(self, name):
		"""
		When setting the name, guess the mime type from the extension.
		Set the content_type for this instance only if a content_type is not
		already defined (this allows an instance to have a content-type pre-
		defined or for a subclass to define the content type, and it will not
		be overridden by the guessed type).
		"""
		ct, _ = mimetypes.guess_type(name)
		if ct and not self.content_type:
			self.content_type = ct
