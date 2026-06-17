# Análise de Perfis Instagram — 2026-06-17

**Nota de escopo:** `config/profiles.json` tem 56 perfis ativos. Para esta execução, foi analisada uma amostra de 15 perfis representando as 7 categorias (ia, marketing, automacao, creator, agencia, founder, negocio-digital), por decisão do usuário, para manter o tempo de execução viável. O Instagram bloqueia crawlers diretos — todos os dados abaixo vêm de WebSearch (resultados públicos indexados), não de scraping do perfil.

## Visão Geral dos Perfis

| Perfil | Categoria | Seguidores (aprox.) | Formato Dominante | Engajamento | Hook Padrão |
|--------|-----------|---------------------|--------------------|-------------|-------------|
| @nick_saraev | automacao | 508K | reels | alto | Comando + promessa ("Comment 'AUTOMATION' to get...") |
| @viverdeia.ai | ia | 113K | misto | medio | sem dados de hook |
| @ninja.automacoes | automacao | — | — | — | limitação de dados |
| @sujeitoprogramador | ia/tech | 165K | misto | medio | sem dados de hook |
| @opensession.co | agencia | 23K | misto | medio | sem dados de hook |
| @fabianocarvalhojr | founder | 66K | misto | medio | sem dados de hook |
| @rafa.grandi | marketing | 247 | — | baixo | limitação — handle não é o esperado |
| @charliehills | creator | 74K | reels/foto | alto | Afirmação provocativa sobre IA ("A verdade é que a IA não vai vender por você...") |
| @vendedorglobal | negocio-digital | 83K | misto | medio | sem dados de hook |
| @brusantanna.ai | ia | — | — | — | limitação de dados |
| @maestrosdaia | ia | — | misto | medio | sem dados de hook |
| @gestordeaudiencia | marketing | — | — | — | limitação de dados |
| @avora.ai | agencia | — | — | — | limitação de dados |
| @eduardocavalcanti | founder | — | — | — | limitação de dados |
| @humam__academy | ia | — | — | — | limitação — possível typo no handle |

---

## Análise Detalhada por Perfil

### @nick_saraev
**Categoria:** automacao
**Bio:** "Founder @ Maker School, LeftClick" — ajuda a "fazer a IA trabalhar pra você"

#### Padrões de Hook identificados
- Modelo: maioria_errando / comando direto — "Comment 'AUTOMATION' to get these AI..." / "Comment 'SYSTEM' to get these AI Automation..."
- Modelo: fenômeno nomeado — "SMMA to AI Agencies - The New Gold Rush!"

#### CTA dominante
- Padrão: palavra-chave nos comentários (ex: "AUTOMATION", "SYSTEM") para receber recurso gratuito

#### Tom de voz
- Adjetivos: direto, didático, orientado a resultado, confiante
- Conteúdo prático: roteiros, scripts e propostas reais usados para escalar a própria agência a $72K/mês; roadmap gratuito de 110 passos até $25K/mês

#### Métricas estimadas
- 344 posts, 508K seguidores
- Formato dominante: reels educativos

**limitacao_dados:** não foi possível confirmar estrutura completa (blocos do post) nem tamanho médio de texto — apenas títulos/hooks de reels via busca.

---

### @viverdeia.ai
**Categoria:** ia
**Bio:** "A Plataforma das Empresas que Crescem com IA" — +2.000 empresas aceleradas com IA Plug & Play

**limitacao_dados:** apenas dados de perfil (113K seguidores, 549 posts) — não foi encontrado hook, CTA ou estrutura de posts específicos via busca.

---

### @sujeitoprogramador
**Categoria:** ia/tech
**Bio:** Matheus Fraga, 12+ anos de experiência, 45K+ alunos

#### Conteúdo identificado
- Temas: dicas de design responsivo, UI interativa, bibliotecas para projetos, frontend/backend (React, Vue, Angular, Node.js, PHP, Java)
- Produto: "Fábrica de Aplicativos" (treinamento intensivo)

**limitacao_dados:** 165K seguidores, 2.996 posts confirmados — mas sem hook/CTA literal encontrado via busca.

---

### @opensession.co
**Categoria:** agencia
**Bio:** "Brand x UX/AI x Design Systems" — ajuda designers e marcas a evoluir a criatividade

**limitacao_dados:** 23K seguidores confirmados — perfil parece ser mais um serviço de design/UX com IA do que um criador de conteúdo educativo; sem hooks específicos encontrados.

---

### @fabianocarvalhojr
**Categoria:** founder
**Bio:** Founder da lasy.ai — foco em Marketing, Tecnologia e IA

