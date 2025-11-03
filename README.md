# 🧠 UFABC Computational Neuroscience Roadmap
**Author:** Cleiton Moura Loura  
**Goal:** Enter UFABC (ENEM 2026) → specialize in *Computational Neuroscience* → grow through open-source research + scholarships *(PIBIC → FAPESP → BEPE → Mestrado)*  

---

## 🌍 Vision
This repository is my public learning journal.  
It tracks my full journey from **ENEM preparation** to **academic research** — integrating study logs, open-source contributions, and reflections.  
Each milestone is documented to inspire other students to follow an open science path.

---

## 📂 Repository Structure

```
ufabc-neuroscience-roadmap/
│
├── README.md
├── docs/
│   ├── index.md
│   ├── enem2026/
│   │   ├── week-01.md
│   │   ├── week-02.md
│   │   └── ...
│   ├── neuroscience/
│   │   ├── coursera-computational-neuroscience.md
│   │   ├── neuromatch-notes.md
│   │   └── open-source-projects.md
│   ├── blog/
│   │   ├── pibic-dream.md
│   │   ├── fapesp-path.md
│   │   └── mestrado-vision.md
│   └── templates/
│       ├── weekly-template.md
│       ├── monthly-summary.md
│       └── research-log.md
│
├── .github/workflows/publish.yml
├── progress.json
└── scripts/sync-notion.py
```

---

## 🗓️ Weekly Template (`docs/templates/weekly-template.md`)

```markdown
---
title: "ENEM Week {{week_number}}"
date: {{date}}
tags: [enem, study, neuroscience, ufabc]
---

## 📚 Study Summary
- **Português:** ...
- **Matemática:** ...
- **Ciências da Natureza:** ...
- **Humanas:** ...
- **Redação:** ...

## 🧩 Projects
- [ ] Coursera: Computational Neuroscience (Module X)
- [ ] GitHub: abagen / nilearn PR review
- [ ] Python: neural signal processing notebook

## 💭 Reflection
> "This week I learned how neurons and neural networks relate mathematically…"

## 🔗 Resources
- [Video: Synaptic Transmission Explained](link)
- [Repo: abagen](https://github.com/rmarkello/abagen)
```

---

## 📈 Monthly Summary (`docs/templates/monthly-summary.md`)

```markdown
---
title: "Monthly Summary — {{month}} {{year}}"
---

## 🧮 ENEM Progress
| Subject | Hours | Improvement | Notes |
|----------|--------|-------------|--------|
| Math | 22h | +8% | mastering functions |
| Biology | 18h | +6% | neurophysiology focus |
| Redação | 6 essays | +200 pts | improved structure |

## 🧠 Research
- Finished **Neuromatch Academy Unit 1**
- Contributed to **abagen documentation**
- Started **Git + Python Neuro Notebooks**

## 🧩 Next Steps
- Prepare for UFABC ENEM simulation  
- Study GitHub Pages + Jekyll customization  
```

---

## 🧪 Research Log (`docs/templates/research-log.md`)

```markdown
---
title: "Computational Neuroscience Research Log"
date: {{date}}
---

## Project
**Topic:** Neural data representation using open atlases  
**Repo:** [Cleiton Moura Loura's abagen-fork](https://github.com/DarkHuggy/abagen-fork)

## Notes
- Learned about **Allen Brain Atlas** and **gene expression maps**
- Explored **abagen pipeline** and **BIDS** format
- Possible mini-project: visualize UFABC datasets using MNE-Python

## Related Reading
- Markello & Arnatkevičiūtė (2021). *Abagen: A toolbox for...*  
- UFABC Neuroengineering Group papers
```

---

## 🌐 GitHub Pages Setup

### Option A — *Jekyll (simple)*
Create `_config.yml` inside `/docs`:
```yaml
title: "Cleiton Moura Loura NeuroBlog"
theme: jekyll-theme-cayman
markdown: kramdown
baseurl: ""
```

Enable Pages:  
> **Settings → Pages → Source → "Deploy from branch" → `/docs`**

---

### Option B — *MkDocs (professional look)*
```yaml
site_name: Cleiton Moura Loura NeuroBlog
theme:
  name: material
  features:
    - navigation.expand
    - content.code.copy
nav:
  - Home: index.md
  - ENEM 2026: enem2026/index.md
  - Neuroscience: neuroscience/index.md
  - Blog: blog/index.md
```

