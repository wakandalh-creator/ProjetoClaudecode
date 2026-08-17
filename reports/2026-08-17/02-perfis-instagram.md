# Análise de Perfis Instagram — 2026-08-17

## Nota metodológica (leia antes de usar os dados abaixo)

Esta execução processou os **61 perfis ativos** de `config/profiles.json` em 13 lotes de ~5 perfis, via WebSearch (+ tentativas de WebFetch), seguindo o Módulo 2 (`monitor/modules/02-instagram.md`).

**Limitação estrutural crítica do ambiente**: `WebFetch` para `instagram.com` — e para qualquer domínio testado, incluindo controles como `en.wikipedia.org` — retornou `EGRESS_BLOCKED` em 100% das tentativas, em todos os 13 lotes. Isso significa que **nenhum dado veio de acesso direto ao Instagram**; tudo veio de snippets indexados pelo Google via WebSearch, que na maioria dos casos truncam legendas em poucas dezenas de caracteres. Isso limita severamente a profundidade dos dados coletados (poucas legendas completas, praticamente nenhuma métrica real de curtidas/comentários/visualizações).

Conforme a regra do módulo, **nenhum dado foi inventado**: onde a busca não retornou informação real e verificável, os campos foram deixados vazios/nulos e a limitação foi documentada.

**Problemas de qualidade da lista de perfis identificados nesta execução** (recomenda-se revisar `config/profiles.json`):
- **Handles não localizados** (nenhum perfil correspondente encontrado): `@yikC`, `@eujoaotorresz`, `@nikolassfaria`, `@humam__academy`, `@jonathan_kamargo`, `@ogabrieeldias`, `@maestroptompts`, `@lindsay.ia`, `@thiagozaao`, `@drisiano`, `@maxcarrau.ia`.
- **Handles prováveis incorretos** (perfil real existe sob variação do handle): `@viverdeia` → provavelmente `@viverdeia.ai`; `@brandsdecoded` → provavelmente `@brandsdecoded__`; `@noevarner` → conteúdo relevante está em `@noevarner.ai`; `@yikchan` → possivelmente `@yikchanltd` (mas em inglês/mercado internacional); `@nathanhodgson` → possivelmente `@nathanhodgson.ai`.
- **Perfis fora do nicho ou ambíguos**: `@rafa.grandi` (conta pessoal de analista jurídico, sem relação com IA/marketing), `@opensession.co` (agência de design/branding nos EUA, não BR), `@neuwebstudio` (estúdio de web design, não IA/marketing), `@eduardocavalcanti` (múltiplas pessoas com esse nome, não confirmado), `@rodrigotadewald` (conta pessoal, conteúdo de IA está em perfil institucional separado `@asimov.academy`).
- **Perfis de audiência internacional/inglês**, fora do escopo "brasileiro" do relatório mas mantidos no config: `@charliehills`, `@chase.h.ai`, `@noevarner` (via `.ai`).

---

## Visão Geral dos Perfis

