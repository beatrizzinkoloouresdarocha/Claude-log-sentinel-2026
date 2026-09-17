import os

from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

LOG_FILE = "logs/app.log"


def extract_errors(file_path):
    """Lê o arquivo e filtra apenas as linhas de ERRO."""
    if not os.path.exists(file_path):
        return []

    with open(file_path, "r") as f:
        lines = f.readlines()

    return [line.strip() for line in lines if "ERROR" in line]


def analyze_with_claude(errors):
    """Envia os erros agrupados para o Claude analisar."""
    error_summary = "\n".join(errors[-5:])  # Analisa os últimos 5 erros

    prompt = f"""
    Você é um Engenheiro DevOps/SRE sênior.
    Análise os seguintes erros de log de produção e forneça:
    1. Causa provável
    2. Nível de severidade (Baixo, Médio, Crítico)
    3. Plano de ação imediato em formato markdown

    Logs de Erro:
    {error_summary}
    """

    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=500,
        messages=[{"role": "user", "content": prompt}],
    )

    return response.content[0].text


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