# Análise de Perfis Instagram — 2026-09-28

**Modo de execução:** Análise (lista de perfis já configurada em `config/profiles.json`, Passo 2 do Módulo 2 executado diretamente, sem etapa de descoberta) — execução automatizada semanal (rotina agendada "Monitor Instagram - Módulo 2 semanal").

**Nota metodológica geral:** Em todas as tentativas desta execução, o WebFetch direto para `instagram.com` retornou bloqueio de rede (`EGRESS_BLOCKED`) pelo proxy do ambiente — confirmado nos 61 perfis. Toda a coleta foi feita via WebSearch (múltiplas queries por perfil, processadas em 13 lotes de ~5 perfis, concorrência 3), que majoritariamente indexa metadados de perfil (bio, contagem de seguidores/posts) e menções de terceiros (agregadores, blogs, cross-posts em TikTok/Threads/YouTube), raramente o texto literal de posts individuais do Instagram. **Nenhum dado de engajamento, hook, CTA ou tema de post foi inventado.** Onde a busca não trouxe evidência direta e específica do perfil, o campo foi marcado "dado insuficiente" e a limitação foi documentada por perfil. Hooks/CTAs vindos de conteúdo espelhado em outra rede (TikTok, Threads, YouTube) e não confirmados como publicados literalmente no Instagram estão sinalizados como tal. Onde a análise identificou ambiguidade entre contas homônimas ou um handle sem correspondência confiável, isso está sinalizado explicitamente — nenhum dado de conta diferente foi atribuído ao perfil-alvo. O orçamento de buscas da sessão esgotou-se ao final da execução (últimos ~6 perfis dos lotes 11-13), reduzindo a profundidade de refinamento disponível para esses casos — sinalizado individualmente.

**Perfis com handle não localizado ou não confirmável nesta execução:** @yikC, @eujoaotorresz, @ai, @jonathan_kamargo, @drisiano, @maestroptompts, @lindsay.ia, @thiagozaao, @gestordeaudiencia, @gabrielsamp.ai, @maxcarrau.ia, @yikchanltd (busca esgotada, sem confirmação).

**Perfis com forte ambiguidade entre contas homônimas (dados abaixo referem-se à melhor correspondência identificada, sinalizada em cada seção):** @nathanhodgson (dados de @nathanhodgson.ai), @eduardocavalcanti (identidade real não confirmada apesar de conta localizada), @noevarner (nenhum dado atribuído com confiança — números pertencem a @noevarner.ai).

**Alerta de possível handle incorreto:** o único @rafa.grandi localizado (Rafael Grandi Borges, analista jurídico do SPGG/RS, 247 seguidores, 36 posts) não corresponde à categoria "marketing" esperada — mesmo achado da execução de 2026-09-21. Recomenda-se confirmar o handle exato com o Lucas.

**Divergências numéricas não resolvidas entre fontes (reportadas, não reconciliadas artificialmente):** @allesinisgalli (8.155 vs 61,3K seguidores), @christiantriad (~304K vs ~571K seguidores), @faladantasmkt (~99K vs ~108K seguidores), @maestrosdaia ("9M seguidores" retornado por um resumo de busca é suspeito/não confiável e não deve ser usado).

---

## Visão Geral dos Perfis

