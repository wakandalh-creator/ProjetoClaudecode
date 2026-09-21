# Análise de Perfis Instagram — 2026-09-21

**Modo de execução:** Análise (lista de perfis já configurada em `config/profiles.json`, Passo 2 do Módulo 2 executado diretamente, sem etapa de descoberta).

**Nota metodológica geral:** Em todas as tentativas desta execução, o WebFetch direto para `instagram.com` (e domínios relacionados) retornou bloqueio de rede (`EGRESS_BLOCKED`) pelo proxy do ambiente. Toda a coleta foi feita via WebSearch (múltiplas queries por perfil), que majoritariamente indexa metadados de perfil (bio, contagem de seguidores/posts) e menções de terceiros (agregadores, blogs, cross-posts em TikTok/Threads/YouTube), raramente o texto literal de posts individuais do Instagram. **Nenhum dado de engajamento, hook, CTA ou tema de post foi inventado.** Onde a busca não trouxe evidência direta e específica do perfil, o campo foi marcado "dado insuficiente" e a limitação foi documentada por perfil. Hooks/CTAs vindos de conteúdo espelhado em outra rede (TikTok, Threads, YouTube) e não confirmados como publicados literalmente no Instagram estão sinalizados como tal. Onde a análise identificou ambiguidade entre contas homônimas ou um handle sem correspondência confiável, isso está sinalizado explicitamente — nenhum dado de conta diferente foi atribuído ao perfil-alvo.

**Perfis com handle não localizado ou não confirmável nesta execução:** @yikC, @eujoaotorresz, @ai, @amandadinizmkt, @jonathan_kamargo, @ogabrieeldias, @gabrielsamp.ai (só localizado no TikTok), @drisiano, @maestroptompts, @thiagozaao.

**Perfis com forte ambiguidade entre contas homônimas (dados abaixo referem-se à melhor correspondência identificada, sinalizada em cada seção):** @nathanhodgson (dados de @nathanhodgson.ai), @gabriel.adamuchi, @eduardocavalcanti, @maxcarrau.ia (nenhum dado atribuído), @noevarner (nenhum dado atribuído — números pertencem a @noevarner.ai).

**Alerta de possível handle incorreto:** o único @rafa.grandi localizado (Rafael Grandi Borges, analista jurídico do SPGG/RS, 247 seguidores, 36 posts) não corresponde à categoria "marketing" esperada. Recomenda-se confirmar o handle exato com o Lucas.

---

## Visão Geral dos Perfis

| Perfil | Categoria | Formato Dominante | Engajamento | Hook / Padrão Observado |
|--------|-----------|--------------------|-------------|--------------------------|
| @charliehills | creator | dado insuficiente | médio (~88K) | dado insuficiente |
| @yikC | creator | dado insuficiente | dado insuficiente | perfil não localizado (homônimos não confirmados) |
| @eujoaotorresz | creator | dado insuficiente | dado insuficiente | perfil não localizado |
| @fabianocarvalhojr | founder | dado insuficiente | médio-alto (~130K) | dado insuficiente |
| @rafa.grandi | marketing | dado insuficiente | baixo (~247) | perfil encontrado não bate com categoria — possível handle incorreto |
| @brusantanna.ai | ia | reels | dado insuficiente | educacional/lista numerada (via Threads) |
| @vendedorglobal | negocio-digital | misto | alto (~83K) | dado insuficiente |
| @oluizmain | creator | reels | dado insuficiente | "Nunca foi sorte" (título de reel) |
| @nick_saraev | automacao | reels | alto (~550K) | "Comment 'AUTOMATION' to get these Blueprints" (9+ variações confirmadas) |
| @nathanhodgson | ia | dado insuficiente | alto (~128K, via @nathanhodgson.ai) | dado insuficiente — handle ambíguo |
| @ai | ia | dado insuficiente | dado insuficiente | perfil não localizado/confirmado |
| @ana.gsoares | marketing | dado insuficiente | médio (~146K) | dado insuficiente |
| @chase.h.ai | ia | misto | alto (~228K) | dado insuficiente (CTA de bio confirmado: DM "Ready") |
| @leosoares.ia | ia | misto | alto (~219K) | dado insuficiente |
| @gabriel.adamuchi | creator | reels | dado insuficiente | dado insuficiente — identidade ambígua |
| @viverdeia.ai | ia | dado insuficiente | médio (~109K) | CTA de comentário confirmado ("Comenta 'TEMPO'...") |
| @ninja.automacoes | automacao | dado insuficiente | baixo-médio (~34K) | prova de resultado (bio: "Faturei R$1MM sozinho") |
| @nikolassasso | creator | dado insuficiente | alto (~181K) | paradoxo/contraste (bio: "Cresça sem trocar tempo por dinheiro") |
| @eduardocavalcanti | founder | dado insuficiente | baixo-médio (~26K) | dado insuficiente — forte ambiguidade de homônimos |
| @jonylan | creator | dado insuficiente | alto (~306K) | branding pessoal ("IA Ninja desde 1994") |
| @allesinisgalli | founder | dado insuficiente | baixo (~8,1K–61,3K, divergente) | dado insuficiente |
| @lonamkt | marketing | reels (baixa confiança) | baixo (~4,3K) | transformação/façanha ("Primeiro milhão aos 18") |
| @gabrielbarbosa.oficial | creator | dado insuficiente | baixo (~7,8K) | autoridade/prova social ("+10MM faturados na internet") |
| @opensession.co | agencia | dado insuficiente | médio (~23K) | dado insuficiente |
| @leandroladeiran | marketing | dado insuficiente | alto (contagem IG não confirmada) | contraste/ironia (indício via TikTok, não confirmado no IG) |
| @christiantriad | creator | dado insuficiente | alto (~571K) | dado insuficiente |
| @oneyaraujo | creator | reels | alto (~2M) | Gancho → Benefício → Mostre → CTA ("Código Viral") |
| @geracaotechs | ia | dado insuficiente | dado insuficiente | dado insuficiente |
| @amandadinizmkt | marketing | dado insuficiente | dado insuficiente | perfil não confirmado (forte ambiguidade) |
| @human___academy | ia | dado insuficiente | alto (~260K) | CTA fixo de bio ("Inscreva-se no Workshop AI Videolab") |
| @geiss11 | creator | misto | médio (~45K) | dado insuficiente |
| @nelmoricalde | creator | dado insuficiente | dado insuficiente | dado insuficiente |
| @rodrigotadewald | marketing | misto | alto (~226K) | dado insuficiente |
| @sujeitoprogramador | ia | misto | alto (~165K) | dado insuficiente |
| @jonathan_kamargo | creator | dado insuficiente | dado insuficiente | perfil não localizado |
| @marianatorre.s | marketing | dado insuficiente | dado insuficiente | perfil não confirmado com detalhe |
| @marketerhub.ai | marketing | dado insuficiente | dado insuficiente | dado insuficiente |
| @marcelaluzzio | marketing | dado insuficiente | médio-alto (~226K) | dado insuficiente |
| @gestordeaudiencia | marketing | dado insuficiente | dado insuficiente | dado insuficiente |
| @sebintel | ia | dado insuficiente | dado insuficiente | dado insuficiente (número de 9M não corroborado, descartado) |
| @avora.ai | agencia | dado insuficiente | dado insuficiente | paradoxo/contraste (truncado) |
| @ogabrieeldias | creator | dado insuficiente | dado insuficiente | perfil não localizado |
| @rodrigobindes | founder | misto | alto (~278K) | dado insuficiente |
| @franklim.gui | creator | misto | médio-alto (~104K) | dado insuficiente |
| @gabrielsamp.ai | ia | dado insuficiente | dado insuficiente | perfil só localizado no TikTok |
| @maestrosdaia | ia | misto | dado insuficiente | dado insuficiente |
| @brandsdecoded__ | marketing | carrossel | alto (~301K) | paradoxo/contraste (metodologia divulgada, não citação literal) |
| @anatex | creator | dado insuficiente | alto (~716K) | dado insuficiente |
| @larissagomes.ia | ia | dado insuficiente | médio (~15K) | CTA de troca por comentário ("Comenta ELITE...") |
| @thiagozaao | creator | dado insuficiente | dado insuficiente | perfil não localizado |
| @neuwebstudio | agencia | misto (não confirmado) | médio (~52K) | dado insuficiente |
| @laschuk | founder | dado insuficiente | médio (~36K) | dado insuficiente |
| @maestroptompts | ia | dado insuficiente | dado insuficiente | perfil não localizado |
| @faladantasmkt | marketing | misto | médio-alto (~99K) | dado insuficiente |
| @lindsay.ia | ia | dado insuficiente (provável reels) | médio (~45K, combinado multi-rede) | CTA de comentário-gatilho ("SETUP"/"FAST") |
| @andrevictor.m | marketing | reels | alto (~244K) | maioria errando/contraste |
| @drisiano | creator | dado insuficiente | dado insuficiente | perfil não localizado |
| @brun0gpt | ia | misto | alto (~157K) | dado insuficiente |
| @maxcarrau.ia | ia | dado insuficiente | dado insuficiente | dado insuficiente — ambiguidade não resolvida |
| @noevarner | creator | dado insuficiente | dado insuficiente | dado insuficiente — ambiguidade com @noevarner.ai |
| @yikchanltd | creator | misto (não confirmado) | médio-alto (~79K) | dado insuficiente |

