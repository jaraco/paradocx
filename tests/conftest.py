import os
import tempfile

import pytest


@pytest.fixture
def sample_stream():
    return open('tests/resources/sample.docx', mode='rb')


@pytest.fixture
def sample_filename():
    return 'tests/resources/sample.docx'


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
