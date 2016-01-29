===============
civic.json-cli
===============

civic.json-cli is a command line interface that helps make civic.json easier to use. This tool will let you:

1. Install a civic.json template to your repository
2. Validate one that's already there.

It implements the `civic.json (extended) <http://open.dc.gov/civic.json>`_ specification, a (backwards compatible) modification to BetaNYC's original civic.json specification. The update aims to broaden civic.json's user base to include civic hackers inside and outside of government.

You can read more about that on the `civic.json (extended) homepage <http://open.dc.gov/civic.json>`_ or in its `GitHub repository <https://github.com/DCgov/civic.json>`_.

Dependencies
===============
* Python 2.7 or 3.3+
* `jsonschema <https://pypi.python.org/pypi/jsonschema/>`_ to validate civic.json files against the schema
* `requests <https://pypi.python.org/pypi/requests/>`_ to get the schema and template files from GitHub and ensure they're up to date
* An active internet connection

Use
===============

Create a civic.json file
___________________________

Run `civicjson init` from the base directory of your repository to initialize a civic.json file (with explanatory text).

Validate a civic.json file
___________________________

Run `civicjson validate` from the folder containing your civic.json file. If there are any errors, it will output them to the console.