---

## Análise Detalhada por Perfil

### @charliehills
**Categoria:** creator
**Bio:** "💙 I help you (actually) use AI 📧 collabs@charliehills.ai 👇 100+ free AI prompts, guides & tools"
**Engajamento estimado:** médio (~88K seguidores, 324 seguindo, 260 posts)
**Tom (inferido da bio, baixa confiança):** educativo, direto, prático
**Limitação:** WebFetch bloqueado. Só metadados de bio/contagens indexados; nenhum post/reel individual acessível. Múltiplas contas homônimas (@charliehills.studio, @charliehillsracing, @charliehills_, @charliehills.ai) — @charliehills (88K) identificado como o mais relevante para "creator" de IA, sem garantia total.

### @yikC
**Categoria:** creator
**Limitação:** Não foi possível localizar com confiança um perfil correspondente ao handle exato "@yikC". Buscas com múltiplas variações retornaram apenas homônimos não relacionados (YWCA International Kids Club, Yik Café, Sifu Yik Chan, Yik Yak app). WebFetch bloqueado. Nenhum dado atribuído.

### @eujoaotorresz
**Categoria:** creator
**Limitação:** Handle exato não localizado. O mais próximo encontrado foi @joaotorresz (sem "eu", 2.039 seguidores, 5 posts) e outros "@eujoao..." com nomes diferentes — não usados para não misturar contas. WebFetch bloqueado. Possível conta pequena/pouco indexada, privada, ou handle mudou.

### @fabianocarvalhojr
**Categoria:** founder
**Bio:** "Crio Agentes de IA que vendem e operam Negócios 24/7 Te Ensino na Aula Grátis"
**Engajamento estimado:** médio-alto (~130K seguidores, 1.865 seguindo, 1.417 posts)
**Tom (inferido da bio):** direto, comercial, educativo
**Limitação:** WebFetch bloqueado. Um fragmento de busca ("Quem mais? 😅 ➡️ Siga @fabianocarvalhojr...") não pôde ser confirmado como legenda própria (pode ser menção/repost de terceiros) — não usado como exemplo confiável.

### @rafa.grandi
**Categoria:** marketing
**Bio:** "Analista Jurídico SPGG/RS e Pai do Cássio" (Rafael Grandi Borges)
**Engajamento estimado:** baixo (~247 seguidores, 284 seguindo, 36 posts)
**⚠️ Alerta:** o único @rafa.grandi localizado é um perfil pessoal pequeno sem qualquer indício de atuação em marketing/conteúdo — não corresponde à categoria "marketing" esperada. Ou é um handle coincidente com outra pessoa de marketing que não apareceu na busca, ou o perfil de marketing real usa handle ligeiramente diferente. **Recomenda-se confirmar o handle exato com o Lucas antes de usar esses dados.**

