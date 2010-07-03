import pkg_resources
import os

def get_resource_filename(name):
	return pkg_resources.resource_filename(__name__, os.path.join('resources', name))

def get_resource_stream(name):
	return pkg_resources.resource_stream(__name__, os.path.join('resources', name))

sample_filename = 'sample.docx'

def pytest_funcarg__sample_stream(request):
	return get_resource_stream(sample_filename)

def pytest_funcarg__sample_filename(request):
	return get_resource_filename(sample_filename)
