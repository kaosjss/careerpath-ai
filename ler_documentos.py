from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


loader = PyPDFLoader("documentos/01_backend_java.pdf")

documentos = loader.load()


splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=150
)


chunks = splitter.split_documents(documentos)


print("Quantidade de páginas:", len(documentos))
print("Quantidade de chunks:", len(chunks))

print("\n--- PRIMEIRO CHUNK ---\n")

print(chunks[0].page_content)