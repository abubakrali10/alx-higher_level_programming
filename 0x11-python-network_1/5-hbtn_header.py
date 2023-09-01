#!/usr/bin/python3
"""fetches a url and displays a value of a variable in header response"""
import requests
import sys

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers['X-Request-Id'])
