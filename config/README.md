# Configuration Templates

This directory contains example configuration files for connecting Claude clients (Code and Desktop) to the Clarion Knowledge Base MCP server.

## Overview

Both Claude Code and Claude Desktop use identical Docker-based configuration to access the MCP server. The configuration tells the Claude client how to communicate with the Clarion Knowledge Base server running in a Docker container.

## Configuration Files

### `claude_code_example.json`
Template configuration for Claude Code (CLI).

### `claude_desktop_example.json`
Template configuration for Claude Desktop (GUI application).

**Note:** Both files contain identical configuration - the Docker command works for both clients.

## Configuration Structure

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

### What This Configuration Does

- **Server Name:** `clarion-knowledge-base` - The identifier for this MCP server
- **Command:** `docker` - Uses Docker to execute the server
- **Args:** Runs the MCP server Python script inside the `clarion-mcp-server` container
- **Communication:** Uses stdin/stdout for MCP protocol communication

## Installation Locations

### Claude Code Configuration

The configuration file location varies by operating system:

#### Windows
```
%USERPROFILE%\.claude.json
```
Typically: `C:\Users\YourUsername\.claude.json`

#### macOS
```
~/.claude.json
```
Typically: `/Users/YourUsername/.claude.json`

#### Linux
```
~/.claude.json
```
Typically: `/home/YourUsername/.claude.json`

### Claude Desktop Configuration

The configuration file location varies by operating system:

#### Windows
```
%APPDATA%\Claude\claude_desktop_config.json
```
Typically: `C:\Users\YourUsername\AppData\Roaming\Claude\claude_desktop_config.json`

#### macOS
```
~/Library/Application Support/Claude/claude_desktop_config.json
```
Typically: `/Users/YourUsername/Library/Application Support/Claude/claude_desktop_config.json`

#### Linux
```
~/.config/Claude/claude_desktop_config.json
```
Typically: `/home/YourUsername/.config/Claude/claude_desktop_config.json`

## Manual Installation Instructions

If the automated installation script doesn't work, you can manually configure the clients:

### Prerequisites

1. **Docker must be running** with the Clarion Knowledge Base containers started:
   ```bash
   cd /path/to/ClarionAI
   docker-compose up -d
   ```

2. **Verify containers are running:**
   ```bash
   docker ps
   ```
   You should see both `clarion-qdrant` and `clarion-mcp-server` containers.

### For Claude Code

1. **Locate or create the configuration file:**
   - Windows: `%USERPROFILE%\.claude.json`
   - macOS/Linux: `~/.claude.json`

2. **Copy the content** from `claude_code_example.json`

3. **If the file already exists** and has other MCP servers, merge the configuration:
   ```json
   {
     "mcpServers": {
       "existing-server": {
         "command": "...",
         "args": [...]
       },
       "clarion-knowledge-base": {
         "command": "docker",
         "args": ["exec", "-i", "clarion-mcp-server", "python", "/app/src/mcp_server.py"]
       }
     }
   }
   ```

4. **Save the file** and restart Claude Code

### For Claude Desktop

1. **Locate or create the configuration file:**
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Linux: `~/.config/Claude/claude_desktop_config.json`

2. **Create the directory if it doesn't exist:**
   - Windows: `mkdir "%APPDATA%\Claude"` (if needed)
   - macOS: `mkdir -p ~/Library/Application\ Support/Claude`
   - Linux: `mkdir -p ~/.config/Claude`

3. **Copy the content** from `claude_desktop_example.json`

4. **If the file already exists** and has other MCP servers, merge the configuration as shown above

5. **Save the file** and restart Claude Desktop

## How the Installation Script Uses These Files

The automated installation scripts (`install.sh` and `install.bat`) use these templates to:

1. Detect which Claude client(s) you have installed
2. Find the correct configuration file location for your OS
3. Merge or create the configuration automatically
4. Verify the Docker containers are running
5. Test the MCP connection

## Verifying the Configuration

### Check Docker Containers

```bash
# Verify containers are running
docker ps

# Should show:
# - clarion-qdrant (Qdrant vector database)
# - clarion-mcp-server (MCP server)
```

### Test the MCP Server Manually

```bash
# Test direct communication with the MCP server
docker exec -i clarion-mcp-server python /app/src/mcp_server.py
# Press Ctrl+C to exit
```

