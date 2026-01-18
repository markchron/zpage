#!/usr/bin/env python3
"""
Script to update image paths in markdown files by adding /assets/images/ prefix.

Usage:
    python update_image_paths.py <markdown_file>
    
Example:
    python update_image_paths.py _posts/2026-01-17-resrsim-benchmark.md
"""

import sys
import re
from pathlib import Path


def update_image_paths(file_path, prefix="/assets/images/"):
    """
    Update image paths in a markdown file by adding a prefix.
    
    Args:
        file_path: Path to the markdown file
        prefix: Prefix to add to image paths (default: /assets/images/)
    """
    file_path = Path(file_path)
    
    if not file_path.exists():
        print(f"Error: File '{file_path}' not found.")
        return False
    
    # Read the file content
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Track changes
    changes_made = 0
    
    # Pattern for markdown image syntax: ![alt](path)
    # Matches images that don't already start with {{ or http/https
    pattern = r'!\[([^\]]*)\]\((?!http|https|\{\{)([^)]+)\)'
    
    def replace_path(match):
        nonlocal changes_made
        alt_text = match.group(1)
        image_path = match.group(2)
        
        # Add the prefix with Jekyll's relative_url filter
        new_path = f'{{{{ "{prefix}{image_path}" | relative_url }}}}'
        changes_made += 1
        
        print(f"  Updating: {image_path} -> {new_path}")
        return f"![{alt_text}]({new_path})"
    
    # Replace all matching image paths
    updated_content = re.sub(pattern, replace_path, content)
    
    if changes_made > 0:
        # Write back to file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        print(f"\n✓ Updated {changes_made} image path(s) in '{file_path}'")
        return True
    else:
        print(f"No image paths to update in '{file_path}'")
        return False


def main():
    if len(sys.argv) < 2:
        print("Usage: python update_image_paths.py <markdown_file>")
        print("\nExample:")
        print("  python update_image_paths.py _posts/2026-01-17-resrsim-benchmark.md")
        sys.exit(1)
    
    markdown_file = sys.argv[1]
    update_image_paths(markdown_file)


if __name__ == "__main__":
    main()
