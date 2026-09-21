# 🛡️ Claude Log Sentinel

O **Claude Log Sentinel** é uma ferramenta de automação em Python desenvolvida para monitorar arquivos de log de produção, identificar falhas/erros críticos e gerar relatórios analíticos de nível DevOps/SRE utilizando a API do Claude (Anthropic).

---

## 🚀 Funcionalidades

- **Varredura Inteligente:** Filtra automaticamente linhas marcadas com `ERROR` ou `ERRO` em arquivos de log.
- **Análise SRE Aprofundada:** Identifica causa provável, nível de severidade e sugere plano de ação em Markdown.
- **Modo Demonstração (Mock Fallback):** Simula a resposta SRE caso nenhuma chave de API válida esteja presente, garantindo execução local sem custos ou erros de autenticação.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**
- **Anthropic SDK** (`anthropic`)
- **python-dotenv**
- **Ruff & Pylance** (Linting e Padronização PEP 8)

---

## 🔧 Como Executar Localmente

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/beatrizzinkoloouresdarocha/Claude-log-sentinel-2026.git](https://github.com/beatrizzinkoloouresdarocha/Claude-log-sentinel-2026.git)
   cd Claude-log-sentinel-2026/claude-log-sentinel
   ```

2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure as Variáveis de Ambiente:**
   Crie um arquivo `.env` na raiz do projeto contendo:
   ```env
   ANTHROPIC_API_KEY=sk-ant-sua_chave_aqui
   ```
   *(Caso não configure uma chave válida, o projeto rodará no **Modo Demonstração** automaticamente).*

4. **Execute o script:**
   ```bash
   python main.py
   ```