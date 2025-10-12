# Installation Guide

This guide provides detailed instructions for installing the Clarion Knowledge Base MCP Server on your system.

## Quick Start

### Prerequisites

Before running the installation script, ensure you have:

1. **Docker Desktop** installed and running
   - Windows: [Download Docker Desktop](https://www.docker.com/products/docker-desktop)
   - Mac: [Download Docker Desktop](https://www.docker.com/products/docker-desktop)
   - Linux: Install Docker Engine and Docker Compose

2. **Python 3.x** (for config file updates)
   - Usually pre-installed on Mac/Linux
   - Windows: [Download Python](https://www.python.org/downloads/)

3. **Claude Code** or **Claude Desktop** installed
   - Get Claude Code: [Anthropic Claude Code](https://claude.ai/code)
   - Get Claude Desktop: [Anthropic Claude Desktop](https://claude.ai/download)

### Installation Steps

#### Linux & macOS

```bash
# 1. Clone the repository
git clone https://github.com/peterparker57/clarion-knowledge-base
cd clarion-knowledge-base

# 2. Run the installer
chmod +x install.sh  # Make it executable (if needed)
./install.sh

# 3. Follow the interactive prompts
# - Choose Claude Code, Desktop, or Both
# - Script will handle everything automatically

# 4. Restart Claude
# - Claude Code: Restart your terminal/IDE
# - Claude Desktop: Quit and restart the app
```

#### Windows

```batch
# 1. Clone the repository
git clone https://github.com/peterparker57/clarion-knowledge-base
cd clarion-knowledge-base

# 2. Run the installer
install.bat

# 3. Follow the interactive prompts
# - Choose Claude Code, Desktop, or Both
# - Script will handle everything automatically

# 4. Restart Claude
# - Claude Code: Restart your terminal/IDE
# - Claude Desktop: Quit and restart the app
```

## What the Installer Does

The installation script performs the following steps automatically:

1. **Prerequisites Check**
   - Verifies Docker is installed and running
   - Checks for required tools (curl/wget, Python)

2. **Download Snapshot**
   - Downloads the pre-built Qdrant vector database (~600MB)
   - Contains 21,747 vectors from 21 Clarion PDFs

3. **Start Docker Containers**
   - Launches Qdrant vector database service
   - Launches MCP server service
   - Waits for services to be healthy

4. **Import Vector Database**
   - Extracts the snapshot
   - Imports it into Qdrant
   - Verifies successful import

5. **Configure Claude**
   - Detects your Claude installation(s)
   - Creates backup of existing config
   - Updates config with MCP server settings

6. **Verify Installation**
   - Tests MCP server connectivity
   - Provides next steps and usage instructions

## Configuration Paths

The installer will automatically detect and update these configuration files:

### Claude Code

- **Linux/macOS**: `~/.claude.json`
- **Windows**: `%USERPROFILE%\.claude.json`

### Claude Desktop

- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

## MCP Server Configuration

The installer adds this configuration to your Claude config file:

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

## Manual Installation

If you prefer to install manually or encounter issues with the automated installer:

### 1. Download Snapshot

```bash
# Download from GitHub Release
curl -L -o qdrant-snapshot.tar.gz \
  https://github.com/peterparker57/clarion-knowledge-base/releases/download/v1.0.0/qdrant-snapshot.tar.gz
```

### 2. Start Docker Services

```bash
docker-compose up -d
```

### 3. Import Snapshot

```bash
# Copy to container
docker cp qdrant-snapshot.tar.gz clarion-mcp-server:/app/

# Run import script
docker exec clarion-mcp-server python /app/scripts/import_snapshot.py /app/qdrant-snapshot.tar.gz
```

### 4. Update Claude Config

Use the helper script:

```bash
# For Claude Code
python scripts/update_claude_config.py ~/.claude.json

# For Claude Desktop (macOS)
python scripts/update_claude_config.py ~/Library/Application\ Support/Claude/claude_desktop_config.json

# For Claude Desktop (Windows)
python scripts/update_claude_config.py %APPDATA%\Claude\claude_desktop_config.json
```

Or manually edit the JSON files and add the MCP server configuration shown above.

## Troubleshooting

### Docker Issues

**Problem**: "Docker daemon is not running"

**Solution**: Start Docker Desktop and wait for it to fully initialize.

---

**Problem**: "Failed to start Docker containers"

**Solutions**:
- Check if ports 6333 and 6334 are available
- Try: `docker-compose down` then `docker-compose up -d`
- Check Docker logs: `docker-compose logs`

---

### Download Issues

**Problem**: "Failed to download snapshot"

**Solutions**:
- Check your internet connection
- Try downloading manually from GitHub Releases
- Place `qdrant-snapshot.tar.gz` in the installation directory
- Re-run the installer (it will skip download if file exists)

---

### Import Issues

**Problem**: "Failed to import snapshot"

**Solutions**:
- Verify Qdrant is running: `docker ps | grep clarion-qdrant`
- Check Qdrant health: `curl http://localhost:6333/health`
- View logs: `docker logs clarion-qdrant`
- Try re-importing: Run the import script manually

---

### Configuration Issues

**Problem**: "MCP server not showing in Claude"

**Solutions**:
1. Verify config file was updated correctly
2. Check the JSON syntax is valid
3. Restart Claude completely (quit and relaunch)
4. Check container is running: `docker ps`
5. View MCP logs in Claude's developer console

---

**Problem**: "Permission denied" errors

**Solution** (Linux/macOS):
```bash
chmod +x install.sh
chmod +x scripts/*.py
```

---

### MCP Server Issues

**Problem**: "MCP server connection failed"

**Solutions**:
- Verify containers are running: `docker ps`
- Test Docker exec: `docker exec clarion-mcp-server python --version`
- Check MCP server logs: `docker logs clarion-mcp-server`
- Restart containers: `docker-compose restart`

---

## Managing Docker Containers

### View Running Containers
```bash
docker ps
```

### Stop Containers
```bash
docker-compose down
```

### Start Containers
```bash
docker-compose up -d
```

### View Logs
```bash
# All services
docker-compose logs -f

# Specific service
docker logs clarion-qdrant
docker logs clarion-mcp-server
```

### Restart Containers
```bash
docker-compose restart
```

### Remove Everything (clean reinstall)
```bash
docker-compose down -v  # WARNING: Removes volumes (vector database)
```

## Updating

To update to a new version:

```bash
# 1. Stop containers
docker-compose down

# 2. Pull latest changes
git pull

# 3. Rebuild containers (if needed)
docker-compose build

# 4. Start containers
docker-compose up -d

# 5. Re-import snapshot (if provided in update)
# Follow import instructions
```

## Uninstalling

To completely remove the Clarion Knowledge Base:

```bash
# 1. Stop and remove containers
docker-compose down -v

# 2. Remove config from Claude Code
# Edit ~/.claude.json and remove "clarion-knowledge-base" entry

# 3. Remove config from Claude Desktop
# Edit config file (see paths above) and remove "clarion-knowledge-base" entry

# 4. Delete repository directory
cd ..
rm -rf clarion-knowledge-base

# 5. Restart Claude
```

## Advanced Configuration

### Custom Qdrant Port

If you need to use different ports, edit `docker-compose.yml`:

```yaml
services:
  qdrant:
    ports:
      - "6333:6333"  # Change first number (host port)
      - "6334:6334"
```

Then update the `QDRANT_PORT` environment variable in the MCP server service.

### Using Local Qdrant

If you already have Qdrant running locally:

1. Don't start the Qdrant container: Comment out the qdrant service in `docker-compose.yml`
2. Update `QDRANT_HOST` in MCP server environment to your Qdrant host
3. Import the snapshot to your existing Qdrant instance

### Development Mode

To mount local source code for development:

```yaml
# In docker-compose.yml, uncomment:
volumes:
  - ./src:/app/src:ro
  - ./data/processed:/app/data/processed:ro
```

## Getting Help

If you encounter issues:

1. Check this troubleshooting guide
2. Review Docker logs: `docker-compose logs`
3. Check GitHub Issues: [Project Issues](https://github.com/peterparker57/clarion-knowledge-base/issues)
4. Join Clarion community forums
5. Contact the maintainer

## System Requirements

### Minimum
- 4 GB RAM
- 2 GB free disk space
- Docker Desktop 20.x or later
- Python 3.7+

### Recommended
- 8 GB RAM
- 5 GB free disk space
- SSD storage
- Modern CPU (4+ cores)

## Platform Support

✅ **Fully Supported**
- Windows 10/11 with Docker Desktop
- macOS 11+ with Docker Desktop
- Ubuntu 20.04+ with Docker Engine
- Debian 10+ with Docker Engine

⚠️ **May Work** (community tested)
- Other Linux distributions
- Windows with WSL2

❌ **Not Supported**
- Windows without Docker Desktop or WSL2
- macOS < 11
- ARM architecture (not tested)
