#!/usr/bin/env python3
"""
Helper script to update Claude configuration files with MCP server settings.
Used by installation scripts to modify JSON config files.

Usage:
    python scripts/update_claude_config.py <config_file_path>

Arguments:
    config_file_path: Path to Claude config JSON file

This script will:
1. Create the config file if it doesn't exist
2. Preserve existing configuration
3. Add or update the clarion-knowledge-base MCP server entry
"""

import json
import os
import sys
from pathlib import Path


def update_claude_config(config_file_path):
    """Update Claude config file with Clarion MCP server configuration."""

    # MCP server configuration
    mcp_config = {
        "clarion-knowledge-base": {
            "command": "docker",
            "args": ["exec", "-i", "clarion-mcp-server", "python", "/app/src/mcp_server.py"]
        }
    }

    config_path = Path(config_file_path)

    # Create parent directory if it doesn't exist
    config_path.parent.mkdir(parents=True, exist_ok=True)

    # Read existing config or create new one
    if config_path.exists():
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
        except json.JSONDecodeError as e:
            print(f"Warning: Existing config has invalid JSON: {e}")
            print("Creating new config file...")
            config = {}
    else:
        config = {}

    # Add or update mcpServers section
    if 'mcpServers' not in config:
        config['mcpServers'] = {}

    config['mcpServers'].update(mcp_config)

    # Write back with pretty formatting
    with open(config_path, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=2, ensure_ascii=False)
        f.write('\n')  # Add trailing newline

    print(f"✓ Config updated successfully: {config_path}")
    return True


def main():
    if len(sys.argv) < 2:
        print("Error: Config file path required")
        print(f"Usage: {sys.argv[0]} <config_file_path>")
        sys.exit(1)

    config_file = sys.argv[1]

    try:
        update_claude_config(config_file)
        sys.exit(0)
    except Exception as e:
        print(f"✗ Error updating config: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
