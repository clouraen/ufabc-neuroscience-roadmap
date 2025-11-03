#!/usr/bin/env python3
"""
Batch translate all English content to all enabled languages using codex CLI.

This script translates all .md files from the English (en) folder
to all other enabled languages using the codex command-line tool.

Prerequisites:
    pip install codex-cli

Setup:
    export OPENAI_API_KEY='your-api-key'
    export OPENAI_API_MODEL='gpt-4o-mini'  # Optional

Usage:
    # Translate to all enabled languages
    python scripts/batch-translate.py

    # Translate to specific languages only
    python scripts/batch-translate.py --languages pt,es,fr,de

    # Dry run (show what would be translated)
    python scripts/batch-translate.py --dry-run

    # Resume from progress file
    python scripts/batch-translate.py --resume

Environment Variables:
    OPENAI_API_KEY: Required - API key for authentication
    OPENAI_API_MODEL: Optional - Model to use (default: gpt-4o-mini)
"""

import os
import sys
import json
import argparse
from pathlib import Path
from typing import List, Dict, Set, Optional
import time

# Add parent directory to path to import translate_content
sys.path.insert(0, str(Path(__file__).parent))

try:
    from translate_content import (  # type: ignore
        load_languages,
        get_api_config,
        translate_file,
        parse_frontmatter
    )
except ImportError:
    print("❌ Error: Could not import translate_content module")
    sys.exit(1)


