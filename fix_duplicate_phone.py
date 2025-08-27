#!/usr/bin/env python3
"""
Script to fix duplicate phone numbers in mobile navbar for property pages
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

def fix_duplicate_phone_numbers(file_path):
    """Fix duplicate phone numbers in mobile navbar"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find the existing mobile navbar fix section
        mobile_fix_pattern = r'(/\* =====================\s+Mobile Navbar Fix - Hide hamburger and nav links\s+===================== \*/\s+@media \(max-width: 991\.98px\) \{[^}]+\})'
        
        if re.search(mobile_fix_pattern, content, re.DOTALL):
            # Replace the existing mobile navbar fix with updated version
            new_mobile_fix = '''/* =====================
   Mobile Navbar Fix - Hide hamburger and nav links
   ===================== */
@media (max-width: 991.98px) {
  /* Hide hamburger and nav links in mobile view */
  .navbar-toggler,
  .navbar-collapse {
    display: none !important;
  }
  
  /* Hide desktop phone number to avoid duplicates */
  .call-btn.d-none.d-lg-inline-flex {
    display: none !important;
  }
  
  /* Show only mobile phone number on right side */
  .call-btn.d-inline-flex.d-lg-none {
    display: inline-flex !important;
    order: 3;
    margin-left: auto;
  }
  
  /* Logo on left side */
  .navbar-brand {
    order: 1;
    margin-right: auto;
  }
  
  /* Adjust container for proper left-right layout */
  .navbar .container-fluid {
    justify-content: space-between;
    align-items: center;
  }
}'''
            
            content = re.sub(mobile_fix_pattern, new_mobile_fix, content, flags=re.DOTALL)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return True
        
        return False
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    """Main function to fix duplicate phone numbers in all property pages"""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    fixed_count = 0
    
    for prop_dir in property_dirs:
        style_path = os.path.join(base_dir, prop_dir, 'style.css')
        
        if os.path.exists(style_path):
            if fix_duplicate_phone_numbers(style_path):
                print(f"✓ Fixed duplicate phone numbers in {prop_dir}/style.css")
                fixed_count += 1
            else:
                print(f"- No mobile navbar fix found in {prop_dir}/style.css")
        else:
            print(f"✗ File not found: {style_path}")
    
    print(f"\nCompleted: Fixed duplicate phone numbers in {fixed_count} property pages")

if __name__ == "__main__":
    main()
