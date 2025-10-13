# Clarion Knowledge Base - Plugin Conversion Plan

## Current Status
- ✅ MCP server fully functional (21,747 vectors, Qdrant database)
- ✅ GitHub repository created: https://github.com/peterparker57/clarion-knowledge-base
- ✅ Release v1.0.0 with 76MB snapshot published
- ✅ Docker infrastructure working (docker-compose + Dockerfile)
- ✅ Installation scripts created (install.sh, install.bat)
- ⏳ **Repository is PRIVATE** (needs to be public for plugin)

## Goal
Convert the existing MCP server into a Claude Code plugin for easy installation:
```bash
# Add the marketplace
/plugin marketplace add https://github.com/peterparker57/clarion-knowledge-base.git

# Install the plugin
/plugin install clarion-knowledge-base
```

---

## Phase 1: Make Repository Public

**Why:** Claude Code plugins require public repositories for marketplace distribution and to enable direct downloads without authentication.

**Tasks:**
1. Change repository visibility from private to public via GitHub settings
2. Verify snapshot can be downloaded without authentication:
   ```bash
   curl -L -o test.tar.gz https://github.com/peterparker57/clarion-knowledge-base/releases/download/v1.0.0/qdrant-snapshot.tar.gz
   ```
3. Confirm README displays correctly on GitHub landing page

**Time:** 5 minutes

---

## Phase 2: Create Plugin Structure

### 2.1 Create `.claude-plugin/marketplace.json`

**Location:** `.claude-plugin/marketplace.json`

**Purpose:** Defines the marketplace metadata and embeds plugin configuration for Claude Code.

**Content structure (corrected in v1.1.1):**
```json
{
  "$schema": "https://anthropic.com/claude-code/marketplace.schema.json",
  "name": "clarion-knowledge-base-marketplace",
  "version": "1.1.1",
  "description": "Clarion programming documentation search for Claude Code",
  "owner": {
    "name": "peterparker57",
    "email": "support@clarion-kb.com"
  },
  "plugins": [
    {
      "name": "clarion-knowledge-base",
      "version": "1.1.1",
      "description": "Semantic search for Clarion programming documentation. MCP server with 21,747 indexed chunks from 21 Clarion PDFs.",
      "author": {
        "name": "peterparker57"
      },
      "repository": "https://github.com/peterparker57/clarion-knowledge-base",
      "homepage": "https://github.com/peterparker57/clarion-knowledge-base",
      "license": "MIT",
      "source": ".",
      "category": "documentation",
      "tags": ["clarion", "documentation", "search", "mcp", "qdrant"],
      "strict": false,

      "mcpServers": {
        "clarion-knowledge-base": {
          "command": "docker",
          "args": ["exec", "-i", "clarion-mcp-server", "python", "/app/src/mcp_server.py"],
          "description": "Semantic search across Clarion programming documentation"
        }
      },

      "hooks": {
        "postInstall": {
          "command": "bash",
          "args": ["scripts/plugin-install.sh"]
        }
      },

      "requirements": {
        "docker": {
          "required": true,
          "message": "Docker Desktop must be installed and running. Download from: https://www.docker.com/products/docker-desktop"
        }
      }
    }
  ]
}
```

**Key changes in v1.1.1:**
- Proper marketplace structure with `$schema`, `owner`, and `plugins` array
- Plugin configuration embedded inside `plugins[0]` with `strict: false`
- Added marketplace-specific fields: `source`, `category`
- Corrected to follow Claude Code marketplace schema

---

### 2.2 Create Plugin Installation Hook

**Location:** `scripts/plugin-install.sh`

**Purpose:** Automates Docker setup when plugin is installed.

**Requirements:**
- Must work on Windows (Git Bash), macOS, and Linux
- Check prerequisites (Docker)
- Download snapshot from GitHub Release
- Build and start Docker containers
- Import Qdrant snapshot
- Verify installation
- Provide clear error messages

