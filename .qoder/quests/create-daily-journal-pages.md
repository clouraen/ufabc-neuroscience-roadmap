# Design: Daily Journal Page Generation System

## Objective

Create a structured daily journal system spanning from November 2, 2025 through October 31, 2026, providing dedicated pages for documenting personal learning experiences and organizing daily study content across ENEM preparation subjects and computational neuroscience topics.

## Scope

### Time Range
- **Start Date**: November 2, 2025 (Sunday)
- **End Date**: October 31, 2026 (Saturday)
- **Total Days**: 365 days

### Content Coverage
- ENEM preparation subjects (Português, Matemática, Ciências da Natureza, Humanas, Redação)
- Computational neuroscience learning activities
- Personal reflections and daily experiences
- Progress tracking and resource documentation

## Target Directory Structure

The daily journal pages will be organized hierarchically within the existing documentation structure:

```
docs/
├── pt/
│   ├── journal/
│   │   ├── 2025/
│   │   │   ├── 11-november/
│   │   │   │   ├── 2025-11-02.md
│   │   │   │   ├── 2025-11-03.md
│   │   │   │   └── ... (through 2025-11-30)
│   │   │   └── 12-december/
│   │   │       ├── 2025-12-01.md
│   │   │       └── ... (through 2025-12-31)
│   │   └── 2026/
│   │       ├── 01-january/
│   │       ├── 02-february/
│   │       ├── ... (continuing months)
│   │       └── 10-october/
│   │           └── ... (through 2026-10-31)
│   └── templates/
│       └── daily-journal-template.md (reference template)
└── en/
    └── journal/ (mirrored structure for English version)
```

### Directory Naming Convention
- Year directories: `YYYY` format (e.g., `2025`, `2026`)
- Month directories: `MM-month_name` format (e.g., `11-november`, `01-january`)
- File names: `YYYY-MM-DD.md` format (e.g., `2025-11-02.md`)

## Daily Journal Template Structure

Each daily journal page will follow a consistent template with the following sections:

### Frontmatter Metadata
| Field | Description | Example |
|-------|-------------|---------|
| `lang` | Language code | `pt` or `en` |
| `title` | Page title with date | `"Daily Journal - November 2, 2025"` |
| `date` | ISO date format | `2025-11-02` |
| `day_of_week` | Weekday name | `Sunday` (Portuguese: `Domingo`) |
| `tags` | Content categorization | `[journal, enem, neuroscience, daily-log]` |

### Content Sections

#### 1. Daily Reflection Section
**Purpose**: Personal documentation of experiences, emotions, thoughts, and observations from the day

**Structure**:
- Open-ended text area for narrative writing
- Prompting questions to guide reflection
- Space for emotional check-in

#### 2. ENEM Study Plan Section
**Purpose**: Organize and track daily study activities for ENEM subjects

**Subjects Covered**:
- Português (Portuguese Language & Literature)
- Matemática (Mathematics)
- Ciências da Natureza (Natural Sciences: Physics, Chemistry, Biology)
- Ciências Humanas (Humanities: History, Geography, Philosophy, Sociology)
- Redação (Essay Writing)

**Per-Subject Structure**:
- Topic focus for the day
- Study goals checklist
- Time allocation tracking
- Notes and key learnings

#### 3. Computational Neuroscience Section
**Purpose**: Document learning activities related to neuroscience and research preparation

**Content Areas**:
- Online courses (Coursera, Neuromatch Academy)
- Research paper reading
- Programming practice (Python, neural data analysis)
- Open-source project contributions
- Theoretical concept exploration

**Structure**:
- Topic/module being studied
- Learning objectives
- Code experiments or exercises
- Questions and areas for deeper study

#### 4. Progress Tracking Section
**Purpose**: Monitor completed tasks and productivity

**Elements**:
- Daily task checklist
- Pomodoro or time-block tracking
- Study hours logged
- Milestone achievements

#### 5. Resources and References Section
**Purpose**: Catalog materials used and discovered during the day

**Types of Resources**:
- Video lectures
- Articles and papers
- GitHub repositories
- Online tools
- Book chapters

#### 6. Tomorrow's Planning Section
**Purpose**: Prepare and organize next day's priorities

**Elements**:
- Priority tasks list
- Subject focus areas
- Scheduled activities
- Preparation notes

