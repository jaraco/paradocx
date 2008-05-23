from openpack.basepack import Part
from openpack.officepack import OfficePackage
from lxml.etree import Element, SubElement, tostring
from lxml.builder import ElementMaker
from util import w

class WordDocument(Part):
	content_type = "application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"
	rel_type = OfficePackage.main_rel

	def __init__(self, package, name, growth_hint=None, fp=None):
		Part.__init__(self, package, name, growth_hint, fp)
		self.xml = w.document()
		self.body = w.body()
		self.xml.append(self.body)

	def dump(self):
		if self.body:
			return tostring(self.xml, encoding=self.encoding or 'utf-8')
		return Part.dump(self)

	def paragraph(self, text=None):
		p = paragraph(text)
		self.body.append(p)
		return p

	def table(self, data=None):
		tbl = table(data)
		self.body.append(tbl)
		return tbl

	@property
	def paragraphs(self):
		return self.body.findall(w['p'])

def paragraph(text=None, style=None, pagebreak=None):
	p = w.p()
	subs = []
	pPr = w.pPr()
	if style:
		pPr.append(
			w.pStyle(attrib={w['val']:style})
		)
	if pagebreak:
		pPr.append(
			w.sectPr()
		)
	if len(pPr):
		subs.append(pPr)
	if text:
		text = unicode(text)
		subs.append(
			w.r(
				w.t(text)
			)
		)
	p.extend(subs)
	return p

def table(data=None):
	tbl = w.tbl()
	data = data or []
	for cells in data:
		tbl.append(
			w.tr(
				*[w.tc(paragraph(value)) for value in cells]
			)
		)
	return tbl
	

