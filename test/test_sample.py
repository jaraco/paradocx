"""Test the sample.docx provided by ooxmldeveloper.org."""

import posixpath
import py.test

from paradocx.package import WordPackage
from paradocx.document import DocumentPart
from paradocx.styles import StylesPart
from paradocx.util import dcterms

from common import get_resource_filename as res

class TestPackageReading(object):
	def setup_class(cls):
		cls.package = WordPackage(res('sample.docx'))

	def test_open(self):
		assert self.package.name == res('sample.docx')
	
	def test_start_part(self):
		assert isinstance(self.package.start_part, DocumentPart)
		assert self.package.start_part.name == '/word/document.xml'
		assert self.package.start_part.name in self.package
	
	def test_styles(self):
		styles_path = posixpath.join('/word', 'styles.xml')
		assert styles_path in self.package.keys()
		srel = self.package.start_part.related(StylesPart.rel_type)[0]
		assert srel == self.package[styles_path]
	
	def test_core_props(self):
		assert self.package.core_properties
		assert id(self.package.core_properties.element.find(dcterms['modified']))

