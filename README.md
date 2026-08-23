# 🎯 CareerPath AI

Sistema inteligente de orientação de carreira em tecnologia baseado em RAG.

## 📌 Sobre o projeto

O CareerPath AI utiliza Retrieval-Augmented Generation (RAG)
para responder perguntas sobre trilhas de carreira e competências
profissionais com base em uma coleção de documentos.

## 🚀 Funcionalidades

- Consulta de informações sobre carreiras em tecnologia
- Busca semântica nos documentos
- Geração de respostas utilizando Gemini
- Interface web com Streamlit
- Apresentação das fontes consultadas

## 🧠 Arquitetura

Usuário
   ↓
Streamlit
   ↓
Sistema RAG
   ↓
Busca nos documentos
   ↓
Google Gemini
   ↓
Resposta fundamentada

## 🛠️ Tecnologias

- Python
- LangChain
- Google Gemini
- RAG
- Streamlit
- Git
- GitHub

## ▶️ Execução local

Clone o repositório:

git clone https://github.com/kaosjss/careerpath-ai.git

Entre na pasta:

cd careerpath-ai

Crie o ambiente virtual:

python -m venv .venv

Ative:

.venv\Scripts\Activate.ps1

Instale as dependências:

pip install -r requirements.txt

Configure a variável:

GEMINI_API_KEY=sua_chave

Execute:

streamlit run streamlit_app.py

## 🌐 Demonstração

https://careerpath-ai1.streamlit.app/

## 👨‍💻 Autor

Kauã Jesus 