| Perfil | Categoria | Formato Dominante | Engajamento | Status dos Dados |
|--------|-----------|--------------------|-------------|-------------------|
| @charliehills | creator | misto | médio | Parcial — criador BR? Não, é britânico/inglês |
| @yikC | creator | — | baixo/desconhecido | Não localizado |
| @eujoaotorresz | creator | — | baixo/desconhecido | Não confirmado |
| @fabianocarvalhojr | founder | misto | baixo/desconhecido | Parcial — real, nicho correto |
| @rafa.grandi | marketing | — | baixo/desconhecido | Fora do nicho |
| @brusantanna.ai | ia | misto | baixo/desconhecido | Muito parcial (1 post) |
| @vendedorglobal | negocio-digital | misto | baixo/desconhecido | Muito parcial |
| @oluizmain | creator | reels | baixo/desconhecido | Parcial |
| @nick_saraev | automacao | reels | baixo/desconhecido | Parcial |
| @nathanhodgson | ia | misto | baixo/desconhecido | Handle ambíguo |
| @ai | ia | — | baixo/desconhecido | Não localizado |
| @ana.gsoares | marketing | — | baixo/desconhecido | Só bio confirmada |
| @chase.h.ai | ia | reels | alto (indício indireto) | Parcial — conteúdo em inglês |
| @leosoares.ia | ia | reels | baixo/desconhecido | Parcial (só CTA) |
| @gabriel.adamuchi | creator | reels | baixo/desconhecido | Muito parcial |
| @viverdeia | ia | desconhecido | baixo/desconhecido | Handle provavelmente incorreto |
| @ninja.automacoes | automacao | desconhecido | baixo/desconhecido | Muito parcial |
| @nikolassfaria | creator | — | baixo/desconhecido | Não localizado |
| @eduardocavalcanti | founder | — | baixo/desconhecido | Ambíguo |
| @jonylan | creator | reels | baixo/desconhecido | Parcial — real, nicho correto |
| @allesinisgalli | founder | reels | baixo | Muito parcial |
| @lonamkt | marketing | misto | baixo/desconhecido | Quase sem atividade no IG |
| @gabrielbarbosa.oficial | creator | misto | baixo/desconhecido | Muito parcial |
| @opensession.co | agencia | misto | baixo/desconhecido | Fora do nicho (EUA) |
| @leandroladeiran | marketing | misto | alto | Parcial — maior perfil da amostra |
| @christiantriad | creator | reels | médio | Parcial — real, nicho correto |
| @oneyaraujo | creator | reels | médio | Parcial — nicho adjacente (growth) |
| @geracaotechs | ia | reels | baixo/desconhecido | Parcial |
| @amandadinizmkt | marketing | reels | baixo/desconhecido | Só bio confirmada |
| @humam__academy | ia | — | baixo/desconhecido | Não localizado |
| @geiss11 | creator | misto | baixo/desconhecido | Só bio confirmada |
| @nelmoricalde | creator | misto | baixo/desconhecido | Só bio confirmada |
| @rodrigotadewald | marketing | misto | baixo/desconhecido | Conta pessoal, sem conteúdo |
| @sujeitoprogramador | ia | misto | baixo/desconhecido | Muito parcial |
| @jonathan_kamargo | creator | — | baixo/desconhecido | Não localizado |
| @marianatorre.s | marketing | — | baixo/desconhecido | Só existência confirmada |
| @marketerhub.ai | marketing | desconhecido | baixo/desconhecido | Parcial (site oficial) |
| @marcelaluzzio | marketing | desconhecido | baixo/desconhecido | Só bio confirmada |
| @gestordeaudiencia | marketing | desconhecido | baixo/desconhecido | Parcial — nicho é dev/Claude Code |
| @sebintel | ia | — | baixo/desconhecido | Só existência confirmada |
| @avora.ai | agencia | misto | baixo/desconhecido | Muito parcial |
| @ogabrieeldias | creator | — | baixo/desconhecido | Não localizado |
| @rodrigobindes | founder | misto | baixo/desconhecido | Parcial |
| @franklim.gui | creator | misto | baixo/desconhecido | Parcial (cross-platform) |
| @gabrielsamp.ai | ia | reels | baixo/desconhecido | Muito parcial |
| @maestrosdaia | ia | misto | baixo/desconhecido | Muito parcial |
| @brandsdecoded | marketing | carrossel | alto (indício) | Parcial — handle divergente |
| @anatex | creator | misto | alto (indício) | Parcial — real, grande porte |
| @larissagomes.ia | ia | reels | baixo/desconhecido | Melhor amostra da execução |
| @thiagozaao | creator | — | baixo/desconhecido | Não localizado |
| @neuwebstudio | agencia | misto | baixo/desconhecido | Fora do nicho |
| @laschuk | founder | reels | baixo/desconhecido | Parcial — real, nicho adjacente |
| @maestroptompts | ia | — | baixo/desconhecido | Não localizado |
| @faladantasmkt | marketing | reels | baixo/desconhecido | Só perfil institucional |
| @lindsay.ia | ia | — | baixo/desconhecido | Não localizado |
| @andrevictor.m | marketing | reels | baixo/desconhecido | Parcial (fontes indiretas) |
| @drisiano | creator | — | baixo/desconhecido | Não localizado |
| @brun0gpt | ia | misto | baixo/desconhecido | Parcial (site oficial) |
| @maxcarrau.ia | ia | — | baixo/desconhecido | Não localizado |
| @noevarner | creator | misto | baixo | Handle divergente (`.ai`) |
| @yikchan | creator | — | baixo/desconhecido | Não confirmado |

---

## Análise Detalhada por Perfil