**Script structure:**
```bash
#!/usr/bin/env bash
set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo "================================================================"
echo "  Clarion Knowledge Base - Plugin Installation"
echo "================================================================"

# 1. Check Docker
if ! command -v docker &> /dev/null; then
    echo -e "${RED}Error: Docker is not installed${NC}"
    echo "Please install Docker Desktop: https://www.docker.com/products/docker-desktop"
    exit 1
fi

if ! docker info &> /dev/null; then
    echo -e "${RED}Error: Docker is not running${NC}"
    echo "Please start Docker Desktop and try again"
    exit 1
fi

# 2. Get repository root
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
REPO_DIR="$( cd "$SCRIPT_DIR/.." && pwd )"
cd "$REPO_DIR"

# 3. Download snapshot if not exists
SNAPSHOT_FILE="qdrant-snapshot.tar.gz"
SNAPSHOT_URL="https://github.com/peterparker57/clarion-knowledge-base/releases/download/v1.0.0/qdrant-snapshot.tar.gz"

if [ ! -f "$SNAPSHOT_FILE" ]; then
    echo -e "${YELLOW}Downloading Qdrant snapshot (76 MB)...${NC}"
    if command -v curl &> /dev/null; then
        curl -L -o "$SNAPSHOT_FILE" "$SNAPSHOT_URL" --progress-bar
    elif command -v wget &> /dev/null; then
        wget -O "$SNAPSHOT_FILE" "$SNAPSHOT_URL"
    else
        echo -e "${RED}Error: Neither curl nor wget found${NC}"
        exit 1
    fi
    echo -e "${GREEN}✓ Snapshot downloaded${NC}"
else
    echo -e "${GREEN}✓ Snapshot already exists${NC}"
fi

# 4. Build Docker images
echo -e "${YELLOW}Building Docker images...${NC}"
docker-compose build --quiet
echo -e "${GREEN}✓ Images built${NC}"

# 5. Start containers
echo -e "${YELLOW}Starting Docker containers...${NC}"
docker-compose up -d
echo -e "${GREEN}✓ Containers started${NC}"

# 6. Wait for Qdrant to be healthy
echo -e "${YELLOW}Waiting for Qdrant to be ready...${NC}"
for i in {1..30}; do
    if docker exec clarion-mcp-server curl -s http://qdrant:6333/health &> /dev/null; then
        echo -e "${GREEN}✓ Qdrant is healthy${NC}"
        break
    fi
    if [ $i -eq 30 ]; then
        echo -e "${RED}Error: Qdrant failed to start${NC}"
        exit 1
    fi
    sleep 2
done

# 7. Import snapshot
echo -e "${YELLOW}Importing vector database...${NC}"
docker exec clarion-mcp-server python /app/scripts/import_snapshot.py "/app/$SNAPSHOT_FILE"
echo -e "${GREEN}✓ Database imported${NC}"

# 8. Verify collection
echo -e "${YELLOW}Verifying installation...${NC}"
POINT_COUNT=$(docker exec clarion-mcp-server python -c "
from qdrant_client import QdrantClient
client = QdrantClient(host='qdrant', port=6333)
collection = client.get_collection('clarion_docs')
print(collection.points_count)
")

if [ "$POINT_COUNT" -gt 20000 ]; then
    echo -e "${GREEN}✓ Verification successful: $POINT_COUNT documents indexed${NC}"
else
    echo -e "${RED}Error: Expected 21,747 documents, found $POINT_COUNT${NC}"
    exit 1
fi

echo ""
echo "================================================================"
echo -e "${GREEN}  Installation Complete!${NC}"
echo "================================================================"
echo ""
echo "The Clarion Knowledge Base MCP server is now running."
echo "Restart Claude Code to start using it."
echo ""
echo "Try asking: 'How do I create a browse procedure in Clarion?'"
echo ""
```

**Parallel Work Opportunity:** This script can run independently while documentation is being updated.

---

### 2.3 Create Slash Commands (Optional)

**Location:** `.claude/commands/`

**Commands to create:**

