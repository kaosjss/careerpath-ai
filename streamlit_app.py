import streamlit as st
from src.rag import responder_pergunta


st.set_page_config(
    page_title="CareerPath AI",
    page_icon="🎯",
    layout="wide"
)


# =========================
# ESTILO
# =========================

st.markdown("""
<style>

.main {
    padding-top: 2rem;
}

.title {
    font-size: 3rem;
    font-weight: 700;
    margin-bottom: 0;
}

.subtitle {
    font-size: 1.2rem;
    color: #888;
    margin-bottom: 2rem;
}

.result-box {
    padding: 1.5rem;
    border-radius: 12px;
    border: 1px solid rgba(128,128,128,0.25);
    margin-top: 1rem;
}

.source-box {
    padding: 1rem;
    border-radius: 10px;
    background-color: rgba(128,128,128,0.08);
    margin-top: 1rem;
}

</style>
""", unsafe_allow_html=True)


# =========================
# CABEÇALHO
# =========================

st.markdown(
    '<div class="title">🎯 CareerPath AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Assistente inteligente para orientação de carreira em tecnologia'
    '</div>',
    unsafe_allow_html=True
)


st.divider()


# =========================
# EXPLICAÇÃO
# =========================

st.markdown("### 🔎 Descubra seu próximo passo")

st.write(
    "Faça perguntas sobre competências, trilhas de carreira e "
    "requisitos profissionais. O CareerPath AI utiliza uma base "
    "de documentos para fundamentar suas respostas."
)


# =========================
# PERGUNTA
# =========================

pergunta = st.text_area(
    "Sua pergunta",
    placeholder=(
        "Ex: Quais competências preciso desenvolver "
        "para trabalhar como desenvolvedor Backend Java?"
    ),
    height=130
)


col1, col2 = st.columns([1, 5])

with col1:
    analisar = st.button(
        "🚀 Analisar",
        type="primary",
        use_container_width=True
    )


# =========================
# PROCESSAMENTO
# =========================

if analisar:

    if not pergunta.strip():

        st.warning("Digite uma pergunta antes de analisar.")

    else:

        with st.spinner("🔎 Consultando a base de conhecimento..."):

            resposta, fontes = responder_pergunta(pergunta)


        st.divider()

        st.markdown("### 💡 Análise")

        st.markdown(
            f'<div class="result-box">{resposta}</div>',
            unsafe_allow_html=True
        )


        if fontes:

            st.markdown("### 📚 Fontes consultadas")

            for fonte in fontes:

                st.markdown(
                    f'<div class="source-box">📄 {fonte}</div>',
                    unsafe_allow_html=True
                )


# =========================
# RODAPÉ
# =========================

st.divider()

st.caption(
    "CareerPath AI • Sistema de orientação de carreira baseado em RAG"
)