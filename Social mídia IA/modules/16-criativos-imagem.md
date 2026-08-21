# Módulo 16 — Criativos de Imagem (agente: Pixel)

## Objetivo

Gerar criativos de imagem (posts únicos, capas de reel) a partir de um roteiro aprovado (`score_iana ≥7`). Regra central: **Pillow primeiro** (custo zero); só escalar pra IA de imagem quando a peça exigir algo que Pillow não alcança.

## Entrada

- Roteiro em `Social mídia IA/producao/roteiros/YYYY-MM-DD/{slug}.md`, com `score_iana ≥7`. Sem essa condição: avisar o Lucas e parar.

## Contexto obrigatório

1. `branding/neovertix/tokens.json` — cores/tipografia (mesmos tokens do módulo 15: `#0A0E1A` fundo, `#F5F7FA` texto, `#43A047` destaque, Chakra Petch/Manrope)
2. `Social mídia IA/_context/marca.md` e `tom-de-voz.md` — números âncora, léxico, banidas
3. `Criador UGC/_context/tecnica-fotos-produto.md` — técnica de trava de fidelidade + lote por categoria (adaptar, não copiar — ver Passo 3)

## Instrução

### Passo 1 — Decidir: Pillow ou Nano Banana

- **Pillow** (default, custo zero): peça tipográfica simples — quote, dado/número âncora em destaque, frase de impacto sobre fundo sólido. Usar/evoluir `ig-saves-engine/create_image.py`.
- **Nano Banana** (`gemini-3.1-flash-image-preview`, via `google-genai`, chave já validada em `ig-saves-engine/.env` — `GOOGLE_API_KEY`; padrão de chamada já existe em `ig-saves-engine/generate_ideas.py`): só quando a peça exigir composição visual complexa, cena ou metáfora visual que Pillow não renderiza (ex: ilustração de um fluxo/processo, cena representando um conceito).
- Na dúvida entre os dois: começar por Pillow. Só escalar se o resultado ficar visualmente pobre pro que o roteiro pede.

### Passo 2 — Regras de prompt (quando usar Nano Banana)

Herdadas do guia externo (`tecnica-fotos-produto.md`), aplicar sempre:
- Parágrafo único por prompt (2-4 frases): proporção, fundo/paleta, posição do elemento central, iluminação, headline exata entre aspas (se houver texto), estilo visual.
- Headline curta (≤4 palavras) — modelo de imagem erra texto longo; texto mais extenso vai por overlay Pillow depois, nunca baked na geração.
- Nunca repetir fundo/composição entre peças do mesmo lote.

### Passo 3 — Trava de fidelidade + lote por categoria (adaptado da marca, não do produto físico)

O guia original trava fidelidade de *produto*; aqui a trava é de **identidade visual da marca**. Bloco fixo a colar no fim de todo prompt de imagem:

```
Identity lock: match the Neovertix visual identity exactly — navy-black
background (#0A0E1A), off-white text (#F5F7FA), single accent green
(#43A047), display type in a geometric condensed sans, body type in a
neutral humanist sans. Do not invent a logo, do not add any robot icon,
do not use purple or gradient effects, do not introduce a second accent
color.
```

- Geração em lote por categoria: agrupar por tipo de peça (ex: dado em destaque, citação, capa de reel, metáfora de processo) em vez de gerar peça a peça isolada — mesmo princípio do guia original, categorias adaptadas ao que o roteiro pedir.
- Rollout disciplinado: gerar 5-6 variações primeiro, nunca o lote inteiro de uma vez — mesmo princípio de `batchSize` pequeno já usado no resto do sistema (ver regra do Swarm no `CLAUDE.md` raiz).

### Passo 4 — Salvar e apresentar

- Salvar em `Social mídia IA/producao/criativos/YYYY-MM-DD/{slug-do-roteiro}/`.
- Apresentar ao Lucas como **preview**, indicando se foi Pillow ou Nano Banana e por quê.

### Passo 5 — Loop de edição

Toda peça é preview até o Lucas aprovar (mesma regra de `pixel.md` e do módulo 15) — ajustes aplicados e reapresentados até OK explícito. Nunca dar a peça por fechada sem essa confirmação.

## Regras

- Pillow é o caminho padrão; Nano Banana é exceção justificada, nunca o primeiro recurso.
- Nunca inventar logo, ícone de robô, gradiente roxo ou segunda cor de destaque.
- Nunca inventar número/dado fora de `marca.md` ou do roteiro aprovado.
- Nunca aprovar peça sem OK explícito do Lucas.