| Perfil | Categoria | Formato Dominante | Engajamento | Hook / Padrão Observado |
|--------|-----------|--------------------|-------------|--------------------------|
| @charliehills | creator | dado insuficiente | dado insuficiente (~88K) | dado insuficiente |
| @yikC | creator | dado insuficiente | dado insuficiente | perfil não localizado |
| @eujoaotorresz | creator | dado insuficiente | dado insuficiente | perfil não localizado |
| @fabianocarvalhojr | founder | dado insuficiente | dado insuficiente (~130K) | "Quem mais? 😅 ➡️ Siga..." (truncado) |
| @rafa.grandi | marketing | dado insuficiente | baixo (~247) | ⚠️ perfil encontrado não bate com categoria |
| @brusantanna.ai | ia | dado insuficiente | dado insuficiente | CTA de comentário (via TikTok, não confirmado no IG) |
| @vendedorglobal | negocio-digital | reels (indício) | médio (~83K) | "Treino apenas quem está pronto p/ lucrar" (bio) |
| @oluizmain | creator | reels (indício) | dado insuficiente | dado insuficiente |
| @nick_saraev | automacao | reels | alto (~550K) | "Comment [PALAVRA] to get [recurso]" (4+ variações) |
| @nathanhodgson | ia | dado insuficiente | dado insuficiente (~128K, via .ai) | dado insuficiente — handle ambíguo |
| @ai | ia | dado insuficiente | dado insuficiente | perfil não localizado |
| @ana.gsoares | marketing | dado insuficiente | dado insuficiente (~146K) | dado insuficiente |
| @chase.h.ai | ia | dado insuficiente | dado insuficiente (~221-228K) | "DM 'Ready' to Apply For 1:1 Mentorship" |
| @leosoares.ia | ia | dado insuficiente | dado insuficiente (~219K) | dado insuficiente (bio inconsistente entre buscas) |
| @gabriel.adamuchi | creator | reels (indício) | dado insuficiente (métrica TikTok, não atribuída) | dado insuficiente |
| @viverdeia.ai | ia | dado insuficiente | dado insuficiente (~109K) | CTA "Comenta 'TEMPO'..." (truncado) |
| @ninja.automacoes | automacao | dado insuficiente | dado insuficiente (~34K) | "Faturei R$1MM sozinho, com agentes de IA" (bio) |
| @nikolassasso | creator | dado insuficiente | dado insuficiente (~181K) | "Criei robôs que fazem o trabalho duro por mim" (bio) |
| @eduardocavalcanti | founder | dado insuficiente | dado insuficiente (~26K) | dado insuficiente — forte ambiguidade de identidade |
| @jonylan | creator | dado insuficiente | dado insuficiente (~306K) | dado insuficiente |
| @allesinisgalli | founder | dado insuficiente | baixo-médio (conflito 8,2K/61,3K) | dado insuficiente |
| @lonamkt | marketing | dado insuficiente | dado insuficiente (~4,3K, "2 posts" suspeito) | "Primeiro milhão aos 18" (bio) |
| @gabrielbarbosa.oficial | creator | dado insuficiente | dado insuficiente (~7,8K) | "+10MM faturados na internet" (bio) |
| @opensession.co | agencia | dado insuficiente | dado insuficiente (~25K) | dado insuficiente |
| @leandroladeiran | marketing | dado insuficiente | dado insuficiente (IG não confirmado) | contraste/humor (via TikTok, não confirmado no IG) |
| @christiantriad | creator | reels (indício) | dado insuficiente (conflito ~304K/~571K) | citação de autoridade (Bill Gates) |
| @oneyaraujo | creator | reels | dado insuficiente (~2M) | Gancho → Benefício → Mostre → CTA ("Código Viral") |
| @geracaotechs | ia | dado insuficiente | dado insuficiente (IG não confirmado) | apresentação de ferramenta de IA + CTA "Comente 'Eu quero'" (via Threads) |
| @amandadinizmkt | marketing | dado insuficiente | dado insuficiente | dado insuficiente — bio conflitante |
| @human___academy | ia | reels (indício) | dado insuficiente (~260K) | dado insuficiente (série "AXIS") |
| @geiss11 | creator | dado insuficiente | dado insuficiente (~45K) | dado insuficiente |
| @nelmoricalde | creator | dado insuficiente | dado insuficiente | dado insuficiente |
| @rodrigotadewald | marketing | dado insuficiente | dado insuficiente (~232K) | dado insuficiente |
| @sujeitoprogramador | ia | dado insuficiente | dado insuficiente (~165K) | "Vagas abertas" (elemento de bio) |
| @jonathan_kamargo | creator | dado insuficiente | dado insuficiente | perfil não localizado |
| @marianatorre.s | marketing | dado insuficiente | dado insuficiente | dado insuficiente — quase sem dados |
| @marketerhub.ai | marketing | dado insuficiente | dado insuficiente | dado insuficiente |
| @marcelaluzzio | marketing | reels (indício forte) | médio-alto (~226K) | estrutura gancho/retenção/CTA (tema, sem citação verbatim) |
| @gestordeaudiencia | marketing | dado insuficiente | dado insuficiente | perfil não localizado |
| @sebintel | ia | reels (indício) | dado insuficiente | dado insuficiente |
| @avora.ai | agencia | dado insuficiente | dado insuficiente | "Siga @avora.ai para conteúdos diários sobre IA na prática!" |
| @ogabrieeldias | creator | dado insuficiente | dado insuficiente | dado insuficiente — só nome confirmado |
| @rodrigobindes | founder | dado insuficiente | médio-alto (~278K) | "Mostro como chegar aos 100k/mês com agência de mkt" (bio) |
| @franklim.gui | creator | dado insuficiente | médio (~104K) | "documentei nos destaques minha jornada até R$7M em 3 anos" (bio) |
| @gabrielsamp.ai | ia | dado insuficiente | dado insuficiente | perfil não localizado no IG (só TikTok) |
| @maestrosdaia | ia | reels (indício fraco) | dado insuficiente (número "9M" suspeito, descartado) | dado insuficiente |
| @brandsdecoded__ | marketing | carrossel | médio-alto (~301K) | "Decodificando o futuro do marketing com AI" (bio) |
| @anatex | creator | reels | alto (~718K) | dado insuficiente (fragmentos truncados) |
| @larissagomes.ia | ia | dado insuficiente | baixo-médio (~15K) | "Te ensino a criar um negócio enxuto e que vende: você + IA" (bio) |
| @thiagozaao | creator | dado insuficiente | dado insuficiente | perfil não localizado |
| @neuwebstudio | agencia | misto (não confirmado) | dado insuficiente (~52K) | dado insuficiente |
| @laschuk | founder | dado insuficiente | dado insuficiente (~36K) | dado insuficiente |
| @maestroptompts | ia | dado insuficiente | dado insuficiente | perfil não localizado |
| @faladantasmkt | marketing | dado insuficiente | dado insuficiente (conflito ~99K/~108K) | dado insuficiente |
| @lindsay.ia | ia | dado insuficiente | dado insuficiente | perfil não localizado |
| @andrevictor.m | marketing | reels (indício) | dado insuficiente (~244K) | dado insuficiente |
| @drisiano | creator | dado insuficiente | dado insuficiente | perfil não localizado |
| @brun0gpt | ia | dado insuficiente | dado insuficiente (~157K) | dado insuficiente |
| @maxcarrau.ia | ia | dado insuficiente | dado insuficiente | perfil não localizado (handle exato) |
| @noevarner | creator | dado insuficiente | dado insuficiente | dado insuficiente — ambiguidade com @noevarner.ai |
| @yikchanltd | creator | dado insuficiente | dado insuficiente | perfil não localizado (busca esgotada) |

---

## Análise Detalhada por Perfil

### @charliehills
**Categoria:** creator
**Bio:** "💙 I help you (actually) use AI 📧 collabs@charliehills.ai 👇 100+ free AI prompts, guides & tools"
**Seguidores/posts:** 88K seguidores, 324 seguindo, 260 posts
**Tom (inferido da bio, baixa confiança):** acessível, prático, direto
**Top temas (inferido da bio):** prompts de IA, ferramentas de IA, guias de IA
**Limitação:** WebFetch bloqueado. Homônimos existem (@charliehills.studio, @charliehillsracing, @charliehills.ai) mas handle exato confirmado consistentemente em 3 buscas — confiança alta na identidade, mas nenhuma legenda de post real recuperada.

