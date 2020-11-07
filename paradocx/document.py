from lxml.etree import fromstring
from openpack.basepack import Part
from openpack.officepack import OfficePackage

from .util import w, expand_namespace as EN


class DocumentPart(Part):
    content_type = (
        "application/"
        "vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"
    )
    rel_type = OfficePackage.main_rel

    def __init__(self, *args, **kwargs):
        Part.__init__(self, *args, **kwargs)
        self.data = w.document()
        self.body = w.body()
        self.data.append(self.body)
        if 'data' in kwargs:
            self.load(kwargs['data'])

    def load(self, xml):
        self.data = fromstring(xml)
        self.body = self.data.find(EN('w:body'))

    def append(self, xml_element):
        self.body.append(xml_element)
