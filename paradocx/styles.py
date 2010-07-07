from openpack.basepack import DefaultNamed, Part

class StylesPart(DefaultNamed, Part):
	content_type = "application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"
	rel_type = "http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles"
	default_name = '/word/styles.xml'

