# Análise de Perfis Instagram — 2026-08-24

## ⚠️ Nota metodológica (leia antes de usar os dados abaixo)

Nesta execução, o `WebFetch` para `instagram.com` (e para praticamente todo domínio externo testado, incluindo `heepsy.com`, `linktr.ee`, `tiktok.com` e até `en.wikipedia.org` como controle) retornou `EGRESS_BLOCKED` — bloqueio do proxy de rede da sessão, não específico do Instagram. Toda a coleta veio exclusivamente de **snippets indexados via WebSearch** (Google), que raramente capturam legendas completas, hooks/CTAs literais ou métricas de engajamento por post.

Além disso, o **orçamento de WebSearch da sessão (200 chamadas) se esgotou** antes de concluir buscas de aprofundamento para os últimos lotes processados (perfis dos lotes 8, 10, 11, 12 e 13), reduzindo ainda mais a profundidade de coleta para ~25 perfis do final da lista.

**Consequência prática:** para a maioria dos 61 perfis ativos, não foi possível confirmar hooks completos, estrutura narrativa, CTA padrão validado ou engajamento real (likes/comentários). Os dados abaixo são o máximo que pôde ser coletado de forma honesta, sem invenção — campos sem evidência real estão marcados como "não encontrado"/"indeterminado", conforme a regra do módulo. Perfis marcados com handle não confirmado tiveram resultados de busca ambíguos ou nulos e não devem ser usados para decisões sem verificação manual.

**Recomendação para o Lucas:** para hooks/CTAs/estrutura narrativa reais e métricas de engajamento por post, será necessário um método de coleta diferente (acesso autenticado ao Instagram, scraper dedicado autorizado, ou execução em ambiente sem bloqueio de egress) — WebSearch/WebFetch genéricos não são suficientes para esse nível de profundidade.

---

## Visão Geral dos Perfis

