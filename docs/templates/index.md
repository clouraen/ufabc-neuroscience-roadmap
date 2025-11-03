---
title: "🔧 DEV.TEMPLATES"
description: "Reusable templates for content creation"
---

# <span class="neon-sign">🔧 DEV.TEMPLATES ///</span>

<div class="neon-divider"></div>

<div class="hologram" style="padding: 2rem; margin: 2rem 0;">

## 📝 CONTENT GENERATION PROTOCOLS

Standardized templates for consistent documentation and efficient content creation.

<div style="margin-top: 1.5rem;">
<span class="neon-badge">Templates</span>
<span class="neon-badge magenta">Automation</span>
<span class="neon-badge yellow">Consistency</span>
<span class="neon-badge">Efficiency</span>
</div>

</div>

---

## 📋 AVAILABLE TEMPLATES

<div class="glow-card" style="margin: 1.5rem 0;">

### [📅 Weekly Study Log](weekly-template.md)
<span class="neon-badge yellow">ENEM PREP</span>

Structured template for documenting weekly study progress across all ENEM subjects.

**Includes:**
- Study hours per subject
- Topics covered
- Practice questions completed
- Reflection & insights
- Next week's goals

</div>

<div class="glow-card" style="margin: 1.5rem 0;">

### [📊 Monthly Summary](monthly-summary.md)
<span class="neon-badge magenta">PROGRESS REVIEW</span>

Comprehensive monthly review template for tracking overall progress.

**Includes:**
- Subject-wise performance
- Mock exam scores
- Research milestones
- Blog post count
- Next month's priorities

</div>

<div class="glow-card" style="margin: 1.5rem 0;">

### [🔬 Research Log](research-log.md)
<span class="neon-badge">NEUROSCIENCE</span>

Template for documenting research activities, papers read, and experiments.

**Includes:**
- Research topic/question
- Methodology notes
- Data & observations
- Related literature
- Next steps

</div>

---

## 🎯 TEMPLATE USAGE

### Quick Start

1. **Choose Template:** Select the appropriate template for your content type
2. **Copy Markdown:** Copy the template markdown to your new file
3. **Fill Sections:** Replace placeholder text with your content
4. **Customize:** Adapt sections as needed
5. **Publish:** Commit and push to auto-deploy

### Best Practices

<ul class="neon-list">
  <li><strong>Consistency:</strong> Use templates for similar content types</li>
  <li><strong>Adaptation:</strong> Modify templates to fit specific needs</li>
  <li><strong>Documentation:</strong> Keep template documentation updated</li>
  <li><strong>Automation:</strong> Use scripts to generate from templates</li>
  <li><strong>Version Control:</strong> Track template changes in git</li>
</ul>

---

## 🛠️ TEMPLATE STRUCTURE

### Standard Frontmatter

All templates include YAML frontmatter:

```yaml
---
title: "Document Title"
date: YYYY-MM-DD
tags: [tag1, tag2, tag3]
category: enem/neuroscience/blog/templates
status: draft/published
---
```

### Common Sections

Most templates share these sections:

- **Header:** Title and metadata
- **Summary:** Brief overview
- **Main Content:** Topic-specific information
- **Reflection:** Personal insights
- **Resources:** Links and references
- **Next Steps:** Action items

---

## 📝 WEEKLY TEMPLATE PREVIEW

```markdown
---
title: "ENEM Week {{week_number}}"
date: {{YYYY-MM-DD}}
tags: [enem, study, weekly]
---

## 📚 STUDY SUMMARY

### Matemática
- **Hours:** {{hours}}
- **Topics:** {{topics}}
- **Practice:** {{questions}} questions

### Ciências da Natureza
- **Hours:** {{hours}}
- **Topics:** {{topics}}

### Ciências Humanas
- **Hours:** {{hours}}
- **Topics:** {{topics}}

### Linguagens
- **Hours:** {{hours}}
- **Topics:** {{topics}}

## 🧠 NEUROSCIENCE ACTIVITIES
- {{activity_1}}
- {{activity_2}}

## 💭 WEEKLY REFLECTION
{{reflection}}

## 🎯 NEXT WEEK GOALS
- [ ] {{goal_1}}
- [ ] {{goal_2}}
```

---

## 📊 MONTHLY TEMPLATE PREVIEW

```markdown
---
title: "Monthly Summary — {{Month}} {{Year}}"
date: {{YYYY-MM-DD}}
tags: [monthly, progress, summary]
---

## 📈 ENEM PROGRESS

| Subject | Hours | Score | Improvement |
|---------|-------|-------|-------------|
| Matemática | {{h}} | {{s}} | {{i}}% |
| Ciências | {{h}} | {{s}} | {{i}}% |
| Humanas | {{h}} | {{s}} | {{i}}% |
| Linguagens | {{h}} | {{s}} | {{i}}% |

## 🧠 RESEARCH HIGHLIGHTS
- {{highlight_1}}
- {{highlight_2}}

## 📝 BLOG POSTS
- {{post_1}}
- {{post_2}}

## 🎯 NEXT MONTH PRIORITIES
1. {{priority_1}}
2. {{priority_2}}
```

