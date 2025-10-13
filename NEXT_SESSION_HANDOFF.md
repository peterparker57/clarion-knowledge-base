# Session Handoff - Clarion Knowledge Base Plugin

**Date:** October 13, 2025
**Current Version:** v1.1.9
**Status:** WORKING - Fixed commands schema (array format)

---

## Current Status

The Clarion Knowledge Base MCP server has been successfully converted to a Claude Code plugin. Version v1.1.9 fixes the commands schema validation error.

### Latest Release
- **Version:** v1.1.9
- **Release URL:** https://github.com/peterparker57/clarion-knowledge-base/releases/tag/v1.1.9
- **Repository:** https://github.com/peterparker57/clarion-knowledge-base (PUBLIC)
- **Status:** ✅ WORKING - Commands schema fixed (array format), ready for testing

---

## What's New in v1.1.9

### Commands Schema Fixed!

**Problem in v1.1.8:**
- Used object format for commands (WRONG)
- Caused validation error: "commands: Invalid input"

**Wrong format (v1.1.8):**
```json
"commands": {
  "clarion-setup": "./.claude/commands/clarion-setup.md"
}
```

**Fixed in v1.1.9:**
Commands must be an **array of string paths**, not an object:
```json
"commands": [
  "./.claude/commands/clarion-setup.md",
  "./.claude/commands/clarion-search.md",
  "./.claude/commands/clarion-status.md"
]
```

According to the documentation, `commands` can be:
- A single string path, OR
- An array of string paths

NOT an object with key-value pairs!

---

## What's New in v1.1.8

### Slash Commands Registration (Wrong Format)

**Problem in v1.1.7:**
- Plugin loaded correctly (no validation errors)
- But `/clarion-setup` gave "unknown slash command" error
- Command files existed but weren't registered

**Attempted Fix in v1.1.8:**
Added `commands` section but used wrong format (object instead of array)

---

## What's New in v1.1.7

### Critical Discovery: PostInstall Hooks Don't Exist!

After extensive testing and documentation research, we discovered that **Claude Code plugins do NOT support PostInstall hooks**.

**Supported hook types only:**
- UserPromptSubmit
- PreToolUse
- PostToolUse
- Stop
- SubagentStop
- Notification

`PostInstall` is NOT a valid hook type, which is why validation kept failing!

### The Fix: Manual Setup via Slash Command

**v1.1.7 Changes:**
- ✅ Removed `hooks` section entirely from plugin.json (not supported)
- ✅ Updated `/clarion-setup` command description for first-time installation
- ✅ Updated README with 3-step install process

**New Installation Flow:**
```bash
# Step 1: Add marketplace
/plugin marketplace add https://github.com/peterparker57/clarion-knowledge-base.git

# Step 2: Install plugin
/plugin install clarion-knowledge-base

# Step 3: Run setup (manually)
/clarion-setup
```

**Why this works:**
- No schema validation errors (hooks removed)
- User has control over when Docker downloads happen
- More transparent installation process
- Slash command already existed, just updated docs

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
| **v1.1.9** | ✅ **Current** | WORKING! Fixed commands schema - array format not object |
| v1.1.8 | ❌ Broken | Commands validation error - used object format instead of array |
| v1.1.7 | ⚠️ Partial | Plugin loads, but slash commands not registered in plugin.json |
| v1.1.6 | ❌ Broken | PostInstall hook doesn't exist in Claude Code (only PreToolUse, PostToolUse, etc.) |
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
- **PostInstall hooks DO NOT EXIST** - Claude Code only supports: UserPromptSubmit, PreToolUse, PostToolUse, Stop, SubagentStop, Notification
- **`commands` must be array or string** - NOT an object with key-value pairs
- Don't use hooks for installation - use slash commands instead
- `strict: true` tells Claude Code to look for plugin.json

---

## Testing Status

### What User Has Tested (On Clean Windows Machine)
- ❌ **v1.1.3:** SSH authentication failed (shorthand format)
- ❌ **v1.1.4:** Schema validation errors (hooks in marketplace.json, source ".")
- ❌ **v1.1.5:** Hook schema error ("postInstall" lowercase, object format invalid)
- ❌ **v1.1.6:** PostInstall hook doesn't exist (Claude Code doesn't support it)
- ✅ **v1.1.7:** Plugin loaded without validation errors! (But slash commands not working)
- ❌ **v1.1.8:** Commands validation error (object format instead of array)

### What Needs Testing (v1.1.9)
1. ⏳ Update marketplace: `/plugin marketplace update clarion-knowledge-base-marketplace`
2. ⏳ Install plugin: `/plugin install clarion-knowledge-base` (should work without errors!)
3. ⏳ Verify slash commands work: `/clarion-setup` (should not say "unknown command")
4. ⏳ Run Docker setup (downloads 76MB, builds containers)
5. ⏳ Restart Claude Code
6. ⏳ Test MCP tool: Ask "How do I create a browse procedure in Clarion?"
7. ⏳ Test other slash commands: `/clarion-status`, `/clarion-search browse`
8. ⏳ Test on Mac/Linux (if possible)
9. ⏳ **DO NOT INSTALL ON DEV MACHINE** (will conflict with existing Docker setup)

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

### "hooks: Invalid input" (v1.1.5-v1.1.6 error)
- **Cause:** PostInstall hooks don't exist in Claude Code! Only these hooks are supported: UserPromptSubmit, PreToolUse, PostToolUse, Stop, SubagentStop, Notification
- **Fix:** v1.1.7 removed hooks entirely - users run `/clarion-setup` manually after installation

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

1. **v1.1.7 SHOULD FINALLY WORK** - PostInstall hooks don't exist, removed them entirely
2. **PostInstall is NOT a valid hook type** - Only: UserPromptSubmit, PreToolUse, PostToolUse, Stop, SubagentStop, Notification
3. **Manual setup is the solution** - Users run `/clarion-setup` after installing plugin
4. **Test on clean Windows machine** - the real test environment for end users
5. **Don't install on dev machine** - will conflict with existing Docker setup
6. **HTTPS URL is correct** - don't second-guess this again
7. **Two-file structure is required** - marketplace.json + plugin.json with strict: true
8. **Installation scripts are still useful** - `/clarion-setup` runs the appropriate script for each platform

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
