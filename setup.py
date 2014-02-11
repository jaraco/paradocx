import os
import sys

with open(os.path.join(os.path.dirname(__file__), 'README')) as f:
    long_description = f.read()

importlib_req = ['importlib'] if sys.version_info < (2,7) else []

setup_params = dict(
    name="paradocx",
    use_hg_version=True,
    packages=['paradocx'],
    long_description=long_description,
    license = 'MIT',
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
    ],
    install_requires=[
        'openpack>=1.1,<2dev',
        'six',
    ] + importlib_req,
    tests_require=[
        'pytest',
    ],
    setup_requires=[
        'hgtools>=1.0',
        'pytest-runner',
    ],
)

if __name__ == '__main__':
    from setuptools import setup
    setup(**setup_params)
