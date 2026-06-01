# Módulo 3 — Benchmark de Conteúdo

## Objetivo

Identificar e analisar os conteúdos de maior performance de cada perfil monitorado — especialmente Reels e Carrosséis. Extrair o que torna cada conteúdo eficaz.

## Dependência

Requer o relatório `reports/YYYY-MM-DD/02-perfis-instagram.md` gerado pelo Módulo 2.

## Instrução para o agente

### Passo 1 — Carregar dados do Módulo 2

Leia `reports/YYYY-MM-DD/02-perfis-instagram.md`.
Extraia a lista de perfis analisados e os `top_posts_temas` de cada um.

### Passo 2 — Busca de conteúdo viral por perfil

Para cada perfil, execute buscas específicas:

```
WebSearch: "@{handle} instagram reel viral 2026"
WebSearch: "@{handle} instagram carrossel mais compartilhado"
WebSearch: "@{handle} instagram conteúdo fixado pinned"
WebSearch: "@{handle} instagram post mais comentado"
```

Também busque casos específicos dos `top_posts_temas` identificados:
```
WebSearch: "@{handle} instagram {tema} reel"
```

### Passo 3 — Extrair dados de cada conteúdo via Swarm

**Tasks:** uma por conteúdo encontrado (perfil × post identificado).

```javascript
instruction: "Analise o conteúdo do perfil @{handle} sobre o tema '{tema}' ({tipo}: reel/carrossel). Extraia: hook exato (1ª linha/imagem), estrutura narrativa, CTA, duração estimada, estilo visual, emoção dominante, performance estimada."

responseSchema: {
  type: "object",
  additionalProperties: false,
  properties: {
    handle: { type: "string" },
    tipo: { type: "string", enum: ["reel", "carrossel", "foto", "story"] },
    tema: { type: "string" },
    hook: { type: "string", description: "Primeira linha ou abertura exata." },
    estrutura: { type: "string", description: "Fluxo em 1 frase: A → B → C." },
    cta: { type: "string" },
    duracao_segundos: { type: "number" },
    num_slides: { type: "number" },
    estilo_visual: { type: "string", description: "1 frase descrevendo o visual." },
    emocao_dominante: { type: "string", enum: ["curiosidade", "medo", "inspiracao", "humor", "urgencia", "nostalgia", "surpresa"] },
    performance_estimada: { type: "string", enum: ["alto", "medio", "baixo"] },
    motivo_performance: { type: "string", description: "Hipótese em 1 frase." },
    limitacao: { type: "string" }
  },
  required: ["handle", "tipo", "tema", "hook", "estrutura", "emocao_dominante", "performance_estimada"]
}

concurrency: 3
batchSize: 5
context: "Baseie-se apenas em dados encontrados via busca. Se não encontrar dados suficientes sobre o conteúdo, preencha 'limitacao'. Nunca invente métricas de visualizações ou engajamento."
```

**Retry:**
```javascript
filter: { column: "hook", exists: false }
```

### Passo 4 — Identificar Top 10 geral

Com `rows()`, recupere todos os conteúdos analisados.
Ordene por `performance_estimada` (alto primeiro) e selecione os 10 melhores entre todos os perfis.

Em caso de empate, priorize:
1. Reels (maior alcance estimado)
2. Carrosséis
3. Fotos

### Passo 5 — Gerar relatório

Escreva `reports/YYYY-MM-DD/03-benchmark.md` com:

**Seção 1 — Top 10 conteúdos de alta performance**

| # | Perfil | Tipo | Tema | Hook | Emoção | Performance |
|---|--------|------|------|------|--------|-------------|

**Seção 2 — Análise por perfil**

Para cada perfil:
- Conteúdos encontrados
- Padrão predominante (tipo + emoção + estrutura)
- Melhor conteúdo identificado

**Seção 3 — Padrões transversais**

- Qual emoção domina entre os top performers?
- Qual estrutura mais se repete?
- Qual tipo de conteúdo (reel/carrossel) tem mais alta performance?
- Qual CTA aparece mais nos top conteúdos?
