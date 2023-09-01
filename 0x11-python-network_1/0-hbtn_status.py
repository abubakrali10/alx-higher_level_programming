#!/usr/bin/python3
"""fetches a url"""
import urllib.request

if __name__ == "__main__":
    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as r:
        res_body = r.read()
        print('Body response:')
        print(f"\t- type: {type(res_body)}")
        print(f"\t- content: {res_body}")
        print(f"\t- utf8 content: {res_body.decode('utf-8')}")
