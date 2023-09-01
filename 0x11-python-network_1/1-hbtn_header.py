#!/usr/bin/python3
"""fetches a url and displays a value of a variable in header response"""
import urllib.request
import sys

if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as r:
        res_header = r.headers
        print(res_header['X-Request-Id'])
