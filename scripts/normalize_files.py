#!/usr/bin/env python3
"""Fix line endings to Unix format"""
import sys
import os

def fix_file(filepath):
    if not os.path.exists(filepath):
        print(f"Error: File '{filepath}' not found.")
        return

    with open(filepath, 'rb') as f:
        content = f.read()

    # Replace CRLF with LF
    if b'\r\n' in content:
        content = content.replace(b'\r\n', b'\n')
        with open(filepath, 'wb') as f:
            f.write(content)
        print(f"Fixed line endings in: {filepath}")
    else:
        print(f"No changes needed for: {filepath}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for f in sys.argv[1:]:
            fix_file(f)
    else:
        # Default to zochat in parent dir if run from scripts/
        target = '../zochat' if os.path.exists('../zochat') else 'zochat'
        fix_file(target)
