#!/usr/bin/python3
"""uses github api to display user id"""
import requests
from requests.auth import HTTPBasicAuth
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    api = 'https://api.github.com/user'

    auth = HTTPBasicAuth(username, password)
    res = requests.get(api, auth=auth)
    print(res.json().get('id'))
