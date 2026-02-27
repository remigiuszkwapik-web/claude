"""
MCP Server implementation providing utility tools and Figma API integration.
"""

import os
from datetime import datetime

import httpx
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

load_dotenv()

FIGMA_API_KEY = os.getenv("FIGMA_API_KEY")
FIGMA_BASE_URL = "https://api.figma.com/v1"

mcp = FastMCP("Utility MCP Server")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _figma_headers() -> dict:
    if not FIGMA_API_KEY:
        raise RuntimeError("FIGMA_API_KEY is not set. Add it to your .env file.")
    return {"X-Figma-Token": FIGMA_API_KEY}


def _figma_get(path: str) -> dict:
    url = f"{FIGMA_BASE_URL}{path}"
    with httpx.Client(timeout=15) as client:
        response = client.get(url, headers=_figma_headers())
    response.raise_for_status()
    return response.json()


# ---------------------------------------------------------------------------
# Math tools
# ---------------------------------------------------------------------------

@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers together."""
    return a + b


@mcp.tool()
def subtract(a: float, b: float) -> float:
    """Subtract b from a."""
    return a - b


@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers together."""
    return a * b


@mcp.tool()
def divide(a: float, b: float) -> float:
    """Divide a by b. Raises an error if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


# ---------------------------------------------------------------------------
# Text tools
# ---------------------------------------------------------------------------

@mcp.tool()
def word_count(text: str) -> dict:
    """Count words, characters, and lines in the given text."""
    words = text.split()
    lines = text.splitlines()
    return {
        "words": len(words),
        "characters": len(text),
        "characters_no_spaces": len(text.replace(" ", "")),
        "lines": len(lines),
    }


@mcp.tool()
def reverse_text(text: str) -> str:
    """Reverse the given text."""
    return text[::-1]


@mcp.tool()
def to_uppercase(text: str) -> str:
    """Convert text to uppercase."""
    return text.upper()


@mcp.tool()
def to_lowercase(text: str) -> str:
    """Convert text to lowercase."""
    return text.lower()


# ---------------------------------------------------------------------------
# Date & time tools
# ---------------------------------------------------------------------------

@mcp.tool()
def current_datetime() -> dict:
    """Return the current date and time in various formats."""
    now = datetime.now()
    return {
        "iso": now.isoformat(),
        "date": now.strftime("%Y-%m-%d"),
        "time": now.strftime("%H:%M:%S"),
        "timestamp": int(now.timestamp()),
    }


@mcp.tool()
def format_datetime(timestamp: int, fmt: str = "%Y-%m-%d %H:%M:%S") -> str:
    """Format a Unix timestamp using the given format string."""
    return datetime.fromtimestamp(timestamp).strftime(fmt)


# ---------------------------------------------------------------------------
# Figma tools
# ---------------------------------------------------------------------------

@mcp.tool()
def figma_get_file(file_key: str) -> dict:
    """Fetch a Figma file by its key and return metadata and the document tree.

    Args:
        file_key: The key from a Figma file URL (e.g. 'abc123' from
                  figma.com/design/abc123/...).
    """
    data = _figma_get(f"/files/{file_key}")
    return {
        "name": data.get("name"),
        "last_modified": data.get("lastModified"),
        "thumbnail_url": data.get("thumbnailUrl"),
        "version": data.get("version"),
        "document": data.get("document"),
    }


@mcp.tool()
def figma_get_node(file_key: str, node_id: str) -> dict:
    """Fetch a specific node from a Figma file.

    Args:
        file_key: The Figma file key.
        node_id:  The node ID (e.g. '1:2' or '1-2').
    """
    node_id_encoded = node_id.replace(":", "-")
    data = _figma_get(f"/files/{file_key}/nodes?ids={node_id_encoded}")
    nodes = data.get("nodes", {})
    key = next(iter(nodes), None)
    return nodes[key] if key else {}


@mcp.tool()
def figma_get_comments(file_key: str) -> list:
    """Return all comments on a Figma file.

    Args:
        file_key: The Figma file key.
    """
    data = _figma_get(f"/files/{file_key}/comments")
    return data.get("comments", [])


@mcp.tool()
def figma_get_images(file_key: str, node_ids: str, scale: float = 1.0, fmt: str = "png") -> dict:
    """Export images for one or more nodes from a Figma file.

    Args:
        file_key: The Figma file key.
        node_ids: Comma-separated list of node IDs to export.
        scale:    Export scale factor (0.01–4). Defaults to 1.0.
        fmt:      Image format — 'png', 'jpg', 'svg', or 'pdf'. Defaults to 'png'.
    """
    ids_encoded = node_ids.replace(":", "-")
    path = f"/images/{file_key}?ids={ids_encoded}&scale={scale}&format={fmt}"
    data = _figma_get(path)
    return data.get("images", {})


@mcp.tool()
def figma_get_components(file_key: str) -> list:
    """List all published components in a Figma file.

    Args:
        file_key: The Figma file key.
    """
    data = _figma_get(f"/files/{file_key}/components")
    return data.get("meta", {}).get("components", [])


@mcp.tool()
def figma_whoami() -> dict:
    """Return information about the authenticated Figma user."""
    return _figma_get("/me")


if __name__ == "__main__":
    mcp.run()