## Template Example (Portuguese)

```
---
lang: pt
title: "Diário - {{day}} de {{month_name}} de {{year}}"
date: {{YYYY-MM-DD}}
day_of_week: {{weekday_name}}
tags: [journal, enem, neuroscience, daily-log]
---

# 📅 {{day}} de {{month_name}} de {{year}} - {{weekday_name}}

## 💭 Reflexão do Dia

Como foi meu dia hoje? O que aprendi? Como me senti?

---

## 📚 Plano de Estudos ENEM

### Português
**Tópico do dia:**  
**Objetivos:**
- [ ] 
- [ ] 

**Tempo dedicado:**  
**Anotações:**

### Matemática
**Tópico do dia:**  
**Objetivos:**
- [ ] 
- [ ] 

**Tempo dedicado:**  
**Anotações:**

### Ciências da Natureza
**Tópico do dia:**  
**Objetivos:**
- [ ] 
- [ ] 

**Tempo dedicado:**  
**Anotações:**

### Ciências Humanas
**Tópico do dia:**  
**Objetivos:**
- [ ] 
- [ ] 

**Tempo dedicado:**  
**Anotações:**

### Redação
**Tópico do dia:**  
**Objetivos:**
- [ ] 
- [ ] 

**Tempo dedicado:**  
**Anotações:**

---

## 🧠 Neurociência Computacional

**Atividade do dia:**  
**Objetivos:**
- [ ] 
- [ ] 

**Progresso:**

**Conceitos aprendidos:**

**Código/Experimentos:**

**Dúvidas para explorar:**

---

## ✅ Progresso do Dia

**Tarefas Concluídas:**
- [ ] 
- [ ] 
- [ ] 

**Horas de estudo:** 

**Conquistas:**

---

## 🔗 Recursos Utilizados

- [Título do recurso](link)
- 

---

## 📝 Planejamento para Amanhã

**Prioridades:**
1. 
2. 
3. 

**Foco principal:**  

**Preparação necessária:**

---

*"Every day is a new opportunity to grow and learn."*
```

## Study Content Distribution Strategy

### Weekday vs Weekend Differentiation

| Day Type | ENEM Focus | Neuroscience Focus | Reflection Emphasis |
|----------|------------|-------------------|---------------------|
| Monday-Friday | High intensity, 2-3 subjects per day | 1-2 hours focused practice | Brief daily check-in |
| Saturday | Light review, essay practice | Project work, coding | Weekly review reflection |
| Sunday | Rest or catch-up | Course videos, reading | Weekly planning, deeper reflection |

### Subject Rotation Recommendation

To ensure comprehensive coverage without overwhelming daily load:

- **Daily Core**: Rotate 2-3 ENEM subjects per day
- **Weekly Coverage**: All 5 ENEM areas covered within each week
- **Neuroscience Integration**: Daily small increment (30-60 minutes)
- **Intensive Days**: Weekends for deeper dives and project work

### Suggested Weekly Pattern

| Day | Primary ENEM Subjects | Neuroscience Activity |
|-----|----------------------|----------------------|
| Monday | Português + Matemática | Coursera module |
| Tuesday | Ciências da Natureza + Redação | Python practice |
| Wednesday | Humanas + Matemática | Research reading |
| Thursday | Português + Ciências da Natureza | GitHub contribution |
| Friday | All subjects (light review) | Theory consolidation |
| Saturday | Redação (full essay) | Project coding |
| Sunday | Reading/catch-up | Course completion |

**Note**: This is a suggested pattern to be included as guidance within the template, allowing flexibility for daily customization.

## Multi-Language Support Integration

### Primary Language: Portuguese (pt)
- Main content creation in `/docs/pt/journal/`
- Full Portuguese template with culturally appropriate phrasing
- Date formatting: "2 de novembro de 2025"
- Weekday names in Portuguese

### Secondary Language: English (en)
- Parallel structure in `/docs/en/journal/`
- English template version
- Date formatting: "November 2, 2025"
- Compatible with existing translation workflow

### Translation Workflow Compatibility
The daily journal pages should integrate with existing translation infrastructure:
- Frontmatter includes `lang` field for language detection
- Content structure supports automated translation via `translate-content.py`
- Markdown syntax compatible with translation processing
- Template variable placeholders translation-friendly

