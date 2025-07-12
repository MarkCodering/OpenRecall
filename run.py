# run.py
from openrecall.main import mcp

if __name__ == "__main__":
    print("Starting OpenRecall MCP server...")
    mcp.start()
    print("OpenRecall MCP server is running.")