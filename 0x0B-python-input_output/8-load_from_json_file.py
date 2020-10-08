#!/usr/bin/python3
'''task 8'''


def load_from_json_file(filename):
    '''load from a file'''
    import json
    with open(filename, 'r') as f:
        obj = f.read()
    return json.loads(obj)
