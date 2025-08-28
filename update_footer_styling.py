#!/usr/bin/env python3
"""
Script to update footer styling across all HTML files:
1. Update copyright text from "Your Project" to "Signature Global"
2. Increase phone number size in footers by adding CSS class
"""

import os
import re

def update_footer_styling_in_file(file_path):
    """Update footer styling in a single HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Update copyright text from "Your Project" to "Signature Global"
        content = re.sub(
            r'© <span id="year"></span> Your Project\. All rights reserved\.',
            '© <span id="year"></span> Signature Global. All rights reserved.',
            content
        )
        
        # Add CSS class to phone number in footer for larger size
        content = re.sub(
            r'<li><i class="fa-solid fa-phone"></i> (\+91 \d+(?: \d+)*)</li>',
            r'<li><i class="fa-solid fa-phone"></i> <span class="footer-phone">\1</span></li>',
            content
        )
        
        # Add CSS styling for footer phone numbers if not already present
        if 'footer-phone' in content and '.footer-phone' not in content:
            # Find the closing </style> tag and add CSS before it
            style_pattern = r'(</style>)'
            if re.search(style_pattern, content):
                css_addition = """
    /* Footer phone number styling */
    .footer-phone {
      font-size: 1.1em;
      font-weight: 600;
      color: #fff;
    }
    """
                content = re.sub(style_pattern, css_addition + r'\1', content)
        
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
            if update_footer_styling_in_file(file_path):
                updated_files += 1
        else:
            print(f"File not found: {file_path}")
    
    print(f"\nCompleted! Updated {updated_files} files.")

if __name__ == "__main__":
    main()
