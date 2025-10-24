"""
Calculator MCP server using FastMCP.
Provides mathematical operations as tools for calculation tasks.
"""

import math
import os

from mcp import SamplingMessage
from mcp.server.fastmcp import Context, FastMCP
from mcp.server.session import ServerSession
from mcp.types import TextContent
from pydantic import FileUrl

# Initialize FastMCP server
mcp = FastMCP("calculator")

# Form schema for elicitation requests
FORM_SCHEMA = {
    "type": "object",
    "properties": {
        "name": {
            "type": "string",
            "title": "Full Name",
            "description": "Your full name",
            "minLength": 1,
        },
        "email": {
            "type": "string",
            "title": "Email Address",
            "description": "Your email address",
            "format": "email",
        },
        "age": {
            "type": "number",
            "title": "Age",
            "description": "Your age in years",
            "minimum": 0,
            "maximum": 150,
        },
    },
    "required": ["name", "email"],
}


@mcp.tool("Adding")
async def add(a: float, b: float, ctx: Context[ServerSession, None]) -> str:
    """Add two numbers together.

    Args:
        a: First number
        b: Second number
    """
    result = a + b
    await ctx.info(f"Adding {a} and {b} = {result}")
    return f"{result}"


if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport="stdio")