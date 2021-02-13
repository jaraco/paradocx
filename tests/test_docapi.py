"""Test the sample.docx provided by ooxmldeveloper.org."""

import io

from paradocx import Document


def test_add_paragraph():
    doc = Document()
    assert not doc.paragraphs
    doc.paragraph('Hello World!')
    assert doc.paragraphs


def test_add_table(table_data):
    doc = Document()
    doc.table(table_data)


def test_save():
    doc = Document()
    stream = io.BytesIO()
    doc._store(stream)
    assert stream.tell() > 0


def test_read_paragraph(writable_filename):
    doc = Document()
    doc.paragraph('Hello World!')
    doc.save(writable_filename)
    doc = Document.from_file(writable_filename)
    assert b'Hello World' in doc.start_part.dump()


def test_read_table(table_data, writable_filename):
    doc = Document()
    doc.table(table_data)
    doc.save(writable_filename)
    doc = Document.from_file(writable_filename)
    assert b'Christian' in doc.start_part.dump()
