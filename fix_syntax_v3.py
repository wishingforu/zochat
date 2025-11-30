#!/usr/bin/env python3
import sys

def fix_zochat():
    with open('zochat', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Find start of cases with strict indentation (8 spaces)
    case_3_idx = -1
    case_4_idx = -1
    case_5_idx = -1

    for i, line in enumerate(lines):
        # Check for exactly 8 spaces followed by 3)
        if line.startswith('        3)'):
            case_3_idx = i
        elif line.startswith('        4)'):
            case_4_idx = i
        elif line.startswith('        5)'):
            case_5_idx = i
            if case_3_idx != -1 and case_4_idx != -1:
                break
    
    print(f"Found indices: 3)={case_3_idx}, 4)={case_4_idx}, 5)={case_5_idx}")

    if case_3_idx == -1 or case_4_idx == -1 or case_5_idx == -1:
        print("Error: Could not find all case markers with correct indentation")
        # Fallback: try to find them even if out of order
        # If 3 is after 4, we might have issues.
        return

    # Extract blocks
    # Block A: from case_3_idx to case_4_idx
    # Block B: from case_4_idx to case_5_idx
    
    # But wait, if they are swapped in the file, case_4_idx might be < case_3_idx?
    # Let's handle that.
    
    first_idx = min(case_3_idx, case_4_idx)
    second_idx = max(case_3_idx, case_4_idx)
    
    # If 3 comes before 4
    if case_3_idx < case_4_idx:
        block_3 = lines[case_3_idx:case_4_idx]
        block_4 = lines[case_4_idx:case_5_idx]
    else:
        # 4 comes before 3 (swapped in file?)
        block_4 = lines[case_4_idx:case_3_idx]
        block_3 = lines[case_3_idx:case_5_idx]

    # Check content
    is_block_3_billing = any("billing" in line.lower() for line in block_3[:20])
    is_block_4_services = any("User Services" in line for line in block_4[:20])

    print(f"Block 3 (from line {case_3_idx}) is billing: {is_block_3_billing}")
    print(f"Block 4 (from line {case_4_idx}) is services: {is_block_4_services}")

    final_case_3 = []
    final_case_4 = []

    # We want Case 3 to be Services, Case 4 to be Billing
    if is_block_3_billing:
        print("Block 3 is Billing -> Moving to Case 4")
        final_case_4 = block_3
        final_case_3 = block_4 # Assuming block 4 is services
    else:
        print("Block 3 is likely Services -> Keeping as Case 3")
        final_case_3 = block_3
        final_case_4 = block_4

    # Ensure Case Numbers are correct
    final_case_3[0] = "        3)\n"
    final_case_4[0] = "        4)\n"

    # Fix Syntax in Billing (final_case_4)
    for i, line in enumerate(final_case_4):
        if "Fetching billing information" in line:
            has_paren = False
            for j in range(max(0, i-5), i):
                if "(" in final_case_4[j] and "echo" not in final_case_4[j]:
                    has_paren = True
            if not has_paren:
                final_case_4.insert(i, "            (\n")
                print("Fixed Billing syntax: Added (")
            break

    # Fix Syntax in Services (final_case_3)
    for i, line in enumerate(final_case_3):
        if "Fetching services..." in line:
            has_paren = False
            for j in range(max(0, i-5), i):
                if "(" in final_case_3[j] and "echo" not in final_case_3[j]:
                    has_paren = True
            if not has_paren:
                final_case_3.insert(i, "                        (\n")
                print("Fixed Services syntax: Added (")
            break

    # Reconstruct file
    # We replace the whole chunk from first_idx to case_5_idx with final_case_3 + final_case_4
    
    start_replace = min(case_3_idx, case_4_idx)
    end_replace = case_5_idx
    
    final_lines = lines[:start_replace] + final_case_3 + final_case_4 + lines[end_replace:]

    with open('zochat', 'w', encoding='utf-8') as f:
        f.writelines(final_lines)
    
    print("File updated successfully")

if __name__ == "__main__":
    fix_zochat()
