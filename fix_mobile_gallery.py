#!/usr/bin/env python3
"""
Script to fix mobile gallery thumbnail section across all property pages
"""

import os
import re

# List of property directories that have the gallery structure
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

def fix_gallery_css(file_path):
    """Fix the mobile gallery CSS in a style.css file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if file has the problematic mobile gallery CSS
        if 'height: 55vh; padding-left: 0; margin-top: 10px; }' in content and 'project_gallery' in content:
            # Replace the problematic line with compact styling
            old_line = '    .swiper-container.nav-slider { width: 100%; height: 55vh; padding-left: 0; margin-top: 10px; }'
            new_replacement = '''    /* Compact horizontal thumbnail strip below */
    .swiper-container.nav-slider { 
      width: 100%; 
      height: 120px; /* Reduced from 55vh to fixed compact height */
      padding-left: 0; 
      margin-top: 10px; 
    }
    /* Ensure thumbnail slides are properly sized */
    .project_gallery .nav-slider .swiper-slide {
      height: 100px;
      width: auto;
    }
    .project_gallery .nav-slider .swiper-slide img {
      height: 100px;
      width: auto;
      object-fit: cover;
    }
  }

  /* Additional mobile refinements for smaller screens */
  @media (max-width: 575.98px) {
    .swiper-container.nav-slider { 
      height: 100px; /* Even more compact on small phones */
    }
    .project_gallery .nav-slider .swiper-slide {
      height: 80px;
    }
    .project_gallery .nav-slider .swiper-slide img {
      height: 80px;
    }'''
            
            if old_line in content:
                content = content.replace(old_line, new_replacement)
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                return True
        
        return False
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    """Main function to apply fixes to all property pages"""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    fixed_count = 0
    
    for prop_dir in property_dirs:
        style_path = os.path.join(base_dir, prop_dir, 'style.css')
        
        if os.path.exists(style_path):
            if fix_gallery_css(style_path):
                print(f"✓ Fixed mobile gallery in {prop_dir}/style.css")
                fixed_count += 1
            else:
                print(f"- No changes needed in {prop_dir}/style.css")
        else:
            print(f"✗ File not found: {style_path}")
    
    print(f"\nCompleted: Fixed mobile gallery thumbnails in {fixed_count} property pages")

if __name__ == "__main__":
    main()
