import os

from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")


loader = PyPDFLoader("documentos/01_backend_java.pdf")

documentos = loader.load()


splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=150
)

chunks = splitter.split_documents(documentos)


embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",
    api_key=api_key
)


vector_store = InMemoryVectorStore(embeddings)


vector_store.add_documents(chunks)


pergunta = "Spring Boot é importante para conseguir um estágio em backend Java?"


resultados = vector_store.similarity_search(
    pergunta,
    k=3
)


for i, resultado in enumerate(resultados, start=1):

    print(f"\n--- RESULTADO {i} ---\n")

    print(resultado.page_content)