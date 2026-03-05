from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.schema import Document
from dotenv import load_dotenv
import google.generativeai as genai
import os
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
class GeminiEmbeddings():
    def embed_documents(self, texts):
        return [
            genai.embed_content(
                model="models/embedding-001",
                content=text
            )['embedding']
            for text in texts
        ]
    def embed_query(self, text):
        return genai.embed_content(
            model="models/embedding-001",
            content=text
        )['embedding']

documents = [
    Document(page_content="This is the first document.", metadata={"id": 1}),
    Document(page_content="Second document for testing.", metadata={"id": 2}),
    Document(page_content="Here is the third document.", metadata={"id": 3}),
    Document(page_content="Fourth document in the list.", metadata={"id": 4}),
    Document(page_content="Finally, the fifth document.", metadata={"id": 5}),
]

vector_store = Chroma(
    embedding_function=GeminiEmbeddings(),
    collection_name="example_collection",
    persist_directory="vector_db",
)

vector_store.add_documents(documents)

#print(vector_store.get(include=["documents"]))

print(vector_store.similarity_search("this is first", k=2)) 