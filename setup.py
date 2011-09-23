import os

with open(os.path.join(os.path.dirname(__file__), 'README')) as f:
    long_description = f.read()

setup_params = dict(
    name="paradocx",
    version="0.3.2",
    packages=['paradocx'],
    long_description=long_description,
    install_requires=[
        'openpack >= 0.4',
    ],
)

if __name__ == '__main__':
    from setuptools import setup
    setup(**setup_params)
