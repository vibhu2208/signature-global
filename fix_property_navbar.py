#!/usr/bin/env python3
"""
Script to hide hamburger menu and nav links in mobile view for property pages
"""

import os
import re

# List of property directories
property_dirs = [
    'CityOfColours',
    'Cloverdale',
    'SignatureGlobalDaxinVistas',
    'SignatureGlobalTwinTower', 
    'SignatureIndustrialandITPlots',
    'global-sco-37D',
    'global-sco-88a',
    'signature-global-city-37D-phase-2',
    'signature-global-city-63a',
    'signature-global-city-79b',
    'signature-global-city-81',
    'signature-global-city-92',
    'signature-global-city-92-2',
    'signature-global-city-93',
    'signature-global-deluxe-dxp',
    'signature-titanium'
]

def add_mobile_navbar_fix(file_path):
    """Add mobile navbar fix to hide hamburger and nav links"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if the fix is already applied
        if '/* Hide hamburger and nav links in mobile view */' in content:
            return False
        
        # Find the end of the file or a good place to add the mobile fix
        mobile_fix = '''
/* =====================
   Mobile Navbar Fix - Hide hamburger and nav links
   ===================== */
@media (max-width: 991.98px) {
  /* Hide hamburger and nav links in mobile view */
  .navbar-toggler,
  .navbar-collapse {
    display: none !important;
  }
  
  /* Ensure phone number stays visible and properly positioned */
  .call-btn {
    display: inline-flex !important;
  }
  
  /* Center the logo in mobile */
  .navbar-brand {
    margin: 0 auto;
  }
  
  /* Adjust container for better mobile layout */
  .navbar .container-fluid {
    justify-content: space-between;
  }
}'''
        
        # Add the fix at the end of the file
        content += mobile_fix
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    """Main function to apply navbar fixes to all property pages"""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    fixed_count = 0
    
    for prop_dir in property_dirs:
        style_path = os.path.join(base_dir, prop_dir, 'style.css')
        
        if os.path.exists(style_path):
            if add_mobile_navbar_fix(style_path):
                print(f"✓ Fixed mobile navbar in {prop_dir}/style.css")
                fixed_count += 1
            else:
                print(f"- Mobile navbar fix already exists in {prop_dir}/style.css")
        else:
            print(f"✗ File not found: {style_path}")
    
    print(f"\nCompleted: Fixed mobile navbar in {fixed_count} property pages")

if __name__ == "__main__":
    main()
