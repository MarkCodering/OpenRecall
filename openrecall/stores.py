import getpass
import os

from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

if not os.environ.get("OPENAI_API_KEY"):
  os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")

embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

def get_vector_store(name: str) -> Chroma:
    """Get a vector store for the given name."""
    return Chroma(
        collection_name=name,
        embedding_function=embeddings,
        persist_directory="./chroma_langchain_db",  # Where to save data locally, remove if not necessary
    )
    
def get_vector_store_by_name(name: str) -> Chroma:
    """Get a vector store by its name."""
    vector_store = get_vector_store(name)
    
    if not vector_store:
        raise ValueError(f"Vector store with name '{name}' does not exist.")
    
    return vector_store

def add_context_to_vector_store(name: str, content: str) -> None:
    """Add context to the vector store."""
    vector_store = get_vector_store(name)
    
    if not vector_store:
        raise ValueError(f"Vector store with name '{name}' does not exist.")
    
    vector_store.add_texts([content])
    
def search_vector_store(name: str, query: str) -> list:
    """Search the vector store for a query."""
    vector_store = get_vector_store(name)
    
    if not vector_store:
        raise ValueError(f"Vector store with name '{name}' does not exist.")
    
    results = vector_store.similarity_search(query, k=5)
    if not results:
        return ["No relevant context found."]
    
    # Return the content of the documents found in the search    
    return [doc.page_content for doc in results]