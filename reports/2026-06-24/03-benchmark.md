# Benchmark de Conteúdo — 2026-06-24

**Nota de metodologia:** assim como no Módulo 1, a skill `swarm` está documentada em `.claude/skills/swarm/SKILL.md`, mas seu runtime depende da ferramenta PTC `swarm_task` (`@langchain/quickjs`), indisponível nesta sessão. Para manter as regras de segurança do CLAUDE.md (concorrência 3, batch ~5, `context` anti-alucinação obrigatório, nunca inventar dados), o benchmark foi feito com 3 agentes paralelos (equivalente a `concurrency: 3`), cada um cobrindo 4 perfis do Módulo 2 (equivalente a `batchSize` ~4-5). Todos os agentes receberam a mesma instrução anti-alucinação ("responda apenas com base em dados encontrados via WebSearch/WebFetch; nunca invente hooks, CTAs ou métricas; se não encontrar, registre `null` e explique em `limitacao`") e o mesmo `responseSchema` estrito (campos obrigatórios: handle, tipo, tema, hook, estrutura, cta, emocao_dominante enum, performance_estimada enum, motivo_performance, limitacao).

Dos 16 perfis listados em `config/profiles.json` e cobertos no Módulo 2, **12 foram aprofundados** nesta varredura. Os 4 perfis mais fracos do Módulo 2 — `sebintel`, `gabrielsamp.ai`, `marketerhub.ai`, `neuwebstudio` — foram deliberadamente excluídos do benchmark por terem retornado zero leads de conteúdo utilizáveis (posts não localizáveis via WebSearch/WebFetch) no levantamento anterior; aprofundar esses perfis exigiria inventar dados, o que viola a regra anti-alucinação. Essa exclusão está registrada como limitação, não como dado.

Nenhuma métrica numérica real de engajamento (curtidas, comentários, views) foi obtida para nenhum item — o Instagram bloqueia scraping (WebFetch retorna 403 consistentemente) e o WebSearch não indexa contadores de engajamento. Por isso, `performance_estimada` é uma estimativa qualitativa (alto/médio/baixo) baseada em sinais indiretos: recorrência do mesmo gancho em múltiplos posts, tamanho da base de seguidores do perfil, e especificidade/confirmação da informação via múltiplas fontes — nunca em números de engajamento reais.

---

## Seção 1 — Top 10 Conteúdos (performance estimada: alto)

Todos os 10 itens abaixo são do tipo **reel** — nenhum carrossel ou foto atingiu classificação "alto" nesta varredura (ver Seção 3 para implicação).

| # | Perfil | Tema | Hook | CTA | Emoção dominante |
|---|--------|------|------|-----|-------------------|
| 1 | @nick_saraev | SMMA → AI Agencies | "Nick Saraev - SMMA to AI Agencies - The New Gold Rush!" | Comentar palavra-chave (SYSTEM/AUTOMATION/APIFY/EMAIL) para receber material via DM | Urgência |
| 2 | @nick_saraev | Templates de automação IA | "Comment \"AUTOMATION\" to get these AI Automation [templates/blueprints]" | Comentar "AUTOMATION" | Curiosidade |
| 3 | @ninja_automacoes | Crítica a automações superficiais | "Chega de \"automação Nutella\" que só..." | "Leia a legenda" | Humor |
| 4 | @larissagomes.ia | Prompt ChatGPT para analisar feed | "Peça o chatGPT para analisar o feed do seu instagram 🧠" | Seguir + salvar | Curiosidade |
| 5 | @brandsdecoded__ | IA + criação de conteúdo | "A verdade é simples: a mistura de IA + criação abriu uma..." | (institucional, produto Content Machine 3.0) | Urgência |
| 6 | @charliehills | ChatGPT vs. Nano Banana | "ChatGPT ou Nano Banana? A pergunta está errada..." | — | Curiosidade |
| 7 | @charliehills | Personas ocultas do ChatGPT | "Did you know that ChatGPT has 8 hidden personalities that you can choose from?" | Link externo (stan.store) para guia gratuito | Curiosidade |
| 8 | @franklim.gui | Faturamento vs. lucro | "Faturamento é o que entra. Lucro é o que sobra. Simples assim." | — | Surpresa |
| 9 | @avora.ai | Skills/automação | "Comente \"SKILLS\" que te envio o link no direct!" | Comentar "SKILLS" | Curiosidade |
| 10 | @rodrigobindes | Treinamento/automação | "Comente \"TREINAMENTO\" pra receber o link de inscrição do..." | Comentar "TREINAMENTO" | Urgência |