### @charliehills (creator)
**Nicho:** IA/produtividade, mas criador **britânico**, conteúdo majoritariamente em inglês — fora do escopo "brasileiro" do relatório.
**Seguidores/posts (não verificado diretamente):** ~88K / 260 posts.
**Hooks:** maioria_errando ("Most people treat AI like a search engine. They type a sentence and pray for a miracle."); transformação_silenciosa ("People see the follower count. They don't see the timeline behind it."); fenômeno_nomeado ("We're so cooked. Nano Banana 2 dropped today...").
**Estrutura:** contraposição direta → explicação prática de ferramenta/método de IA → oferta de recurso gratuito.
**CTA:** link na bio para "100+ free AI prompts, guides & tools".
**Tom:** direto, didático, confiante, pessoal/confessional. Ex.: "Don't prompt harder. Switch smarter."
**Temas:** prompts/ferramentas de IA, produtividade, bastidores de crescimento, storytelling de carreira.
**Limitação:** frases vêm de Substack Notes do mesmo autor, não confirmadas como idênticas no IG; métricas de curtidas vêm de blog terceiro não verificável.

### @yikC (creator)
**Não localizado.** Buscas retornaram apenas contas não relacionadas (YWCA Kids Club, Yik Yak app). Nenhum dado coletado.

### @eujoaotorresz (creator)
**Não confirmado.** Único achado parecido (`@joaotorresz`, Portugal, 5 posts) sem garantia de ser o mesmo perfil. Nenhum dado atribuído.

### @fabianocarvalhojr (founder)
**Nicho confirmado:** fundador da lasy.ai, "Crio Agentes de IA que vendem e operam Negócios 24/7". ~130K seguidores, 1.417 posts.
**Hooks:** paradoxo_contraste ("Entre 2 MILHÕES de startups de IA de todos os segmentos..."); outro ("Marketing, Automação e IA | Nos anos 90, pouca gente sabia..."; "Qual IA você tem mais utilizado por ai? Quero saber!").
**Estrutura:** mistura conteúdo institucional sobre IA/automação empresarial com posts de bastidores/parceria e engajamento direto (perguntas à audiência).
**CTA:** pergunta direta pedindo interação nos comentários.
**Tom:** institucional, direto, educativo, entusiasta (emojis 🚀).
**Temas:** agentes de IA para negócios, automação empresarial, consultoria (Atrium Contábil), eventos (Amcham, Hub de IA).
**Limitação:** amostra de apenas 7 posts (de 1.417 totais) via snippets truncados — frequências são estimativas de baixa confiança.

### @rafa.grandi (marketing)
**Fora do nicho.** Confirmado como conta pessoal real (Rafael Grandi Borges, 247 seguidores, 36 posts) — bio "Analista Jurídico SPGG/RS e Pai do Cássio". Sem relação com IA/marketing. Nenhum dado extraído.

### @brusantanna.ai (ia)
**Nicho confirmado** ("Bruna Santanna | Estrategista de IA").
**Hook (único, origem TikTok, não confirmado no IG):** "Analisei meu próprio conteúdo com duas IAs e descobri exatamente por que alguns vídeos viralizavam e outros não. Agora são 300 seguidores novos por dia."
**CTA:** comentar palavra-chave para receber guia via DM.
**Tom:** pessoal, direto, didático, orientado a resultado.
**Temas:** IA aplicada a análise de conteúdo, growth, mentoria (Potenc.IA Bradesco/Prosper Sprints).
**Limitação:** apenas 1 post real localizado, sem confirmação de que foi replicado no Instagram.

### @vendedorglobal (negocio-digital)
**Nicho confirmado** (Murilo Bevervanso, e-commerce/Shopee). ~83K seguidores, ~2.280 posts (não verificado diretamente).
**Hook (único):** paradoxo_contraste — "Você não precisa de dropshipping para vender na Shopee...".
**Temas:** e-commerce em marketplaces, afiliados, cursos/mentoria.
**Limitação:** CTA, engajamento e formato dominante não confirmados; apenas 1 legenda parcial encontrada.

### @oluizmain (creator)
**Nicho confirmado** ("Luiz Main", "Creator Mobile & IA"). ~215K seguidores, 191 posts.
**Hooks:** paradoxo_contraste ("Nunca foi sorte. #videomakermobile"); outro ("📲 Faço meus trabalhos inteiramente com o meu [celular]").
**Tom:** motivacional, direto, aspiracional, bastidor/processo.
**Temas:** produção de vídeo com celular, "clonagem de autoridade", curso Mobile Pro.
**Limitação:** apenas 2 fragmentos curtos de legendas; sem CTA ou engajamento confirmados.

