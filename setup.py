# Modified from https://github.com/CAMBI-tech/BciPy
# Note: To use the 'upload' functionality of this file, you must:
# $ pip install twine
import os
import sys
from setuptools import find_packages, setup, Command

# Package meta-data.
NAME = 'ExpSyncPy'
DESCRIPTION = 'Facilitate experimental data sharing.'
URL = 'https://github.com/CAMBI-tech/ExpSyncPy'
EMAIL = 'memmott@ohsu.com'
AUTHOR = 'CAMBI'
REQUIRES_PYTHON = '~=3.6'
VERSION = '0.0.0'

#Class UploadCommand  - waiting for further instructions 

#Where the magic happens: 

from setuptools import find_packages, setup
setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages()
    include_package_data=True,
    license='', #Possible: MIT ? 
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'], 
    test_suite='tests',
)