#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of civicjson.
# https://github.com/DCgov/civic.json-cli

# Licensed under the CC0-1.0 license:
# https://creativecommons.org/publicdomain/zero/1.0/
# Copyright (c) 2016, Emanuel Feld <elefbet@gmail.com>

from setuptools import setup, find_packages
from civicjson import __version__

with open('README_PYPI.rst') as infile:
    long_description = infile.read()

setup(
    name='civicjson',
    version=__version__,
    description='Tools to make the civic.json (extended) specification easy to use.',
    long_description=long_description,
    keywords='civic.json civic',
    author='Emanuel Feld',
    author_email='elefbet@gmail.com',
    url='https://github.com/DCgov/civic.json-cli',
    license='CC0-1.0',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
        'Environment :: Console',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Operating System :: OS Independent'
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=['jsonschema>=2.5.1', 'requests>=2.9.1'],
    test_suite='nose.collector',
    tests_require=['nose-progressive', 'tox'],
    entry_points={
        'console_scripts': [
            'civicjson=civicjson.commands:main'
        ],
    }
)
