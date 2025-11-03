#!/usr/bin/env python3
"""
Create English translation templates from Portuguese content.

This script reads Portuguese Markdown files and creates corresponding
English files with translation placeholders.

Usage:
    python scripts/create-translation-template.py
"""

import os
import re
from pathlib import Path


def extract_frontmatter(content):
    """Extract frontmatter from content."""
    if not content.startswith('---'):
        return {}, content
    
    match = re.match(r'^---\n(.*?)\n---\n(.*)$', content, re.DOTALL)
    if match:
        frontmatter_text = match.group(1)
        body = match.group(2)
        
        # Parse frontmatter
        frontmatter = {}
        for line in frontmatter_text.split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                key = key.strip()
                value = value.strip().strip('"').strip("'")
                frontmatter[key] = value
        
        return frontmatter, body
    
    return {}, content


def create_translation_template(pt_file, en_file):
    """Create English translation template from Portuguese file."""
    with open(pt_file, 'r', encoding='utf-8') as f:
        pt_content = f.read()
    
    frontmatter, body = extract_frontmatter(pt_content)
    
    # Update frontmatter for English
    frontmatter['lang'] = 'en'
    if 'title' in frontmatter:
        frontmatter['title'] = f"[EN] {frontmatter['title']}"
    
    # Create English frontmatter
    en_frontmatter = "---\n"
    for key, value in frontmatter.items():
        en_frontmatter += f"{key}: {value}\n"
    en_frontmatter += "---\n\n"
    
    # Add translation placeholder in body
    en_body = f"[Translation needed]\n\n{body}"
    
    en_content = en_frontmatter + en_body
    
    # Ensure parent directory exists
    os.makedirs(os.path.dirname(en_file), exist_ok=True)
    
    with open(en_file, 'w', encoding='utf-8') as f:
        f.write(en_content)
    
    print(f"Created: {en_file}")


def main():
    docs_dir = Path(__file__).parent.parent / "docs"
    pt_dir = docs_dir / "pt"
    en_dir = docs_dir / "en"
    
    if not pt_dir.exists():
        print(f"Portuguese directory not found: {pt_dir}")
        return
    
    # Find all Portuguese Markdown files
    pt_files = list(pt_dir.rglob('*.md'))
    
    created = 0
    for pt_file in pt_files:
        # Calculate relative path
        rel_path = pt_file.relative_to(pt_dir)
        en_file = en_dir / rel_path
        
        # Skip if English file already exists
        if en_file.exists():
            print(f"Skipped (exists): {en_file}")
            continue
        
        create_translation_template(pt_file, en_file)
        created += 1
    
    print(f"\nTotal templates created: {created}")


if __name__ == "__main__":
    main()