### @nick_saraev (automacao)
**Nicho confirmado** — referência internacional em AI automation/agências.
**Hooks:** outro (apresentação de credencial: "writer, entrepreneur, and AI/automation..."); maioria_errando ("Wondering how to launch an AI automation...").
**CTA:** comentar palavra-chave (ex.: "AUTOMATION", "EMAIL") para receber material via DM.
**Tom:** educacional, direto, confiante, orientado a negócios.
**Temas:** agências de automação (n8n, Make.com), primeiro cliente, Maker School, sistema "N8N Instagram Parasite".
**Limitação:** seguidores divergentes entre fontes (400K–550K, não confirmado); 3-4 legendas parciais apenas.

### @nathanhodgson (ia)
**Handle ambíguo.** O handle exato "@nathanhodgson" não foi confirmado — variantes encontradas: `@nathanhodgson.ai` (128K seguidores, "Built a 6-Figure Business Powered By AI", mais alinhado ao nicho), `@nathanhodgson_` (3K seguidores, 0 posts), `@nathanjameshodgson` (eletricista, sem relação). Nenhum dado de conteúdo confiável coletado.

### @ai (ia)
**Não localizado.** Nenhuma bio, seguidores ou conteúdo encontrado. Indício não confirmado: pode ser handle "OG" de 2 letras (colecionador), não necessariamente perfil de conteúdo ativo.

### @ana.gsoares (marketing)
Confirmado (Ana G Soares, ~146K seguidores, 2.840 posts, CEO @uniagiloficial, podcast Agilize-se). **Temas:** carreira ágil, certificação LACP, imersão "IA Architect". **Limitação:** nenhuma legenda real ou CTA verbatim encontrado — só bio/posicionamento.

### @chase.h.ai (ia)
**Nicho de IA confirmado, mas conteúdo majoritariamente em inglês/audiência global**, não brasileira. ~221K seguidores, 751 posts.
**Hook:** fenômeno_nomeado — reel viral sobre a skill "Ponytail" para Claude Code (via cobertura de terceiros: Hacker News, Reddit, projeto citado atingiu ~40-44 mil estrelas no GitHub).
**CTA:** "DM 'Ready' to Apply For 1:1 Mentorship" (bio).
**Tom:** direto, hype/grandiloquente, técnico-educativo.
**Temas:** Claude Code, "hacks" de IA, mentoria 1:1 (~175 mil alunos reivindicados).
**Limitação:** hook veio de reportagem de terceiros, não de transcrição direta; sem curtidas/comentários confirmados.

### @leosoares.ia (ia)
Confirmado — CEO da Acelera IA, 219K seguidores, 2.226 posts.
**CTA (fragmentos reais, truncados):** "Comenta 'ACELERA IA'..." (em ≥3 reels); "Comenta 'IA7'".
**Tom:** comercial, direto, educativo-vendedor, assertivo.
**Temas:** IA para negócios, imersão "Lançamento Pago com IA", funil comentário+DM.
**Limitação:** nenhuma transcrição completa de vídeo; hook de abertura não classificável.

### @gabriel.adamuchi (creator)
Perfil "IA Fácil". Único conteúdo real localizado foi um prompt de Natal republicado por terceiros no Threads (formato "Prompt:" + texto em inglês).
**Tom:** prático, acessível, direto, humorístico.
**Temas:** prompts de IA generativa, tutoriais "IA Fácil".
**Limitação:** sem seguidores/posts do IG confirmados (só do TikTok, plataforma diferente); conteúdo veio de repost de terceiro, não confirmado como idêntico ao original.

### @viverdeia (ia)
**Handle provavelmente incorreto** — o perfil real da educação/aceleração de empresas com IA (Rafael Milagre) parece ser `@viverdeia.ai`.
**Hook:** paradoxo_contraste — "Do 0 a 100 milhões com IA em 18 meses".
**Temas:** educação sobre IA para empresas, estudos de caso de crescimento.
**Limitação:** seguidores inconsistentes entre buscas (116K vs 129K); nenhuma transcrição verbatim de post.

### @ninja.automacoes (automacao)
Confirmado como real ("Automação e IA — Matheus Pessoa"), mas risco de confusão com perfil parecido `@ninja_automacoes` (underscore). Nenhuma legenda/CTA atribuível com segurança encontrada.

### @nikolassfaria (creator)
**Não localizado.** Nenhuma variação de busca (incluindo "Nikolas Faria") retornou correspondência.

