from xml.etree.ElementTree import Element
import re

class NameSpace(object):
	map = {
		'w' : "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
		'r' : 'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
		've' : 'http://schemas.openxmlformats.org/markup-compatibility/2006',
		'wp' : 'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing',
	}

	def __getattr__(self, prefix):
		if prefix in self.map:
			def wrap(tag, **params):
				attrs = {}
				for name, value in params.iteritems():
					attrs[self.nsify(prefix, name)] = value
				return Element(self.nsify(prefix, tag), **attrs)
			return wrap
		raise AttributeError(prefix)

	def nsify(self, prefix, tag):
		return "{%s}%s" % (self.map[prefix], tag)

ns = NameSpace()

def properties(element):
	basetag = element.tag.split('}')[1]
	proptag = "%sPr" % basetag
	props = element.find(ns.nsify('w', proptag))
	if not props:
		props = ns.w(proptag)
		element.append(props)
	return props

