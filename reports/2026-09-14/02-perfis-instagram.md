# Análise de Perfis Instagram — 2026-09-14

**Modo de execução:** Análise (lista de perfis já configurada em `config/profiles.json`, Passo 2 do Módulo 2 executado diretamente, sem etapa de descoberta).

**Nota metodológica geral:** O Instagram bloqueia scraping/crawling direto e WebFetch ao domínio `instagram.com` retornou bloqueio de rede (`EGRESS_BLOCKED`) nesta sessão. Toda a coleta foi feita via WebSearch (1–2 buscas por perfil), que majoritariamente indexa metadados de perfil (bio, contagem de seguidores/posts) e menções de terceiros (blogs, cross-posts em TikTok/YouTube/Threads), raramente o texto literal de posts individuais do Instagram. **Nenhum dado de engajamento, hook, CTA ou tema de post foi inventado.** Onde a busca não trouxe evidência direta e específica do perfil, o campo foi marcado como "dado insuficiente"/null e a limitação foi documentada na seção final. Exemplos de hooks/CTAs oriundos de conteúdo espelhado em outra rede (TikTok, YouTube) e não confirmados como publicados literalmente no Instagram estão sinalizados como tal.

---

## Visão Geral dos Perfis

| Perfil | Categoria | Formato Dominante | Engajamento | Hook / Padrão Observado |
|--------|-----------|--------------------|-------------|--------------------------|
| @charliehills | creator | misto | médio-alto (~88K) | dado insuficiente |
| @yikC | creator | — | dado insuficiente | perfil não localizado |
| @eujoaotorresz | creator | — | baixo (não confirmado) | dado insuficiente |
| @fabianocarvalhojr | founder | misto | alto (~130K) | dado insuficiente |
| @rafa.grandi | marketing | — | baixo (~247) | perfil pessoal, fora do nicho |
| @brusantanna.ai | ia | reels | dado insuficiente | comentário-gatilho ("Comenta CLAUDE") |
| @vendedorglobal | negocio-digital | misto | alto (~83K) | dado insuficiente |
| @oluizmain | creator | reels (inferido) | dado insuficiente | dado insuficiente |
| @nick_saraev | automacao | reels | alto (~550K) | comentário-gatilho ("Comment 'AUTOMATION'") |
| @nathanhodgson | ia | — | dado insuficiente | perfil não confirmado (handle ambíguo) |
| @ai | ia | — | dado insuficiente | perfil não indexado |
| @ana.gsoares | marketing | misto | alto (~146K) | dado insuficiente |
| @chase.h.ai | ia | reels | alto (~221-228K) | DM-gatilho ("DM 'Ready'") |
| @leosoares.ia | ia | misto | alto (~219K) | dado insuficiente |
| @gabriel.adamuchi | creator | reels | dado insuficiente | dado insuficiente |
| @viverdeia.ai | ia | misto | alto (~109K) | comentário-gatilho (variação) |
| @ninja.automacoes | automacao | reels (indício) | dado insuficiente | dado insuficiente |
| @nikolassasso | creator | dado insuficiente | alto (~181K) | dado insuficiente |
| @eduardocavalcanti | founder | — | médio (handle ambíguo) | dado insuficiente |
| @jonylan | creator | reels | alto (~306K) | dado insuficiente |
| @allesinisgalli | founder | — | baixo (~8.155) | dado insuficiente |
| @lonamkt | marketing | — | baixo (2 posts) | atividade concentrada no YouTube |
| @gabrielbarbosa.oficial | creator | — | baixo (~7.782) | dado insuficiente |
| @opensession.co | agencia | dado insuficiente | médio (~23K) | dado insuficiente |
| @leandroladeiran | marketing | misto | alto (audiência multi-rede) | dado insuficiente |
| @christiantriad | creator | dado insuficiente | alto (~571K) | dado insuficiente |
| @oneyaraujo | creator | reels | alto (~2M) | "Código Viral": gancho→benefício→mostre→CTA |
| @geracaotechs | ia | dado insuficiente | dado insuficiente | dado insuficiente |
| @amandadinizmkt | marketing | — | dado insuficiente | perfil não localizado no Instagram |
| @human___academy | ia | dado insuficiente | alto (~260K) | dado insuficiente |
| @geiss11 | creator | dado insuficiente | médio (~45K) | dado insuficiente |
| @nelmoricalde | creator | dado insuficiente | dado insuficiente | perfil não localizado |
| @rodrigotadewald | marketing | dado insuficiente | alto (~226K) | dado insuficiente |
| @sujeitoprogramador | ia | dado insuficiente | alto (~168K) | dado insuficiente |
| @jonathan_kamargo | creator | — | dado insuficiente | perfil não localizado |
| @marianatorre.s | marketing | — | dado insuficiente | perfil existe, sem dados de conteúdo |
| @marketerhub.ai | marketing | dado insuficiente | dado insuficiente | dado insuficiente |
| @marcelaluzzio | marketing | reels (indício) | alto (~226K) | dado insuficiente |
| @gestordeaudiencia | marketing | dado insuficiente | dado insuficiente | associação a conteúdo incerta |
| @sebintel | ia | reels | dado insuficiente | dado insuficiente |
| @avora.ai | agencia | dado insuficiente | dado insuficiente | CTA de seguir (parcial) |
| @ogabrieeldias | creator | — | dado insuficiente | handle não confirmado |
| @rodrigobindes | founder | dado insuficiente | alto (~278K) | dado insuficiente |
| @franklim.gui | creator | dado insuficiente | alto (~104K) | dado insuficiente |
| @gabrielsamp.ai | ia | — | dado insuficiente | handle não confirmado no Instagram |
| @maestrosdaia | ia | reels | médio-alto (dado via TikTok) | "agente de IA que trabalha enquanto você dorme" (via TikTok) |
| @brandsdecoded__ | marketing | carrossel | alto (~301K) | dado insuficiente (padrão descrito, não confirmado) |
| @anatex | creator | reels | alto (~626-671K) | dado insuficiente |
| @larissagomes.ia | ia | misto | médio (~15K) | dica de prompt (via TikTok) |
| @thiagozaao | creator | — | dado insuficiente | perfil não localizado |
| @neuwebstudio | agencia | misto | médio (~52K) | dado insuficiente |
| @laschuk | founder | dado insuficiente | médio (~36K) | dado insuficiente |
| @maestroptompts | ia | — | dado insuficiente | perfil não localizado (só marca similar) |
| @faladantasmkt | marketing | misto | alto (~99K IG / +2M multi-rede) | dado insuficiente |
| @lindsay.ia | ia | dado insuficiente | médio (~45K, não confirmado) | funil comentário→DM (não confirmado) |
| @andrevictor.m | marketing | reels | alto (~244K) | "Fiz meu primeiro milhão aos 18..." (via YouTube/podcast) |
| @drisiano | creator | — | dado insuficiente | perfil não localizado |
| @brun0gpt | ia | misto | alto (~157K) | dado insuficiente (método "Impulso GPT VIRAL") |
| @maxcarrau.ia | ia | — | dado insuficiente | perfil não localizado |
| @noevarner | creator | dado insuficiente | baixo/médio (via variante .ai) | dado insuficiente |
| @yikchanltd | creator | reels | alto (~79K) | série de 7 episódios, gancho de 8 palavras |

