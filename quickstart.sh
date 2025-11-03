#!/bin/bash

# ⚡ NEURAL.NEXUS QUICK START SCRIPT ///
# Cyberpunk theme setup automation

set -e

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "⚡ NEURAL.NEXUS QUICK START ///"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Colors
CYAN='\033[0;36m'
MAGENTA='\033[0;35m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check Python
echo -e "${CYAN}[1/5] Checking Python installation...${NC}"
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
    echo "✅ Python $PYTHON_VERSION found"
else
    echo "❌ Python 3 not found. Please install Python 3.11+"
    exit 1
fi

# Check pip
echo -e "${CYAN}[2/5] Checking pip installation...${NC}"
if command -v pip3 &> /dev/null; then
    echo "✅ pip found"
else
    echo "❌ pip not found. Please install pip"
    exit 1
fi

# Install dependencies
echo -e "${CYAN}[3/5] Installing dependencies...${NC}"
echo "This may take a few minutes..."
pip3 install -r requirements.txt
echo "✅ Dependencies installed"

# Verify MkDocs
echo -e "${CYAN}[4/5] Verifying MkDocs installation...${NC}"
if command -v mkdocs &> /dev/null; then
    MKDOCS_VERSION=$(mkdocs --version | cut -d' ' -f3)
    echo "✅ MkDocs $MKDOCS_VERSION installed"
else
    echo "❌ MkDocs not found. Installation may have failed."
    exit 1
fi

# Check theme files
echo -e "${CYAN}[5/5] Checking cyberpunk theme files...${NC}"
if [ -f "docs/stylesheets/cyberpunk.css" ]; then
    echo "✅ cyberpunk.css found"
else
    echo "⚠️  cyberpunk.css not found"
fi

if [ -f "docs/javascripts/cyberpunk.js" ]; then
    echo "✅ cyberpunk.js found"
else
    echo "⚠️  cyberpunk.js not found"
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo -e "${MAGENTA}✅ SETUP COMPLETE ///${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo -e "${YELLOW}Next steps:${NC}"
echo ""
echo "  1. Start development server:"
echo -e "     ${CYAN}mkdocs serve --config-file mkdocs-cyberpunk.yml${NC}"
echo ""
echo "  2. View site at:"
echo -e "     ${CYAN}http://127.0.0.1:8000${NC}"
echo ""
echo "  3. Build for production:"
echo -e "     ${CYAN}mkdocs build --config-file mkdocs-cyberpunk.yml${NC}"
echo ""
echo "  4. Deploy to GitHub Pages:"
echo -e "     ${CYAN}mkdocs gh-deploy --config-file mkdocs-cyberpunk.yml${NC}"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo -e "${MAGENTA}⚡ WAKE UP, SAMURAI ///${NC}"
echo -e "${CYAN}WE HAVE NEUROSCIENCE TO LEARN${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