### @yikC
**Categoria:** creator
**Limitação:** Perfil NÃO localizado com confiança. Buscas retornaram apenas homônimos não relacionados (@yikc_ywca, @yikcafeoficial, @yikchanltd — handle diferente, @ykc, @yik.milk). Nenhum dado atribuído.

### @eujoaotorresz
**Categoria:** creator
**Limitação:** Handle exato NÃO localizado. Candidato mais próximo @joaotorresz (sem "eu", 2.039 seguidores, só 5 posts, Portugal) é handle diferente — não atribuído por risco de erro.

### @fabianocarvalhojr
**Categoria:** founder
**Bio:** "Founder lasy.ai — Crio Agentes de IA que vendem e operam Negócios 24/7"
**Seguidores/posts:** 130K seguidores, 1.865 seguindo, 1.417 posts
**Hook/estrutura:** [{modelo: outro, exemplo: "Quem mais? 😅 ➡️ Siga @fabianocarvalhojr que te ensino...", frequência: baixa}] — truncado, baixa confiança
**Tom:** direto, didático, informal (baixa-média confiança)
**Top temas:** Agentes de IA, automação de negócios/vendas com IA
**Limitação:** Handle confirmado com alta confiança (cross-check YouTube/Threads). Só uma legenda truncada recuperada — insuficiente para padrões completos.

### @rafa.grandi
**Categoria:** marketing (dada) — NÃO CONFERE com o que foi encontrado
**Bio:** "Analista Jurídico SPGG/RS e Pai do Cássio" (Rafael Grandi Borges)
**Seguidores/posts:** 247 seguidores, 284 seguindo, 36 posts
**Engajamento estimado:** baixo (~247 — perfil pessoal pequeno)
**⚠️ Alerta:** único @rafa.grandi localizado é perfil pessoal de analista jurídico, sem indício de atuação em marketing — mesmo achado da execução de 2026-09-21. Recomenda-se confirmar handle com o Lucas.

### @brusantanna.ai
**Categoria:** ia
**Bio:** título "Bruna Santanna | Estrategista de IA" (corpo não confirmado)
**Hook/tom:** nenhum do IG confirmado — vídeo de TikTok do mesmo handle menciona "Analisei meu próprio conteúdo com duas IAs... Comenta CLAUDE aqui que eu te mando o guia completo" (não atribuído ao IG, só referência lateral)
**Top temas:** IA aplicada a conteúdo/viralização (inferido só do TikTok)
**Limitação:** Nenhum número de seguidores/posts do IG localizado.

### @vendedorglobal
**Categoria:** negocio-digital
**Bio:** "📈 E-commerce & IA | +100M Views 🔥 Treino apenas quem está pronto p/ lucrar ⚡ Troop do MAESTRO!" (Murilo Bevervanso)
**Seguidores/posts:** 83K seguidores, 2.280 posts, seguindo 4.745
**Tom:** assertivo, exclusivista, orientado a resultado (baixa confiança)
**Top temas:** e-commerce, marketplace, IA aplicada a vendas
**Limitação:** Conta relacionada distinta @bruno.vendedorglobal não confundida. Nenhuma legenda de post individual recuperada.

### @oluizmain
**Categoria:** creator
**Bio:** não encontrado texto exato; nome "Luiz Main"; site institucional cita 200 mil seguidores (não confirmado como IG)
**Top temas:** produção de vídeo/conteúdo, mentoria de criadores, curso "AI Creator Pro" (do site, não de posts IG)
**Limitação:** Perfil com menos dados confiáveis do lote — nenhuma bio exata, seguidores ou caption completa confirmados no IG.

### @nick_saraev
**Categoria:** automacao
**Bio:** "🚀 Founder @ Maker School 🤖 Helping 2000+ beginners land their First AI client 👇 Get your first client in 90 days or money back"
**Seguidores/posts:** 550K seguidores, 368 posts, seguindo 165
**Hooks:** [Comment APIFY / AUTOMATION / SYSTEM / EMAIL "to get these [recurso]"] — 4 variações confirmadas, frequência alta/média
**Estrutura:** título "Comment [PALAVRA] to get [recurso]" → conteúdo educacional sobre automação (n8n, Make.com, Apify) → isca de lead via comentário → DM
**Tom:** direto, educacional, orientado a resultado, confiante
**Formato dominante:** reels (confirmado)
**Engajamento estimado:** alto (550K seguidores, múltiplos reels indexados individualmente)
**Top temas:** automação de IA (n8n, Make.com, Apify), agências de automação, geração de leads, case de receita ($72K/mês)
**Limitação:** Melhor cobertura do lote (Google indexa reels individuais). Contas fã não confundidas.

### @nathanhodgson
**Categoria:** ia — ⚠️ AMBIGUIDADE: handle exato não localizado como perfil ativo
**Melhor correspondência:** @nathanhodgson.ai (128K seguidores, 339 posts, 86 seguindo)
**Bio:** "Built a 6-Figure Business Powered By AI • Trusted by Google · Meta · OpenAI • hello@nathanhodgson.co.uk • Learn how to start your own AI business"
**Top temas:** negócio de IA, automação (Zapier/Make.com), DM automation, consultoria B2B (do site nathanhodgson.co.uk)
**Limitação:** Handle exato não existe; dados atribuídos ao .ai (confiança média-alta). Outras contas: @nathanhodgson_ (abandonada), @nathanjameshodgson (eletricista, não relacionado).

### @ai
**Categoria:** ia
**Limitação:** Perfil NÃO localizado. Handle provavelmente reservado/não-criador. Candidatos com "ai" no nome (@officialai, @welcome.ai, @eluna.ai, @meta.ai) não são o handle exato — nenhum dado atribuído.

