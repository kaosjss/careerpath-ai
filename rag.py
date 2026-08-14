import os
from pathlib import Path

from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader, CSVLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import (
    ChatGoogleGenerativeAI,
    GoogleGenerativeAIEmbeddings
)
from langchain_core.vectorstores import InMemoryVectorStore


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

PASTA_DOCUMENTOS = Path("documentos")


# 1. CARREGAR TODOS OS DOCUMENTOS
documentos = []


for arquivo_pdf in PASTA_DOCUMENTOS.glob("*.pdf"):

    print(f"Carregando PDF: {arquivo_pdf.name}")

    loader = PyPDFLoader(str(arquivo_pdf))

    paginas = loader.load()

    documentos.extend(paginas)


for arquivo_csv in PASTA_DOCUMENTOS.glob("*.csv"):

    print(f"Carregando CSV: {arquivo_csv.name}")

    loader = CSVLoader(
        file_path=str(arquivo_csv),
        encoding="utf-8"
    )

    linhas = loader.load()

    documentos.extend(linhas)


print(f"\nTotal de documentos carregados: {len(documentos)}")


# 2. DIVIDIR OS DOCUMENTOS EM CHUNKS
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=150
)

chunks = splitter.split_documents(documentos)

print(f"Total de chunks: {len(chunks)}")


# 3. CRIAR EMBEDDINGS
embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",
    api_key=api_key
)


# 4. CRIAR VECTOR STORE
vector_store = InMemoryVectorStore(embeddings)

vector_store.add_documents(chunks)


# 5. CRIAR O MODELO GEMINI
llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    api_key=api_key
)


# 6. PERGUNTA DO USUÁRIO
pergunta = input("\nDigite sua pergunta para o CareerPath AI: ")


# 7. BUSCAR OS CHUNKS MAIS RELEVANTES
resultados = vector_store.similarity_search(
    pergunta,
    k=5
)


# 8. MONTAR O CONTEXTO
contexto = "\n\n".join(
    resultado.page_content
    for resultado in resultados
)


# 9. MONTAR O PROMPT
prompt = f"""
Você é o CareerPath AI, um assistente de orientação de carreira em tecnologia.

Responda usando SOMENTE as informações presentes no CONTEXTO.

Não invente experiência, requisitos, níveis ou informações que não estejam nos documentos.

Se não houver informação suficiente no contexto, diga claramente que não possui informação suficiente.

Quando possível:
- identifique competências já presentes;
- identifique lacunas;
- priorize no máximo 3 gaps;
- explique o que estudar primeiro;
- use informações de Backend, Cloud, Dados, Scoring, vagas e regras quando forem relevantes.

CONTEXTO:

{contexto}


PERGUNTA DO USUÁRIO:

{pergunta}
"""


# 10. GERAR RESPOSTA
resposta = llm.invoke(prompt)


print("\n====================================")
print("CAREERPATH AI")
print("====================================\n")

print(resposta.content[0]["text"])


# 11. MOSTRAR FONTES RECUPERADAS
print("\n====================================")
print("FONTES CONSULTADAS")
print("====================================\n")


for resultado in resultados:

    source = resultado.metadata.get("source", "Fonte desconhecida")
    page = resultado.metadata.get("page")

    if page is not None:
        print(f"- {source} | página {page + 1}")
    else:
        print(f"- {source}")