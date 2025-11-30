#!/bin/bash

# Read the file
cp zochat zochat.bak

# Simple sed replacements in order
sed -i 's/\[3\].*View Billing.*Credits/[3]${RESET} ${BOLD}User Services${RESET}     - Manage services/; 
s/\[4\].*User Services.*Manage/[4]${RESET} ${BOLD}View Billing${RESET}      - Credits and usage/; 
/\[5\].*Update Tool/d; 
s/\[6\].*Exit/[5]${RESET} ${BOLD}Exit${RESET}              - Close application/' zochat

# Now fix the case numbers  
# Change "        3)" where comment is "# View billing" to    " 4)"
sed -i '/View billing/{N;s/        3)/        4)/}' zochat

# Change "        4)" where comment is "# User Services" to "        3)"
sed -i '/User Services Management/{N;s/        4)/        3)/}' zochat

# Remove the update_script case (5)
sed -i '/^        5)$/,/^            ;;$/{ /update_script/,/;;/d; }' zochat

# Change "        6)" where comment has "Goodbye" to "        5)"
sed -i '/Goodbye/{s/        6)/        5)/}' zochat

echo "Done!"
