from dotenv import load_dotenv
import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

load_dotenv()

OPEN_AI_KEY=os.getenv("API_KEY")
os.environ["OPENAI_API_KEY"] = OPEN_AI_KEY

documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(documents=documents)

query_engine = index.as_query_engine()
response = query_engine.query("What was the net profit in 2022?")
print(response)