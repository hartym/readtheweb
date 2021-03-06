# This file is autogenerated by edgy.project code generator.
# All changes will be overwritten.

from setuptools import setup, find_packages

tolines = lambda c: list(filter(None, map(lambda s: s.strip(), c.split('\n'))))

def read(filename, flt=None):
    with open(filename) as f:
        content = f.read().strip()
        return flt(content) if callable(flt) else content

def requirements_filter(c):
    install_requires = []
    for requirement in tolines(c):
        _pos = requirement.find('#egg=')
        if _pos != -1:
            requirement = requirement[_pos+5:].strip()
        _pos = requirement.find('#')
        if _pos != -1:
            requirement = requirement[0:_pos].strip()
        if len(requirement):
            install_requires.append(requirement)
    return install_requires

version = read('version.txt')

setup(
    name = 'readtheweb',
    description = '',
    license = 'Copyright ',
    install_requires = ['blessings >=1.6,<1.7',
 'CacheControl[filecache] >=0.11,<0.12',
 'cerberus >=0.9,<0.10',
 'certifi==2015.04.28',
 'edgy.event >=0.1.5,<0.2',
 'edgy.workflow >=0.1.1,<0.2',
 'html2text',
 'markdown >=2.6,<2.7',
 'rdc.common',
 'rdc.etl',
 'requests-futures',
 'requests[security]',
 'simplejson >=3.8,<3.9',
 'urlnorm >=1.1,<1.2'],
    version = version,
    long_description = read('README.rst'),
    classifiers = read('classifiers.txt', tolines),
    packages = find_packages(exclude=['ez_setup', 'example', 'test']),
    include_package_data = True,
    extras_require = {'dev': ['coverage >=4.0,<4.2',
         'django-debug-toolbar >=1.4,<1.5',
         'fake-factory',
         'flake8 ==2.5.0',
         'gitchangelog >=2.0,<3.0',
         'ipdb ==0.8.1',
         'nose >=1.3,<1.4',
         'pylint >=1.4,<1.5',
         'pytest >=2.8,<2.9',
         'pytest-cov >=2.2,<2.3',
         'pytest-django >=2.9.1',
         'mock >=1.3,<1.4',
         'sphinx',
         'sphinx_rtd_theme']},
    url = '',
    download_url = ''.format(version=version),
)
