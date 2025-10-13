# Session Handoff - Clarion Knowledge Base Plugin

**Date:** October 12, 2025
**Current Version:** v1.1.6
**Status:** Schema fixed + cross-platform support added

---

## Current Status

The Clarion Knowledge Base MCP server has been successfully converted to a Claude Code plugin. The latest version (v1.1.6) fixes the hook schema validation error and adds cross-platform installation support.

### Latest Release
- **Version:** v1.1.6
- **Release URL:** https://github.com/peterparker57/clarion-knowledge-base/releases/tag/v1.1.6 (pending)
- **Repository:** https://github.com/peterparker57/clarion-knowledge-base (PUBLIC)
- **Status:** Hook schema fixed, cross-platform support added (Windows/Mac/Linux)

---

## What's New in v1.1.6

### Hook Schema Fix
**Problem in v1.1.5:**
```json
"hooks": {
  "postInstall": {
    "command": "bash",
    "args": ["scripts/plugin-install.sh"]
  }
}
```

**Fixed in v1.1.6:**
```json
"hooks": {
  "PostInstall": "./scripts/plugin-install.js"
}
```

**Changes:**
- ✅ Capitalized hook key: `PostInstall` (was `postInstall`)
- ✅ Simple string path format (was object with command/args)
- ✅ Points to cross-platform Node.js wrapper

### Cross-Platform Installation Support
Created three installation scripts:
1. **`scripts/plugin-install.js`** - Node.js wrapper (cross-platform, used by hook)
   - Detects Windows vs Mac/Linux
   - Automatically runs the correct script
2. **`scripts/plugin-install.ps1`** - PowerShell version (Windows native)
   - Full-featured installation script
   - Uses PowerShell built-in to Windows
3. **`scripts/plugin-install.sh`** - Bash version (Mac/Linux, existing)
   - Original bash script maintained
4. **`scripts/plugin-install.cmd`** - Batch wrapper (Windows alternative)
   - Calls PowerShell script
   - Fallback option

---

## Installation Command (For End Users)

```bash
# Step 1: Add the marketplace
/plugin marketplace add https://github.com/peterparker57/clarion-knowledge-base.git

# Step 2: Install the plugin
/plugin install clarion-knowledge-base
```

**IMPORTANT:** Use the HTTPS URL, NOT the shorthand `owner/repo` format (requires SSH keys).

---

## Plugin Structure (v1.1.5)

### Correct Two-File Setup

```
.claude-plugin/
├── marketplace.json  (marketplace metadata only)
└── plugin.json       (plugin configuration: mcpServers, hooks, requirements)
```

### Key Configuration Details

**marketplace.json:**
- Contains marketplace metadata
- Lists available plugins
- `"source": "./"` (must start with `"./"`)
- `"strict": true` (tells Claude Code to read plugin.json)
- NO `mcpServers`, `hooks`, or `requirements` here

**plugin.json:**
- Contains actual plugin configuration
- `mcpServers`: Docker exec command for MCP server
- `hooks.postInstall`: Points to `scripts/plugin-install.sh`
- `requirements.docker`: Requires Docker Desktop

---

## What the Plugin Does

When a user installs the plugin:

1. **Marketplace Registration:** `/plugin marketplace add` registers the GitHub repo
2. **Plugin Installation:** `/plugin install` triggers:
   - Downloads plugin files from GitHub
   - Runs `scripts/plugin-install.sh` (postInstall hook)
   - Script does:
     - Checks Docker is running
     - Downloads `qdrant-snapshot.tar.gz` (76MB) from v1.0.0 release
     - Runs `docker-compose build` and `docker-compose up -d`
     - Imports snapshot into Qdrant
     - Verifies 21,747+ documents indexed
   - Configures MCP server to run via Docker exec

---

## Version History (Learning from Mistakes)

| Version | Status | Issue/Fix |
|---------|--------|-------|
| **v1.1.6** | ✅ **Current** | Fixed hook schema: "PostInstall" (capitalized), simple path format, cross-platform support |
| v1.1.5 | ❌ Broken | Hook schema error: "postInstall" lowercase, object format instead of string |
| v1.1.4 | ❌ Broken | Schema errors: hooks in marketplace.json, source "." |
| v1.1.3 | ❌ Broken | SSH authentication error (shorthand format) |
| v1.1.2 | ❌ Broken | HTTPS URL but wrong file structure |
| v1.1.1 | ❌ Broken | Fixed marketplace structure, wrong URL |
| v1.1.0 | ❌ Broken | Incorrect marketplace.json structure |
| v1.0.0 | ✅ Working | Original MCP server (manual install) |

---

## Lessons Learned

### 1. Marketplace URL Format
- **Use:** `https://github.com/owner/repo.git` (HTTPS URL)
- **NOT:** `owner/repo` (requires SSH keys - breaks for most users)

### 2. File Structure
- **marketplace.json:** Marketplace metadata ONLY
- **plugin.json:** Plugin configuration with mcpServers, hooks, requirements
- **Two files are required** when using `strict: true`

### 3. Schema Requirements
- `source` must be `"./"` not `"."`
- `hooks` cannot be in marketplace.json
- `hooks` keys must be capitalized: `"PostInstall"` not `"postInstall"`
- `hooks` values must be simple string paths, NOT objects with `command`/`args`
- `strict: true` tells Claude Code to look for plugin.json

---

