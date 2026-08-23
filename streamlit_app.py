import streamlit as streamlit
from src.rag import responder_perguntas
st.set_pageconfig(
    page_title="CareerPath AI",
    page_icon="🎯",
    layout="centered"
) 

st.title("🎯 CarrerPath AI")
st.subheader("Assistente de orientação de carreiras, competências e trilha " "de tecnoligia com base nos documentos disponíveis."
)

pergunta = st.text_area(
    "Digite sua pergunta:",
    placeholder= "Ex: Quais competências preciso desenvolver para Backend Java?",
    height=120
)

if st.button("Analisar",
type="primary"):
    if not pergunta.strip():
        st.warning("Digite uma pergunta primeiro.")
    else:
        with
st.spinner("Analisando..."):
        resposta, fontes = 
        responder_perguntas(pergunta)
        st.markdown("### Resposta")
        st.write(resposta)

        if fontes:
            st.markdown("### 📚 fontes")

            for fonte in fontes:
                st.write(f"-{fonte}")