### @brusantanna.ai
**Categoria:** ia
**Bio:** "Bruna Santanna | Estrategista de IA" (texto completo não capturado)
**Hook/estrutura:** conteúdo educacional em lista numerada ("Segundo: conversas longas matam seu limite...") — confirmado no Threads do mesmo handle, não confirmado como publicado no Instagram propriamente.
**CTA:** "comenta [palavra-chave]" para acessar aulas/conteúdo
**Tom:** técnico, didático, direto, prático
**Formato dominante:** reels (indicado por URLs /reels/ e espelhamento em TikTok/Threads)
**Top temas:** uso otimizado do Claude/Claude Code, estratégia de conteúdo com IA, aulas/comunidade
**Limitação:** WebFetch bloqueado. Seguidores não encontrados. Textos específicos vêm de Threads/TikTok sob o mesmo handle, não do feed do Instagram diretamente.

### @vendedorglobal
**Categoria:** negocio-digital
**Bio:** "📈 E-commerce & IA | +100M Views 🔥 Treino apenas quem está pronto p/ lucrar ⚡ Troop do MAESTRO!"
**Engajamento estimado:** alto (~83K seguidores, 2.280 posts, 4.745 seguindo)
**Tom (inferido):** comercial, aspiracional, direto
**Limitação:** WebFetch bloqueado. Nenhuma busca retornou texto exato de hook/gancho específico. Estrutura, CTA de post e temas específicos não confirmados.

### @oluizmain
**Categoria:** creator
**Bio:** não localizada em texto completo; descrição recorrente "Creator Mobile"/"Mentor CEO"
**Hook:** "🍀 Nunca foi sorte. #videomakermobile" (título de post); "📲 Faço meus trabalhos inteiramente com o meu [celular]..." (título de reel truncado)
**Tom:** motivacional, prático, autoral, aspiracional
**Formato dominante:** reels
**Top temas:** produção de vídeo com celular, bastidores, curso "Mobile Pro", motivação de criador
**Limitação:** WebFetch bloqueado. Seguidores não encontrados (página exige login). Apenas títulos truncados de 2-3 reels localizados.

### @nick_saraev
**Categoria:** automacao
**Bio:** "🚀 Founder @ Maker School 🤖 Helping 2000+ beginners land their First AI client 👇 Get your first client in 90 days or money back"
**Engajamento estimado:** alto (~550K seguidores, 368 posts, 165 seguindo)
**Hook/CTA padrão:** "Comment '[PALAVRA-CHAVE]' to get [recurso gratuito]" — padrão repetido em 9+ reels distintos confirmados: "AUTOMATION", "QWEN", "IMAGES", "VOICE", "BLUEPRINT", "EMAIL", "APIFY", "VIDEO"
**Estrutura típica:** [tema de automação] + promessa de benefício/ROI + CTA "Comment '[PALAVRA-CHAVE]'"
**Tom:** direto, orientado a resultado, técnico, promocional, acessível a iniciantes
**Formato dominante:** reels (confirmado)
**Top temas:** automação com IA (n8n, Qwen), geração de imagem/voz/vídeo por IA, templates de automação, conseguir o primeiro cliente de IA
**Limitação:** Perfil com melhor cobertura de evidência do lote — ainda assim, apenas títulos/hooks iniciais confirmados, não o corpo completo das legendas.

### @nathanhodgson
**Categoria:** ia
**⚠️ Ambiguidade de handle:** três variações distintas encontradas — @nathanhodgson_ (3.005 seguidores, indicando migração), @nathanjameshodgson (334 seguidores, eletricista, provavelmente pessoa diferente) e @nathanhodgson.ai (128K seguidores, foco em negócios com IA — melhor correspondência com a categoria "ia"). Dados abaixo referem-se a @nathanhodgson.ai, não ao handle literal.
**Bio:** "Built a 6-Figure Business Powered By AI • Trusted by Google · Meta · OpenAI"
**Engajamento estimado:** alto (~128K seguidores, 339 posts, 86 seguindo — de @nathanhodgson.ai)
**Limitação:** Recomenda-se confirmar manualmente com o Lucas qual é o handle/conta correto.

### @ai
**Categoria:** ia
**Limitação:** WebFetch bloqueado. Buscas com múltiplas variações não retornaram nenhuma evidência direta sobre bio, seguidores ou posts deste handle específico — apenas handles parecidos mas diferentes (@welcome.ai, @getintoai, @officialai). Não foi possível confirmar sequer se é uma conta ativa/pública relevante.

### @ana.gsoares
**Categoria:** marketing
**Bio:** CEO de @uniagiloficial (Universidade Ágil), apresentadora do podcast @agilizesepodcast; métodos ágeis + liderança + IA (incluindo Claude); criadora do "Método LACP"; 10k+ profissionais treinados, comunidade 200k+
**Engajamento estimado:** médio (~146K seguidores, 2.840 posts)
**Top temas (inferido de bio/site):** metodologia ágil (LACP), liderança, IA aplicada à gestão de projetos, podcast Agilize-se
**Limitação:** WebFetch bloqueado. Bio, seguidores e área de atuação confirmados via LinkedIn/site oficial, mas nenhum texto literal de post/reel específico foi encontrado.

### @chase.h.ai
**Categoria:** ia
**Bio:** "🤖 | Making AI Simple ⚡️ | DM 'Ready' to Apply For 1:1 Mentorship 🚀 | Master Claude Code👇" (confirmada via fonte agregadora)
**CTA padrão:** DM "Ready" para aplicar para mentoria 1:1 (confirmado, literal na bio)
**Engajamento estimado:** alto (~228K-229K seguidores, variação entre fontes 221K-228K)
**Top temas:** Claude Code (workflows, deploy de agentes), automação no-code, mentoria/monetização com IA
**Limitação:** WebFetch bloqueado. Nenhum hook, tom de voz ou caption de post individual localizado com texto exato.

### @leosoares.ia
**Categoria:** ia
**Bio:** "Léo Soares | IA p/ Negócios" — CEO da Acelera IA 🤖 "AI must generate RESULTS" (variações de título também aparecem: "IA p/ Infoprodutos", "IA p/ Lançamentos")
**Engajamento estimado:** alto (~219K seguidores, 2.226 posts)
**Top temas (inferido):** IA aplicada a negócios, infoprodutos e lançamentos, empreendedorismo
**Limitação:** WebFetch bloqueado. Nenhum texto literal de post/reel/carrossel localizado.