class TranslationProgress:
    """Track translation progress and resume capability."""
    
    def __init__(self, progress_file: Path):
        self.progress_file = progress_file
        self.data = self._load()
    
    def _load(self) -> Dict:
        """Load progress from file."""
        if self.progress_file.exists():
            with open(self.progress_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {
            'completed': [],
            'failed': [],
            'stats': {
                'total_files': 0,
                'total_languages': 0,
                'translations_completed': 0,
                'translations_failed': 0,
                'translations_skipped': 0
            }
        }
    
    def _save(self):
        """Save progress to file."""
        with open(self.progress_file, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, indent=2, ensure_ascii=False)
    
    def is_completed(self, file_path: str, lang_code: str) -> bool:
        """Check if translation is already completed."""
        key = f"{file_path}:{lang_code}"
        return key in self.data['completed']
    
    def mark_completed(self, file_path: str, lang_code: str):
        """Mark translation as completed."""
        key = f"{file_path}:{lang_code}"
        if key not in self.data['completed']:
            self.data['completed'].append(key)
            self.data['stats']['translations_completed'] += 1
            self._save()
    
    def mark_failed(self, file_path: str, lang_code: str, error: str):
        """Mark translation as failed."""
        key = f"{file_path}:{lang_code}"
        self.data['failed'].append({
            'key': key,
            'file': file_path,
            'lang': lang_code,
            'error': error,
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
        })
        self.data['stats']['translations_failed'] += 1
        self._save()
    
    def mark_skipped(self):
        """Mark translation as skipped."""
        self.data['stats']['translations_skipped'] += 1
    
    def set_totals(self, total_files: int, total_languages: int):
        """Set total counts."""
        self.data['stats']['total_files'] = total_files
        self.data['stats']['total_languages'] = total_languages
        self._save()
    
    def get_stats(self) -> Dict:
        """Get current statistics."""
        return self.data['stats']
    
    def get_failed(self) -> List[Dict]:
        """Get list of failed translations."""
        return self.data.get('failed', [])


def get_english_files(docs_dir: Path) -> List[Path]:
    """Get all English markdown files."""
    en_dir = docs_dir / 'en'
    if not en_dir.exists():
        print(f"❌ Error: English directory not found: {en_dir}")
        return []
    
    files = sorted(en_dir.rglob('*.md'))
    return files


def get_target_languages(lang_config: Dict, specified_langs: Optional[List[str]] = None) -> List[str]:
    """Get list of target languages (excluding English)."""
    if specified_langs:
        # Validate specified languages
        all_langs = lang_config['languages']
        valid_langs = []
        for lang in specified_langs:
            if lang == 'en':
                continue  # Skip English
            if lang in all_langs:
                valid_langs.append(lang)
            else:
                print(f"⚠️  Warning: Language '{lang}' not found in languages.json")
        return valid_langs
    
    # Use all enabled languages except English
    enabled = lang_config.get('enabled', ['pt', 'en'])
    return [lang for lang in enabled if lang != 'en']


def batch_translate(
    docs_dir: Path,
    target_langs: List[str],
    progress: TranslationProgress,
    dry_run: bool = False,
    resume: bool = False
):
    """Translate all English content to target languages."""
    
    # Get API config
    try:
        config = get_api_config()
    except ValueError as e:
        print(f"❌ Error: {e}")
        print("\nSetup for codex CLI:")
        print("  1. Install: pip install codex-cli")
        print("  2. Set API key: export OPENAI_API_KEY='your-api-key'")
        sys.exit(1)
    
    # Load language config
    lang_config = load_languages()
    all_languages = lang_config['languages']
    
    # Get English files
    en_files = get_english_files(docs_dir)
    if not en_files:
        print("❌ No English files found to translate")
        return
    
    # Set totals
    progress.set_totals(len(en_files), len(target_langs))
    
    print("\n" + "="*70)
    print("🌍 MULTILINGUAL TRANSLATION BATCH JOB")
    print("="*70)
    print(f"\n📁 Source: docs/en/ ({len(en_files)} files)")
    print(f"🌐 Target languages: {len(target_langs)}")
    print(f"🤖 Model: {config['model']}")
    print(f"🛠️  Tool: codex CLI")
    print(f"📊 Total translations: {len(en_files) * len(target_langs)}")
    
    if dry_run:
        print("\n🔍 DRY RUN MODE - No actual translations will be performed")
    
    if resume:
        stats = progress.get_stats()
        print(f"\n♻️  RESUME MODE")
        print(f"   Already completed: {stats['translations_completed']}")
        print(f"   Already failed: {stats['translations_failed']}")
        print(f"   Already skipped: {stats['translations_skipped']}")
    
    print("\n" + "="*70)
    
    if dry_run:
        print("\n📋 Files to translate:")
        for i, en_file in enumerate(en_files[:10], 1):
            rel_path = en_file.relative_to(docs_dir / 'en')
            print(f"   {i}. {rel_path}")
        if len(en_files) > 10:
            print(f"   ... and {len(en_files) - 10} more files")
        
        print(f"\n🌐 Target languages ({len(target_langs)}):")
        lang_names = [f"{lang} ({all_languages[lang]['native']})" 
                     for lang in target_langs[:10]]
        for name in lang_names:
            print(f"   • {name}")
        if len(target_langs) > 10:
            print(f"   ... and {len(target_langs) - 10} more languages")
        return
    
    # Start translation
    start_time = time.time()
    
    for file_idx, en_file in enumerate(en_files, 1):
        rel_path = en_file.relative_to(docs_dir / 'en')
        print(f"\n{'='*70}")
        print(f"📄 [{file_idx}/{len(en_files)}] Processing: {rel_path}")
        print(f"{'='*70}")
        
        # Translate to each language
        for lang_idx, lang_code in enumerate(target_langs, 1):
            if lang_code not in all_languages:
                print(f"  ⚠️  [{lang_idx}/{len(target_langs)}] Language '{lang_code}' not found, skipping")
                continue
            
            lang_info = all_languages[lang_code]
            lang_display = f"{lang_code} ({lang_info['native']})"
            
            # Check if already completed (resume mode)
            if resume and progress.is_completed(str(rel_path), lang_code):
                print(f"  ⏭️  [{lang_idx}/{len(target_langs)}] {lang_display} - Already completed")
                progress.mark_skipped()
                continue
            
            # Check if target file already exists and is translated
            target_file = docs_dir / lang_code / rel_path
            if target_file.exists():
                with open(target_file, 'r', encoding='utf-8') as f:
                    existing_content = f.read()
                    if '[Translation needed]' not in existing_content:
                        print(f"  ✓ [{lang_idx}/{len(target_langs)}] {lang_display} - Already translated")
                        progress.mark_completed(str(rel_path), lang_code)
                        continue
            
            # Perform translation
            print(f"  🔄 [{lang_idx}/{len(target_langs)}] Translating to {lang_display}...")
            
            try:
                success = translate_file(en_file, lang_code, lang_info, config, docs_dir)
                
                if success:
                    progress.mark_completed(str(rel_path), lang_code)
                    print(f"  ✅ [{lang_idx}/{len(target_langs)}] {lang_display} - Translation complete!")
                else:
                    print(f"  ⏭️  [{lang_idx}/{len(target_langs)}] {lang_display} - Skipped")
                    progress.mark_skipped()
                
                # Rate limiting
                time.sleep(0.5)
                
            except Exception as e:
                error_msg = str(e)[:100]
                print(f"  ❌ [{lang_idx}/{len(target_langs)}] {lang_display} - Error: {error_msg}")
                progress.mark_failed(str(rel_path), lang_code, str(e))
    
    # Final statistics
    elapsed_time = time.time() - start_time
    stats = progress.get_stats()
    
    print("\n" + "="*70)
    print("✅ TRANSLATION BATCH JOB COMPLETE")
    print("="*70)
    print(f"\n📊 Statistics:")
    print(f"   Files processed: {stats['total_files']}")
    print(f"   Target languages: {stats['total_languages']}")
    print(f"   Total possible translations: {stats['total_files'] * stats['total_languages']}")
    print(f"   ✅ Completed: {stats['translations_completed']}")
    print(f"   ⏭️  Skipped: {stats['translations_skipped']}")
    print(f"   ❌ Failed: {stats['translations_failed']}")
    print(f"\n⏱️  Time elapsed: {elapsed_time/60:.2f} minutes")
    
    if stats['translations_failed'] > 0:
        print(f"\n⚠️  {stats['translations_failed']} translations failed. See progress.json for details.")
        print("   You can retry failed translations with: --resume")
    
    print(f"\n💾 Progress saved to: {progress.progress_file}")
    print("="*70 + "\n")


def main():
    parser = argparse.ArgumentParser(
        description='Batch translate English content to all enabled languages',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Translate to all enabled languages
  python scripts/batch-translate.py

  # Translate to specific languages only
  python scripts/batch-translate.py --languages en,es,fr,de,it

  # See what would be translated (dry run)
  python scripts/batch-translate.py --dry-run

  # Resume from previous run
  python scripts/batch-translate.py --resume

Environment Variables:
  OPENAI_API_KEY     Required - Your API key for OpenAI or compatible service
  OPENAI_API_MODEL   Optional - Model to use (default: gpt-4o-mini)

Codex CLI Setup:
  pip install codex-cli
  export OPENAI_API_KEY='your-api-key'
        """
    )
    
    parser.add_argument(
        '--languages',
        help='Comma-separated list of language codes to translate to (e.g., en,es,fr)',
        type=str
    )
    
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be translated without actually translating'
    )
    
    parser.add_argument(
        '--resume',
        action='store_true',
        help='Resume from previous run using progress.json'
    )
    
    parser.add_argument(
        '--progress-file',
        help='Path to progress file (default: progress.json)',
        type=Path,
        default=Path(__file__).parent.parent / 'progress.json'
    )
    
    args = parser.parse_args()
    
    # Parse language list
    target_langs = None
    if args.languages:
        target_langs = [lang.strip() for lang in args.languages.split(',')]
    
    # Setup paths
    docs_dir = Path(__file__).parent.parent / "docs"
    
    # Load language config
    lang_config = load_languages()
    
    # Get target languages
    target_langs = get_target_languages(lang_config, target_langs)
    
    if not target_langs:
        print("❌ No target languages specified")
        sys.exit(1)
    
    # Initialize progress tracker
    progress = TranslationProgress(args.progress_file)
    
    # Run batch translation
    batch_translate(
        docs_dir=docs_dir,
        target_langs=target_langs,
        progress=progress,
        dry_run=args.dry_run,
        resume=args.resume
    )


if __name__ == "__main__":
    main()
