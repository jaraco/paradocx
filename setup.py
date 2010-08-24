from setuptools import setup

setup(
    name="paradocx",
    version="0.3.2",
    packages=['paradocx'],
    long_description=open('README').read(),
    install_requires=[
        'openpack >= 0.4',
    ],
)

