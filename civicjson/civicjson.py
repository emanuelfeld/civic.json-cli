from __future__ import print_function

import os
import json
from collections import OrderedDict
from jsonschema import Draft4Validator


def add_template(name=""):
    success = False
    try:
        repo_dir = os.getcwd()
        file_dir = os.path.dirname(os.path.realpath(__file__))
        with open(file_dir + '/data/template.json') as infile:
            boilerplate = json.load(infile, object_pairs_hook=OrderedDict)
        with open(repo_dir + '/civic.json', 'w') as outfile:
            json.dump(boilerplate, outfile, indent=4)
        print("civic.json created in {}".format(repo_dir))
        success = True
    except:
        pass
    finally:
        return success


def validate_file():
    success = False
    repo_dir = os.getcwd()
    file_dir = os.path.dirname(os.path.realpath(__file__))
    try:
        with open(repo_dir + '/civic.json') as civic_infile:
            repo_civic = json.load(civic_infile, object_pairs_hook=OrderedDict)
        with open(file_dir + '/data/schema.json') as schema_infile:
            schema = json.load(schema_infile, object_pairs_hook=OrderedDict)
        v = Draft4Validator(schema)
        errors = sorted(v.iter_errors(repo_civic), key=lambda e: e.path)
        if not errors:
            print("civic.json file valid")
            success = True
        else:
            for error in errors:
                message = error.message.replace("u'", "'")
                print("Error in {0}: {1}".format(error.path[0], message))
    except IOError:
        print("Error: civic.json file not found in this directory\nInitialize one with: civicjson init")
    finally:
        return success
