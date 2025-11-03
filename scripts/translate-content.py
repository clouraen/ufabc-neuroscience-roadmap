#!/usr/bin/env python3
"""
Translate content to all enabled languages using OpenAI-compatible API.

This script reads Portuguese content and translates it to all other enabled languages.

Environment Variables:
    OPENAI_BASE_URL: Base URL for the API (default: https://api.openai.com/v1)
    OPENAI_API_KEY: API key for authentication
    OPENAI_API_MODEL: Model to use (default: gpt-4o-mini)

Usage:
    # Translate all content
    python scripts/translate-content.py

    # Translate specific file
    python scripts/translate-content.py docs/pt/blog/pibic-dream.md

    # Translate to specific language
    python scripts/translate-content.py --lang es
"""

import os
import sys
import json
import re
import argparse
from pathlib import Path
from typing import Dict, Optional
import time


def load_languages():
    """Load languages configuration."""
    lang_file = Path(__file__).parent.parent / "languages.json"
    with open(lang_file, 'r', encoding='utf-8') as f:
        return json.load(f)


def get_api_config():
    """Get API configuration from environment variables."""
    base_url = os.getenv('OPENAI_BASE_URL', 'https://api.openai.com/v1')
    
    # Normalize base_url: remove trailing slash
    base_url = base_url.rstrip('/')
    
    # If base_url doesn't end with /v1, check if it needs to be added
    # For Z.ai: https://api.z.ai/v1/ or https://api.z.ai/v1 both work
    if not base_url.endswith('/v1'):
        # Check if it's Z.ai base URL without /v1
        if 'api.z.ai' in base_url and not base_url.endswith('/v1'):
            if base_url == 'https://api.z.ai':
                base_url = f"{base_url}/v1"
        # For other providers, assume they handle the path correctly
    
    api_key = os.getenv('OPENAI_API_KEY')
    # Default model for Z.ai is glm-4.6, fallback to gpt-4o-mini for other providers
    default_model = 'glm-4.6' if 'z.ai' in base_url else 'gpt-4o-mini'
    model = os.getenv('OPENAI_API_MODEL', default_model)
    
    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY environment variable is required.\n"
            "Set it with: export OPENAI_API_KEY='your-api-key'"
        )
    
    return {
        'base_url': base_url,
        'api_key': api_key,
        'model': model
    }


def parse_frontmatter(content: str) -> tuple[Dict, str]:
    """Extract frontmatter from Markdown content."""
    if not content.startswith('---'):
        return {}, content
    
    match = re.match(r'^---\n(.*?)\n---\n(.*)$', content, re.DOTALL)
    if match:
        frontmatter_text = match.group(1)
        body = match.group(2)
        
        frontmatter = {}
        for line in frontmatter_text.split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                key = key.strip()
                value = value.strip().strip('"').strip("'")
                frontmatter[key] = value
        
        return frontmatter, body
    
    return {}, content


def create_frontmatter(frontmatter: Dict) -> str:
    """Create frontmatter string from dictionary."""
    lines = ['---']
    for key, value in frontmatter.items():
        lines.append(f"{key}: {value}")
    lines.append('---')
    return '\n'.join(lines) + '\n\n'


