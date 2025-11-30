#!/usr/bin/env python3
import re

def fix_zochat():
    with open('zochat', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # 1. Extract the blocks for Case 3 and Case 4
    case_3_start = -1
    case_3_end = -1
    case_4_start = -1
    case_4_end = -1

    for i, line in enumerate(lines):
        if line.strip() == '3)':
            case_3_start = i
        elif line.strip() == '4)':
            if case_3_start != -1 and case_3_end == -1:
                case_3_end = i
            case_4_start = i
        elif line.strip() == '5)':
            if case_4_start != -1:
                case_4_end = i
                break

    if case_3_start == -1 or case_4_start == -1:
        print("Could not find cases 3 and 4")
        return

    case_3_lines = lines[case_3_start:case_3_end]
    case_4_lines = lines[case_4_start:case_4_end]

    # 2. Identify which is which
    # Check if case 3 is actually billing
    is_case_3_billing = any("billing" in line.lower() for line in case_3_lines[:10])
    
    # Check if case 4 is actually services
    is_case_4_services = any("User Services" in line for line in case_4_lines[:10])

    final_case_3 = []
    final_case_4 = []

    if is_case_3_billing and is_case_4_services:
        print("Swapping cases: Case 3 (Billing) <-> Case 4 (Services)")
        final_case_3 = case_4_lines
        final_case_4 = case_3_lines
    else:
        print("Cases seem correct or unclear, checking individual content")
        final_case_3 = case_3_lines
        final_case_4 = case_4_lines

    # 3. Fix Syntax in Billing (now in final_case_4)
    # It needs an opening ( before the logic starts if it ends with ) | less -R
    # And correct the case number to 4)
    final_case_4[0] = "        4)\n"
    
    # Find where to insert (
    # Look for "Fetching billing information"
    insert_idx = -1
    for i, line in enumerate(final_case_4):
        if "Fetching billing information" in line:
            insert_idx = i
            break
    
    if insert_idx != -1:
        # Check if ( is already there
        if "(" not in final_case_4[insert_idx-1]:
             final_case_4.insert(insert_idx, "            (\n")
             print("Added missing ( to Billing case")

    # 4. Fix Syntax in User Services (now in final_case_3)
    # It needs correct case number 3)
    final_case_3[0] = "        3)\n"
    
    # Inside User Services, check Option 1 (List Services) for missing (
    # Look for "Fetching services..."
    insert_idx = -1
    for i, line in enumerate(final_case_3):
        if "Fetching services..." in line:
            insert_idx = i
            break
            
    if insert_idx != -1:
         # Check if ( is already there
        if "(" not in final_case_3[insert_idx-1]:
             final_case_3.insert(insert_idx, "                        (\n")
             print("Added missing ( to User Services -> List Services")

    # 5. Reconstruct file
    new_lines = lines[:case_3_start] + final_case_3 + final_case_4 + lines[case_4_end:]
    
    with open('zochat', 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    
    print("File fixed successfully")

if __name__ == "__main__":
    fix_zochat()
