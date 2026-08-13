import os

from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import (
    ChatGoogleGenerativeAI,
    GoogleGenerativeAIEmbeddings
)
from langchain_core.vectorstores import InMemoryVectorStore


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")


# 1. Carrega o PDF
loader = PyPDFLoader("documentos/01_backend_java.pdf")
documentos = loader.load()


# 2. Divide em chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=150
)

chunks = splitter.split_documents(documentos)


# 3. Cria embeddings
embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",
    api_key=api_key
)


# 4. Cria banco vetorial
vector_store = InMemoryVectorStore(embeddings)

vector_store.add_documents(chunks)


# 5. Cria o Gemini
llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    api_key=api_key
)


# 6. Pergunta do usuário
pergunta = "Spring Boot é importante para conseguir um estágio em backend Java?"


# 7. Busca os chunks mais relevantes
resultados = vector_store.similarity_search(
    pergunta,
    k=3
)


# 8. Junta os chunks encontrados
contexto = "\n\n".join(
    resultado.page_content
    for resultado in resultados
)


# 9. Monta o prompt
prompt = f"""
Você é o CareerPath AI.

Responda usando SOMENTE as informações presentes no contexto abaixo.

Se a resposta não estiver no contexto, diga que não possui informação suficiente.

CONTEXTO:
{contexto}

PERGUNTA:
{pergunta}
"""


# 10. Envia para o Gemini
resposta = llm.invoke(prompt)


print("\n--- RESPOSTA DO CAREERPATH AI ---\n")

print(resposta.content[0]["text"])
