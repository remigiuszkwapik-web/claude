#!/bin/bash
set -euo pipefail

# Only run in remote (Claude Code on the web) environments
if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

echo "Setting up Figma MCP environment..."

# Ensure Node.js and npx are available
if ! command -v node &> /dev/null; then
  echo "ERROR: Node.js is not installed. Figma MCP requires Node.js."
  exit 1
fi

if ! command -v npx &> /dev/null; then
  echo "ERROR: npx is not available. Figma MCP requires npx."
  exit 1
fi

echo "Node.js version: $(node --version)"
echo "npm version: $(npm --version)"

# Pre-cache the Figma MCP server package so it's available during the session
# This avoids download latency when the MCP server is first invoked
echo "Caching @figma/mcp package..."
npm install -g @figma/mcp 2>/dev/null || true

echo "Figma MCP environment setup complete."
