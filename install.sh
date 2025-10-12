#!/bin/bash

#######################################################################
# Clarion Knowledge Base MCP Server - Installation Script
# For Linux & macOS
#
# This script will:
# 1. Check prerequisites (Docker)
# 2. Download the Qdrant vector database snapshot
# 3. Start Docker containers
# 4. Import the vector database
# 5. Configure Claude Code and/or Claude Desktop
# 6. Verify the installation
#######################################################################

set -e  # Exit on error

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Configuration
SNAPSHOT_URL="https://github.com/peterparker57/clarion-knowledge-base/releases/download/v1.0.0/qdrant-snapshot.tar.gz"
SNAPSHOT_FILE="qdrant-snapshot.tar.gz"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Functions for colored output
print_header() {
    echo -e "${CYAN}================================================================${NC}"
    echo -e "${CYAN}  $1${NC}"
    echo -e "${CYAN}================================================================${NC}"
}

print_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

print_error() {
    echo -e "${RED}✗ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠ $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ $1${NC}"
}

print_step() {
    echo -e "${CYAN}▸ $1${NC}"
}

# Error handler
error_exit() {
    print_error "$1"
    echo ""
    print_info "Installation failed. Please check the error messages above."
    exit 1
}

# Check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check prerequisites
check_prerequisites() {
    print_step "Checking prerequisites..."

    # Check for Docker
    if ! command_exists docker; then
        error_exit "Docker is not installed. Please install Docker Desktop from https://www.docker.com/products/docker-desktop"
    fi
    print_success "Docker is installed"

    # Check if Docker daemon is running
    if ! docker info >/dev/null 2>&1; then
        error_exit "Docker daemon is not running. Please start Docker Desktop."
    fi
    print_success "Docker daemon is running"

    # Check for docker-compose or docker compose
    if ! command_exists docker-compose && ! docker compose version >/dev/null 2>&1; then
        error_exit "docker-compose is not available. Please install docker-compose or use Docker Desktop which includes it."
    fi
    print_success "docker-compose is available"

    # Check for curl (for downloading)
    if ! command_exists curl; then
        error_exit "curl is not installed. Please install curl (apt-get install curl / brew install curl)"
    fi
    print_success "curl is available"

    # Check for jq (for JSON manipulation)
    if ! command_exists jq; then
        print_warning "jq is not installed. Will use Python for JSON manipulation."
        USE_PYTHON_JSON=true
    else
        print_success "jq is available"
        USE_PYTHON_JSON=false
    fi

    echo ""
}

# Interactive prompt for Claude installation type
prompt_installation_type() {
    print_header "Installation Type Selection"
    echo ""
    echo "Which Claude client(s) do you want to configure?"
    echo ""
    echo "  1) Claude Code only"
    echo "  2) Claude Desktop only"
    echo "  3) Both Claude Code and Claude Desktop"
    echo ""

    while true; do
        read -p "Enter your choice (1-3): " choice
        case $choice in
            1)
                INSTALL_CLAUDE_CODE=true
                INSTALL_CLAUDE_DESKTOP=false
                print_success "Will configure Claude Code only"
                break
                ;;
            2)
                INSTALL_CLAUDE_CODE=false
                INSTALL_CLAUDE_DESKTOP=true
                print_success "Will configure Claude Desktop only"
                break
                ;;
            3)
                INSTALL_CLAUDE_CODE=true
                INSTALL_CLAUDE_DESKTOP=true
                print_success "Will configure both Claude Code and Claude Desktop"
                break
                ;;
            *)
                print_error "Invalid choice. Please enter 1, 2, or 3."
                ;;
        esac
    done
    echo ""
}

