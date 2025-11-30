#!/usr/bin/env python3
"""
Quick test to verify the cookie header format is correct.
We'll use your ACTUAL token from the browser.
"""

import requests

# Your actual domain and the REAL token from browser DevTools
domain = "danielmontano.zo.computer"
# This is the token from your browser (first part)
real_token = "eyJhbGciOiJFUzI1NiIsImtpZCI6IjkxYmU5Yjk3LTMzM2ItNDQxMC04NmEwLTUyYTUyNzAwZDcxNSIsInR5cCI6IkpXVCJ9.eyJtb2RlIjoiYWNjZXNzIiwidHlwZSI6InVzZXIiLCJwcm9wZXJ0aWVzIjp7ImlkIjoidXNyX3pJUVI0VXF0NUdnbzNndjAiLCJmdWxsX25hbWUiOiJEYW5pZWwgTW9uZ2UgTW9udGFubyIsImVtYWlsIjoiZG1vbmdlbW9udGFub0B1ZGFsbGFzLmVkdSIsInBpY3R1cmUiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS9BQ2c4b2NMYW9xclRYRzNQV3QyRWpuQWJqSFhRZkdnT01pTU5scjRpVG5Xb0QybTROTFNObUZNPXM5Ni1jIiwiZG9tYWlucyI6WyJkYW5pZWxtb250YW5vIl19LCJhdWQiOiJvbi1zdWJzdHJhdGUiLCJpc3MiOiJodHRwczovL2F1dGguem8uY29tcHV0ZXIiLCJzdWIiOiJ1c3JfeklRUjRVcXQ1R2dvM2d2MCIsImV4cCI6MTc2NjMwMzI4MH0.9CCO-vuYppBxt40UvewxGahKeJcFyG6fjP7etxEGyKUUk4ckvXtyACvwKZ0e1sDlHl-5CELjXaGnsH_V8YaAwg"

url = f"https://{domain}/api/workspace-tree?root=w&showHidden=false"

print(f"[*] Testing with REAL browser token")
print(f"[*] URL: {url}")
print()

response = requests.get(
    url,
    headers={
        'cookie': f'access_token={real_token}',
        'origin': f'https://{domain}'
    },
    timeout=10
)

print(f"[*] Response Status: {response.status_code}")
print(f"[*] Content-Type: {response.headers.get('content-type')}")
print()

if response.status_code == 200:
    try:
        data = response.json()
        print("[SUCCESS!] API works with the real browser token!")
        print(f"   Name: {data.get('name', 'N/A')}")
        print(f"   Type: {data.get('type', 'N/A')}")
        print(f"   Children: {len(data.get('children', []))} items")
    except:
        print("[FAIL] Got 200 but not JSON (still HTML redirect)")
        print(response.text[:200])
else:
    print(f"[FAIL] Got status {response.status_code}")