### @eduardocavalcanti (founder)
**Ambíguo.** Perfil existe mas múltiplas pessoas homônimas indexadas (professor de física, CEO Fundamentei/mercado financeiro). Não confirmado se pertence ao nicho pesquisado.

### @jonylan (creator)
Confirmado — "Jony Lan | Marketing Digital, Vendas e IA" ("O Ninja da Internet"), ~306K seguidores, 3.255 posts. Bio: "Inteligência Artificial Ninja da internet desde 1994".
**Tom:** direto, autoridade, didático, comercial/vendedor.
**Temas:** IA em marketing/vendas, ferramentas (Perplexity), cases com +7.500 empresas, palestras/treinamentos.
**Limitação:** nenhuma legenda completa recuperada, apenas títulos truncados.

### @allesinisgalli (founder)
Confirmado ("Allessandra Sinisgalli — AI & MARKETING / IA CLUB"). **Hook (único):** lançamento de comunidade paga "IA CLUB".
**Limitação:** seguidores conflitantes entre fontes (8.155 vs 61,3K via Heepsy, taxa de engajamento 0,45% considerada baixa).

### @lonamkt (marketing)
Felipe Lona — perfil **pouco ativo no Instagram** (~2 posts, 4.316 seguidores); conteúdo concentrado no YouTube. Amostra insuficiente para caracterizar hooks/CTA/engajamento.

### @gabrielbarbosa.oficial (creator)
Confirmado ("Gabriel Barbosa | Negócios Digitais", 7.782 seguidores, 47 posts). **Hook único:** bio "+10MM faturados na internet". **Temas:** negócios digitais, lifestyle de empreendedor.

### @opensession.co (agencia)
**Fora do nicho.** Agência de design/branding sediada em San Diego, EUA, conteúdo majoritariamente em inglês, foco em UX/design systems — não marketing digital/automação/IA para empreendedores BR. 23K seguidores.

### @leandroladeiran (marketing)
**Maior perfil da amostra** (estimativas entre 1,8M–2M+ seguidores, não confirmado com exatidão).
**Hook (origem TikTok, não confirmado no IG):** maioria_errando — "Quem não sabe COPYWRITING dançou… Meu gingado te influenciou a me seguir, afinal?".
**Estrutura (inferida de material de curso):** framework "Promise Marketing vs. Premise Marketing" + "O Antagonista" (criar vilão/crença errada no início).
**Tom:** bem-humorado, irreverente, direto, provocador, autoconfiante.
**Temas:** copywriting (Light Copy), Stories 10x, método VTSD (Venda Todo Santo Dia).

### @christiantriad (creator)
Confirmado — "Christian Barbosa - IA, Tech & Saas", criador da "Tríade do Tempo".
**Hooks:** fenômeno_nomeado ("O Google acaba de..."); paradoxo_contraste ("Extremamente preciso! 🤯 Você confiaria..."); outro ("❌ DESCONFIE TODA VEZ QUE VOCÊ...").
**CTA:** comentar/digitar palavra-chave (ex.: "OMAT", "EU QUERO") para receber material.
**Tom:** direto, provocador, confiante, didático, urgente.
**Temas:** novidades de IA, produtividade/gestão do tempo, ceticismo sobre IA.
**Limitação:** seguidores inconsistentes (571K vs 349K entre fontes).

### @oneyaraujo (creator)
Nicho adjacente (growth/viralização, não IA/automação puro). "Oney Araújo | Marketing Viral".
**Hooks:** fenômeno_nomeado ("O Instagram não é mais uma rede social..."; "Essa I.A faz os cortes...").
**CTA:** link na bio para curso pago "Código Viral".
**Tom:** didático, vendedor, urgente, acessível, entusiasmado.
**Temas:** viralização no Instagram, ferramentas de IA para edição de vídeo, algoritmo.
**Limitação:** ~2M seguidores não verificado em fonte primária; hooks são cross-posts do TikTok.

### @geracaotechs (ia)
"Tecnologia e I.A" (Glauton Filho) — curadoria de ferramentas de IA.
**Hooks:** fenômeno_nomeado ("Esse site te permite criar jogos só descrevendo sua ideia..."); outro ("Qual das 2 IAs você...").
**Temas:** IA generativa (imagem, jogos, vídeo), comparação entre IAs.
**Limitação:** maior parte dos dados vem do Threads/Pinterest, não do Instagram diretamente.

