# Terminal MCP Server

This project provides a simple MCP (Model Context Protocol) server using the [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk). It exposes a single tool, `terminal_tool`, which enables any MCP-compatible client (such as Claude Desktop, MCP Inspector, or custom LLM applications) to execute terminal commands on the host machine and receive their output in real time.

This server is ideal for experimentation, automation, or integrating shell command execution into LLM workflows. **Note:** For safety, it is intended for local or trusted environments only.

## Features
- Exposes a single tool: `terminal_tool`
- Runs shell commands asynchronously (non-blocking)
- Returns command output or error message

## Requirements
- Python 3.8+
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)

## Installation
Install the MCP SDK:

```bash
pip install mcp
```

## Usage
1. Clone or copy this repository.
2. Run the server in development mode:

```bash
mcp dev server.py
```

3. Use the MCP Inspector or a compatible client (e.g., Claude Desktop) to interact with the `terminal_tool`.

### Example
Call the tool with a command string:

```json
{
  "command": "echo Hello, World!"
}
```

The tool will return:

```
Hello, World!
```

## Security Warning
**This server executes arbitrary shell commands.**
- Do NOT expose this server to untrusted users or the public internet.
- For demonstration and local use only.
- Consider adding command restrictions or sandboxing for production use.

## License
MIT
