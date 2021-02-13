"""
Tests for paradocx.image
"""

from __future__ import with_statement

import mimetypes
import warnings
import pytest

from paradocx.image import ImagePart


def test_content_types():
    part = ImagePart(None, '/word/media/foo.jpg')
    jpeg_types = ('image/jpeg', 'image/pjpeg')
    assert part.content_type in jpeg_types
    part = ImagePart(None, '/word/media/bar.jpeg')
    assert part.content_type in jpeg_types
    with pytest.warns(UserWarning):
        part = ImagePart(None, '/foo/bar/strange eps file.eps')
    assert part.content_type == 'application/postscript'
    part = ImagePart(None, '/name without extension')
    assert part.content_type is None
    part = ImagePart(None)
    assert part.content_type == mimetypes.guess_type(part.name)[0]


def test_set_content_type():
    # if the content_type is set, setting .name shouldn't reset it
    part = ImagePart(None)
    part.content_type = 'image/png'
    part.name = '/foo.jpeg'
    assert part.content_type == 'image/png'


def test_interoperability_warning():
    with warnings.catch_warnings(record=True) as w:
        # Cause all warnings to always be triggered.
        warnings.simplefilter("always")
        # Trigger interoperability warning
        ImagePart(None, '/foo/bar/some_unsupported_format.gif')
        # Verify the warning
        assert len(w) == 1
        assert issubclass(w[-1].category, UserWarning)
        msg = str(w[-1].message)
        assert "image/gif" in msg and "not" in msg and "interoperable" in msg
