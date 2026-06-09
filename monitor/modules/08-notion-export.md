# Módulo 8 — Exportação para Notion

Exporta os resultados do monitoramento para as databases do Notion, centralizando todas as informações em um único lugar.

## Pré-requisitos

Este módulo depende dos Módulos 1, 5 e 6. Só execute após confirmar que existem:
- `reports/YYYY-MM-DD/01-tendencias.md`
- `reports/YYYY-MM-DD/05-modelos-conteudo.md`
- `reports/YYYY-MM-DD/06-aplicacao-negocio.md`
- `reports/YYYY-MM-DD/RESUMO.md`

## IDs das Databases

```
NOTION_DB_TENDENCIAS  = a88964e71a624671ae877e6cf18c1e82
NOTION_DB_IDEIAS      = e0bf7febd28f496e8ec3477a226e7dfa
NOTION_DB_INSIGHTS    = 68de9b5215aa477884ecf92fa30ece7a
NOTION_DB_RESUMO      = 93a0b7e423424160b76c894400f578b1
```

## Etapa 1 — Exportar Tendências

Leia `reports/YYYY-MM-DD/01-tendencias.md` e para cada tendência identificada crie um registro em **Monitor — Tendências** com:

| Campo | Conteúdo |
|-------|----------|
| `tendencia` | Nome da tendência (título) |
| `descricao` | Descrição em 2-3 frases |
| `categoria` | Uma de: IA, Marketing, Conteudo, Tecnologia, Comportamento, Outro |
| `relevancia` | Alta / Media / Baixa (baseado na força do sinal) |
| `data` | Data de hoje (YYYY-MM-DD) |
| `fonte` | URL da fonte principal, se disponível |
| `tags` | Palavras-chave separadas por vírgula |

Máximo: 10 tendências por execução.

## Etapa 2 — Exportar Ideias de Conteúdo

Leia `reports/YYYY-MM-DD/05-modelos-conteudo.md` e para cada ideia crie um registro em **Monitor — Ideias de Conteúdo** com:

| Campo | Conteúdo |
|-------|----------|
| `titulo` | Título da ideia |
| `formato` | Reel / Carrossel / Post / Story |
| `hook` | Gancho/primeira frase |
| `roteiro` | Roteiro em passos |
| `tendencia_origem` | Qual tendência gerou essa ideia |
| `data` | Data de hoje |
| `status` | Sempre `nova` |

Máximo: 5 ideias por execução.

## Etapa 3 — Exportar Insights

Leia `reports/YYYY-MM-DD/06-aplicacao-negocio.md` e extraia os insights estratégicos. Para cada um crie um registro em **Monitor — Insights** com:

| Campo | Conteúdo |
|-------|----------|
| `titulo` | Título curto do insight |
| `insight` | Descrição completa |
| `categoria` | Mercado / Concorrencia / Audiencia / Conteudo / Estrategia |
| `acao_recomendada` | O que fazer com esse insight |
| `data` | Data de hoje |
| `prioridade` | Alta / Media / Baixa |

Máximo: 5 insights por execução.

## Etapa 4 — Criar Resumo Diário

Leia `reports/YYYY-MM-DD/RESUMO.md` e crie **um único registro** em **Monitor — Resumo Diário** com:

| Campo | Conteúdo |
|-------|----------|
| `data` | YYYY-MM-DD (título) |
| `destaques` | 3-5 highlights do dia extraídos do RESUMO.md |
| `tendencias_count` | Número de tendências exportadas |
| `ideias_count` | Número de ideias exportadas |
| `insights_count` | Número de insights exportados |
| `perfis_analisados` | Número de perfis Instagram analisados |
| `post_destaque` | Título do post mais promissor do dia |
| `link_relatorio` | `https://github.com/wakandalh-creator/ProjetoClaudecode/tree/master/reports/YYYY-MM-DD` |

## Regras

- Nunca duplicar registros — verifique se já existe um resumo para a data antes de criar
- Limitar textos ao máximo de 1990 caracteres por campo rich_text
- Se um campo não tiver conteúdo claro, deixar em branco (não inventar)
- Reportar ao final: quantos registros foram criados em cada database

## Entregável

Confirmação no formato:
```
✅ Notion atualizado — YYYY-MM-DD
• Tendências: N registros → Monitor — Tendências
• Ideias: N registros → Monitor — Ideias de Conteúdo
• Insights: N registros → Monitor — Insights
• Resumo: 1 registro → Monitor — Resumo Diário
```
