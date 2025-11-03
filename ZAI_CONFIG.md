# Z.ai API Configuration

This repository is configured to use **Z.ai** API for automatic translations.

## 🔧 Configuration

Set these environment variables:

```bash
export OPENAI_API_KEY='b743822ac39c45ffa5d5ab0973c72635.0pUk5DtRi7hAHDbH'
export OPENAI_BASE_URL='https://api.z.ai/v1'
export OPENAI_API_MODEL='glm-4.6'  # Z.ai GLM-4.6 model
```

## 📝 Setup

### Quick Setup
```bash
# Set environment variables
export OPENAI_API_KEY='b743822ac39c45ffa5d5ab0973c72635.0pUk5DtRi7hAHDbH'
export OPENAI_BASE_URL='https://api.z.ai/v1'
export OPENAI_API_MODEL='glm-4.6'

# Test translation
python scripts/translate-content.py docs/pt/index.md --lang es
```

### Persistent Setup (Recommended)

Create a `.env` file in the repository root:

```bash
cat > .env << 'EOF'
OPENAI_API_KEY=b743822ac39c45ffa5d5ab0973c72635.0pUk5DtRi7hAHDbH
OPENAI_BASE_URL=https://api.z.ai/v1
OPENAI_API_MODEL=glm-4.6
EOF

# Load the environment
source .env
```

## 🚀 Usage

```bash
# Translate all content to all languages
python scripts/translate-content.py

# Translate to specific language
python scripts/translate-content.py --lang es

# Translate specific file
python scripts/translate-content.py docs/pt/blog/pibic-dream.md
```

## 🔗 Z.ai Resources

- API Documentation: [https://api.z.ai/](https://api.z.ai/)
- API Keys Management: Manage your keys at Z.ai dashboard
- Model Information: Check Z.ai docs for available models

## ⚠️ Notes

- The script automatically appends `/v1` to `https://api.z.ai` if needed
- Make sure your Z.ai API key has sufficient credits/quota
- The API endpoint format should be: `https://api.z.ai/v1/chat/completions`