### @gabriel.adamuchi
**Categoria:** creator
**⚠️ Ambiguidade de identidade:** pelo menos 3 handles/contas associados a "Gabriel Adamuchi" (@gabriel.adamuchi "IA Fácil", @fenixytb, @adamuchi.gabriel) — dados de seguidores encontrados pertencem majoritariamente a contas irmãs, não atribuídos aqui.
**Bio (inferida):** "IA Fácil" — tornar IA fácil de aprender e lucrar
**Formato dominante:** reels
**Top temas (não confirmados como centrais deste handle específico):** prompts de IA, tutoriais "IA descomplicada"
**Limitação:** WebFetch bloqueado. Nenhum texto literal de post, hook, CTA ou legenda localizado.

### @viverdeia.ai
**Categoria:** ia
**Bio (inferida):** "A Plataforma das Empresas que Crescem com IA" — +2000 empresas aceleradas com soluções "Plug & Play"
**CTA confirmado (em post real):** "Comenta 'TEMPO' que eu te envio agora a @viverdeia.ai pra..." (post instagram.com/p/DYz-58MxdbQ/)
**Engajamento estimado:** médio (~109K seguidores, 524 posts, 3 seguindo — conta institucional)
**Limitação:** WebFetch bloqueado. Conta institucional (marca "Viver de IA"), distinta do perfil pessoal do fundador Rafael Milagre (@rafaelmilagre) — cuidado para não confundir. Estrutura, tom e temas específicos não confirmados.

### @ninja.automacoes
**Categoria:** automacao
**Bio:** "🤖Faturei R$1MM sozinho, com agentes de IA 📚Te ensino a criar um negócio automático 🥷 Clica no link pra saber mais"
**CTA padrão:** "Clica no link pra saber mais" (bio)
**Engajamento estimado:** baixo-médio (~34K seguidores, 65 posts, 79 seguindo)
**Limitação:** WebFetch bloqueado. Conta gerida por Matheus Pessoa. Nenhuma legenda de post real confirmada além da bio.

### @nikolassasso
**Categoria:** creator
**Bio:** "🤖 Criei robôs que fazem o trabalho duro por mim 👨🏻‍💻 Cresça sem trocar ⌛ por dinheiro 🧠 Conteúdo. Vendas. Automação. 👇 Vídeos infinitos com IA"
**Hook modelos:** paradoxo/contraste ("Cresça sem trocar tempo por dinheiro"); transformação silenciosa ("Criei robôs que fazem o trabalho duro por mim") — ambos texto da bio
**Engajamento estimado:** alto (~181K seguidores, 1.469 posts, 821 seguindo)
**Top temas (inferido):** IA para negócios, automação, vendas, prompts (produto "Prompt Hacker")
**Limitação:** WebFetch bloqueado. Ambiguidade de homônimos (@eusounikolas, @nikolas_sassoafiliado, @nikolassassooficial) — dados referem-se apenas ao handle principal confirmado. Um possível CTA foi descartado por falta de confirmação de autoria.

### @eduardocavalcanti
**Categoria:** founder
**⚠️ Maior ambiguidade de homônimos do lote:** três "Eduardo Cavalcanti" distintos — (1) o analisado aqui, ligado a "Blog da Engenharia"/IBIA, ~26K seguidores; (2) cofundador da Fundamentei, que publica por @fundamentei (~65K), não por este handle; (3) @profeduardocavalcanti, não relacionado.
**Bio (indireta):** fundador do "Blog da Engenharia", Presidente do IBIA (Instituto Brasileiro de Inteligência Artificial)
**Engajamento estimado:** baixo-médio (~26K seguidores, 1.674 posts, 1.953 seguindo)
**Limitação:** WebFetch bloqueado. Um fragmento de legenda ("Vivemos na era da inteligência artificial...") tem autoria não 100% confirmada — tratado como indício, não confirmação.

### @jonylan
**Categoria:** creator
**Bio:** "Inteligência Artificial Ninja da internet desde 1994 ✉️ falecomjony@outlook.com 📣 Palestras, treinamentos e consultorias Builder em @googlebrasil"
**Hook:** branding pessoal — "Inteligência Artificial Ninja da internet desde 1994" (texto da bio)
**Engajamento estimado:** alto (~306K seguidores, 3.255 posts, 1.076 seguindo)
**Top temas (inferido):** marketing digital, vendas, inteligência artificial
**Limitação:** WebFetch bloqueado. Um reel de terceiros creditando "@jonylan" não pôde ser confirmado como legenda original (parece reupload) — não usado como hook confirmado.

### @allesinisgalli
**Categoria:** founder
**Bio (paráfrase, não literal):** mentora de marketing com IA, fundadora da "IA CLUB COMUNIDADE", 15+ anos de marketing (Austrália e Brasil)
**Engajamento estimado:** baixo (ER 0,45% segundo Heepsy) — divergência de seguidores entre fontes: 8.155 (direto do Instagram) vs. 61,3K (Heepsy), não resolvida
**Tom (inferido):** mentora, educativa, motivacional
**Limitação:** WebFetch bloqueado. Nenhuma legenda, hook ou CTA específico localizado — apenas posicionamento geral via LinkedIn/Heepsy.

### @lonamkt
**Categoria:** marketing
**Bio:** "🇮🇹 Primeiro milhão aos 18 👇 Me acompanhe aqui"
**Hook:** transformação/façanha (paradoxo de idade) — "Primeiro milhão aos 18" (bio, não confirmado como abertura de reel)
**CTA:** "Me acompanhe aqui" (bio)
**Engajamento estimado:** baixo (~4.316 seguidores, 490 seguindo, apenas 2 posts — conta pequena/recente)
**Limitação:** Volume muito baixo de posts (2) impede análise de padrão real. Títulos de vídeos do YouTube associados ("Do 0 ao R$1.000.000" etc.) não confirmados como pertencentes ao mesmo Instagram.

