#!/usr/bin/env python3
"""
Enable all languages in languages.json.

This script updates the 'enabled' array to include all available languages.
"""

import json
from pathlib import Path


def main():
    """Enable all languages."""
    lang_file = Path(__file__).parent.parent / "languages.json"
    
    with open(lang_file, 'r', encoding='utf-8') as f:
        config = json.load(f)
    
    # Get all language codes
    all_codes = list(config['languages'].keys())
    
    # Update enabled list
    config['enabled'] = all_codes
    
    # Save
    with open(lang_file, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Enabled {len(all_codes)} languages!")
    print(f"\nLanguages enabled:")
    for code in sorted(all_codes):
        lang_info = config['languages'][code]
        print(f"  {code}: {lang_info['native']} ({lang_info['name']})")


if __name__ == "__main__":
    main()

