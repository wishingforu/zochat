#!/usr/bin/env python3
import re
import sys

with open('zochat', 'r') as f:
    content = f.read()

# 1. Update menu display (lines 132-137)
content = re.sub(
    r'(echo -e "  \$\{CYAN\}\[1\]\$\{RESET\} \$\{BOLD\}Chat with AI\$\{RESET\}      - Start a conversation"\n)'
    r'(    echo -e "  \$\{CYAN\}\[2\]\$\{RESET\} \$\{BOLD\}Events\$\{RESET\}            - View and schedule tasks"\n)'
    r'(    echo -e "  \$\{CYAN\}\[3\]\$\{RESET\} \$\{BOLD\}View Billing\$\{RESET\}      - Credits and usage"\n)'
    r'(    echo -e "  \$\{CYAN\}\[4\]\$\{RESET\} \$\{BOLD\}User Services\$\{RESET\}     - Manage services"\n)'
    r'(    echo -e "  \$\{CYAN\}\[5\]\$\{RESET\} \$\{BOLD\}Update Tool\$\{RESET\}       - Get latest version"\n)'
    r'(    echo -e "  \$\{CYAN\}\[6\]\$\{RESET\} \$\{BOLD\}Exit\$\{RESET\}              - Close application")',
    r'\1\2    echo -e "  ${CYAN}[3]${RESET} ${BOLD}User Services${RESET}     - Manage services"\n'
    r'    echo -e "  ${CYAN}[4]${RESET} ${BOLD}View Billing${RESET}      - Credits and usage"\n'
    r'    echo -e "  ${CYAN}[5]${RESET} ${BOLD}Exit${RESET}              - Close application"',
    content
)

# 2. Find and renumber case 3 (View Billing) to 4
content = re.sub(r'(\s+)3\)\n(\s+# View billing)', r'\g<1>4)\n\2', content)

# 3. Rename case 4 to 3 (User Services)
content = re.sub(r'(\s+)4\)\n(\s+# User Services)', r'\g<1>3)\n\2', content)

# 4. Remove case 5 (Update Tool)
content = re.sub(
    r'        5\)\n            update_script\n            ;;\n',
    '',
    content
)

# 5. Rename case 6 to 5 (Exit)
content = re.sub(r'(\s+)6\)\n(\s+echo ""\n\s+echo -e "\$\{DIM\}Goodbye)', r'\g<1>5)\n\2', content)

with open('zochat', 'w') as f:
    f.write(content)

print("Menu reorganized successfully!")