---

## Análise Detalhada por Perfil

### @charliehills
**Categoria:** creator
- Hook: dado insuficiente
- Estrutura: dado insuficiente
- CTA: dado insuficiente
- Tom: prático, direto, educativo (inferido da bio)
- Formato dominante: misto (não confirmado)
- Engajamento estimado: médio-alto (~88K seguidores, 260 posts)
- Temas: uso prático de ferramentas de IA
- Limitação: perfil encontrado (bio focada em "I help you (actually) use AI"), mas nenhum post/hook/CTA específico indexado. Existem handles similares (@charliehills.studio, @charliehillsracing) não confundir.

### @yikC
**Categoria:** creator
- Limitação: handle exato não localizado via busca; resultados retornaram contas não relacionadas (Yik Yak app, YWCA International Kids Club, Yik Café). Provável perfil pequeno/nicho ou grafia diferente.

### @eujoaotorresz
**Categoria:** creator
- Engajamento estimado: baixo (perfil aproximado @joaotorresz, sem "eu": ~2K seguidores, 5 posts — correspondência não confirmada)
- Limitação: handle exato não indexado; não é possível confirmar se o achado aproximado é o mesmo perfil.

### @fabianocarvalhojr
**Categoria:** founder
- Hook/CTA: dado insuficiente
- Tom: técnico, empreendedor, direto (inferido)
- Formato dominante: misto (1.417 posts)
- Engajamento estimado: alto (~130K seguidores)
- Temas: agentes de IA para vendas/operação de negócios (fundador da lasy.ai)
- Limitação: perfil confirmado e ativo (YouTube/Threads também), mas nenhum hook/CTA/tema de post individual indexado com texto exato.

### @rafa.grandi
**Categoria:** marketing
- Engajamento estimado: baixo (247 seguidores, 36 posts)
- Limitação: perfil localizado (Rafael Grandi Borges, analista jurídico) é conta pessoal pequena sem relação aparente com o nicho monitorado (IA/marketing/negócio digital).

