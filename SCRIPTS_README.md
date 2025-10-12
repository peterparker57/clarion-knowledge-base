# Installation Scripts Documentation

This document describes all the installation scripts and utilities created for the Clarion Knowledge Base MCP Server project.

## Overview

The installation system provides automated, cross-platform setup for both Linux/Mac and Windows users. The scripts handle everything from downloading the vector database to configuring Claude clients.

## Files Created

### Main Installation Scripts

#### 1. `install.sh` (Linux/macOS)
- **Size:** 17KB
- **Language:** Bash
- **Features:**
  - Interactive installation wizard
  - Color-coded output for better UX
  - Prerequisite checking (Docker, curl, jq/Python)
  - Automatic snapshot download with progress bar
  - Docker container management
  - Qdrant health monitoring
  - Snapshot import automation
  - Automatic Claude config detection and update
  - Config file backup before modification
  - Connection testing
  - Comprehensive error handling
  - Idempotent (safe to run multiple times)

**Usage:**
```bash
chmod +x install.sh
./install.sh
```

#### 2. `install.bat` (Windows)
- **Size:** 15KB
- **Language:** Batch/PowerShell hybrid
- **Features:**
  - Same features as install.sh
  - UTF-8 support for proper character display
  - PowerShell integration for downloads
  - Windows path handling
  - Colored console output
  - Error level checking
  - Delayed expansion for variable handling

**Usage:**
```batch
install.bat
```

### Configuration Utilities

#### 3. `scripts/update_claude_config.py`
- **Size:** 2.4KB
- **Language:** Python 3
- **Purpose:** Standalone utility for updating Claude JSON config files
- **Features:**
  - Creates config directories if missing
  - Preserves existing configuration
  - Validates JSON syntax
  - Handles encoding properly (UTF-8)
  - Can be used independently of main installers

**Usage:**
```bash
python scripts/update_claude_config.py ~/.claude.json
```

### Testing Scripts

#### 4. `scripts/test_installation.sh` (Linux/macOS)
- **Size:** 7.4KB
- **Language:** Bash
- **Purpose:** Comprehensive installation verification
- **Tests Performed:**
  - Docker daemon status
  - Container running status
  - Qdrant health check
  - Collection existence and point count
  - MCP server Python environment
  - Required dependencies (qdrant_client, sentence_transformers, mcp)
  - Container networking
  - Claude Code configuration
  - Claude Desktop configuration
  - Snapshot file presence

**Usage:**
```bash
./scripts/test_installation.sh
```

#### 5. `scripts/test_installation.bat` (Windows)
- **Size:** 7.4KB
- **Language:** Batch
- **Purpose:** Same as test_installation.sh for Windows
- **Features:** Same tests as Linux version, adapted for Windows

**Usage:**
```batch
scripts\test_installation.bat
```

### Documentation

#### 6. `INSTALLATION.md`
- **Size:** ~20KB
- **Content:**
  - Detailed installation instructions
  - Manual installation steps
  - Configuration paths for all platforms
  - Comprehensive troubleshooting guide
  - Docker container management
  - Update procedures
  - Uninstallation instructions
  - Advanced configuration options
  - System requirements
  - Platform support matrix

#### 7. `QUICK_START.md`
- **Size:** ~3KB
- **Content:**
  - 3-step installation guide
  - Quick verification steps
  - Common usage examples
  - Basic troubleshooting
  - Quick reference commands

## Installation Flow

### User Experience

```
1. User runs install.sh or install.bat
   ↓
2. Interactive prompt: "Claude Code, Desktop, or Both?"
   ↓
3. Prerequisites check (Docker, tools)
   ↓
4. Download snapshot (~600MB) with progress
   ↓
5. Start Docker containers (Qdrant + MCP Server)
   ↓
6. Wait for Qdrant to be healthy (with progress dots)
   ↓
7. Copy snapshot to container
   ↓
8. Import snapshot into Qdrant
   ↓
9. Update Claude config files (with backup)
   ↓
10. Test MCP server connection
   ↓
11. Display success message and next steps
```

### Technical Flow

```
Prerequisites Check
├── Docker installed?
├── Docker daemon running?
├── docker-compose available?
├── curl/PowerShell available?
└── Python available?

Download Phase
├── Check if snapshot exists
├── Prompt to re-download if exists
├── Download with progress indicator
└── Verify file size

Docker Phase
├── Check if containers running
├── Prompt to restart if running
├── Start docker-compose services
├── Wait for Qdrant health check
└── Verify both containers are up

Import Phase
├── Check if collection exists
├── Prompt to re-import if exists
├── Copy snapshot to container
├── Run import script in container
├── Wait for completion
└── Verify collection has points

Configuration Phase
├── Detect Claude installation paths
├── Backup existing config files
├── Update JSON with MCP config
├── Preserve existing settings
└── Verify JSON is valid

Verification Phase
├── Test Python in container
├── Test MCP server import
└── Display final instructions
```

