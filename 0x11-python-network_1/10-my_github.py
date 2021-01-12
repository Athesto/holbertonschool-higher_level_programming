#!/usr/bin/python3
'''
a Python script that takes your Github credentials (username and password)
and uses the Github API to display your id
'''

if __name__ == '__main__':
    from requests import get
    from sys import argv
    myobj = {
        "url":  "https://api.github.com/user",
        "auth": (
                argv[1],
                argv[2]
        )
    }
    req = get(**myobj)
    print(req.json().get('id'))
