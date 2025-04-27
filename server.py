from mcp.server.fastmcp import FastMCP
import subprocess
import asyncio

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

if __name__ == "__main__":
    mcp.run()