## MkDocs Navigation Integration

### Navigation Structure Addition

The `mkdocs.yml` configuration will require navigation entries for the daily journal section:

```
nav:
  - Home: pt/index.md
  - ENEM 2026:
    - pt/enem2026/index.md
    - pt/enem2026/week-01.md
    - pt/enem2026/week-02.md
  - Daily Journal:
    - pt/journal/index.md
    - 2025:
      - November: pt/journal/2025/11-november/
      - December: pt/journal/2025/12-december/
    - 2026:
      - January: pt/journal/2026/01-january/
      - February: pt/journal/2026/02-february/
      - ... (all months through October)
  - Neuroscience:
    - pt/neuroscience/index.md
    ...
```

### Index Pages

Create monthly and yearly index pages to facilitate navigation:

| Index Type | Purpose | Location Example |
|------------|---------|------------------|
| Journal Home | Overview of journal system, quick links | `docs/pt/journal/index.md` |
| Yearly Index | List all months in year with summaries | `docs/pt/journal/2025/index.md` |
| Monthly Index | Calendar view or list of all days | `docs/pt/journal/2025/11-november/index.md` |

### Calendar Navigation Enhancement

Consider adding a calendar-style navigation component to improve browsing:
- Visual monthly calendar showing days with entries
- Quick date picker functionality
- Progress indicators (completed vs. incomplete entries)

## Automation Script Design

### Script Purpose
Automate the generation of 365 daily journal pages with proper directory structure, consistent naming, and pre-filled template content.

### Script Requirements

| Requirement | Description |
|-------------|-------------|
| Date Range Handling | Calculate all dates from 2025-11-02 to 2026-10-31 |
| Directory Creation | Auto-create year/month directory structure |
| Template Population | Fill template variables with date-specific values |
| Bilingual Support | Generate both Portuguese and English versions |
| Overwrite Protection | Check for existing files to prevent data loss |
| Weekday Calculation | Determine correct day of week for each date |
| Month Name Localization | Translate month names to Portuguese/English |

### Script Input Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `start_date` | Date | First journal date | 2025-11-02 |
| `end_date` | Date | Last journal date | 2026-10-31 |
| `output_dir` | Path | Base directory for journal files | `docs/pt/journal/` |
| `template_path` | Path | Template file location | `docs/pt/templates/daily-journal-template.md` |
| `language` | String | Target language | `pt` |
| `force_overwrite` | Boolean | Overwrite existing files | `false` |

### Script Output

- 365 markdown files in Portuguese (pt directory)
- 365 markdown files in English (en directory)
- Directory structure with year/month organization
- Index files for navigation
- Generation summary report

### Template Variable Substitution

The script will replace template placeholders with actual date values:

| Placeholder | Replacement Logic | Example (Nov 2, 2025) |
|-------------|-------------------|----------------------|
| `{{day}}` | Day number | `2` |
| `{{month_name}}` | Localized month name | `novembro` (pt) / `November` (en) |
| `{{year}}` | Four-digit year | `2025` |
| `{{YYYY-MM-DD}}` | ISO date format | `2025-11-02` |
| `{{weekday_name}}` | Localized weekday | `Domingo` (pt) / `Sunday` (en) |

### Month Name Localization Tables

**Portuguese Month Names:**
| Number | Name |
|--------|------|
| 01 | janeiro |
| 02 | fevereiro |
| 03 | março |
| 04 | abril |
| 05 | maio |
| 06 | junho |
| 07 | julho |
| 08 | agosto |
| 09 | setembro |
| 10 | outubro |
| 11 | novembro |
| 12 | dezembro |

**Portuguese Weekday Names:**
| Number | Name |
|--------|------|
| 0 | Domingo |
| 1 | Segunda-feira |
| 2 | Terça-feira |
| 3 | Quarta-feira |
| 4 | Quinta-feira |
| 5 | Sexta-feira |
| 6 | Sábado |

### Error Handling

The script should handle:
- Invalid date ranges
- Missing template files
- Permission errors during directory creation
- Disk space limitations
- Character encoding issues for non-ASCII characters

## Content Guidance System

### Study Topic Suggestions

To help with daily planning, each template can include contextual suggestions based on:

