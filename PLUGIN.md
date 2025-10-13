# Claude Code Plugin Guide

This document explains how to install and use the Clarion Knowledge Base as a Claude Code plugin.

## What is a Claude Code Plugin?

Claude Code plugins are pre-packaged MCP (Model Context Protocol) servers that can be installed with a single command. They extend Claude's capabilities by providing specialized tools and knowledge bases.

The Clarion Knowledge Base plugin gives Claude instant access to 21,747 indexed documentation chunks from 21 Clarion PDF manuals, enabling semantic search and natural language queries about Clarion programming.

## Quick Installation

```bash
/plugin add peterparker57/clarion-knowledge-base
```

That's all you need! The plugin system handles everything automatically.

### Prerequisites

Before installing the plugin, ensure you have:

1. **Docker Desktop** installed and running
   - Windows: [Download Docker Desktop](https://www.docker.com/products/docker-desktop)
   - macOS: [Download Docker Desktop](https://www.docker.com/products/docker-desktop)
   - Linux: Docker Engine + Docker Compose

2. **Claude Code** installed and running
   - Get it at [claude.ai/code](https://claude.ai/code)

3. **Sufficient Resources**
   - 2GB free disk space (for vector database)
   - 4GB RAM minimum (8GB recommended)
   - Active internet connection (for initial download)

## How This Plugin Works

### Architecture Overview

The plugin uses a Docker-based architecture:

```
┌─────────────────────────────────────────┐
│         Claude Code (You)               │
│  Ask: "How do I create a browse?"       │
└──────────────┬──────────────────────────┘
               │ MCP Protocol
               ▼
┌─────────────────────────────────────────┐
│   Docker Container: clarion-mcp-server  │
│   - Python MCP server                   │
│   - Generates embeddings                │
│   - Searches vector database            │
└──────────────┬──────────────────────────┘
               │ gRPC
               ▼
┌─────────────────────────────────────────┐
│   Docker Container: clarion-qdrant      │
│   - Qdrant vector database              │
│   - 21,747 documentation chunks         │
│   - Semantic search engine              │
└─────────────────────────────────────────┘
```

### Key Components

1. **Qdrant Vector Database**
   - Stores documentation as 768-dimensional embeddings
   - Enables semantic search (understands intent, not just keywords)
   - Persistent storage via Docker volume (655 MB)
   - Runs on ports 6333 (REST) and 6334 (gRPC)

2. **MCP Server**
   - Bridges Claude and the vector database
   - Converts queries to embeddings
   - Formats results with citations
   - Runs on-demand via `docker exec`

3. **Docker Orchestration**
   - Manages both services
   - Handles networking
   - Provides automatic restarts
   - Isolates dependencies

## What Happens During Installation

When you run `/plugin add peterparker57/clarion-knowledge-base`, the plugin system:

### Step 1: Download Plugin Files
- Clones the repository to your plugins directory
- Typically: `~/.claude/plugins/clarion-knowledge-base`
- Downloads plugin metadata and configuration

### Step 2: Check Prerequisites
- Verifies Docker is installed and running
- Checks available disk space
- Validates system requirements

### Step 3: Download Vector Database
- Downloads pre-built Qdrant snapshot (~76 MB compressed)
- Extracts to Docker volume (~655 MB uncompressed)
- Contains 21,747 indexed documentation chunks

### Step 4: Start Docker Containers
- Launches `clarion-qdrant` (vector database)
- Launches `clarion-mcp-server` (MCP server)
- Waits for health checks to pass
- Configures networking between containers

### Step 5: Configure Claude Code
- Updates `claude_code_config.json` automatically
- Adds MCP server configuration
- Registers available tools:
  - `search_docs` - Semantic documentation search

### Step 6: Verify Installation
- Tests MCP server connectivity
- Performs sample query
- Confirms vector database is loaded
- Reports status and next steps

### Step 7: Register Slash Commands
- Installs custom slash commands:
  - `/clarion-search` - Search documentation
  - `/clarion-status` - Check container status
  - `/clarion-setup` - Restart containers

**Total installation time:** Typically 30-60 seconds (depending on download speed)

## Using the Plugin

### Natural Language Queries

Simply ask Claude questions about Clarion:

```
"How do I create a browse in Clarion?"
"What's the syntax for a QUEUE?"
"Explain the ABC library FileManager class"
"How do I connect to a SQL database?"
```

Claude will automatically use the `search_docs` tool to find relevant documentation and provide answers with source citations.

### Slash Commands

The plugin includes three convenient slash commands:

#### `/clarion-search <query>`

Search documentation directly:

```bash
/clarion-search how to create a template
/clarion-search FILE driver syntax
/clarion-search ABC library browse class
```

**Example output:**
```markdown
Found 5 relevant chunks:

Result 1: Template Guide (Score: 0.8542)
[Documentation excerpt with syntax and examples...]

Result 2: Template Language Reference (Score: 0.7891)
[Additional details and cross-references...]
```

#### `/clarion-status`

Check the health of Docker containers:

```bash
/clarion-status
```

**Shows:**
- Container running status
- Qdrant health check
- Database statistics (21,747 chunks loaded)
- MCP server connectivity

#### `/clarion-setup`

Restart containers (useful after system reboot):

```bash
/clarion-setup
```

**Actions:**
- Checks Docker is running
- Starts/restarts containers
- Verifies database is loaded
- Reports final status

### Advanced Search Parameters

When Claude uses the `search_docs` tool, you can request specific parameters:

```
"Search for FILE drivers in the core language documentation"
→ Filters by doc_type: "core_language"

"Find the top 10 results for browse templates"
→ Uses max_results: 10

"Search with high relevance for QUEUE syntax"
→ Applies min_score: 0.7
```

**Available doc_type filters:**
- `core_language` - Language Reference, Programming Guide
- `libraries` - ABC Library, Internet Builder, Math Library
- `ide_development` - IDE Reference, User Guide
- `templates` - Template Guide, Template Language Reference
- `specialized` - File Drivers, XML, Report Writer
- `advanced` - Application Broker, Enterprise features
- `utilities` - Various utility documentation

## Plugin vs Manual Installation

| Feature | Plugin Install | Manual Install |
|---------|----------------|----------------|
| **Installation Time** | 30-60 seconds | 5-10 minutes |
| **Command** | `/plugin add` | Clone + run scripts |
| **Configuration** | Automatic | Manual or script-assisted |
| **Updates** | `/plugin update` | Git pull + rebuild |
| **Removal** | `/plugin remove` | Manual cleanup |
| **Slash Commands** | Auto-installed | Manual creation |
| **Docker Setup** | Automated | Automated |
| **Complexity** | Very simple | Moderate |
| **Control** | Less (automated) | More (manual steps) |
| **Best For** | Most users | Advanced users, developers |

**Recommendation:** Use the plugin unless you need to:
- Modify the source code
- Use custom Docker configurations
- Debug installation issues
- Develop new features

## Troubleshooting

### Plugin Installation Failed

**Symptom:** `/plugin add` command fails

**Common Causes & Solutions:**

1. **Docker not running**
   ```bash
   # Start Docker Desktop and wait for it to fully initialize
   # Look for the whale icon in your system tray
   # Retry: /plugin add peterparker57/clarion-knowledge-base
   ```

2. **Insufficient disk space**
   ```bash
   # Free up at least 2GB of disk space
   # Check available space:
   # Windows: dir C:\
   # Mac/Linux: df -h
   ```

3. **Network issues**
   ```bash
   # Check internet connection
   # Try downloading manually:
   curl -L https://github.com/peterparker57/clarion-knowledge-base/releases/latest
   ```

4. **Port conflicts (6333, 6334)**
   ```bash
   # Check if ports are in use:
   # Windows: netstat -ano | findstr :6333
   # Mac/Linux: lsof -i :6333
   # Stop conflicting services or modify docker-compose.yml
   ```

### Plugin Not Responding

**Symptom:** Slash commands don't work or searches timeout

**Solutions:**

1. **Check container status**
   ```bash
   /clarion-status
   # Or manually:
   docker ps | grep clarion
   ```

2. **Restart containers**
   ```bash
   /clarion-setup
   # Or manually:
   docker-compose -f ~/.claude/plugins/clarion-knowledge-base/docker-compose.yml restart
   ```

3. **Check Docker logs**
   ```bash
   docker logs clarion-mcp-server
   docker logs clarion-qdrant
   ```

4. **Verify database is loaded**
   ```bash
   docker exec clarion-qdrant curl http://localhost:6333/collections/clarion_docs
   # Should show: "points_count": 21747
   ```

### Slash Commands Not Working

**Symptom:** `/clarion-search` not recognized

**Solutions:**

1. **Verify plugin is installed**
   ```bash
   /plugin list
   # Should show: clarion-knowledge-base
   ```

2. **Check command files exist**
   ```bash
   # Commands should be in:
   # ~/.claude/plugins/clarion-knowledge-base/.claude/commands/
   ls ~/.claude/plugins/clarion-knowledge-base/.claude/commands/
   ```

3. **Restart Claude Code**
   - Completely quit Claude Code
   - Restart it
   - Try slash commands again

### Search Returns No Results

**Symptom:** All queries return "No results found"

**Solutions:**

1. **Check database is populated**
   ```bash
   /clarion-status
   # Should show 21,747 vectors loaded
   ```

2. **Verify Qdrant is healthy**
   ```bash
   docker exec clarion-qdrant curl http://localhost:6333/health
   # Should return: {"status":"ok"}
   ```

3. **Try broader search terms**
   ```
   Instead of: "Very specific obscure feature"
   Try: "General topic area" or "Common keyword"
   ```

4. **Rebuild database (last resort)**
   ```bash
   cd ~/.claude/plugins/clarion-knowledge-base
   ./install.sh
   # Choose to re-import the database
   ```

### Docker Container Keeps Stopping

**Symptom:** Containers not running after restart

**Solutions:**

1. **Check Docker resource limits**
   - Open Docker Desktop → Settings → Resources
   - Ensure at least 2GB RAM allocated
   - Increase if needed

2. **Review container logs for errors**
   ```bash
   docker logs clarion-qdrant
   docker logs clarion-mcp-server
   ```

3. **Restart Docker Desktop**
   - Quit Docker Desktop completely
   - Start it again
   - Wait for full initialization
   - Run: `/clarion-setup`

4. **Check for system conflicts**
   ```bash
   # Other services using same ports?
   netstat -ano | findstr :6333  # Windows
   lsof -i :6333                 # Mac/Linux
   ```

## Managing the Plugin

### Updating the Plugin

To update to the latest version:

```bash
/plugin update clarion-knowledge-base
```

This will:
- Pull latest code from GitHub
- Rebuild Docker containers if needed
- Update vector database if a new snapshot is available
- Preserve your existing data

### Disabling the Plugin

Temporarily disable without uninstalling:

```bash
/plugin disable clarion-knowledge-base
```

To re-enable:

```bash
/plugin enable clarion-knowledge-base
```

### Uninstalling the Plugin

Complete removal:

```bash
/plugin remove clarion-knowledge-base
```

This will:
- Stop and remove Docker containers
- Remove Docker volumes (vector database)
- Delete plugin files from `~/.claude/plugins/`
- Remove MCP server configuration
- Remove slash commands

**Note:** This does NOT uninstall Docker itself.

### Manual Cleanup (if needed)

If `/plugin remove` fails, manual cleanup:

```bash
# 1. Stop and remove containers
docker-compose -f ~/.claude/plugins/clarion-knowledge-base/docker-compose.yml down -v

# 2. Delete plugin directory
# Mac/Linux:
rm -rf ~/.claude/plugins/clarion-knowledge-base

# Windows:
rmdir /s /q %USERPROFILE%\.claude\plugins\clarion-knowledge-base

# 3. Edit claude_code_config.json and remove "clarion-knowledge-base" entry
# Location: ~/.claude/claude_code_config.json (Mac/Linux)
#           %USERPROFILE%\.claude\claude_code_config.json (Windows)

# 4. Restart Claude Code
```

## Advanced Configuration

### Custom Docker Ports

If you need to change the default ports (6333, 6334):

1. Edit `docker-compose.yml` in the plugin directory:
   ```yaml
   services:
     qdrant:
       ports:
         - "7333:6333"  # Change host port (first number)
         - "7334:6334"
   ```

2. Update environment variables:
   ```yaml
   services:
     mcp-server:
       environment:
         - QDRANT_PORT=6333  # Keep container port same
   ```

3. Restart containers:
   ```bash
   /clarion-setup
   ```

### Development Mode

To work on the plugin source code:

1. **Mount local source code:**
   ```yaml
   # In docker-compose.yml:
   services:
     mcp-server:
       volumes:
         - ./src:/app/src:ro
   ```

2. **Run MCP server locally (outside Docker):**
   ```bash
   cd ~/.claude/plugins/clarion-knowledge-base
   python -m venv .venv
   source .venv/bin/activate  # Mac/Linux
   .venv\Scripts\activate     # Windows
   pip install -r requirements.txt
   python src/mcp_server.py
   ```

3. **Update Claude config to use local Python:**
   ```json
   {
     "mcpServers": {
       "clarion-knowledge-base": {
         "command": "python",
         "args": ["/path/to/plugin/src/mcp_server.py"]
       }
     }
   }
   ```

### Rebuilding the Vector Database

For developers who want to rebuild from source PDFs:

```bash
cd ~/.claude/plugins/clarion-knowledge-base

# Ensure PDFs are in Documents/ directory
ls Documents/  # Should show 21 Clarion PDF manuals

# Activate virtual environment
python -m venv .venv
source .venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Run processing pipeline
python src/pipeline_v3.py --recreate

# Restart Docker
docker-compose restart
```

**Note:** Original Clarion PDFs are not included in the repository. You must have licensed Clarion documentation.

## Performance Tuning

### Search Performance

Typical query times: < 100ms

If searches are slow:

1. **Check system resources:**
   ```bash
   docker stats clarion-qdrant clarion-mcp-server
   ```

2. **Optimize Docker resources:**
   - Allocate more RAM in Docker Desktop settings
   - Use SSD storage for Docker volumes
   - Increase CPU cores if available

3. **Reduce result count:**
   ```
   "Find top 3 results for..." instead of "Find all results for..."
   ```

### Disk Space Management

The vector database uses ~655 MB. To check usage:

```bash
docker volume ls
docker volume inspect clarion-knowledge-base_qdrant-data
```

To free space (WARNING: deletes database):

```bash
docker volume rm clarion-knowledge-base_qdrant-data
```

Then re-run `/clarion-setup` to rebuild.

## FAQ

### Do I need to keep Docker running?

Yes. The plugin requires Docker to be running for the Qdrant database and MCP server.

### Can I use this with Claude Desktop?

The plugin system is primarily for Claude Code. For Claude Desktop, use the manual installation method (see [INSTALLATION.md](INSTALLATION.md)).

### Does this work offline?

Once installed, the search functionality works offline. However, initial installation requires internet for downloading the vector database.

### How much does this cost?

The plugin is free and open-source (MIT license). Docker Desktop is free for personal use.

### Can I add my own Clarion documentation?

Yes, but it requires rebuilding the vector database. See "Rebuilding the Vector Database" above.

### Is my data sent to the cloud?

No. All search happens locally within Docker containers. Only your Claude interactions go to Anthropic's servers.

### How do I report bugs?

Open an issue on GitHub: [github.com/peterparker57/clarion-knowledge-base/issues](https://github.com/peterparker57/clarion-knowledge-base/issues)

### Can I contribute improvements?

Yes! The project is open-source. See the main [README.md](README.md) for contribution guidelines.

## Support Resources

- **Documentation:** [README.md](README.md) - Main documentation
- **Installation:** [INSTALLATION.md](INSTALLATION.md) - Detailed manual installation
- **Issues:** [GitHub Issues](https://github.com/peterparker57/clarion-knowledge-base/issues)
- **Discussions:** [GitHub Discussions](https://github.com/peterparker57/clarion-knowledge-base/discussions)
- **MCP Protocol:** [Model Context Protocol Docs](https://modelcontextprotocol.io/)
- **Docker Help:** [Docker Documentation](https://docs.docker.com/)

---

**Made with ❤️ for the Clarion Developer Community**

*Instant documentation access via Claude AI - install in 30 seconds*
