#!/usr/bin/env python3
"""Fix line endings to Unix format"""

with open('zochat', 'rb') as f:
    content = f.read()

# Replace CRLF with LF
content = content.replace(b'\r\n', b'\n')

with open('zochat', 'wb') as f:
    f.write(content)

print("Line endings fixed!")
