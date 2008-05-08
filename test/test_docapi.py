"""Test the sample.docx provided by ooxmldeveloper.org."""

import os
import py.test
import common

from paradocx.package import WordPackage
from paradocx.document import WordDocument
from paradocx.styles import StylesPart

here = os.path.abspath(os.path.dirname(__file__))

class TestDocAPI(object):
	filepath = os.path.join(here, 'resources/apiout.docx')
	def setup_class(cls):
		cls.package = WordPackage(cls.filepath)
		cls.document = cls.package.start_part

	def test_add_paragraph(self):
		assert not self.document.paragraphs
		p = self.document.paragraph('Hello World!')
		assert self.document.paragraphs
	
	def test_add_table(self):
		data = [
			['Name', 'Age'],
			['Christian', 29],
			['Sarah', 28],
			['Curtis', 4],
			['Eli', 2],
		]
		t = self.document.table(data)

	def test_save(self):
		self.package.save()
		self.document = None
		self.package = None
	
	def test_open_generated(self):
		self.package = WordPackage(self.filepath)
		self.document = self.package.start_part
		self.doctext = self.document.fp.read()
	
	def test_read_paragraph(self):
		assert 'Hello World' in self.doctext

	def test_read_table(self):
		assert 'Christian' in self.doctext

	def teardown_class(cls):
		os.remove(cls.filepath)

