from openpack.basepack import Part
from openpack.officepack import OfficePackage
from xml.etree import ElementTree
from util import ns, properties

w = ns.w

class WordDocument(Part):
	content_type = "application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"
	rel_type = OfficePackage.main_rel

	def __init__(self, package, name, growth_hint=None, fp=None):
		Part.__init__(self, package, name, growth_hint, fp)
		self.xml = w('document')
		self.body = w('body')
		self.xml.append(self.body)

	def dump(self):
		if self.body:
			return ElementTree.tostring(self.xml, self.encoding or 'utf-8')
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
		return self.body.find(ns.nsify('w', 'p'))

def style(element, stylename):
	props = properties(element)
	props.append(w('pStyle', val=stylename))
	return props

def properties(element):
	basetag = element.tag.split('}')[1]
	proptag = "%sPr" % basetag
	props = element.find(ns.nsify('w', proptag))
	if not props:
		props = w(proptag)
		element.append(props)
	return props

def paragraph(text=None):
	p = w('p')
	if text:
		text = unicode(text)
		t = w('t')
		t.text = text
		r = w('r')
		r.append(t)
		p.append(r)
	return p

def table(data=None):
	tbl = w('tbl')
	data = data or []
	for cells in data:
		tr = w('tr')
		for value in cells:
			tc = w('tc')
			tc.append(paragraph(value))
			tr.append(tc)
		tbl.append(tr)
	return tbl
	

