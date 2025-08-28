#!/usr/bin/env python3
"""
Script to add footer phone styling to all project CSS files
"""

import os

def add_footer_phone_css(css_file_path):
    """Add footer phone CSS styling to a CSS file"""
    try:
        with open(css_file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if footer-phone styling already exists
        if '.footer-phone' in content:
            print(f"CSS already exists: {css_file_path}")
            return False
        
        # Add the footer phone CSS at the end of the file
        footer_phone_css = """
/* Footer phone number styling */
.footer-phone {
  font-size: 1.2em;
  font-weight: 600;
  color: #fff;
}
"""
        
        # Append the CSS to the end of the file
        content += footer_phone_css
        
        with open(css_file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Added CSS: {css_file_path}")
        return True
        
    except Exception as e:
        print(f"Error processing {css_file_path}: {e}")
        return False

def main():
    """Main function to add CSS to all style.css files"""
    base_dir = r"c:\Users\100acress.com\Documents\GitHub\signature-global"
    
    # List of directories containing style.css files
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
        css_file_path = os.path.join(base_dir, directory, "style.css")
        if os.path.exists(css_file_path):
            if add_footer_phone_css(css_file_path):
                updated_files += 1
        else:
            print(f"File not found: {css_file_path}")
    
    print(f"\nCompleted! Added CSS to {updated_files} files.")

if __name__ == "__main__":
    main()
