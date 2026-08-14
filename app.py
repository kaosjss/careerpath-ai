from src.rag import responder_pergunta


pergunta = input("Digite sua pergunta: ")

resposta, fontes = responder_pergunta(pergunta)


print("\nCAREERPATH AI\n")

print(resposta)


print("\nFONTES\n")

for fonte in fontes:
    print("-", fonte)