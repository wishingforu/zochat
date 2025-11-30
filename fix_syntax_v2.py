#!/usr/bin/env python3
import sys

def fix_zochat():
    with open('zochat', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Find start of cases
    case_3_idx = -1
    case_4_idx = -1
    case_5_idx = -1

    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped == '3)':
            case_3_idx = i
        elif stripped == '4)':
            case_4_idx = i
        elif stripped == '5)':
            case_5_idx = i
            # We found all we need (assuming they are in order 3, 4, 5)
            if case_3_idx != -1 and case_4_idx != -1:
                break
    
    print(f"Found indices: 3)={case_3_idx}, 4)={case_4_idx}, 5)={case_5_idx}")

    if case_3_idx == -1 or case_4_idx == -1 or case_5_idx == -1:
        print("Error: Could not find all case markers")
        return

    # Extract blocks
    # Block 3 goes from case_3_idx to case_4_idx - 1
    block_3 = lines[case_3_idx:case_4_idx]
    
    # Block 4 goes from case_4_idx to case_5_idx - 1
    block_4 = lines[case_4_idx:case_5_idx]

    # Check content to confirm identity
    is_block_3_billing = any("billing" in line.lower() for line in block_3[:10])
    is_block_4_services = any("User Services" in line for line in block_4[:10])

    print(f"Block 3 is billing: {is_block_3_billing}")
    print(f"Block 4 is services: {is_block_4_services}")

    new_block_3 = []
    new_block_4 = []

    # Swap if needed (Block 3 has Billing, Block 4 has Services -> Swap)
    if is_block_3_billing and is_block_4_services:
        print("Swapping blocks...")
        new_block_3 = block_4
        new_block_4 = block_3
    else:
        print("Not swapping blocks (already correct or unknown)")
        new_block_3 = block_3
        new_block_4 = block_4

    # Fix Case Numbers
    new_block_3[0] = new_block_3[0].replace('4)', '3)', 1)
    new_block_4[0] = new_block_4[0].replace('3)', '4)', 1)

    # Fix Syntax in Billing (now new_block_4)
    # Needs ( before "Fetching billing information"
    for i, line in enumerate(new_block_4):
        if "Fetching billing information" in line:
            # Check previous lines for (
            has_paren = False
            for j in range(max(0, i-5), i):
                if "(" in new_block_4[j] and "echo" not in new_block_4[j]:
                    has_paren = True
            
            if not has_paren:
                # Insert ( at i-1 (after echo "")
                new_block_4.insert(i, "            (\n")
                print("Fixed Billing syntax: Added (")
            break

    # Fix Syntax in Services (now new_block_3)
    # Needs ( inside Option 1
    for i, line in enumerate(new_block_3):
        if "Fetching services..." in line:
             # Check previous lines for (
            has_paren = False
            for j in range(max(0, i-5), i):
                if "(" in new_block_3[j] and "echo" not in new_block_3[j]:
                    has_paren = True
            
            if not has_paren:
                # Insert ( at i-1 (after echo "")
                new_block_3.insert(i, "                        (\n")
                print("Fixed Services syntax: Added (")
            break

    # Reconstruct file
    final_lines = lines[:case_3_idx] + new_block_3 + new_block_4 + lines[case_5_idx:]

    with open('zochat', 'w', encoding='utf-8') as f:
        f.writelines(final_lines)
    
    print("File updated successfully")

if __name__ == "__main__":
    fix_zochat()
