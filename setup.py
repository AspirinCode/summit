# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import os.path

readme = ''
here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, 'README.rst')
if os.path.exists(readme_path):
    with open(readme_path, 'rb') as stream:
        readme = stream.read().decode('utf8')

setup(
    long_description=readme,
    name='summit',
    version='0.2.2',
    description='Tools for optimizing chemical processes',
    python_requires='==3.*,>=3.6.0',
    project_urls={
        'homepage': 'https://pypi.org/project/summit',
        'repository': 'https://github.com/sustainable-processes/summit'
    },
    author='Kobi Felton',
    author_email='kobi.c.f@gmail.com',
    packages=['summit', 'summit.data', 'summit.initial_design'],
    package_data={
        'summit.data': ['*.csv'],
    },
    install_requires=[
        'gpy==1.*,>=1.9.0', 'matplotlib==3.*,>=3.0.0', 'numpy==1.16.0',
        'pandas==0.*,>=0.24.1', 'platypus-opt==1.*,>=1.0.0',
        'sklearn==0.*,>=0.0.0'
    ],
)
