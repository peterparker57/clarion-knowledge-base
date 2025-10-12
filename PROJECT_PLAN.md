# Clarion Knowledge Base - GitHub Distribution Project Plan

## Project Goal
Create a GitHub repository with simplified installation for distributing the Clarion Knowledge Base MCP server to other Clarion developers. The installation should be as simple as possible - ideally 3 steps taking ~5 minutes total.

## Current Status
- ✅ MCP server fully functional and tested
- ✅ Vector database populated with 21,747 chunks from 21 Clarion PDFs
- ✅ Code indentation issue resolved (V3 pipeline)
- ✅ Search quality validated (0.67 avg relevance)
- ✅ HTML documentation created
- ⏳ Not yet in git repository
- ⏳ No GitHub repo exists yet

## GitHub Repository Information
- **Owner:** peterparker57
- **Repository Name:** clarion-knowledge-base (suggested)
- **Visibility:** Private initially (can make public later)
- **Future URL:** https://github.com/peterparker57/clarion-knowledge-base

## Target User Installation Flow
```bash
# Step 1: Clone repository
git clone https://github.com/peterparker57/clarion-knowledge-base
cd clarion-knowledge-base

# Step 2: Run installer (handles everything)
./install.sh      # Mac/Linux
# or
install.bat       # Windows

# Step 3: Restart Claude (Code or Desktop)
```

## Key Technical Details
- **Qdrant vector database size:** 655MB (Docker volume: qdrant_storage)
- **Processed markdown:** 11MB (data/processed/)
- **Total vector points:** 21,747
- **Source PDFs:** 21 files in Documents/
- **Python version:** 3.13+
- **Current location:** C:\Dev\ClarionAI

## Components to Build

### 1. Repository Initialization & Cleanup
**Tasks:**
- Initialize git repository in C:\Dev\ClarionAI
- Create comprehensive .gitignore
- Remove old V1/V2 files (keep only V3 production code)
- Clean up unnecessary files
- Set git user config (use GitHub token info)

**Files to Keep:**
- src/mcp_server.py (production)
- src/embeddings.py
- src/vector_store.py
- src/chunking.py
- src/pdf_processor_v3.py
- src/pipeline_v3.py
- requirements.txt
- documentation/index.html
- README.md (to be created)

**Files to Remove/Ignore:**
- src/pdf_processor.py (old V1)
- src/pdf_processor_v2.py (old V2)
- src/pipeline.py (old V1)
- src/pipeline_v2.py (old V2)
- src/fix_indentation.py (one-time script)
- data/chunks/ (regenerated)
- .venv/ (user creates their own)
- __pycache__/

### 2. Qdrant Snapshot Export
**Tasks:**
- Create snapshot of current Qdrant vector database (655MB)
- Export from Docker volume: qdrant_storage
- Compress for distribution
- Test restoration process
- Prepare for GitHub Release attachment

**Scripts to Create:**
- `scripts/export_snapshot.py` - Export current Qdrant DB
- `scripts/import_snapshot.py` - Import snapshot on user side

### 3. Docker Compose Configuration
**Tasks:**
- Create docker-compose.yml with two services:
  - Qdrant service (with volume for persistence)
  - MCP server service (Python container)
- Create Dockerfile for MCP server
- Configure networking between services
- Set up health checks
- Configure automatic snapshot import on first run

**Files to Create:**
- `docker-compose.yml`
- `Dockerfile`
- `.dockerignore`

### 4. Installation Scripts
**Tasks:**
- Create cross-platform installation scripts
- Interactive prompts: "Claude Code, Desktop, or Both?"
- Auto-detect OS and configure appropriate paths
- Download Qdrant snapshot from GitHub Release
- Start Docker services
- Configure Claude config files
- Verify installation

**Files to Create:**
- `install.sh` (Mac/Linux with bash)
- `install.bat` (Windows batch script)

**Features:**
- Check prerequisites (Docker, Python for local dev)
- Download snapshot from GitHub Release
- Extract and load into Qdrant
- Start docker-compose services
- Detect Claude installation paths
- Write config files with correct absolute paths
- Test MCP connection
- Print success message with next steps

### 5. Documentation Updates

#### README.md (GitHub landing page)
**Sections:**
- Project overview and features
- Quick start (3 steps)
- Prerequisites
- Installation for Claude Code
- Installation for Claude Desktop
- Usage examples
- Troubleshooting basics
- Link to full HTML documentation
- Technical details
- License/acknowledgements

#### documentation/index.html (Update existing)
**Add sections for:**
- Claude Code configuration (existing)
- Claude Desktop configuration (NEW)
  - Windows: %APPDATA%\Claude\claude_desktop_config.json
  - macOS: ~/Library/Application Support/Claude/claude_desktop_config.json
  - Linux: ~/.config/Claude/claude_desktop_config.json
- Side-by-side comparison of both clients
- Platform-specific instructions (Windows/Mac/Linux)
- Docker-based installation flow (updated)

#### Config Templates
**Files to Create:**
- `config/claude_code_example.json` - Template with placeholder paths
- `config/claude_desktop_example.json` - Template with placeholder paths
- Comments explaining what to customize

### 6. GitHub Repository Setup
**Tasks:**
- Create GitHub repository via API or web interface
- Push initial commit with all files
- Create GitHub Release (v1.0.0)
- Upload Qdrant snapshot as release asset
- Write release notes
- Test installation from fresh clone

**GitHub Release Assets:**
- `qdrant-snapshot.tar.gz` (655MB compressed)
- Installation instructions in release notes

### 7. Testing & Validation
**Tasks:**
- Test installation on Windows (your machine)
- Test with Claude Code
- Test with Claude Desktop
- Verify search functionality
- Test from fresh directory
- Document any issues found

## Configuration Examples

### Claude Code Config (~/.claude.json)
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

### Claude Desktop Config (OS-specific paths)
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

## Parallel Execution Opportunities

These tasks can be done in parallel by subagents:

**Group A (Repository Setup) - Can run in parallel:**
1. Create .gitignore and clean up old files
2. Initialize git and configure
3. Create README.md structure

**Group B (Docker Infrastructure) - Can run in parallel:**
1. Create docker-compose.yml
2. Create Dockerfile
3. Create Qdrant export/import scripts

**Group C (Installation Scripts) - Can run in parallel:**
1. Create install.sh (Linux/Mac)
2. Create install.bat (Windows)
3. Create config file templates

**Group D (Documentation) - Can run in parallel:**
1. Update documentation/index.html for both clients
2. Create comprehensive README.md
3. Create configuration examples

**Sequential Dependencies:**
- Group A must complete before committing to git
- Group B (Qdrant export) must complete before creating GitHub Release
- Groups A, B, C, D can all work in parallel

## Success Criteria
- ✅ GitHub repository created and populated
- ✅ Installation works on Windows
- ✅ Works with both Claude Code and Claude Desktop
- ✅ Installation takes < 10 minutes
- ✅ No manual Python/pip/processing required by user
- ✅ Comprehensive documentation included
- ✅ Search functionality preserved (0.6+ relevance)
- ✅ Code indentation maintained

## Post-Distribution
- Monitor for issues
- Create troubleshooting FAQ
- Consider: Tutorial video
- Consider: Making repository public for wider distribution
- Consider: Clarion community forum announcement

## Notes
- Keep GitHub token secure (don't commit to repo)
- PDFs may need copyright consideration (don't distribute if unclear)
- Test on clean machine if possible
- Consider creating a demo video
