#!/usr/bin/python3
'''
A script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)
'''
if __name__ == '__main__':
    from sys import argv
    from urllib import request, error

    url = argv[1]
    try:
        with request.urlopen(url) as req:
            print(req.read().decode('utf-8'))
    except error.HTTPError as err:
        print("Error code: {}". format(err.code))
