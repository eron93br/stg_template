import streamlit as st
from src.ui import footer

st.set_page_config(page_title="chat School", layout="wide")

st.html("styles.html")

hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.write("")
st.write("")

# Centralizando elementos
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown(
        "<h3 style='text-align: center; color: #5a5a5a; margin-bottom: 24px;'> chat School </h3>",
        unsafe_allow_html=True,
    )
    st.image("images/logo.png")
    st.markdown(
        "<p style='text-align: center; color: #888; max-width: 400px; margin: auto;'>Criando uma LLM personalizada.</p>",
        unsafe_allow_html=True,
    )
    st.write("")

# Rodapé
footer()
