#!/usr/bin/python3
"""uses github api to display last 10 commits for a repo"""
import requests
import sys

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    api = f'https://api.github.com/repos/{owner}/{repo}/commits'
    res = requests.get(api)

    try:
        for i in range(10):
            data = res.json()[i]
            print(f"{data['sha']}: {data['commit']['author']['name']}")
    except IndexError:
        pass