### @amandadinizmkt (marketing)
Bio confirma nicho ("IA para Empreendedoras"), mas **nenhum conteúdo de post localizado** — buscas retornaram majoritariamente homônima não relacionada (Amanda Diniz, beleza).

### @humam__academy (ia)
**Handle provavelmente incorreto.** Não localizado; candidato mais próximo: `@human___academy` (3 underscores, ~260K seguidores, "A Maior Escola de IA para Criativos").

### @geiss11 (creator)
Confirmado (Henrique Geiss, ~45K seguidores, 83 posts, venda de infoprodutos internacionais) — nicho adjacente, sem evidência de conteúdo educativo de IA/automação. Nenhuma legenda real encontrada.

### @nelmoricalde (creator)
Confirmado ("IA, Negócios & Lucro"; ligado à agência Zuvora). Nenhuma legenda/reel real localizado.

### @rodrigotadewald (marketing)
CEO/cofundador Asimov Finance/Academy — parece conta pessoal, sem conteúdo ativo. Os reels de IA encontrados pertencem ao perfil institucional separado `@asimov.academy`, não a este.

### @sujeitoprogramador (ia)
Confirmado (Matheus Fraga, ~168K seguidores, 3.040 posts, programação + IA). Apenas 1 título de reel truncado ("IA dentro do seu VSCode para ajudar na...") — insuficiente para hooks/CTA.

### @jonathan_kamargo (creator)
**Não localizado.** Nenhuma variação de grafia retornou correspondência.

### @marianatorre.s (marketing)
Só a existência da URL foi confirmada (indexada como "Mariana Torres"). Nenhuma bio, seguidores ou conteúdo encontrado.

### @marketerhub.ai (marketing)
Bio confirmada ("Empowering Digital Marketers") e proposta de valor do site oficial (comunidade de marketing com IA, "AI theme pages"). Nenhuma legenda/CTA verbatim do Instagram encontrada.

### @marcelaluzzio (marketing)
Bio confirmada ("Marketing de Conteúdo & I.A", MBA em IA pela USP). Seguidores (226K) não verificados — vieram de resumo automático de busca. Nenhuma legenda real encontrada.

### @gestordeaudiencia (marketing)
Perfil mais alinhado a IA/dev (uso do Claude Code) do que marketing digital tradicional. Repositório GitHub associado encontrado. Nenhuma legenda/CTA/engajamento real do Instagram encontrado.

### @sebintel (ia)
Apenas existência do handle confirmada em múltiplas plataformas — sem bio, seguidores, ou qualquer evidência do nicho.

### @avora.ai (agencia)
Confirmado no nicho de IA ("conteúdos diários sobre IA na prática").
**Hook único:** "Avora wasn't created just to talk about AI. It was built to turn...".
**CTA:** "Siga @avora.ai para conteúdos diários sobre IA na prática!"
**Limitação:** apenas 2 posts indexados; ambiguidade com contas correlatas (@avora_br_, @avora.oficial).

### @ogabrieeldias (creator)
**Não localizado.** Buscas redirecionaram para contas diferentes (@ogabrielsa, colunista de esporte; @igabidias, perfil pessoal não relacionado).

### @rodrigobindes (founder)
Confirmado ("Mentor de Agências de Marketing Digital", 278K seguidores, ligado à Ultralize).
**Hooks:** paradoxo_contraste ("De 'Eugência' a Agência de 100k/mês..."); outro ("Oceano Azul das Agências 2.0...").
**Temas:** escalar agências, sair do operacional, workshops presenciais.
**Limitação:** apenas 2 títulos de posts encontrados.

### @franklim.gui (creator)
Confirmado (46K seguidores, 159 posts; bio: cursos sobre IA/Claude Code e low-ticket).
**Hooks:** fenômeno_nomeado ("Entre 90 mil skills do Claude Code essas 10 são lendárias"); paradoxo_contraste ("não da mais pra rodar lowticket no brasil").
**Limitação:** exemplos vieram do YouTube do mesmo criador, não confirmados como posts do Instagram.

### @gabrielsamp.ai (ia)
**Hooks (2 títulos de reels):** "Conecte o Instagram ao Claude e Automatize suas Análises"; "Olha só essa automação no n8n que o claude 4 sonet criou".
**Temas:** automação com Claude/n8n, integração Instagram+IA.
**Limitação:** sem bio, nome de exibição ou seguidores confirmados; amostra mínima (2 títulos).

