"""
MCP Server implementation providing utility tools.
"""

from datetime import datetime
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Utility MCP Server")


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


if __name__ == "__main__":
    mcp.run()
