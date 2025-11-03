#!/usr/bin/env python3
"""
Add or update language frontmatter in Markdown files.

Usage:
    python scripts/update-lang-frontmatter.py <lang> <directory>
    
Example:
    python scripts/update-lang-frontmatter.py pt docs/pt/
    python scripts/update-lang-frontmatter.py en docs/en/
"""

import sys
import os
import re
from pathlib import Path


def update_frontmatter(file_path, lang):
    """Add or update lang field in frontmatter."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if file has frontmatter
    if not content.startswith('---'):
        # Add frontmatter at the beginning
        content = f"---\nlang: {lang}\n---\n\n{content}"
    else:
        # Extract frontmatter
        frontmatter_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
        if frontmatter_match:
            frontmatter = frontmatter_match.group(1)
            body = content[frontmatter_match.end():].lstrip()
            
            # Check if lang already exists
            if re.search(r'^lang:', frontmatter, re.MULTILINE):
                # Update existing lang
                frontmatter = re.sub(r'^lang:.*$', f'lang: {lang}', frontmatter, flags=re.MULTILINE)
            else:
                # Add lang to frontmatter
                frontmatter = f"{frontmatter}\nlang: {lang}"
            
            content = f"---\n{frontmatter}\n---\n\n{body}"
        else:
            # Malformed frontmatter, add lang at start
            content = f"---\nlang: {lang}\n---\n\n{content}"
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True


def process_directory(directory, lang):
    """Process all Markdown files in directory recursively."""
    directory = Path(directory)
    if not directory.exists():
        print(f"Directory not found: {directory}")
        return
    
    md_files = list(directory.rglob('*.md'))
    updated = 0
    
    for md_file in md_files:
        try:
            update_frontmatter(md_file, lang)
            updated += 1
            print(f"Updated: {md_file}")
        except Exception as e:
            print(f"Error processing {md_file}: {e}")
    
    print(f"\nTotal files updated: {updated}")


def main():
    if len(sys.argv) != 3:
        print("Usage: python update-lang-frontmatter.py <lang> <directory>")
        print("Example: python update-lang-frontmatter.py pt docs/pt/")
        sys.exit(1)
    
    lang = sys.argv[1]
    directory = sys.argv[2]
    
    if lang not in ['pt', 'en']:
        print("Language must be 'pt' or 'en'")
        sys.exit(1)
    
    process_directory(directory, lang)


if __name__ == "__main__":
    main()

