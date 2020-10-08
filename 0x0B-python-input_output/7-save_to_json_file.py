#!/usr/bin/python3
'''task 7'''


def save_to_json_file(my_obj, filename):
    '''save as json'''
    import json
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