1. **`.claude/commands/clarion-search.md`**
```markdown
Search Clarion documentation using semantic search.

Usage: /clarion-search <query>

Examples:
- /clarion-search how to create a browse
- /clarion-search FILE driver syntax
- /clarion-search ABC library templates

This command uses the Clarion Knowledge Base MCP server to search across 21,747 indexed documentation chunks from 21 Clarion PDF manuals.
```

2. **`.claude/commands/clarion-setup.md`**
```markdown
Re-run the Clarion Knowledge Base Docker setup.

Usage: /clarion-setup

This will:
1. Check Docker is running
2. Start/restart containers
3. Verify the database is loaded
4. Display status

Use this if containers were stopped or after system restart.
```

3. **`.claude/commands/clarion-status.md`**
```markdown
Check status of Clarion Knowledge Base Docker containers.

Usage: /clarion-status

Displays:
- Container running status (clarion-qdrant, clarion-mcp-server)
- Qdrant health check
- Database collection stats
- MCP server connectivity

Quick diagnostic tool.
```

**Parallel Work Opportunity:** Slash commands can be created by a separate subagent while plugin infrastructure is being built.

---

### 2.4 Update Documentation

**Files to update:**

1. **README.md** - Major rewrite
   - Move plugin installation to TOP as primary method
   - Add prominent badge/section: "Install in 30 seconds"
   - Keep manual installation as "Advanced Installation"
   - Update quick start section
   - Add troubleshooting for plugin-specific issues

2. **Create PLUGIN.md** - New file
   - What is a Claude Code plugin
   - How this plugin works
   - What happens during installation
   - Plugin-specific troubleshooting
   - Slash command reference
   - How to uninstall/disable

3. **Update INSTALLATION.md**
   - Add plugin installation section at top
   - Mark manual installation as "Alternative Method"
   - Add section on plugin vs manual pros/cons

**Example README.md update:**
```markdown
# Clarion Knowledge Base

Semantic search for Clarion programming documentation via Claude AI.

[![Claude Code Plugin](https://img.shields.io/badge/Claude%20Code-Plugin-blue)](https://github.com/peterparker57/clarion-knowledge-base)
[![Docker](https://img.shields.io/badge/Docker-Required-blue)](https://www.docker.com/products/docker-desktop)

## Quick Install (30 seconds)

```bash
# Step 1: Add the marketplace
/plugin marketplace add https://github.com/peterparker57/clarion-knowledge-base.git

# Step 2: Install the plugin
/plugin install clarion-knowledge-base
```

That's it! Restart Claude Code and start asking about Clarion.

## What You Get

- 🔍 Semantic search across 21 Clarion PDF manuals
- 📚 21,747 indexed documentation chunks
- ⚡ Fast query responses (<2 seconds)
- 🐳 Automated Docker setup
- 💡 Works with Claude Code and Claude Desktop

[Rest of README...]
```

**Parallel Work Opportunity:** Documentation can be updated by a separate subagent while plugin code is being written.

---

## Phase 3: Testing

### 3.1 Local Testing

**Prerequisites:**
- Stop existing containers: `docker-compose down`
- Remove existing config if testing fresh

**Test commands:**
```bash
# 1. Add marketplace
/plugin marketplace add https://github.com/peterparker57/clarion-knowledge-base.git

# 2. Install plugin
/plugin install clarion-knowledge-base

# 3. Wait for installation to complete

# 4. Restart Claude Code

# 5. Test MCP server
Ask: "How do I create a browse in Clarion?"

# 5. Test slash commands (if created)
/clarion-status
/clarion-search browse procedures
```

**What to verify:**
- ✅ Plugin installs without errors
- ✅ Docker containers start automatically
- ✅ Snapshot downloads and imports
- ✅ MCP server responds to queries
- ✅ Slash commands work (if implemented)
- ✅ Error messages are clear and helpful

### 3.2 Clean Machine Testing

**After local validation, test on clean machine:**
1. Machine with Docker Desktop installed
2. Claude Code installed
3. No previous Clarion Knowledge Base setup
4. Run installation commands:
   ```bash
   /plugin marketplace add https://github.com/peterparker57/clarion-knowledge-base.git
   /plugin install clarion-knowledge-base
   ```