| Perfil | Categoria | Formato Dominante | Engajamento | Seguidores (aprox., não verificado) | Hook/CTA identificado |
|---|---|---|---|---|---|
| @charliehills | creator | indeterminado | indeterminado | 88K | não encontrado |
| @yikC | creator | indeterminado | indeterminado | — | perfil não localizado na busca |
| @eujoaotorresz | creator | indeterminado | indeterminado | — | handle não confirmado (risco de mistura de identidade) |
| @fabianocarvalhojr | founder | indeterminado | indeterminado | 130K | não encontrado (verbatim) |
| @rafa.grandi | marketing | indeterminado | indeterminado | — | perfil-alvo não confirmado (só achado perfil de 247 seguidores, provável pessoa diferente) |
| @brusantanna.ai | ia | indeterminado | indeterminado | — | não encontrado |
| @vendedorglobal | negocio-digital | indeterminado (indício reels) | alto | 83K | não encontrado (verbatim) |
| @oluizmain | creator | indeterminado | alto | 215K | "🍀 Nunca foi sorte. #videomakermobile" (fragmento) |
| @nick_saraev | automacao | reels | alto | ~500-550K | "Comment [PALAVRA-CHAVE]" (lead magnet) |
| @nathanhodgson | ia | indeterminado | alto | 128K (via handle alternativo @nathanhodgson.ai) | "I created an AI agent in under 30..." |
| @ai | ia | não encontrado | indeterminado | — | handle genérico, sem dados verificáveis |
| @ana.gsoares | marketing | não encontrado | alto | 146K | "Esse prompt te ajuda a encontrar vagas..." |
| @chase.h.ai | ia | não encontrado | alto | ~221-228K | "DM 'Ready' to Apply For 1:1 Mentorship" |
| @leosoares.ia | ia | reels | alto | 219K | "Comenta [PALAVRA] que eu te mando" |
| @gabriel.adamuchi | creator | reels | indeterminado (IG) | — (TikTok 195K) | "IA FÁCIL Prompt: ..." |
| @viverdeia.ai | ia | reels | alto | 129K | "Acesse o link da bio e faça parte..." |
| @ninja.automacoes | automacao | reels (indício) | indeterminado | — | não encontrado |
| @nikolassasso | creator | reels | alto | 185K | não encontrado |
| @eduardocavalcanti | founder | indeterminado | alto | 184K | não encontrado |
| @jonylan | creator | reels | alto | 306K | "Já me siga para..." |
| @allesinisgalli | founder | indeterminado | indeterminado (dados inconsistentes) | 8K–61K (fontes conflitantes) | não encontrado |
| @lonamkt | marketing | reels | baixo | ~4.3K | "Chaves para o Primeiro Milhão (digital)..." |
| @gabrielbarbosa.oficial | creator | misto | indeterminado | ~7.8K | não encontrado (verbatim) |
| @opensession.co | agencia | misto | indeterminado | 23K | "Comment 'OS' and we'll send you 150+ design resources" — nota: agência de design em San Diego (EUA), foco em UX/branding, não no nicho BR de negócio digital |
| @leandroladeiran | marketing | indeterminado (IG) | indeterminado (forte no TikTok) | 882K (TikTok, não IG) | "Quem não sabe COPYWRITING dançou..." (origem: TikTok, não confirmado no IG) |
| @christiantriad | creator | indeterminado | alto (dados inconsistentes) | 349K–571K | não encontrado |
| @oneyaraujo | creator | reels | alto | ~2M (fonte externa) | "me segue" / "link na bio" |
| @geracaotechs | ia | indeterminado | indeterminado | — (Threads 11.2K) | não encontrado no IG |
| @amandadinizmkt | marketing | indeterminado | indeterminado | — | não encontrado no IG (só TikTok) |
| @human___academy | ia | reels | alto | 260K | "A IA não cria sozinha, ela reorganiza..." |
| @geiss11 | creator | indeterminado | indeterminado | 45K | não encontrado |
| @nelmoricalde | creator | indeterminado | indeterminado | — | não encontrado |
| @rodrigotadewald | marketing | reels (amostra pequena) | indeterminado | — | "Essa é polêmica, eu sei: Mas o que é melhor?..." |
| @sujeitoprogramador | ia | reels | alto | 168K | "Se você não passou por isso então você ainda não é dev júnior" |
| @jonathan_kamargo | creator | indeterminado | indeterminado | — | handle não confirmado |
| @marianatorre.s | marketing | indeterminado | indeterminado | — | não encontrado |
| @marketerhub.ai | marketing | reels (indício) | indeterminado | — | não encontrado |
| @marcelaluzzio | marketing | reels | alto | 226K | "Tenha acesso a sua equipe de IA agora. 👇 Comente..." |
| @gestordeaudiencia | marketing | indeterminado | indeterminado | — | perfil não confirmado na busca |
| @sebintel | ia | reels (indício) | indeterminado | — | não encontrado |
| @avora.ai | agencia | indeterminado | indeterminado | — | não encontrado |
| @ogabrieeldias | creator | indeterminado | indeterminado | — | handle não confirmado |
| @rodrigobindes | founder | indeterminado | alto | 278K | não encontrado (verbatim) |
| @franklim.gui | creator | indeterminado | médio | 46K | não encontrado (verbatim) |
| @gabrielsamp.ai | ia | indeterminado | indeterminado | — | não encontrado no IG (só achado no TikTok) |
| @maestrosdaia | ia | indeterminado | indeterminado | — (TikTok 71.4K) | não encontrado no IG |
| @brandsdecoded__ | marketing | indeterminado | alto | 306K | não encontrado (verbatim) |
| @anatex | creator | reels | alto | 705K | "Aqui está: 👇 1️⃣ - Salva esse REELS agora 📌" |
| @larissagomes.ia | ia | indeterminado | baixo/médio | 15K | "Peça o chatGPT para analisar o feed do seu instagram..." |
| @thiagozaao | creator | indeterminado | indeterminado | — | handle não confirmado |
| @neuwebstudio | agencia | misto | médio | 52K | não encontrado (verbatim) — nicho real: web design, não negócio digital BR |
| @laschuk | founder | reels | médio | 36K | "copie daqui 👇..." (fragmento) |
| @maestroptompts | ia | indeterminado | indeterminado | — | handle não confirmado |
| @faladantasmkt | marketing | indeterminado | alto | 99K | não encontrado (verbatim) |
| @lindsay.ia | ia | indeterminado | indeterminado | — | handle não confirmado |
| @andrevictor.m | marketing | reels | indeterminado | ~200K | não encontrado (verbatim) |
| @drisiano | creator | indeterminado | indeterminado | — | handle não confirmado |
| @brun0gpt | ia | indeterminado | indeterminado | — | não encontrado |
| @maxcarrau.ia | ia | indeterminado | indeterminado | — | não encontrado |
| @noevarner | creator | indeterminado | indeterminado | — | não encontrado |
| @yikchanltd | creator | reels (indício) | alto | ~79K | "5 Day AI Training..." (origem: Substack, não confirmado no IG) — possível duplicata de @yikC, não confirmado |

