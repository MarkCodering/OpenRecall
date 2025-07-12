# openrecall/main.py

from openrecall.loader import load_web_url, load_pdf_file
from openrecall.stores import (
    add_context_to_vector_store,
    search_vector_store,
    get_vector_store,
    get_vector_store_by_name,
)
from mcp.server.fastmcp import FastMCP


class OpenRecallApp:
    def __init__(self, name: str = "OpenRecall"):
        self.mcp = FastMCP(name)
        self._register_commands()

    def _register_commands(self):
        @self.mcp.resource("url://{url}")
        def load_web_url_command(url: str) -> str:
            content = load_web_url(url)
            if content.startswith("No content found"):
                return content
            add_context_to_vector_store("web_context", content)
            return "Content loaded and added to vector store."

        @self.mcp.resource("pdf://{file_path}")
        def load_pdf_file_command(file_path: str) -> str:
            content = load_pdf_file(file_path)
            if content.startswith("No content found"):
                return content
            add_context_to_vector_store("pdf_context", content)
            return "Content loaded and added to vector store."

        @self.mcp.resource("search://{name}/{query}")
        def search_vector_store_command(name: str, query: str) -> list:
            try:
                return search_vector_store(name, query)
            except ValueError as e:
                return str(e)

        @self.mcp.tool("get_vector_store_by_name")
        def get_vector_store_by_name_command(name: str) -> str:
            try:
                get_vector_store_by_name(name)
                return f"Vector store '{name}' retrieved successfully."
            except ValueError as e:
                return str(e)

        @self.mcp.tool("get_vector_store")
        def get_vector_store_command(name: str) -> str:
            try:
                get_vector_store(name)
                return f"Vector store '{name}' retrieved successfully."
            except ValueError as e:
                return str(e)

    def run(self):
        self.mcp.run()
        print("OpenRecall MCP server is running.")


if __name__ == "__main__":
    app = OpenRecallApp()
    app.run()