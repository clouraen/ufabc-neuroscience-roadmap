# Quick Start: Multilingual Translation

## 🚀 Translate Portuguese Content to Other Languages

### Step 1: Set API Key

```bash
export OPENAI_API_KEY='sk-your-api-key-here'
```

### Step 2: Choose Your Translation Strategy

#### Option A: Translate to Popular Languages (Recommended)
**~150 API calls, $0.50-$1.00**

```bash
./scripts/batch-translate.sh --popular
```

Translates to: English, Spanish, French, German, Italian, Japanese, Chinese, Russian, Arabic, Hindi

#### Option B: Translate to Specific Languages
**~75 API calls, $0.25-$0.50**

```bash
./scripts/batch-translate.sh --languages en,es,fr,de,it
```

#### Option C: Translate to ALL Languages (158+)
**~2,370 API calls, $5-$10 ⚠️**

```bash
./scripts/batch-translate.sh
```

### Step 3: Preview First (Optional)

```bash
./scripts/batch-translate.sh --dry-run
```

### Step 4: Resume if Interrupted

```bash
./scripts/batch-translate.sh --resume
```

## 📊 What Gets Translated

All Portuguese (`.md`) files in `docs/pt/`:
- ✅ `index.md` - Homepage
- ✅ `blog/*.md` - Blog posts (4 files)
- ✅ `enem2026/*.md` - ENEM study logs (3 files)
- ✅ `neuroscience/*.md` - Neuroscience notes (4 files)
- ✅ `templates/*.md` - Templates (3 files)

**Total: 15 markdown files**

## 🌍 Supported Languages

**Popular (--popular):**
- 🇺🇸 English (en)
- 🇪🇸 Spanish (es)
- 🇫🇷 French (fr)
- 🇩🇪 German (de)
- 🇮🇹 Italian (it)
- 🇯🇵 Japanese (ja)
- 🇨🇳 Chinese (zh)
- 🇷🇺 Russian (ru)
- 🇸🇦 Arabic (ar)
- 🇮🇳 Hindi (hi)

**All Languages:** 158+ languages (see `languages.json`)

## 💡 Tips

1. **Start Small:** Use `--popular` for your first run
2. **Check Progress:** Monitor `progress.json` file
3. **Cost Aware:** Popular languages ≈ $1, All languages ≈ $10
4. **Dry Run:** Test with `--dry-run` before committing

## 📖 Full Documentation

See [`TRANSLATION_GUIDE.md`](./TRANSLATION_GUIDE.md) for complete documentation.

---

**Questions?** Check the [Translation Guide](./TRANSLATION_GUIDE.md) or `progress.json` for errors.
