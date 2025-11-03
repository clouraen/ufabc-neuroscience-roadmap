# Automatic Translation with OpenAI-Compatible API

This repository includes an automated translation system that uses OpenAI-compatible APIs to translate content to all enabled languages.

## 🔧 Configuration

### Environment Variables

Set these environment variables before running the translation script:

```bash
# Required
export OPENAI_API_KEY='your-api-key-here'

# Optional (defaults shown)
export OPENAI_BASE_URL='https://api.openai.com/v1'
export OPENAI_API_MODEL='gpt-4o-mini'
```

### Supported API Providers

The script works with any OpenAI-compatible API, including:
- **OpenAI**: `https://api.openai.com/v1`
- **Anthropic Claude**: `https://api.anthropic.com/v1` (with adapter)
- **Local LLMs**: `http://localhost:8000/v1` (e.g., using Ollama, vLLM)
- **Other providers**: Any OpenAI-compatible endpoint

### Example Setup

```bash
# For OpenAI
export OPENAI_API_KEY='sk-...'
export OPENAI_BASE_URL='https://api.openai.com/v1'
export OPENAI_API_MODEL='gpt-4o-mini'

# For local LLM (e.g., Ollama)
export OPENAI_API_KEY='ollama'  # Not needed for local
export OPENAI_BASE_URL='http://localhost:11434/v1'
export OPENAI_API_MODEL='llama3.2'
```

## 🚀 Usage

### Translate All Content

Translate all Portuguese content to all enabled languages:

```bash
python scripts/translate-content.py
```

### Translate Specific File

Translate a single file to all enabled languages:

```bash
python scripts/translate-content.py docs/pt/blog/pibic-dream.md
```

### Translate to Specific Language

Translate all content to just one language:

```bash
python scripts/translate-content.py --lang es
```

### Dry Run

See what would be translated without actually doing it:

```bash
python scripts/translate-content.py --dry-run
```

### Using the Shell Wrapper

```bash
./scripts/translate-content.sh
```

## 📋 How It Works

1. **Reads Portuguese Content**: Starts from `/docs/pt/` directory
2. **Finds All Files**: Discovers all Markdown files recursively
3. **For Each Language**: Translates to each enabled language (except Portuguese)
4. **Preserves Structure**: 
   - Keeps frontmatter structure
   - Preserves Markdown formatting
   - Maintains links and code blocks
5. **Creates Files**: Saves translated content in `/docs/[lang-code]/`

## 🎯 Translation Features

- **Smart Formatting**: Preserves all Markdown, links, code blocks
- **Frontmatter Handling**: Updates language metadata automatically
- **Skip Existing**: Won't overwrite already-translated files
- **Error Handling**: Continues on errors, reports issues
- **Rate Limiting**: Includes small delays between requests

## 💡 Best Practices

1. **Start Small**: Test with a single file first
   ```bash
   python scripts/translate-content.py docs/pt/index.md --lang es
   ```

2. **Review Translations**: Always review AI translations for accuracy
   - Technical terms may need manual correction
   - Cultural context might need adjustment
   - Some idioms don't translate well

3. **Cost Management**: 
   - Use `gpt-4o-mini` for cost-effectiveness
   - Translate in batches if needed
   - Monitor API usage

4. **Incremental Translation**:
   - Translate new content as you create it
   - Don't retranslate everything each time
   - Script skips already-translated files

## 🔍 Troubleshooting

### API Key Not Set
```
❌ Error: OPENAI_API_KEY environment variable is required.
```
**Solution**: Set the environment variable:
```bash
export OPENAI_API_KEY='your-key'
```

### API Connection Error
```
Error calling API: Connection refused
```
**Solution**: 
- Check your `OPENAI_BASE_URL`
- Verify network connectivity
- For local LLMs, ensure server is running

### Rate Limiting
If you hit rate limits:
- The script includes delays between requests
- Consider translating in smaller batches
- Use `--lang` to translate one language at a time

### Translation Quality Issues
- Review and manually edit translations
- Consider using a different model (e.g., `gpt-4o` instead of `gpt-4o-mini`)
- Provide more context in the prompt if needed

## 📊 Example Workflow

```bash
# 1. Set up environment
export OPENAI_API_KEY='sk-...'
export OPENAI_API_MODEL='gpt-4o-mini'

# 2. Test with one file
python scripts/translate-content.py docs/pt/index.md --lang es

# 3. Check the result
cat docs/es/index.md

# 4. If good, translate all to Spanish
python scripts/translate-content.py --lang es

# 5. Eventually translate to all languages
python scripts/translate-content.py
```

## 🎨 Customization

### Change Translation Model

```bash
export OPENAI_API_MODEL='gpt-4o'  # Better quality, higher cost
export OPENAI_API_MODEL='gpt-3.5-turbo'  # Faster, lower cost
```

### Custom API Endpoint

```bash
# For Anthropic Claude (with adapter)
export OPENAI_BASE_URL='https://api.anthropic.com/v1'
export OPENAI_API_MODEL='claude-3-sonnet'

# For local Ollama
export OPENAI_BASE_URL='http://localhost:11434/v1'
export OPENAI_API_MODEL='llama3.2'
```

## 📝 Notes

- Translations are stored in language-specific folders
- Original Portuguese content in `/docs/pt/` is never modified
- Script respects existing translations (won't overwrite)
- Frontmatter is automatically updated with correct language code

---

**Ready to translate?** Set your API key and run the script!

```bash
export OPENAI_API_KEY='your-key'
python scripts/translate-content.py
```

