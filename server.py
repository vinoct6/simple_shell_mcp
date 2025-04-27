from mcp.server.fastmcp import FastMCP
import subprocess
import asyncio
import os

# Create an MCP server
mcp = FastMCP("TerminalServer")

@mcp.tool()
async def terminal_tool(command: str) -> str:
    """Run a terminal command and return its output (non-blocking)."""
    try:
        process = await asyncio.create_subprocess_shell(
            command,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()
        output = stdout.decode().strip() if stdout else stderr.decode().strip()
        return output
    except Exception as e:
        return f"Error: {e}"

@mcp.resource("file://mcpreadme")
def get_mcp_readme() -> str:
    """Return the contents of the mcpreadme.md file from the Desktop."""
    desktop_path = os.path.expanduser("~/Desktop/mcpreadme.md")
    try:
        with open(desktop_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"Error reading mcpreadme.md: {e}"

if __name__ == "__main__":
    mcp.run("stdio")
