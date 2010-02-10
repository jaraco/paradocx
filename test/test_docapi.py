"""Test the sample.docx provided by ooxmldeveloper.org."""

import os
import py.test
import common

from paradocx import Document, w
from paradocx.styles import StylesPart

here = os.path.abspath(os.path.dirname(__file__))

class TestDocAPI(object):
	filepath = os.path.join(here, 'resources/apiout.docx')
	def setup_class(cls):
		cls.document = Document(cls.filepath)

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
		self.document.save()
		self.document = None
	
	def test_read_paragraph(self):
		self.document = Document(self.filepath)
		self.doctext = self.document.data
		assert 'Hello World' in self.doctext

	def test_read_table(self):
		self.document = Document(self.filepath)
		self.doctext = self.document.data
		assert 'Christian' in self.doctext

	def teardown_class(cls):
		os.remove(cls.filepath)

