from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader, CSVLoader


PASTA_DOCUMENTOS = Path("documentos")

documentos = []


# Carregar todos os PDFs
for arquivo_pdf in PASTA_DOCUMENTOS.glob("*.pdf"):

    print(f"Carregando PDF: {arquivo_pdf.name}")

    loader = PyPDFLoader(str(arquivo_pdf))

    paginas = loader.load()

    documentos.extend(paginas)


# Carregar todos os CSVs
for arquivo_csv in PASTA_DOCUMENTOS.glob("*.csv"):

    print(f"Carregando CSV: {arquivo_csv.name}")

    loader = CSVLoader(
        file_path=str(arquivo_csv),
        encoding="utf-8"
    )

    linhas = loader.load()

    documentos.extend(linhas)


print("\n-----------------------------")
print("TOTAL DE DOCUMENTOS:", len(documentos))
print("-----------------------------")



print("\n--- TESTE DE CONTEÚDO ---\n")

for i, documento in enumerate(documentos[:10]):
    print(f"\nDOCUMENTO {i + 1}")
    print(documento.metadata)
    print(documento.page_content[:300])