### @gabrielbarbosa.oficial
**Categoria:** creator
**Bio:** "🚀 +10MM faturados na internet 🌎Te ensino a ter uma operação enxuta e lucrativa de qualquer lugar do mundo" (nome: "Gabriel Barbosa | Negócios Digitais")
**Hook:** autoridade/prova social — "+10MM faturados na internet" (bio)
**Engajamento estimado:** baixo (~7.782 seguidores, 754 seguindo, 47 posts)
**Limitação:** Múltiplos homônimos "Gabriel Barbosa" (incluindo o jogador "Gabigol") — perfil correto identificado com confiança pelo título exato e bio de negócios digitais, mas sem dado de conteúdo além da bio.

### @opensession.co
**Categoria:** agencia
**Bio:** "Brand x UX/AI x Design Systems. We help designers and brands level up their creativity."
**Engajamento estimado:** médio (~23K seguidores, 538 seguindo, 19 posts)
**Top temas (inferido):** design systems, branding, IA aplicada a design (MCP, Figma)
**Limitação:** WebFetch bloqueado. Empresa de design (San Diego, EUA) com forte presença em blog/Medium/Substack — usado só como corroboração de tema geral. Nenhuma legenda, hook ou CTA de post localizado.

### @leandroladeiran
**Categoria:** marketing
**Nome confirmado:** Leandro Ladeira Neiva. Bio do Instagram não localizada em texto verbatim.
**Hook (indício via TikTok, mesmo handle, não confirmado no IG):** "Quem não sabe COPYWRITING dançou… Meu gingado te influenciou a me seguir, afinal?"
**Engajamento estimado:** alto — referência nacional em copywriting; audiência combinada ~4,3M (Instagram+YouTube+TikTok) segundo hafi.pro; 881K seguidores confirmados no TikTok
**Top temas:** copywriting, métodos "Light Copy" e "Stories 10x", vendas, lançamentos digitais
**Limitação:** WebFetch bloqueado. Bio, contagem de seguidores e conteúdo específico do Instagram não puderam ser extraídos — dados de tom/hook vêm do TikTok sob o mesmo handle, tratados como indício fraco.

### @christiantriad
**Categoria:** creator
**Bio:** "Christian Barbosa - IA, Tech & Saas" — criador do método "A Tríade do Tempo", +2 milhões de pessoas treinadas (não verificado diretamente)
**Engajamento estimado:** alto (~571K seguidores, 901 seguindo, 4.333 posts)
**Limitação:** WebFetch bloqueado. Apenas resumo agregado de bio/seguidores; sem acesso a posts individuais, hooks, CTAs ou frases de tom.

### @oneyaraujo
**Categoria:** creator
**Bio:** "Oney Araújo | Marketing Viral" — criador do curso "Código Viral" (50-62 mil+ alunos), +11 anos de criação de conteúdo
**Estrutura ensinada:** Gancho (3s iniciais) → Benefício → Mostre → CTA (metodologia que ele ensina — não confirmado se é a estrutura literal de seus próprios posts)
**Engajamento estimado:** alto (~2M seguidores, 511 seguindo, 1.273 posts)
**Formato dominante:** reels (negócio central é ensinar Reels virais)
**Top temas:** viralização de Reels, crescimento de seguidores, venda online, curso Código Viral
**Limitação:** WebFetch bloqueado. Hook/CTA exatos de posts reais do Instagram não confirmados.

### @geracaotechs
**Categoria:** ia
**Bio:** "Tecnologia e I.A" / "Tudo sobre IA e mundo tech!" (perfil de Glauton Filho)
**Top temas (indexados, não confirmados como top posts):** ferramentas de IA e tecnologia
**Limitação:** WebFetch bloqueado. Número de seguidores não confirmado (11,2K encontrado é do Threads, não do Instagram — não usado como proxy). Sem hooks, CTAs, estrutura ou tom coletados diretamente do Instagram.

### @amandadinizmkt
**Categoria:** marketing
**Limitação:** WebFetch bloqueado. Busca confirmou apenas a existência da URL e uma conta correspondente no TikTok, mas não bio, seguidores, posts, hooks ou tom do Instagram em si. Forte ambiguidade de homônimos "Amanda Diniz" (lifestyle, beleza, maternidade) — nenhuma confirmada como o perfil de marketing correto. Nenhum dado atribuído.

### @human___academy
**Categoria:** ia
**Bio:** "A Maior Escola de IA para Criativos ⚡️ Aprenda a dirigir tecnologia com criatividade Inscreva-se agora no Workshop AI Videolab"
**CTA padrão:** "Inscreva-se agora no Workshop AI Videolab" (fixo na bio)
**Engajamento estimado:** alto (~260K seguidores, 496 seguindo, 450 posts)
**Top temas:** workshop AI Videolab, criação de vídeo com IA, formação para criativos
**Limitação:** WebFetch bloqueado. Bio/seguidores de snippet agregado possivelmente desatualizado. Sem acesso a posts individuais.

### @geiss11
**Categoria:** creator
**Bio:** "O que você procura está aqui" (Henrique Geiss) — venda de produtos digitais, funis, escala
**Engajamento estimado:** médio (~45K seguidores, 601 seguindo, 83 posts)
**Top temas (inferido):** marketing digital, produtos digitais/PLR, faturamento/escala
**Limitação:** WebFetch bloqueado. Nenhuma legenda/roteiro real acessado.

### @nelmoricalde
**Categoria:** creator
**Bio (indireta):** "Nelmo Ricalde | IA, Negócios & Lucro" — fundador da Zuvora, ex-mercado financeiro, mentor na comunidade "A Nova Inteligência"
**Limitação:** WebFetch bloqueado. Nenhuma contagem de seguidores, post, hook ou CTA localizado — apenas identificação da pessoa via LinkedIn/imprensa.

### @rodrigotadewald
**Categoria:** marketing
**Bio:** "Te ensino a usar todo o potencial da IA" (Rodrigo Soares Tadewald, sócio-fundador Asimov Academy/Asimov Finance, +30.000 alunos)
**Engajamento estimado:** alto (~226K seguidores, 58 seguindo, 101 posts)
**Formato dominante:** misto (reels confirmados por link de reel específico, mas conteúdo não acessível)
**Limitação:** WebFetch bloqueado. Links de reels específicos localizados, mas conteúdo/legenda não acessível.

