#!/usr/bin/env python3
"""
Script to update footer information across all HTML files:
- Remove email line (info@signatureglobal.in or info@example.com)
- Remove Sector 92, Gurugram location line
- Update phone numbers to 8527134491
"""

import os
import re

def update_footer_in_file(file_path):
    """Update footer content in a single HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Remove email line (both variations)
        content = re.sub(r'\s*<li><i class="fa-solid fa-envelope"></i> info@signatureglobal\.in</li>\s*\n?', '', content)
        content = re.sub(r'\s*<li><i class="fa-solid fa-envelope"></i> info@example\.com</li>\s*\n?', '', content)
        
        # Remove Sector 92, Gurugram location line
        content = re.sub(r'\s*<li><i class="fa-solid fa-location-dot"></i> Sector 92, Gurugram</li>\s*\n?', '', content)
        
        # Update phone numbers to 8527134491
        content = re.sub(r'<li><i class="fa-solid fa-phone"></i> \+91 \d+(?: \d+)*</li>', 
                        '<li><i class="fa-solid fa-phone"></i> +91 8527134491</li>', content)
        
        # Write back if changes were made
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated: {file_path}")
            return True
        else:
            print(f"No changes needed: {file_path}")
            return False
            
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    """Main function to update all HTML files"""
    base_dir = r"c:\Users\100acress.com\Documents\GitHub\signature-global"
    
    # List of directories containing index.html files
    directories = [
        ".",  # Root directory
        "CityOfColours",
        "Cloverdale", 
        "SignatureGlobalDaxinVistas",
        "SignatureGlobalTwinTower",
        "SignatureIndustrialandITPlots",
        "global-sco-37D",
        "global-sco-88a",
        "signature-global-city-37D-phase-2",
        "signature-global-city-63a",
        "signature-global-city-79b",
        "signature-global-city-81",
        "signature-global-city-92",
        "signature-global-city-92-2",
        "signature-global-city-93",
        "signature-global-deluxe-dxp",
        "signature-titanium"
    ]
    
    updated_files = 0
    
    for directory in directories:
        file_path = os.path.join(base_dir, directory, "index.html")
        if os.path.exists(file_path):
            if update_footer_in_file(file_path):
                updated_files += 1
        else:
            print(f"File not found: {file_path}")
    
    print(f"\nCompleted! Updated {updated_files} files.")

if __name__ == "__main__":
    main()
