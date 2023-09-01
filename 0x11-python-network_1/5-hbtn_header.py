#!/usr/bin/python3
"""fetches a url and displays a value of a variable in header response"""
import requests
import sys

r = requests.get(sys.argv[1])
print(r.headers['X-Request-Id'])
