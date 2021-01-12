#!/usr/bin/python3
'''
script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
'''

if __name__ == '__main__':
    from sys import argv
    from requests import post
    myobj = {
        "url": "http://0.0.0.0:5000/search_user",
        "data": {
            "q": "" if len(argv) < 2 else argv[1]
        }
    }
    req = post(**myobj)
    try:
        print("[{id}] {name}".format(**req.json()))
    except:
        print("No result")
