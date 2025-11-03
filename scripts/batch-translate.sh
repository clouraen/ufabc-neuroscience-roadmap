#!/bin/bash

# Batch Translation Wrapper Script
# This script provides a convenient way to run batch translations

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Get script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

echo -e "${BLUE}╔═══════════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║         MULTILINGUAL CONTENT TRANSLATION TOOL                     ║${NC}"
echo -e "${BLUE}╚═══════════════════════════════════════════════════════════════════╝${NC}"
echo ""

# Check if OPENAI_API_KEY is set
if [ -z "$OPENAI_API_KEY" ]; then
    echo -e "${RED}❌ Error: OPENAI_API_KEY environment variable is not set${NC}"
    echo ""
    echo "Recommended setup for Qwen (Alibaba - most cost-effective):"
    echo -e "${YELLOW}  export OPENAI_API_KEY='sk-your-dashscope-key'${NC}"
    echo -e "${YELLOW}  export OPENAI_API_BASE='https://dashscope.aliyuncs.com/compatible-mode/v1'${NC}"
    echo ""
    echo "Get your Qwen API key at: https://dashscope.aliyun.com/"
    echo ""
    echo "Alternatively for OpenAI:"
    echo -e "${YELLOW}  export OPENAI_API_KEY='sk-your-openai-key'${NC}"
    echo -e "${YELLOW}  export OPENAI_BASE_URL='https://api.openai.com/v1'${NC}"
    echo ""
    echo "Optional environment variables:"
    echo "  export OPENAI_API_MODEL='qwen-turbo'  # Or 'qwen-plus' for better quality"
    echo ""
    exit 1
fi

# Display configuration
echo -e "${GREEN}✓ Configuration:${NC}"
echo "  API Key: ${OPENAI_API_KEY:0:8}...${OPENAI_API_KEY: -4}"

# Determine which API base is set
if [ -n "$OPENAI_API_BASE" ]; then
    echo "  Base URL: ${OPENAI_API_BASE}"
    if [[ "$OPENAI_API_BASE" == *"dashscope"* ]]; then
        echo "  Provider: Qwen (Alibaba DashScope)"
        echo "  Model: ${OPENAI_API_MODEL:-qwen-turbo (auto-detected)}"
    fi
elif [ -n "$OPENAI_BASE_URL" ]; then
    echo "  Base URL: ${OPENAI_BASE_URL}"
    if [[ "$OPENAI_BASE_URL" == *"openai"* ]]; then
        echo "  Provider: OpenAI"
        echo "  Model: ${OPENAI_API_MODEL:-gpt-4o-mini (auto-detected)}"
    fi
else
    echo "  Base URL: https://dashscope.aliyuncs.com/compatible-mode/v1 (default)"
    echo "  Provider: Qwen (Alibaba DashScope)"
    echo "  Model: ${OPENAI_API_MODEL:-qwen-turbo (auto-detected)}"
fi
echo ""

# Change to project root
cd "$PROJECT_ROOT"

# Parse command line arguments
ACTION="translate"

if [ "$1" == "--help" ] || [ "$1" == "-h" ]; then
    echo "Usage: $0 [OPTIONS]"
    echo ""
    echo "Options:"
    echo "  --dry-run              Show what would be translated without translating"
    echo "  --resume               Resume from previous run"
    echo "  --languages CODES      Translate to specific languages (comma-separated)"
    echo "  --popular              Translate to popular languages only (en,es,fr,de,it,ja,zh,ru)"
    echo "  --help, -h             Show this help message"
    echo ""
    echo "Examples:"
    echo "  $0                           # Translate to all enabled languages"
    echo "  $0 --dry-run                 # Preview what would be translated"
    echo "  $0 --languages en,es,fr      # Translate to English, Spanish, French only"
    echo "  $0 --popular                 # Translate to popular languages"
    echo "  $0 --resume                  # Resume from previous run"
    echo ""
    exit 0
fi

# Build python command
PYTHON_CMD="python3 scripts/batch-translate.py"

if [ "$1" == "--dry-run" ]; then
    echo -e "${YELLOW}🔍 Running in DRY RUN mode${NC}"
    PYTHON_CMD="$PYTHON_CMD --dry-run"
elif [ "$1" == "--resume" ]; then
    echo -e "${YELLOW}♻️  Resuming from previous run${NC}"
    PYTHON_CMD="$PYTHON_CMD --resume"
elif [ "$1" == "--popular" ]; then
    echo -e "${BLUE}🌍 Translating to popular languages${NC}"
    PYTHON_CMD="$PYTHON_CMD --languages en,es,fr,de,it,ja,zh,ru,pt,ar,hi"
elif [ "$1" == "--languages" ]; then
    if [ -z "$2" ]; then
        echo -e "${RED}❌ Error: --languages requires language codes${NC}"
        echo "Example: $0 --languages en,es,fr"
        exit 1
    fi
    echo -e "${BLUE}🌍 Translating to: $2${NC}"
    PYTHON_CMD="$PYTHON_CMD --languages $2"
fi

echo ""
echo -e "${BLUE}Starting translation process...${NC}"
echo ""

# Run the translation
eval $PYTHON_CMD

EXIT_CODE=$?

if [ $EXIT_CODE -eq 0 ]; then
    echo ""
    echo -e "${GREEN}╔═══════════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${GREEN}║              TRANSLATION COMPLETED SUCCESSFULLY                   ║${NC}"
    echo -e "${GREEN}╚═══════════════════════════════════════════════════════════════════╝${NC}"
    echo ""
else
    echo ""
    echo -e "${RED}╔═══════════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${RED}║              TRANSLATION FAILED                                   ║${NC}"
    echo -e "${RED}╚═══════════════════════════════════════════════════════════════════╝${NC}"
    echo ""
    echo "Check the error messages above for details."
    exit $EXIT_CODE
fi
