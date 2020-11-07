import six

from paradocx.util import w
from paradocx.package import WordPackage


class Document(WordPackage):
    def paragraph(self, text=None, style=None):
        p = paragraph(text, style=style)
        self.start_part.append(p)
        return p

    def table(self, data=None, style=None):
        tbl = table(data, style=style)
        self.start_part.append(tbl)
        return tbl

    @property
    def paragraphs(self):
        return self.start_part.body.findall(w['p'])


def run(text=None, bold=False, italic=False, font=None):
    rPr = w.rPr()
    if bold:
        rPr.append(w.b())
    if italic:
        rPr.append(w.i())
    if font:
        rFont = w.rFont()
        rFont.attrib[w['ascii']] = font
        rPr.append(rFont)
    r = w.r()
    if len(rPr):
        r.append(rPr)
    if text:
        r.append(w.t(six.text_type(text)))
    return r


def paragraph(text=None, style=None, pagebreak=None):
    p = w.p()
    subs = []
    pPr = w.pPr()
    if style:
        s = w.pStyle()
        s.attrib[w['val']] = style
        pPr.append(s)
    if pagebreak:
        pPr.append(w.sectPr())
    if len(pPr):
        subs.append(pPr)
    if text:
        if isinstance(text, six.string_types):
            text = six.text_type(text)
            subs.append(w.r(w.t(text)))
        elif hasattr(text, 'tag'):
            subs.append(text)
    p.extend(subs)
    return p


def table(data=None, style=None):
    tbl = w.tbl()
    tblPr = w.tblPr()
    tbl.append(tblPr)
    data = data or []
    for cells in data:
        tbl.append(w.tr(*[w.tc(paragraph(value)) for value in cells]))
    if style:
        s = w.tblStyle()
        s.attrib[w['val']] = style
        tblPr.append(s)
    return tbl
