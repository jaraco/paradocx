import os

with open(os.path.join(os.path.dirname(__file__), 'README')) as f:
    long_description = f.read()

setup_params = dict(
    name="paradocx",
    use_hg_version=True,
    packages=['paradocx'],
    long_description=long_description,
    install_requires=[
        'openpack>=1.0',
    ],
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
