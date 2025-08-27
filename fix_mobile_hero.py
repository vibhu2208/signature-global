#!/usr/bin/env python3
"""
Script to fix mobile hero section layout issues across property pages
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

def add_mobile_hero_fix(file_path):
    """Add mobile hero section fixes"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if mobile hero fix already exists
        if '/* Mobile Hero Section Fix */' in content:
            return False
        
        # Find the existing mobile navbar fix and add hero fix after it
        mobile_navbar_pattern = r'(@media \(max-width: 991\.98px\) \{[^}]+\})'
        
        mobile_hero_fix = '''

/* =====================
   Mobile Hero Section Fix
   ===================== */
@media (max-width: 991.98px) {
  /* Optimize hero height for mobile */
  .hero {
    height: 70vh; /* Reduced from 100vh for better mobile experience */
    min-height: 500px; /* Ensure minimum height */
  }
  
  /* Improve hero image positioning on mobile */
  .hero-img {
    object-position: center center;
    width: 100%;
    height: 100%;
  }
  
  /* Adjust hero overlay for mobile */
  .hero-overlay {
    padding: 0 1.5rem;
    max-width: 90%;
  }
  
  .hero-overlay h1 {
    font-size: clamp(1.5rem, 6vw, 2.5rem);
    line-height: 1.2;
    margin-bottom: 0.5rem;
  }
  
  .hero-overlay p {
    font-size: clamp(0.9rem, 3vw, 1.1rem);
    line-height: 1.4;
  }
}

/* Additional fixes for small phones */
@media (max-width: 575.98px) {
  .hero {
    height: 60vh;
    min-height: 450px;
  }
  
  .hero-overlay {
    padding: 0 1rem;
  }
  
  .hero-overlay h1 {
    font-size: clamp(1.3rem, 7vw, 2rem);
  }
  
  .hero-overlay p {
    font-size: clamp(0.85rem, 3.5vw, 1rem);
  }
}'''
        
        if re.search(mobile_navbar_pattern, content):
            # Add hero fix after the existing mobile navbar fix
            content = re.sub(mobile_navbar_pattern, r'\1' + mobile_hero_fix, content)
        else:
            # Add at the end if no mobile navbar fix found
            content += mobile_hero_fix
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    """Main function to apply mobile hero fixes to all property pages"""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    fixed_count = 0
    
    for prop_dir in property_dirs:
        style_path = os.path.join(base_dir, prop_dir, 'style.css')
        
        if os.path.exists(style_path):
            if add_mobile_hero_fix(style_path):
                print(f"✓ Fixed mobile hero section in {prop_dir}/style.css")
                fixed_count += 1
            else:
                print(f"- Mobile hero fix already exists in {prop_dir}/style.css")
        else:
            print(f"✗ File not found: {style_path}")
    
    print(f"\nCompleted: Fixed mobile hero section in {fixed_count} property pages")

if __name__ == "__main__":
    main()
