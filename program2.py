from dotenv import load_dotenv
import os

load_dotenv()

OPEN_AI_KEY = os.getenv("API_KEY")
os.environ["OPENAI_API_KEY"] = OPEN_AI_KEY

PERSIST_DIR = "./storage"

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage

if not os.path.exists(PERSIST_DIR):
    documents = SimpleDirectoryReader("./data").load_data()
    index = VectorStoreIndex.from_documents(documents=documents)
    
    index.storage_context.persist(persist_dir=PERSIST_DIR)
    
else:
    storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
    index = load_index_from_storage(storage_context=storage_context)
    
    
query_engine = index.as_query_engine()

question = "What was the revenue of Tesla in 2022 as per the document"

response = query_engine.query(question)

print(response)