# Download snapshot
download_snapshot() {
    print_step "Downloading Qdrant vector database snapshot..."

    # Check if snapshot already exists
    if [ -f "$SCRIPT_DIR/$SNAPSHOT_FILE" ]; then
        print_warning "Snapshot file already exists."
        read -p "Do you want to re-download it? (y/n): " redownload
        if [[ ! "$redownload" =~ ^[Yy]$ ]]; then
            print_info "Using existing snapshot file."
            return 0
        fi
        rm -f "$SCRIPT_DIR/$SNAPSHOT_FILE"
    fi

    # Download with progress
    if ! curl -L -o "$SCRIPT_DIR/$SNAPSHOT_FILE" --progress-bar "$SNAPSHOT_URL"; then
        error_exit "Failed to download snapshot from $SNAPSHOT_URL"
    fi

    # Verify file was downloaded
    if [ ! -f "$SCRIPT_DIR/$SNAPSHOT_FILE" ]; then
        error_exit "Snapshot file not found after download"
    fi

    # Check file size (should be substantial)
    local file_size=$(stat -f%z "$SCRIPT_DIR/$SNAPSHOT_FILE" 2>/dev/null || stat -c%s "$SCRIPT_DIR/$SNAPSHOT_FILE" 2>/dev/null)
    local size_mb=$((file_size / 1024 / 1024))

    if [ $size_mb -lt 1 ]; then
        error_exit "Downloaded file seems too small ($size_mb MB). Download may have failed."
    fi

    print_success "Snapshot downloaded successfully ($size_mb MB)"
    echo ""
}

# Start Docker containers
start_docker_services() {
    print_step "Starting Docker containers..."

    cd "$SCRIPT_DIR"

    # Check if containers are already running
    if docker ps --format '{{.Names}}' | grep -q "clarion-qdrant"; then
        print_warning "Containers are already running."
        read -p "Do you want to restart them? (y/n): " restart
        if [[ "$restart" =~ ^[Yy]$ ]]; then
            print_info "Stopping existing containers..."
            docker-compose down || docker compose down
        else
            print_info "Using existing containers."
            return 0
        fi
    fi

    # Start containers
    print_info "Starting Qdrant and MCP server containers..."
    if docker-compose up -d 2>/dev/null || docker compose up -d 2>/dev/null; then
        print_success "Containers started"
    else
        error_exit "Failed to start Docker containers"
    fi

    # Wait for Qdrant to be healthy
    print_info "Waiting for Qdrant to be ready..."
    local max_wait=60
    local waited=0
    while [ $waited -lt $max_wait ]; do
        if docker exec clarion-qdrant curl -f http://localhost:6333/health >/dev/null 2>&1; then
            print_success "Qdrant is ready"
            echo ""
            return 0
        fi
        sleep 2
        waited=$((waited + 2))
        echo -n "."
    done

    echo ""
    error_exit "Qdrant failed to start within ${max_wait} seconds"
}

# Import snapshot
import_snapshot() {
    print_step "Importing vector database snapshot..."

    # Check if collection already exists
    if docker exec clarion-qdrant curl -s http://localhost:6333/collections/clarion_docs 2>/dev/null | grep -q "clarion_docs"; then
        print_warning "Collection 'clarion_docs' already exists."
        read -p "Do you want to re-import the snapshot? This will delete the existing collection. (y/n): " reimport
        if [[ ! "$reimport" =~ ^[Yy]$ ]]; then
            print_info "Skipping snapshot import."
            echo ""
            return 0
        fi
    fi

    # Copy snapshot to container
    print_info "Copying snapshot to MCP server container..."
    if ! docker cp "$SCRIPT_DIR/$SNAPSHOT_FILE" clarion-mcp-server:/app/qdrant-snapshot.tar.gz; then
        error_exit "Failed to copy snapshot to container"
    fi

    # Run import script
    print_info "Running import script (this may take a minute)..."
    if docker exec clarion-mcp-server python /app/scripts/import_snapshot.py /app/qdrant-snapshot.tar.gz; then
        print_success "Snapshot imported successfully"
    else
        error_exit "Failed to import snapshot"
    fi

    echo ""
}

