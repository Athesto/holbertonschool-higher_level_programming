#!/usr/bin/python3
'''script that fetches https://intranet.hbtn.io/status'''

if __name__ == '__main__':
    from urllib import request
    url = "https://intranet.hbtn.io/status"
    with request.urlopen(url) as req:
        ans = req.read().decode('utf-8')
        print("Body response:")
        print("\t- type: {}".format(type(ans)))
        print("\t- content: {}".format(ans))
