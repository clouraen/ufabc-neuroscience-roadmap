# Translation Guide / Guia de Tradução

## Structure / Estrutura

The site supports multiple languages. Content is organized as:

- `/pt/` - Portuguese (default)
- `/en/` - English

O site suporta múltiplos idiomas. O conteúdo é organizado como:

- `/pt/` - Português (padrão)
- `/en/` - Inglês

## Adding New Content / Adicionando Novo Conteúdo

### Portuguese (Default)
1. Create your content in `docs/pt/`
2. Ensure frontmatter includes `lang: pt`

### English
1. Run the translation template generator:
   ```bash
   python scripts/create-translation-template.py
   ```
2. Edit the English files in `docs/en/`
3. Replace `[Translation needed]` placeholders
4. Update frontmatter: `lang: en`

## Updating Language Metadata

To update language metadata in existing files:

```bash
# For Portuguese files
python scripts/update-lang-frontmatter.py pt docs/pt/

# For English files
python scripts/update-lang-frontmatter.py en docs/en/
```

## Language Switcher

The language switcher is automatically included via `_includes/language-switcher.html`. It appears on all pages and allows users to switch between Portuguese and English versions.

## Notes

- Keep file structure consistent between languages
- Update links to use language prefixes (`/pt/` or `/en/`)
- Both languages share the same templates and assets

