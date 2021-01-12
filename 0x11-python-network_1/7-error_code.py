#!/usr/bin/python3
'''
A script that takes in a URL, sends a request to the URL
and displays the body of the response.
'''


if __name__ == '__main__':
    from requests import get
    from sys import argv
    url = argv[1]

    req = get(url)
    if (req.status_code) < 400:
        print(req.text)
    else:
        print("Error code: {}".format(req.status_code))
