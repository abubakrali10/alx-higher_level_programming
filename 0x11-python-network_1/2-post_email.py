#!/usr/bin/python3
"""sends a POST request to URL with email and displays response"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = {'email': sys.argv[2]}
    email_value = urllib.parse.urlencode(email).encode('ascii')
    req = urllib.request.Request(url, email_value)
    with urllib.request.urlopen(req) as r:
        res_body = r.read()
        print(res_body.decode('utf-8'))
