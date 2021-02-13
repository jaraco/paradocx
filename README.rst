.. image:: https://img.shields.io/pypi/v/paradocx.svg
   :target: `PyPI link`_

.. image:: https://img.shields.io/pypi/pyversions/paradocx.svg
   :target: `PyPI link`_

.. _PyPI link: https://pypi.org/project/paradocx

.. image:: https://github.com/jaraco/paradocx/workflows/tests/badge.svg
   :target: https://github.com/jaraco/paradocx/actions?query=workflow%3A%22tests%22
   :alt: tests

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Code style: Black

.. .. image:: https://readthedocs.org/projects/skeleton/badge/?version=latest
..    :target: https://skeleton.readthedocs.io/en/latest/?badge=latest

``paradocx`` builds on the Open Office XML Spec provided by openpack to
provide interfaces for working with Microsoft Word documents in the
Office 2007 'docx' format.

Introduction
============

Constructing simple documents using Paradocx is fairly straightforward::

    >>> import paradocx
    >>> doc = paradocx.Document()
    >>> doc.paragraph('Things to do', style='Heading 1')
    <Element {http://schemas.openxmlformats.org/wordprocessingml/2006/main}p at 0x22a1240>
    >>> doc.paragraph('First, spend some time learning paradocx usage.')
    <Element {http://schemas.openxmlformats.org/wordprocessingml/2006/main}p at 0x22a12d0>
    >>> doc.paragraph('Then, put together some examples')
    <Element {http://schemas.openxmlformats.org/wordprocessingml/2006/main}p at 0x22a1240>
    >>> doc.paragraph('Finally, put those examples in the paradocx documentation')
    <Element {http://schemas.openxmlformats.org/wordprocessingml/2006/main}p at 0x22a12d0>
    >>> doc.save('mydoc.docx')

Using `part-edit` from `Openpack <https://pypi.org/project/openpack>`_,
one can see the document that was constructed::

    > EDITOR=cat part-edit mydoc.docx/word/document.xml
    <w:document xmlns:dcterms="http://purl.org/dc/terms/" xmlns:ve="http://schemas.openxmlformats.org/markup-compatibility/2006" xmlns:dcmitype="http://purl.org/dc/dcmitype/" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing" xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
      <w:body>
        <w:p>
          <w:pPr>
            <w:pStyle w:val="Heading 1"/>
          </w:pPr>
          <w:r>
            <w:t>Things to do</w:t>
          </w:r>
        </w:p>
        <w:p>
          <w:r>
            <w:t>First, spend some time learning paradocx usage.</w:t>
          </w:r>
        </w:p>
        <w:p>
          <w:r>
            <w:t>Then, put together some examples</w:t>
          </w:r>
        </w:p>
        <w:p>
          <w:r>
            <w:t>Finally, put those examples in the paradocx documentation</w:t>
          </w:r>
        </w:p>
      </w:body>
    </w:document>


One may also append tables to a document::

    >>> import paradocx
    >>> doc = paradocx.Document()
    >>> doc.table([['a', 'b', 'c'], ['1', '2', '3']])
    <Element {http://schemas.openxmlformats.org/wordprocessingml/2006/main}tbl at 0x2231240>
    >>> doc.save('data.docx')


Object Model and Advanced Usage
===============================

The core object for a Word document is the `paradocx.package.WordPackage`. All
operations involving constructing a Word document use some form of this class
(the `paradocx.Document` subclasses `WordPackage`).

See `the source
<https://github.com/jaraco/paradocx/blob/master/paradocx/package.py>`_
for a trivial example of usage.

Each `WordPackage` is a container of a number of related parts. The parts
represent the various aspects of a document. The following example, adapted
from real-world usage, shows how
one might construct a more complex structure from a series of XML templates
on the file system::

    import string

    def load_template(name, **params):
        with open(name) as f:
            template = string.Template(f.read())
        return template.substitute(params)

    doc = WordPackage()
    doc.start_part.data = load_template('document.xml', text="Hello world")

    # styles
    styles = StylesPart(doc)
    doc.add(styles)
    styles.data = load_template('styles.xml')
    doc.start_part.relate(styles)

    title = "My initial document"

    # Header for cover page
    cover_header = HeaderPart(doc, '/word/cover-header.xml')
    doc.add(cover_header)
    cover_header.data = load_template('cover-header.xml', title=title)
    doc.start_part.relate(cover_header, 'PmxHdr0')

    # body header
    header = HeaderPart(doc)
    doc.add(header)
    header.data = load_template('header.xml', title=title)
    doc.start_part.relate(header, 'PmxHdr1')

    # body footer
    footer = FooterPart(doc)
    doc.add(footer)
    footer.data = load_template('footer.xml',
        date=unicode(datetime.datetime.now()))
    doc.start_part.relate(footer, 'PmxFtr1')

    # image1
    image1 = ImagePart(doc, '/word/media/logo.png')
    doc.add(image1, override=False)
    with open('my_logo.png', 'rb') as logo_data:
        image1.data = logo_data.read()
    doc.start_part.relate(image1, 'Logo1')
    header.relate(image1, 'Logo1')
    # cover page uses the logo, so relate it
    cover_header.relate(image1, 'Logo1')

    # settings
    settings = SettingsPart(doc)
    doc.add(settings)
    settings.data = load_template('settings.xml')
    doc.start_part.relate(settings)

    doc.save(...)

For more details on constructing the XML data for the underlying parts,
consider using a reference document and the OpenPack tools for inspecting
the document for the necessary elements, or consider reading some of the
resources at the `Microsoft Dev Center
<http://msdn.microsoft.com/en-us/library/office/aa338205%28v=office.12%29.aspx>`_
or read up on the `standards developed around Office Open XML
<http://en.wikipedia.org/wiki/Office_Open_XML>`_.

Testing
=======

Paradocx uses `tox <https://pypi.org/project/tox>`_ for
running the tests. To test, simply invoke ``tox`` on the repo.
