import os
import tempfile

import pytest
import pkg_resources


def get_resource_filename(name):
    return pkg_resources.resource_filename(__name__, os.path.join('resources', name))


def get_resource_stream(name):
    return pkg_resources.resource_stream(__name__, os.path.join('resources', name))


_sample_filename = 'sample.docx'


@pytest.fixture
def sample_stream():
    return get_resource_stream(_sample_filename)


@pytest.fixture
def sample_filename():
    return get_resource_filename(_sample_filename)


@pytest.fixture
def table_data():
    data = [
        ['Name', 'Age'],
        ['Christian', 29],
        ['Sarah', 28],
        ['Curtis', 4],
        ['Eli', 2],
    ]
    return data


@pytest.fixture
def writable_filename(request):
    """
    Whenever a function needs a 'writable_filename', create one, but
    be sure it's cleaned up afterward.
    """
    fobj, name = tempfile.mkstemp()
    os.close(fobj)
    os.remove(name)

    def remove_if_exists():
        if os.path.exists(name):
            os.remove(name)

    request.addfinalizer(remove_if_exists)
    return name
