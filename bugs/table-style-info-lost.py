# This script generates the document used to demonstrate the undesirable
#  behavior of MS Word 2007. See
#  http://social.msdn.microsoft.com/Forums/en-US/worddev/thread/894ee235-373f-4368-b2cb-6794614f49b0
#  for more details
from paradocx import Document
from paradocx.styles import StylesPart


def run():
    doc = Document()
    doc.table(
        [
            'foo bar baz bing'.split(),
            'bar foo bing baz'.split(),
        ],
        style='CustomTable2',
    )
    styles = StylesPart(doc)
    styles.load(
        """
    <w:styles
    xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"
    xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
        <w:style w:type="table" w:customStyle="1" w:styleId="CustomTable">
            <w:name w:val="Custom Table"/>
            <w:qFormat/>
            <w:pPr>
                <w:spacing w:after="120"/>
            </w:pPr>
        </w:style>
        <w:style w:type="table" w:customStyle="1" w:styleId="CustomTable2">
            <w:name w:val="Custom Table 2"/>
            <w:basedOn w:val="CustomTable"/>
            <w:qFormat/>
            <w:pPr>
                <w:spacing w:after="120"/>
            </w:pPr>
        </w:style>
    </w:styles>
    """
    )
    doc.add(styles)
    doc.start_part.relate(styles)
    doc.save('doc.docx')


__name__ == '__main__' and run()