**limitacao_dados:** 66K seguidores, 1.901 seguindo, 979 posts confirmados — sem hook/CTA literal encontrado via busca.

---

### @rafa.grandi
**Categoria:** marketing

**limitacao_dados:** o handle configurado aponta para um perfil pessoal (Rafael Grandi Borges, 247 seguidores, bio "Jurídico SPGG/RS e Pai do Cássio") que não corresponde ao perfil de marketing/growth esperado. Possível handle incorreto em `config/profiles.json` — recomenda-se revisão.

---

### @charliehills
**Categoria:** creator
**Bio:** Especialista em IA aplicada a negócios digitais (Vislo AI); marketer digital focado em pequenos negócios

#### Padrões de Hook identificados
- Modelo: paradoxo/contraste — "A verdade é que a IA não vai vender por você..."
- Modelo: pergunta retórica/provocação — "Quer fazer seu agente de IA vender enquanto você dorme?"
- Tema recorrente: "AGIR NO DIGITAL | MARKETING, AUTOMAÇÃO & IA"

#### Tom de voz
- Adjetivos: direto, prático, didático, sem rodeios — combina bem com o tom desejado pelo Lucas em `config/business.json`

#### Métricas estimadas
- 74K seguidores, 202 posts
- Formato dominante: mistura de reels e fotos/carrossel

**limitacao_dados:** estrutura completa do post (blocos internos) não confirmada — apenas hooks/títulos via busca.

---

### @vendedorglobal
**Categoria:** negocio-digital
**Bio:** Murilo Bevervanso — "E-commerce & IA | +100M Views"; chama a audiência de "Troop do MAESTRO"

**limitacao_dados:** 83K seguidores, 2.280 posts confirmados — sem hook/CTA literal encontrado via busca.

---

### @brusantanna.ai
**Categoria:** ia

**limitacao_dados:** nenhum dado específico encontrado via WebSearch — apenas resultados genéricos sobre ferramentas de IA para Instagram, não sobre o perfil em si.

---

### @maestrosdaia
**Categoria:** ia
**Bio:** Canal para dominar automação e IA no dia a dia do negócio sem programar, usando Make, n8n e Lovable

**limitacao_dados:** sem hook/CTA literal nem métricas de seguidores confirmadas via busca.

---

### @gestordeaudiencia
**Categoria:** marketing

**limitacao_dados:** a busca não retornou o perfil exato — resultados genéricos sobre "audiência no Instagram" e um perfil diferente ("Acelerador de Audiência", 122K seguidores). Não é possível confirmar dados de @gestordeaudiencia.

---

### @avora.ai
**Categoria:** agencia

**limitacao_dados:** encontrado apenas o site institucional (avoraai.io) — nenhum dado de posts ou perfil do Instagram via busca.

---

### @eduardocavalcanti
**Categoria:** founder

**limitacao_dados:** busca não retornou nenhum resultado específico sobre este perfil — apenas artigos genéricos de marketing digital.

---

### @humam__academy
**Categoria:** ia

**limitacao_dados:** possível erro de digitação no handle configurado. A busca encontrou um perfil muito similar, **@human___academy** (298K seguidores, "Maior Plataforma de IA para Criativos"), com 3 underscores em vez de 2 e "human" em vez de "humam". Recomenda-se verificar e corrigir em `config/profiles.json`.

---

## Perfis Sugeridos pelo Sistema
N/A — `config/profiles.json` já tinha perfis ativos (modo análise), Modo Descoberta não foi executado.

---

## Limitações de Dados

- **10 de 15 perfis** retornaram apenas dados de superfície (seguidores, bio, nicho) sem hooks/CTAs/estrutura específicos — o Instagram não expõe esse nível de detalhe a buscas públicas indexadas.
- **@ninja.automacoes** — busca retornou resultados sobre uma ferramenta de automação chamada "Insta Ninja", não sobre o perfil configurado. Sem dados confiáveis.
- **@rafa.grandi** — handle aparenta apontar para perfil pessoal não relacionado a marketing/growth. Revisar configuração.
- **@humam__academy** — possível erro de digitação; perfil correto pode ser @human___academy.
- **Cobertura parcial:** apenas 15 dos 56 perfis ativos foram analisados nesta execução (amostra por categoria). Os 41 perfis restantes não foram processados.
- Nenhum dado de engajamento (curtidas, comentários, taxa) pôde ser confirmado numericamente — todas as classificações de "engajamento" são estimativas qualitativas baseadas em seguidores e tom do conteúdo, não em métricas reais.
