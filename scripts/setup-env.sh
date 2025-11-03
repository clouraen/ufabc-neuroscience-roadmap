#!/bin/bash
# Helper script to set up environment variables for translation

echo "🔧 Setting up translation environment variables..."
echo ""

# Check if .env file exists
if [ -f .env ]; then
    echo "✅ Found .env file, loading it..."
    set -a
    source .env
    set +a
    echo "✅ Environment variables loaded from .env"
else
    echo "⚠️  No .env file found. Creating from .env.example..."
    if [ -f .env.example ]; then
        cp .env.example .env
        echo "📝 Created .env file. Please edit it and add your API key!"
        echo "   Then run: source .env"
    else
        echo "❌ .env.example not found. Please create .env manually."
    fi
fi

echo ""
echo "Current environment:"
echo "  OPENAI_API_KEY: ${OPENAI_API_KEY:+✅ Set (${#OPENAI_API_KEY} chars)}${OPENAI_API_KEY:-❌ Not set}"
echo "  OPENAI_BASE_URL: ${OPENAI_BASE_URL:-https://api.openai.com/v1 (default)}"
echo "  OPENAI_API_MODEL: ${OPENAI_API_MODEL:-gpt-4o-mini (default)}"
echo ""
echo "To set variables manually:"
echo "  export OPENAI_API_KEY='your-key'"
echo "  export OPENAI_BASE_URL='https://api.openai.com/v1'"
echo "  export OPENAI_API_MODEL='gpt-4o-mini'"

