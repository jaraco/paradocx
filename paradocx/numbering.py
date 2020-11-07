from openpack.basepack import DefaultNamed, Part


class NumberingPart(DefaultNamed, Part):
    content_type = (
        'application/'
        'vnd.openxmlformats-officedocument.wordprocessingml.numbering+xml'
    )
    rel_type = (
        'http://schemas.openxmlformats.org'
        '/officeDocument/2006/relationships/numbering'
    )
    default_name = '/word/numbering.xml'


class AbstractNumbering(object):
    def __init__(self, id, **props):
        self.id = id
        self.properties = props


class Numbering(object):
    pass