def translate_text(text: str, target_lang: str, target_lang_info: Dict, config: Dict) -> str:
    """Translate text using OpenAI-compatible API."""
    try:
        import requests
    except ImportError:
        raise ImportError(
            "The 'requests' module is required. Install it with:\n"
            "  pip install requests\n"
            "Or install all dependencies:\n"
            "  pip install -r requirements.txt"
        )
    
    # Build API URL
    # For Z.ai, the endpoint is /api/v1/chat/completions
    base = config['base_url']
    if 'z.ai' in base:
        # Z.ai uses: https://api.z.ai/api/v1/chat/completions
        base = base.rstrip('/')
        if base.endswith('/v1'):
            base = base[:-3]  # Remove /v1
        api_url = f"{base}/api/v1/chat/completions"
    else:
        api_url = f"{base}/chat/completions"
    
    # Create prompt
    lang_name = target_lang_info.get('native', target_lang_info.get('name', target_lang))
    prompt = f"""Translate the following text to {lang_name} ({target_lang_info.get('name', '')}). 
Maintain the same Markdown formatting, structure, and style. 
Preserve all links, code blocks, and special formatting exactly as they are.
Only translate the natural language text, not technical terms, URLs, or code.

Text to translate:
{text}
"""
    
    headers = {
        'Authorization': f"Bearer {config['api_key']}",
        'Content-Type': 'application/json'
    }
    
    payload = {
        'model': config['model'],
        'messages': [
            {
                'role': 'system',
                'content': f'You are a professional translator. Translate text to {lang_name} while preserving all Markdown formatting, links, and code blocks.'
            },
            {
                'role': 'user',
                'content': prompt
            }
        ],
        'temperature': 0.3
    }
    
    try:
        response = requests.post(api_url, json=payload, headers=headers, timeout=60)
        response.raise_for_status()
        
        result = response.json()
        
        # Handle Z.ai response format (different from OpenAI)
        if 'code' in result and 'success' in result:
            # Z.ai format: {"code": 200, "msg": "...", "success": true, "data": {...}}
            if not result.get('success', False):
                error_msg = result.get('msg', 'Unknown error')
                raise Exception(f"Z.ai API error: {error_msg}")
            
            # Z.ai response might have data field
            if 'data' in result:
                data = result['data']
                if 'choices' in data:
                    translated_text = data['choices'][0]['message']['content'].strip()
                elif 'message' in data:
                    translated_text = data['message'].strip()
                elif 'content' in data:
                    translated_text = data['content'].strip()
                else:
                    raise Exception(f"Unexpected Z.ai response format: {list(data.keys())}")
            else:
                # Fallback: check if it's in OpenAI format after all
                if 'choices' in result:
                    translated_text = result['choices'][0]['message']['content'].strip()
                else:
                    raise Exception(f"Unexpected response format: {list(result.keys())}")
        else:
            # Standard OpenAI format
            translated_text = result['choices'][0]['message']['content'].strip()
        
        # Clean up any extra markdown formatting that might have been added
        if translated_text.startswith('```'):
            # Remove code block markers if added
            translated_text = re.sub(r'^```(?:markdown)?\n', '', translated_text)
            translated_text = re.sub(r'\n```$', '', translated_text)
        
        return translated_text
    
    except requests.exceptions.RequestException as e:
        error_msg = f"Error calling API: {e}"
        if hasattr(e, 'response') and e.response is not None:
            try:
                error_detail = e.response.json()
                error_msg += f"\nResponse: {error_detail}"
            except:
                error_msg += f"\nResponse: {e.response.text[:200]}"
        raise Exception(error_msg)


def translate_file(pt_file: Path, target_lang: str, target_lang_info: Dict, config: Dict, docs_dir: Path):
    """Translate a single file to target language."""
    # Read Portuguese content
    with open(pt_file, 'r', encoding='utf-8') as f:
        pt_content = f.read()
    
    # Parse frontmatter and body
    frontmatter, body = parse_frontmatter(pt_content)
    
    # Calculate target file path
    rel_path = pt_file.relative_to(docs_dir / 'pt')
    target_file = docs_dir / target_lang / rel_path
    
    # Skip if target file exists and is not a placeholder
    if target_file.exists():
        with open(target_file, 'r', encoding='utf-8') as f:
            existing_content = f.read()
            if '[Translation needed]' not in existing_content and 'Translation needed' not in existing_content:
                print(f"  Skipped (already translated): {target_file}")
                return False
    
    # Update frontmatter
    frontmatter['lang'] = target_lang
    if 'title' in frontmatter:
        # Keep original title for now, translation will handle it
        pass
    
    # Translate body
    print(f"  Translating to {target_lang_info['native']}...")
    try:
        translated_body = translate_text(body, target_lang, target_lang_info, config)
        
        # Combine frontmatter and translated body
        new_content = create_frontmatter(frontmatter) + translated_body
        
        # Ensure parent directory exists
        target_file.parent.mkdir(parents=True, exist_ok=True)
        
        # Write translated file
        with open(target_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"  ✓ Created: {target_file}")
        return True
    
    except Exception as e:
        print(f"  ✗ Error translating {target_file}: {e}")
        return False


