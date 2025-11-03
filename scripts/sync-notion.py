#!/usr/bin/env python3
"""
Sync Notion database to Markdown files for the NeuroBlog.

This script reads from a Notion database (e.g., "ENEM 2026 Tracker")
and exports entries to Markdown files in the docs/ directory.

Setup:
1. Create a Notion integration at https://www.notion.so/my-integrations
2. Get your integration token (NOTION_TOKEN)
3. Get your database ID from the Notion page URL
4. Share your database with the integration

Usage:
    python scripts/sync-notion.py

Environment Variables:
    NOTION_TOKEN: Your Notion integration token
    NOTION_DATABASE_ID: The ID of your Notion database
"""

import os
import json
from datetime import datetime
from pathlib import Path

# Try to import notion client (install with: pip install notion-client)
try:
    from notion_client import Client
except ImportError:
    print("Warning: notion-client not installed. Install with: pip install notion-client")
    print("This script will create a template structure instead.")
    Client = None


def get_notion_client():
    """Initialize Notion client from environment variables."""
    token = os.getenv("NOTION_TOKEN")
    if not token:
        print("Warning: NOTION_TOKEN not set. Using template mode.")
        return None
    return Client(auth=token)


def convert_notion_to_markdown(page, docs_path):
    """Convert a Notion page to Markdown format."""
    # Extract page properties (adjust based on your Notion database structure)
    title = page.get("properties", {}).get("Title", {}).get("title", [{}])[0].get("plain_text", "Untitled")
    date = page.get("properties", {}).get("Date", {}).get("date", {}).get("start", datetime.now().isoformat())
    tags = page.get("properties", {}).get("Tags", {}).get("multi_select", [])
    
    # Generate filename
    safe_title = "".join(c for c in title if c.isalnum() or c in (" ", "-", "_")).rstrip()
    filename = f"{safe_title.lower().replace(' ', '-')}.md"
    
    # Create frontmatter
    tags_list = [tag["name"] for tag in tags]
    frontmatter = f"""---
title: "{title}"
date: {date}
tags: {tags_list}
---

"""
    
    # TODO: Fetch page content from Notion API
    # For now, create a placeholder
    content = f"{frontmatter}\n# {title}\n\n*Content synced from Notion*\n"
    
    return filename, content


def sync_notion_database(database_id, docs_path):
    """Sync a Notion database to Markdown files."""
    client = get_notion_client()
    if not client:
        print("Notion client not available. Skipping sync.")
        return
    
    try:
        results = client.databases.query(database_id=database_id)
        
        for page in results.get("results", []):
            filename, content = convert_notion_to_markdown(page, docs_path)
            filepath = docs_path / filename
            
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            
            print(f"Synced: {filename}")
    
    except Exception as e:
        print(f"Error syncing from Notion: {e}")


def main():
    """Main function."""
    docs_path = Path(__file__).parent.parent / "docs" / "enem2026"
    docs_path.mkdir(parents=True, exist_ok=True)
    
    database_id = os.getenv("NOTION_DATABASE_ID")
    
    if database_id:
        sync_notion_database(database_id, docs_path)
    else:
        print("NOTION_DATABASE_ID not set.")
        print("\nTo use this script:")
        print("1. Create a Notion integration at https://www.notion.so/my-integrations")
        print("2. Set NOTION_TOKEN environment variable")
        print("3. Set NOTION_DATABASE_ID environment variable")
        print("4. Share your Notion database with the integration")


if __name__ == "__main__":
    main()

