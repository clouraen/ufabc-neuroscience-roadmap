# Multilingual Translation Guide

This guide explains how to translate Portuguese content to all enabled languages for the multilingual site.

## 📋 Overview

The translation system automatically translates all `.md` files from the Portuguese (`pt`) folder to all other enabled languages using OpenAI-compatible APIs.

**Key Features:**
- ✅ Translates 15+ Portuguese markdown files
- ✅ Supports 158+ languages via Google Translate compatibility
- ✅ Uses OpenAI API (gpt-4o-mini by default)
- ✅ Progress tracking and resume capability
- ✅ Batch processing with error handling
- ✅ Preserves markdown formatting and frontmatter

## 🚀 Quick Start

### 1. Set Up API Key

```bash
# Required: Set your OpenAI API key
export OPENAI_API_KEY='sk-your-api-key-here'

# Optional: Customize API endpoint and model
export OPENAI_BASE_URL='https://api.openai.com/v1'
export OPENAI_API_MODEL='gpt-4o-mini'
```

### 2. Run Translation

#### Option A: Translate to All Languages (158+)

```bash
./scripts/batch-translate.sh
```

This will translate all Portuguese content to **all enabled languages** (~158 languages).

**⚠️ Warning:** This will make approximately **15 files × 158 languages = 2,370 API calls**. 
Estimated cost: ~$5-10 depending on your API provider.

#### Option B: Translate to Popular Languages Only

```bash
./scripts/batch-translate.sh --popular
```

Translates to: English, Spanish, French, German, Italian, Japanese, Chinese, Russian, Arabic, Hindi

**Estimated:** 15 files × 10 languages = 150 API calls (~$0.50-$1.00)

#### Option C: Translate to Specific Languages

```bash
./scripts/batch-translate.sh --languages en,es,fr,de,it
```

**Estimated:** 15 files × 5 languages = 75 API calls (~$0.25-$0.50)

### 3. Preview Before Translating (Dry Run)

```bash
./scripts/batch-translate.sh --dry-run
```

This shows what would be translated without making any API calls.

## 📊 Progress Tracking

The system automatically tracks progress in `progress.json`:

```json
{
  "completed": [
    "index.md:en",
    "index.md:es",
    "blog/pibic-dream.md:en"
  ],
  "failed": [],
  "stats": {
    "total_files": 15,
    "total_languages": 158,
    "translations_completed": 45,
    "translations_failed": 0,
    "translations_skipped": 10
  }
}
```

### Resume from Previous Run

If the translation process is interrupted, you can resume:

```bash
./scripts/batch-translate.sh --resume
```

This will skip already-completed translations and continue from where it left off.

## 🛠️ Advanced Usage

### Using Python Script Directly

```bash
# Translate to all languages
python3 scripts/batch-translate.py

# Translate to specific languages
python3 scripts/batch-translate.py --languages en,es,fr,de

# Dry run
python3 scripts/batch-translate.py --dry-run

# Resume from previous run
python3 scripts/batch-translate.py --resume

# Custom progress file
python3 scripts/batch-translate.py --progress-file my-progress.json
```

### Using Original Translation Script

For single file translation:

```bash
# Translate specific file
python3 scripts/translate-content.py docs/pt/blog/pibic-dream.md

# Translate to specific language only
python3 scripts/translate-content.py --lang es

# Translate all files to one language
python3 scripts/translate-content.py --lang en
```

## 📁 Directory Structure

```
docs/
├── pt/                    # Source Portuguese content
│   ├── index.md
│   ├── blog/
│   ├── enem2026/
│   ├── neuroscience/
│   └── templates/
├── en/                    # English translations
├── es/                    # Spanish translations
├── fr/                    # French translations
└── [158+ other languages]
```

Each language folder mirrors the structure of the `pt` folder.

## 🌍 Supported Languages

The system supports **158+ languages** including:

**Popular Languages:**
- 🇺🇸 English (en)
- 🇪🇸 Spanish (es)
- 🇫🇷 French (fr)
- 🇩🇪 German (de)
- 🇮🇹 Italian (it)
- 🇯🇵 Japanese (ja)
- 🇨🇳 Chinese (zh, zh-CN, zh-TW)
- 🇷🇺 Russian (ru)
- 🇸🇦 Arabic (ar)
- 🇮🇳 Hindi (hi)

