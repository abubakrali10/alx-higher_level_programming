#!/usr/bin/python3
"""sends a POST request to URL with email, and displays body of response"""
import requests
import sys

r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
print(r.text)
