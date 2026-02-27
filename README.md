# Utility MCP Server

A [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) server that exposes utility tools for math operations, text processing, and date/time handling.

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

## Setup

```bash
pip install -r requirements.txt
```

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