If this command waits for input, the server is working correctly.

### Check in Claude Code

After configuration:
1. Start Claude Code
2. Run: `/mcp` or check MCP servers list
3. You should see "clarion-knowledge-base" listed
4. Try a test query: "Search Clarion docs for QUEUE definition"

### Check in Claude Desktop

After configuration:
1. Restart Claude Desktop completely
2. Look for the MCP server indicator in the interface
3. Try asking: "Can you search the Clarion documentation for information about QUEUE structures?"

## Troubleshooting

### Docker Container Not Running

**Symptom:** Configuration is correct but connection fails

**Solution:**
```bash
# Check container status
docker ps -a | grep clarion

# If stopped, start them
cd /path/to/ClarionAI
docker-compose up -d

# Check logs if issues persist
docker logs clarion-mcp-server
```

### Configuration File Not Found

**Symptom:** Can't locate the configuration file

**Solution:**
- **Windows:** Open PowerShell and run: `echo $env:USERPROFILE` (Code) or `echo $env:APPDATA` (Desktop)
- **macOS/Linux:** Run: `echo ~` and navigate from there

### Permission Denied

**Symptom:** Can't write to configuration file

**Solution:**
- **Windows:** Run editor as Administrator
- **macOS/Linux:** Check file permissions with `ls -la` and adjust if needed

### MCP Server Not Appearing

**Symptom:** Configuration saved but server doesn't show up

**Solution:**
1. Verify JSON syntax is valid (use a JSON validator)
2. Ensure no extra commas or missing brackets
3. Restart the client completely (not just refresh)
4. Check client logs for error messages

### Multiple MCP Servers Conflict

**Symptom:** Other MCP servers stop working after adding Clarion

**Solution:**
- Ensure proper JSON syntax with commas between server entries
- Each server should be a separate entry in the `mcpServers` object
- Validate the entire JSON file structure

## Docker-Based vs. Local Python Setup

### Why Docker?

The Docker-based configuration offers several advantages:

1. **No local Python setup required** by end users
2. **Consistent environment** across all platforms
3. **Isolated dependencies** - no conflicts with other Python projects
4. **Easy updates** - just pull new Docker images
5. **Automatic networking** between MCP server and Qdrant database

### Traditional Setup (Alternative)

If you prefer not to use Docker, you can configure a local Python installation:

```json
{
  "mcpServers": {
    "clarion-knowledge-base": {
      "command": "/path/to/python",
      "args": ["/path/to/ClarionAI/src/mcp_server.py"],
      "env": {
        "QDRANT_HOST": "localhost",
        "QDRANT_PORT": "6333"
      }
    }
  }
}
```

**Requirements for local setup:**
- Python 3.13+
- Virtual environment with all dependencies installed
- Qdrant running locally on port 6333
- Absolute paths to Python interpreter and script

**Note:** The Docker setup is recommended for easier installation and maintenance.

## Platform-Specific Notes

### Windows

- Use forward slashes OR double backslashes in JSON paths
- PowerShell can help locate config directories
- Windows Defender may scan Docker containers on first run

### macOS

- Claude Desktop config is in `Application Support` (hidden by default)
- Use Finder > Go > Go to Folder to navigate to hidden directories
- May need to grant Terminal permissions to access Claude config

### Linux

- Configuration typically in `~/.config/Claude/`
- Check your distribution's snap/flatpak directories if using containerized Claude Desktop
- Ensure Docker daemon is running: `sudo systemctl status docker`

## Additional Resources

- **Full Documentation:** See `documentation/index.html`
- **Project README:** See root `README.md`
- **Docker Compose:** See `docker-compose.yml` for container details
- **MCP Server Code:** See `src/mcp_server.py`

## Getting Help

If you encounter issues:

1. Check the troubleshooting section above
2. Verify Docker containers are running
3. Validate JSON syntax in configuration files
4. Check client logs for specific error messages
5. Review the full documentation at `documentation/index.html`

## Updates and Maintenance

When updating the Clarion Knowledge Base:

1. Pull the latest changes from the repository
2. Restart Docker containers: `docker-compose restart`
3. Configuration files typically don't need changes
4. Client restart may be required after container updates

---

**Last Updated:** October 2025
**Version:** 1.0
