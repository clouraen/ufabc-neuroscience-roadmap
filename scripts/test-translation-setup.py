#!/usr/bin/env python3
"""
Test translation setup - verifies everything is configured correctly
"""

import json
import sys
from pathlib import Path

def test_setup():
    """Test if translation setup is correct."""
    
    print("="*70)
    print("TRANSLATION SETUP TEST")
    print("="*70)
    print()
    
    success = True
    
    # Test 1: Check languages.json
    print("✓ Test 1: Checking languages.json...")
    lang_file = Path('languages.json')
    if not lang_file.exists():
        print("  ❌ languages.json not found!")
        success = False
    else:
        with open(lang_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            total_langs = len(data.get('languages', {}))
            enabled_langs = len(data.get('enabled', []))
            print(f"  ✓ Found {total_langs} language definitions")
            print(f"  ✓ {enabled_langs} languages enabled")
            print(f"  ✓ Default language: {data.get('default', 'not set')}")
    
    print()
    
    # Test 2: Check Portuguese content
    print("✓ Test 2: Checking Portuguese content...")
    pt_dir = Path('docs/pt')
    if not pt_dir.exists():
        print("  ❌ docs/pt directory not found!")
        success = False
    else:
        pt_files = list(pt_dir.rglob('*.md'))
        print(f"  ✓ Found {len(pt_files)} Portuguese markdown files")
        if pt_files:
            print("  ✓ Sample files:")
            for f in pt_files[:5]:
                print(f"     - {f.relative_to(pt_dir)}")
            if len(pt_files) > 5:
                print(f"     ... and {len(pt_files) - 5} more")
    
    print()
    
    # Test 3: Check scripts
    print("✓ Test 3: Checking translation scripts...")
    scripts = [
        'scripts/translate-content.py',
        'scripts/batch-translate.py',
        'scripts/batch-translate.sh'
    ]
    for script in scripts:
        script_path = Path(script)
        if script_path.exists():
            print(f"  ✓ {script} found")
        else:
            print(f"  ❌ {script} not found!")
            success = False
    
    print()
    
    # Test 4: Check API key
    print("✓ Test 4: Checking API configuration...")
    import os
    api_key = os.getenv('OPENAI_API_KEY')
    if api_key:
        print(f"  ✓ OPENAI_API_KEY is set ({api_key[:8]}...{api_key[-4:]})")
    else:
        print("  ⚠️  OPENAI_API_KEY not set (required for translation)")
        print("     Set with: export OPENAI_API_KEY='your-key'")
    
    base_url = os.getenv('OPENAI_BASE_URL', 'https://api.openai.com/v1')
    print(f"  ✓ API Base URL: {base_url}")
    
    model = os.getenv('OPENAI_API_MODEL', 'gpt-4o-mini')
    print(f"  ✓ Model: {model}")
    
    print()
    
    # Test 5: Estimate translation scope
    print("✓ Test 5: Estimating translation scope...")
    if pt_dir.exists() and lang_file.exists():
        pt_files = list(pt_dir.rglob('*.md'))
        with open(lang_file, 'r') as f:
            data = json.load(f)
            target_langs = [l for l in data.get('enabled', []) if l != 'pt']
        
        total_translations = len(pt_files) * len(target_langs)
        print(f"  ✓ Source files: {len(pt_files)}")
        print(f"  ✓ Target languages: {len(target_langs)}")
        print(f"  ✓ Total translations needed: {total_translations}")
        print(f"  ✓ Estimated API calls: ~{total_translations}")
        
        # Cost estimation (rough)
        cost_per_call = 0.002  # ~$0.002 per translation with gpt-4o-mini
        estimated_cost = total_translations * cost_per_call
        print(f"  ✓ Estimated cost: ${estimated_cost:.2f} - ${estimated_cost*2:.2f}")
    
    print()
    print("="*70)
    
    if success:
        print("✅ SETUP TEST PASSED")
        print()
        print("You can now run translation:")
        print("  ./scripts/batch-translate.sh --dry-run    # Preview")
        print("  ./scripts/batch-translate.sh --popular    # Translate to popular languages")
        print("  ./scripts/batch-translate.sh              # Translate to all")
    else:
        print("❌ SETUP TEST FAILED")
        print()
        print("Please fix the issues above before running translation.")
        sys.exit(1)
    
    print("="*70)


if __name__ == '__main__':
    try:
        test_setup()
    except Exception as e:
        print(f"❌ Error during setup test: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
