import streamlit as st

main_page = st.Page("pages/capa.py", title="Início", icon="🏠")
page_3 = st.Page("pages/chatbot.py", title="Chatbot", icon="🤖")

pg = st.navigation([main_page,  page_3])

pg.run()