---

## Análise Detalhada — Perfis com Dados Reais Relevantes

*(Os demais 40+ perfis não tiveram dados suficientes além do que consta na tabela acima; ver seção "Limitações de Dados" para a lista completa.)*

### @nick_saraev
**Categoria:** automacao | **Bio:** "🚀 Founder @ Maker School 🤖 Helping 2000+ beginners land their First AI client"

- **CTA dominante:** comentar uma palavra-chave (AUTOMATION, APIFY, EMAIL) para receber template/material gratuito — padrão observado repetidamente em títulos de reels
- **Estrutura observada:** gancho de resultado/ferramenta + CTA de comentário para lead magnet
- **Formato:** reels (existência de contas-fã dedicadas a repostar seus reels: @reelsofnicksaraev, @bestofnicksaraev)
- **Temas:** automação com IA (Make.com, Apify), agência de automação, primeiro cliente de IA, escalar agência a $25K/mês
- **Limitação:** nenhuma legenda foi capturada em texto integral — hooks acima são padrão inferido de títulos truncados, não citações literais completas.

### @leosoares.ia
**Categoria:** ia | **Bio:** "🔹 CEO Acelera IA 🤖 Inteligência Artificial p/ Negócios 💰 IA tem que gerar RESULTADO ❇️"

- **CTA dominante:** "Comenta [palavra-chave] que eu te mando/envio" — confirmado em múltiplos reels reais e distintos (ex: "IA12", "IA04", "ACELERA IA")
- **Estrutura observada:** promessa de material/ferramenta + CTA de comentário para liberar acesso (comment-to-unlock)
- **Formato:** reels (múltiplas URLs /reel/ distintas; nenhum carrossel/foto localizado)
- **Engajamento:** alto — 219K seguidores, 2.226 posts; parceiro confirmado de rede de afiliados (Hotmart FIRE)
- **Temas:** IA para negócios/lançamentos, automação empresarial (Plataforma Acelera IA), parcerias/afiliados

### @anatex
**Categoria:** creator | **Bio:** "Coloque a IA para trabalhar no seu negócio: ganhe tempo, reduza custos e crie novas oportunidades de receita nessa nova era"

- **Hook real:** "Aqui está: 👇 1️⃣ - Salva esse REELS agora 📌 Nunca mais ..." (lista numerada + CTA de salvar embutido no início)
- **CTA dominante:** "Salva esse REELS agora"
- **Formato:** reels
- **Engajamento:** alto — 705K seguidores, 1.411 posts (maior perfil confirmado da lista)
- **Temas:** IA para negócios, produtividade/redução de custos com IA

