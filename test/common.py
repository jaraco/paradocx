import pkg_resources
import os

def get_resource_filename(name):
	return pkg_resources.resource_filename(__name__, os.path.join('resources', name))

def get_resource_stream(name):
	return pkg_resources.resource_stream(__name__, os.path.join('resources', name))
