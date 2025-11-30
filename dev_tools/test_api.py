#!/usr/bin/env python3
"""Test script to verify Zo Computer API connectivity"""

import os
import sys
import requests

def load_config():
    """Load configuration from zo-chat config file"""
    config_path = os.path.expanduser("~/.config/zo-chat/config")
    
    if not os.path.exists(config_path):
        print(f"[ERROR] Config file not found at {config_path}")
        print("Run 'zochat' first to set up your credentials")
        return None
    
    try:
        with open(config_path, 'r') as f:
            lines = f.readlines()
            
        config = {}
        for line in lines:
            line = line.strip()
            if '=' in line and not line.startswith('#'):
                key, value = line.split('=', 1)
                config[key] = value.strip('"').strip("'")
        
        return config
    except Exception as e:
        print(f"[ERROR] Error reading config: {e}")
        return None

def test_api():
    """Test API connectivity"""
    config = load_config()
    if not config:
        sys.exit(1)
    
    domain = config.get('DOMAIN', 'zo.computer')
    access_token = config.get('ACCESS_TOKEN')
    
    if not access_token:
        print("[ERROR] ACCESS_TOKEN not found in config")
        sys.exit(1)
    
    print(f"[*] Testing API for: {domain}")
    print(f"[*] Token (first 20 chars): {access_token[:20]}...")
    print()
    
    # Test the workspace-tree endpoint
    url = f"https://{domain}/api/workspace-tree?root=w&showHidden=false"
    
    print(f"[*] Testing endpoint: {url}")
    print()
    
    try:
        response = requests.get(
            url,
            headers={
                'cookie': f'access_token={access_token}',
                'origin': f'https://{domain}'
            },
            timeout=10
        )
        
        print(f"[*] Response Status: {response.status_code}")
        print(f"[*] Response Headers: {dict(response.headers)}")
        print()
        
        if response.status_code == 200:
            data = response.json()
            print("[SUCCESS] API IS WORKING!")
            print()
            print(f"[*] Workspace info:")
            print(f"   Name: {data.get('name', 'N/A')}")
            print(f"   Type: {data.get('type', 'N/A')}")
            print(f"   Children: {len(data.get('children', []))} items")
            if data.get('children'):
                print()
                print("   First few items:")
                for child in data.get('children', [])[:5]:
                    print(f"     - {child.get('name')} ({child.get('type')})")
        else:
            print(f"[ERROR] API ERROR: Status {response.status_code}")
            print(f"Response body: {response.text[:500]}")
            
    except Exception as e:
        print(f"[ERROR] Connection Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    test_api()
