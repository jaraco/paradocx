from openpack.basepack import Part
from openpack.officepack import OfficePackage

class WordDocument(Part):
    content_type = "application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"
    rel_type = OfficePackage.main_rel

    def __init__(self, package, name, growth_hint=None, fp=None):
        Part.__init__(self, package, name, growth_hint, fp)
        self.numbering = None

