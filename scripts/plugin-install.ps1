#!/usr/bin/env pwsh
# PowerShell installation script for Clarion Knowledge Base Plugin
# Compatible with PowerShell 5.1+ (Windows) and PowerShell Core 7+ (cross-platform)

$ErrorActionPreference = "Stop"

Write-Host "================================================================" -ForegroundColor Cyan
Write-Host "  Clarion Knowledge Base - Plugin Installation" -ForegroundColor Cyan
Write-Host "================================================================" -ForegroundColor Cyan
Write-Host ""

# 1. Check Docker
Write-Host "Checking Docker installation..." -ForegroundColor Yellow
if (!(Get-Command docker -ErrorAction SilentlyContinue)) {
    Write-Host "Error: Docker is not installed" -ForegroundColor Red
    Write-Host "Please install Docker Desktop: https://www.docker.com/products/docker-desktop"
    exit 1
}

Write-Host "Checking Docker daemon..." -ForegroundColor Yellow
try {
    docker info | Out-Null
} catch {
    Write-Host "Error: Docker is not running" -ForegroundColor Red
    Write-Host "Please start Docker Desktop and try again"
    exit 1
}

# 2. Get repository root
$ScriptDir = Split-Path -Parent $PSCommandPath
$RepoDir = Split-Path -Parent $ScriptDir
Set-Location $RepoDir
Write-Host "Working directory: $RepoDir" -ForegroundColor Gray

# 3. Download snapshot if not exists
$SnapshotFile = "qdrant-snapshot.tar.gz"
$SnapshotUrl = "https://github.com/peterparker57/clarion-knowledge-base/releases/download/v1.0.0/qdrant-snapshot.tar.gz"

if (!(Test-Path $SnapshotFile)) {
    Write-Host "Downloading Qdrant snapshot (76 MB)..." -ForegroundColor Yellow
    try {
        # Use curl if available (Windows 10+), otherwise use Invoke-WebRequest
        if (Get-Command curl -ErrorAction SilentlyContinue) {
            curl -L -o $SnapshotFile $SnapshotUrl --progress-bar
        } else {
            $ProgressPreference = 'SilentlyContinue'
            Invoke-WebRequest -Uri $SnapshotUrl -OutFile $SnapshotFile
            $ProgressPreference = 'Continue'
        }
        Write-Host "✓ Snapshot downloaded" -ForegroundColor Green
    } catch {
        Write-Host "Error downloading snapshot: $_" -ForegroundColor Red
        exit 1
    }
} else {
    Write-Host "✓ Snapshot already exists" -ForegroundColor Green
}

# 4. Build Docker images
Write-Host "Building Docker images (this may take 3-5 minutes on first run)..." -ForegroundColor Yellow
try {
    docker-compose build
    Write-Host "✓ Images built" -ForegroundColor Green
} catch {
    Write-Host "Error building images: $_" -ForegroundColor Red
    exit 1
}

# 5. Start containers
Write-Host "Starting Docker containers..." -ForegroundColor Yellow
try {
    docker-compose up -d
    Write-Host "✓ Containers started" -ForegroundColor Green
} catch {
    Write-Host "Error starting containers: $_" -ForegroundColor Red
    exit 1
}

# 6. Wait for Qdrant to be healthy
Write-Host "Waiting for Qdrant to be ready..." -ForegroundColor Yellow
$MaxAttempts = 30
$Attempt = 0
$QdrantReady = $false

while ($Attempt -lt $MaxAttempts) {
    $Attempt++
    try {
        $null = docker exec clarion-mcp-server curl -s http://qdrant:6333/health 2>&1
        if ($LASTEXITCODE -eq 0) {
            $QdrantReady = $true
            Write-Host "✓ Qdrant is healthy" -ForegroundColor Green
            break
        }
    } catch {
        # Continue waiting
    }

    if ($Attempt -eq $MaxAttempts) {
        Write-Host "Error: Qdrant failed to start within 60 seconds" -ForegroundColor Red
        exit 1
    }

    Start-Sleep -Seconds 2
}

# 7. Import snapshot
Write-Host "Importing vector database..." -ForegroundColor Yellow
try {
    docker exec clarion-mcp-server python scripts/import_snapshot.py qdrant-snapshot.tar.gz
    Write-Host "✓ Database imported" -ForegroundColor Green
} catch {
    Write-Host "Error importing database: $_" -ForegroundColor Red
    exit 1
}

# 8. Verify collection
Write-Host "Verifying installation..." -ForegroundColor Yellow
try {
    $VerifyScript = @"
from qdrant_client import QdrantClient
client = QdrantClient(host='qdrant', port=6333)
collection = client.get_collection('clarion_docs')
print(collection.points_count)
"@

    $PointCount = docker exec clarion-mcp-server python -c $VerifyScript
    $PointCount = [int]$PointCount.Trim()

    if ($PointCount -gt 20000) {
        Write-Host "✓ Verification successful: $PointCount documents indexed" -ForegroundColor Green
    } else {
        Write-Host "Error: Expected 21,747 documents, found $PointCount" -ForegroundColor Red
        exit 1
    }
} catch {
    Write-Host "Error verifying installation: $_" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "================================================================" -ForegroundColor Cyan
Write-Host "  Installation Complete!" -ForegroundColor Green
Write-Host "================================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "The Clarion Knowledge Base MCP server is now running." -ForegroundColor White
Write-Host "Restart Claude Code to start using it." -ForegroundColor White
Write-Host ""
Write-Host "Try asking: 'How do I create a browse procedure in Clarion?'" -ForegroundColor Cyan
Write-Host ""
