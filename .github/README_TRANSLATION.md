# 🌍 Multilingual Translation System

Complete system for translating Portuguese content to 158+ languages.

## 📚 Documentation Quick Links

| Document | Description |
|----------|-------------|
| [**QUICK_START.md**](../QUICK_START.md) | ⚡ Fast start guide - Get translating in 2 minutes |
| [**TRANSLATION_GUIDE.md**](../TRANSLATION_GUIDE.md) | 📖 Complete documentation - Everything you need to know |
| [**TRANSLATION_COMMANDS.md**](./TRANSLATION_COMMANDS.md) | 🎯 Cheat sheet - Quick command reference |
| [**IMPLEMENTATION_SUMMARY.md**](../IMPLEMENTATION_SUMMARY.md) | 🔧 Technical details - How it works |

## 🚀 Quick Start (2 Steps)

### Step 1: Set API Key
```bash
export OPENAI_API_KEY='sk-your-api-key-here'
```

### Step 2: Translate
```bash
# Popular languages (recommended)
./scripts/batch-translate.sh --popular

# Or specific languages
./scripts/batch-translate.sh --languages en,es,fr,de,it
```

**Done!** Your content is now multilingual 🎉

## 📊 What Gets Translated

- ✅ 15 Portuguese markdown files
- ✅ Homepage, blog posts, study logs
- ✅ Neuroscience notes, templates
- ✅ All frontmatter and metadata
- ✅ Preserves markdown formatting

## 🌍 Supported Languages

**158+ languages** including:
- 🇺🇸 English, 🇪🇸 Spanish, 🇫🇷 French, 🇩🇪 German, 🇮🇹 Italian
- 🇯🇵 Japanese, 🇨🇳 Chinese, 🇰🇷 Korean, 🇷🇺 Russian
- 🇸🇦 Arabic, 🇮🇳 Hindi, 🇵🇹 Portuguese, 🇹🇷 Turkish
- And 145+ more!

## 💰 Cost Estimate

| Strategy | Languages | Cost |
|----------|-----------|------|
| 5 languages | en,es,fr,de,it | $0.25-$0.50 |
| 10 languages (popular) | Common languages | $0.50-$1.00 |
| All 158+ languages | Everything | $5.00-$10.00 |

## 🛠️ Key Features

- ✅ **Batch Translation** - Translate all files at once
- ✅ **Progress Tracking** - Resume interrupted translations
- ✅ **Smart Skipping** - Don't retranslate existing content
- ✅ **Error Handling** - Detailed failure logging
- ✅ **Cost Control** - Multiple strategies to manage costs
- ✅ **Dry Run** - Preview before spending credits

## 🎯 Common Commands

```bash
# Preview (no API calls)
./scripts/batch-translate.sh --dry-run

# Translate to English only
./scripts/batch-translate.sh --languages en

# Translate to popular languages
./scripts/batch-translate.sh --popular

# Resume interrupted translation
./scripts/batch-translate.sh --resume

# Check progress
cat progress.json
```

## 📖 Need Help?

1. **Getting Started**: Read [QUICK_START.md](../QUICK_START.md)
2. **Complete Guide**: See [TRANSLATION_GUIDE.md](../TRANSLATION_GUIDE.md)
3. **Commands**: Check [TRANSLATION_COMMANDS.md](./TRANSLATION_COMMANDS.md)
4. **Technical Details**: View [IMPLEMENTATION_SUMMARY.md](../IMPLEMENTATION_SUMMARY.md)

## 🎓 Recommended Workflow

1. **Set API key**: `export OPENAI_API_KEY='...'`
2. **Test**: `./scripts/batch-translate.sh --dry-run`
3. **Start small**: `./scripts/batch-translate.sh --languages en`
4. **Scale up**: `./scripts/batch-translate.sh --popular`
5. **Deploy**: Commit and push translated files

---

**Ready to make your site multilingual?** Start with the [Quick Start Guide](../QUICK_START.md)! 🚀