### @ana.gsoares
**Categoria:** marketing
**Bio:** "CEO @uniagiloficial host @agilizesepodcast 🌎Tenha liberdade financeira E geográfica + de R$12 milhões/ano faturados pelos alunos 👇🏼BLACK FRIDAY!" (snapshot com promo datada)
**Seguidores/posts:** ~146K seguidores, 877 seguindo, 2.840 posts
**Tom:** aspiracional, resultado-orientado, promocional (baixa confiança)
**Top temas:** liberdade financeira/geográfica, faturamento de alunos, podcast Agilize-se
**Limitação:** Só bio encontrada, nenhuma caption de post.

### @chase.h.ai
**Categoria:** ia
**Bio:** "🤖 | Making AI Simple ⚡️ | DM 'Ready' to Apply For 1:1 Mentorship 🚀 | Master Claude Code👇"
**Seguidores/posts:** ~221K-228K seguidores (discrepância entre fontes), 751 posts
**CTA:** "DM 'Ready' to Apply For 1:1 Mentorship" + "Comment 'claude' to get my Claude Code for non-coders guide" (via Threads)
**Tom:** direto, didático, promocional, orientado-a-ferramenta
**Top temas:** AI/no-code tools, Claude Code workflows, mentoria 1:1, agentic AI para negócios
**Limitação:** Não confundido com @chase.ai/@chase.variantai.

### @leosoares.ia
**Categoria:** ia
**Bio:** taglines variáveis entre snapshots: "IA p/ Negócios" / "IA p/ Infoprodutos" / "IA p/ Lançamentos" (achado em si — possível A/B test)
**Seguidores/posts:** ~219K seguidores
**Tom:** prático, orientado-a-resultado, empreendedor (baixa confiança)
**Top temas:** IA aplicada a negócios, infoprodutos, lançamentos, empresa/curso "Acelera IA"
**Limitação:** Bio inconsistente entre buscas. Homônimo @leosoares_sp (político) não confundido.

### @gabriel.adamuchi
**Categoria:** creator
**Bio:** "🤖 Aprenda IA de forma descomplicada!" (marca "IA Fácil")
**Seguidores/posts:** ⚠️ 195,2K/1,9M likes é do TikTok, NÃO confirmado para o Instagram
**Tom:** acessível, descomplicado, didático (baixa confiança)
**Top temas:** IA aplicada ao dia a dia, prompts, ferramentas de IA
**Limitação:** Risco de contaminação cross-platform (marca "IA Fácil" em várias redes). Métricas do TikTok não atribuídas ao IG.

### @viverdeia.ai
**Categoria:** ia
**Bio:** "A Plataforma das Empresas que Crescem com IA / +2000 Empresas aceleradas com IA Plug & Play"
**Seguidores/posts:** ~109K seguidores, 524 posts, seguindo 3
**CTA:** "Comenta 'TEMPO' que eu te envio agora a @viverdeia.ai pra..." (truncado)
**Tom:** corporativo, orientado a resultado, institucional (baixa confiança)
**Top temas:** IA para empresas, aceleração de negócios plug & play
**Limitação:** Fundador Rafael Milagre (@rafaelmilagre, conta pessoal separada) não misturado. Só uma referência de post real (truncada).

### @ninja.automacoes
**Categoria:** automacao
**Bio:** "🤖Faturei R$1MM sozinho, com agentes de IA 📚Te ensino a criar um negócio automático 🥷 Clica no link pra saber mais"
**Seguidores/posts:** ~34K seguidores, 65 posts, 79 seguindo
**CTA:** "Clica no link pra saber mais"
**Tom:** direto, vendedor, prova-social (baixa confiança)
**Top temas:** automação com n8n, agentes de IA para negócios, produtos digitais/cursos
**Limitação:** Nenhuma legenda de post individual recuperada além da bio. Produto "InstaNinja" (SaaS terceiro) não confundido.

### @nikolassasso
**Categoria:** creator
**Bio:** "🤖 Criei robôs que fazem o trabalho duro por mim 👨🏻‍💻 Cresça sem trocar ⌛ por dinheiro 🧠 Conteúdo. Vendas. Automação."
**Seguidores/posts:** ~181K seguidores, 1.469 posts
**Tom:** assertivo, aspiracional, objetivo (baixa confiança)
**Top temas:** IA para negócios, vendas online, automação, curso "Prompt Hacker"
**Limitação:** Vários homônimos não confundidos (confiança média-alta na identidade). Conta secundária @eusounikolas não misturada.

### @eduardocavalcanti
**Categoria:** founder (dada)
**Bio:** não encontrado (fragmento truncado: "Inteligência Artificial Engenheiro apaixonado por...")
**Seguidores/posts:** ~26K seguidores, 1.953 seguindo, 1.674 posts
**Limitação:** AMBIGUIDADE SIGNIFICATIVA — nome muito comum, múltiplas contas não relacionadas e perfis LinkedIn distintos. Não foi possível confirmar identidade real. Perfil de menor confiança do lote 4.

### @jonylan
**Categoria:** creator
**Bio:** "Inteligência Artificial Ninja da internet desde 1994 ✉️ falecomjony@outlook.com 📣 Palestras, treinamentos e consultorias Builder em @googlebrasil"
**Seguidores/posts:** ~306K seguidores (posts não encontrado)
**Tom:** autoridade, institucional, veterano (baixa confiança)
**Top temas:** marketing digital, vendas, IA, dicas de Reels (via cross-post TikTok)
**Limitação:** Nome real Jony Lan (Belo Horizonte). Nenhuma legenda confirmada como pertencente a este perfil especificamente.

### @allesinisgalli
**Categoria:** founder
**Bio:** não verbatim; mentora de marketing com IA, 15+ anos de experiência, Austrália/Brasil
**Seguidores/posts:** ⚠️ DADOS CONFLITANTES — 8.155 seguidores/3.548 posts/0.45% engajamento vs 61,3K seguidores (mesma taxa). Não reconciliado.
**Tom:** educativa, confiante, tech-forward (baixa confiança)
**Top temas:** IA aplicada a marketing/vendas, mentoria para empreendedores
**Limitação:** Conflito de contagem de seguidores não resolvido — recomenda-se confirmar com o Lucas. Identidade (handle exato) com confiança alta.