---

## 🔬 RESEARCH TEMPLATE PREVIEW

```markdown
---
title: "Research Log: {{Topic}}"
date: {{YYYY-MM-DD}}
tags: [research, neuroscience]
---

## 🎯 RESEARCH QUESTION
{{question}}

## 🔬 METHODOLOGY
{{methods}}

## 📊 DATA & OBSERVATIONS
{{data}}

## 📚 RELATED LITERATURE
- {{paper_1}}
- {{paper_2}}

## 💡 INSIGHTS
{{insights}}

## 🔜 NEXT STEPS
- [ ] {{step_1}}
- [ ] {{step_2}}
```

---

## ⚙️ AUTOMATION SCRIPTS

### Generate from Template

```python
# scripts/generate-from-template.py
import datetime
from pathlib import Path

def generate_weekly_log(week_number):
    template = Path('docs/templates/weekly-template.md').read_text()
    date = datetime.date.today()
    
    content = template.replace('{{week_number}}', str(week_number))
    content = content.replace('{{YYYY-MM-DD}}', str(date))
    
    output_path = f'docs/enem2026/week-{week_number:02d}.md'
    Path(output_path).write_text(content)
    print(f'Generated: {output_path}')

# Usage:
# python scripts/generate-from-template.py 15
```

### Batch Generate

```bash
#!/bin/bash
# Generate next 4 weeks of logs
for i in {15..18}; do
  python scripts/generate-from-template.py $i
done
```

---

## 🎨 CYBERPUNK STYLING GUIDE

### Use Themed Components

```markdown
<!-- Neon Badge -->
<span class="neon-badge">Status</span>
<span class="neon-badge magenta">Important</span>
<span class="neon-badge yellow">Warning</span>

<!-- Glow Card -->
<div class="glow-card">
Your content here
</div>

<!-- Neon Button -->
<a href="path" class="neon-btn">Button Text</a>

<!-- Progress Bar -->
<div class="neon-progress">
  <div class="neon-progress-bar" style="width: 75%;"></div>
</div>

<!-- Divider -->
<div class="neon-divider"></div>

<!-- Hologram Effect -->
<div class="hologram">Content</div>
```

---

## 📦 TEMPLATE MANAGEMENT

### Version Control

All templates are version-controlled in Git:

```bash
# View template history
git log -- docs/templates/

# Revert to previous template version
git checkout HEAD~1 -- docs/templates/weekly-template.md

# Create new template
cp docs/templates/weekly-template.md docs/templates/custom-template.md
git add docs/templates/custom-template.md
git commit -m "Add custom template"
```

### Template Validation

```python
# scripts/validate-templates.py
import yaml
from pathlib import Path

def validate_frontmatter(filepath):
    content = Path(filepath).read_text()
    if not content.startswith('---'):
        return False, "Missing frontmatter"
    
    try:
        yaml_content = content.split('---')[1]
        yaml.safe_load(yaml_content)
        return True, "Valid"
    except:
        return False, "Invalid YAML"

# Validate all templates
for template in Path('docs/templates').glob('*.md'):
    valid, msg = validate_frontmatter(template)
    print(f'{template.name}: {msg}')
```

---

## 🚀 ADVANCED USAGE

### Notion Integration

Sync templates with Notion databases:

```python
# scripts/sync-templates-notion.py
from notion_client import Client

notion = Client(auth=os.environ["NOTION_API_KEY"])
database_id = os.environ["NOTION_DATABASE_ID"]

# Create page from template
notion.pages.create(
    parent={"database_id": database_id},
    properties={
        "Title": {"title": [{"text": {"content": "Week 15"}}]},
        "Type": {"select": {"name": "ENEM Study Log"}},
    },
    children=[/* Markdown blocks */]
)
```

### Automated Publishing

GitHub Actions workflow to auto-generate weekly logs:

```yaml
name: Auto-generate Weekly Log
on:
  schedule:
    - cron: '0 0 * * 0'  # Every Sunday

jobs:
  generate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: python scripts/generate-from-template.py
      - run: git commit -m "Auto-generate weekly log"
      - run: git push
```

---

<div style="text-align: center; margin: 3rem 0; padding: 2rem; border: 2px solid #00f3ff; border-radius: 8px; background: rgba(0, 243, 255, 0.05);">

**⚡ "Templates are the scaffolding of consistent creativity."**

**🔧 Build once, reuse infinitely.**

[← Back to Mainframe](../index.md){ .neon-btn }

</div>
