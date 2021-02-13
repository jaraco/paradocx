"""Test the sample.docx provided by ooxmldeveloper.org."""

import os
import posixpath
import random
import hashlib

from paradocx.package import WordPackage
from paradocx.document import DocumentPart
from paradocx.styles import StylesPart, Style
from paradocx.util import dcterms


def test_open(sample_stream):
    pkg = WordPackage.from_stream(sample_stream)
    assert not hasattr(pkg, 'filename')


def test_open_file(sample_filename):
    pkg = WordPackage.from_file(sample_filename)
    assert pkg.filename == sample_filename


def test_start_part(sample_stream):
    pkg = WordPackage.from_stream(sample_stream)
    assert isinstance(pkg.start_part, DocumentPart)
    assert pkg.start_part.name == '/word/document.xml'
    assert pkg.start_part.name in pkg


def test_create_empty_styles():
    StylesPart(None)


def test_styles(sample_stream):
    pkg = WordPackage.from_stream(sample_stream)
    styles_path = posixpath.join('/word', 'styles.xml')
    assert styles_path in pkg.keys()
    srel = pkg.start_part.related(StylesPart.rel_type)[0]
    assert srel == pkg[styles_path]


def test_core_props(sample_stream):
    pkg = WordPackage.from_stream(sample_stream)
    assert pkg.core_properties
    assert id(pkg.core_properties.element.find(dcterms['modified']))


def test_style_class(sample_stream):
    pkg = WordPackage.from_stream(sample_stream)
    styles_part = pkg['/word/styles.xml']
    styles = styles_part.get_styles()
    assert len(styles)
    assert all(isinstance(style, Style) for style in styles)
    assert len(styles) == len(set(style.id for style in styles))
    style_names = [style.name for style in styles]
    assert len(set(style_names)) == len(styles)


def test_replace_style_id(sample_stream):
    pkg = WordPackage.from_stream(sample_stream)
    styles_part = pkg['/word/styles.xml']
    styles_part.replace_style_id('DefaultParagraphFont', 'NewId')
    # header char is based on the default paragraph font
    header_char = styles_part.get_style_by_id('HeaderChar')
    assert header_char.based_on_id == 'NewId'


def test_replace_styles_by_name(sample_stream):
    pkg = WordPackage.from_stream(sample_stream)
    orig_styles_part = pkg['/word/styles.xml']
    new_styles_part = StylesPart(None, '/who/cares', data=orig_styles_part.dump())
    # change an id in the "new" styles
    style = random.choice(new_styles_part.get_styles())
    random_bytes = os.urandom(100)
    new_id = hashlib.md5(random_bytes).hexdigest()
    orig_style_id, style.id = style.id, new_id
    style_name = style.name
    # tag the element, so we're sure it gets copied to the orig styles
    style.attrib['tag'] = 'test-replace-styles'
    orig_styles_part.replace_styles(new_styles_part)
    assert new_id not in (style.id for style in orig_styles_part.get_styles())
    assert style_name in (style.name for style in orig_styles_part.get_styles())
    style = orig_styles_part.get_style_by_id(orig_style_id)
    assert b'test-replace-styles' in orig_styles_part.dump()
