# 🚀 CYBERPUNK SETUP GUIDE

Complete guide to setting up and deploying the Neural Nexus Cyberpunk theme.

---

## 📋 PREREQUISITES

### Required Software
- **Python 3.11+** - [Download](https://www.python.org/downloads/)
- **Git** - [Download](https://git-scm.com/downloads)
- **pip** - Comes with Python
- **Text Editor** - VS Code, Sublime, or similar

### Optional Tools
- **Node.js** - For additional automation
- **Docker** - For containerized deployment

---

## ⚡ QUICK SETUP (5 Minutes)

### 1. Clone Repository

```bash
git clone https://github.com/clouraen/ufabc-neuroscience-roadmap.git
cd ufabc-neuroscience-roadmap
```

### 2. Install Dependencies

```bash
# Install Python packages
pip install -r requirements.txt

# Verify installation
mkdocs --version
```

### 3. Run Locally

```bash
# Start development server with cyberpunk theme
mkdocs serve --config-file mkdocs-cyberpunk.yml

# Site available at: http://127.0.0.1:8000
```

### 4. Build for Production

```bash
# Generate static site
mkdocs build --config-file mkdocs-cyberpunk.yml

# Output in: site/
```

---

## 🎨 THEME CUSTOMIZATION

### Color Scheme

Edit `docs/stylesheets/cyberpunk.css`:

```css
:root {
  /* Change primary colors */
  --cyber-cyan: #00f3ff;      /* Neon cyan */
  --cyber-magenta: #ff006e;   /* Neon magenta */
  --cyber-yellow: #ffbe0b;    /* Neon yellow */
  
  /* Adjust backgrounds */
  --bg-darkest: #0a0e27;      /* Darkest layer */
  --bg-dark: #0f1419;         /* Dark layer */
}
```

### Typography

Edit `mkdocs-cyberpunk.yml`:

```yaml
theme:
  font:
    text: Roboto Mono        # Change main font
    code: Fira Code          # Change code font
```

### Effects Intensity

Edit `docs/javascripts/cyberpunk.js`:

```javascript
// Adjust matrix rain density
const columns = canvas.width / fontSize;  // More = denser

// Change glitch frequency
setInterval(randomGlitch, 5000);  // Higher = less frequent
```

---

## 🔧 CONFIGURATION

### MkDocs Settings

**Main config:** `mkdocs-cyberpunk.yml`

Key sections:
```yaml
site_name: "Your Site Name"
site_url: https://yourusername.github.io/your-repo

theme:
  name: material
  palette:
    - scheme: cyberpunk  # Dark mode
    - scheme: bladerunner  # Light mode
  
  features:
    - navigation.instant
    - search.suggest
    # ... more features
```

### Navigation Structure

```yaml
nav:
  - Home: index.md
  - Section 1:
      - subsection/index.md
      - subsection/page1.md
  - Section 2:
      - subsection2/index.md
```

### Plugins

```yaml
plugins:
  - search          # Built-in search
  - minify          # Minify HTML/CSS/JS
  - git-revision-date-localized  # Show last updated
```

---

## 🌐 DEPLOYMENT OPTIONS

### GitHub Pages (Recommended)

#### Automatic Deployment

Every commit to `main` triggers auto-deployment via GitHub Actions.

**Workflow:** `.github/workflows/deploy-cyberpunk.yml`

#### Manual Deployment

```bash
# Deploy to gh-pages branch
mkdocs gh-deploy --config-file mkdocs-cyberpunk.yml
```

#### Enable GitHub Pages

1. Go to repository **Settings**
2. Navigate to **Pages**
3. Source: **Deploy from a branch**
4. Branch: **gh-pages** / **root**
5. Save

### Alternative Hosting

#### Netlify

```bash
# Build command
mkdocs build --config-file mkdocs-cyberpunk.yml

# Publish directory
site/
```

#### Vercel

```json
{
  "buildCommand": "mkdocs build --config-file mkdocs-cyberpunk.yml",
  "outputDirectory": "site"
}
```

#### Custom Server

```bash
# Build site
mkdocs build --config-file mkdocs-cyberpunk.yml

# Copy to server
rsync -avz site/ user@server:/var/www/html/
```

---

## 📝 CONTENT MANAGEMENT

### Creating New Pages

```bash
# Create new markdown file
touch docs/section/new-page.md

# Add frontmatter
cat > docs/section/new-page.md << 'EOF'
---
title: "Page Title"
description: "Page description"
---

# Page Content Here
EOF

# Add to navigation in mkdocs-cyberpunk.yml
```

### Using Templates

```bash
# Copy template
cp docs/templates/weekly-template.md docs/enem2026/week-15.md

# Fill in content
# ... edit file ...

# Commit and push (auto-deploys)
git add docs/enem2026/week-15.md
git commit -m "Add week 15 study log"
git push
```

### Batch Content Generation

```bash
# Generate multiple weeks
for i in {15..20}; do
  cp docs/templates/weekly-template.md docs/enem2026/week-$i.md
done
```

---

## 🎯 CYBERPUNK COMPONENTS

### Use Themed Elements

#### Neon Badges

```markdown
<span class="neon-badge">Default</span>
<span class="neon-badge magenta">Magenta</span>
<span class="neon-badge yellow">Yellow</span>
```

#### Glow Cards

```markdown
<div class="glow-card">
  <h3>Card Title</h3>
  <p>Card content with hover glow effect</p>
</div>
```

#### Progress Bars

```markdown
<div class="neon-progress">
  <div class="neon-progress-bar" style="width: 75%;"></div>
</div>
```

#### Neon Buttons

```markdown
<a href="path" class="neon-btn">
  <span></span><span></span><span></span><span></span>
  Button Text
</a>
```

#### Dividers

```markdown
<div class="neon-divider"></div>
```

---

## 🐛 TROUBLESHOOTING

### Common Issues

#### MkDocs Not Found

```bash
# Reinstall
pip install --upgrade mkdocs mkdocs-material
```

#### Theme Not Loading

```bash
# Clear browser cache
# Hard refresh: Ctrl+Shift+R (Windows) / Cmd+Shift+R (Mac)

# Verify CSS files exist
ls docs/stylesheets/
# Should show: cyberpunk.css, glitch.css, neon.css
```

#### JavaScript Errors

```bash
# Check browser console (F12)
# Verify JS files exist
ls docs/javascripts/
# Should show: cyberpunk.js, terminal.js
```

#### Build Errors

```bash
# Verbose build output
mkdocs build --config-file mkdocs-cyberpunk.yml --verbose

# Check for syntax errors in markdown files
# Validate YAML frontmatter
```

### Performance Issues

```bash
# Reduce matrix rain particles
# Edit docs/javascripts/cyberpunk.js
const particleCount = 50;  // Reduce from 100

# Disable effects on mobile
if (window.innerWidth > 768) {
  initMatrixRain();
}
```

---

## 🔄 UPDATING

### Update Dependencies

```bash
# Update all packages
pip install --upgrade -r requirements.txt

# Update specific package
pip install --upgrade mkdocs-material
```

### Pull Latest Changes

```bash
# Fetch and merge upstream
git pull origin main

# Rebuild site
mkdocs build --config-file mkdocs-cyberpunk.yml
```

### Update Theme

```bash
# Pull latest theme files
git checkout main -- docs/stylesheets/ docs/javascripts/

# Test locally
mkdocs serve --config-file mkdocs-cyberpunk.yml
```

---

## 📊 MONITORING

### Analytics Setup

Add to `mkdocs-cyberpunk.yml`:

```yaml
extra:
  analytics:
    provider: google
    property: G-XXXXXXXXXX
```

### Performance Monitoring

```bash
# Check build time
time mkdocs build --config-file mkdocs-cyberpunk.yml

# Check site size
du -sh site/

# Lighthouse audit
npx lighthouse http://127.0.0.1:8000 --view
```

---

## 🚀 ADVANCED FEATURES

### Custom Domain

1. Add `CNAME` file to `docs/`:
```bash
echo "your-domain.com" > docs/CNAME
```

2. Configure DNS:
```
Type: CNAME
Name: www
Value: yourusername.github.io
```

### Search Optimization

```yaml
# In mkdocs-cyberpunk.yml
plugins:
  - search:
      separator: '[\s\-\_\:\!\[\]\(\)\"\`\/\.]+'
      lang: en
```

### Multi-language Support

```bash
# Run translation script
./scripts/batch-translate.sh --languages en,es,fr

# Update config for language selector
# See docs/languages/index.md
```

---

## 📚 RESOURCES

### Official Documentation
- [MkDocs](https://www.mkdocs.org/)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- [GitHub Pages](https://pages.github.com/)

### Community
- [MkDocs Discussions](https://github.com/mkdocs/mkdocs/discussions)
- [Material Theme Discussions](https://github.com/squidfunk/mkdocs-material/discussions)

### Tutorials
- [Creating a blog with MkDocs](https://squidfunk.github.io/mkdocs-material/setup/)
- [GitHub Actions for MkDocs](https://github.com/marketplace/actions/deploy-mkdocs)

---

## 🤝 SUPPORT

### Getting Help

1. **Documentation:** Check this guide first
2. **Issues:** Search [GitHub Issues](https://github.com/clouraen/ufabc-neuroscience-roadmap/issues)
3. **Discussions:** Start a [Discussion](https://github.com/clouraen/ufabc-neuroscience-roadmap/discussions)
4. **Contact:** Reach out via [GitHub](https://github.com/clouraen)

### Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

<div align="center">

**⚡ NEURAL.NEXUS SETUP COMPLETE ///**

Ready to build your cyberpunk site!

</div>
