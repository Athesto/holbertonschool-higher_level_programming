#!/usr/bin/python3
'''script that fetches https://intranet.hbtn.io/status'''

if __name__ == '__main__':
    from requests import get
    url = "https://intranet.hbtn.io/status"
    req = get(url)
    dir(req)
    ans = req.text
    print("Body response:")
    print("\t- type: {}".format(type(ans)))
    print("\t- content: {}".format(ans))
