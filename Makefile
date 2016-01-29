# This file is part of civicjson.
# https://github.com/DCgov/civic.json-cli

# Licensed under the CC0-1.0 license:
# https://creativecommons.org/publicdomain/zero/1.0/
# Copyright (c) 2016, Emanuel Feld <elefbet@gmail.com>

# lists all available targets
list:
	@sh -c "$(MAKE) -p no_targets__ | awk -F':' '/^[a-zA-Z0-9][^\$$#\/\\t=]*:([^=]|$$)/ {split(\$$1,A,/ /);for(i in A)print A[i]}' | grep -v '__\$$' | grep -v 'make\[1\]' | grep -v 'Makefile' | sort"
# required for list
no_targets__:

# install all dependencies (do not forget to create a virtualenv first)
setup:
	@pip install -U -e .\[tests\]

# test your application (tests in the tests/ directory)
test: unit

unit:
	@coverage run --source=civicjson setup.py test

# show coverage in html format
coverage-html: unit
	@coverage html

# run tests against all supported python versions
tox:
	@tox
