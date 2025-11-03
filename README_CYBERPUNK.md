# ⚡ NEURAL.NEXUS /// - Cyberpunk Neuroscience Journey

<div align="center">

![Status](https://img.shields.io/badge/STATUS-ONLINE-00f3ff?style=for-the-badge&logo=statuspage&logoColor=white)
![ENEM](https://img.shields.io/badge/ENEM-2026-ff006e?style=for-the-badge&logo=academic&logoColor=white)
![Theme](https://img.shields.io/badge/THEME-CYBERPUNK_2077-ffbe0b?style=for-the-badge&logo=cyberpunk&logoColor=white)
![Neuroscience](https://img.shields.io/badge/FOCUS-COMPUTATIONAL_NEUROSCIENCE-00f3ff?style=for-the-badge&logo=brain&logoColor=white)

**Cybernetic Journey // ENEM 2026 → UFABC → Computational Neuroscience → ∞**

[🌐 Live Site](https://clouraen.github.io/ufabc-neuroscience-roadmap) | [📖 Documentation](#) | [🎨 Theme Guide](#cyberpunk-theme)

</div>

---

## 🎯 MISSION STATEMENT

This repository documents my journey from **ENEM preparation** to becoming a **computational neuroscientist** at UFABC, styled with a **Cyberpunk 2077 + Blade Runner 2049** aesthetic. It's a public learning journal, research log, and open-source contribution platform.

### Mission Phases

```
Phase 1: FOUNDATION     (2024-2025) → ENEM prep + Python + Intro Neuroscience
Phase 2: APPLICATION    (2025-2026) → Research + Projects + Mock Exams  
Phase 3: EXECUTION      (2026)      → ENEM 2026 + UFABC Admission
Phase 4: ADVANCEMENT    (2027+)     → PIBIC → FAPESP → BEPE → Master's
```

---

## 🚀 QUICK START

### Prerequisites

- Python 3.11+
- pip (Python package manager)
- Git

### Local Development

```bash
# Clone the repository
git clone https://github.com/clouraen/ufabc-neuroscience-roadmap.git
cd ufabc-neuroscience-roadmap

# Install dependencies
pip install -r requirements.txt
pip install mkdocs-material
pip install mkdocs-minify-plugin
pip install mkdocs-git-revision-date-localized-plugin

# Serve locally with cyberpunk theme
mkdocs serve --config-file mkdocs-cyberpunk.yml

# Build for production
mkdocs build --config-file mkdocs-cyberpunk.yml
```

The site will be available at `http://127.0.0.1:8000`

---

## 📂 REPOSITORY STRUCTURE

```
ufabc-neuroscience-roadmap/
│
├── .github/
│   └── workflows/
│       └── deploy-cyberpunk.yml    # Auto-deploy on commit
│
├── docs/
│   ├── index.md                     # Cyberpunk homepage
│   ├── stylesheets/
│   │   ├── cyberpunk.css           # Main cyberpunk styling
│   │   ├── glitch.css              # Glitch effects
│   │   └── neon.css                # Neon glow effects
│   ├── javascripts/
│   │   ├── cyberpunk.js            # Interactive effects
│   │   └── terminal.js             # Terminal interface
│   ├── neuroscience/               # 🧠 Neural Protocols
│   │   ├── index.md
│   │   ├── coursera-computational-neuroscience.md
│   │   ├── neuromatch-notes.md
│   │   ├── open-source-projects.md
│   │   └── research-database.md
│   ├── enem2026/                   # 📡 ENEM Matrix
│   │   ├── index.md
│   │   ├── week-01.md
│   │   ├── week-02.md
│   │   └── progress.md
│   ├── blog/                       # 💾 Memory Logs
│   │   ├── index.md
│   │   ├── pibic-dream.md
│   │   ├── fapesp-path.md
│   │   ├── mestrado-vision.md
│   │   └── daily-journal.md
│   └── templates/                  # 🔧 Dev Templates
│       ├── index.md
│       ├── weekly-template.md
│       ├── monthly-summary.md
│       └── research-log.md
│
├── scripts/                        # Automation scripts
│   ├── sync-notion.py
│   ├── translate-content.py
│   └── batch-translate.sh
│
├── mkdocs-cyberpunk.yml            # Cyberpunk theme config
├── requirements.txt
└── README.md
```

---

## 🎨 CYBERPUNK THEME

### Design Philosophy

Inspired by **Cyberpunk 2077** and **Blade Runner 2049**, the theme features:

- **Neon Color Palette:**
  - Cyan: `#00f3ff` (Primary accent)
  - Magenta: `#ff006e` (Secondary accent)
  - Yellow: `#ffbe0b` (Highlights)
  - Dark backgrounds with grid patterns

- **Visual Effects:**
  - Glitch animations on headers
  - Neon glow on interactive elements
  - Scanline overlays (CRT effect)
  - Matrix-style digital rain background
  - Terminal-style code blocks

- **Typography:**
  - Roboto Mono (headers & UI)
  - Fira Code (code blocks)
  - Uppercase headers with letter-spacing
  - Monospace everywhere for tech aesthetic

### Custom Components

#### Neon Buttons
```html
<a href="path" class="neon-btn">
  <span></span><span></span><span></span><span></span>
  Button Text
</a>
```

#### Glow Cards
```html
<div class="glow-card">
  Your content here
</div>
```

#### Neon Badges
```html
<span class="neon-badge">Default</span>
<span class="neon-badge magenta">Magenta</span>
<span class="neon-badge yellow">Yellow</span>
```

#### Progress Bars
```html
<div class="neon-progress">
  <div class="neon-progress-bar" style="width: 75%;"></div>
</div>
```

### Interactive Terminal

Access the cyberpunk terminal by:
- Clicking the "⌨️ TERMINAL" button (bottom right)
- Pressing `Ctrl + ~`

Available commands:
```bash
help        # Display available commands
status      # System status information
mission     # Mission objectives
neuro       # Neuroscience progress
github      # Open GitHub profile
cyberpunk   # Random Cyberpunk 2077 quote
whoami      # User information
clear       # Clear terminal
```

---

## 🔄 AUTOMATIC DEPLOYMENT

### GitHub Actions Workflow

Every commit to `main` automatically:

1. ✅ Builds the MkDocs site with cyberpunk theme
2. ✅ Optimizes HTML/CSS/JS
3. ✅ Deploys to GitHub Pages
4. ✅ Reports deployment status

**Workflow file:** `.github/workflows/deploy-cyberpunk.yml`

### Manual Deployment

```bash
# Build and deploy to GitHub Pages
mkdocs gh-deploy --config-file mkdocs-cyberpunk.yml
```

---

## 📊 CONTENT STRUCTURE

### Navigation Hierarchy

```
⚡ MAINFRAME (Home)
├── 🧠 NEURAL.PROTOCOLS (Neuroscience)
│   ├── Coursera Archives
│   ├── Neuromatch Logs
│   ├── OpenSource Ops
│   └── Research Database
├── 📡 ENEM.MATRIX //2026
│   ├── Weekly Logs
│   └── Progress Dashboard
├── 💾 MEMORY.LOGS (Blog)
│   ├── PIBIC Dream Protocol
│   ├── FAPESP Route Map
│   ├── Mestrado Vision
│   └── Daily Journal
└── 🔧 DEV.TEMPLATES
    ├── Weekly Template
    ├── Monthly Summary
    └── Research Log
```

---

## 🛠️ TECH STACK

### Core Technologies
- **Static Site Generator:** MkDocs Material
- **Styling:** Custom CSS (Cyberpunk theme)
- **Interactivity:** Vanilla JavaScript
- **Deployment:** GitHub Actions + GitHub Pages
- **Content:** Markdown + YAML frontmatter

### Python Dependencies
```txt
mkdocs>=1.5.3
mkdocs-material>=9.4.0
mkdocs-minify-plugin>=0.7.0
mkdocs-git-revision-date-localized-plugin>=1.2.0
pymdown-extensions>=10.0
```

### Additional Features
- Multi-language support (243+ languages via Google Translate)
- Notion API integration for content sync
- Git-based version control
- Responsive design (mobile-friendly)

---

## 🌍 MULTI-LANGUAGE SUPPORT

The site supports **243+ languages** through automated translation:

```bash
# Translate to popular languages
./scripts/batch-translate.sh --popular

# Translate to specific languages
./scripts/batch-translate.sh --languages en,es,fr,de,it

# Translate to all enabled languages
./scripts/batch-translate.sh
```

See [TRANSLATION_GUIDE.md](TRANSLATION_GUIDE.md) for details.

---

## 📈 PROGRESS TRACKING

### Current Status

```
⚡ NEURAL.NEXUS STATUS REPORT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ENEM PREP:        [█████████░] 90%
NEUROSCIENCE:     [███████░░░] 70%
PROGRAMMING:      [████████░░] 80%
RESEARCH:         [█████░░░░░] 50%
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE:            FOUNDATION (1/4)
NEXT MILESTONE:   ENEM Mock Exam Q2 2025
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Key Metrics
- **Study Hours:** 450+ hours
- **Completed Courses:** 3
- **GitHub Contributions:** 15+
- **Blog Posts:** 12
- **ENEM Practice Score:** 680 → Target: 800+

---

## 🤝 CONTRIBUTING

This is a personal learning journal, but suggestions and feedback are welcome!

### Ways to Contribute
1. 🐛 Report issues or bugs
2. 💡 Suggest improvements to theme/design
3. 📚 Share neuroscience resources
4. 🎨 Propose visual enhancements
5. 🌐 Help with translations

### Code Style
- Follow existing cyberpunk naming conventions
- Use `neon-*` classes for themed components
- Maintain monospace typography
- Keep the dark + neon aesthetic

---

## 📜 LICENSE

MIT License - feel free to fork and adapt for your own journey!

---

## 🔗 CONNECT

<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-clouraen-00f3ff?style=for-the-badge&logo=github&logoColor=white)](https://github.com/clouraen)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-ff006e?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/cleiton-moura-loura)
[![Website](https://img.shields.io/badge/Site-Neural.Nexus-ffbe0b?style=for-the-badge&logo=firefox&logoColor=white)](https://clouraen.github.io/ufabc-neuroscience-roadmap)

</div>

---

## 💭 INSPIRATION

> **"Open knowledge is the future of neuroscience."**  
> — Ross Markello, *abagen developer*

> **"Wake the f*** up, Samurai. We have a city to burn."**  
> — Johnny Silverhand, *Cyberpunk 2077*

> **"I've seen things you people wouldn't believe..."**  
> — Roy Batty, *Blade Runner*

---

<div align="center">

## ⚡ WAKE UP, SAMURAI ///

### WE HAVE NEUROSCIENCE TO LEARN

**© 2024-2026 Cleiton Moura Loura // NEURAL.NEXUS // All Rights Reserved**

*Powered by MkDocs Material + Cyberpunk Theme*

</div>
