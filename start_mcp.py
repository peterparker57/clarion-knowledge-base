"""
Wrapper script to start MCP server with correct Python path
"""
import sys
import os
from pathlib import Path

# Add src directory to Python path
project_root = Path(__file__).parent
src_dir = project_root / "src"
sys.path.insert(0, str(src_dir))

# Change to project directory
os.chdir(project_root)

# Import and run the server
from mcp_server import main
import asyncio

if __name__ == "__main__":
    asyncio.run(main())