5. Verify complete installation

---

## Phase 4: Release

### 4.1 Git Commit and Tag

```bash
git add .
git commit -m "Add Claude Code plugin support

- Add .claude-plugin/marketplace.json for plugin distribution
- Create automated installation hook (scripts/plugin-install.sh)
- Add optional slash commands for convenience
- Update documentation for plugin-first installation
- Create PLUGIN.md with plugin-specific docs

This enables easy two-step installation:
/plugin marketplace add https://github.com/peterparker57/clarion-knowledge-base.git
/plugin install clarion-knowledge-base

🤖 Generated with Claude Code

Co-Authored-By: Claude <noreply@anthropic.com>"

git tag v1.1.0
git push origin main --tags
```

### 4.2 Create GitHub Release

**Title:** Clarion Knowledge Base v1.1.0 - Claude Code Plugin Support

**Release notes:**
```markdown
# What's New in v1.1.0

## Claude Code Plugin Support 🎉

You can now install the Clarion Knowledge Base with two simple commands:

```bash
# Add the marketplace
/plugin marketplace add https://github.com/peterparker57/clarion-knowledge-base.git

# Install the plugin
/plugin install clarion-knowledge-base
```

Installation takes ~30 seconds and handles all Docker setup automatically!

## Changes

- ✨ Added Claude Code plugin support
- ✨ Automated Docker setup via installation hook
- ✨ Optional slash commands for common operations
- 📝 Updated documentation with plugin-first installation
- 🔓 Repository is now public for easier access

## Installation Methods

### Plugin (Recommended)
```bash
/plugin marketplace add https://github.com/peterparker57/clarion-knowledge-base.git
/plugin install clarion-knowledge-base
```

### Manual Installation
See [INSTALLATION.md](INSTALLATION.md) for manual Docker setup.

## Requirements

- Docker Desktop (installed and running)
- Claude Code or Claude Desktop

## Release Assets

- **qdrant-snapshot.tar.gz** (76 MB) - Pre-populated vector database
  - Automatically downloaded by plugin installer
  - 21,747 indexed Clarion documentation chunks

---

Built with Claude Code for the Clarion Developer Community

🤖 Generated with [Claude Code](https://claude.com/claude-code)
```

---

## Parallel Execution Opportunities

The following tasks can be done simultaneously by different subagents:

**Group A (Plugin Infrastructure):**
1. Create `.claude-plugin/marketplace.json`
2. Create `scripts/plugin-install.sh`
3. Test installation hook locally

**Group B (Slash Commands):**
1. Create `.claude/commands/clarion-search.md`
2. Create `.claude/commands/clarion-setup.md`
3. Create `.claude/commands/clarion-status.md`

**Group C (Documentation):**
1. Update README.md for plugin-first approach
2. Create PLUGIN.md
3. Update INSTALLATION.md
4. Update QUICK_START.md

**Sequential Dependencies:**
- Group A, B, C can all run in parallel
- Testing requires Group A to be complete
- Git commit/release requires all groups complete

---

## Success Criteria

- ✅ Plugin installs with single command
- ✅ Docker setup is fully automated
- ✅ Snapshot downloads from public GitHub Release
- ✅ Containers start and import database successfully
- ✅ MCP server responds to queries
- ✅ Documentation is clear and plugin-focused
- ✅ Works on clean machine with zero prior setup
- ✅ Installation time < 2 minutes (most time is downloading 76MB)

---

## Estimated Timeline

- Phase 1 (Make Public): 5 minutes
- Phase 2 (Plugin Structure): 2-3 hours
  - marketplace.json: 15 minutes
  - plugin-install.sh: 1 hour
  - Slash commands: 30 minutes
  - Documentation: 1 hour
- Phase 3 (Testing): 30 minutes
- Phase 4 (Release): 15 minutes

**Total: 3-4 hours**

---

## Rollback Plan

If plugin conversion has issues:
- Keep v1.0.0 available (manual installation still works)
- Plugin is additive - doesn't break existing functionality
- Can revert to private repo if needed (though breaks plugin downloads)
