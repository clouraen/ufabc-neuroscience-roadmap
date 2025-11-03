#!/usr/bin/env python3
"""
Generate language folders and templates for all languages from languages.json.

This script creates the folder structure and index files for all enabled languages.
"""

import json
import os
from pathlib import Path


def load_languages():
    """Load languages configuration."""
    lang_file = Path(__file__).parent.parent / "languages.json"
    with open(lang_file, 'r', encoding='utf-8') as f:
        return json.load(f)


def create_language_index(docs_dir, lang_code, lang_info):
    """Create index.md for a language."""
    lang_dir = docs_dir / lang_code
    lang_dir.mkdir(parents=True, exist_ok=True)
    
    index_file = lang_dir / "index.md"
    
    if index_file.exists():
        print(f"Skipped (exists): {index_file}")
        return
    
    title = lang_info.get('name', lang_code.upper())
    native = lang_info.get('native', title)
    flag = lang_info.get('flag', '🌐')
    
    content = f"""---
title: "Welcome to Cleiton Moura Loura's NeuroBlog"
lang: {lang_code}
date: 2024-01-01
---

{{% include language-switcher.html %}}

# 🧠 Welcome to My Computational Neuroscience Journey

Hello! This is my public learning journal tracking my journey from ENEM preparation to becoming a computational neuroscience researcher at UFABC.

## 🗺️ Navigation

- **[ENEM 2026 Studies](/{lang_code}/enem2026/)** - Weekly study logs and progress
- **[Neuroscience Learning](/{lang_code}/neuroscience/)** - Courses, notes, and open-source projects
- **[Blog Posts](/{lang_code}/blog/)** - Reflections on my academic journey

## 📊 Current Phase

Currently in **Phase 1: Foundations** (2024-2025)
- Building ENEM fundamentals
- Learning Python basics
- Introduction to computational neuroscience

## 🎯 Goals

1. ✅ Enter UFABC via ENEM 2026
2. ✅ Specialize in Computational Neuroscience
3. ✅ Grow through open-source research
4. ✅ Pursue scholarships: PIBIC → FAPESP → BEPE → Master's

---

*"Open knowledge is the future of neuroscience."* — Ross Markello

---
*[Translation needed - {native}]*
"""
    
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Created: {index_file}")


def create_language_folders(docs_dir, lang_code):
    """Create standard folder structure for a language."""
    lang_dir = docs_dir / lang_code
    folders = ['enem2026', 'neuroscience', 'blog', 'templates']
    
    for folder in folders:
        (lang_dir / folder).mkdir(parents=True, exist_ok=True)
    
    print(f"Created folders for: {lang_code}")


def main():
    """Main function."""
    config = load_languages()
    docs_dir = Path(__file__).parent.parent / "docs"
    
    all_languages = config.get('languages', {})
    enabled = config.get('enabled', ['pt', 'en'])
    
    print(f"Total languages available: {len(all_languages)}")
    print(f"Currently enabled: {enabled}")
    print(f"\nTo enable all languages, update 'enabled' in languages.json\n")
    
    # Create folders for enabled languages
    for lang_code in enabled:
        if lang_code in all_languages:
            lang_info = all_languages[lang_code]
            create_language_folders(docs_dir, lang_code)
            create_language_index(docs_dir, lang_code, lang_info)
        else:
            print(f"Warning: Language code '{lang_code}' not found in languages.json")
    
    # Optionally create for all languages (uncomment to enable)
    # print("\nCreating for ALL languages...")
    # for lang_code, lang_info in all_languages.items():
    #     create_language_folders(docs_dir, lang_code)
    #     create_language_index(docs_dir, lang_code, lang_info)
    
    print("\nDone!")


if __name__ == "__main__":
    main()

