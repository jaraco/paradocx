"""Test the sample.docx provided by ooxmldeveloper.org."""

import os
import py.test
import common

from paradocx.package import WordPackage
from paradocx.document import WordDocument
from paradocx.styles import StylesPart
from paradocx.util import dcterms

here = os.path.abspath(os.path.dirname(__file__))

class TestPackageReading(object):
	def setup_class(cls):
		cls.package = WordPackage(os.path.join(here, 'resources/sample.docx'))

	def test_open(self):
		assert self.package.name == os.path.join(here, 'resources/sample.docx')
	
	def test_start_part(self):
		assert isinstance(self.package.start_part, WordDocument)
		assert self.package.start_part.name == '/word/document.xml'
		assert self.package.start_part.name in self.package
	
	def test_styles(self):
		assert '/word/styles.xml' in self.package
		srel = self.package.start_part.related(StylesPart.rel_type)[0]
		assert srel == self.package['/word/styles.xml']
	
	def test_core_props(self):
		assert self.package.core_properties
		assert id(self.package.core_properties.element.find(dcterms['modified']))

