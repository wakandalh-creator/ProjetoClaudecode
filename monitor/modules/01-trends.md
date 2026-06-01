# Módulo 1 — Monitoramento de Tendências

## Objetivo

Varrer fontes públicas e gerar um digest semanal das principais novidades em IA, automação, marketing, growth e SaaS.

## Instrução para o agente

### Passo 1 — Carregar configurações

Leia `config/sources.json` e extraia:
- Lista de `topics`
- Lista de `web_sources` (URL + foco)
- Lista de `search_queries`

### Passo 2 — Vasculhar fontes via Swarm

Use a skill Swarm para processar todas as fontes em paralelo.

**Fonte das tasks:** array construído com web_sources + search_queries.

**Para cada web_source:**
```
instruction: "Acesse {url} via WebFetch. Extraia as 3-5 principais novidades relacionadas a: {topics}. Para cada uma: titulo, data_publicacao, topico_central, resumo_1_frase, relevancia."
```

**Para cada search_query:**
```
instruction: "Execute WebSearch para '{query}'. Extraia as 3 notícias/posts mais relevantes. Para cada um: titulo, fonte, topico_central, resumo_1_frase, relevancia."
```

**responseSchema (obrigatório, additionalProperties: false):**
```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "novidades": {
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "titulo": { "type": "string" },
          "fonte": { "type": "string" },
          "data": { "type": "string" },
          "topico": { "type": "string" },
          "resumo": { "type": "string", "description": "Máximo 1 frase." },
          "relevancia": { "type": "string", "enum": ["alto", "medio", "baixo"] }
        },
        "required": ["titulo", "fonte", "topico", "resumo", "relevancia"]
      }
    },
    "limitacao": { "type": "string", "description": "Se fonte inacessível, explique aqui." }
  },
  "required": ["novidades"]
}
```

**Parâmetros Swarm:**
```javascript
concurrency: 3
batchSize: 5
context: "Foque em IA, Claude Code, agentes, automação, marketing, SaaS, growth. Responda apenas com dados encontrados. Se a fonte estiver inacessível, preencha 'limitacao'."
```

### Passo 3 — Retry obrigatório

Após o run inicial, execute retry para itens sem novidades:
```javascript
filter: { column: "novidades", exists: false }
```

### Passo 4 — Agregar resultados

Use `rows()` para recuperar todos os resultados.
Agrupe por `topico` e ordene por `relevancia` (alto primeiro).
Filtre duplicatas por `titulo` similar.

### Passo 5 — Identificar padrões

Com todas as novidades coletadas, responda:
- O que está emergindo como tendência esta semana?
- Existe algum sinal de alerta (mudança relevante para o negócio)?
- O que é ruído e pode ser ignorado?

### Passo 6 — Gerar relatório

Escreva o arquivo `reports/YYYY-MM-DD/01-tendencias.md` seguindo o template em `monitor/templates/report-trends.md`.

Use a data de hoje no nome da pasta. Se a pasta não existir, crie-a.

## Critérios de qualidade

- Mínimo de 10 novidades distintas coletadas
- Pelo menos 1 novidade de relevância "alto" por tópico principal
- Fontes inacessíveis documentadas, não silenciadas
- Relatório gerado e salvo antes de concluir o módulo
