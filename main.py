import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    api_key=api_key
)

resposta = llm.invoke(
    "Explique em uma frase o que faz um desenvolvedor backend."
)

print(resposta.content[0]["text"])