Run locally:
```bash
pip install mkdocs-material
mkdocs serve
mkdocs gh-deploy
```

---

## ⚙️ Automation Flow
- **Daily:** update Notion "ENEM 2026 Tracker"  
- **Weekly:** `scripts/sync-notion.py` exports to Markdown  
- **GitHub Action:** deploys to GitHub Pages  
- **Visitors:** see your live open-source neuroscience journey 🚀  

---

## ✨ Optional Enhancements

| Feature | Tool |
|----------|------|
| Graph of study hours | Python + Matplotlib |
| Comments | giscus.app |
| RSS Feed | MkDocs Blog plugin |
| Custom Domain | `darkhuggy.dev/neuroblog` |
| Notion Sync | Notion API + Python script |

---

## 🧭 Roadmap Overview

| Phase | Duration | Focus |
|-------|-----------|-------|
| **Phase 1 (2024-2025)** | Foundations | ENEM core subjects + Python basics + intro neuroscience |
| **Phase 2 (2025-2026)** | Application | Open-source projects + research + mock exams |
| **Phase 3 (2026)** | Execution | ENEM 2026 + publish learning blog + UFABC admission |
| **Phase 4 (2027+)** | Growth | PIBIC → FAPESP → BEPE → Master's in Computational Neuroscience |

---

## 💡 Inspiration
> "Open knowledge is the future of neuroscience."  
> — Ross Markello, *Abagen developer*

---

## 🧩 Connect
- **GitHub:** [Cleiton Moura Loura's GitHub](https://github.com/DarkHuggy)  
- **NeuroBlog:** [darkhuggy.github.io/ufabc-neuroscience-roadmap](https://darkhuggy.github.io/ufabc-neuroscience-roadmap)

---

### 🧱 Next step
You can now:
1. Create this repo on GitHub (`ufabc-neuroscience-roadmap`)  
2. Copy this file as your main `README.md`  
3. Add `/docs` templates and push  
4. Enable **GitHub Pages** → your live NeuroBlog will appear automatically 🌱  

---

## 🌍 Multi-Language Support - 243 Languages!

This repository supports **all 243+ languages** from Google Translate! 🎉

### Current Status
- **158+ languages defined** in `languages.json`
- **Currently enabled:** Portuguese (pt) and English (en)
- **Expandable to:** All 243+ Google Translate languages
- **Language switcher:** Dynamic dropdown with "View All" option

### Quick Enable All Languages
```bash
# Enable all 158+ languages at once
python scripts/enable-all-languages.py

# Generate folder structure for all enabled languages
python scripts/generate-all-languages.py
```

### Language Features
- Dynamic dropdown language switcher on every page
- Browser language detection with localStorage preference
- Language selection page showing all available languages
- RTL (Right-to-Left) support for Arabic, Hebrew, Urdu, etc.
- Automatic URL routing with language prefixes

### Adding Translations

**Option 1: Automatic Translation (Recommended)**
```bash
# Set up API credentials
export OPENAI_API_KEY='your-api-key'
export OPENAI_BASE_URL='https://api.openai.com/v1'  # Optional
export OPENAI_API_MODEL='gpt-4o-mini'  # Optional

# Translate all content to all enabled languages
python scripts/translate-content.py

# Or translate to specific language
python scripts/translate-content.py --lang es
```

**Option 2: Manual Translation**
```bash
# Generate English translation templates from Portuguese content
python scripts/create-translation-template.py

# Update language metadata in files
python scripts/update-lang-frontmatter.py pt docs/pt/
python scripts/update-lang-frontmatter.py en docs/en/
```

See `docs/TRANSLATION_API.md` for automatic translation setup.

### Supported Languages Include:
🌍 **Major Languages:** English, Spanish, French, German, Italian, Portuguese  
🌏 **Asian:** Chinese, Japanese, Korean, Hindi, Thai, Vietnamese  
🌍 **Middle Eastern:** Arabic, Hebrew, Persian, Urdu, Turkish  
🌍 **African:** Swahili, Zulu, Xhosa, Amharic, Hausa  
🌍 **Regional:** Catalan, Basque, Galician, Welsh, Irish  
🌍 **And 150+ more languages!**

See `docs/MULTILANGUAGE.md` for complete documentation.