### @brusantanna.ai
**Categoria:** ia
- Hook: comentário-gatilho — "Comenta CLAUDE aqui que eu te mando o guia completo" (1 amostra, via cross-post no TikTok)
- Estrutura: análise de conteúdo próprio com IA → resultado numérico → oferta via comentário-gatilho
- CTA: comentário-gatilho para receber material via DM
- Tom: estratégico, didático, orientado a resultado
- Formato dominante: reels
- Engajamento estimado: dado insuficiente (sem contagem de seguidores)
- Temas: estratégia de IA para crescimento de conteúdo, análise de vídeos com IA
- Limitação: exemplo de CTA confirmado via post espelhado no TikTok, não no Instagram diretamente; sem número de seguidores.

### @vendedorglobal
**Categoria:** negocio-digital
- Hook: dado insuficiente
- CTA (bio): "Treinamento apenas p/ quem está pronto p/ lucrar" — filtro de qualificação, não CTA de post
- Tom: comercial, motivacional, direto
- Formato dominante: misto (2.280 posts)
- Engajamento estimado: alto (~83K no Instagram; também ~250K YouTube, ~35K TikTok)
- Temas: e-commerce, marketplace, IA aplicada a negócios online
- Limitação: bio e presença multiplataforma confirmadas (Murilo Bevervanso); nenhum hook/tema de post específico indexado.

### @oluizmain
**Categoria:** creator
- Formato dominante: reels (inferido pelo produto vendido — curso de produção de vídeo mobile)
- Temas: produção de vídeo mobile, portfólio para Instagram/TikTok
- Limitação: site associado (luizmain.com, curso "Mobile Pro") localizado, mas seguidores, hooks e CTAs não disponíveis — página exige login.

### @nick_saraev
**Categoria:** automacao
- Hook/CTA: comentário-gatilho — "Comment 'AUTOMATION' to get these AI..." (padrão recorrente, citado em múltiplas fontes)
- Estrutura: tutorial/walkthrough de automação (n8n, Claude Code, OpenAI Codex) → prova social → CTA de comentário
- Tom: prático, mão-na-massa, educativo, direto
- Formato dominante: reels (~3.2K reels indexados)
- Engajamento estimado: alto (~550K seguidores)
- Temas: automação com IA (n8n), Claude Code, geração de leads, "primeiro cliente de IA em 90 dias"
- Limitação: existem handles relacionados (@nick.saraev, @nickautomates, @nicksaraevdaily); não é possível garantir que todas as métricas pertencem exatamente a este handle com underscore.

### @nathanhodgson
**Categoria:** ia
- Limitação: handle não confirmado — múltiplas contas distintas de pessoas diferentes chamadas "Nathan Hodgson" (eletricista, conta pessoal, conta sem posts), nenhuma claramente correspondente a um perfil de conteúdo do nicho.

### @ai
**Categoria:** ia
- Limitação: nenhuma informação específica sobre o perfil encontrada; handle de 2 letras provavelmente institucional/reservado ou inacessível à indexação.

### @ana.gsoares
**Categoria:** marketing
- Hook/CTA: dado insuficiente
- Tom: motivacional, empreendedor, didático
- Formato dominante: misto (2.840 posts)
- Engajamento estimado: alto (~146K seguidores)
- Temas: empreendedorismo digital, gestão ágil (CEO da Uniagil), liberdade financeira/geográfica, podcast "Vivendo do Digital"
- Limitação: nenhum hook/CTA/tema de post individual com texto exato indexado.

### @chase.h.ai
**Categoria:** ia
- Hook/CTA: "DM 'Ready' to Apply For 1:1 Mentorship" (CTA de bio, recorrente em fontes externas)
- Estrutura: tutorial de IA/automação sem código → prova de autoridade (Claude Code) → CTA de aplicação por DM
- Tom: simplificador, acessível, motivacional, autoridade técnica
- Formato dominante: reels (751 posts)
- Engajamento estimado: alto (~221–228K seguidores; ~163K YouTube, ~137K TikTok)
- Temas: IA sem código, deploy de agentes de IA, tutoriais Claude Code
- Limitação: pequena divergência na contagem de seguidores entre fontes (221K vs 228K).

### @leosoares.ia
**Categoria:** ia
- Hook/CTA: dado insuficiente
- Tom: autoridade, orientado a lucro, empresarial
- Engajamento estimado: alto (~219K seguidores)
- Temas: IA aplicada a negócios, lançamentos digitais, infoprodutos (CEO Acelera IA)
- Limitação: nenhum hook/CTA/tema de post individual com texto exato indexado.

### @gabriel.adamuchi
**Categoria:** creator
- Hook/CTA: dado insuficiente
- Tom: simplificador, didático, acessível
- Formato dominante: reels (marca "IA Fácil", também em TikTok/YouTube)
- Temas: ensino de IA simplificado, prompts de IA
- Limitação: marca confirmada, mas seguidores e hooks/CTAs específicos não indexados.

