#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of civicjson.
# https://github.com/DCgov/civic.json

# Licensed under the CC0-1.0 license:
# http://www.opensource.org/licenses/CC0-1.0-license
# Copyright (c) 2016, Emanuel Feld <elefbet@gmail.com>

from preggy import expect

from civicjson import __version__
from tests.base import TestCase


class VersionTestCase(TestCase):
    def test_has_proper_version(self):
        expect(__version__).to_equal('0.1.0')
