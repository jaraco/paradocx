from openpack.basepack import Part
from openpack.officepack import OfficePackage
from lxml.etree import tostring
from util import w

class DocumentPart(Part):
	content_type = "application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"
	rel_type = OfficePackage.main_rel

	def __init__(self, *args, **kwargs):
		Part.__init__(self, *args, **kwargs)
		self.xml = w.document()
		self.body = w.body()
		self.xml.append(self.body)

	def dump(self):
		if len(self.body):
			t = tostring(self.xml, encoding='utf-8', pretty_print=True)
			return t
		return Part.dump(self)
	
	def append(self, xml_element):
		self.body.append(xml_element)

