"""
Loader module for OpenRecall.
This module is to load context files and resources as a data for further embedding to the vector database.
"""

from langchain_docling import DoclingLoader
from langchain_community.document_loaders import PyPDFLoader

# Web - URL
def load_web_url(url: str) -> str:
    """Load content from a web URL."""
    
    loader = DoclingLoader(url)
    documents = loader.load()
    
    num_docs = len(documents)
    
    if num_docs == 0:
        return "No content found at the provided URL."
    
    # Return all of the content as a single string
    return "\n\n".join(doc.page_content for doc in documents)

def load_pdf_file(file_path: str) -> str:
    """Load content from a PDF file."""
    
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    
    num_docs = len(documents)
    
    if num_docs == 0:
        return "No content found in the provided PDF file."
    
    # Return all of the content as a single string
    return "\n\n".join(doc.page_content for doc in documents)  
