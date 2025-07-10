import streamlit as st
import pandas as pd
import plotly.express as px

def footer():
    """
    Exibe um rodapé estilizado na interface do usuário utilizando Streamlit.

    O rodapé contém informações de copyright e é exibido centralizado na parte inferior da página.
    O estilo é definido com HTML e CSS embutidos.

    Uso:
        Esta função deve ser chamada em um aplicativo Streamlit para renderizar o rodapé.

    Retorno:
        Não retorna nenhum valor. Apenas renderiza o conteúdo na interface do usuário.
    """
    st.markdown("""
        <div style='text-align: center; color: #bbb; font-size: 0.9em; margin-top: 100px;'>
            © 2025 Curso Fundamentos de IA Generativa - CESAR School
        </div>
    """, unsafe_allow_html=True)

def tooltip(texto, dica):
    """
    Gera uma string HTML que exibe um texto com uma dica (tooltip) ao passar o cursor sobre ele.

    Args:
        texto (str): O texto principal que será exibido.
        dica (str): A dica que será exibida como tooltip ao passar o cursor sobre o texto.

    Returns:
        str: Uma string HTML formatada com o texto e a dica.
    """
    return f"<span title='{dica}' style='text-decoration:underline dotted; cursor:help;'>{texto}</span>"
