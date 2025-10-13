Run the Clarion Knowledge Base setup and installation.

Usage: /clarion-setup

**IMPORTANT: Run this command after installing the plugin!**

This will:
1. Check Docker is running
2. Download the Qdrant snapshot (76 MB, one-time)
3. Build and start Docker containers
4. Import the vector database
5. Verify 21,747+ documents are indexed

After setup completes, restart Claude Code to enable the MCP server.

You can also use this command to restart containers after system reboot.
