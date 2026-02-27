#!/bin/bash
set -euo pipefail

# Only run in remote (Claude Code on the web) environments
if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

echo "Figma MCP (HTTP transport) is configured via https://mcp.figma.com/mcp"
echo "No additional dependencies required."
