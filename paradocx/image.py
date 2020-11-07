from openpack.basepack import DefaultNamed, Part
import mimetypes
import warnings


class ImagePart(DefaultNamed, Part):
    rel_type = (
        'http://schemas.openxmlformats.org/officeDocument/2006/relationships/image'
    )
    default_name = '/word/media/image.jpeg'

    """
    ECMA-376 3nd Edition Part 1 Page 170 states:
    A producer that wants interoperability should use
    one of the following standard formats:
        - image/png ISO/IEC 15948:2003, http://www.libpng.org/pub/png/spec/
        - image/jpeg, http://www.w3.org/Graphics/JPEG
    """
    interoperability_types = ['image/png', 'image/jpeg']

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
            if ct not in self.interoperability_types:
                warnings.warn(
                    "Image type %s is not guaranteed to be interoperable" % ct
                )
