from __future__ import print_function

import os
import json
import requests

from requests.exceptions import ConnectionError
from collections import OrderedDict
from jsonschema import Draft4Validator


def add_template():
    success = False
    try:
        repo_dir = os.getcwd()
        file_dir = os.path.dirname(os.path.realpath(__file__))
        template_request = requests.get('https://raw.githubusercontent.com/DCgov/civic.json/master/template.json')
        if template_request.status_code == 200:
            template = template_request.text
            template = json.loads(template, object_pairs_hook=OrderedDict)
            with open(repo_dir + '/civic.json', 'w') as outfile:
                json.dump(template, outfile, indent=4)
            print("civic.json created in {}".format(repo_dir))
            success = True
        else:
            print("Couldn't download civic.json template.")
    except ConnectionError:
        print("Couldn't download civic.json schema. Are you online?")
    finally:
        return success


def validate_file():
    success = False
    repo_dir = os.getcwd()
    file_dir = os.path.dirname(os.path.realpath(__file__))
    try:
        schema_request = requests.get('https://raw.githubusercontent.com/DCgov/civic.json/master/schema.json')
        if schema_request.status_code == 200:
            schema = schema_request.text
            schema = json.loads(schema, object_pairs_hook=OrderedDict)
            with open(repo_dir + '/civic.json') as civic_infile:
                repo_civic = json.load(civic_infile, object_pairs_hook=OrderedDict)
            v = Draft4Validator(schema)
            errors = sorted(v.iter_errors(repo_civic), key=lambda e: e.path)
            if errors:
                for error in errors:
                    message = error.message.replace("u'", "'")
                    print("Error in {0}: {1}".format(error.path[0], message))
            else:
                print("civic.json file valid")
                success = True
        else:
            print("Couldn't download civic.json schema.")
    except ConnectionError:
        print("Couldn't download civic.json schema. Are you online?")
    except IOError:
        print("Error: civic.json file not found in this directory\nInitialize one with: civicjson init")
    finally:
        return success