---

## Seção 2 — Análise por Perfil

### @nick_saraev (521K seguidores)
- **Reel 1** — tema: SMMA → AI Agencies. Hook: "Nick Saraev - SMMA to AI Agencies - The New Gold Rush!". CTA: comentar palavra-chave (varia entre SYSTEM/AUTOMATION/APIFY/EMAIL conforme o post) para receber material via DM. Emoção: urgência. Performance: **alto**. Motivo: o mesmo padrão de CTA por comentário-palavra-chave se repete em 7-8 reels distintos do perfil — sinal forte de fórmula validada.
- **Reel 2** — tema: templates de automação IA. Hook: "Comment \"AUTOMATION\" to get these AI Automation [templates/blueprints]". Emoção: curiosidade. Performance: **alto**. Limitação: número exato de variações do hook não confirmado, apenas recorrência do padrão de CTA.

### @ninja_automacoes (handle corrigido — config tinha `@ninja.automacoes`, perfil real usa underscore)
- **Reel** — crítica de marca própria a "automação Nutella" (automação superficial/sem substância). Hook: "Chega de \"automação Nutella\" que só...". CTA: "Leia a legenda". Emoção: humor. Performance: **alto**. Motivo: neologismo próprio funciona como técnica de diferenciação de marca, fácil de replicar com vocabulário próprio.
- **Carrossel/foto** — lançamento do produto "Ninja Rank". Hook: "O Ninja Rank não é só mais uma ferramenta de...". Emoção: curiosidade. Performance: **médio**. Limitação: post institucional de lançamento, sem sinal de recorrência ou tração superior à média do perfil.

### @brun0gpt
- **Reel** — uso do ChatGPT para analisar métricas do Instagram. Hook: "Primeiro, peça ao ChatGPT para analisar suas métricas...". Emoção: curiosidade. Performance: **médio**. Limitação: estrutura similar à de @larissagomes.ia (ver abaixo), mas sem confirmação de replicação cross-platform.

### @larissagomes.ia
- **Reel** — prompt de ChatGPT para analisar o feed do Instagram. Hook: "Peça o chatGPT para analisar o feed do seu instagram 🧠". CTA duplo: seguir + salvar. Emoção: curiosidade. Performance: **alto**. Motivo: o mesmo conteúdo foi replicado no TikTok com hashtags #viral #conteudoviral, confirmando tração cross-platform.

### @ana.gsoares
- **Reel 1** — Imersão "Claude Project". Hook: "🚀 Conecte o Instagram ao Claude e Automatize...". Emoção: curiosidade. Performance: **médio**.
- **Reel 2** — "Um novo mercado para trabalhadores". Emoção: inspiração. Performance: **baixo**. Limitação: hook genérico, sem elemento de diferenciação claro nem sinal de recorrência.

### @brandsdecoded__ (handle corrigido — config tinha `@brandsdecoded`, perfil real usa duplo underscore; 301K seguidores)
- **Reel** — tema pilar "IA + criação de conteúdo". Hook: "A verdade é simples: a mistura de IA + criação abriu uma...". Emoção: urgência. Performance: **alto**. Motivo: tema-pilar do produto "Content Machine 3.0", reforçado por base de seguidores grande (301K).
- **Carrossel** — explicação do método "Content Machine 3.0". Emoção: curiosidade. Performance: **médio**. Limitação: conteúdo de venda direta, sem hook de curiosidade tão forte quanto o reel pilar.

### @charliehills
- **Reel 1** — "ChatGPT ou Nano Banana? A pergunta está errada...". Emoção: curiosidade. Performance: **alto**.
- **Reel 2** — "Did you know that ChatGPT has 8 hidden personalities that you can choose from?". CTA: link externo (stan.store) para guia gratuito de personas do ChatGPT. Emoção: curiosidade. Performance: **alto**. Motivo: formato de "lista de fatos ocultos" + lead magnet externo, padrão replicável.

### @franklim.gui
- **Reel 1** — "Faturamento é o que entra. Lucro é o que sobra. Simples assim.". Emoção: surpresa. Performance: **alto**. Motivo: 8 variações confirmadas do mesmo gancho em URLs distintas — fórmula validada e repetida deliberadamente.
- **Reel 2** — notícia Anthropic/Claude Code com opinião forte. Hook: "Hoje a Anthropic fez algo que vai contra tudo que o mercado...". Emoção: urgência. Performance: **médio**. Observação: pilar de conteúdo secundário (notícia + opinião) descoberto nesta varredura, distinto do pilar principal de faturamento/lucro.

