#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of civicjson.
# https://github.com/DCgov/civic.json-cli

# Licensed under the CC0-1.0 license:
# https://creativecommons.org/publicdomain/zero/1.0/
# Copyright (c) 2016, Emanuel Feld <elefbet@gmail.com>

import subprocess
from nose.tools import *
import os
from civicjson import __version__


def subprocess_helper(cmd):
    return subprocess.check_output(cmd, universal_newlines=True)


def test_has_proper_version():
    eq_(__version__, '0.1.1')


def test_downloads_template():
    cmd = ['civicjson', 'init']
    out = subprocess_helper(cmd)
    eq_(out.strip(), 'civic.json created in /Users/emanuelfeld/Documents/civicjson')


def test_validates_civicjson():
    cmd = ['civicjson', 'validate']
    out = subprocess_helper(cmd)
    eq_(out.strip(), "Error in status: '[required] project status (Ideation, Alpha, Beta, Production, or Archival)' is not one of ['Ideation', 'Alpha', 'Beta', 'Production', 'Archival']")


def test_no_civic_json():
    repo_dir = os.getcwd()
    civic_path = os.path.join(repo_dir, 'civic.json')
    subprocess_helper(['rm', civic_path])
    out = subprocess_helper(['civicjson', 'validate'])
    assert "Error: civic.json file not found in this directory" in out.strip()


def test_usage():
    cmd = ['civicjson']
    out = subprocess_helper(cmd)
    assert "Usage:" in out.strip()
