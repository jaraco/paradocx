"""Test the sample.docx provided by ooxmldeveloper.org."""

import posixpath

from paradocx.package import WordPackage
from paradocx.document import DocumentPart
from paradocx.styles import StylesPart
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
