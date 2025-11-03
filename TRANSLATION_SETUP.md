# Translation Setup Quick Guide

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- `requests` - For API calls
- `notion-client` - For Notion integration (optional)

### 2. Set Environment Variables

```bash
# Required
export OPENAI_API_KEY='your-api-key-here'

# Optional (with defaults)
export OPENAI_BASE_URL='https://api.openai.com/v1'
export OPENAI_API_MODEL='gpt-4o-mini'
```

**For OpenAI:**
```bash
export OPENAI_API_KEY='sk-...'
export OPENAI_BASE_URL='https://api.openai.com/v1'
export OPENAI_API_MODEL='gpt-4o-mini'
```

**For Local LLM (e.g., Ollama):**
```bash
export OPENAI_API_KEY='ollama'  # Not needed for local
export OPENAI_BASE_URL='http://localhost:11434/v1'
export OPENAI_API_MODEL='llama3.2'
```

### 3. Test Translation

```bash
# Translate one file to one language (test)
python scripts/translate-content.py docs/pt/index.md --lang es

# Check the result
cat docs/es/index.md
```

### 4. Translate All Content

```bash
# Translate to all enabled languages
python scripts/translate-content.py
```

## 📝 Example Workflow

```bash
# 1. Install dependencies
pip install requests

# 2. Set API key
export OPENAI_API_KEY='sk-your-key-here'

# 3. Test with one file
python scripts/translate-content.py docs/pt/index.md --lang es

# 4. If successful, translate everything
python scripts/translate-content.py
```

## 🔧 Troubleshooting

### "ModuleNotFoundError: No module named 'requests'"
```bash
pip install requests
```

### "OPENAI_API_KEY environment variable is required"
```bash
export OPENAI_API_KEY='your-key'
```

### API Errors
- Check your API key is valid
- Verify `OPENAI_BASE_URL` is correct
- For local LLMs, ensure the server is running

## 📚 Full Documentation

See `docs/TRANSLATION_API.md` for complete documentation.

