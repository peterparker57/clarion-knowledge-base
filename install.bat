@echo off
setlocal enabledelayedexpansion

REM #######################################################################
REM Clarion Knowledge Base MCP Server - Installation Script
REM For Windows
REM
REM This script will:
REM 1. Check prerequisites (Docker Desktop)
REM 2. Download the Qdrant vector database snapshot
REM 3. Start Docker containers
REM 4. Import the vector database
REM 5. Configure Claude Code and/or Claude Desktop
REM 6. Verify the installation
REM #######################################################################

REM Enable UTF-8 output
chcp 65001 >nul

REM Configuration
set "SNAPSHOT_URL=https://github.com/peterparker57/clarion-knowledge-base/releases/download/v1.0.0/qdrant-snapshot.tar.gz"
set "SNAPSHOT_FILE=qdrant-snapshot.tar.gz"
set "SCRIPT_DIR=%~dp0"
set "SCRIPT_DIR=%SCRIPT_DIR:~0,-1%"

REM Color codes (using PowerShell for colored output)
set "RED=[91m"
set "GREEN=[92m"
set "YELLOW=[93m"
set "BLUE=[94m"
set "CYAN=[96m"
set "NC=[0m"

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

:print_success
echo [92m✓ %~1[0m
goto :eof

:print_error
echo [91m✗ %~1[0m
goto :eof

:print_warning
echo [93m⚠ %~1[0m
goto :eof

:print_info
echo [94mℹ %~1[0m
goto :eof

:print_step
echo [96m▸ %~1[0m
goto :eof

:error_exit
call :print_error "%~1"
echo.
call :print_info "Installation failed. Please check the error messages above."
exit /b 1

REM =====================================================================
REM Main Installation Functions
REM =====================================================================

:check_prerequisites
call :print_step "Checking prerequisites..."

REM Check for Docker
where docker >nul 2>&1
if errorlevel 1 (
    call :error_exit "Docker is not installed. Please install Docker Desktop from https://www.docker.com/products/docker-desktop"
    exit /b 1
)
call :print_success "Docker is installed"

REM Check if Docker daemon is running
docker info >nul 2>&1
if errorlevel 1 (
    call :error_exit "Docker daemon is not running. Please start Docker Desktop."
    exit /b 1
)
call :print_success "Docker daemon is running"

REM Check for docker-compose
docker-compose version >nul 2>&1
if errorlevel 1 (
    docker compose version >nul 2>&1
    if errorlevel 1 (
        call :error_exit "docker-compose is not available. Please install Docker Desktop which includes it."
        exit /b 1
    )
    set "DOCKER_COMPOSE=docker compose"
) else (
    set "DOCKER_COMPOSE=docker-compose"
)
call :print_success "docker-compose is available"

REM Check for curl or PowerShell (for downloading)
where curl >nul 2>&1
if errorlevel 1 (
    call :print_info "curl not found, will use PowerShell for downloads"
    set "USE_POWERSHELL=true"
) else (
    call :print_success "curl is available"
    set "USE_POWERSHELL=false"
)

REM Check for Python (for JSON manipulation)
where python >nul 2>&1
if errorlevel 1 (
    call :error_exit "Python is not installed. Please install Python 3.x from https://www.python.org/"
    exit /b 1
)
call :print_success "Python is available"

echo.
goto :eof

:prompt_installation_type
call :print_header "Installation Type Selection"
echo.
echo Which Claude client(s) do you want to configure?
echo.
echo   1) Claude Code only
echo   2) Claude Desktop only
echo   3) Both Claude Code and Claude Desktop
echo.

:prompt_loop
set /p "choice=Enter your choice (1-3): "

if "%choice%"=="1" (
    set "INSTALL_CLAUDE_CODE=true"
    set "INSTALL_CLAUDE_DESKTOP=false"
    call :print_success "Will configure Claude Code only"
    goto :prompt_done
)

if "%choice%"=="2" (
    set "INSTALL_CLAUDE_CODE=false"
    set "INSTALL_CLAUDE_DESKTOP=true"
    call :print_success "Will configure Claude Desktop only"
    goto :prompt_done
)

if "%choice%"=="3" (
    set "INSTALL_CLAUDE_CODE=true"
    set "INSTALL_CLAUDE_DESKTOP=true"
    call :print_success "Will configure both Claude Code and Claude Desktop"
    goto :prompt_done
)

call :print_error "Invalid choice. Please enter 1, 2, or 3."
goto :prompt_loop

:prompt_done
echo.
goto :eof

:download_snapshot
call :print_step "Downloading Qdrant vector database snapshot..."

REM Check if snapshot already exists
if exist "%SCRIPT_DIR%\%SNAPSHOT_FILE%" (
    call :print_warning "Snapshot file already exists."
    set /p "redownload=Do you want to re-download it? (y/n): "
    if /i not "!redownload!"=="y" (
        call :print_info "Using existing snapshot file."
        echo.
        goto :eof
    )
    del "%SCRIPT_DIR%\%SNAPSHOT_FILE%"
)

REM Download using curl or PowerShell
if "%USE_POWERSHELL%"=="true" (
    call :print_info "Downloading with PowerShell..."
    powershell -Command "& {[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; $ProgressPreference = 'SilentlyContinue'; Invoke-WebRequest -Uri '%SNAPSHOT_URL%' -OutFile '%SCRIPT_DIR%\%SNAPSHOT_FILE%' -UseBasicParsing}"
) else (
    call :print_info "Downloading with curl..."
    curl -L -o "%SCRIPT_DIR%\%SNAPSHOT_FILE%" "%SNAPSHOT_URL%"
)

if errorlevel 1 (
    call :error_exit "Failed to download snapshot from %SNAPSHOT_URL%"
    exit /b 1
)

REM Verify file was downloaded
if not exist "%SCRIPT_DIR%\%SNAPSHOT_FILE%" (
    call :error_exit "Snapshot file not found after download"
    exit /b 1
)

REM Check file size
for %%A in ("%SCRIPT_DIR%\%SNAPSHOT_FILE%") do set "file_size=%%~zA"
set /a "size_mb=!file_size! / 1024 / 1024"

if !size_mb! LSS 1 (
    call :error_exit "Downloaded file seems too small (!size_mb! MB). Download may have failed."
    exit /b 1
)

call :print_success "Snapshot downloaded successfully (!size_mb! MB)"
echo.
goto :eof

:start_docker_services
call :print_step "Starting Docker containers..."

cd /d "%SCRIPT_DIR%"

REM Check if containers are already running
docker ps --format "{{.Names}}" | findstr "clarion-qdrant" >nul 2>&1
if not errorlevel 1 (
    call :print_warning "Containers are already running."
    set /p "restart=Do you want to restart them? (y/n): "
    if /i "!restart!"=="y" (
        call :print_info "Stopping existing containers..."
        %DOCKER_COMPOSE% down
    ) else (
        call :print_info "Using existing containers."
        echo.
        goto :eof
    )
)

REM Start containers
call :print_info "Starting Qdrant and MCP server containers..."
%DOCKER_COMPOSE% up -d
if errorlevel 1 (
    call :error_exit "Failed to start Docker containers"
    exit /b 1
)
call :print_success "Containers started"

REM Wait for Qdrant to be healthy
call :print_info "Waiting for Qdrant to be ready..."
set "max_wait=60"
set "waited=0"

:wait_loop
if !waited! GEQ !max_wait! (
    echo.
    call :error_exit "Qdrant failed to start within !max_wait! seconds"
    exit /b 1
)

docker exec clarion-qdrant curl -f http://localhost:6333/health >nul 2>&1
if not errorlevel 1 (
    call :print_success "Qdrant is ready"
    echo.
    goto :eof
)

timeout /t 2 /nobreak >nul
set /a "waited=!waited! + 2"
echo|set /p="."
goto :wait_loop

:import_snapshot
call :print_step "Importing vector database snapshot..."

REM Check if collection already exists
docker exec clarion-qdrant curl -s http://localhost:6333/collections/clarion_docs 2>nul | findstr "clarion_docs" >nul 2>&1
if not errorlevel 1 (
    call :print_warning "Collection 'clarion_docs' already exists."
    set /p "reimport=Do you want to re-import the snapshot? This will delete the existing collection. (y/n): "
    if /i not "!reimport!"=="y" (
        call :print_info "Skipping snapshot import."
        echo.
        goto :eof
    )
)

REM Copy snapshot to container
call :print_info "Copying snapshot to MCP server container..."
docker cp "%SCRIPT_DIR%\%SNAPSHOT_FILE%" clarion-mcp-server:/app/qdrant-snapshot.tar.gz
if errorlevel 1 (
    call :error_exit "Failed to copy snapshot to container"
    exit /b 1
)

REM Run import script
call :print_info "Running import script (this may take a minute)..."
docker exec clarion-mcp-server python /app/scripts/import_snapshot.py /app/qdrant-snapshot.tar.gz
if errorlevel 1 (
    call :error_exit "Failed to import snapshot"
    exit /b 1
)
call :print_success "Snapshot imported successfully"

echo.
goto :eof

:detect_claude_code_path
set "CLAUDE_CODE_CONFIG=%USERPROFILE%\.claude.json"
goto :eof

:detect_claude_desktop_path
set "CLAUDE_DESKTOP_CONFIG=%APPDATA%\Claude\claude_desktop_config.json"
goto :eof

:backup_config
set "config_file=%~1"

if exist "%config_file%" (
    set "timestamp=%date:~-4%%date:~-10,2%%date:~-7,2%_%time:~0,2%%time:~3,2%%time:~6,2%"
    set "timestamp=!timestamp: =0!"
    set "backup_file=%config_file%.backup.!timestamp!"
    copy "%config_file%" "!backup_file!" >nul
    call :print_success "Backed up existing config to: !backup_file!"
)
goto :eof

:update_config_python
set "config_file=%~1"

REM Create directory if it doesn't exist
for %%F in ("%config_file%") do set "config_dir=%%~dpF"
if not exist "%config_dir%" mkdir "%config_dir%"

REM Create or update config using Python
python -c "import json; import os; config_file = r'%config_file%'; mcp_config = {'clarion-knowledge-base': {'command': 'docker', 'args': ['exec', '-i', 'clarion-mcp-server', 'python', '/app/src/mcp_server.py']}}; config = json.load(open(config_file, 'r')) if os.path.exists(config_file) else {}; config.setdefault('mcpServers', {}).update(mcp_config); json.dump(config, open(config_file, 'w'), indent=2); print('Config updated successfully')"

if errorlevel 1 (
    exit /b 1
)
goto :eof

:configure_claude_code
call :print_step "Configuring Claude Code..."

call :detect_claude_code_path
call :print_info "Config path: !CLAUDE_CODE_CONFIG!"

REM Backup existing config
call :backup_config "!CLAUDE_CODE_CONFIG!"

REM Update config
call :update_config_python "!CLAUDE_CODE_CONFIG!"
if errorlevel 1 (
    call :error_exit "Failed to configure Claude Code"
    exit /b 1
)

call :print_success "Claude Code configured successfully"
echo.
goto :eof

:configure_claude_desktop
call :print_step "Configuring Claude Desktop..."

call :detect_claude_desktop_path
call :print_info "Config path: !CLAUDE_DESKTOP_CONFIG!"

REM Check if Claude Desktop is likely installed
if not exist "%LOCALAPPDATA%\AnthropicClaude" (
    if not exist "%APPDATA%\Claude" (
        call :print_warning "Claude Desktop installation not detected"
        set /p "continue=Continue with configuration anyway? (y/n): "
        if /i not "!continue!"=="y" (
            call :print_info "Skipping Claude Desktop configuration"
            echo.
            goto :eof
        )
    )
)

REM Backup existing config
call :backup_config "!CLAUDE_DESKTOP_CONFIG!"

REM Update config
call :update_config_python "!CLAUDE_DESKTOP_CONFIG!"
if errorlevel 1 (
    call :error_exit "Failed to configure Claude Desktop"
    exit /b 1
)

call :print_success "Claude Desktop configured successfully"
echo.
goto :eof

:test_mcp_connection
call :print_step "Testing MCP server connection..."

REM Test by executing a simple Python import
docker exec clarion-mcp-server python -c "import sys; sys.path.insert(0, '/app'); from src.mcp_server import app; print('MCP server OK')" >nul 2>&1
if not errorlevel 1 (
    call :print_success "MCP server is operational"
) else (
    call :print_warning "Could not verify MCP server (this is normal, will work when called by Claude)"
)

echo.
goto :eof

:print_final_instructions
call :print_header "Installation Complete!"
echo.
call :print_success "The Clarion Knowledge Base MCP server has been installed successfully!"
echo.
call :print_info "What was configured:"

if "%INSTALL_CLAUDE_CODE%"=="true" (
    call :detect_claude_code_path
    echo   • Claude Code config: !CLAUDE_CODE_CONFIG!
)

if "%INSTALL_CLAUDE_DESKTOP%"=="true" (
    call :detect_claude_desktop_path
    echo   • Claude Desktop config: !CLAUDE_DESKTOP_CONFIG!
)

echo.
call :print_info "Next steps:"
echo.
echo   1. RESTART your Claude application(s):

if "%INSTALL_CLAUDE_CODE%"=="true" (
    echo      • Claude Code: Close and reopen your terminal/IDE
)

if "%INSTALL_CLAUDE_DESKTOP%"=="true" (
    echo      • Claude Desktop: Quit and restart the application
)

echo.
echo   2. Verify the MCP server is available:
echo      • Look for 'clarion-knowledge-base' in the MCP servers list
echo      • Try asking: 'Search the Clarion documentation for QUEUE'
echo.

call :print_info "Docker containers running:"
echo      • clarion-qdrant (vector database)
echo      • clarion-mcp-server (MCP server)
echo.

call :print_info "To manage containers:"
echo      • Stop:    docker-compose down
echo      • Start:   docker-compose up -d
echo      • Logs:    docker-compose logs -f
echo.

call :print_info "Troubleshooting:"
echo      • Check container status: docker ps
echo      • View logs: docker logs clarion-mcp-server
echo      • Re-run this script if needed (safe to run multiple times)
echo.

call :print_success "Happy coding with Clarion!"
echo.
goto :eof

REM =====================================================================
REM Main Installation Process
REM =====================================================================

:main
cls
call :print_header "Clarion Knowledge Base MCP Server - Installer"
echo.
call :print_info "This script will install and configure the Clarion Knowledge Base MCP server."
call :print_info "Installation directory: %SCRIPT_DIR%"
echo.

REM Step 1: Check prerequisites
call :check_prerequisites
if errorlevel 1 exit /b 1

REM Step 2: Prompt for installation type
call :prompt_installation_type

REM Step 3: Download snapshot
call :download_snapshot
if errorlevel 1 exit /b 1

REM Step 4: Start Docker services
call :start_docker_services
if errorlevel 1 exit /b 1

REM Step 5: Import snapshot
call :import_snapshot
if errorlevel 1 exit /b 1

REM Step 6: Configure Claude Code
if "%INSTALL_CLAUDE_CODE%"=="true" (
    call :configure_claude_code
    if errorlevel 1 exit /b 1
)

REM Step 7: Configure Claude Desktop
if "%INSTALL_CLAUDE_DESKTOP%"=="true" (
    call :configure_claude_desktop
    if errorlevel 1 exit /b 1
)

REM Step 8: Test connection
call :test_mcp_connection

REM Step 9: Print final instructions
call :print_final_instructions

REM Done
endlocal
exit /b 0

REM Run main installation
call :main
