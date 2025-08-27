import os
import re

# Define the font import and CSS variables
FONT_IMPORT = "@import url('https://fonts.googleapis.com/css2?family=TASA+Orbiter:wght@400..800&display=swap');"
FONT_VARIABLES = """  --font-primary: 'TASA Orbiter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
  --font-secondary: 'TASA Orbiter', sans-serif;"""

# Function to update a single CSS file
def update_css_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Add font import if not present
        if "@import url('https://fonts.googleapis.com" not in content:
            content = FONT_IMPORT + '\n\n' + content
        
        # Update :root variables
        if ':root' in content:
            # Add font variables to :root
            if '--font-primary' not in content:
                content = re.sub(
                    r'(:root\s*\{[^}]*)(\})',
                    lambda m: m.group(1) + '\n' + FONT_VARIABLES + '\n' + m.group(2),
                    content,
                    flags=re.DOTALL
                )
        else:
            # Add :root if it doesn't exist
            content = f":root {{{FONT_VARIABLES}}}\n\n{content}"
        
        # Update body font-family
        if 'body' in content or 'body\n' in content or 'body {' in content:
            content = re.sub(
                r'(body\s*\{[^}]*font-family\s*:)[^;]*(;|\n|\})',
                r'\1 var(--font-primary, sans-serif)\2',
                content,
                flags=re.IGNORECASE
            )
        else:
            content = f"body {{ font-family: var(--font-primary, sans-serif); }}\n\n{content}"
        
        # Save the updated content
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
    except Exception as e:
        print(f"Error updating {file_path}: {str(e)}")
        return False

# Main function
def main():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    updated_count = 0
    error_count = 0
    
    # Find all style.css files
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.lower() == 'style.css':
                file_path = os.path.join(root, file)
                print(f"Updating {file_path}...")
                if update_css_file(file_path):
                    updated_count += 1
                else:
                    error_count += 1
    
    print(f"\nUpdate complete!")
    print(f"Updated: {updated_count} files")
    print(f"Errors: {error_count} files")

if __name__ == "__main__":
    main()
