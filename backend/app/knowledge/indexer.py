from pathlib import Path

from llama_index.core import (
    Settings,
    SimpleDirectoryReader,
    VectorStoreIndex,
)

from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.llms.ollama import Ollama

# ---------- Configure Ollama ----------

Settings.embed_model = OllamaEmbedding(
    model_name="nomic-embed-text",
    base_url="http://127.0.0.1:11434",
)

Settings.llm = Ollama(
    model="llama3.2",
    base_url="http://127.0.0.1:11434",
    request_timeout=300.0,
)

# ---------- Load documents ----------

knowledge_path = Path(__file__).resolve().parents[2] / "knowledge"

documents = SimpleDirectoryReader(
    str(knowledge_path)
).load_data()

# ---------- Build vector index ----------

index = VectorStoreIndex.from_documents(documents)

# ---------- Export query engine ----------

query_engine = index.as_query_engine()