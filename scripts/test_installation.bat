@echo off
setlocal enabledelayedexpansion

REM #######################################################################
REM Test Script for Clarion Knowledge Base MCP Server Installation
REM For Windows
REM
REM This script verifies that the installation completed successfully
REM and all components are working correctly.
REM #######################################################################

chcp 65001 >nul

set "TESTS_PASSED=0"
set "TESTS_FAILED=0"

REM =====================================================================
REM Helper Functions
REM =====================================================================

:print_header
echo.
echo ================================================================
echo   %~1
echo ================================================================
echo.
goto :eof

:print_test
echo [94m▸ Testing: %~1[0m
goto :eof

:print_success
echo [92m  ✓ %~1[0m
set /a "TESTS_PASSED=!TESTS_PASSED! + 1"
goto :eof

:print_fail
echo [91m  ✗ %~1[0m
set /a "TESTS_FAILED=!TESTS_FAILED! + 1"
goto :eof

:print_warning
echo [93m  ⚠ %~1[0m
goto :eof

REM =====================================================================
REM Test Functions
REM =====================================================================

:test_docker
call :print_test "Docker daemon"
docker info >nul 2>&1
if not errorlevel 1 (
    call :print_success "Docker is running"
) else (
    call :print_fail "Docker is not running"
)
goto :eof

:test_containers
call :print_test "Docker containers"

REM Check Qdrant container
docker ps --format "{{.Names}}" | findstr "clarion-qdrant" >nul 2>&1
if not errorlevel 1 (
    call :print_success "Qdrant container is running"
) else (
    call :print_fail "Qdrant container is not running"
)

REM Check MCP server container
docker ps --format "{{.Names}}" | findstr "clarion-mcp-server" >nul 2>&1
if not errorlevel 1 (
    call :print_success "MCP server container is running"
) else (
    call :print_fail "MCP server container is not running"
)
goto :eof

:test_qdrant_health
call :print_test "Qdrant health"
curl -f http://localhost:6333/health >nul 2>&1
if not errorlevel 1 (
    call :print_success "Qdrant is healthy and responding"
) else (
    call :print_fail "Qdrant is not responding on port 6333"
)
goto :eof

:test_collection
call :print_test "Clarion docs collection"

for /f "delims=" %%i in ('curl -s http://localhost:6333/collections/clarion_docs 2^>nul') do set "response=%%i"
echo !response! | findstr "clarion_docs" >nul 2>&1
if not errorlevel 1 (
    REM Try to extract point count (basic parsing)
    call :print_success "Collection exists and is accessible"
) else (
    call :print_fail "Collection 'clarion_docs' not found"
)
goto :eof

:test_mcp_server
call :print_test "MCP server environment"

docker exec clarion-mcp-server python --version >nul 2>&1
if not errorlevel 1 (
    call :print_success "Python is available in MCP server"
) else (
    call :print_fail "Python not available in MCP server"
)

REM Test MCP server imports
docker exec clarion-mcp-server python -c "import sys; sys.path.insert(0, '/app'); from src import mcp_server" >nul 2>&1
if not errorlevel 1 (
    call :print_success "MCP server code is importable"
) else (
    call :print_fail "MCP server code cannot be imported"
)
goto :eof

:test_dependencies
call :print_test "Python dependencies"

REM Test qdrant_client
docker exec clarion-mcp-server python -c "import qdrant_client" >nul 2>&1
if not errorlevel 1 (
    call :print_success "qdrant_client is installed"
) else (
    call :print_fail "qdrant_client is not installed"
)

REM Test sentence_transformers
docker exec clarion-mcp-server python -c "import sentence_transformers" >nul 2>&1
if not errorlevel 1 (
    call :print_success "sentence_transformers is installed"
) else (
    call :print_fail "sentence_transformers is not installed"
)

REM Test mcp
docker exec clarion-mcp-server python -c "import mcp" >nul 2>&1
if not errorlevel 1 (
    call :print_success "mcp is installed"
) else (
    call :print_fail "mcp is not installed"
)
goto :eof

:test_claude_code_config
call :print_test "Claude Code configuration"

set "config_path=%USERPROFILE%\.claude.json"
if exist "!config_path!" (
    findstr "clarion-knowledge-base" "!config_path!" >nul 2>&1
    if not errorlevel 1 (
        call :print_success "Claude Code config contains MCP server"
    ) else (
        call :print_fail "Claude Code config missing MCP server entry"
    )
) else (
    call :print_warning "Claude Code config not found (may not be configured)"
)
goto :eof

:test_claude_desktop_config
call :print_test "Claude Desktop configuration"

set "config_path=%APPDATA%\Claude\claude_desktop_config.json"
if exist "!config_path!" (
    findstr "clarion-knowledge-base" "!config_path!" >nul 2>&1
    if not errorlevel 1 (
        call :print_success "Claude Desktop config contains MCP server"
    ) else (
        call :print_fail "Claude Desktop config missing MCP server entry"
    )
) else (
    call :print_warning "Claude Desktop config not found (may not be configured)"
)
goto :eof

:test_network
call :print_test "Container networking"

docker exec clarion-mcp-server curl -f http://qdrant:6333/health >nul 2>&1
if not errorlevel 1 (
    call :print_success "MCP server can reach Qdrant via Docker network"
) else (
    call :print_fail "MCP server cannot reach Qdrant"
)
goto :eof

:test_snapshot
call :print_test "Snapshot file"

if exist "qdrant-snapshot.tar.gz" (
    for %%A in ("qdrant-snapshot.tar.gz") do set "size=%%~zA"
    set /a "size_mb=!size! / 1024 / 1024"
    call :print_success "Snapshot file exists (!size_mb! MB)"
) else (
    call :print_warning "Snapshot file not found (may have been deleted after import)"
)
goto :eof

REM =====================================================================
REM Main Test Execution
REM =====================================================================

:main
cls
call :print_header "Clarion Knowledge Base - Installation Test"

echo Running diagnostic tests...
echo.

REM Run all tests
call :test_docker
call :test_containers
call :test_qdrant_health
call :test_collection
call :test_mcp_server
call :test_dependencies
call :test_network
call :test_claude_code_config
call :test_claude_desktop_config
call :test_snapshot

REM Summary
call :print_header "Test Summary"

set /a "total=!TESTS_PASSED! + !TESTS_FAILED!"
echo Total tests: !total!
echo [92mPassed: !TESTS_PASSED![0m
echo [91mFailed: !TESTS_FAILED![0m
echo.

if !TESTS_FAILED! EQU 0 (
    echo [92m✓ All critical tests passed![0m
    echo.
    echo Your Clarion Knowledge Base installation appears to be working correctly.
    echo.
    echo Next steps:
    echo   1. Restart Claude Code or Claude Desktop
    echo   2. Look for 'clarion-knowledge-base' in the MCP servers list
    echo   3. Try asking: 'Search the Clarion documentation for QUEUE'
    echo.
    exit /b 0
) else (
    echo [91m✗ Some tests failed[0m
    echo.
    echo Please check the errors above and:
    echo   1. Ensure Docker Desktop is running
    echo   2. Verify containers are started: docker-compose up -d
    echo   3. Check logs: docker-compose logs
    echo   4. Review INSTALLATION.md for troubleshooting
    echo.
    exit /b 1
)

:eof
endlocal
goto :main