### @lonamkt
**Categoria:** marketing
**Bio:** "🇮🇹 Primeiro milhão aos 18" (Felipe Lona)
**Seguidores/posts:** 4.316 seguidores; "2 posts" reportado (suspeito — conta nova/reformulada ou dado desatualizado)
**Tom:** ousado, direto, aspiracional (baixa confiança)
**Top temas:** tráfego pago, e-commerce, "de 0 a R$1 milhão" (inferido de YouTube, não confirmado no IG)
**Limitação:** "2 posts" não confiável sem verificação. Todo conteúdo temático vem de YouTube, não do IG.

### @gabrielbarbosa.oficial
**Categoria:** creator
**Bio:** "🚀 +10MM faturados na internet 🌎Te ensino a ter uma operação enxuta e lucrativa de qualquer lugar do mundo"
**Seguidores/posts:** 7.782 seguidores, 754 seguindo, 47 posts
**Tom:** aspiracional, direto, orientado a resultado (baixa confiança)
**Top temas:** negócios digitais, operação enxuta/lucrativa
**Limitação:** Múltiplos homônimos "Gabriel Barbosa" (incl. jogador "Gabigol") NÃO confundidos.

### @opensession.co
**Categoria:** agencia
**Bio:** "Brand x UX/AI x Design Systems We help designers and brands level up their creativity."
**Seguidores/posts:** 25K seguidores, 881 seguindo, 26 posts
**Tom:** profissional, criativo, orientado a design (baixa confiança)
**Top temas:** brand identity, UX/AI, design systems, art direction
**Limitação:** Estúdio de design (San Diego). Só dados de bio confirmados, nenhuma legenda real.

### @leandroladeiran
**Categoria:** marketing
**Bio IG:** não encontrado (bloqueado por login wall). Bio TikTok (mesmo handle, NÃO confirmado como do IG): "Pensador contemporâneo que às vezes conta umas piadas ruins"
**Hook (via TikTok, NÃO verificado no IG):** "Quem não sabe COPYWRITING dançou… Meu gingado te influenciou a me seguir, afinal?"
**Tom:** irreverente, humorístico, direto, didático (baixa-média confiança, cross-platform)
**Top temas:** copywriting ("Light Copy"), técnica "Stories 10x", marketing digital, humor — tudo inferido de TikTok/YouTube
**Limitação:** Perfil de dado mais fraco do lote 5 — bio, seguidores e legendas específicas do IG NÃO confirmadas.

### @christiantriad
**Categoria:** creator
**Bio:** "🤖 Empresário Tech - IA, Tech & Saas 💻 Criador do método 'A Tríade do Tempo' 2M+ pessoas treinadas ❤️ @easy.dcor" (Christian Barbosa)
**Seguidores/posts:** ⚠️ DADOS CONFLITANTES — 571K/4.333 posts vs 304,3K/464 seguindo/1.547 posts
**Hook:** [{modelo: outro, exemplo: "Como disse Bill Gates, 'A vida não é justa, acostume-se...'", frequência: baixa}]
**Tom:** direto, motivacional, autoritativo (baixa confiança)
**Formato dominante:** reels (indício único)
**Top temas:** produtividade/gestão do tempo, IA e tecnologia, empreendedorismo tech
**Limitação:** Contagem de seguidores inconsistente entre buscas — reportada a divergência.

### @oneyaraujo
**Categoria:** creator
**Bio:** "🏆 Revelando Segredos de como Viralizar, Ganhar Seguidores e Vender Online. 🚀 +62.000 alunos e contando... 👉🏻 Código Viral por 12x de R$ 19,98" (Oney Araújo)
**Seguidores/posts:** 2M seguidores, 511 seguindo, 1.273 posts
**Estrutura:** Gancho → Benefício → Mostre → CTA (framework declarado pelo próprio criador)
**CTA:** "Código Viral no link da bio" (+ variações: "Confia 👍🏻", "Comenta seu nicho que te dou um help")
**Tom:** persuasivo, didático, promocional, direto (confiança média)
**Formato dominante:** reels
**Top temas:** marketing viral/reels, crescimento de seguidores, venda online, roteiro/gancho de vídeo
**Limitação:** Boa consistência de seguidores/posts. Legendas majoritariamente de conteúdo cross-postado no TikTok.

### @geracaotechs
**Categoria:** ia
**Bio:** não encontrado exato; título indexado "Tecnologia e I.A (@geracaotechs) - Glauton Filho"
**Hooks (via Threads, cross-postado, não 100% confirmado no IG):** apresentação de ferramenta de IA + explicação em bullets com emojis
**CTA:** "Comente 'Eu quero'"
**Tom:** didático, entusiasmado, acessível (confiança média)
**Top temas:** ferramentas de IA generativa (jogos, imagens, vídeo), tutoriais de prompt
**Limitação:** Seguidores/posts do IG não confirmados (só Threads: 11,2K, não atribuído ao IG).

### @amandadinizmkt
**Categoria:** marketing
**Bio:** não encontrado — dois títulos conflitantes: "Marketing & Empreendedorismo" vs "IA para Empreendedoras"
**Top temas:** IA para empreendedoras, Claude Code aplicado a negócios (inferido de GitHub/YouTube, não do IG)
**Limitação:** Conta com MENOS dados confirmados — nenhuma legenda real, bio conflitante, nenhum número de seguidores.

### @human___academy
**Categoria:** ia
**Bio:** "A Maior Escola de IA para Criativos" (boa confiança, bate com site humanacademy.ai)
**Seguidores/posts:** 260K seguidores, 496 seguindo, 450 posts
**Tom:** profissional, inspirador, técnico-criativo (inferido de citação do CEO no site oficial, não do IG)
**Formato dominante:** reels (série "AXIS", amostra pequena)
**Top temas:** cursos/workshops de IA para criativos, criação audiovisual com IA, produto "AI Video Lab"
**Limitação:** Seguidores/posts confirmados com boa consistência. Nenhuma legenda completa de post real encontrada.

