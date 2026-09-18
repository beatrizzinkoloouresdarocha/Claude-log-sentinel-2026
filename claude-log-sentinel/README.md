# Claude Log Sentinel 2026

Um monitor e analisador de logs de erros que utiliza a API da Anthropic (Claude) para gerar diagnosticos automaticos.

## 🚀 Como Executar

1. Clone o repositorio
2. Crie e ative o ambiente virtual:
   python -m venv venv
   .\venv\Scripts\activate
3. Instale as dependencias:
   pip install -r requirements.txt
4. Crie um arquivo .env baseado no .env.example e adicione sua chave de API:
   ANTHROPIC_API_KEY=sk-ant-api03-sua_chave
5. Execute o simulador de logs:
   python app.py
6. Execute o analisador:
   python main.py
