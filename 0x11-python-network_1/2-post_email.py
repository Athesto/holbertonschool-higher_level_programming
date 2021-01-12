#!/usr/bin/python3
'''
script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response
'''

if __name__ == '__main__':
    from urllib import request, parse
    from sys import argv
    url = argv[1]
    email = argv[2]
    data = parse.urlencode({"email": email})
    data = data.encode('utf-8')

    with request.urlopen(url, data) as req:
        print(req.read().decode('utf-8'))
