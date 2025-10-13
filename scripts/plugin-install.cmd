@echo off
REM Windows batch wrapper for Clarion Knowledge Base Plugin installation
REM This calls the PowerShell version of the installation script

echo Starting Clarion Knowledge Base installation...

REM Check if PowerShell is available
where pwsh >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    REM Use PowerShell Core if available
    pwsh -ExecutionPolicy Bypass -File "%~dp0plugin-install.ps1"
) else (
    REM Fall back to Windows PowerShell
    powershell -ExecutionPolicy Bypass -File "%~dp0plugin-install.ps1"
)

REM Exit with the same code as the PowerShell script
exit /b %ERRORLEVEL%
