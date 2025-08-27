import os
import re

# List of property directories that have brochure buttons
property_dirs = [
    'SignatureIndustrialandITPlots',
    'SignatureGlobalDaxinVistas', 
    'SignatureGlobalTwinTower',
    'signature-global-deluxe-dxp',
    'signature-global-city-79b',
    'signature-global-city-81',
    'signature-global-city-92',
    'signature-global-city-92-2',
    'signature-global-city-37D-phase-2',
    'signature-global-city-63a',
    'CityOfColours',
    'Cloverdale',
    'global-sco-37D',
    'global-sco-88a'
]

def remove_brochure_button_from_html(file_path):
    """Remove the brochure button HTML from index.html"""
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return False
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove the floating download brochure button HTML block
    brochure_button_pattern = r'\s*<!-- Floating Download Brochure Button -->\s*<a href="#" class="brochure-btn"[^>]*>.*?</a>\s*'
    content = re.sub(brochure_button_pattern, '\n', content, flags=re.DOTALL)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Removed brochure button from: {file_path}")
    return True

def remove_brochure_css_from_style(file_path):
    """Remove the brochure button CSS from style.css"""
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return False
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove the brochure button CSS block
    css_pattern = r'\s*/\* Floating Download Brochure Button \*/.*?(?=\s*/\*|\s*@media|\s*$)'
    content = re.sub(css_pattern, '\n', content, flags=re.DOTALL)
    
    # Also remove any remaining brochure-btn specific styles
    brochure_css_pattern = r'\s*\.brochure-btn[^}]*}\s*'
    content = re.sub(brochure_css_pattern, '\n', content, flags=re.DOTALL)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Removed brochure CSS from: {file_path}")
    return True

# Process all property directories
for dir_name in property_dirs:
    html_file = os.path.join(dir_name, 'index.html')
    css_file = os.path.join(dir_name, 'style.css')
    
    print(f"\nProcessing {dir_name}...")
    
    # Remove from HTML
    remove_brochure_button_from_html(html_file)
    
    # Remove from CSS
    remove_brochure_css_from_style(css_file)

print("\nBrochure button removal completed!")
