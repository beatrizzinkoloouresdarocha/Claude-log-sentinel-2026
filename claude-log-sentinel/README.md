# 🛡️ Claude Log Sentinel

> **Análise automatizada de logs e diagnóstico de falhas utilizando a API do Claude (Anthropic).**

O **Claude Log Sentinel** é uma ferramenta em Python desenvolvida para varrer arquivos de log em busca de erros, exceções e falhas de execução, enviando os trechos críticos para a API da Anthropic. O Claude analisa os contextos das falhas e devolve diagnósticos claros e sugestões de correção diretamente no terminal.

---

## 🚀 Funcionalidades

- 🔍 **Varredura Automatizada:** Identifica e extrai linhas de erro e rastros de pilha (*stack traces*) em arquivos de log.
- 🤖 **Diagnóstico Inteligente:** Utiliza a IA do Claude para explicar a causa raiz de falhas complexas em linguagem acessível.
- 💡 **Sugestão de Soluções:** Receba recomendações práticas de como corrigir o código ou a infraestrutura afetada.
- 🔒 **Segurança:** Gestão de credenciais via variáveis de ambiente (`.env`).

---

## 🛠️ Pré-requisitos

- Python 3.10 ou superior instalado.
- Chave de API da Anthropic ([Obtenha sua API Key aqui](https://console.anthropic.com/)).

---

## 📦 Instalação e Configuração

### 1. Clonar o Repositório

```bash
git clone [https://github.com/beatrizzinkoloouresdarocha/Claude-log-sentinel-2026.git](https://github.com/beatrizzinkoloouresdarocha/Claude-log-sentinel-2026.git)
cd Claude-log-sentinel-2026/claude-log-sentinel