"""Test the sample.docx provided by ooxmldeveloper.org."""

from paradocx import Document, w
from paradocx.styles import StylesPart

class TestDocAPI(object):
	filepath = res('apiout.docx')
	def setup_method(self, method):
		self.document = Document.from_file(self.filepath)

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
		self.test_add_paragraph()
		self.test_save()
		document = Document(self.filepath)
		doctext = document.data
		assert 'Hello World' in doctext

	def test_read_table(self):
		self.test_add_table()
		self.test_save()
		document = Document(self.filepath)
		doctext = document.data
		assert 'Christian' in doctext