### @larissagomes.ia
**Categoria:** ia | **Bio:** "💻 Te ensino a criar um negócio enxuto e que vende: você + IA ⚡️ Compartilho o que aplico sobre IA. Domine o chatGPT👇🏻"

- **Hook real (via cross-post TikTok, mesmo handle):** "Peça o chatGPT para analisar o feed do seu instagram 🧠 ANTES DE MAIS NADA... siga @larissagomes.ia para receber mais conteúdos como esse..."
- **Estrutura:** tutorial passo a passo numerado (prompt pronto para copiar/colar): 1️⃣ Elementos Visuais, 2️⃣ Clareza da Mensagem, 3️⃣ Sugestões de Melhorias
- **CTA:** "siga @larissagomes.ia para receber mais conteúdos como esse" + "📩 Salva pra lembrar de analisar o seu perfil!"
- **Tamanho estimado:** ~250 palavras (amostra única, não é média confiável)
- **Engajamento:** baixo/médio — 15K seguidores, 262 posts
- **Ressalva:** legenda encontrada veio de cópia cross-postada no TikTok, pode ser outlier não representativo do padrão típico do Instagram.

### @marcelaluzzio
**Categoria:** marketing | **Bio:** "Marcela Lúzio | Marketing de Conteúdo & I.A"

- **CTA (fragmento real):** "Tenha acesso a sua equipe de IA agora. 👇 Comente '[palavra cortada]'"
- **Formato:** reels
- **Engajamento:** alto — 226K seguidores, 964 posts; fonte cita alcance de "+1 milhão de pessoas/mês"
- **Temas:** uso de IA/ChatGPT para crescer nas redes, conteúdo viral em vídeo curto, criação rápida de posts/apresentações com IA

### @human___academy
**Categoria:** ia | **Bio:** "A Maior Escola de IA para Criativos" — "Learn to direct technology with creativity"

- **Hooks reais (fragmentos):** "🧠 A IA não cria sozinha, ela reorganiza. Se..." / "A IA chegou no VFX. E não é só pra gerar..." / "Como criar mãos reais usando IA 👐 Você..."
- **Estrutura:** conceito de IA ligado a aplicação prática em VFX/criação visual, formato mini-tutorial/lista numerada
- **Formato:** reels (todos os 9 resultados indexados eram /reel/)
- **Engajamento:** alto — 260K seguidores, 450 posts
- **Temas:** VFX com IA, criação de mãos/imagens realistas, clones com IA, evento "AI Videolab"

### @sujeitoprogramador
**Categoria:** ia | **Bio:** perfil de Matheus Fraga, programador há +12 anos, +45.000 alunos

- **Hooks reais:** "Se você não passou por isso então você ainda não é dev júnior" / "Quem nunca passou por isso ta trabalhando errado" (padrão "teste de pertencimento")
- **Estrutura:** abertura de "teste de pertencimento" (se você [passou/não passou] por X, você [é/não é] dev) seguida de conteúdo técnico
- **Formato:** reels (~2.5K reels indexados)
- **Engajamento:** alto — 168K seguidores, 3.040 posts
- **Temas:** desenvolvimento web (JS, HTML/CSS, React), responsividade/Flexbox, referências de design para devs

### @oneyaraujo
**Categoria:** creator | **Bio:** "Marketing Viral" — criador do curso "Código Viral"

- **CTA dominante:** "me segue" / "link na bio" — recorrente nos títulos indexados
- **Hook real:** "Não diga 'Lá ele' sem antes..." (frase truncada)
- **Formato:** reels (todos os resultados eram /reel/)
- **Engajamento:** alto — ~2 milhões de seguidores (fonte externa: reportei.com), curso com +50 mil alunos
- **Temas:** marketing viral, hooks/ganchos para reels, curso próprio "Código Viral"

