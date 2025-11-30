#!/usr/bin/env python3
"""Test nested folder API call"""

import requests

domain = "danielmontano.zo.computer"
access_token = "eyJhbGciOiJFUzI1NiIsImtpZCI6IjkxYmU5Yjk3LTMzM2ItNDQxMC04NmEwLTUyYTUyNzAwZDcxNSIsInR5cCI6IkpXVCJ9.eyJtb2RlIjoiYWNjZXNzIiwidHlwZSI6InVzZXIiLCJwcm9wZXJ0aWVzIjp7ImlkIjoidXNyX3pJUVI0VXF0NUdnbzNndjAiLCJmdWxsX25hbWUiOiJEYW5pZWwgTW9uZ2UgTW9udGFubyIsImVtYWlsIjoiZG1vbmdlbW9udGFub0B1ZGFsbGFzLmVkdSIsInBpY3R1cmUiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS9BQ2c4b2NMYW9xclRYRzNQV3QyRWpuQWJqSFhRZkdnT01pTU5scjRpVG5Xb0QybTROTFNObUZNPXM5Ni1jIiwiZG9tYWlucyI6WyJkYW5pZWxtb250YW5vIl19LCJhdWQiOiJvbi1zdWJzdHJhdGUiLCJpc3MiOiJodHRwczovL2F1dGguem8uY29tcHV0ZXIiLCJzdWIiOiJ1c3JfeklRUjRVcXQ1R2dvM2d2MCIsImV4cCI6MTc2NjMwMzI4MH0.9CCO-vuYppBxt40UvewxGahKeJcFyG6fjP7etxEGyKUUk4ckvXtyACvwKZ0e1sDlHl-5CELjXaGnsH_V8YaAwg"

# Test nested folder
print("[*] Testing nested folder: apps/cobalt")
url = f"https://{domain}/api/file/apps/cobalt"
response = requests.get(url, headers={'cookie': f'access_token={access_token}', 'origin': f'https://{domain}'})
print(f"    Status: {response.status_code}")
if response.status_code == 200:
    data = response.json()
    print(f"    isDir: {data.get('isDir')}")
    if data.get('directoryContents'):
        print(f"    Items: {len(data['directoryContents'])}")
        for item in data['directoryContents'][:5]:
            print(f"      - {item['name']} ({'dir' if item['isDirectory'] else 'file'})")