### @viverdeia.ai
**Categoria:** ia
- Hook: dado insuficiente
- CTA: comentário-gatilho (variação do padrão comum) — ex. citado por fonte externa: "Comenta 'TEMPO' que eu te envio agora"
- Tom: institucional, escala, autoridade de mercado
- Formato dominante: misto (524 posts)
- Engajamento estimado: alto (~109K seguidores)
- Temas: soluções de IA plug-and-play para empresas, cases de crescimento, plataforma educacional (fundador Rafael Milagre)
- Limitação: apenas 1 exemplo de CTA confirmado via fonte externa; nenhum hook de abertura com texto exato indexado.

### @ninja.automacoes
**Categoria:** automacao
- Formato dominante: reels (indício, não confirmado)
- Temas: automação de Instagram, IA, chatbot/DM automático
- Limitação: apenas descrição genérica do nicho (autor "Matheus Pessoa") encontrada; nenhum post ou métrica específica indexada.

### @nikolassasso
**Categoria:** creator
- Tom: direto, provocador, "vendedor", tech, motivacional (inferido da bio: "Criei robôs que fazem o trabalho duro por mim")
- Engajamento estimado: alto (~181K seguidores, 1.469 posts)
- Temas: IA para negócios, automação, vendas online, "crescer sem trocar tempo por dinheiro"
- Limitação: métricas de perfil confirmadas, mas nenhum hook/CTA/estrutura de post específica indexada.

### @eduardocavalcanti
**Categoria:** founder
- Engajamento estimado: médio (~26K seguidores, 1.674 posts — incerto, possível confusão com @profeduardocavalcanti, 9.800 seguidores)
- Temas: Inteligência Artificial, engenharia
- Limitação: handle ambíguo — múltiplos "Eduardo Cavalcanti" no Instagram/LinkedIn/Crunchbase; não confirmado qual é o perfil-alvo.

### @jonylan
**Categoria:** creator
- Formato dominante: reels (também ativo no TikTok com conteúdo replicado)
- Engajamento estimado: alto (~306K seguidores)
- Temas: marketing digital, vendas, IA, dicas de Instagram, treinamentos/consultoria
- Limitação: perfil e nicho confirmados (bio "IA Ninja da internet desde 1994"), mas nenhum hook/CTA/estrutura específica encontrada.

### @allesinisgalli
**Categoria:** founder
- Engajamento estimado: baixo (~8.155 seguidores, 3.548 posts)
- Temas: IA & Marketing (comunidade "IA CLUB"), lifestyle
- Limitação: apenas métricas básicas de perfil encontradas; nenhum post/hook/CTA específico indexado.

### @lonamkt
**Categoria:** marketing
- Engajamento estimado: baixo (~4.316 seguidores, apenas 2 posts no Instagram)
- Temas: tráfego pago/campanhas, marketing digital, "primeiro milhão aos 18", vendas online
- Limitação: Instagram tem pouquíssimos posts; conteúdo relevante concentrado no YouTube, fora do escopo desta pesquisa.

### @gabrielbarbosa.oficial
**Categoria:** creator
- Engajamento estimado: baixo (~7.782 seguidores, 47 posts)
- Temas: negócios digitais, faturamento online (declara 10M+ gerados), operação enxuta/remota
- Limitação: apenas bio e métricas encontradas; nenhum post/hook/CTA específico indexado.

### @opensession.co
**Categoria:** agencia
- Tom: criativo, técnico, "design system", estratégico (inferido da bio: "Brand x UX/AI x Design Systems")
- Engajamento estimado: médio (~23K seguidores, apenas 19 posts)
- Temas: branding, UX/AI, design systems, identidade de marca, direção de arte
- Limitação: perfil é de agência de design (San Diego), não criador individual; nenhum post/reel específico encontrado, apenas descrição institucional.

### @leandroladeiran
**Categoria:** marketing
- Tom: irônico, direto, humor ácido, provocador
- Formato dominante: misto (reels + forte presença em TikTok/YouTube — "Podcast do Ladeira")
- Engajamento estimado: alto (~881K TikTok citados; audiência total ~4,3M multiplataforma — Instagram isolado não confirmado)
- Temas: copywriting, marketing digital, marketing perpétuo, criação de produtos digitais, lançamentos, humor
- Limitação: número de seguidores específico do Instagram não confirmado; nenhum hook/CTA específico de post encontrado.

### @christiantriad
**Categoria:** creator
- Tom: educacional, técnico, autoridade, metodológico (método "Tríade do Tempo")
- Engajamento estimado: alto (~571K seguidores, 4.333 posts)
- Temas: IA, Tech & SaaS, produtividade, gestão de tempo (70/20/10)
- Limitação: perfil e métricas confirmados, mas nenhum hook/CTA/estrutura de reel específica indexada — resultados retornaram principalmente conteúdo institucional da metodologia.