### @geiss11
**Categoria:** creator
**Bio:** "🇧🇷🇺🇾🇲🇽🇲🇨🇫🇷🇮🇹🇨🇭🇦🇷🇨🇱 🏛️ | Vendo Produtos Digitais no Mundo Todo 👇 | O que você procura está aqui" (Henrique Geiss)
**Seguidores/posts:** ~45K seguidores, 601 seguindo, 83 posts
**Tom:** comercial, internacional, direto (baixa confiança)
**Top temas:** produtos digitais, infoprodutos
**Limitação:** Nenhuma legenda real, nenhum dado de engajamento.

### @nelmoricalde
**Categoria:** creator
**Bio:** "Nelmo Ricalde | IA, Negócios & Lucro" (tagline); fundador da "Zuvora", mentor em "A Nova Inteligência"
**Tom:** educativo, empreendedor, tech (baixa confiança)
**Top temas:** inteligência artificial, negócios, lucratividade
**Limitação:** Nenhum seguidor/post/legenda encontrado — dado muito raso, mas identidade sem ambiguidade.

### @rodrigotadewald
**Categoria:** marketing
**Bio:** não verbatim; co-fundador da Asimov Academy (30.000+ alunos), ensina IA/Python
**Seguidores/posts:** ~232K seguidores, 62 seguindo, 103 posts
**Tom:** didático, técnico, autoridade (baixa confiança)
**Top temas:** inteligência artificial, Python, educação em tecnologia
**Limitação:** Identidade bem confirmada. Nenhuma legenda real encontrada apesar de buscas direcionadas.

### @sujeitoprogramador
**Categoria:** ia
**Bio:** "👨🏻‍💻 Programador há + de 12 anos 🔥 + de 45.000 alunos. 📕 [Vagas abertas] Aprenda programação e IA do zero ao mercado"
**Seguidores/posts:** ~165K seguidores, 6.108 seguindo, 2.996 posts
**Tom:** motivacional, didático, direto ao mercado (baixa confiança)
**Top temas:** programação, IA, carreira em tech, cursos
**Limitação:** Identidade bem confirmada (Matheus Fraga). Nenhuma legenda real recuperada apesar de conta madura (2.996 posts).

### @jonathan_kamargo
**Categoria:** creator
**Limitação:** PERFIL NÃO LOCALIZADO. Homônimos não relacionados não atribuídos. Recomenda-se verificação manual direta.

### @marianatorre.s
**Categoria:** marketing
**Limitação:** URL exata existe mas NENHUM dado de bio/seguidores/posts/legendas indexado. Forte risco de homônimos (@torresmarianaof 717K etc.) — NÃO atribuídos. Perfil essencialmente sem dados.

### @marketerhub.ai
**Categoria:** marketing
**Bio:** "Empowering Digital Marketers" (título curto, possivelmente truncado)
**Top temas:** comunidade privada de marketing com IA (do site institucional, não confirmado como tema de posts)
**Limitação:** Conta confirmada existir, mas sem seguidores/posts/legendas reais. Homônimos @marketerhubcom/@marketer_hub não atribuídos.

### @marcelaluzzio
**Categoria:** marketing
**Bio:** "Marcela Lúzio | Marketing de Conteúdo & I.A" (paráfrase); MBA em IA para negócios digitais pela USP
**Seguidores/posts:** 226K seguidores, 658 seguindo, 964 posts
**Estrutura:** conteúdo educativo sobre marketing + IA, incl. reels ensinando estrutura (gancho → corpo → CTA)
**Tom:** educativo, estratégico, didático (baixa confiança)
**Formato dominante:** reels (indício forte)
**Engajamento estimado:** médio-alto (base 226K)
**Top temas:** estrutura de reels (gancho/retenção/CTA), marketing de conteúdo com IA, infoprodutos, uso de IA generativa
**Limitação:** Perfil com MAIS dados recuperáveis do lote 8. Nenhuma legenda verbatim confirmada.

### @gestordeaudiencia
**Categoria:** marketing
**Limitação:** PERFIL NÃO LOCALIZADO. Handle "segredosdaaudiencia" (diferente) e conta TikTok não relacionada encontrados mas NÃO atribuídos. Recomenda-se verificação/possível erro de digitação.

### @sebintel
**Categoria:** ia
**Limitação:** Existência confirmada em múltiplas plataformas, mas NENHUM dado de bio/seguidores/posts/legendas indexado.

### @avora.ai
**Categoria:** agencia
**Bio:** não encontrado completo; fragmentos: "Siga @avora.ai para conteúdos diários sobre IA na prática!" e "Avora wasn't created just to talk about AI. It was built to turn..." (truncado, em inglês — incomum)
**Tom:** prático, educativo (baixíssima confiança)
**Top temas:** IA na prática (conteúdo diário)
**Limitação:** Agência de IA confirmada existir (Belo Horizonte). Página nunca carregou conteúdo em snippets — só 2 fragmentos truncados.

### @ogabrieeldias
**Categoria:** creator
**Bio:** "Gabriel Dias | SaaS Founder" (nome de exibição, não corpo da bio)
**Limitação:** Handle confirmado com alta confiança, mas ZERO conteúdo de post encontrado. Múltiplos homônimos "Gabriel Dias" não misturados.

