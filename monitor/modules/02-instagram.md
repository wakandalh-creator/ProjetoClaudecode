# Módulo 2 — Monitoramento de Perfis Instagram

## Objetivo

Analisar os perfis monitorados usando a skill `instagram-content-cloner` (Fase 1) para extrair padrões profundos de hook, estrutura, CTA, tom e performance.

## Instrução para o agente

### Passo 1 — Verificar lista de perfis

Leia `config/profiles.json`.

**Se `profiles` estiver vazio → MODO DESCOBERTA:**

Execute o Passo 1A antes do Passo 2.

**Se `profiles` tiver entradas ativas → MODO ANÁLISE:**

Pule para o Passo 2 diretamente.

---

### Passo 1A — Modo Descoberta (lista vazia)

Quando não há perfis configurados, o sistema descobre automaticamente.

**Execute WebSearch com as seguintes queries:**
- "melhores perfis instagram inteligência artificial brasil 2026"
- "top creators instagram automação marketing digital"
- "perfis instagram AI agency founder brasil seguir"
- "instagram influencer SaaS growth hacking brasil"
- "creator IA Claude automação conteúdo instagram"

Para cada resultado promissor, extraia: handle, categoria sugerida, justificativa em 1 frase.

**Agrupe por categoria** (ia, marketing, automacao, creator, agencia, founder, negocio-digital).

**Apresente ao usuário uma lista de 10-15 sugestões** no formato:

```
PERFIS SUGERIDOS PARA MONITORAMENTO
====================================
IA / Claude / Agentes:
  • @handle1 — motivo em 1 frase
  • @handle2 — motivo em 1 frase

Marketing / Growth:
  • @handle3 — motivo em 1 frase
  ...

Para confirmar perfis, diga:
"Adicione @handle1 e @handle3 em config/profiles.json"
```

Salve as sugestões também em `reports/YYYY-MM-DD/02-perfis-instagram.md` (seção "Perfis Sugeridos").

**Aguarde confirmação do usuário antes de prosseguir com a análise profunda.**

---

### Passo 2 — Análise com instagram-content-cloner (Fase 1)

Para cada perfil com `active: true` em `config/profiles.json`:

**Invoque a Fase 1 da skill `instagram-content-cloner`:**

Use WebSearch para coletar posts disponíveis publicamente do perfil:
- Query: `"{handle}" instagram posts reels 2026 site:instagram.com OR "{handle}" instagram conteúdo`
- Tente também WebFetch na URL do perfil (pode retornar metadados parciais)
- Se Instagram bloquear, use WebSearch ampliada: `"{handle}" site:instagram.com OR "{handle}" instagram viral`

**Para cada post encontrado, extraia segundo a Fase 1:**

```
Hook (1ª linha):
  - Modelo: paradoxo/contraste | fenômeno nomeado | maioria errando | transformação silenciosa
  - Exemplo exato da frase

Estrutura:
  - Fluxo narrativo (problema → contexto → decodificação → conexão → insight)
  - Nº de blocos, listas, bullet points, storytelling

CTA:
  - Tipo: palavra-chave nos comentários | pergunta reflexiva | DM implícita | link na bio
  - Exemplo exato

Tom de voz:
  - Formal/informal, analítico/emocional, urgente/calmo
  - 3-5 adjetivos + exemplo de frase característica

Tamanho:
  - Palavras aproximadas por tipo (educativo / prova social / produto)
```

**Use Swarm para processar perfis em paralelo:**

```javascript
// tasks: um objeto por perfil ativo
instruction: "Analise o perfil @{handle} ({url}) do Instagram. Use WebSearch para encontrar posts recentes. Extraia: hook_modelos (array), estrutura_tipica, cta_padrao, tom_adjetivos (array), tamanho_medio_palavras, top_posts_temas (array de strings)."

responseSchema: {
  type: "object",
  additionalProperties: false,
  properties: {
    handle: { type: "string" },
    hook_modelos: {
      type: "array",
      items: {
        type: "object",
        additionalProperties: false,
        properties: {
          modelo: { type: "string", enum: ["paradoxo_contraste", "fenomeno_nomeado", "maioria_errando", "transformacao_silenciosa", "outro"] },
          exemplo: { type: "string" },
          frequencia: { type: "string", enum: ["alta", "media", "baixa"] }
        },
        required: ["modelo", "exemplo", "frequencia"]
      }
    },
    estrutura_tipica: { type: "string", description: "Diagrama textual do fluxo." },
    cta_padrao: { type: "string" },
    cta_variacoes: { type: "array", items: { type: "string" } },
    tom_adjetivos: { type: "array", items: { type: "string" } },
    tom_exemplo_frase: { type: "string" },
    tamanho_medio_educativo: { type: "number" },
    formato_dominante: { type: "string", enum: ["reels", "carrossel", "foto", "misto"] },
    engajamento_estimado: { type: "string", enum: ["alto", "medio", "baixo"] },
    top_posts_temas: { type: "array", items: { type: "string" } },
    limitacao_dados: { type: "string" }
  },
  required: ["handle", "hook_modelos", "estrutura_tipica", "cta_padrao", "tom_adjetivos", "formato_dominante", "engajamento_estimado"]
}

concurrency: 3
batchSize: 5
context: "Analise apenas com base nos dados encontrados via busca. Se não encontrar posts suficientes, documente em 'limitacao_dados'. Nunca invente dados de engajamento."
```

**Retry obrigatório:**
```javascript
filter: { column: "hook_modelos", exists: false }
```

### Passo 3 — Validar e salvar

Use `rows()` para recuperar todos os resultados.
Verifique que cada perfil ativo tem ao menos um resultado.

Escreva `reports/YYYY-MM-DD/02-perfis-instagram.md` seguindo o template em `monitor/templates/report-instagram.md`.

## Nota sobre limitações do Instagram

O Instagram bloqueia crawlers. A estratégia é:
1. WebFetch na URL do perfil (captura metadados da página quando disponível)
2. WebSearch ampliada como fallback principal
3. Se nenhum dado for encontrado, o campo `limitacao_dados` é preenchido e o usuário é notificado

Nunca inventar dados. Documentar claramente o que foi e o que não foi coletado.