### @oneyaraujo
**Categoria:** creator
- Hook: "Pode parecer estranho o que vou falar aqui para vocês" (outro, alta freq.); "Por que ninguém está falando de…" (fenômeno nomeado, alta); "Você precisa parar de começar os seus vídeos assim" (maioria errando, média); "Eu vou provar pra você em um minuto…" (outro, média)
- Estrutura: framework "Código Viral" — Gancho → Benefício → Mostre → CTA
- CTA: convite para seguir/produto ("Me segue para viralizar seus Reels e vender muito na internet"; venda do curso "Código Viral")
- Tom: didático, vendedor, direto, motivacional, "hacker de crescimento"
- Formato dominante: reels
- Engajamento estimado: alto (~2M seguidores, 1.273 posts, curso com 62 mil alunos)
- Temas: como viralizar Reels, ganhar seguidores, vender online, fórmulas de hook, dicas de Instagram
- Limitação: exemplos de hook vieram de conteúdo replicado no TikTok do mesmo criador, não confirmados literalmente como postados no Instagram — tratar como indicativo do padrão de discurso, não citação exata.

### @geracaotechs
**Categoria:** ia
- Tom: didático, tech, acessível (foco em ferramentas de IA)
- Temas: ferramentas de IA, criação de jogos com IA, tecnologia, comunidade paga ("Comunidade Geração Techs")
- Limitação: nenhum número de seguidores/posts nem hook/CTA específico encontrado; identidade do criador (Glauton Filho) confirmada via Threads/Pinterest, não via Instagram diretamente.

### @amandadinizmkt
**Categoria:** marketing
- Limitação: nenhum perfil de Instagram público indexado encontrado para este handle exato; busca só retornou conta correspondente no TikTok e perfis homônimos não relacionados no Instagram. Perfil pode ser pequeno, privado ou não existir mais.

### @human___academy
**Categoria:** ia
- Tom: criativo, educacional, inspirador, tech (posicionamento "maior escola de IA para criativos")
- Engajamento estimado: alto (~260K seguidores)
- Temas: educação em IA para criativos, workshops, direção criativa com tecnologia
- Limitação: perfil e posicionamento confirmados, mas nenhum post/hook/CTA específico indexado.

### @geiss11
**Categoria:** creator
- Engajamento estimado: médio (~45K seguidores, 83 posts)
- Temas: venda de produtos digitais em escala internacional
- Limitação: apenas métricas básicas de perfil (Henrique Geiss) encontradas; nenhum post/hook/CTA específico indexado.

### @nelmoricalde
**Categoria:** creator
- Limitação: nenhum post público indexado. Único dado indireto: perfil LinkedIn associado à Zuvora (Agência de IA e Performance, Porto Alegre) — não confirma conteúdo do Instagram.

### @rodrigotadewald
**Categoria:** marketing
- Tom: educacional, mentor, técnico (baixa confiança, inferido)
- Engajamento estimado: alto (~226K seguidores, 101 posts)
- Temas: uso prático de IA (bio menciona 30.000+ alunos em @asimov.academy)
- Limitação: apenas metadados agregados e bio; nenhum conteúdo de post, hook ou CTA específico indexado.

### @sujeitoprogramador
**Categoria:** ia
- Tom: didático, acessível, motivacional (inferido)
- Engajamento estimado: alto (~168K seguidores)
- Temas: programação, carreira em tecnologia, IA aplicada ao ensino de código (Matheus Fraga, 45.000+ alunos)
- Limitação: nenhum post/hook/CTA específico indexado.

### @jonathan_kamargo
**Categoria:** creator
- Limitação: nenhum perfil correspondente exato localizado (2 tentativas); resultados retornaram apenas handles similares mas distintos (@camargojay, @kamargo___, @maknoj).

### @marianatorre.s
**Categoria:** marketing
- Limitação: perfil existe (confirmado via link direto e réplica no TikTok), mas nenhuma bio, nicho, seguidores ou conteúdo retornado — resultados dominados por homônimos não relacionados.

### @marketerhub.ai
**Categoria:** marketing
- Tom: profissional, comunitário, prático (inferido da bio "Empowering Digital Marketers")
- Temas: marketing com IA, prompts, templates, cases de monetização
- Limitação: bio e descrição do produto (comunidade privada de marketing com IA) encontradas; nenhum número de seguidores ou post específico indexado.

### @marcelaluzzio
**Categoria:** marketing
- Formato dominante: reels (indício via URLs `/reel/`)
- Engajamento estimado: alto (~226K seguidores)
- Temas: marketing de conteúdo com IA, infoprodutos, vendas com IA (MBA em IA para negócios digitais, USP)
- Limitação: localizados apenas links de reels sem conteúdo/legenda extraível; nenhum hook/CTA específico confirmado.

