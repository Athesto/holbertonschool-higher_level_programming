#!/usr/bin/python3
'''a Python script that fetches https://intranet.hbtn.io/status'''

if __name__ == "__main__":
    import urllib.request

    url = "https://intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        html = response.read()
        print('\t- type: {}'.format(type(html)))
        print('\t- content: {}'.format(html))
        print('\t- uft8 content: {}'.format(html.decode('utf-8')))
