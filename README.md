# Clarion Knowledge Base - MCP Server

> **Semantic search for Clarion programming documentation via Claude AI**

[![Claude Code Plugin](https://img.shields.io/badge/Claude%20Code-Plugin-blue)](https://github.com/peterparker57/clarion-knowledge-base)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Docker](https://img.shields.io/badge/docker-required-blue.svg)
![Python](https://img.shields.io/badge/python-3.13+-blue.svg)

Instantly search across 21 Clarion documentation manuals using natural language queries in Claude Code or Claude Desktop. Powered by semantic search with 21,747 indexed documentation chunks.

---

## Overview

**Clarion Knowledge Base** is a Model Context Protocol (MCP) server that brings the entire Clarion programming language documentation to your fingertips within Claude AI. Instead of manually searching through PDF manuals, simply ask Claude natural language questions about Clarion programming and get instant, relevant answers with source citations.

### Why This Matters for Clarion Developers

- **Instant Documentation Access**: Search 21 PDF manuals (Language Reference, ABC Library, Templates, IDE, etc.) in seconds
- **Natural Language Queries**: Ask questions like "How do I create a browse?" instead of keyword searching
- **Works in Your Workflow**: Integrates seamlessly with Claude Code and Claude Desktop
- **Always Available**: Runs locally via Docker - no cloud dependency for documentation lookup
- **Semantic Understanding**: Finds relevant content even if you don't know the exact terminology

### Key Features

- **21,747 Indexed Chunks** - Complete coverage of Clarion documentation
- **Semantic Search** - Understands intent, not just keywords
- **MCP Protocol Integration** - Native Claude Code and Claude Desktop support
- **Docker-Based** - Simple deployment, no Python environment setup needed
- **Qdrant Vector Database** - Fast, efficient similarity search
- **Source Citations** - Every result includes document source and location
- **Filtered Search** - Optionally search within specific documentation categories

---

## Quick Install (2 Minutes)

**The easiest way to install is using the Claude Code plugin system:**

```bash
# Step 1: Add the marketplace
/plugin marketplace add https://github.com/peterparker57/clarion-knowledge-base.git

# Step 2: Install the plugin
/plugin install clarion-knowledge-base

# Step 3: Run the setup command (this downloads and configures everything)
/clarion-setup
```

**Requirements:** Docker Desktop must be installed and running.

The setup command will:
- Download and configure Docker containers
- Set up the Qdrant vector database (~76 MB)
- Import 21,747 documentation chunks
- Verify everything is working

After setup completes, **restart Claude Code** and you can use slash commands like `/clarion-search` or simply ask Claude questions about Clarion programming!

---

## NEW: Standalone Web App (No Claude Required!)

**Want to use the Clarion Knowledge Base without Claude?** Use our standalone web application with your own LLM provider (DeepSeek, OpenAI, Claude, Gemini, Grok, or FREE local Ollama).

### Quick Start (Pre-Built Docker Image):

```bash
# Create and enter a folder for Clarion KB
mkdir ~/clarion-kb
cd ~/clarion-kb

# Download deployment file
curl -O https://raw.githubusercontent.com/peterparker57/clarion-knowledge-base/main/docker-compose-public.yml

# Start the app (first time downloads ~12GB)
docker-compose -f docker-compose-public.yml up -d

# Open browser
open http://localhost:8080
```

**That's it!** No building, no Git clone - just pull and run from Docker Hub.

**Important:** Run all commands in the same folder (the `clarion-kb` folder you created).

#### Custom Port Configuration

Port 8080 already in use? No problem!

**Option 1: Environment Variable** (easiest)
```bash
CLARION_WEB_PORT=8081 docker-compose -f docker-compose-public.yml up -d
# Access at http://localhost:8081
```

**Option 2: Edit the File**
Edit `docker-compose-public.yml` and change:
```yaml
ports:
  - "8080:8080"  # Change first number: "8081:8080"
```

**Common alternative ports:** 8081, 8082, 3000, 5000, 9090

#### First Startup Time

**⚠️ Important:** On first startup, services may take 2-3 minutes to become healthy while:
- Qdrant restores the 21,747 documentation chunks from snapshot (~90 seconds)
- Web app loads the sentence transformer embedding model (~80MB)
- Docker performs health checks to ensure services are ready

**Be patient!** The containers will start automatically once Qdrant is healthy.

Check startup progress:
```bash
docker-compose -f docker-compose-public.yml logs -f
```

Wait for: `"Uvicorn running on http://0.0.0.0:8080"` before accessing the web interface.

### Features:
- 🌐 **Browser-Based Interface** - Access from any device
- 🔑 **Multiple LLM Providers**: DeepSeek ($0.35/1M), OpenAI, Claude, Gemini, Grok, or Ollama (FREE)
- 💰 **Real-Time Pricing** - See cost per model before you query
- 📊 **3 Query Modes**: Augmented (docs + AI), Strict (docs only), Chat (AI only - fast)
- 📱 **Mobile Friendly** - Works on phones/tablets
- 📚 **Same Data**: 21,747 documentation chunks as MCP mode
- 🎯 **Source Citations** - Every answer includes document sources

### When to Use Each Mode:

| Feature | MCP Mode | Web App |
|---------|----------|---------|
| Best for | Claude Code/Desktop users | Everyone |
| LLM | Claude (Anthropic) | Any provider (your choice) |
| Interface | Claude chat | Web browser |
| Cost | Claude subscription | Pay-per-use or FREE (Ollama) |
| Mobile | ❌ No | ✅ Yes |

**📖 Full Documentation:** See [README-WEBAPP.md](README-WEBAPP.md) for complete instructions, LLM provider setup, and troubleshooting.

**🐳 Docker Hub:** [clarionlive/clarion-knowledge-base-webapp](https://hub.docker.com/r/clarionlive/clarion-knowledge-base-webapp)

---

## Alternative: Manual Installation (MCP Mode)

If you prefer manual installation or need more control, you can install via the installer scripts:

```bash
# Step 1: Clone the repository
git clone https://github.com/peterparker57/clarion-knowledge-base
cd clarion-knowledge-base

# Step 2: Run the installer
./install.sh      # Mac/Linux
# or
install.bat       # Windows

# Step 3: Restart Claude Code or Claude Desktop
# The Clarion Knowledge Base will now be available as an MCP server
```

**What happens during installation:**
1. Checks Docker is installed and running
2. Downloads pre-built vector database (~76 MB compressed)
3. Starts Docker containers (Qdrant + MCP server)
4. Configures Claude Code/Desktop automatically
5. Verifies the MCP server is working

**Note:** The installer will prompt you to choose Claude Code, Claude Desktop, or both.

See [PLUGIN.md](PLUGIN.md) for detailed plugin documentation or [INSTALLATION.md](INSTALLATION.md) for manual installation details.

---

## Prerequisites

Before installation, ensure you have:

- **Docker Desktop** - [Download here](https://www.docker.com/products/docker-desktop/)
  - Must be installed and running
  - At least 2GB available disk space
- **Claude Code** or **Claude Desktop** - [Get Claude](https://claude.ai/)
  - Either or both clients supported
- **Internet Connection** - Required for initial database download (~76 MB)
- **System Requirements:**
  - Windows 10/11, macOS 10.15+, or Linux
  - 4GB RAM minimum (8GB recommended)

---

## Installation Details

**Recommended:** Use the plugin installation method described above (`/plugin add peterparker57/clarion-knowledge-base`).

The following sections are for manual configuration or troubleshooting.

### For Claude Code

The installer (or plugin) automatically configures Claude Code, but if you need to configure manually:

**Configuration File Locations:**
- **Windows:** `%USERPROFILE%\.claude\claude_code_config.json`
- **macOS:** `~/.claude/claude_code_config.json`
- **Linux:** `~/.config/claude-code/config.json`

**Example Configuration:**
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

**Verify Installation:**
1. Restart Claude Code completely
2. Open a new chat or project
3. Type `/mcp` to see available servers
4. Look for "clarion-knowledge-base" in the list
5. Try a test query: "How do I define a QUEUE in Clarion?"

### For Claude Desktop

The installer automatically configures Claude Desktop, but for manual configuration:

**Configuration File Locations:**
- **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`
- **macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Linux:** `~/.config/Claude/claude_desktop_config.json`

**Example Configuration:**
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

**Verify Installation:**
1. Completely quit and restart Claude Desktop
2. Look for the tools icon (🔧) in the chat interface
3. Click to see available tools
4. "search_docs" from clarion-knowledge-base should appear
5. Try asking: "Explain the FILE driver in Clarion"

---

## Usage Examples

Once installed, you can query Clarion documentation naturally within Claude:

### Example Queries

**Basic Language Questions:**
```
"How do I create a browse in Clarion?"
"What's the syntax for a LOOP statement?"
"Explain the difference between GROUP and QUEUE"
```

**Library and Component Questions:**
```
"How do I use the ABC library for file handling?"
"What are the methods available in the BrowseClass?"
"Show me examples of the Internet Builder classes"
```

**Template and IDE Questions:**
```
"What are embed points in Clarion templates?"
"How do I create a custom template?"
"Explain the Application Generator options"
```

**Database and Advanced Topics:**
```
"How do I connect to a SQL database in Clarion?"
"What's the FILE driver architecture?"
"How do I implement XML processing?"
```

### Example Output

When you ask a question, you'll receive:

```markdown
# Search Results for: "How do I define a QUEUE in Clarion?"

**Found 5 relevant chunks**

## Result 1: Language Reference
**Score:** 0.8542 | **Type:** core_language | **Chunk:** 42/156

**Content:**
```
QUEUE Structure

A QUEUE is a memory-resident table with automatic memory management...
[Full documentation excerpt with proper formatting]
```

## Result 2: Programming Guide
**Score:** 0.7891 | **Type:** core_language | **Chunk:** 89/201

**Content:**
```
[Additional relevant content...]
```

---
*Retrieved from Clarion Knowledge Base (Vector Store: 5 chunks)*
```

### Tips for Effective Queries

1. **Be Specific**: "How do I sort a QUEUE?" vs. "QUEUE sorting"
2. **Use Natural Language**: Write questions as you would ask a colleague
3. **Include Context**: "In templates, how do I..." helps filter results
4. **Try Multiple Phrasings**: If results aren't great, rephrase your question
5. **Use Filters**: Specify doc_type for focused searches (see Advanced Usage)

---

## Architecture

### System Overview

```
┌─────────────────────────────────────────────────────────────┐
│                    Claude AI (Code/Desktop)                  │
│                                                              │
│  User asks: "How do I create a browse in Clarion?"          │
└────────────────────────┬─────────────────────────────────────┘
                         │ MCP Protocol
                         ▼
┌─────────────────────────────────────────────────────────────┐
│              Docker Container: clarion-mcp-server            │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  MCP Server (Python)                                 │  │
│  │  - Receives query                                    │  │
│  │  - Generates embedding (768-dim vector)              │  │
│  │  - Searches vector database                          │  │
│  │  - Formats results with citations                    │  │
│  └────────────────────┬─────────────────────────────────┘  │
└─────────────────────────┼─────────────────────────────────────┘
                         │ gRPC/HTTP
                         ▼
┌─────────────────────────────────────────────────────────────┐
│              Docker Container: clarion-qdrant                │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Qdrant Vector Database                              │  │
│  │  - 21,747 documentation chunks                       │  │
│  │  - 768-dimensional embeddings                        │  │
│  │  - < 100ms search latency                            │  │
│  │  - Persistent storage (Docker volume)                │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

### Components

**1. Qdrant Vector Database**
- Stores 21,747 document chunks as 768-dimensional embeddings
- Uses `all-MiniLM-L6-v2` sentence transformer model
- Persistent storage via Docker volume (655 MB)
- Ports: 6333 (REST API), 6334 (gRPC)

**2. MCP Server (Python)**
- Implements Model Context Protocol for Claude integration
- Handles query embedding generation
- Performs vector similarity search
- Formats results with metadata and citations
- Runs on-demand via `docker exec` (no persistent process)

**3. Docker Compose Orchestration**
- Manages both services as a unit
- Handles networking between containers
- Provides health checks and automatic restarts
- Isolates dependencies (no Python environment conflicts)

### Communication Flow

1. **User Query** → Claude Code/Desktop receives natural language question
2. **MCP Call** → Claude invokes `search_docs` tool via MCP protocol
3. **Embedding** → MCP server generates query embedding using sentence transformers
4. **Vector Search** → Qdrant finds similar document chunks via cosine similarity
5. **Results** → MCP server formats results with scores, sources, and content
6. **Response** → Claude receives structured results and presents to user

---

## Troubleshooting

### Common Issues

#### Docker Not Running
**Symptom:** Installation fails with "Cannot connect to Docker daemon"

**Solution:**
```bash
# Start Docker Desktop application
# Wait for it to fully start (whale icon in system tray)
# Retry installation
```

#### Port Conflicts (6333, 6334)
**Symptom:** "Port already in use" error

**Solution:**
```bash
# Check what's using the ports
# Windows:
netstat -ano | findstr :6333
# Mac/Linux:
lsof -i :6333

# Stop conflicting service or change ports in docker-compose.yml
```

#### MCP Server Not Responding
**Symptom:** Claude shows "MCP server timeout" or no response

**Solution:**
```bash
# Check if containers are running
docker ps

# Should see both:
# - clarion-qdrant
# - clarion-mcp-server

# If not running:
cd /path/to/clarion-knowledge-base
docker-compose up -d

# Check logs
docker logs clarion-mcp-server
docker logs clarion-qdrant
```

#### Configuration File Not Found
**Symptom:** "Could not find Claude config file"

**Solution:**
1. Verify Claude Code/Desktop is installed
2. Run Claude at least once to create config directory
3. Manually create config file using examples above
4. Ensure JSON syntax is valid (use a JSON validator)

#### Search Returns No Results
**Symptom:** All queries return "No results found"

**Solution:**
```bash
# Check if vector database is populated
docker exec -it clarion-qdrant curl http://localhost:6333/collections/clarion_docs

# Should show points_count: 21747
# If not, database may need re-import
```

### Checking Logs

**View MCP Server logs:**
```bash
docker logs clarion-mcp-server
# Add -f to follow logs in real-time
docker logs -f clarion-mcp-server
```

**View Qdrant logs:**
```bash
docker logs clarion-qdrant
```

**View all logs:**
```bash
docker-compose logs
```

### Restarting Services

**Restart both services:**
```bash
cd /path/to/clarion-knowledge-base
docker-compose restart
```

**Restart individual service:**
```bash
docker restart clarion-mcp-server
# or
docker restart clarion-qdrant
```

**Full restart (stops and starts):**
```bash
docker-compose down
docker-compose up -d
```

---

## Advanced Usage

### Updating the Vector Database

If you want to rebuild the vector database from scratch (for developers):

```bash
# 1. Ensure you have source PDFs in Documents/
# 2. Activate Python virtual environment
python -m venv .venv
source .venv/bin/activate  # Mac/Linux
# or
.venv\Scripts\activate  # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run processing pipeline
python src/pipeline_v3.py --recreate

# 5. Restart Docker services
docker-compose restart
```

### Rebuilding Containers

Force rebuild of Docker images:

```bash
# Rebuild without cache
docker-compose build --no-cache

# Restart with new images
docker-compose up -d --force-recreate
```

### Environment Variables

Customize behavior via environment variables in `docker-compose.yml`:

```yaml
environment:
  - QDRANT_HOST=qdrant        # Qdrant container hostname
  - QDRANT_PORT=6333          # Qdrant REST API port
  - COLLECTION_NAME=clarion_docs  # Vector collection name
```

### Development Setup

For local development outside Docker:

```bash
# 1. Clone repository
git clone https://github.com/peterparker57/clarion-knowledge-base
cd clarion-knowledge-base

# 2. Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Mac/Linux
.venv\Scripts\activate     # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Start Qdrant only
docker-compose up -d qdrant

# 5. Run MCP server locally (for testing)
python src/mcp_server.py

# 6. Configure Claude to use local Python instead of Docker
# Update config to point to your local Python interpreter
```

---

## Technical Details

### Technology Stack

- **Language:** Python 3.13+
- **Vector Database:** Qdrant (latest)
- **Embedding Model:** sentence-transformers/all-MiniLM-L6-v2
  - Dimension: 768
  - Model size: ~80 MB
  - Inference: CPU-based, ~50ms per query
- **MCP Protocol:** Version 1.17.0
- **PDF Processing:** PyMuPDF4LLM (for developers rebuilding DB)
- **Containerization:** Docker & Docker Compose

### Database Statistics

- **Total Chunks:** 21,747
- **Source Documents:** 21 Clarion PDF manuals
- **Average Chunk Size:** 574 characters
- **Storage Size:**
  - Compressed (download): 76 MB
  - Uncompressed (Docker volume): 655 MB
- **Search Performance:** < 100ms typical query time

### Documentation Categories

The vector database includes these document types:

- **core_language** - Language Reference, Programming Guide, Learning Clarion
- **libraries** - ABC Library Reference, Internet Builder, Business Math Library
- **ide_development** - IDE Reference, User Guide, Getting Started
- **templates** - Template Guide, Template Language Reference
- **specialized** - File Drivers, XML, Report Writer, Application Broker

### Filtered Search Example

Use the `doc_type` parameter to search specific categories:

```python
# In Claude, you can specify:
search_docs(
    query="How do I handle file errors?",
    doc_type="core_language",
    max_results=3,
    min_score=0.5
)
```

---

## Documentation

### Full Documentation

Complete HTML documentation is available in the repository:
- **Local:** Open `documentation/index.html` in your browser
- **Includes:** Detailed architecture, API reference, development guides

### External Resources

- **MCP Protocol:** [Model Context Protocol Docs](https://modelcontextprotocol.io/)
- **Qdrant Documentation:** [qdrant.tech/documentation](https://qdrant.tech/documentation/)
- **Docker Documentation:** [docs.docker.com](https://docs.docker.com/)
- **Claude AI:** [claude.ai](https://claude.ai/)

---

## Contributing

This project is designed for **Clarion developers** who want instant access to documentation within Claude AI.

### Future Improvements

Potential enhancements we're considering:
- Support for custom Clarion documentation (your company's docs)
- Integration with Clarion community forums and knowledge bases
- Enhanced metadata (code examples, version-specific docs)
- Multi-language support
- GraphRAG for relationship mapping between concepts

### Feedback Welcome

Found a bug? Have a suggestion? Please:
1. Check existing GitHub Issues
2. Open a new issue with details
3. Include logs and reproduction steps
4. Tag appropriately (bug, enhancement, documentation)

**Note:** This is a community tool. Response times may vary.

---

## License & Acknowledgements

### License

This project is licensed under the **MIT License** - see LICENSE file for details.

**Important:** This tool processes Clarion documentation which is copyrighted by **SoftVelocity Inc.** The vector database is derived from official Clarion documentation PDFs. This tool is intended for **personal and educational use** by licensed Clarion developers. The original PDF documentation is not redistributed with this project.

### Clarion Documentation

All documentation content is copyright **SoftVelocity Inc.** and used under fair use for personal reference purposes. This tool does not replace official documentation but provides enhanced search capabilities.

### Acknowledgements

This project stands on the shoulders of incredible open-source tools:

- **Claude AI & MCP Protocol** - [Anthropic](https://anthropic.com/) for the Model Context Protocol
- **Qdrant** - [qdrant.tech](https://qdrant.tech/) for the vector database engine
- **Sentence Transformers** - [sbert.net](https://www.sbert.net/) for the embedding model
- **PyMuPDF4LLM** - [pymupdf.io](https://pymupdf.io/) for PDF parsing
- **Docker** - [docker.com](https://www.docker.com/) for containerization
- **Python Community** - For all the amazing libraries that make this possible

**Special Thanks:**
- SoftVelocity for creating Clarion and maintaining excellent documentation
- The Clarion developer community for feedback and support

---

## Project Status

**Version:** 1.0.0
**Status:** Production Ready ✓
**Last Updated:** 2025-10-12

### Tested Environments

- ✓ Windows 10/11 with Docker Desktop
- ✓ macOS 12+ with Docker Desktop
- ✓ Linux (Ubuntu 22.04+) with Docker Engine
- ✓ Claude Code (latest)
- ✓ Claude Desktop (latest)

### Known Limitations

1. **Code Indentation:** Some code examples may have lost indentation during PDF conversion. Clarion code should be manually formatted before use.
2. **PDF Quality:** Search quality depends on source PDF quality. Some older manuals may have OCR artifacts.
3. **No Incremental Updates:** To update documentation, full rebuild currently required.
4. **English Only:** Only English language documentation is supported.

---

## Contact & Support

- **GitHub Repository:** [github.com/peterparker57/clarion-knowledge-base](https://github.com/peterparker57/clarion-knowledge-base)
- **Issues:** [GitHub Issues](https://github.com/peterparker57/clarion-knowledge-base/issues)
- **Discussions:** [GitHub Discussions](https://github.com/peterparker57/clarion-knowledge-base/discussions)

---

<div align="center">

**Made with ❤️ for the Clarion Developer Community**

*Bringing 20+ years of Clarion documentation to your AI assistant*

[⭐ Star on GitHub](https://github.com/peterparker57/clarion-knowledge-base) | [📖 Read the Docs](documentation/index.html) | [🐛 Report Bug](https://github.com/peterparker57/clarion-knowledge-base/issues)

</div>