### @gestordeaudiencia
**Categoria:** marketing
- Limitação: busca não retornou o perfil diretamente (dominada por resultados genéricos sobre Claude Code + Remotion). Associação entre esse conteúdo e a conta não é confirmada — não tratar como dado do perfil. Nenhum dado confiável de seguidores, posts ou hooks.

### @sebintel
**Categoria:** ia
- Formato dominante: reels (confirmado via `/reels/`)
- Temas: ferramentas de geração de vídeo com IA (menção a "Seedance 2.0" em post espelhado no Facebook)
- Limitação: perfil confirmado (também em TikTok/YouTube/Facebook), mas Instagram exige login para detalhes; sem seguidores, hooks ou CTA confirmados.

### @avora.ai
**Categoria:** agencia
- Hook: "Avora wasn't created just to talk about AI. It was built to turn..." (baixa freq., 1 amostra)
- CTA (parcial): "Siga @avora.ai para conteúdos diários sobre IA na prática!"
- Tom: prático, direto, orientado a aplicação
- Temas: IA aplicada no dia a dia, posicionamento de marca
- Limitação: conta baseada em Belo Horizonte-MG (confirmado via Facebook irmão @avora.ia); apenas trechos parciais de 2 posts indexados, sem contagem de seguidores.

### @ogabrieeldias
**Categoria:** creator
- Limitação: handle exato não localizado; resultados retornaram perfis distintos não confirmados como o mesmo (@ogabrielsa/Gabriel Sá no X; vários @gabrielXdias não relacionados a IA).

### @rodrigobindes
**Categoria:** founder
- Tom: mentor, orientado a resultado/faturamento, direto (inferido)
- Engajamento estimado: alto (~278K seguidores, 1.835 posts)
- Temas: mentoria para agências de marketing digital, faturamento (R$100k/mês), parcerias (@marketingpararestaurante, @ultralizeoficial)
- Limitação: metadados agregados e bio confirmados; nenhum post/hook/CTA específico indexado.

### @franklim.gui
**Categoria:** creator
- Tom: transparente, jornada pessoal, motivacional (inferido)
- Engajamento estimado: alto (~104K seguidores, 58 posts)
- Temas: jornada até R$7M em 3 anos, venda de produtos "lowticket", tráfego direto
- Limitação: conteúdo relacionado (lowticket, tráfego) majoritariamente localizado no YouTube dele, não confirmado como replicado literalmente no Instagram.

### @gabrielsamp.ai
**Categoria:** ia
- Limitação: handle não confirmado como existente no Instagram (apenas presença correspondente no TikTok localizada, sem detalhes). Perfis "Gabriel Sampaio" no Instagram (surfista, cantor sertanejo) parecem pessoas diferentes.

### @maestrosdaia
**Categoria:** ia
- Hook: "O agente de IA que trabalha enquanto você dorme" (baixa freq., via TikTok)
- Tom: comunitário, aspiracional, prático (inferido — "Maestria", "Lyra Academy")
- Formato dominante: reels (confirmado via `/reels/` no Instagram e vídeos no TikTok)
- Engajamento estimado: médio-alto (~72K TikTok, 577.5K likes — Instagram não confirmado separadamente)
- Temas: agentes de IA, automação, comunidade/curso
- Limitação: métricas são do TikTok, não confirmadas diretamente no Instagram; frase de hook não confirmada como postada literalmente no Instagram.

### @brandsdecoded__
**Categoria:** marketing
- Estrutura: carrossel com copy "estilo BrandsDecoded" + imagens cinemáticas + CTA de conversão (descrito pela marca, não confirmado por post específico)
- Tom: estratégico, técnico, autoral, orientado a dados, premium
- Formato dominante: carrossel
- Engajamento estimado: alto (~301K seguidores, 1.734 posts, agência com >20 mil clientes segundo fontes)
- Temas: criação de conteúdo com IA (Claude/Canva/Figma), carrosséis de autoridade, "Content Machine 3.0"
- Limitação: nenhuma frase de hook/CTA literal encontrada — apenas descrições de terceiros sobre o método.

### @anatex
**Categoria:** creator
- Tom: instrutivo, acolhedor, prático, motivacional
- Formato dominante: reels
- Engajamento estimado: alto (626K–671K seguidores, fontes inconsistentes entre si)
- Temas: IA para negócios, produtividade/automação, mentoria para mulheres 40+
- Limitação: nenhum post/hook literal indexado; apenas descrição de posicionamento da conta.

