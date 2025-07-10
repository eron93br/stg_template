import streamlit as st
"""
Este código utiliza a biblioteca Streamlit para criar uma aplicação web com navegação entre páginas.

Funções e Objetos:
- `st.Page`: Cria uma página com um arquivo associado, título e ícone.
    - `main_page`: Página inicial da aplicação, associada ao arquivo "pages/capa.py", com título "Início" e ícone "🏠".
    - `page_3`: Página do chatbot, associada ao arquivo "pages/chatbot.py", com título "Chatbot" e ícone "🤖".
- `st.navigation`: Configura a navegação entre as páginas criadas.
    - `pg`: Objeto de navegação que gerencia as páginas definidas.
- `pg.run()`: Executa a navegação, permitindo que o usuário interaja com as páginas da aplicação.

Este código é ideal para criar uma interface simples e interativa com múltiplas páginas em Streamlit.
"""

main_page = st.Page("pages/capa.py", title="Início", icon="🏠")
page_3 = st.Page("pages/chatbot.py", title="Chatbot", icon="🤖")

pg = st.navigation([main_page,  page_3])

pg.run()