### @sujeitoprogramador
**Categoria:** ia
**Bio:** "👨🏻‍💻 Programador há + de 12 anos 🔥 + de 45.000 alunos" (Matheus Fraga)
**Engajamento estimado:** alto (~165K seguidores, 6.108 seguindo, 2.996 posts)
**Top temas:** programação (Python, cursos), Inteligência Artificial, formação de alunos
**Limitação:** WebFetch bloqueado. Alto volume de posts sugere forte atividade, mas sem acesso a legendas reais.

### @jonathan_kamargo
**Categoria:** creator
**Limitação:** Identidade/existência do handle exato não confirmada. Múltiplas buscas retornaram apenas homônimos não confirmados (@camargojay, @maknoj, @kamargo___, @mkamargo_, um ciclista venezuelano). WebFetch bloqueado. Nenhum dado atribuído.

### @marianatorre.s
**Categoria:** marketing
**Limitação:** WebSearch confirmou apenas que o handle existe e pertence a alguém chamado "Mariana Torres" — nenhum outro dado coletado. Múltiplos homônimos muito parecidos (@marianatorre, @marianatorresoficial_, @marianatorresbr, entre outros) — confirmação de qual "Mariana Torres" exatamente não foi possível. Nenhum dado atribuído.

### @marketerhub.ai
**Categoria:** marketing
**Bio (tagline):** "Empowering Digital Marketers"
**Top temas (inferido do site oficial):** comunidade/curso de marketing com IA, prompts, templates
**Limitação:** WebFetch bloqueado (Instagram e site oficial). Existência confirmada e vínculo com marketerhub.ai (comunidade paga) e conta espelho no TikTok, mas sem bio completa, seguidores, hooks ou CTAs.

### @marcelaluzzio
**Categoria:** marketing
**Bio:** "🔱 Te faço crescer e vender mais com IA 💎 MBA em IA para negócios digitais (USP) 🔥 Crie e venda seu Infoproduto com IA 👇🏼" (nome: "Marcela Lúzio | Marketing de Conteúdo & I.A")
**Engajamento estimado:** médio-alto (~226K seguidores, 658 seguindo, 964 posts)
**Tom (inferido):** direta, didática, vendedora, orientada a resultado, tecnológica
**Top temas:** marketing de conteúdo com IA, infoprodutos com IA, uso de Claude para produtividade
**Limitação:** WebFetch bloqueado. Dois trechos de texto ("Destrave seus resultados com esses únicos 4 comandos...", "Ative o Claude para trabalhar por você") vêm do Threads vinculado, não confirmados como idênticos ao Instagram.

### @gestordeaudiencia
**Categoria:** marketing
**Bio (indício):** menção a "Galeria de Prompts Prontos" para Claude Code (texto exato não confirmado)
**Top temas (inferido de repositório GitHub vinculado, provável autoria Daniel Feitosa):** Claude Code, automações com IA, prompts prontos, comunidade "Vibe Coding"
**Limitação:** WebFetch bloqueado. Identidade parcialmente inferida via GitHub; nenhum post real do Instagram indexado com texto legível.

### @sebintel
**Categoria:** ia
**Limitação:** WebFetch bloqueado. Apenas existência confirmada (nome "Seb Intel"), com presença espelhada em TikTok/YouTube e reels em datas específicas (5 e 7 de setembro de 2025). Um número de "9 milhões de seguidores" encontrado em única busca não foi corroborado por segunda fonte — descartado por risco de alucinação do resumidor de busca. Nenhum dado de engajamento reportado.

### @avora.ai
**Categoria:** agencia
**Bio:** não localizada com confiança; Facebook associado sugere Belo Horizonte-MG
**Hook:** paradoxo/contraste — "Avora wasn't created just to talk about AI. It was built to turn..." (trecho truncado, legenda em inglês); convite direto — "Siga @avora.ai para conteúdos diários sobre IA na prática!"
**Limitação:** WebFetch bloqueado. Busca só indexou 2 posts/snippets, sem contagem de seguidores/posts ou bio completa.

### @ogabrieeldias
**Categoria:** creator
**Limitação:** Handle exato não confirmado em múltiplas variações de busca. Apenas homônimos claramente diferentes (@ogabrielsa, @gabrielmdias, @gabrielladiassh, @agabrieladiasoficial). Nenhum dado atribuído. Recomenda-se confirmar grafia exata com o Lucas.

### @rodrigobindes
**Categoria:** founder
**Bio:** "Mostro como chegar aos 100k/mês com agência de mkt" (mentor de agências de marketing digital)
**Engajamento estimado:** alto (~278K seguidores, 1.835 posts, 1.482 seguindo)
**Tom (inferido):** mentor, direto, orientado a resultado, prático
**Top temas (parcialmente via LinkedIn/YouTube associados, não confirmado no feed):** escala de agências de marketing digital, branding/posicionamento
**Limitação:** WebFetch bloqueado. Nenhuma legenda exata de post/reel capturada.

### @franklim.gui
**Categoria:** creator
**Bio (destaques):** jornada até R$7M em 3 anos; ensina venda "lowticket" gratuitamente no YouTube
**Engajamento estimado:** médio-alto (~104K seguidores, 58 posts, 489 seguindo)
**Top temas (majoritariamente do YouTube associado, não confirmado no IG):** venda "lowticket", jornada de faturamento, tráfego pago, uso de IA para clonar páginas de vendas
**Limitação:** WebFetch bloqueado. Nenhuma legenda completa do Instagram capturada.

### @gabrielsamp.ai
**Categoria:** ia
**Limitação:** Busca confirmou existência de um perfil TikTok com o handle exato, mas nenhum resultado indexou um perfil de Instagram correspondente. Homônimos "Gabriel Sampaio" (@gabrielsampaaio, @gabrielsamps) têm handles diferentes, não confirmados. Perfil possivelmente novo/pouco indexado ou com atividade concentrada no TikTok. Nenhum dado atribuído.