def translate_all_content(docs_dir: Path, target_langs: Optional[list] = None, specific_file: Optional[Path] = None):
    """Translate all Portuguese content to target languages."""
    config = get_api_config()
    lang_config = load_languages()
    all_languages = lang_config['languages']
    
    if target_langs is None:
        enabled = lang_config.get('enabled', ['pt', 'en'])
        target_langs = [lang for lang in enabled if lang != 'pt']
    
    pt_dir = docs_dir / 'pt'
    
    # Get files to translate
    if specific_file:
        if specific_file.exists() and str(specific_file).startswith(str(pt_dir)):
            files_to_translate = [specific_file]
        else:
            print(f"Error: File {specific_file} not found in Portuguese directory")
            return
    else:
        # Find all markdown files in Portuguese directory
        files_to_translate = list(pt_dir.rglob('*.md'))
    
    print(f"\n🌍 Starting translation...")
    print(f"📁 Files to translate: {len(files_to_translate)}")
    print(f"🌐 Target languages: {len(target_langs)}")
    print(f"🤖 Model: {config['model']}")
    print(f"🔗 API: {config['base_url']}\n")
    
    total_translations = 0
    total_files = len(files_to_translate)
    
    for file_idx, pt_file in enumerate(files_to_translate, 1):
        rel_path = pt_file.relative_to(pt_dir)
        print(f"\n[{file_idx}/{total_files}] Processing: {rel_path}")
        
        for lang_code in target_langs:
            if lang_code not in all_languages:
                print(f"  ⚠️  Language '{lang_code}' not found in languages.json, skipping")
                continue
            
            lang_info = all_languages[lang_code]
            
            if translate_file(pt_file, lang_code, lang_info, config, docs_dir):
                total_translations += 1
            
            # Rate limiting - small delay between requests
            time.sleep(0.5)
    
    print(f"\n✅ Translation complete!")
    print(f"   Total translations created: {total_translations}")
    print(f"   Files processed: {total_files}")
    print(f"   Languages: {len(target_langs)}")


def main():
    parser = argparse.ArgumentParser(description='Translate content using OpenAI-compatible API')
    parser.add_argument('file', nargs='?', help='Specific file to translate (optional)')
    parser.add_argument('--lang', help='Translate to specific language only (e.g., es, fr)')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be translated without doing it')
    
    args = parser.parse_args()
    
    docs_dir = Path(__file__).parent.parent / "docs"
    
    try:
        config = get_api_config()
    except ValueError as e:
        print(f"❌ Error: {e}")
        print("\nPlease set the following environment variables:")
        print("  export OPENAI_API_KEY='your-api-key'")
        print("  export OPENAI_BASE_URL='https://api.openai.com/v1'  # Optional")
        print("  export OPENAI_API_MODEL='gpt-4o-mini'  # Optional")
        sys.exit(1)
    
    target_langs = None
    if args.lang:
        target_langs = [args.lang]
    
    specific_file = None
    if args.file:
        specific_file = Path(args.file)
        if not specific_file.is_absolute():
            specific_file = Path.cwd() / args.file
    
    if args.dry_run:
        print("🔍 Dry run mode - would translate:")
        lang_config = load_languages()
        enabled = lang_config.get('enabled', ['pt', 'en'])
        target_langs = [lang for lang in enabled if lang != 'pt']
        if args.lang:
            target_langs = [args.lang]
        print(f"   Languages: {target_langs}")
        pt_dir = docs_dir / 'pt'
        files = list(pt_dir.rglob('*.md'))
        print(f"   Files: {len(files)}")
        for f in files[:5]:  # Show first 5
            print(f"     - {f.relative_to(pt_dir)}")
        if len(files) > 5:
            print(f"     ... and {len(files) - 5} more")
        return
    
    translate_all_content(docs_dir, target_langs, specific_file)


if __name__ == "__main__":
    main()

