#!/usr/bin/python3
"""fetches url using requests library"""
import requests

r = requests.get('https://alx-intranet.hbtn.io/status')
response = r.text
print('Body response:')
print(f"\t- type: {type(response)}")
print(f"\t- content: {response}")
