# Utility MCP Server

A [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) server that exposes utility tools for math operations, text processing, date/time handling, and **Figma API** integration.

## Tools

### Math
| Tool | Description |
|------|-------------|
| `add(a, b)` | Add two numbers |
| `subtract(a, b)` | Subtract b from a |
| `multiply(a, b)` | Multiply two numbers |
| `divide(a, b)` | Divide a by b |

### Text
| Tool | Description |
|------|-------------|
| `word_count(text)` | Count words, characters, and lines |
| `reverse_text(text)` | Reverse a string |
| `to_uppercase(text)` | Convert to uppercase |
| `to_lowercase(text)` | Convert to lowercase |

### Date & Time
| Tool | Description |
|------|-------------|
| `current_datetime()` | Return current date/time in multiple formats |
| `format_datetime(timestamp, fmt)` | Format a Unix timestamp |

### Figma
| Tool | Description |
|------|-------------|
| `figma_whoami()` | Return info about the authenticated Figma user |
| `figma_get_file(file_key)` | Fetch a Figma file's metadata and document tree |
| `figma_get_node(file_key, node_id)` | Fetch a specific node from a Figma file |
| `figma_get_comments(file_key)` | List all comments on a Figma file |
| `figma_get_images(file_key, node_ids, scale, fmt)` | Export node images (png/jpg/svg/pdf) |
| `figma_get_components(file_key)` | List all published components in a Figma file |

## Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Copy `.env.example` to `.env` and fill in your Figma API key:

```bash
cp .env.example .env
# then edit .env and set FIGMA_API_KEY=<your key>
```

You can generate a Figma personal access token at:
**Figma → Account Settings → Security → Personal access tokens**

## Running the server

```bash
python server.py
```

The server runs over stdio by default, which is compatible with MCP clients such as Claude Desktop.

## Claude Desktop configuration

Add the following to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "utility": {
      "command": "python",
      "args": ["/path/to/server.py"]
    }
  }
}
```
