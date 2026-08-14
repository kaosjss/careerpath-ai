from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader, CSVLoader


PASTA_DOCUMENTOS = Path("documentos")


def carregar_documentos():
    documentos = []

    for arquivo_pdf in PASTA_DOCUMENTOS.glob("*.pdf"):
        loader = PyPDFLoader(str(arquivo_pdf))
        paginas = loader.load()
        documentos.extend(paginas)

    for arquivo_csv in PASTA_DOCUMENTOS.glob("*.csv"):
        loader = CSVLoader(
            file_path=str(arquivo_csv),
            encoding="utf-8"
        )

        linhas = loader.load()
        documentos.extend(linhas)

    return documentos