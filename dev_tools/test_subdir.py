#!/usr/bin/env python3
"""Test subdirectory API call"""

import requests

domain = "danielmontano.zo.computer"
access_token = "eyJhbGciOiJFUzI1NiIsImtpZCI6IjkxYmU5Yjk3LTMzM2ItNDQxMC04NmEwLTUyYTUyNzAwZDcxNSIsInR5cCI6IkpXVCJ9.eyJtb2RlIjoiYWNjZXNzIiwidHlwZSI6InVzZXIiLCJwcm9wZXJ0aWVzIjp7ImlkIjoidXNyX3pJUVI0VXF0NUdnbzNndjAiLCJmdWxsX25hbWUiOiJEYW5pZWwgTW9uZ2UgTW9udGFubyIsImVtYWlsIjoiZG1vbmdlbW9udGFub0B1ZGFsbGFzLmVkdSIsInBpY3R1cmUiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS9BQ2c4b2NMYW9xclRYRzNQV3QyRWpuQWJqSFhRZkdnT01pTU5scjRpVG5Xb0QybTROTFNObUZNPXM5Ni1jIiwiZG9tYWlucyI6WyJkYW5pZWxtb250YW5vIl19LCJhdWQiOiJvbi1zdWJzdHJhdGUiLCJpc3MiOiJodHRwczovL2F1dGguem8uY29tcHV0ZXIiLCJzdWIiOiJ1c3JfeklRUjRVcXQ1R2dvM2d2MCIsImV4cCI6MTc2NjMwMzI4MH0.9CCO-vuYppBxt40UvewxGahKeJcFyG6fjP7etxEGyKUUk4ckvXtyACvwKZ0e1sDlHl-5CELjXaGnsH_V8YaAwg"

# Test 1: Root directory
print("[*] Test 1: Fetching ROOT directory")
url1 = f"https://{domain}/api/workspace-tree?root=w&showHidden=false"
response1 = requests.get(url1, headers={'cookie': f'access_token={access_token}', 'origin': f'https://{domain}'})
data1 = response1.json()
print(f"    Name: {data1.get('name')}")
print(f"    Children: {len(data1.get('children', []))}")
print(f"    First 5 items: {[c['name'] for c in data1.get('children', [])[:5]]}")
print()

# Test 2: Subdirectory with path parameter
print("[*] Test 2: Fetching 'apps' subdirectory (with path param)")
url2 = f"https://{domain}/api/workspace-tree?root=w&path=apps&showHidden=false"
response2 = requests.get(url2, headers={'cookie': f'access_token={access_token}', 'origin': f'https://{domain}'})
data2 = response2.json()
print(f"    Name: {data2.get('name')}")
print(f"    Children: {len(data2.get('children', []))}")
if data2.get('children'):
    print(f"    First 5 items: {[c['name'] for c in data2.get('children', [])[:5]]}")
print()

# Test 3: Alternative API endpoint
print("[*] Test 3: Trying /api/file/apps endpoint")
url3 = f"https://{domain}/api/file/apps"
response3 = requests.get(url3, headers={'cookie': f'access_token={access_token}', 'origin': f'https://{domain}'})
print(f"    Status: {response3.status_code}")
print(f"    Content-Type: {response3.headers.get('content-type', 'N/A')}")
if response3.status_code == 200:
    try:
        data3 = response3.json()
        print(f"    Data: {str(data3)[:200]}")
    except:
        print(f"    Text: {response3.text[:200]}")