### @maestrosdaia (ia)
Ligado à comunidade paga "Maestros da IA" (R$97/mês). **Hook único (origem TikTok):** "O agente de IA que trabalha enquanto você dorme". Seguidores só confirmados no TikTok (71,4K), não no IG.

### @brandsdecoded (marketing)
**Handle divergente** — perfil ativo real é `@brandsdecoded__` (2 underscores), 301K seguidores, Leonardo Varrichio, "Decodificando o futuro do marketing com AI".
**Hooks:** fenômeno_nomeado ("Um novo tipo de conteúdo tem ganhado força no Instagram..."); outro ("Esse carrossel foi feito no Claude.").
**Temas:** carrosséis com IA, método "Content Machine 3.0".
**Engajamento "alto"** é inferência do porte da conta, não métrica real.

### @anatex (creator)
Confirmado — "Ana Tex - Inteligência Artificial para Negócios", 705K seguidores, 1.411 posts.
**Hooks:** paradoxo_contraste ("A IA não transforma empresas sozinha; ela muda a lógica..."); fenômeno_nomeado ("Empresas que integram IA, dados e automação lideram o..."); transformação_silenciosa ("A automação com inteligência artificial deixou de ser uma...").
**Tom:** institucional, consultivo, assertivo, corporativo.
**Temas:** IA corporativa, automação e dados, consultoria (parceria @atriumcontab).
**Limitação:** todas as legendas encontradas vieram truncadas; engajamento "alto" é estimativa pelo porte, não métrica real.

### @larissagomes.ia (ia)
**Melhor amostra de dados desta execução** — cross-posts no TikTok/Threads reproduziram legenda completa de ao menos 1 post.
**Hooks:** outro ("Peça o chatGPT para analisar o feed do seu instagram"); maioria_errando ("Você quer crescer no Instagram, mas quase nunca para pra analisar o próprio perfil").
**Estrutura:** hook de dor comum → promessa de solução via prompt pronto → entrega do prompt em etapas numeradas → CTA de seguir logo no início → fechamento com CTA de salvar + hashtags.
**CTA:** "siga @larissagomes.ia..."; "📩 Salva pra lembrar de analisar o seu perfil!"
**Tom:** prático, didático, acessível, urgente (emojis/maiúsculas).
**Tamanho médio educativo:** ~180 palavras (estimativa de 1 único post completo, não amostra representativa).
**Temas:** prompts de ChatGPT para Instagram, crescimento com IA, mentoria com +1.500 alunos.

### @thiagozaao (creator)
**Não localizado.** Nenhuma variação de busca retornou correspondência.

### @neuwebstudio (agencia)
**Fora do nicho.** Agência de web design/animações Figma, conteúdo majoritariamente em inglês, forte presença no TikTok (172K+) em vez do Instagram (52K seguidores).

### @laschuk (founder)
Confirmado — Guilherme Laschuk, email marketing/"emailhacker", 36K seguidores, 200 posts.
**Hooks:** maioria_errando ("Todo dia vejo gente..."); transformação_silenciosa ("Quando comecei com..."); outro ("copie daqui 👇 antes de..."; "5 modelos aqui 👇"); paradoxo_contraste ("nunca consegui vender...").
**CTA:** convite para copiar/usar modelo ou template.
**Tom:** direto, prático, confessional, vendedor, informal.
**Temas:** email marketing, ActiveCampaign, modelos/templates, tráfego próprio.
**Limitação:** ~8 títulos de reels indexados, todos truncados — nenhum texto completo lido.

### @maestroptompts (ia)
**Não localizado** (possível erro de digitação no handle, ex. letras trocadas em "prompts").

### @faladantasmkt (marketing)
Confirmado (Jessica Dantas, ~99-108K seguidores, 1.774 posts, mentoria de conteúdo/reels). Nenhuma legenda de post individual encontrada — apenas páginas institucionais.

### @lindsay.ia (ia)
**Não localizado.** Buscas retornaram apenas "Lindsay" associadas ao estado americano de Iowa (abreviação "IA" em inglês), não ao nicho de IA em português.

### @andrevictor.m (marketing)
**Hooks (fontes indiretas — podcasts/marketplaces de curso):** paradoxo_contraste ("Fiz meu Primeiro Milhão aos 18 anos desse Jeito.."); transformação_silenciosa ("Ainda bem que eu não desisti quando a...").
**Tom:** ousado, motivacional, ostentoso, direto.
**Temas:** dropshipping, mentoria individual, ostentação financeira.
**Limitação:** nenhuma legenda confirmada diretamente de post do Instagram.

