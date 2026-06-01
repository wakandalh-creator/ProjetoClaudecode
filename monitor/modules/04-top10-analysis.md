# Módulo 4 — Análise Profunda dos Top 10 Conteúdos

## Objetivo

Para cada um dos 10 conteúdos de maior performance identificados no Módulo 3, fazer uma análise estratégica profunda: por que funcionou, qual padrão existe, se é replicável e como adaptar ao negócio do Lucas.

## Dependência

Requer `reports/YYYY-MM-DD/03-benchmark.md` — especificamente a tabela "Top 10 conteúdos de alta performance".

## Instrução para o agente

### Passo 1 — Carregar Top 10

Leia `reports/YYYY-MM-DD/03-benchmark.md` e extraia os 10 conteúdos da tabela principal.

Leia também `config/business.json` para ter o contexto do negócio do Lucas ao analisar replicabilidade.

### Passo 2 — Análise profunda via Swarm

**Tasks:** um objeto por conteúdo do Top 10.

```javascript
instruction: "Analise o conteúdo: perfil @{handle}, tipo {tipo}, tema '{tema}', hook '{hook}', estrutura '{estrutura}', emoção '{emocao_dominante}'. Responda as 6 perguntas estratégicas com base no contexto de negócio fornecido."

context: "Negócio do Lucas: {business_positioning}. Nicho: {possible_niches}. Público: {target_audience}. Objetivo de conteúdo: {content_goal}. Analise replicabilidade considerando esse contexto específico."

responseSchema: {
  type: "object",
  additionalProperties: false,
  properties: {
    handle: { type: "string" },
    tema: { type: "string" },
    porque_performou: { type: "string", description: "Hipótese fundamentada em 2-3 frases." },
    padrao_estrutural: { type: "string", description: "Qual estrutura narrativa ou visual se repete." },
    dor_ou_desejo: { type: "string", description: "Qual dor latente ou desejo o conteúdo ataca." },
    framework_replicavel: { type: "string", description: "Descreva o framework em passos: 1. X → 2. Y → 3. Z" },
    adaptacao_ao_negocio: { type: "string", description: "Como adaptar especificamente para o posicionamento de Lucas." },
    replicabilidade: { type: "string", enum: ["alta", "media", "baixa"] },
    justificativa_replicabilidade: { type: "string", description: "Por que essa classificação." },
    ideia_conteudo_adaptado: { type: "string", description: "Uma ideia concreta de conteúdo adaptado para o negócio de Lucas, com hook sugerido." }
  },
  required: ["handle", "tema", "porque_performou", "padrao_estrutural", "dor_ou_desejo", "framework_replicavel", "adaptacao_ao_negocio", "replicabilidade", "ideia_conteudo_adaptado"]
}

concurrency: 3
batchSize: 5
```

**Critérios de classificação de replicabilidade:**
- **Alta** — formato, hook e estrutura podem ser adaptados diretamente ao nicho de Lucas com mudança mínima de contexto
- **Média** — requer adaptação significativa de tema, linguagem ou persona
- **Baixa** — muito dependente da audiência, nicho ou persona específica do criador original

**Retry:**
```javascript
filter: { column: "replicabilidade", exists: false }
```

### Passo 3 — Classificar e ordenar

Com `rows()`, recupere todos os resultados.

Ordene: Alta replicabilidade → Média → Baixa.
Dentro de cada grupo, priorize os que têm `ideia_conteudo_adaptado` mais específica.

### Passo 4 — Gerar relatório

Escreva `reports/YYYY-MM-DD/04-top10-analise.md` com:

**Seção 1 — Alta Replicabilidade**
Para cada conteúdo nesta categoria: análise completa + ideia adaptada pronta.

**Seção 2 — Média Replicabilidade**
Análise resumida + ideia adaptada com ajustes necessários.

**Seção 3 — Baixa Replicabilidade**
Apenas registro do padrão para referência futura.

**Seção 4 — Frameworks Reutilizáveis**
Liste os frameworks identificados (independente de perfil) que podem ser usados repetidamente.

**Formato para cada conteúdo:**

```markdown
### #N — @handle | {tipo} | "{tema}"

**Por que performou:** {porque_performou}
**Padrão estrutural:** {padrao_estrutural}
**Dor/Desejo atacado:** {dor_ou_desejo}
**Framework:** {framework_replicavel}
**Replicabilidade:** Alta / Média / Baixa — {justificativa}

> 💡 **Ideia adaptada para Lucas:**
> {ideia_conteudo_adaptado}
```