### @rodrigobindes
**Categoria:** founder
**Bio:** "Mostro como chegar aos 100k/mês com agência de mkt" ("Mentor de Agências de Marketing Digital")
**Seguidores/posts:** 278K seguidores, 1.835 posts, 1.482 seguindo
**Tom:** direto, mentor, orientado a resultado (baixa-média confiança)
**Engajamento estimado:** médio-alto (base 278K)
**Top temas:** agências de marketing digital, faturamento/100k por mês, mentoria de agências
**Limitação:** Identidade bem confirmada (co-fundador "Ultralize" com Erico Rocha, Leandro Ladeira, Guilherme Cardoso). Nenhuma legenda real recuperada, só bio.

### @franklim.gui
**Categoria:** creator
**Bio:** "documentei nos destaques minha jornada até R$7M em 3 anos 📹 ensino de graça no YouTube vender Lowticket 👉 me chama no direct e conta onde tá travado" (Guilherme Franklim)
**Seguidores/posts:** 104K seguidores, 489 seguindo, 58 posts
**Hook:** [{modelo: transformacao_silenciosa, exemplo: "documentei nos destaques minha jornada até R$7M em 3 anos", frequência: não determinável}]
**CTA:** "me chama no direct e conta onde tá travado"
**Tom:** direto, motivacional, informal/coloquial (média confiança)
**Engajamento estimado:** médio (104K seguidores/58 posts, especulativo)
**Top temas:** vendas lowticket, jornada de faturamento pessoal (R$7M), educação gratuita
**Limitação:** Boa confirmação de identidade. Nenhuma legenda individual do IG recuperada — tema "ferramentas de IA" vem do YouTube, não confirmado no IG.

### @gabrielsamp.ai
**Categoria:** ia
**Limitação:** PERFIL NÃO LOCALIZADO no Instagram — handle só existe confirmado no TikTok. Homônimos "Gabriel Sampaio" no IG (surfista, cantor sertanejo) NÃO batem com categoria "ia" e não foram atribuídos.

### @maestrosdaia
**Categoria:** ia
**Bio:** não encontrado no IG; equivalente TikTok "Fundadores Maestria | Lyra Academy | Junte-se à Comunidade Maestros da IA" (não confirmado idêntico no IG)
**Seguidores/posts:** ⚠️ NÃO CONFIÁVEL — resumo de busca retornou "9 milhões de seguidores, 5 posts" que não aparece em snippet bruto (suspeita de erro) e contradiz TikTok (72K). NÃO USAR.
**Tom:** educativo, prático (baixa confiança)
**Top temas:** cursos de IA, agentes de IA, dicas de IA
**Limitação:** Perfil existe mas bio real/seguidores confiáveis/legendas completas não extraídos.

### @brandsdecoded__
**Categoria:** marketing
**Bio:** "// Decodificando o futuro do marketing com AI ↓ Criei uma ferramenta que automatiza a criação de carrosséis por @leo.varricchio" (Leonardo Varrichio)
**Seguidores/posts:** 301K seguidores, 3 seguindo, 1.734 posts
**Estrutura (de material promocional, não confirmado em posts):** roteiros estruturados por emoção/tipo/CTA via ferramenta "Roteiro Machine"
**Tom:** estratégico, tecnológico, direto, autoritativo (baixa confiança)
**Formato dominante:** carrossel (produto central é automação de carrosséis "Content Machine 3.0")
**Engajamento estimado:** médio-alto (301K seguidores)
**Top temas:** carrosséis de autoridade com IA, automação de conteúdo, marketing digital com IA
**Limitação:** Bio/seguidores/posts com boa confiança. Nenhuma legenda real de post individual encontrada.

### @anatex
**Categoria:** creator (nota: bio real sugere "IA para Negócios", não creator genérico)
**Bio:** não encontrado texto exato; nome "Ana Tex - Inteligência Artificial para Negócios"
**Seguidores/posts:** 718K seguidores, 1.113 seguindo, 1.468 posts
**Tom:** prático, motivacional, empreendedor, didático (baixa confiança)
**Formato dominante:** reels (forte indício)
**Engajamento estimado:** alto (718K seguidores)
**Top temas:** automação de negócios com IA, cursos/mentoria de IA, produtividade com IA
**Limitação:** Perfil grande e bem indexado mas todas legendas retornadas truncadas — nenhuma citação completa verificada.

### @larissagomes.ia
**Categoria:** ia
**Bio (IG, exata):** "💻 Te ensino a criar um negócio enxuto e que vende: você + IA ⚡️ Compartilho o que aplico sobre IA Domine o chatGPT👇🏻"
**Seguidores/posts:** 15K seguidores, 20 seguindo, 262 posts (IG)
**Hook (via TikTok, NÃO confirmado no IG):** "Peça o chatGPT para analisar o feed do seu instagram 🧠"
**Tom:** prático, direto, didático, acessível (confiança média)
**Engajamento estimado:** baixo-médio (15K seguidores IG)
**Top temas:** análise de feed/perfil com ChatGPT, prompts prontos de IA para negócio, crescer e vender com IA
**Limitação:** Bio IG confirmada com boa confiança. Único exemplo de estrutura/hook/CTA completo vem de cross-post no TikTok.

### @thiagozaao
**Categoria:** creator
**Limitação:** PERFIL NÃO LOCALIZADO em 5 buscas diferentes. Possível handle com erro de digitação, conta pequena/nova, privada ou excluída.

### @neuwebstudio
**Categoria:** agencia
**Bio:** "Cinematic Web Design TikTok 👉 172k+ 19 Figma Animations 75% off LAST SALE 👇" (via snippet, não verificado ao vivo)
**Seguidores/posts:** ~52K seguidores, ~100 seguindo, 168 posts
**Tom:** cinematográfico, técnico, promocional (baixa confiança)
**Top temas:** web design, Figma animations, parallax scrolling, tutoriais UI/UX (inferido do TikTok)
**Limitação:** Nenhuma legenda real do IG nem dado de engajamento encontrado.

