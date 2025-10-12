# Quick Start Guide

Get up and running with the Clarion Knowledge Base MCP Server in 3 simple steps!

## Prerequisites

- ✅ Docker Desktop installed and running
- ✅ Claude Code or Claude Desktop installed
- ✅ Internet connection for downloading (~600MB)

## Installation (3 Steps)

### Linux / macOS

```bash
# Step 1: Clone the repository
git clone https://github.com/peterparker57/clarion-knowledge-base
cd clarion-knowledge-base

# Step 2: Run the installer
./install.sh

# Step 3: Restart Claude
# That's it! The installer handles everything automatically.
```

### Windows

```batch
# Step 1: Clone the repository
git clone https://github.com/peterparker57/clarion-knowledge-base
cd clarion-knowledge-base

# Step 2: Run the installer
install.bat

# Step 3: Restart Claude
# That's it! The installer handles everything automatically.
```

## What Gets Installed

The installer will:
- ✅ Download the pre-built vector database (~600MB)
- ✅ Start Docker containers (Qdrant + MCP Server)
- ✅ Import 21,747 documentation vectors from 21 Clarion PDFs
- ✅ Configure Claude Code and/or Claude Desktop
- ✅ Verify the installation

Total time: **5-10 minutes** (depending on download speed)

## Verify Installation

After restarting Claude:

1. Look for **"clarion-knowledge-base"** in the MCP servers list
2. Ask Claude: **"Search the Clarion documentation for QUEUE"**
3. You should get relevant results from the Clarion documentation!

## Test Your Installation

Run the test script to verify everything is working:

**Linux/macOS:**
```bash
./scripts/test_installation.sh
```

**Windows:**
```batch
scripts\test_installation.bat
```

## Usage Examples

Try these queries in Claude:

- "Search for information about QUEUE structures"
- "Find examples of FILE declarations"
- "Look up SQL connection syntax in Clarion"
- "Show me how to use THREAD in Clarion"
- "Find documentation about WINDOW controls"

## Managing Containers

### View Status
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
docker-compose logs -f
```

## Troubleshooting

### MCP Server Not Showing in Claude?

1. **Restart Claude completely** (quit and relaunch)
2. Check containers are running: `docker ps`
3. Review config file:
   - Claude Code: `~/.claude.json` (Linux/Mac) or `%USERPROFILE%\.claude.json` (Windows)
   - Claude Desktop: See [INSTALLATION.md](INSTALLATION.md) for paths

### Import Failed?

1. Check Qdrant is running: `docker ps | grep clarion-qdrant`
2. Test Qdrant health: `curl http://localhost:6333/health`
3. Re-run import: `docker exec clarion-mcp-server python /app/scripts/import_snapshot.py`

### Docker Issues?

1. Ensure Docker Desktop is running
2. Restart Docker Desktop
3. Try: `docker-compose down && docker-compose up -d`

## Need More Help?

- 📖 Full documentation: [INSTALLATION.md](INSTALLATION.md)
- 🐛 Report issues: [GitHub Issues](https://github.com/peterparker57/clarion-knowledge-base/issues)
- 💡 Advanced configuration: See [INSTALLATION.md](INSTALLATION.md#advanced-configuration)

## Uninstall

```bash
# Stop and remove containers
docker-compose down -v

# Remove config from Claude (edit JSON files)
# - Claude Code: ~/.claude.json
# - Claude Desktop: See INSTALLATION.md for paths

# Delete repository
cd ..
rm -rf clarion-knowledge-base
```

---

**That's it!** You now have instant access to 21 Clarion documentation manuals through Claude. Happy coding! 🚀
