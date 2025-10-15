# Clarion Knowledge Base - Web App

> **Quick search Clarion documentation from your browser - no IDE setup required!**

Search across 21 Clarion documentation manuals using natural language queries. Works with any LLM provider: DeepSeek, OpenAI, Claude, Gemini, Grok, and local Ollama.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Docker](https://img.shields.io/badge/docker-required-blue.svg)

---

## Quick Start (4 Commands)

1. **Prerequisites**: [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed

2. **Create a folder and navigate to it**:
   ```bash
   mkdir ~/clarion-kb
   cd ~/clarion-kb
   ```

3. **Download deployment file**:
   ```bash
   curl -O https://raw.githubusercontent.com/peterparker57/clarion-knowledge-base/main/docker-compose-public.yml
   ```

4. **Start the app** (first time takes 2-3 min to download ~12GB):
   ```bash
   docker-compose -f docker-compose-public.yml up -d
   ```

5. **Open browser**: http://localhost:8080

6. **Configure your LLM Provider**:
   - Click the "Provider" dropdown
   - Select a provider (DeepSeek recommended - cheapest at $0.35/1M tokens)
   - Click "Model" to see pricing for each model
   - Enter your API key
   - Click "Save"
   - Start searching!

---

## Port Configuration

The web app runs on **port 8080** by default. If this port is already in use on your system, you can easily change it.

### Method 1: Environment Variable (Recommended)

Set the `CLARION_WEB_PORT` environment variable when starting:

```bash
cd ~/clarion-kb
CLARION_WEB_PORT=8081 docker-compose -f docker-compose-public.yml up -d
```

Then access at: http://localhost:8081

**Common alternative ports:** 8081, 8082, 3000, 5000, 9090

### Method 2: Edit the Configuration File

1. Open `docker-compose-public.yml` in a text editor
2. Find the line under `web-app` → `ports`:
   ```yaml
   ports:
     - "8080:8080"  # Change the FIRST number only
   ```
3. Change to your desired port:
   ```yaml
   ports:
     - "8081:8080"  # Now accessible at http://localhost:8081
   ```
4. Save and restart:
   ```bash
   cd ~/clarion-kb
   docker-compose -f docker-compose-public.yml up -d
   ```

### Method 3: Use Default with Port Forwarding

If you're comfortable with networking, you can keep port 8080 and use your router/firewall to forward another port to it.

---

## Features

- **21,747 Indexed Documentation Chunks** - Complete Clarion documentation coverage
- **Multiple LLM Providers**:
  - **DeepSeek** ($0.35/1M) - Recommended for cost
  - **OpenAI** (GPT-4o, GPT-5, o1, o3-mini) - Latest models
  - **Anthropic Claude** (Sonnet, Opus, Haiku) - High quality
  - **Google Gemini** (2.5 Pro, 2.0 Flash) - Fast and affordable
  - **xAI Grok** (Grok 4, Grok 4 Fast) - X's AI
  - **Ollama** (FREE) - Local models (llama3, mistral, etc.)
- **3 Query Modes**:
  - **Augmented** (Default) - Best for code generation and examples
  - **Strict** - Documentation lookup only
  - **Chat** - Quick answers without doc search
- **Source Citations** - Every answer includes document sources
- **Real-time Pricing** - See cost per query for each model

---

## Usage Example

**Query**: "How do I create a browse procedure?"

**Answer** (with code examples and source citations):
```clarion
To create a browse procedure:
1. Use the Application Generator...
[Complete answer with code samples]

Sources: ABC Library Reference (p. 124), Template Guide (p. 45)
```

**Cost**: ~$0.0003 (DeepSeek) / ~$0.002 (GPT-4o)

---

## Supported LLM Providers

### API-Based Providers

Get API keys from:
- **DeepSeek**: https://platform.deepseek.com/api_keys
- **OpenAI**: https://platform.openai.com/api-keys
- **Anthropic**: https://console.anthropic.com/settings/keys
- **Google Gemini**: https://ai.google.dev/gemini-api/docs/api-key
- **xAI Grok**: https://x.ai/api

### Local Provider (Free)

**Ollama** - Run LLMs locally for free:
1. Install Ollama: https://ollama.ai/download
2. Pull a model: `ollama pull llama3`
3. Select "Ollama (Local)" in the web app
4. No API key needed!

---

## Managing the App

**Important:** All commands below should be run from the same folder where you downloaded `docker-compose-public.yml` (e.g., `~/clarion-kb`).

### View Logs
```bash
cd ~/clarion-kb  # Navigate to your Clarion KB folder
docker-compose -f docker-compose-public.yml logs -f web-app
```

### Stop the App
```bash
cd ~/clarion-kb
docker-compose -f docker-compose-public.yml down
```

### Restart the App
```bash
cd ~/clarion-kb
docker-compose -f docker-compose-public.yml restart
```

### Update to Latest Version
```bash
cd ~/clarion-kb
docker-compose -f docker-compose-public.yml pull
docker-compose -f docker-compose-public.yml up -d
```

### Remove Everything (including data)
```bash
cd ~/clarion-kb
docker-compose -f docker-compose-public.yml down -v
```

---

## Integration with MCP Plugin

### Already Have the MCP Plugin Installed?

If you're already using the Clarion Knowledge Base MCP plugin with Claude Code/Desktop, you can add the web app to share the same Qdrant database:

```bash
# Download the addon compose file
curl -O https://raw.githubusercontent.com/peterparker57/clarion-knowledge-base/main/docker-compose-webapp-addon.yml

# Start the web app (connects to existing MCP Qdrant)
docker-compose -f docker-compose-webapp-addon.yml up -d

# Access the web UI
open http://localhost:8080
```

**Benefits of running both:**
- Share the same documentation database (no duplication)
- Use MCP for conversational queries in Claude
- Use web app for quick lookups and testing with different LLMs

### Want to Install the MCP Plugin?

For **chat-style conversations** in your IDE or Claude Desktop, use our MCP server:

**MCP Server Installation** (Claude Code / Claude Desktop):
```bash
# Install via Claude Code plugin system
/plugin marketplace add https://github.com/peterparker57/clarion-knowledge-base.git
/plugin install clarion-knowledge-base
/clarion-setup
```

**Full MCP Documentation**: [Clarion Knowledge Base MCP](https://github.com/peterparker57/clarion-knowledge-base)

---

## Pricing Comparison

Per-query costs (typical 2000 tokens):

| Provider | Model | Cost/Query |
|----------|-------|------------|
| DeepSeek | deepseek-chat | $0.0007 |
| OpenAI | gpt-4o-mini | $0.0008 |
| Google | gemini-2.0-flash | $0.0005 |
| Ollama | llama3 (local) | **FREE** |
| OpenAI | gpt-4o | $0.0125 |
| Anthropic | claude-sonnet-4-5 | $0.0180 |

**Recommendation**: Start with DeepSeek or Ollama (free)

---

## Troubleshooting

### Port 8080 Already in Use

**Symptom:** Error message like "port is already allocated" or "address already in use"

**Solution 1 - Environment Variable** (easiest):
```bash
cd ~/clarion-kb
docker-compose -f docker-compose-public.yml down  # Stop current containers
CLARION_WEB_PORT=8081 docker-compose -f docker-compose-public.yml up -d  # Restart on port 8081
```

**Solution 2 - Edit Configuration**:
1. Edit `docker-compose-public.yml`
2. Change `- "8080:8080"` to `- "8081:8080"` (or another available port)
3. Restart: `docker-compose -f docker-compose-public.yml up -d`

**Solution 3 - Find What's Using Port 8080**:
```bash
# Windows
netstat -ano | findstr :8080

# Mac/Linux
lsof -i :8080
```

Then stop that service or use a different port for Clarion KB.

### Container Shows "Unhealthy" Status

**Symptom:** `docker ps` shows containers as "unhealthy" after startup

**This is normal!** On first startup, services need 60-90 seconds to become healthy:
- **Qdrant**: Restores 21,747 documentation chunks from snapshot (~60 seconds)
- **Web app**: Loads sentence transformer embedding model (~80MB, ~30 seconds)

**Solution**:
```bash
# Watch the startup progress
docker-compose -f docker-compose-public.yml logs -f

# Wait for this message:
# "Uvicorn running on http://0.0.0.0:8080"

# Check status after 90 seconds
docker ps  # Should show "healthy" status
```

If containers still show "unhealthy" after 2 minutes, check logs for errors.

### Container Won't Start
```bash
# Check logs
docker logs clarion-web-app
docker logs clarion-qdrant

# Verify Docker Desktop is running
docker ps
```

### Can't Connect to Qdrant
```bash
# Restart both services
docker-compose -f docker-compose-public.yml restart

# Or restart individual service
docker restart clarion-qdrant
docker restart clarion-web-app
```

### API Key Not Saving
- Make sure you clicked "Save" after entering the key
- Check that the container has write permissions to `/app/.secrets`

---

## Documentation Coverage

The knowledge base includes all official Clarion documentation:

- **Core Language** (3 docs): Language Reference, Programming Guide, Learning Clarion
- **Libraries** (5 docs): ABC Library, Internet Builder, Business Math, File Driver, Report Writer
- **IDE & Development** (4 docs): IDE Reference, User Guide, Getting Started
- **Templates** (2 docs): Template Guide, Language Reference
- **Specialized** (4 docs): Database Drivers, XML Support, Report Writer, Application Broker
- **Advanced** (2 docs): Advanced topics and techniques
- **Utilities** (1 doc): Utilities and tools

**Total**: 21 manuals, 21,747 searchable chunks

---

## Technology Stack

- **FastAPI** - REST API framework
- **Qdrant** - Vector database for semantic search
- **Sentence Transformers** - Text embedding model
- **Docker** - Containerization
- **Multiple LLM Providers** - DeepSeek, OpenAI, Anthropic, Google, xAI, Ollama

---

## License

MIT License - See [LICENSE](LICENSE) file for details

---

## Support

- **Issues**: https://github.com/peterparker57/clarion-knowledge-base/issues
- **Discussions**: https://github.com/peterparker57/clarion-knowledge-base/discussions

---

## Related Projects

- **MCP Server**: Conversational interface for Claude Desktop/Code
- **Clarion Language**: https://www.clarioncentral.com/
