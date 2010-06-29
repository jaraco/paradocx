import os

here = os.path.abspath(os.path.dirname(__file__))

def get_resource_filename(name):
	return os.path.join(here, 'resources', name)