#### ENEM Preparation Timeline
- **November 2025 - February 2026**: Foundation building, core concepts
- **March - June 2026**: Intensive practice, problem-solving
- **July - September 2026**: Advanced topics, integration
- **October 2026**: Review, mock exams, final preparation

#### Computational Neuroscience Learning Path
- **Beginner Phase**: Coursera fundamentals, basic Python
- **Intermediate Phase**: Neuromatch Academy, neural data analysis
- **Advanced Phase**: Research contributions, paper reading
- **Project Phase**: Original research or open-source contributions

### Adaptive Study Recommendations

While the template provides structure, include guidance notes suggesting:
- Lighter academic load on Fridays for mental rest
- Weekend project-based learning for deeper engagement
- Pre-exam weeks focus on ENEM review over new neuroscience topics
- Holiday periods for catching up or exploring passion projects

## Integration with Existing System

### Compatibility with Current Features

| Existing Component | Integration Point | Adaptation Needed |
|-------------------|------------------|-------------------|
| Weekly ENEM logs | Daily journals complement weekly summaries | Cross-reference links between daily and weekly content |
| Blog posts | Personal reflections can evolve into blog entries | Flag significant journal entries for blog expansion |
| Neuroscience notes | Daily neuroscience section feeds into research logs | Link to detailed course notes and project documentation |
| Templates directory | Daily template stored alongside existing templates | Consistent formatting and metadata structure |
| Translation system | Daily journals follow same multilingual pattern | Compatible frontmatter and markdown structure |

### Notion Sync Consideration

The existing `sync-notion.py` script syncs content from Notion. Consider:
- Whether daily journals will be written in Notion first, then synced
- Or written directly in markdown files
- Potential for bidirectional sync to enable mobile journaling via Notion

### GitHub Pages Deployment

Daily journal pages will be automatically published via existing GitHub Actions workflow when:
- Changes pushed to repository
- MkDocs builds static site including journal pages
- Deployed to GitHub Pages with proper navigation

## Quality Assurance Criteria

### Template Validation
- All date variables correctly substituted
- Frontmatter YAML syntax valid
- Links and references properly formatted
- Language-appropriate content for pt/en versions

### Structural Validation
- Directory hierarchy matches specification
- File naming convention consistent
- No duplicate dates
- Complete date range coverage (all 365 days)

### Content Validation
- All template sections present in each file
- Checkbox markdown syntax correct
- Headings hierarchy logical
- Metadata fields complete

## Future Enhancement Opportunities

### Analytics and Insights
- Study hours aggregation across all daily entries
- Subject coverage heatmap visualization
- Progress tracking dashboards
- Habit streak tracking

### Automation Enhancements
- Daily journal reminder notifications
- Auto-populate completed tasks from previous day's planning
- Smart study plan suggestions based on historical patterns
- Integration with calendar apps for time blocking

### Community Features
- Public sharing of sanitized journal entries
- Study buddy matching based on journal topics
- Community study challenges and accountability
- Aggregated learning resources from all journals

### AI-Assisted Features
- Reflection prompt generation based on day's activities
- Study plan optimization recommendations
- Progress anomaly detection (falling behind alerts)
- Personalized learning path adjustments

## Success Metrics

The daily journal system will be considered successful if it achieves:

1. **Consistency**: Provides structure for daily documentation from Nov 2025 through Oct 2026
2. **Completeness**: All 365 days have pre-generated, accessible journal pages
3. **Usability**: Easy navigation and clear template structure
4. **Integration**: Seamlessly fits within existing documentation ecosystem
5. **Flexibility**: Allows customization while maintaining structure
6. **Motivation**: Encourages regular journaling and learning habits

## Implementation Notes

### Technical Constraints
- Markdown files must be UTF-8 encoded to support Portuguese characters
- YAML frontmatter must use proper escaping for special characters
- File paths should be cross-platform compatible (avoid OS-specific separators in script)

### Content Constraints
- Keep template open-ended to accommodate varying daily experiences
- Avoid overly prescriptive structure that might discourage journaling
- Balance between guidance and freedom

### Maintenance Considerations
- Template updates should be easy to propagate to existing pages if needed
- Version control allows tracking of journal evolution over time
- Backup strategy important due to personal nature of journal content