### @larissagomes.ia
**Categoria:** ia
- Hook: "Peça o chatGPT para analisar o feed do seu instagram 🧠" (1 amostra, via cross-post no TikTok)
- Estrutura: abertura com dica prática → prompt completo copiável → CTA de seguir → hashtags
- CTA: "siga @larissagomes.ia para receber mais conteúdos como esse"
- Tom: didático, acessível, direto
- Engajamento estimado: médio (~15K seguidores)
- Temas: prompts de ChatGPT/IA para marketing, análise de perfil com IA, negócio enxuto com IA
- Limitação: exemplo de conteúdo veio de cross-post no TikTok, não confirmado como publicado originalmente no Instagram.

### @thiagozaao
**Categoria:** creator
- Limitação: nenhum perfil público indexado com esse handle exato (2 tentativas, incluindo variação "thiago zaão"); perfil pode ser pequeno, recente ou com grafia diferente.

### @neuwebstudio
**Categoria:** agencia
- Tom: criativo, técnico, moderno, inspirador
- Formato dominante: misto (forte presença também replicada no TikTok)
- Engajamento estimado: médio (~52K seguidores, 168 posts)
- Temas: web design cinemático, animações parallax, tutoriais Figma/Webflow, portfólio de sites
- Limitação: sem frases de hook/CTA literais; dados vieram majoritariamente do TikTok espelhado.

### @laschuk
**Categoria:** founder
- Tom: direto, contrarian, autoral, cru
- Engajamento estimado: médio (~36K seguidores, 200 posts)
- Temas: email marketing, "owned traffic" (tráfego próprio vs. dependência de anúncios pagos)
- Limitação: bio confirmada ("EmailHacker", "not for sale"), mas nenhum post individual indexado.

### @maestroptompts
**Categoria:** ia
- Limitação: nenhum perfil público indexado com esse handle exato. Encontrado apenas site "maestroprompts.com" ("Mestre dos Prompts", grafia diferente) — possível marca relacionada, não confirmada como o mesmo perfil.

### @faladantasmkt
**Categoria:** marketing
- Tom: didático, vendedor, autêntico, acolhedor
- Formato dominante: misto (reels + stories, forte uso de stories para vendas)
- Engajamento estimado: alto (~99K seguidores no Instagram; +2M multi-rede, segundo fontes)
- Temas: mentoria de conteúdo/negócios digitais, atração de clientes premium, vendas via stories
- Limitação: variações de handle (@faladantas.mkt, @faladantas) podem ser contas diferentes/antigas da mesma pessoa — não confirmado qual é a atual.

### @lindsay.ia
**Categoria:** ia
- CTA (padrão descrito): comentário-gatilho (ex.: "SETUP"/"FAST") → guia via DM
- Estrutura: conteúdo educativo sobre IA aplicada → CTA de comentário → funil automático de DM
- Tom: prático, educador, orientado a resultado
- Engajamento estimado: médio (~45K seguidores combinados, fonte terceira)
- Temas: renda com IA (Claude, n8n, no-code), automação de negócios
- Limitação: correspondência com a criadora "Lindsay.Ai / AI Money Hub" (fonte: CreatorDB) não confirmada como o mesmo perfil — tratar com cautela.

### @andrevictor.m
**Categoria:** marketing
- Hook: "Fiz meu primeiro milhão aos 18 anos desse jeito..." (transformação silenciosa, alta freq. — via títulos de vídeos/podcasts)
- Estrutura: storytelling pessoal (origem humilde → marco de sucesso → lição/CTA de negócio digital)
- Tom: ousado, motivacional, provocador, aspiracional
- Formato dominante: reels
- Engajamento estimado: alto (~244K seguidores)
- Temas: dropshipping, infoprodutos, empreendedorismo digital, marcos de riqueza pessoal
- Limitação: frases vieram de títulos de vídeos/podcasts (YouTube/Spotify), não de posts do Instagram diretamente.

### @drisiano
**Categoria:** creator
- Limitação: nenhum perfil público indexado com esse handle exato (2 tentativas); apenas handles parecidos e não relacionados (@driso__, @driano, @drisansone).

### @brun0gpt
**Categoria:** ia
- Estrutura: gancho controverso (0–3s) → conteúdo de valor com prompt de IA → CTA de curso/templates
- Tom: didático, orientado a resultado, autoridade técnica, direto
- Formato dominante: misto (10 templates reel, 7 carrossel, 6 stories, conforme curso vendido)
- Engajamento estimado: alto (~157K seguidores; crescimento de 0 a 96K em ~10 meses sem tráfego pago, segundo fonte)
- Temas: ChatGPT para marketing/vendas, templates de conteúdo com IA, crescimento orgânico
- Limitação: números de crescimento/templates vêm de material promocional do próprio curso, não confirmados por posts individuais.

### @maxcarrau.ia
**Categoria:** ia
- Limitação: nenhum perfil público indexado com esse handle exato. Existe handle similar "@maxcarrau" (sem ".ia") e canal YouTube "Max carrau | IA", correspondência não confirmada.

