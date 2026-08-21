# Pipeline n8n — Estruturação (Caminho A/B)

Workflows escritos manualmente (JSON de exportação do n8n) porque o MCP `n8n-mcp` não expôs suas ferramentas nesta sessão apesar de conectado — ver histórico da conversa. **Importar cada arquivo via n8n → Workflows → Import from File**, na ordem abaixo, e revisar antes de ativar.

## Por que este pipeline existe

Ver `Piloto — Salões e Barbearias JF (Caminho A-B).md` no vault Obsidian da Estruturação (`03 — Operação/03.1 — Processos e Checklists/`) para o contexto completo do negócio. Resumo técnico: pipeline genérico de aquisição (prospecção → site → venda → monitoramento), testado primeiro no nicho salão/barbearia em Juiz de Fora-MG, com dois caminhos por prospect — **A** (sem site) e **B** (site fraco existente).

## Ordem de importação e dependências

```
00-orquestrador-principal
 ├─→ 01-caminho-a-sem-site ─┐
 ├─→ 02-caminho-b-com-site ─┤
 │                          ▼
 │                  03-briefing-claude-api
 │                          │
 ▼                          ▼
04-checkpoint-1-triagem (Wait+Telegram)
                            │
05-checkpoint-2-staging (Wait+Telegram)
                            │
06-outreach-whatsapp
                            │
07-agente-vendas-ana (AI Agent)
      │ (se pedir ajuste)
      ▼
07b-loop-ajuste-pre-pagamento (Wait+Telegram) ──volta pra Etapa 5 manual (Claude Code) + 05
      │ (aprovado, sem mais ajuste)
      ▼
08-contratos-pagamento (Autentique + Asaas)
      │
09-deploy-hostinger (checagem MX + FTP)
      │
10-monitoramento-pos-entrega
```

Os sub-workflows (`01`, `02`, `03`, `04`, `05`, `07b`) são chamados via node **Execute Workflow** a partir do orquestrador ou de `07`. Importe TODOS antes de tentar rodar o orquestrador, e depois de importar cada um, copie o **Workflow ID** gerado pelo n8n para as referências `Execute Workflow` que apontam pra ele (o n8n troca os IDs no import — os arquivos aqui usam nomes como placeholder, não IDs reais).

## O que NÃO está automatizado (permanece manual, fora do n8n)

- **Etapa 5 — construção do site**: Claude Code + skill `landing`, dentro do VS Code. O `04-checkpoint-1-triagem` só aprova o lote de prospects; a construção do site acontece fora do n8n antes do `05-checkpoint-2-staging`.
- **Etapa 11** não existe mais como etapa separada — a pergunta de ajuste foi fundida na Camada 2 do Agente Ana (`07`), antes do pagamento.

## Credenciais a configurar no n8n antes de ativar (Settings → Credentials)

Status 2026-08-05: **Asaas confirmado pelo Lucas como já incluído** (conta ativa; nós `asaas-api` referenciados em 3 workflows da instância). Autentique **saiu do fluxo manual** (decisão: sem contrato formal na venda direta — ver Piloto, pendência 6). Demais credenciais: confirmar/criar antes de rodar de verdade.

| Nome sugerido da credencial | Tipo no n8n | Usado em |
|---|---|---|
| `apify-api` | HTTP Header Auth (Bearer) | `01`, `02` |
| `anthropic-api` | HTTP Header Auth (`x-api-key`) ou credencial nativa Anthropic, se disponível na sua versão do n8n | `03`, `07` |
| `telegram-bot-fundador` | Telegram API | `04`, `05`, `07b` |
| `whatsapp-business-api` | HTTP Header Auth ou credencial nativa WhatsApp, conforme provedor escolhido (Meta Cloud API direto vs. BSP) | `06`, `07` |
| `autentique-api` | HTTP Header Auth (Bearer) | `08` |
| `asaas-api` | HTTP Header Auth (`access_token`) | `08` |
| `hostinger-ftp` | FTP | `09` |
| `google-pagespeed-api` | HTTP Query Auth (API key) | `10` |

## Placeholders que exigem decisão antes de ativar (não inventados)

- **Apify actor ID** para scraping de Instagram e de avaliações do Google — depende de qual actor da Apify Store você escolher (ou actor customizado).
- **Provedor de WhatsApp Business API** — Meta Cloud API direto vs. BSP (Twilio/Z-API/360dialog). Os nodes de `06` e `07` estão com a URL genérica da Cloud API da Meta como exemplo — trocar se usar BSP.
- **Template de contrato no Autentique** (2 contratos: desenvolvimento + manutenção) — precisa existir na conta Autentique antes.
- **IDs de produto/plano no Asaas** para a cobrança de setup (parcelada) e assinatura mensal.
- Todos sinalizados com `// TODO:` nos nodes `Set`/`Code` correspondentes.

## Convenção de nomes

Prefixo numérico = ordem de execução no pipeline linear; `07b` = ramificação condicional de `07`. Nome do workflow no n8n = nome do arquivo sem `.json`, para ficar buscável (o MCP só enxerga nome+descrição, não tags).