### @laschuk
**Categoria:** founder
**Bio:** nome de exibição "LASCHUK | email marketing 🏆"
**Seguidores/posts:** ~36K seguidores, 61 seguindo, 200 posts
**Tom:** educacional, direto, promocional (baixa confiança)
**Top temas:** email marketing, tráfego próprio/owned traffic, growth sem ads pagos
**Limitação:** Sobrenome comum — vários homônimos excluídos corretamente. Nenhuma legenda real encontrada.

### @maestroptompts
**Categoria:** ia (não confirmada)
**Limitação:** PERFIL NÃO LOCALIZADO. Site "maestroprompts.com" (produto, não perfil IG) não atribuído. Zero dados reportados.

### @faladantasmkt
**Categoria:** marketing
**Bio:** paráfrase — Jessica Dantas, "Mentora de conteúdo & negócios digitais", vende online há 14 anos, 10.000+ clientes
**Seguidores/posts:** ⚠️ ~99K-108K seguidores (discrepância entre fontes), 143 seguindo, 1.774 posts
**Tom:** mentora, direta, orientada a vendas, educacional (baixa confiança)
**Top temas:** como vender infoprodutos/mentorias, crescimento no Instagram, atrair clientes qualificados
**Limitação:** Discrepância de seguidores não resolvida. Busca de legendas reais bloqueada por esgotamento de orçamento de busca da sessão.

### @lindsay.ia
**Categoria:** ia (não confirmada)
**Limitação:** PERFIL NÃO LOCALIZADO. Resultados só trouxeram "Lindsay" ligados a Iowa (EUA), não relacionados. Zero dados reportados.

### @andrevictor.m
**Categoria:** marketing
**Bio:** paráfrase — primeiro milhão aos 18, Ferrari Portofino (~R$3M à vista), 50 países até os 22
**Seguidores/posts:** 244K seguidores, 286 posts (não confirmado por fonte primária)
**Tom:** ostentação, aspiracional, empreendedor (baixa confiança)
**Formato dominante:** reels (múltiplos reels indexados, cadência regular)
**Top temas:** dropshipping, marketing digital, empreendedorismo (do canal YouTube associado, não confirmado no IG)
**Limitação:** Nenhuma legenda/CTA real encontrada — só resumo de bio parafraseado.

### @drisiano
**Categoria:** creator
**Limitação:** PERFIL NÃO LOCALIZADO. Homônimos parciais claramente não relacionados não atribuídos.

### @brun0gpt
**Categoria:** ia
**Bio:** "Marketing e Vendas com Inteligência Artificial" (nome exibição "Bruno Francisco | IA e Marketing")
**Seguidores/posts:** 157K seguidores, 171 seguindo, 1.334 posts
**Tom:** técnico, prático, voltado a vendas (baixa confiança)
**Top temas:** IA aplicada a marketing e vendas
**Limitação:** Handle/nome confirmados com boa confiança. Nenhuma legenda, CTA ou engajamento real encontrado.

### @maxcarrau.ia
**Categoria:** ia
**Limitação:** PERFIL NÃO LOCALIZADO para o handle exato. instagram.com/maxcarrau (sem ".ia") parece privado/inativo. Homônimo @maxcarraa (cantor argentino) NÃO atribuído.

### @noevarner
**Categoria:** creator — ⚠️ AMBIGUIDADE: handle exato sem bio/métricas extraídas
**Estatística encontrada (NÃO confirmada para o handle exato):** 91.740 seguidores, 625 posts, 0,45% engajamento pertencem a @noevarner.ai (conta distinta, bate com site noevarner.com "AI systems for content, ads, and growth")
**Top temas (não confirmado para o handle exato):** automação com IA para conteúdo/ads/growth
**Limitação:** Múltiplos handles candidatos (@noevarner, @noevarner.ai, @therealnoevarner), nenhum confirmado como o exato pedido. Recomenda-se confirmação manual do Lucas.

### @yikchanltd
**Categoria:** creator
**Limitação:** Nenhum dado coletado. WebFetch bloqueado; orçamento de buscas da sessão esgotado (200/200 chamadas já usadas por outras tarefas desta execução) antes de executar as buscas planejadas. Recomenda-se re-executar em sessão nova.

---

## Perfis Sugeridos pelo Sistema
Não aplicável — `config/profiles.json` já tinha perfis ativos configurados (Modo Análise), sem etapa de descoberta nesta execução.

---

## Limitações de Dados (resumo)

- **Bloqueio de rede:** WebFetch para `instagram.com` bloqueado (`EGRESS_BLOCKED`) em 100% das tentativas (61/61 perfis) — toda a coleta veio de WebSearch (snippets indexados pelo Google), sem acesso direto à página do Instagram.
- **Orçamento de busca esgotado:** a sessão atingiu o limite de WebSearch ao final da execução, reduzindo a profundidade de refinamento para os últimos perfis processados (@faladantasmkt, @lindsay.ia, @maestroptompts, @drisiano, @maxcarrau.ia, @noevarner, @yikchanltd).
- **12 perfis não localizados** com confiança suficiente: @yikC, @eujoaotorresz, @ai, @jonathan_kamargo, @drisiano, @maestroptompts, @lindsay.ia, @thiagozaao, @gestordeaudiencia, @gabrielsamp.ai, @maxcarrau.ia, @yikchanltd.
- **3 perfis com ambiguidade de identidade não resolvida:** @nathanhodgson, @eduardocavalcanti, @noevarner.
- **1 perfil com possível handle incorreto:** @rafa.grandi (categoria "marketing" não bate com o perfil encontrado, mesmo achado há duas execuções seguidas — recomenda-se correção definitiva no `config/profiles.json`).
- **4 perfis com divergência numérica entre fontes não reconciliada:** @allesinisgalli, @christiantriad, @faladantasmkt, @maestrosdaia (este último com número suspeito descartado).
- Nenhum dado de engajamento, hook, CTA ou tema de post foi inventado em nenhum dos 61 perfis. Onde não havia evidência real, o campo foi marcado "dado insuficiente" ou "não encontrado".
