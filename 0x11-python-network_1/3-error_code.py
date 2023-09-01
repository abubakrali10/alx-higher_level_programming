#!/usr/bin/python3
"""send a request to the URL and display the body of the response"""
import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(req) as r:
            res_body = r.read()
            print(res_body.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