### @noevarner
**Categoria:** creator
- Tom: técnico, empreendedor, orientado a automação, direto
- Engajamento estimado: baixo/médio (conta associada @noevarner.ai: 91.740 seguidores, 625 posts, taxa de engajamento de 0,45% segundo Social Blade)
- Temas: sistemas de IA para conteúdo/ads/crescimento, automação de negócios, "Claude Code Ads Automation"
- Limitação: handle exato tem múltiplas variações associadas (@therealnoevarner, @noevarner3, @noevarner.ai); não ficou claro qual corresponde exatamente à URL configurada.

### @yikchanltd
**Categoria:** creator
- Hook/Estrutura: série de 7 episódios — título + gancho de 8 palavras + pontos de fala + payoff na tela + cliffhanger (alta freq., descrita como método recorrente)
- CTA: "DM 'Ai' to join a $10,000/month Passive Income Group like 500+ members"
- Tom: mentor, motivacional, técnico, orientado a riqueza
- Formato dominante: reels
- Engajamento estimado: alto (~79K seguidores, 1.296 posts; reels citados com até 10M de views)
- Temas: IA para eCommerce, geração de vídeo com IA (Seedance), mentoria de renda passiva, biblioteca de 2000+ hooks virais
- Limitação: nenhuma limitação relevante — dados razoavelmente substanciais encontrados via busca.

---

## Perfis Sugeridos pelo Sistema
Não aplicável — execução em Modo Análise (lista de perfis já configurada), Passo 1A (Modo Descoberta) não foi executado.

---

## Limitações de Dados

- **@yikC** — handle exato não localizado via busca; resultados retornaram contas não relacionadas.
- **@eujoaotorresz** — handle exato não indexado; correspondência aproximada não confirmada.
- **@rafa.grandi** — perfil localizado é conta pessoal pequena, sem relação aparente ao nicho monitorado.
- **@nathanhodgson** — handle ambíguo; múltiplas pessoas homônimas, nenhuma confirmada como perfil do nicho.
- **@ai** — handle de 2 letras, nenhuma informação específica indexada.
- **@ninja.automacoes** — apenas descrição genérica de nicho; sem post/métrica específica.
- **@eduardocavalcanti** — handle ambíguo (múltiplos "Eduardo Cavalcanti").
- **@lonamkt** — Instagram quase sem posts (2); atividade principal é no YouTube.
- **@opensession.co** — perfil institucional (agência), sem post/reel específico indexado.
- **@geracaotechs** — sem seguidores/posts/hook/CTA confirmados.
- **@amandadinizmkt** — nenhum perfil de Instagram público indexado com este handle.
- **@nelmoricalde** — nenhum post público indexado; apenas associação indireta via LinkedIn.
- **@jonathan_kamargo** — nenhum perfil correspondente exato localizado.
- **@marianatorre.s** — perfil existe, mas sem bio/nicho/conteúdo retornado nas buscas.
- **@marketerhub.ai** — apenas bio/descrição do produto; sem seguidores ou post específico.
- **@gestordeaudiencia** — associação entre conteúdo encontrado e o perfil é incerta; não deve ser tratada como confirmada.
- **@sebintel** — perfil confirmado, mas Instagram exige login; sem métricas ou conteúdo.
- **@ogabrieeldias** — handle não confirmado; resultados são de perfis distintos.
- **@gabrielsamp.ai** — handle não confirmado como existente no Instagram.
- **@thiagozaao** — nenhum perfil público indexado com este handle.
- **@maestroptompts** — nenhum perfil localizado; apenas marca de grafia similar.
- **@lindsay.ia** — correspondência com a criadora encontrada não confirmada como o mesmo perfil.
- **@drisiano** — nenhum perfil público indexado com este handle.
- **@maxcarrau.ia** — nenhum perfil público indexado; handle similar sem ".ia" encontrado, correspondência não confirmada.
- **@noevarner** — múltiplas variações de handle associadas; não confirmado qual corresponde exatamente à URL configurada.
- Demais perfis com dado parcial (bio/seguidores confirmados, mas sem hook/CTA/tema de post específico): ver limitação individual em cada seção acima.

**Resumo geral:** dos 61 perfis ativos, a maioria teve apenas metadados de perfil (bio, seguidores, posicionamento) confirmados via busca — não conteúdo indexado de posts individuais com hooks/CTAs textuais exatos. Cerca de 22 perfis tiveram handle não localizado ou ambíguo. Os perfis com evidência mais completa de hook/estrutura/CTA foram @oneyaraujo, @nick_saraev, @chase.h.ai, @andrevictor.m, @yikchanltd e @larissagomes.ia (parcial, via cross-post no TikTok). Nenhum dado de engajamento, hook ou conteúdo de post foi inventado; toda lacuna foi documentada explicitamente conforme regra do Módulo 2.
