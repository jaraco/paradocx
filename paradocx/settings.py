from openpack.basepack import DefaultNamed, Part


class SettingsPart(DefaultNamed, Part):
    content_type = (
        'application/' 'vnd.openxmlformats-officedocument.wordprocessingml.settings+xml'
    )
    rel_type = (
        'http://schemas.openxmlformats.org'
        '/officeDocument/2006/relationships/settings'
    )
    default_name = '/word/settings.xml'
