import os

from anthropic import APIError, Anthropic
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")
LOG_FILE = os.path.join("logs", "app.log")


def extract_errors(file_path: str) -> list[str]:
    """Lê o arquivo e filtra apenas as linhas de ERRO."""
    if not os.path.exists(file_path):
        print(f"⚠️ Arquivo de log '{file_path}' não foi encontrado.")
        return []

    with open(file_path, encoding="utf-8") as f:
        lines = f.readlines()

    return [line.strip() for line in lines if "ERROR" in line or "ERRO" in line]


def get_mock_analysis() -> str:
    """Retorna um relatório de demonstração para gravação sem uso de chave real."""
    return """
### 1. Causa Provável
Ocorreram falhas repetidas de conexão com o banco de dados PostgreSQL devido a estouro de timeout e conexões pendentes não encerradas.

### 2. Nível de Severidade
🔴 **CRÍTICO** - Impacta diretamente a disponibilidade dos serviços dependentes de autenticação.

### 3. Plano de Ação Imediato
1. **Reiniciar Pool de Conexões:** Executar a reciclagem do pool no serviço da aplicação.
2. **Aumentar Timeout:** Ajustar a variável `DB_TIMEOUT` de 5s para 15s temporariamente.
3. **Verificar Instância:** Avaliar o uso de CPU/RAM no servidor de banco de dados.
"""


def analyze_with_claude(errors: list[str]) -> str:
    """Envia os erros agrupados para o Claude analisar ou simula o retorno se a chave for inválida."""
    mock_keys = [
        "sua_chave_aqui",
        "sk-ant-api03-sua_chave",
    ]

    is_mock = (
        not api_key
        or api_key in mock_keys
        or any(api_key.startswith(k) for k in mock_keys)
        or not api_key.startswith("sk-ant-")
    )

    if is_mock:
        print("💡 [MODO DEMONSTRAÇÃO] Chave real não detectada ou inválida. Gerando análise simulada...")
        return get_mock_analysis()

    try:
        client = Anthropic(api_key=api_key)
        error_summary = "\n".join(errors[-5:])

        prompt = f"""
        Você é um Engenheiro DevOps/SRE sênior.
        Analise os seguintes erros de log de produção e forneça:
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
        first_content = response.content[0]
        return getattr(first_content, "text", str(first_content))
    except (APIError, Exception):  # noqa: BLE001
        print("💡 [MODO DEMONSTRAÇÃO] Erro de autenticação ou conexão. Retornando análise simulada...")
        return get_mock_analysis()


if __name__ == "__main__":
    print("🔍 Varrendo logs em busca de falhas...")
    found_errors = extract_errors(LOG_FILE)

    if found_errors:
        print(f"⚠️ Encontrados {len(found_errors)} erros. Solicitando análise ao Claude...\n")
        analysis = analyze_with_claude(found_errors)
        print("--- RELATÓRIO DO CLAUDE ---")
        print(analysis)
    else:
        print("✅ Nenhum erro encontrado nos logs.")