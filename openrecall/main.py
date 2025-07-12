# Main entry point for the application
# This file initializes the MCP server and starts the application to load the context files and resources as a context.

# openrecall/main.py
from mcp.server.fastmcp import FastMCP
from openrecall.loader import load_web_url, load_pdf_file
from openrecall.stores import add_context_to_vector_store, search_vector_store , get_vector_store, get_vector_store_by_name

# Create an MCP server
mcp = FastMCP("OpenRecall")

# Load the web context 
@mcp.add_resource("load_web_url")
def load_web_url_command(url: str) -> str:
    """Load content from a web URL and add it to the vector store."""
    content = load_web_url(url)
    if content.startswith("No content found"):
        return content
    
    # Add the loaded content to the vector store
    add_context_to_vector_store("web_context", content)
    return "Content loaded and added to vector store."

# Load the PDF file context
@mcp.add_resource("load_pdf_file")
def load_pdf_file_command(file_path: str) -> str:
    """Load content from a PDF file and add it to the vector store."""
    content = load_pdf_file(file_path)
    if content.startswith("No content found"):
        return content
    
    # Add the loaded content to the vector store
    add_context_to_vector_store("pdf_context", content)
    return "Content loaded and added to vector store."

# Search the vector store
@mcp.add_resource("search_vector_store")
def search_vector_store_command(name: str, query: str) -> list:
    """Search the vector store for a query."""
    try:
        results = search_vector_store(name, query)
        return results
    except ValueError as e:
        return str(e)
    
# Get a vector store by name
@mcp.add_tool("get_vector_store_by_name")
def get_vector_store_by_name_command(name: str) -> str:
    """Get a vector store by its name."""
    try:
        vector_store = get_vector_store_by_name(name)
        return f"Vector store '{name}' retrieved successfully."
    except ValueError as e:
        return str(e)
    
# Get a vector store
@mcp.add_tool("get_vector_store")
def get_vector_store_command(name: str) -> str:
    """Get a vector store for the given name."""
    try:
        vector_store = get_vector_store(name)
        return f"Vector store '{name}' retrieved successfully."
    except ValueError as e:
        return str(e)
