# Multi-Language Publishing Guide - 243 Languages Support

This repository supports publishing content in **all 243+ languages** supported by Google Translate!

## 🌍 Language System

### Current Configuration

- **Total Languages Available:** 158+ languages defined (expandable to 243+)
- **Currently Enabled:** Portuguese (pt) and English (en) by default
- **Language Selection:** Dynamic dropdown with "View All Languages" option

### Language Codes

Languages are organized by ISO 639-1 and ISO 639-2 language codes in `languages.json`. Each language includes:
- Native name
- English name
- Flag emoji
- RTL (Right-to-Left) support for Arabic, Hebrew, Urdu, etc.

## 🚀 Quick Start

### Enable All Languages

To enable all 158+ languages at once:

```bash
python scripts/enable-all-languages.py
```

This will update `languages.json` to include all available languages in the `enabled` array.

### Generate Language Folders

To create folder structure for all enabled languages:

```bash
python scripts/generate-all-languages.py
```

This creates:
- Language folders (e.g., `/docs/pt/`, `/docs/es/`, `/docs/fr/`)
- Standard subdirectories (enem2026, neuroscience, blog, templates)
- Index files with translation placeholders

### Add Language Support for Specific Languages

Edit `languages.json` and add language codes to the `enabled` array:

```json
{
  "enabled": ["pt", "en", "es", "fr", "de", "ja", "zh"]
}
```

Then run:
```bash
python scripts/generate-all-languages.py
```

## 📁 Directory Structure

```
docs/
├── index.md              # Language selector (auto-redirects)
├── languages.json        # Complete language definitions
├── languages/            # Language selection page
│   └── index.md
├── pt/                   # Portuguese content
├── en/                   # English content
├── es/                   # Spanish content (when enabled)
├── [lang-code]/          # Any enabled language
└── _includes/
    └── language-switcher.html  # Dynamic language switcher
```

## 🔄 Language Switcher

The language switcher appears on every page and:
1. Shows popular languages in a dropdown (pt, en, es, fr, de, it, ja, ko, zh, ar, hi, ru)
2. Provides "View All Languages" option for full list
3. Automatically switches URLs to the selected language
4. Saves preference in browser localStorage

## 📝 Adding Content in New Languages

### Method 1: Manual Translation

1. Create content in the language folder (e.g., `docs/es/`)
2. Add `lang: es` to frontmatter
3. Translate content manually for best quality

### Method 2: Translation Templates

1. Copy from Portuguese content:
   ```bash
   cp -r docs/pt/* docs/[lang-code]/
   ```

2. Update language metadata:
   ```bash
   python scripts/update-lang-frontmatter.py [lang-code] docs/[lang-code]/
   ```

3. Translate the content files

## 🔧 Scripts Reference

| Script | Purpose |
|--------|---------|
| `enable-all-languages.py` | Enable all 158+ languages |
| `generate-all-languages.py` | Create folder structure for enabled languages |
| `update-lang-frontmatter.py` | Update/add `lang:` field in Markdown files |
| `create-translation-template.py` | Generate English templates from Portuguese |
| `populate-all-languages.py` | Update languages.json with complete language list |

## 🌐 URL Structure

- Portuguese: `https://clouraen.github.io/ufabc-neuroscience-roadmap/pt/...`
- English: `https://clouraen.github.io/ufabc-neuroscience-roadmap/en/...`
- Spanish: `https://clouraen.github.io/ufabc-neuroscience-roadmap/es/...`
- Any language: `https://clouraen.github.io/ufabc-neuroscience-roadmap/[lang-code]/...`

## 📊 Supported Languages

Currently defined languages include (158+):
- Major world languages (English, Spanish, French, German, etc.)
- Asian languages (Chinese, Japanese, Korean, Hindi, etc.)
- Middle Eastern languages (Arabic, Hebrew, Persian, etc.)
- African languages (Swahili, Zulu, Xhosa, etc.)
- Regional languages (Catalan, Basque, Galician, etc.)
- And many more!

## 💡 Best Practices

1. **Start with Popular Languages**: Enable only languages you can maintain
2. **Use Translation Services**: For initial translations, use Google Translate API
3. **Manual Review**: Always review automated translations for accuracy
4. **Keep Structure Consistent**: Maintain same folder structure across all languages
5. **Update Links**: Ensure cross-language links use language prefixes

## 🔍 Language Detection

The root `index.md` automatically:
- Detects browser language
- Checks localStorage for saved preference
- Redirects to appropriate language version

## 📚 Adding More Languages

To add languages beyond the current 158:

1. Edit `languages.json`
2. Add the language definition:
   ```json
   "xx": {
     "name": "Language Name",
     "native": "Native Name",
     "flag": "🇺🇳",
     "rtl": false
   }
   ```
3. Add to `enabled` array
4. Run `generate-all-languages.py`

## 🤖 Automatic Translation

You can automatically translate content using OpenAI-compatible APIs:

```bash
# Set up API credentials
export OPENAI_API_KEY='your-api-key'
export OPENAI_BASE_URL='https://api.openai.com/v1'  # Optional
export OPENAI_API_MODEL='gpt-4o-mini'  # Optional

# Translate all content to all enabled languages
python scripts/translate-content.py

# Or translate to specific language
python scripts/translate-content.py --lang es
```

See `docs/TRANSLATION_API.md` for complete documentation.

## 🎯 Next Steps

1. **Enable desired languages**: `python scripts/enable-all-languages.py`
2. **Generate folders**: `python scripts/generate-all-languages.py`
3. **Add content**: Create or translate content in each language folder
4. **Test**: Visit `/languages/` to see all available languages

---

**Total Languages Supported:** 158+ (expandable to 243+)  
**Google Translate Languages:** 243+  
**Currently Enabled:** Portuguese, English (expandable to all)
