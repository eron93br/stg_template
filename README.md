
# GenAI LLM Template

## Criação da chave de acesso API Gemini

Para rodar este projeto localmente, crie um arquivo `.env` e coloque no mesmo o conteúdo associado à sua chave API_KEY, que pode ser obtida no site do [Gemini](https://ai.google.dev/gemma/docs/core/gemma_on_gemini_api?hl=pt-br). Obtenha a chave clicando no botão "Gerar chave de API".

```
GEMINI_API_KEY = COLOQUE_SUA_CHAVE_AQUI
```

## Como Rodar o Projeto Python Localmente

1. **Crie um ambiente virtual venv (opcional, mas recomendado):**

   ```bash
   python -m venv .venv
   # Para Linux/Mac:
   source .venv/bin/activate
   # Para Windows:
   .venv\Scripts\activate
   ```

2. **Instalação das dependências:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Execute o aplicativo:**

   ```bash
   streamlit run app.py
   ```

4. **Para acessar a aplicação:**  
   Acesse em [http://localhost:8501](http://localhost:8501)
