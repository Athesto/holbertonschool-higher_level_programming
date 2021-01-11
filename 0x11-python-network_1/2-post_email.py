#!/usr/bin/python3
'''
script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response
'''

if __name__ == '__main__':
    from urllib import request
    from sys import argv
    url = argv[1]
    email = argv[2]

    with request.urlopen(url) as req:
        print("Your email is: {}".format(email))
