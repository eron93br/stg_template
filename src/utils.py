import streamlit as st

def check_messages_count(maximo=5):
    """
    Verifica se o número de mensagens enviadas na sessão atual excede o limite especificado.

    Args:
        maximo (int, opcional): O número máximo de mensagens permitido na sessão. 
        O valor padrão é 5.

    Returns:
        bool: Retorna True se o número de mensagens estiver dentro do limite permitido, 
        caso contrário, retorna False e exibe uma mensagem informativa ao usuário.

    Nota:
        Caso o limite de mensagens seja atingido, uma mensagem informativa será exibida 
        utilizando `st.info`, indicando ao usuário que ele deve recarregar a página para reiniciar a sessão.
    """
    if "message_count" not in st.session_state:
        st.session_state.message_count = 0
    if st.session_state.message_count >= maximo:
        st.info(f"Você atingiu o limite de {maximo} perguntas nesta sessão. Recarregue a página para reiniciar.")
        return False
    return True