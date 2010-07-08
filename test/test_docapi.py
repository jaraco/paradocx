"""Test the sample.docx provided by ooxmldeveloper.org."""

from StringIO import StringIO

from paradocx import Document, w
from paradocx.styles import StylesPart

def test_add_paragraph():
	doc = Document()
	assert not doc.paragraphs
	p = doc.paragraph('Hello World!')
	assert doc.paragraphs

def test_add_table(table_data):
	doc = Document()
	t = doc.table(table_data)

def test_save():
	doc = Document()
	stream = StringIO()
	doc._store(stream)
	assert stream.tell() > 0

def test_read_paragraph(writable_filename):
	doc = Document()
	p = doc.paragraph('Hello World!')
	doc.save(writable_filename)
	doc = Document.from_file(writable_filename)
	assert 'Hello World' in doc.start_part.dump()

def test_read_table(table_data, writable_filename):
	doc = Document()
	t = doc.table(table_data)
	doc.save(writable_filename)
	doc = Document.from_file(writable_filename)
	assert 'Christian' in doc.start_part.dump()
