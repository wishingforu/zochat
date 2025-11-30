#!/bin/bash
# Simple targeted sed script to reorganize menu

cd /c/Users/danie/OneDrive/Desktop/zochat

# 1. Fix menu display lines (132-137)
sed -i '132s/\[3\].*View Billing/[3]${RESET} ${BOLD}User Services${RESET}     - Manage services/' zochat
sed -i '133s/\[4\].*User Services/[4]${RESET} ${BOLD}View Billing${RESET}      - Credits and usage/' zochat
sed -i '134d' zochat  # Delete line 134 ([5] Update Tool)
sed -i '134s/\[6\].*Exit/[5]${RESET} ${BOLD}Exit${RESET}              - Close application/' zochat

# 2. Change case 3) from Billing to Services
sed -i '269s/# View billing information/# User Services Management/' zochat

# 3. Change case 4) from Services to Billing  
sed -i '389s/# User Services Management/# View billing information/' zochat

# 4. Remove case 5 (Update Tool) - lines 540-543
sed -i '540,543d' zochat

# 5. Change case 6 to case 5 (Exit)
sed -i '540s/        6)/        5)/' zochat

echo "Done! Menu reorganized."
