from openpack.basepack import DefaultNamed, Part


class HeaderPart(DefaultNamed, Part):
    content_type = (
        "application/" "vnd.openxmlformats-officedocument.wordprocessingml.header+xml"
    )
    rel_type = (
        "http://schemas.openxmlformats.org/officeDocument/2006/relationships/header"
    )
    default_name = '/word/header.xml'


class FooterPart(DefaultNamed, Part):
    content_type = (
        "application/" "vnd.openxmlformats-officedocument.wordprocessingml.footer+xml"
    )
    rel_type = (
        "http://schemas.openxmlformats.org/officeDocument/2006/relationships/footer"
    )
    default_name = '/word/footer.xml'
