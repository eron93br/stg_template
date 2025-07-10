import streamlit as st
import google.generativeai as genai
from streamlit_chat import message
from src.utils import check_messages_count
from src.ui import footer
import os
from dotenv import load_dotenv

# carrega configuracoes de um arquivo .env
load_dotenv()

# Checa se tem API Key
gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    st.error("❌ API Key do Gemini não configurada. O chatbot está temporariamente indisponível.")
    st.stop()

# configura chaves para API gemini
genai.configure(api_key=gemini_api_key)

st.set_page_config(page_title="Chatbot", page_icon="🤖", layout="centered")

st.sidebar.image("images/logo.png", use_container_width=True, width=1)
st.markdown("""
<div style="text-align:center; margin-top: 2rem; margin-bottom: 0.2rem;">
    <h2> LLM GenAI School</h2>
    <p style="color:#8b949e;">Tire suas sobre assistens de IA.</p>
</div>
""", unsafe_allow_html=True)

if "chat" not in st.session_state:
    model = genai.GenerativeModel('gemma-3-27b-it')
    st.session_state.chat = model.start_chat(history=[
        {"role": "user", "parts": [
            "Você é um assistente para dúvidas sobre agentes de IA. Não responda mensagens fora desse contexto. Seja claro e sucinto."
        ]},
        {"role": "model", "parts": [
            "Olá! Como posso ajudar você hoje?"
        ]}
    ])
    
if "chat_history_ui" not in st.session_state:
    st.session_state.chat_history_ui = [
        ("Gemini", "Olá! Como posso ajudar você hoje?")
    ]

if not check_messages_count(5):
    st.stop()

for idx, (speaker, msg) in enumerate(st.session_state.chat_history_ui):
    is_user = speaker == "Usuário"
    message(msg, is_user=is_user, key=f"msg_{idx}")

with st.form("user_input_form", clear_on_submit=True):
    user_input = st.text_area("Digite sua dúvida...", key="user_input", height=80, max_chars=800)
    send_btn = st.form_submit_button("Enviar")

if send_btn and user_input.strip():
    st.session_state.chat_history_ui.append(("Usuário", user_input))
    try:
        with st.spinner("Gemini está digitando..."):
            response = st.session_state.chat.send_message(user_input)
        st.session_state.chat_history_ui.append(("Gemini", response.text))
    except Exception as e:
        st.session_state.chat_history_ui.append(("Gemini",
            "❌ Não foi possível responder agora. "
            "Pode ser um problema temporário, limitação de uso da API ou a chave expirou. "
            "Se o erro persistir, entre em contato com o administrador."))
        # (opcional) st.write(f"DEBUG: {e}")
    st.session_state.message_count += 1
    
    st.rerun()

# Rodapé (footer)
footer()