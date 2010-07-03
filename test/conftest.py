import pkg_resources
import os
import tempfile

def get_resource_filename(name):
	return pkg_resources.resource_filename(__name__, os.path.join('resources', name))

def get_resource_stream(name):
	return pkg_resources.resource_stream(__name__, os.path.join('resources', name))

sample_filename = 'sample.docx'

def pytest_funcarg__sample_stream(request):
	return get_resource_stream(sample_filename)

def pytest_funcarg__sample_filename(request):
	return get_resource_filename(sample_filename)

def pytest_funcarg__table_data(request):
	data = [
		['Name', 'Age'],
		['Christian', 29],
		['Sarah', 28],
		['Curtis', 4],
		['Eli', 2],
	]
	return data

def pytest_funcarg__writable_filename(request):
	"""
	Whenever a function needs a 'writable_filename', create one, but
	be sure it's cleaned up afterward.
	"""
	fobj, name = tempfile.mkstemp()
	os.close(fobj); os.remove(name)
	def remove_if_exists():
		if os.path.exists(name):
			os.remove(name)
	request.addfinalizer(remove_if_exists)
	return name