## Testing Status

### What User Has Tested (On Clean Windows Machine)
- ❌ **v1.1.3:** SSH authentication failed (shorthand format)
- ❌ **v1.1.4:** Schema validation errors (hooks in marketplace.json, source ".")
- ❌ **v1.1.5:** Hook schema error ("postInstall" lowercase, object format invalid)

### What Needs Testing (v1.1.6)
1. ✅ Add marketplace: `/plugin marketplace add https://github.com/peterparker57/clarion-knowledge-base.git`
2. ⏳ Install plugin on clean Windows machine: `/plugin install clarion-knowledge-base`
3. ⏳ Verify MCP server loads correctly after installation
4. ⏳ Test on Mac/Linux (if possible)
5. ⏳ **DO NOT INSTALL ON DEV MACHINE** (will conflict with existing Docker setup)

### Recommended Testing Approach
User should test marketplace registration (steps 1-3 above) on their dev machine to verify the schema is valid. Full installation should be tested on a clean machine or by an end user.

---

## Important Files

### Plugin Configuration
- `.claude-plugin/marketplace.json` - Marketplace metadata
- `.claude-plugin/plugin.json` - Plugin configuration
- `scripts/plugin-install.sh` - Installation automation script

### Documentation (For End Users)
- `README.md` - Main documentation (installation at top)
- `PLUGIN.md` - Plugin-specific guide (643 lines)
- `INSTALLATION.md` - Detailed installation instructions
- `PLUGIN_CONVERSION_PLAN.md` - Developer reference

### Slash Commands (Optional Features)
- `.claude/commands/clarion-search.md` - Search documentation
- `.claude/commands/clarion-setup.md` - Re-run setup
- `.claude/commands/clarion-status.md` - Check container status

---

## GitHub Credentials

**Username:** peterparker57
**Token:** [User will provide if needed]
**Repository:** clarion-knowledge-base (PUBLIC)

---

## Docker Setup

**Existing Containers (Don't Break These):**
- `clarion-qdrant` - Qdrant vector database
- `clarion-mcp-server` - Python MCP server

**Files:**
- `docker-compose.yml` - Container orchestration
- `Dockerfile` - MCP server image
- `qdrant-snapshot.tar.gz` - 76MB snapshot (21,747 vectors)

**MCP Server Command:**
```bash
docker exec -i clarion-mcp-server python /app/src/mcp_server.py
```

---

## Next Steps

### If Marketplace Registration Works (v1.1.5)
1. ✅ Celebrate - the plugin structure is correct!
2. Have an end user test full installation on a clean machine
3. If successful, announce to Clarion community
4. Consider submitting to community plugin marketplaces

### If Marketplace Registration Fails
1. Read the error message carefully
2. Check Claude Code docs: https://docs.claude.com/en/docs/claude-code/plugin-marketplaces
3. Validate JSON files:
   - `.claude-plugin/marketplace.json`
   - `.claude-plugin/plugin.json`
4. Look at working examples in Anthropic's official plugins

### Future Enhancements (See FUTURE_ROADMAP.md)
- Auto-update mechanism
- Health check endpoints
- Usage analytics
- Additional documentation sources

---

## Common Issues & Solutions

### "SSH authentication failed"
- **Cause:** Using shorthand `owner/repo` format
- **Fix:** Use HTTPS URL: `https://github.com/peterparker57/clarion-knowledge-base.git`

### "Invalid schema: plugins.0.hooks: Invalid input"
- **Cause:** hooks in marketplace.json instead of plugin.json
- **Fix:** v1.1.5 fixed this - hooks are now in plugin.json

### "source: Invalid input: must start with './'"
- **Cause:** `source` was `"."` instead of `"./"`
- **Fix:** v1.1.5 fixed this - source is now `"./"`

### "hooks: Invalid input" (v1.1.5 error)
- **Cause:** Hook key was lowercase `postInstall` instead of `PostInstall`, and value was object instead of string
- **Fix:** v1.1.6 fixed this - uses `"PostInstall"` with simple path string

### "Docker is not running"
- **Cause:** User doesn't have Docker Desktop running
- **Fix:** Start Docker Desktop before plugin installation

---

## Documentation References

- **Claude Code Docs:** https://docs.claude.com/en/docs/claude-code/plugin-marketplaces
- **Plugin Structure:** Two files - marketplace.json + plugin.json
- **MCP Protocol:** https://modelcontextprotocol.io

---

## Key Takeaways for Next Session

1. **v1.1.6 should work** - fixed hook schema validation and added cross-platform support
2. **Hook schema is finicky** - must use capitalized `PostInstall` with simple string path
3. **Test on clean Windows machine** - the real test environment for end users
4. **Cross-platform is critical** - Node.js wrapper ensures Windows/Mac/Linux compatibility
5. **Don't install on dev machine** - will conflict with existing Docker setup
6. **HTTPS URL is correct** - don't second-guess this again
7. **Two-file structure is required** - marketplace.json + plugin.json with strict: true

---

## Quick Reference

**Add Marketplace:**
```bash
/plugin marketplace add https://github.com/peterparker57/clarion-knowledge-base.git
```

**List Marketplaces:**
```bash
/plugin marketplace list
```

**List Plugins:**
```bash
/plugin list
```

**Install Plugin (end users only):**
```bash
/plugin install clarion-knowledge-base
```

---

**End of Handoff Document**