# Detect Claude Code config path
detect_claude_code_path() {
    local config_path="$HOME/.claude.json"

    if [ -f "$config_path" ]; then
        echo "$config_path"
        return 0
    fi

    # If file doesn't exist, return the path anyway (we'll create it)
    echo "$config_path"
    return 0
}

# Detect Claude Desktop config path
detect_claude_desktop_path() {
    local config_path=""

    # macOS
    if [[ "$OSTYPE" == "darwin"* ]]; then
        config_path="$HOME/Library/Application Support/Claude/claude_desktop_config.json"
    # Linux
    else
        config_path="$HOME/.config/Claude/claude_desktop_config.json"
    fi

    if [ -f "$config_path" ]; then
        echo "$config_path"
        return 0
    fi

    # If file doesn't exist, return the path anyway (we'll create it)
    echo "$config_path"
    return 0
}

# Backup config file
backup_config() {
    local config_file="$1"

    if [ -f "$config_file" ]; then
        local backup_file="${config_file}.backup.$(date +%Y%m%d_%H%M%S)"
        cp "$config_file" "$backup_file"
        print_success "Backed up existing config to: $backup_file"
    fi
}

# Update config file using Python
update_config_python() {
    local config_file="$1"
    local config_dir=$(dirname "$config_file")

    # Create directory if it doesn't exist
    mkdir -p "$config_dir"

    # Create or update config using Python
    python3 <<EOF
import json
import os

config_file = "$config_file"
mcp_config = {
    "clarion-knowledge-base": {
        "command": "docker",
        "args": ["exec", "-i", "clarion-mcp-server", "python", "/app/src/mcp_server.py"]
    }
}

# Read existing config or create new one
if os.path.exists(config_file):
    with open(config_file, 'r') as f:
        try:
            config = json.load(f)
        except json.JSONDecodeError:
            config = {}
else:
    config = {}

# Add or update mcpServers section
if 'mcpServers' not in config:
    config['mcpServers'] = {}

config['mcpServers'].update(mcp_config)

# Write back
with open(config_file, 'w') as f:
    json.dump(config, f, indent=2)

print("Config updated successfully")
EOF
}

# Update config file using jq
update_config_jq() {
    local config_file="$1"
    local config_dir=$(dirname "$config_file")

    # Create directory if it doesn't exist
    mkdir -p "$config_dir"

    # Create config JSON
    local mcp_config='{"clarion-knowledge-base":{"command":"docker","args":["exec","-i","clarion-mcp-server","python","/app/src/mcp_server.py"]}}'

    # If file exists, merge with existing config
    if [ -f "$config_file" ]; then
        local temp_file=$(mktemp)
        jq --argjson mcp "$mcp_config" '.mcpServers += $mcp' "$config_file" > "$temp_file"
        mv "$temp_file" "$config_file"
    else
        # Create new config file
        echo "{\"mcpServers\":$mcp_config}" | jq '.' > "$config_file"
    fi
}

# Configure Claude Code
configure_claude_code() {
    print_step "Configuring Claude Code..."

    local config_path=$(detect_claude_code_path)
    print_info "Config path: $config_path"

    # Backup existing config
    backup_config "$config_path"

    # Update config
    if [ "$USE_PYTHON_JSON" = true ]; then
        update_config_python "$config_path"
    else
        update_config_jq "$config_path"
    fi

    if [ $? -eq 0 ]; then
        print_success "Claude Code configured successfully"
    else
        error_exit "Failed to configure Claude Code"
    fi

    echo ""
}

