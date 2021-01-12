#!/usr/bin/python3
'''
Script that list 10 commits from the most recent to oldest of the repository
rails by the user rails
'''

if __name__ == "__main__":
    from sys import argv
    from requests import get
    args = {
        "repo": argv[1],
        "owner": argv[2]
    }
    url = "https://api.github.com/repos/{owner}/{repo}/commits".format(**args)

    req = get(url).json()[:10]

    for item in req:
        print("{sha}: {commit[author][name]}".format(**item))