### @drisiano (creator)
**Não localizado.**

### @brun0gpt (ia)
Confirmado (157K seguidores, 1.334 posts; cursos "Impulso"/"GPT").
**Hook:** maioria_errando — "Cansado de usar IA de forma amadora?".
**Estrutura (segundo método vendido pelo próprio criador):** Gancho → História → Oferta.
**Temas:** IA aplicada a marketing/vendas, ChatGPT, growth de Instagram.
**Limitação:** estrutura inferida do material educacional vendido, não de amostragem real de posts.

### @maxcarrau.ia (ia)
**Não confirmado.** Contas parecidas mas distintas: @maxcarrau (sem dados), @maxcarraa (cantor argentino), @iawithmax (IA em francês).

### @noevarner (creator)
**Handle divergente** — conteúdo relevante está em `@noevarner.ai` (~92-104K seguidores), não em `@noevarner` (conta pequena/genérica). Conteúdo em inglês, mercado americano/Flórida — fora do nicho brasileiro.
**Hooks (de @noevarner.ai):** outro ("Want real automation examples? Join our free Skool community."); fenômeno_nomeado ("In my DIGITAL BAG… 💰 LITERALLY 💻 I launched my Skool...").
**CTA:** convite recorrente para comunidade Skool gratuita, funil para "NoeAI Premium" (US$97/mês).
**Engajamento:** baixo (0,45% via Social Blade — ~278 curtidas/135 comentários médios, não contagem direta).

### @yikchan (creator)
**Não confirmado.** Handle mais próximo encontrado (`@yikchanltd`, "Sifu Yik Chan") é em inglês, mercado internacional de e-commerce/IA — não confirmado como o mesmo perfil nem alinhado ao nicho BR.

---

## Perfis Sugeridos pelo Sistema

Não aplicável nesta execução — `config/profiles.json` já tinha 61 perfis ativos, então o Módulo 2 foi direto para o Passo 2 (Modo Análise), pulando o modo descoberta.

---

## Limitações de Dados (resumo consolidado)

1. **WebFetch bloqueado (`EGRESS_BLOCKED`) para todos os domínios testados neste ambiente**, incluindo instagram.com e sites terceiros (blogs, espelhos como Picuki/gramhir, e até en.wikipedia.org como controle). Toda a coleta desta execução veio exclusivamente de snippets indexados via WebSearch (Google), que na maioria das vezes truncam legendas — isso é a causa raiz da maioria das lacunas abaixo, não falta de esforço de busca.
2. **Nenhuma métrica real de curtidas, comentários ou visualizações** foi obtida para nenhum dos 61 perfis — todos os campos `engajamento_estimado` são inferências fracas baseadas em porte de conta/indícios indiretos, nunca dados diretos.
3. **11 handles não foram localizados de forma alguma**: @yikC, @eujoaotorresz, @nikolassfaria, @humam__academy, @jonathan_kamargo, @ogabrieeldias, @maestroptompts, @lindsay.ia, @thiagozaao, @drisiano, @maxcarrau.ia.
4. **5 handles parecem incorretos** (perfil real existe sob variação): @viverdeia (→ @viverdeia.ai), @brandsdecoded (→ @brandsdecoded__), @noevarner (conteúdo relevante em @noevarner.ai), @nathanhodgson (possível @nathanhodgson.ai), @yikchan (possível @yikchanltd, mas fora do nicho).
5. **5 perfis confirmados como fora do nicho de IA/automação/marketing digital brasileiro**: @rafa.grandi (pessoal/jurídico), @opensession.co (design/branding EUA), @neuwebstudio (web design EUA/TikTok), @eduardocavalcanti (ambíguo entre homônimos), @rodrigotadewald (conta pessoal sem conteúdo, IA está em perfil institucional separado).
6. **Vários perfis com nicho correto mas amostra mínima** (1-3 fragmentos truncados de posts) — os campos de `hook_modelos`, `estrutura_tipica` e `cta_padrao` desses perfis devem ser tratados como indícios de baixa confiança, não como caracterização completa do padrão de conteúdo.
7. **Recomendação:** revisar e corrigir os handles sinalizados nos itens 3 e 4 em `config/profiles.json`, e decidir se os perfis do item 5 devem ser removidos da lista de monitoramento por não corresponderem ao nicho.
