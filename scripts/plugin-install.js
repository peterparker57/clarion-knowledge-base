#!/usr/bin/env node
/**
 * Cross-platform installation script wrapper for Clarion Knowledge Base Plugin
 * Detects OS and runs the appropriate installation script
 */

const { spawn } = require('child_process');
const path = require('path');
const os = require('os');
const fs = require('fs');

const scriptDir = __dirname;
const platform = os.platform();

console.log('Clarion Knowledge Base - Plugin Installation');
console.log(`Detected platform: ${platform}`);
console.log('');

let command, args, scriptFile;

if (platform === 'win32') {
  // Windows: Use PowerShell
  scriptFile = path.join(scriptDir, 'plugin-install.ps1');

  // Check if PowerShell Core (pwsh) is available, otherwise use Windows PowerShell
  const pwshAvailable = tryCommand('pwsh', ['--version']);

  if (pwshAvailable) {
    command = 'pwsh';
  } else {
    command = 'powershell';
  }

  args = ['-ExecutionPolicy', 'Bypass', '-File', scriptFile];

} else {
  // Mac/Linux: Use bash
  scriptFile = path.join(scriptDir, 'plugin-install.sh');

  if (!fs.existsSync(scriptFile)) {
    console.error(`Error: Installation script not found: ${scriptFile}`);
    process.exit(1);
  }

  // Make sure script is executable
  try {
    fs.chmodSync(scriptFile, '755');
  } catch (err) {
    // Ignore chmod errors (might not have permission, but script might still work)
  }

  command = 'bash';
  args = [scriptFile];
}

console.log(`Running: ${command} ${args.join(' ')}\n`);

// Run the installation script
const child = spawn(command, args, {
  stdio: 'inherit',
  shell: true
});

child.on('error', (err) => {
  console.error(`Error running installation script: ${err.message}`);
  process.exit(1);
});

child.on('exit', (code) => {
  process.exit(code || 0);
});

/**
 * Check if a command is available
 */
function tryCommand(cmd, args) {
  try {
    require('child_process').execSync(`${cmd} ${args.join(' ')}`, {
      stdio: 'ignore',
      timeout: 5000
    });
    return true;
  } catch (err) {
    return false;
  }
}
