# 🌍 Translation Commands Cheat Sheet

Quick reference for translating Portuguese content to multiple languages.

## 🚦 Prerequisites

```bash
# Set your OpenAI API key (REQUIRED)
export OPENAI_API_KEY='sk-your-api-key-here'
```

## ⚡ Quick Commands

### Preview (No API Calls)
```bash
./scripts/batch-translate.sh --dry-run
```

### Popular Languages (~$1)
```bash
./scripts/batch-translate.sh --popular
```
**Translates to:** English, Spanish, French, German, Italian, Japanese, Chinese, Russian, Arabic, Hindi

### Specific Languages
```bash
./scripts/batch-translate.sh --languages en,es,fr,de,it
```

### All Languages (~$10)
```bash
./scripts/batch-translate.sh
```

### Resume Interrupted Translation
```bash
./scripts/batch-translate.sh --resume
```

## 📊 Translation Strategies

| Command | Languages | API Calls | Cost | Time |
|---------|-----------|-----------|------|------|
| `--languages en` | 1 | ~15 | $0.05 | 1 min |
| `--languages en,es,fr,de,it` | 5 | ~75 | $0.25 | 3 min |
| `--popular` | 10 | ~150 | $0.50-$1 | 5 min |
| (default - all) | 158+ | ~2,370 | $5-$10 | 30-60 min |

## 🔍 Check Progress

```bash
# View progress statistics
cat progress.json

# Check completed translations
jq '.stats' progress.json

# List failed translations
jq '.failed' progress.json

# Count translated files
find docs/en -name "*.md" | wc -l
```

## 🛠️ Advanced Usage

### Python Script Directly

```bash
# Translate to all enabled languages
python3 scripts/batch-translate.py

# Specific languages
python3 scripts/batch-translate.py --languages en,es,fr

# Dry run
python3 scripts/batch-translate.py --dry-run

# Resume
python3 scripts/batch-translate.py --resume

# Custom progress file
python3 scripts/batch-translate.py --progress-file my-progress.json
```

### Single File Translation

```bash
# Translate specific file to all languages
python3 scripts/translate-content.py docs/pt/blog/pibic-dream.md

# Translate to specific language
python3 scripts/translate-content.py docs/pt/index.md --lang es
```

## 🧪 Testing

```bash
# Test setup
python3 scripts/test-translation-setup.py

# Validate configuration
python3 -c "import json; print(json.load(open('languages.json'))['enabled'][:10])"

# Count Portuguese files
find docs/pt -name "*.md" | wc -l
```

## 🎯 Recommended Workflow

### First Time Setup

```bash
# 1. Set API key
export OPENAI_API_KEY='sk-...'

# 2. Test setup
python3 scripts/test-translation-setup.py

# 3. Preview what will be translated
./scripts/batch-translate.sh --dry-run

# 4. Start with English only
./scripts/batch-translate.sh --languages en

# 5. Check results
ls -la docs/en/
cat docs/en/index.md

# 6. If satisfied, translate more
./scripts/batch-translate.sh --popular
```

### Regular Updates

```bash
# When Portuguese content changes
./scripts/batch-translate.sh --languages en,es,fr,de,it --resume
```

### Full Translation

```bash
# For complete multilingual site
./scripts/batch-translate.sh
```

## 💰 Cost Estimation

Based on OpenAI gpt-4o-mini pricing:

- **Per file**: ~$0.002 - $0.005
- **5 languages**: ~$0.25 - $0.50
- **10 languages**: ~$0.50 - $1.00
- **All 158+ languages**: ~$5.00 - $10.00

## 🐛 Troubleshooting

### API Key Not Set
```bash
export OPENAI_API_KEY='your-key'
```

### Check API Configuration
```bash
echo $OPENAI_API_KEY
echo $OPENAI_BASE_URL
echo $OPENAI_API_MODEL
```

### Clear Progress and Start Over
```bash
mv progress.json progress.json.bak
./scripts/batch-translate.sh --popular
```

### View Failed Translations
```bash
jq '.failed' progress.json
```

## 📖 Full Documentation

- [`QUICK_START.md`](../QUICK_START.md) - Getting started guide
- [`TRANSLATION_GUIDE.md`](../TRANSLATION_GUIDE.md) - Complete documentation
- [`IMPLEMENTATION_SUMMARY.md`](../IMPLEMENTATION_SUMMARY.md) - Technical details

---

**💡 Tip:** Always start with `--dry-run` to preview before spending API credits!