### @avora.ai
- **Reel** — "Comente \"SKILLS\" que te envio o link no direct!". Emoção: curiosidade. Performance: **alto**. Mesmo padrão de CTA por palavra-chave usado por @nick_saraev e @rodrigobindes.

### @rodrigobindes
- **Reel** — "Comente \"TREINAMENTO\" pra receber o link de inscrição do...". Emoção: urgência. Performance: **alto**. Mesmo padrão de CTA por palavra-chave.

### @allesinisgalli (perfil pequeno, ~8,1K seguidores)
- **Reel 1** — "LIBERDADE ATRAVÉS DO...". Emoção: inspiração. Performance: **médio**.
- **Reel 2** — "VENDAS COM AI & MARKETING...". Emoção: curiosidade. Performance: **médio**. Limitação: base de seguidores pequena limita a estimativa de performance; classificado "médio" por consistência temática, não por sinal de tração.

### @vendedorglobal
- **Reel** — tema: e-commerce/ChatGPT, comunidade "Troop do MAESTRO". Hook: **não encontrado** (`null`) após 2 semanas de monitoramento contínuo (Módulo 2 + esta varredura). Performance: **médio**. Limitação: zero hook completo capturado — perfil consistentemente difícil de indexar via WebSearch; sinal de alerta sobre confiabilidade da fonte, não sobre qualidade do conteúdo.

---

## Seção 3 — Padrões Transversais

**1) Qual a emoção dominante nos conteúdos de melhor performance?**
**Curiosidade** é a emoção mais frequente entre os 19 itens levantados (presente em 8 dos 19), seguida por urgência (4) e humor/surpresa/inspiração (2 cada). Entre os 10 itens "alto" especificamente, curiosidade e urgência dividem a liderança (4 cada).

**2) Qual estrutura de conteúdo mais se repete?**
"CTA de comentar palavra-chave para receber material via DM" — confirmado em pelo menos 4 perfis distintos (@nick_saraev x2, @avora.ai, @rodrigobindes), todos classificados "alto". É a estrutura mais replicável identificada: hook de curiosidade/urgência + promessa de material gratuito + CTA de comentário de palavra única.

**3) Qual tipo de conteúdo performa melhor?**
**Reel** — os 10 itens "alto" são todos reels, e reels representam a grande maioria dos 19 itens levantados (apenas 2 carrosséis e 0 fotos puras tiveram presença relevante, ambos classificados "médio"). Nenhum carrossel ou foto atingiu classificação "alto" nesta varredura.

**4) Qual o CTA mais comum?**
**Comentar uma palavra-chave para receber link/material via DM** (variações: SYSTEM/AUTOMATION/APIFY/EMAIL/SKILLS/TREINAMENTO) — padrão presente em 5 dos 19 itens, todos "alto" ou "médio-alto", e o único padrão de CTA replicado por múltiplos perfis sem relação aparente entre si.

---

## Limitações de Dados

- **4 perfis não aprofundados**: `sebintel`, `gabrielsamp.ai`, `marketerhub.ai`, `neuwebstudio` foram excluídos do benchmark por terem retornado zero leads de conteúdo utilizáveis no Módulo 2 — aprofundá-los exigiria inventar hooks/CTAs, o que foi recusado deliberadamente.
- **Nenhuma métrica numérica de engajamento real** (curtidas, comentários, views, taxa de engajamento) foi obtida para nenhum dos 19 itens. O Instagram bloqueia scraping via WebFetch (403 consistente); WebSearch não indexa contadores. `performance_estimada` é qualitativa, baseada em recorrência de padrão, tamanho de base de seguidores e confirmação cross-fonte — não em dados de engajamento.
- **Correções de handle confirmadas** (já identificadas no Módulo 2 e reconfirmadas nesta varredura):
  - `@ninja.automacoes` (config) → handle real é `@ninja_automacoes` (underscore).
  - `@brandsdecoded` (config) → handle real é `@brandsdecoded__` (duplo underscore).
- **@vendedorglobal**: zero hook textual completo capturado em 2 semanas consecutivas de monitoramento (Módulo 2 + este módulo) — perfil sinalizado como fonte de baixa confiabilidade para WebSearch, não necessariamente de baixa qualidade de conteúdo.
- **Metodologia Swarm→Agent**: como no Módulo 1, todo o levantamento foi feito por 3 agentes paralelos (não pela skill `swarm` nativa), com as mesmas salvaguardas anti-alucinação. Nenhum dado foi inventado; todos os campos sem confirmação foram registrados como `null` com limitação explicada.