# Configure Claude Desktop
configure_claude_desktop() {
    print_step "Configuring Claude Desktop..."

    local config_path=$(detect_claude_desktop_path)
    print_info "Config path: $config_path"

    # Check if Claude Desktop is likely installed
    if [[ "$OSTYPE" == "darwin"* ]]; then
        if [ ! -d "/Applications/Claude.app" ]; then
            print_warning "Claude Desktop app not found at /Applications/Claude.app"
            read -p "Continue with configuration anyway? (y/n): " continue
            if [[ ! "$continue" =~ ^[Yy]$ ]]; then
                print_info "Skipping Claude Desktop configuration"
                echo ""
                return 0
            fi
        fi
    fi

    # Backup existing config
    backup_config "$config_path"

    # Update config
    if [ "$USE_PYTHON_JSON" = true ]; then
        update_config_python "$config_path"
    else
        update_config_jq "$config_path"
    fi

    if [ $? -eq 0 ]; then
        print_success "Claude Desktop configured successfully"
    else
        error_exit "Failed to configure Claude Desktop"
    fi

    echo ""
}

# Test MCP connection
test_mcp_connection() {
    print_step "Testing MCP server connection..."

    # Test by executing a simple Python import
    if docker exec clarion-mcp-server python -c "import sys; sys.path.insert(0, '/app'); from src.mcp_server import app; print('MCP server OK')" >/dev/null 2>&1; then
        print_success "MCP server is operational"
    else
        print_warning "Could not verify MCP server (this is normal, will work when called by Claude)"
    fi

    echo ""
}

# Print final instructions
print_final_instructions() {
    print_header "Installation Complete!"
    echo ""
    print_success "The Clarion Knowledge Base MCP server has been installed successfully!"
    echo ""
    print_info "What was configured:"

    if [ "$INSTALL_CLAUDE_CODE" = true ]; then
        echo "  • Claude Code config: $(detect_claude_code_path)"
    fi

    if [ "$INSTALL_CLAUDE_DESKTOP" = true ]; then
        echo "  • Claude Desktop config: $(detect_claude_desktop_path)"
    fi

    echo ""
    print_info "Next steps:"
    echo ""
    echo "  1. RESTART your Claude application(s):"

    if [ "$INSTALL_CLAUDE_CODE" = true ]; then
        echo "     • Claude Code: Close and reopen your terminal/IDE"
    fi

    if [ "$INSTALL_CLAUDE_DESKTOP" = true ]; then
        echo "     • Claude Desktop: Quit and restart the application"
    fi

    echo ""
    echo "  2. Verify the MCP server is available:"
    echo "     • Look for 'clarion-knowledge-base' in the MCP servers list"
    echo "     • Try asking: 'Search the Clarion documentation for QUEUE'"
    echo ""

    print_info "Docker containers running:"
    echo "     • clarion-qdrant (vector database)"
    echo "     • clarion-mcp-server (MCP server)"
    echo ""

    print_info "To manage containers:"
    echo "     • Stop:    docker-compose down"
    echo "     • Start:   docker-compose up -d"
    echo "     • Logs:    docker-compose logs -f"
    echo ""

    print_info "Troubleshooting:"
    echo "     • Check container status: docker ps"
    echo "     • View logs: docker logs clarion-mcp-server"
    echo "     • Re-run this script if needed (safe to run multiple times)"
    echo ""

    print_success "Happy coding with Clarion!"
    echo ""
}

# Main installation process
main() {
    clear
    print_header "Clarion Knowledge Base MCP Server - Installer"
    echo ""
    print_info "This script will install and configure the Clarion Knowledge Base MCP server."
    print_info "Installation directory: $SCRIPT_DIR"
    echo ""

    # Step 1: Check prerequisites
    check_prerequisites

    # Step 2: Prompt for installation type
    prompt_installation_type

    # Step 3: Download snapshot
    download_snapshot

    # Step 4: Start Docker services
    start_docker_services

    # Step 5: Import snapshot
    import_snapshot

    # Step 6: Configure Claude Code
    if [ "$INSTALL_CLAUDE_CODE" = true ]; then
        configure_claude_code
    fi

    # Step 7: Configure Claude Desktop
    if [ "$INSTALL_CLAUDE_DESKTOP" = true ]; then
        configure_claude_desktop
    fi

    # Step 8: Test connection
    test_mcp_connection

    # Step 9: Print final instructions
    print_final_instructions
}

# Run main installation
main