**Regional Languages:**
- And 140+ more languages!

See `languages.json` for the complete list.

## 💰 Cost Estimation

Based on OpenAI API pricing (gpt-4o-mini):

| Scenario | Files | Languages | API Calls | Est. Cost |
|----------|-------|-----------|-----------|-----------|
| All languages | 15 | 158 | 2,370 | $5-10 |
| Popular only | 15 | 10 | 150 | $0.50-$1 |
| Top 5 languages | 15 | 5 | 75 | $0.25-$0.50 |
| Single language | 15 | 1 | 15 | $0.05-$0.10 |

**Note:** Costs vary by provider. Some providers offer free tiers.

## 🔧 Configuration

### Language Selection

Edit `languages.json` to enable/disable languages:

```json
{
  "languages": { ... },
  "default": "pt",
  "enabled": ["pt", "en", "es", "fr", "de", "it"]
}
```

### API Configuration

Set environment variables:

```bash
# OpenAI (default)
export OPENAI_API_KEY='sk-...'
export OPENAI_BASE_URL='https://api.openai.com/v1'
export OPENAI_API_MODEL='gpt-4o-mini'

# Alternative providers (Azure, Anthropic, etc.)
export OPENAI_API_KEY='your-key'
export OPENAI_BASE_URL='https://your-provider.com/v1'
export OPENAI_API_MODEL='your-model'
```

## 🐛 Troubleshooting

### API Key Not Set

```
❌ Error: OPENAI_API_KEY environment variable is not set
```

**Solution:** Set the API key:
```bash
export OPENAI_API_KEY='sk-your-key-here'
```

### Translation Failed

Check `progress.json` for failed translations and error details:

```json
{
  "failed": [
    {
      "file": "blog/post.md",
      "lang": "es",
      "error": "API timeout",
      "timestamp": "2024-01-01 12:00:00"
    }
  ]
}
```

**Solution:** Use `--resume` to retry failed translations.

### Rate Limiting

If you encounter rate limits, the script automatically adds delays between requests (0.5s).

For aggressive rate limits, modify the delay in `batch-translate.py`:

```python
# Change from 0.5 to higher value
time.sleep(1.0)  # 1 second delay
```

## 📝 How It Works

1. **Source Detection:** Finds all `.md` files in `docs/pt/`
2. **Target Languages:** Uses enabled languages from `languages.json`
3. **Translation:** For each file and language:
   - Reads Portuguese content
   - Extracts frontmatter (metadata)
   - Sends body to OpenAI API for translation
   - Preserves markdown formatting and links
   - Updates language metadata
   - Saves to `docs/{lang}/...`
4. **Progress Tracking:** Records completed, failed, and skipped translations
5. **Resume Support:** Skips already-translated files on resume

## 🎯 Best Practices

1. **Start Small:** Test with `--popular` or `--languages en,es` first
2. **Use Dry Run:** Always preview with `--dry-run` before large batches
3. **Monitor Progress:** Check `progress.json` during long runs
4. **Resume Support:** Use `--resume` if interrupted
5. **Cost Management:** Be aware of API costs for large batches
6. **Quality Check:** Review a few translations manually before deploying

## 🔄 Updating Translations

When Portuguese content changes, re-run the translation:

```bash
# The script automatically detects changed files
./scripts/batch-translate.sh --languages en,es,fr
```

Or translate specific files:

```bash
python3 scripts/translate-content.py docs/pt/blog/new-post.md
```

## 📚 Related Documentation

- [`TRANSLATION_SETUP.md`](../TRANSLATION_SETUP.md) - Original translation setup
- [`languages.json`](../languages.json) - Language configuration
- [`mkdocs.yml`](../mkdocs.yml) - MkDocs configuration

## 🤝 Contributing

To add support for new languages:

1. Add language to `languages.json`
2. Enable in the `enabled` array
3. Run translation: `./scripts/batch-translate.sh --languages xx`

## 📞 Support

For issues or questions:
- Check `progress.json` for error details
- Review API provider documentation
- Ensure environment variables are set correctly

---

**Happy Translating! 🌍🎉**
