from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import (
    ChatGoogleGenerativeAI,
    GoogleGenerativeAIEmbeddings
)
from langchain_core.vectorstores import InMemoryVectorStore

from src.loaders import carregar_documentos

from src.config import (
    GEMINI_API_KEY,
    MODELO_CHAT,
    MODELO_EMBEDDING,
    CHUNK_SIZE,
    CHUNK_OVERLAP,
    TOP_K
)


documentos = carregar_documentos()


splitter = RecursiveCharacterTextSplitter(
    chunk_size=CHUNK_SIZE,
    chunk_overlap=CHUNK_OVERLAP
)

chunks = splitter.split_documents(documentos)


embeddings = GoogleGenerativeAIEmbeddings(
   model=MODELO_EMBEDDING,
api_key=GEMINI_API_KEY
)


vector_store = InMemoryVectorStore(embeddings)

vector_store.add_documents(chunks)


llm = ChatGoogleGenerativeAI(
   model=MODELO_CHAT,
api_key=GEMINI_API_KEY
)


def responder_pergunta(pergunta):

    resultados = vector_store.similarity_search(
        pergunta,
        k=TOP_K
    )

    blocos_contexto = []

    fontes = []

    for resultado in resultados:

        source = resultado.metadata.get(
            "source",
            "Fonte desconhecida"
        )

        page = resultado.metadata.get("page")

        if page is not None:
            fonte = f"{source} | página {page + 1}"
        else:
            fonte = source

        bloco = f"""
FONTE: {fonte}

CONTEÚDO:
{resultado.page_content}
"""

        blocos_contexto.append(bloco)

        if fonte not in fontes:
            fontes.append(fonte)


    contexto = "\n\n".join(blocos_contexto)


    prompt = f"""
Você é o CareerPath AI, um assistente especializado
em orientação de carreira em tecnologia.

Responda SOMENTE com base no contexto fornecido.

REGRAS:

- Não invente competências ou experiências.
- Diferencie competência declarada de competência evidenciada.
- Não atribua nível automaticamente.
- Identifique no máximo 3 lacunas principais.
- Priorize requisitos obrigatórios antes de diferenciais.
- Se não houver informação suficiente, diga claramente.

CONTEXTO:

{contexto}

PERGUNTA:

{pergunta}
"""


    resposta = llm.invoke(prompt)


    if isinstance(resposta.content, list):
        texto = resposta.content[0]["text"]
    else:
        texto = resposta.content


    return texto, fontes