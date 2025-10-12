#!/bin/bash

#######################################################################
# Test Script for Clarion Knowledge Base MCP Server Installation
#
# This script verifies that the installation completed successfully
# and all components are working correctly.
#######################################################################

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m'

# Test results
TESTS_PASSED=0
TESTS_FAILED=0

print_test() {
    echo -e "${BLUE}▸ Testing: $1${NC}"
}

print_success() {
    echo -e "${GREEN}  ✓ $1${NC}"
    TESTS_PASSED=$((TESTS_PASSED + 1))
}

print_fail() {
    echo -e "${RED}  ✗ $1${NC}"
    TESTS_FAILED=$((TESTS_FAILED + 1))
}

print_header() {
    echo ""
    echo -e "${CYAN}================================================================${NC}"
    echo -e "${CYAN}  $1${NC}"
    echo -e "${CYAN}================================================================${NC}"
    echo ""
}

# Test 1: Docker is running
test_docker() {
    print_test "Docker daemon"
    if docker info >/dev/null 2>&1; then
        print_success "Docker is running"
    else
        print_fail "Docker is not running"
    fi
}

# Test 2: Containers are running
test_containers() {
    print_test "Docker containers"

    # Check Qdrant container
    if docker ps --format '{{.Names}}' | grep -q "clarion-qdrant"; then
        print_success "Qdrant container is running"
    else
        print_fail "Qdrant container is not running"
    fi

    # Check MCP server container
    if docker ps --format '{{.Names}}' | grep -q "clarion-mcp-server"; then
        print_success "MCP server container is running"
    else
        print_fail "MCP server container is not running"
    fi
}

# Test 3: Qdrant health
test_qdrant_health() {
    print_test "Qdrant health"

    if curl -f http://localhost:6333/health >/dev/null 2>&1; then
        print_success "Qdrant is healthy and responding"
    else
        print_fail "Qdrant is not responding on port 6333"
    fi
}

# Test 4: Collection exists
test_collection() {
    print_test "Clarion docs collection"

    response=$(curl -s http://localhost:6333/collections/clarion_docs 2>/dev/null)
    if echo "$response" | grep -q "clarion_docs"; then
        # Get collection stats
        points=$(echo "$response" | grep -o '"points_count":[0-9]*' | cut -d':' -f2)
        if [ ! -z "$points" ] && [ "$points" -gt 0 ]; then
            print_success "Collection exists with $points points"
        else
            print_fail "Collection exists but appears empty"
        fi
    else
        print_fail "Collection 'clarion_docs' not found"
    fi
}

# Test 5: MCP server Python environment
test_mcp_server() {
    print_test "MCP server environment"

    if docker exec clarion-mcp-server python --version >/dev/null 2>&1; then
        print_success "Python is available in MCP server"
    else
        print_fail "Python not available in MCP server"
    fi

    # Test MCP server imports
    if docker exec clarion-mcp-server python -c "import sys; sys.path.insert(0, '/app'); from src import mcp_server" >/dev/null 2>&1; then
        print_success "MCP server code is importable"
    else
        print_fail "MCP server code cannot be imported"
    fi
}

# Test 6: Required dependencies
test_dependencies() {
    print_test "Python dependencies"

    deps=("qdrant_client" "sentence_transformers" "mcp")
    for dep in "${deps[@]}"; do
        if docker exec clarion-mcp-server python -c "import $dep" >/dev/null 2>&1; then
            print_success "$dep is installed"
        else
            print_fail "$dep is not installed"
        fi
    done
}

# Test 7: Claude Code config
test_claude_code_config() {
    print_test "Claude Code configuration"

    config_path="$HOME/.claude.json"
    if [ -f "$config_path" ]; then
        if grep -q "clarion-knowledge-base" "$config_path"; then
            print_success "Claude Code config contains MCP server"
        else
            print_fail "Claude Code config missing MCP server entry"
        fi
    else
        echo -e "${YELLOW}  ⚠ Claude Code config not found (may not be configured)${NC}"
    fi
}

# Test 8: Claude Desktop config
test_claude_desktop_config() {
    print_test "Claude Desktop configuration"

    # macOS path
    if [[ "$OSTYPE" == "darwin"* ]]; then
        config_path="$HOME/Library/Application Support/Claude/claude_desktop_config.json"
    # Linux path
    else
        config_path="$HOME/.config/Claude/claude_desktop_config.json"
    fi

    if [ -f "$config_path" ]; then
        if grep -q "clarion-knowledge-base" "$config_path"; then
            print_success "Claude Desktop config contains MCP server"
        else
            print_fail "Claude Desktop config missing MCP server entry"
        fi
    else
        echo -e "${YELLOW}  ⚠ Claude Desktop config not found (may not be configured)${NC}"
    fi
}

# Test 9: Network connectivity
test_network() {
    print_test "Container networking"

    if docker exec clarion-mcp-server curl -f http://qdrant:6333/health >/dev/null 2>&1; then
        print_success "MCP server can reach Qdrant via Docker network"
    else
        print_fail "MCP server cannot reach Qdrant"
    fi
}

# Test 10: Snapshot file
test_snapshot() {
    print_test "Snapshot file"

    if [ -f "qdrant-snapshot.tar.gz" ]; then
        size=$(stat -f%z "qdrant-snapshot.tar.gz" 2>/dev/null || stat -c%s "qdrant-snapshot.tar.gz" 2>/dev/null)
        size_mb=$((size / 1024 / 1024))
        print_success "Snapshot file exists ($size_mb MB)"
    else
        echo -e "${YELLOW}  ⚠ Snapshot file not found (may have been deleted after import)${NC}"
    fi
}

# Main test execution
main() {
    print_header "Clarion Knowledge Base - Installation Test"

    echo "Running diagnostic tests..."
    echo ""

    # Run all tests
    test_docker
    test_containers
    test_qdrant_health
    test_collection
    test_mcp_server
    test_dependencies
    test_network
    test_claude_code_config
    test_claude_desktop_config
    test_snapshot

    # Summary
    print_header "Test Summary"

    total=$((TESTS_PASSED + TESTS_FAILED))
    echo -e "Total tests: $total"
    echo -e "${GREEN}Passed: $TESTS_PASSED${NC}"
    echo -e "${RED}Failed: $TESTS_FAILED${NC}"
    echo ""

    if [ $TESTS_FAILED -eq 0 ]; then
        echo -e "${GREEN}✓ All critical tests passed!${NC}"
        echo ""
        echo "Your Clarion Knowledge Base installation appears to be working correctly."
        echo ""
        echo "Next steps:"
        echo "  1. Restart Claude Code or Claude Desktop"
        echo "  2. Look for 'clarion-knowledge-base' in the MCP servers list"
        echo "  3. Try asking: 'Search the Clarion documentation for QUEUE'"
        echo ""
        exit 0
    else
        echo -e "${RED}✗ Some tests failed${NC}"
        echo ""
        echo "Please check the errors above and:"
        echo "  1. Ensure Docker is running"
        echo "  2. Verify containers are started: docker-compose up -d"
        echo "  3. Check logs: docker-compose logs"
        echo "  4. Review INSTALLATION.md for troubleshooting"
        echo ""
        exit 1
    fi
}

# Run main
main
