#!/usr/bin/python3
"""sends a post request to url with letter as parameter"""
import requests
import sys

if __name__ == "__main__":
    payload = {'q': ''}
    url = 'http://0.0.0.0:5000/search_user'

    if len(sys.argv) > 1:
        payload['q'] = sys.argv[1]

    r = requests.post(url, data=payload)
    try:
        res = r.json()
        if not res:
            print("No result")
        else:
            print(f"[{res.get('id')}] {res.get('name')}")
    except ValueError:
        print("Not a valid JSON")
