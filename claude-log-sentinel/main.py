import os
import sys

from anthropic import Anthropic, APIError
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Obtém a chave de API
api_key = os.getenv("ANTHROPIC_API_KEY")

# Verifica se a chave foi configurada antes de iniciar o cliente
if not api_key:
    print("❌ ERRO: A variável ANTHROPIC_API_KEY não foi encontrada no arquivo .env.")
    print("Crie um arquivo '.env' na raiz do projeto com o conteúdo: ANTHROPIC_API_KEY=sua_chave_aqui")
    sys.exit(1)

client = Anthropic(api_key=api_key)

LOG_FILE = os.path.join("logs", "app.log")


def extract_errors(file_path: str) -> list[str]:
    """Lê o arquivo e filtra apenas as linhas de ERRO."""
    if not os.path.exists(file_path):
        print(f"⚠️ Arquivo de log '{file_path}' não foi encontrado.")
        return []

    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Filtra linhas contendo "ERROR" ou "ERRO"
    return [line.strip() for line in lines if "ERROR" in line or "ERRO" in line]


def analyze_with_claude(errors: list[str]) -> str:
    """Envia os erros agrupados para o Claude analisar."""
    error_summary = "\n".join(errors[-5:])  # Analisa os últimos 5 erros

    prompt = f"""
    Você é um Engenheiro DevOps/SRE sênior.
    Analise os seguintes erros de log de produção e forneça:
    1. Causa provável
    2. Nível de severidade (Baixo, Médio, Crítico)
    3. Plano de ação imediato em formato markdown

    Logs de Erro:
    {error_summary}
    """

    try:
        response = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=500,
            messages=[{"role": "user", "content": prompt}],
        )
        first_content = response.content[0]
        return getattr(first_content, "text", str(first_content))
    except APIError as e:
        return f"❌ Erro na API do Claude: {e.message}"


if __name__ == "__main__":
    print("🔍 Varrendo logs em busca de falhas...")
    found_errors = extract_errors(LOG_FILE)

    if found_errors:
        print(
            f"⚠️ Encontrados {len(found_errors)} erros. Solicitando análise ao Claude...\n"
        )
        analysis = analyze_with_claude(found_errors)
        print("--- RELATÓRIO DO CLAUDE ---")
        print(analysis)
    else:
        print("✅ Nenhum erro encontrado nos logs.")