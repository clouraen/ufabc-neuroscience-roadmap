#!/usr/bin/env python3
"""
Translate content to all enabled languages using codex CLI.

This script reads English content and translates it to all other enabled languages
using the codex command-line tool.

Prerequisites:
    pip install codex-cli

Environment Variables:
    OPENAI_API_KEY: API key for authentication (required)
    OPENAI_API_MODEL: Model to use (default: gpt-4o-mini)

Setup:
    export OPENAI_API_KEY='your-api-key'
    export OPENAI_API_MODEL='gpt-4o-mini'  # Optional

Usage:
    # Translate all content
    python scripts/translate-content.py

    # Translate specific file
    python scripts/translate-content.py docs/en/blog/pibic-dream.md

    # Translate to specific language
    python scripts/translate-content.py --lang es

Codex CLI will handle the API communication automatically.
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
    """Get API configuration from environment variables for codex CLI."""
    api_key = os.getenv('OPENAI_API_KEY')
    
    # Model selection for codex CLI
    model = os.getenv('OPENAI_API_MODEL', 'gpt-4o-mini')
    
    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY environment variable is required.\n"
            "Set your API key:\n"
            "  export OPENAI_API_KEY='your-api-key'\n"
            "\n"
            "Codex CLI will use OpenAI's API or compatible endpoints.\n"
            "Install codex CLI: pip install codex-cli"
        )
    
    return {
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
    """Translate text using codex CLI tool."""
    import subprocess
    
    # Create prompt
    lang_name = target_lang_info.get('native', target_lang_info.get('name', target_lang))
    prompt = f"""Translate the following text to {lang_name} ({target_lang_info.get('name', '')}). 
Maintain the same Markdown formatting, structure, and style. 
Preserve all links, code blocks, and special formatting exactly as they are.
Only translate the natural language text, not technical terms, URLs, or code.

Text to translate:
{text}
"""
    
    try:
        # Build codex command
        cmd = ['codex']
        
        # Add model if specified
        if config.get('model'):
            cmd.extend(['--model', config['model']])
        
        # Add the prompt as the last positional argument
        cmd.append(prompt)
        
        # Execute codex CLI with OPENAI_API_KEY in environment
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=120,
            env={**os.environ, 'OPENAI_API_KEY': config['api_key']}
        )
        
        if result.returncode != 0:
            error_msg = f"Codex CLI error (exit code {result.returncode})"
            if result.stderr:
                error_msg += f": {result.stderr[:200]}"
            raise Exception(error_msg)
        
        translated_text = result.stdout.strip()
        
        # Clean up any extra markdown formatting that might have been added
        if translated_text.startswith('```'):
            # Remove code block markers if added
            translated_text = re.sub(r'^```(?:markdown)?\n', '', translated_text)
            translated_text = re.sub(r'\n```$', '', translated_text)
        
        return translated_text
    
    except subprocess.TimeoutExpired:
        raise Exception("Translation timeout: codex CLI took too long to respond")
    except FileNotFoundError:
        raise Exception(
            "codex CLI not found. Please install it with:\n"
            "  pip install codex-cli\n"
            "Or ensure it's in your PATH"
        )
    except Exception as e:
        raise Exception(f"Error using codex CLI: {e}")


def translate_file(en_file: Path, target_lang: str, target_lang_info: Dict, config: Dict, docs_dir: Path):
    """Translate a single file to target language."""
    # Read English content
    with open(en_file, 'r', encoding='utf-8') as f:
        en_content = f.read()
    
    # Parse frontmatter and body
    frontmatter, body = parse_frontmatter(en_content)
    
    # Calculate target file path
    rel_path = en_file.relative_to(docs_dir / 'en')
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
    """Translate all English content to target languages."""
    config = get_api_config()
    lang_config = load_languages()
    all_languages = lang_config['languages']
    
    if target_langs is None:
        enabled = lang_config.get('enabled', ['pt', 'en'])
        target_langs = [lang for lang in enabled if lang != 'en']
    
    en_dir = docs_dir / 'en'
    
    # Get files to translate
    if specific_file:
        if specific_file.exists() and str(specific_file).startswith(str(en_dir)):
            files_to_translate = [specific_file]
        else:
            print(f"Error: File {specific_file} not found in English directory")
            return
    else:
        # Find all markdown files in English directory
        files_to_translate = list(en_dir.rglob('*.md'))
    
    print(f"\n🌍 Starting translation...")
    print(f"📁 Files to translate: {len(files_to_translate)}")
    print(f"🌐 Target languages: {len(target_langs)}")
    print(f"🤖 Model: {config['model']}")
    print(f"🛠️  Tool: codex CLI\n")
    
    total_translations = 0
    total_files = len(files_to_translate)
    
    for file_idx, en_file in enumerate(files_to_translate, 1):
        rel_path = en_file.relative_to(en_dir)
        print(f"\n[{file_idx}/{total_files}] Processing: {rel_path}")
        
        for lang_code in target_langs:
            if lang_code not in all_languages:
                print(f"  ⚠️  Language '{lang_code}' not found in languages.json, skipping")
                continue
            
            lang_info = all_languages[lang_code]
            
            if translate_file(en_file, lang_code, lang_info, config, docs_dir):
                total_translations += 1
            
            # Rate limiting - small delay between requests
            time.sleep(0.5)
    
    print(f"\n✅ Translation complete!")
    print(f"   Total translations created: {total_translations}")
    print(f"   Files processed: {total_files}")
    print(f"   Languages: {len(target_langs)}")


def main():
    parser = argparse.ArgumentParser(description='Translate content using codex CLI')
    parser.add_argument('file', nargs='?', help='Specific file to translate (optional)')
    parser.add_argument('--lang', help='Translate to specific language only (e.g., es, fr)')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be translated without doing it')
    
    args = parser.parse_args()
    
    docs_dir = Path(__file__).parent.parent / "docs"
    
    try:
        config = get_api_config()
    except ValueError as e:
        print(f"❌ Error: {e}")
        print("\nSetup for codex CLI:")
        print("  1. Install: pip install codex-cli")
        print("  2. Set API key: export OPENAI_API_KEY='your-api-key'")
        print("  3. Optional model: export OPENAI_API_MODEL='gpt-4o-mini'")
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
        target_langs = [lang for lang in enabled if lang != 'en']
        if args.lang:
            target_langs = [args.lang]
        print(f"   Languages: {target_langs}")
        en_dir = docs_dir / 'en'
        files = list(en_dir.rglob('*.md'))
        print(f"   Files: {len(files)}")
        for f in files[:5]:  # Show first 5
            print(f"     - {f.relative_to(en_dir)}")
        if len(files) > 5:
            print(f"     ... and {len(files) - 5} more")
        return
    
    translate_all_content(docs_dir, target_langs, specific_file)


if __name__ == "__main__":
    main()

