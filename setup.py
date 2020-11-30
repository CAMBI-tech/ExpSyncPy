# Modified from https://github.com/CAMBI-tech/BciPy
# Note: To use the 'upload' functionality of this file, you must:
# $ pip install twine
import os
import sys
from setuptools import find_packages, setup, Command

# Package meta-data.
NAME = 'ExpSyncPy'
DESCRIPTION = 'Facilitate experimental data sharing.'
VERSION = '0.0.0'

# Class UploadCommand  - waiting for further instructions

# Where the magic happens:

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    packages=find_packages(),
    include_package_data=True,
    license='',  # Possible: MIT ?
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)