### @maestrosdaia
**Categoria:** ia
**Bio (indireta):** comunidade "Maestros da IA", IA aplicada a negócios (comunidade paga, curso R$97/mês)
**Formato dominante (inferido):** misto (reels e possivelmente carrossel)
**Top temas (inferido do site institucional):** agentes de IA, automação (WhatsApp/Instagram), cursos/comunidade paga
**Limitação:** WebFetch bloqueado. Número de 72K seguidores/577K curtidas encontrado é do TikTok homônimo, não atribuído ao Instagram. Nenhum print, legenda ou métrica real do Instagram encontrado.

### @brandsdecoded__
**Categoria:** marketing
**Bio:** "BrandsDecoded®️ | AI Content Agency" — "Decodificando o futuro do marketing com AI"
**Estrutura (divulgada como metodologia de produto, não confirmada como padrão de todo post):** 4 "arquétipos" de carrossel — Erro Comum, Tendência, Decodificação de Marca, Mudança de Comportamento
**Engajamento estimado:** alto (~301K seguidores)
**Formato dominante:** carrossel (confiança moderada — marca é centrada em "máquina de carrosséis")
**Top temas:** carrosséis com IA (Claude/Canva/Figma), estratégia de conteúdo, cases de resultado (fundador Leonardo Varrichio)
**Limitação:** WebFetch bloqueado. Dados de seguidores/bio vêm de snippet agregado, não de leitura direta. Nenhum hook/CTA com citação exata de post real confirmado.

### @anatex
**Categoria:** creator
**Bio:** "Especialista em ajudar profissionais a usar inteligência artificial para automatizar seus negócios e aumentar lucro" (nome: "Ana Tex - Inteligência Artificial para Negócios")
**Engajamento estimado:** alto (~716K seguidores, 1.102 seguindo, 1.453 posts)
**Limitação:** WebFetch bloqueado. Ambiguidade de nome com outros perfis "Anatex" (@anatexmagazine, @anatexhome, @anatex.sk etc.) — perfil correto identificado com boa confiança pela categoria, mas sem citação literal de post para tom/hook/CTA.

### @larissagomes.ia
**Categoria:** ia
**Bio:** "💻 Te ensino a criar um negócio enxuto e que vende: você + IA ⚡️ Compartilho o que aplico sobre IA Domine o chatGPT👇🏻"
**Hook confirmado (via TikTok, mesmo handle):** "Peça o chatGPT para analisar o feed do seu instagram 🧠 ANTES DE MAIS NADA... siga @larissagomes.ia para receber mais conteúdos como esse..."
**Estrutura:** conteúdo tipo "prompt pronto para copiar e colar" com etapas numeradas (1️⃣ Elementos Visuais, 2️⃣ Clareza da Mensagem, 3️⃣ Sugestões de Melhorias)
**CTA:** "siga @larissagomes.ia..."; variação de troca: "Comenta ELITE que te mando o link"
**Tom:** didático, direto, prático, motivacional, acessível
**Engajamento estimado:** médio (~15K seguidores, 262 posts)
**Top temas:** análise de perfil do Instagram com ChatGPT, prompts prontos, ensino de ChatGPT aplicado a negócios
**Limitação:** WebFetch bloqueado. Hook citado veio de vídeo republicado no TikTok — confiança razoável, mas não confirmado diretamente no Instagram.

### @thiagozaao
**Categoria:** creator
**Limitação:** Perfil não localizado em nenhuma busca (múltiplas variações testadas). Apenas homônimos parciais de outros "Thiago" (thiagozoinho, thiagosetra, thiagoarzua). WebFetch bloqueado. Possível conta pequena/pouco indexada, privada, grafia diferente, ou inexistente. Nenhum dado atribuído.

### @neuwebstudio
**Categoria:** agencia
**Bio:** "Cinematic Web Design | TikTok 👉 172k+ | 19 Figma Animations | 75% off LAST SALE 👇"
**Engajamento estimado:** médio (~52K seguidores, 168 posts, 100 seguindo)
**Top temas:** web design, animações Figma, parallax scrolling, UX/UI
**Limitação:** WebFetch bloqueado. Conteúdo disponível é majoritariamente do TikTok da mesma marca — não deve ser confundido com o comportamento específico no Instagram.

### @laschuk
**Categoria:** founder
**Bio:** dado insuficiente com confiança (fragmentos conflitantes — "EmailHacker" em uma fonte)
**Engajamento estimado:** médio (~36K seguidores, 200 posts, 61 seguindo)
**Top temas (inferido):** email marketing, "tráfego próprio", marketing digital
**Limitação:** WebFetch bloqueado. Nome completo, bio exata, hooks e tom não confirmados por citação literal.

### @maestroptompts
**Categoria:** ia
**Limitação:** Nenhuma evidência direta e específica encontrada em múltiplas variações de busca. Apenas homônimos não relacionados (@thetruemaestro, @maestro_io) e um produto diferente ("Mestre dos Prompts", domínio distinto, sem vínculo confirmado). Nenhum dado atribuído. Possível conta pequena/recente, privada, ou digitação divergente do handle real.

### @faladantasmkt
**Categoria:** marketing
**Bio:** "Jessica Dantas | Mentora de conteúdo & negócios digitais"
**Engajamento estimado:** médio-alto (~99K seguidores — divergência entre buscas: 88K/99K/108K)
**Tom (inferido):** educativo, direto, motivacional, estratégico
**Top temas (inferido):** marketing de conteúdo, crescimento no Instagram, reels que vendem, mentoria
**Limitação:** WebFetch bloqueado. Existe perfil pessoal homônimo distinto (@faladantas, sem "mkt") — alguns dados biográficos de marcas (Unilever, Tim etc.) podem pertencer ao perfil pessoal, não incluídos como fato confirmado deste perfil.

### @lindsay.ia
**Categoria:** ia
**Identidade confirmada:** Lindsay Gonzales, Fresno CA — consultora certificada em automação com IA, marca "AI Money Hub"
**CTA padrão (via agregadores, não citação literal):** comentar palavra-chave ("SETUP"/"FAST") para receber guia via DM
**Tom (inferido):** prático, didático, orientado a resultado, acessível
**Engajamento estimado:** médio (~45K seguidores "combinados" — possivelmente somando outras redes)
**Top temas:** automação com IA, consultoria/freelancing de IA, ferramentas (Claude, n8n)
**Limitação:** WebFetch bloqueado. Métricas de agregador de terceiros podem incluir outras plataformas. Nenhuma legenda literal coletada.

