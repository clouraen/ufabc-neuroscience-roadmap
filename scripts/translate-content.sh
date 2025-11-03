#!/bin/bash
# Convenience wrapper for translate-content.py

# Set default values if not already set
export OPENAI_BASE_URL="${OPENAI_BASE_URL:-https://api.openai.com/v1}"
export OPENAI_API_MODEL="${OPENAI_API_MODEL:-gpt-4o-mini}"

# Check if API key is set
if [ -z "$OPENAI_API_KEY" ]; then
    echo "❌ Error: OPENAI_API_KEY environment variable is not set"
    echo ""
    echo "Please set it with:"
    echo "  export OPENAI_API_KEY='your-api-key'"
    echo ""
    echo "Optional:"
    echo "  export OPENAI_BASE_URL='https://api.openai.com/v1'"
    echo "  export OPENAI_API_MODEL='gpt-4o-mini'"
    exit 1
fi

# Run the translation script
python3 "$(dirname "$0")/translate-content.py" "$@"

