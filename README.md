# 🎯 CareerPath AI

> Sistema inteligente de orientação de carreira em tecnologia baseado em Retrieval-Augmented Generation (RAG).

<p align="center">
  <img src="assets/careerpath-demo.png" alt="CareerPath AI funcionando" width="850">
</p>

## 📌 Sobre o projeto

O **CareerPath AI** é uma aplicação desenvolvida para auxiliar estudantes e profissionais na identificação de competências e conhecimentos necessários para diferentes trilhas de carreira na área de tecnologia.

O sistema utiliza **Retrieval-Augmented Generation (RAG)** para consultar uma base de documentos antes de gerar uma resposta com o Google Gemini.

Dessa forma, as respostas são fundamentadas no conteúdo disponível na base de conhecimento, reduzindo respostas inventadas ou não relacionadas aos documentos.

---

## 🚀 Funcionalidades

- 🔎 Consulta de informações sobre carreiras em tecnologia
- 🧠 Busca semântica na base de documentos
- 🤖 Geração de respostas utilizando Google Gemini
- 📚 Apresentação das fontes consultadas
- 🌐 Interface web desenvolvida com Streamlit
- ☁️ Aplicação disponível online
- 🔐 Gerenciamento seguro das credenciais através de Secrets

---

## 🧠 Como funciona

O CareerPath AI utiliza uma arquitetura baseada em RAG:

```text
                    ┌──────────────────┐
                    │      Usuário     │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │    Streamlit     │
                    │  Interface Web   │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │       RAG        │
                    │ Busca semântica  │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │    Documentos    │
                    │ Base de conhecimento │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │   Google Gemini  │
                    │ Geração da resposta │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Resposta baseada │
                    │    na base       │
                    └──────────────────┘
```

### Fluxo

1. O usuário envia uma pergunta.
2. O sistema realiza uma busca semântica nos documentos.
3. Os conteúdos mais relevantes são recuperados.
4. O contexto encontrado é enviado ao Google Gemini.
5. O modelo gera uma resposta baseada nesse contexto.
6. As fontes utilizadas são apresentadas ao usuário.

---

## 🛠️ Tecnologias utilizadas

| Tecnologia | Utilização |
|---|---|
| 🐍 Python | Desenvolvimento da aplicação |
| 🦜 LangChain | Construção do pipeline RAG |
| 🤖 Google Gemini | Geração das respostas |
| 🔎 Embeddings | Busca semântica |
| 📄 PyPDF | Processamento dos documentos PDF |
| 🌐 Streamlit | Interface web |
| 🔧 Git | Controle de versão |
| 🐙 GitHub | Hospedagem do código |
| ☁️ Streamlit Cloud | Deploy da aplicação |

---

## 📂 Estrutura do projeto

```text
careerpath-ai/
│
├── 📁 documentos/
│   └── Base de conhecimento utilizada pelo RAG
│
├── 📁 src/
│   ├── config.py
│   ├── rag.py
│   └── Outros componentes do sistema
│
├── 📁 .devcontainer/
│
├── 📄 app.py
├── 📄 main.py
├── 📄 streamlit_app.py
├── 📄 requirements.txt
├── 📄 .gitignore
└── 📄 README.md
```

---

## 🌐 Demonstração

O CareerPath AI está disponível online:

👉 **https://careerpath-ai1.streamlit.app/**

Você pode fazer perguntas sobre as diferentes trilhas de carreira disponíveis na base de conhecimento e receber respostas fundamentadas nos documentos.

---

## 💻 Como executar localmente

### 1. Clone o repositório

```bash
git clone https://github.com/kaosjss/careerpath-ai.git
cd careerpath-ai
```

### 2. Crie um ambiente virtual

```bash
python -m venv .venv
```

### 3. Ative o ambiente virtual no Windows

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Instale as dependências

```powershell
pip install -r requirements.txt
```

### 5. Configure a chave da API

Crie um arquivo `.env` na raiz do projeto:

```text
GEMINI_API_KEY=sua_chave_do_gemini
```

> ⚠️ Nunca compartilhe ou publique sua chave da API. O arquivo `.env` está incluído no `.gitignore`.

### 6. Execute a aplicação

```powershell
streamlit run streamlit_app.py
```

A aplicação estará disponível localmente no endereço fornecido pelo Streamlit.

---

## 🔐 Segurança

As credenciais da API não são armazenadas no código-fonte nem no repositório.

No ambiente local, a chave é armazenada através de variáveis de ambiente.

No deploy, as credenciais são configuradas através do sistema de **Secrets do Streamlit Cloud**.

---

## 🧪 Testes realizados

O sistema foi testado utilizando diferentes tipos de perguntas.

### Perguntas relacionadas à base

- Competências necessárias para Backend Java
- Competências necessárias para Cloud & OCI
- Competências necessárias para Dados & BI
- Perguntas específicas sobre competências profissionais

### Perguntas fora da base

Também foi realizado um teste com uma pergunta sem relação com os documentos disponíveis.

Nesse caso, o sistema identificou que não havia informações suficientes na base para responder.

Isso ajuda a evitar respostas não fundamentadas no conteúdo disponibilizado ao RAG.

---

## 🎯 Objetivo

O projeto demonstra a aplicação prática de técnicas de **Inteligência Artificial Generativa e RAG** para construção de uma ferramenta de orientação profissional.

Além de gerar respostas, o sistema busca garantir que as informações apresentadas estejam relacionadas ao conteúdo disponível na base de conhecimento.

---

## 📈 Possíveis melhorias futuras

- 👤 Sistema de perfil do usuário
- 🎯 Recomendações personalizadas de carreira
- 📊 Avaliação de competências
- 🗺️ Roadmap individual de estudos
- 📚 Expansão da base de conhecimento
- 🔎 Filtros por área de tecnologia
- 💾 Histórico de consultas

---

## 👨‍💻 Autor

**Kauã Jesus**

Estudante de Ciência da Computação e desenvolvedor do CareerPath AI.

---

## 📄 Licença

Este projeto foi desenvolvido para fins acadêmicos e de aprendizado.