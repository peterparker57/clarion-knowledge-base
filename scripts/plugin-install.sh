#!/usr/bin/env bash
set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo "================================================================"
echo "  Clarion Knowledge Base - Plugin Installation"
echo "================================================================"

# 1. Check Docker
if ! command -v docker &> /dev/null; then
    echo -e "${RED}Error: Docker is not installed${NC}"
    echo "Please install Docker Desktop: https://www.docker.com/products/docker-desktop"
    exit 1
fi

if ! docker info &> /dev/null; then
    echo -e "${RED}Error: Docker is not running${NC}"
    echo "Please start Docker Desktop and try again"
    exit 1
fi

# 2. Get repository root
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
REPO_DIR="$( cd "$SCRIPT_DIR/.." && pwd )"
cd "$REPO_DIR"

# 3. Download snapshot if not exists
SNAPSHOT_FILE="qdrant-snapshot.tar.gz"
SNAPSHOT_URL="https://github.com/peterparker57/clarion-knowledge-base/releases/download/v1.0.0/qdrant-snapshot.tar.gz"

if [ ! -f "$SNAPSHOT_FILE" ]; then
    echo -e "${YELLOW}Downloading Qdrant snapshot (76 MB)...${NC}"
    if command -v curl &> /dev/null; then
        curl -L -o "$SNAPSHOT_FILE" "$SNAPSHOT_URL" --progress-bar
    elif command -v wget &> /dev/null; then
        wget -O "$SNAPSHOT_FILE" "$SNAPSHOT_URL"
    else
        echo -e "${RED}Error: Neither curl nor wget found${NC}"
        exit 1
    fi
    echo -e "${GREEN}✓ Snapshot downloaded${NC}"
else
    echo -e "${GREEN}✓ Snapshot already exists${NC}"
fi

# 4. Build Docker images
echo -e "${YELLOW}Building Docker images (this may take 3-5 minutes on first run)...${NC}"
docker-compose build
echo -e "${GREEN}✓ Images built${NC}"

# 5. Start containers
echo -e "${YELLOW}Starting Docker containers...${NC}"
docker-compose up -d
echo -e "${GREEN}✓ Containers started${NC}"

# 6. Wait for Qdrant to be healthy
echo -e "${YELLOW}Waiting for Qdrant to be ready...${NC}"
for i in {1..30}; do
    if docker exec clarion-mcp-server curl -s http://qdrant:6333/health &> /dev/null; then
        echo -e "${GREEN}✓ Qdrant is healthy${NC}"
        break
    fi
    if [ $i -eq 30 ]; then
        echo -e "${RED}Error: Qdrant failed to start${NC}"
        exit 1
    fi
    sleep 2
done

# 7. Import snapshot
echo -e "${YELLOW}Importing vector database...${NC}"
docker exec clarion-mcp-server python scripts/import_snapshot.py qdrant-snapshot.tar.gz
echo -e "${GREEN}✓ Database imported${NC}"

# 8. Verify collection
echo -e "${YELLOW}Verifying installation...${NC}"
POINT_COUNT=$(docker exec clarion-mcp-server python -c "
from qdrant_client import QdrantClient
client = QdrantClient(host='qdrant', port=6333)
collection = client.get_collection('clarion_docs')
print(collection.points_count)
")

if [ "$POINT_COUNT" -gt 20000 ]; then
    echo -e "${GREEN}✓ Verification successful: $POINT_COUNT documents indexed${NC}"
else
    echo -e "${RED}Error: Expected 21,747 documents, found $POINT_COUNT${NC}"
    exit 1
fi

echo ""
echo "================================================================"
echo -e "${GREEN}  Installation Complete!${NC}"
echo "================================================================"
echo ""
echo "The Clarion Knowledge Base MCP server is now running."
echo "Restart Claude Code to start using it."
echo ""
echo "Try asking: 'How do I create a browse procedure in Clarion?'"
echo ""