### @andrevictor.m
**Categoria:** marketing
**Bio (destaques):** primeiro milhão aos 18 anos, Ferrari Portofino de R$3M à vista, 50 países até os 22 anos, saiu da escola aos 16
**Hook:** maioria errando/contraste — "Não conheço ninguém no marketing que..." (título de reel, texto completo não recuperado)
**Tom:** ostentação, aspiracional, direto, confiante
**Formato dominante:** reels
**Engajamento estimado:** alto (~244K seguidores, 286 posts; +17,5K no TikTok espelhado)
**Top temas:** empreendedorismo digital, dropshipping, marketing digital, ostentação/lifestyle
**Limitação:** WebFetch bloqueado. Apenas título de um reel recuperado, sem legenda completa.

### @drisiano
**Categoria:** creator
**Limitação:** Nenhum resultado correspondente ao handle exato em múltiplas queries. Apenas homônimos parciais (@driano, @driso__, @drmiano). WebFetch bloqueado. Nenhum dado atribuído.

### @brun0gpt
**Categoria:** ia
**Bio:** "Bruno Francisco | IA e Marketing" — foco em Marketing e Vendas com IA
**Tom (inferido):** educativo, técnico, comercial, direto
**Engajamento estimado:** alto (~157K seguidores, 171 seguindo, 1.334 posts)
**Limitação:** WebFetch bloqueado. Nenhuma legenda, hook, CTA ou tema de post individual recuperado.

### @maxcarrau.ia
**Categoria:** ia
**Limitação:** Ambiguidade não resolvida entre @maxcarraa (cantor argentino, sem relação com IA), @maxcarrau (sem sufixo .ia), @iawithmax (francês) e um canal YouTube "Max carrau | IA". Um post potencialmente relevante não pôde ser confirmado como pertencente ao handle exato — descartado. Nenhum dado atribuído.

### @noevarner
**Categoria:** creator
**Limitação:** Forte ambiguidade entre @noevarner (handle exato, sem dados específicos), @noevarner.ai (104K seguidores segundo Social Blade — conta mais documentada), @therealnoevarner (7.123 seguidores) e @noevarner3. A pessoa por trás (Noe Varner, empreendedor de automação com IA na Flórida, ex-técnico de futebol universitário, foco em Claude Code) é identificável, mas os números encontrados pertencem majoritariamente a @noevarner.ai, não ao handle exato solicitado. Nenhum dado quantitativo/qualitativo atribuído ao handle exato para evitar misturar contas.

### @yikchanltd
**Categoria:** creator
**Bio:** "Sifu Yik Chan - A.I., eCom, Business and Life Mentor" / "8 Figure eCom Expert & A.I. Coach" — featured em Yahoo Finance & Forbes; DM "AI" para "$10,000/month Passive Income Group"
**Hook (indício, não confirmação plena):** "I've built an AI business mentor. Trained on my framework..." (título de post)
**Engajamento estimado:** médio-alto (~79.000 seguidores, 110 seguindo, 1.296 posts)
**Limitação:** WebFetch bloqueado. Conteúdo de estratégia geral de Instagram vem do Substack pessoal do autor (material didático dele, não amostra real do que publica no perfil) — não usado para preencher hook/CTA/tom. Métricas de um perfil relacionado (@sifuyik, "35k em 30 dias") pertencem a outra conta e foram excluídas.

---

## Perfis Sugeridos pelo Sistema
Não aplicável nesta execução — `config/profiles.json` já tinha perfis ativos configurados (Modo Análise, Passo 2 executado diretamente).

---

## Limitações de Dados

**Bloqueio de rede geral:** WebFetch direto para `instagram.com` retornou `EGRESS_BLOCKED` em 100% das tentativas nos 61 perfis, nesta sessão. Toda a coleta veio de WebSearch (snippets indexados por buscadores, agregadores de terceiros como Heepsy/Social Blade/CreatorDB, e cross-posts em TikTok/Threads/YouTube sob o mesmo handle). Isso impede sistematicamente a leitura de legendas completas de posts, contagens exatas e atualizadas de seguidores/curtidas/comentários, e a confirmação de hooks/CTAs/tom de voz por amostragem representativa — a maioria dos campos qualitativos (hook_modelos, estrutura_tipica, tom_exemplo_frase, tamanho_medio_educativo) ficou marcada "dado insuficiente" para a maior parte dos 61 perfis.

**Perfis não localizados / não confirmáveis (nenhum dado atribuído):** @yikC, @eujoaotorresz, @ai, @amandadinizmkt, @jonathan_kamargo, @ogabrieeldias, @gabrielsamp.ai (só existe no TikTok), @drisiano, @maestroptompts, @thiagozaao, @maxcarrau.ia, @noevarner (handle exato).

**Perfis com ambiguidade resolvida por melhor correspondência (sinalizado por perfil):** @nathanhodgson (usado @nathanhodgson.ai), @gabriel.adamuchi, @eduardocavalcanti, @nikolassasso, @anatex, @faladantasmkt, @marianatorre.s (identidade parcial).

**Possível handle incorreto — requer confirmação do Lucas:** @rafa.grandi (perfil encontrado é pessoal/jurídico, não bate com categoria "marketing").

**Divergências numéricas entre fontes não resolvidas:** @allesinisgalli (8,1K vs. 61,3K seguidores), @faladantasmkt (88K/99K/108K seguidores), @sebintel (9M seguidores citado em única fonte, descartado por falta de corroboração).

**Recomendação para próximas execuções:** considerar habilitar acesso de rede a instagram.com (ou usar uma ferramenta de scraping autorizada) para elevar a taxa de campos preenchidos além de bio/seguidores; sem isso, a análise profunda de hooks/estrutura/CTA (Fase 1 do instagram-content-cloner) permanece estruturalmente limitada pelo bloqueio de egress do ambiente, repetindo o padrão já observado na execução de 2026-09-14.