## Key Features

### Idempotency
All scripts are designed to be run multiple times safely:
- Checks before overwriting files
- Prompts before destructive operations
- Skips steps already completed
- Backs up configs before modification

### Error Handling
- Clear error messages with context
- Helpful suggestions for fixes
- Graceful failure with cleanup
- Exit codes for scripting

### User Experience
- Color-coded output (success/error/warning/info)
- Progress indicators for long operations
- Interactive prompts with validation
- Clear next steps after completion
- Backup notifications

### Cross-Platform Support
- Linux (Ubuntu, Debian, etc.)
- macOS (11+)
- Windows (10/11)
- Automatic OS detection
- Platform-specific paths
- Appropriate tools for each platform

## Configuration Paths

### Claude Code
```
Linux/macOS:  ~/.claude.json
Windows:      %USERPROFILE%\.claude.json
```

### Claude Desktop
```
macOS:   ~/Library/Application Support/Claude/claude_desktop_config.json
Linux:   ~/.config/Claude/claude_desktop_config.json
Windows: %APPDATA%\Claude\claude_desktop_config.json
```

## MCP Server Configuration

Both scripts inject this configuration:

```json
{
  "mcpServers": {
    "clarion-knowledge-base": {
      "command": "docker",
      "args": ["exec", "-i", "clarion-mcp-server", "python", "/app/src/mcp_server.py"]
    }
  }
}
```

## Testing

### Automated Tests
Run test scripts to verify:
- All components installed correctly
- Docker containers running
- Qdrant responding
- Collection populated
- MCP server functional
- Dependencies installed
- Configuration files updated

### Manual Testing
After installation:
1. Restart Claude
2. Check for "clarion-knowledge-base" in MCP list
3. Try query: "Search Clarion docs for QUEUE"
4. Verify relevant results returned

## Troubleshooting

### Common Issues

**Docker not running:**
```bash
# Solution: Start Docker Desktop
```

**Port conflicts:**
```bash
# Solution: Stop conflicting services or change ports in docker-compose.yml
```

**Download fails:**
```bash
# Solution: Download manually and place in project directory
```

**Import fails:**
```bash
# Solution: Check Qdrant health, restart containers, try manual import
```

**Config not updated:**
```bash
# Solution: Use update_claude_config.py manually or check JSON syntax
```

## Development Notes

### Design Decisions

1. **Dual Config Methods:** Scripts support both jq and Python for JSON manipulation to ensure compatibility.

2. **Progress Feedback:** Long operations show progress to prevent user confusion.

3. **Backup Strategy:** Always backup before modifying configs to prevent data loss.

4. **Container Names:** Hardcoded as defined in docker-compose.yml:
   - `clarion-qdrant` for Qdrant service
   - `clarion-mcp-server` for MCP server

5. **Snapshot URL:** Placeholder URL, update when creating GitHub release:
   ```
   https://github.com/peterparker57/clarion-knowledge-base/releases/download/v1.0.0/qdrant-snapshot.tar.gz
   ```

### Testing Status

**Linux/macOS (install.sh):**
- ✅ Syntax validated
- ✅ Made executable
- ⏳ Full installation test pending

**Windows (install.bat):**
- ✅ Syntax validated
- ✅ File created
- ⏳ Full installation test pending

**Utilities:**
- ✅ update_claude_config.py - Syntax validated
- ✅ test_installation.sh - Syntax validated
- ✅ test_installation.bat - Syntax validated

### Future Enhancements

Potential improvements:
1. Add checksum verification for downloaded snapshot
2. Implement retry logic for failed downloads
3. Add option to skip snapshot download for users with existing file
4. Create Docker image on Docker Hub to avoid building locally
5. Add support for custom Qdrant installations
6. Implement logging to file for troubleshooting
7. Add option for silent/unattended installation
8. Create web-based installer status page

## Security Considerations

1. **No Credentials:** Scripts don't handle passwords or tokens
2. **HTTPS Downloads:** Snapshot downloaded over HTTPS
3. **Config Backup:** Existing configs backed up before modification
4. **Read-Only Mounts:** Docker volumes mounted read-only where possible
5. **No Sudo Required:** Installation doesn't require elevated privileges (except Docker itself)

## Maintenance

### Updating for New Versions

When releasing new versions:

1. Update snapshot URL in both install.sh and install.bat
2. Update version numbers in documentation
3. Test on all supported platforms
4. Update changelog
5. Create GitHub release with new snapshot

### Adding New Platforms

To support new platforms:

1. Detect platform in install scripts
2. Add platform-specific config paths
3. Test thoroughly
4. Update documentation
5. Add to platform support matrix

## Support

For issues with installation scripts:
1. Run test script for diagnostics
2. Check INSTALLATION.md troubleshooting section
3. Review Docker logs
4. Open GitHub issue with test script output

---

**Created:** October 12, 2025
**Version:** 1.0.0
**Maintainer:** peterparker57
**License:** See project LICENSE file