### @nathanhodgson (⚠️ discrepância de handle)
O handle exato fornecido (`nathanhodgson`) não corresponde a nenhum perfil ativo relevante. O perfil real do nicho é **@nathanhodgson.ai** — reportar essa divergência antes de usar os dados. Bio: "Built a 6-Figure Business Powered By AI • Trusted by Google · Meta · OpenAI". 128K seguidores, 339 posts.

### @yikchanltd (possível duplicata de @yikC)
Nome de exibição "Sifu Yik Chan — A.I., eCom, Business and Life Mentor". Não foi possível confirmar nem descartar se é a mesma pessoa/conta de @yikC (que não teve nenhum dado localizado). Recomenda-se verificação manual e, se confirmado duplicado, consolidar ou remover uma entrada de `config/profiles.json`.

---

## Perfis Sugeridos pelo Sistema
N/A — sistema em Modo Análise (lista de perfis já configurada em `config/profiles.json`, Passo 1A não executado).

---

## Limitações de Dados

**Limitação técnica geral (afeta todos os 61 perfis):** `WebFetch` bloqueado por proxy de egress de rede (`EGRESS_BLOCKED`) para instagram.com e para praticamente todo domínio externo testado nesta sessão — nenhum perfil pôde ser acessado diretamente. Toda a coleta veio de snippets truncados do WebSearch. O orçamento de WebSearch da sessão (200 chamadas) se esgotou antes da conclusão dos lotes finais, reduzindo ainda mais a cobertura dos últimos ~25 perfis processados.

**Perfis sem nenhum dado real verificável** (nem bio, nem seguidores, nem conteúdo — recomenda-se verificar handle ou tentar coleta manual):
@yikC, @eujoaotorresz (handle ambíguo — múltiplos perfis parecidos, nenhum confirmado), @ai (handle genérico, resultados poluídos), @ninja.automacoes (handle ambíguo com contas parecidas), @nelmoricalde, @jonathan_kamargo (handle não localizado), @gestordeaudiencia (perfil não confirmado existir), @avora.ai, @ogabrieeldias (handle ambíguo), @gabrielsamp.ai (só achado no TikTok), @maestroptompts (handle não localizado), @lindsay.ia (handle não localizado), @drisiano (handle não localizado), @brun0gpt, @maxcarrau.ia, @noevarner, @thiagozaao (handle não localizado), @marianatorre.s, @sebintel, @geracaotechs (só Threads), @amandadinizmkt (só TikTok), @maestrosdaia (só TikTok), @geiss11 (só bio).

**Perfis com dados parciais e ressalvas importantes:**
- @rafa.grandi — único perfil com esse handle exato encontrado tem 247 seguidores e é analista jurídico, não corresponde ao perfil de marketing/growth esperado. Dados não atribuídos por precaução.
- @allesinisgalli — contagem de seguidores inconsistente entre fontes da mesma ferramenta (8K vs 61K).
- @christiantriad — contagem de seguidores inconsistente entre buscas (349K vs 571K).
- @leandroladeiran — métricas fortes e único hook real encontrados são do TikTok (mesmo handle), não confirmados no Instagram; há pelo menos 3 handles de Instagram diferentes associados ao nome "Leandro Ladeira".
- @opensession.co — parece ser uma agência de design/branding sediada em San Diego (EUA), não um perfil do nicho de negócio digital BR — vale reavaliar o encaixe na categoria.
- @neuwebstudio — nicho real aparenta ser web design/UX, não diretamente IA/negócio digital BR.

**Handles a revisar em `config/profiles.json`:**
- `nathanhodgson` → perfil ativo real parece ser `nathanhodgson.ai`.
- `yikchanltd` vs `yikC` → possível duplicata, não confirmada.

**Nenhum dado de engajamento por post (likes/comentários) foi encontrado para nenhum dos 61 perfis** — apenas contagens de seguidores/posts aproximadas via snippets de busca, não verificadas diretamente na página. Os campos `engajamento_estimado` marcados como "alto/médio/baixo" na tabela usam a contagem de seguidores como proxy, não engajamento real medido.
