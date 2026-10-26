# Análise de Perfis Instagram — 2026-10-26

## ⚠️ Achado Operacional (leia antes do resto do relatório)

Esta execução (Módulo 2, modo análise, 61 perfis ativos em `config/profiles.json`) rodou em um ambiente onde:

1. **`WebFetch` em qualquer URL `instagram.com` falha com erro de DNS** (`getaddrinfo ENOTFOUND www.instagram.com`) — confirmado repetidamente em todos os 12 lotes processados. Não é o bloqueio usual de scraping do Instagram: é o domínio inteiro inacessível a partir desta sessão/proxy de saída. Nenhum metadado de página (bio, contagem de seguidores) pôde ser obtido por essa via.
2. **`WebSearch` não indexa o conteúdo de posts** da grande maioria dos 61 perfis monitorados — são contas pequenas/de nicho (criadores BR de IA, automação e marketing digital), e os motores de busca usados não retornam páginas de posts individuais do Instagram para esses handles. Na maioria das buscas, os resultados foram apenas contas homônimas não relacionadas ou conteúdo genérico sobre o nicho.

**Resultado:** não foi possível coletar hooks, estrutura de posts, CTAs, tom de voz ou engajamento real para **48 dos 61 perfis** (nenhum dado, nem indireto). Para outros **13 perfis** foi encontrado apenas algum indício indireto e **não confirmado** (estimativas de seguidores/nicho via agregadores de terceiros como CreatorDB, Favikon, Heepsy, Reportei) — explicitamente marcado como não-oficial em cada caso, e **nenhum hook/CTA/frase foi inventado** para preencher essas lacunas, conforme a regra do módulo.

**Recomendação para o Lucas:** se o monitoramento de Instagram for prioritário, vale considerar (a) liberar `instagram.com` no proxy de saída do ambiente, (b) usar uma API oficial (Meta Graph API / Instagram Basic Display) ou um serviço de terceiros autorizado para coleta, já que busca textual indexada claramente não é suficiente para perfis pequenos/nicho.

---

## Visão Geral dos Perfis

| # | Perfil | Categoria | Dado real encontrado? | Observação |
|---|--------|-----------|------------------------|------------|
| 1 | @charliehills | creator | Não | Nenhum resultado correspondente |
| 2 | @yikC | creator | Não | Nenhum resultado correspondente |
| 3 | @eujoaotorresz | creator | Não | Nenhum resultado correspondente |
| 4 | @fabianocarvalhojr | founder | Não | Nenhum resultado correspondente |
| 5 | @rafa.grandi | marketing | Não | Nenhum resultado correspondente |
| 6 | @brusantanna.ai | ia | Não | Nenhum resultado correspondente |
| 7 | @vendedorglobal | negocio-digital | Não | Nenhum resultado correspondente |
| 8 | @oluizmain | creator | Não | Nenhum resultado correspondente |
| 9 | @nick_saraev | automacao | Indireto (não confirmado) | Agregadores sugerem 100k–693k seguidores (estimativas divergentes); nicho automação/IA |
| 10 | @nathanhodgson | ia | Indireto (não confirmado) | Agregadores sugerem ~142–146k seguidores; nicho tutoriais de IA |
| 11 | @ai | ia | Não | Nenhum resultado correspondente |
| 12 | @ana.gsoares | marketing | Não | Nenhum resultado correspondente |
| 13 | @chase.h.ai | ia | Não | Nenhum resultado correspondente |
| 14 | @leosoares.ia | ia | Não | Nenhum resultado correspondente |
| 15 | @gabriel.adamuchi | creator | Indireto (não confirmado) | Página Gumroad homônima sugere nicho de marketing digital/IA |
| 16 | @viverdeia.ai | ia | Não | Nenhum resultado correspondente |
| 17 | @ninja.automacoes | automacao | Não | Nenhum resultado correspondente |
| 18 | @nikolassasso | creator | Indireto (não confirmado) | CreatorDB: ~181k seguidores, nicho marketing digital/infoprodutos — texto da fonte suspeito de ser template |
| 19 | @eduardocavalcanti | founder | Não | Menor cobertura de busca entre todos os perfis |
| 20 | @jonylan | creator | Indireto (não confirmado) | CreatorDB: ~346k seguidores — mesma fonte/template suspeito do item 18 |
| 21 | @allesinisgalli | founder | Não | Nenhum resultado correspondente |
| 22 | @lonamkt | marketing | Não | Nenhum resultado correspondente |
| 23 | @gabrielbarbosa.oficial | creator | Não | Só homônimo (jogador "Gabigol"), sem confirmação |
| 24 | @opensession.co | agencia | Não | Nenhum resultado correspondente |
| 25 | @leandroladeiran | marketing | Indireto (não confirmado) | Possível confusão com "Leandro Ladeira" (grafia diferente) ou agregador ~3,2M seguidores |
| 26 | @christiantriad | creator | Não | Nenhum resultado correspondente |
| 27 | @oneyaraujo | creator | Indireto (não confirmado) | Possível "Oney Araújo", ex-YouTuber, curso "Código Viral®" — vínculo não confirmado |
| 28 | @geracaotechs | ia | Não | Nenhum resultado correspondente |
| 29 | @amandadinizmkt | marketing | Não | Nenhum resultado correspondente |
| 30 | @human___academy | ia | Indireto (não confirmado) | Possível vínculo com marca maior "Human Academy" (Nando Blum) — não confirmado |
| 31 | @geiss11 | creator | Não | Nenhum resultado correspondente |
| 32 | @nelmoricalde | creator | Não | Nenhum resultado correspondente |
| 33 | @rodrigotadewald | marketing | Não | Nenhum resultado correspondente |
| 34 | @sujeitoprogramador | ia | Não | Nenhum resultado correspondente |
| 35 | @jonathan_kamargo | creator | Não | Nenhum resultado correspondente |
| 36 | @marianatorre.s | marketing | Não | Nenhum resultado correspondente |
| 37 | @marketerhub.ai | marketing | Não | Nenhum resultado correspondente |
| 38 | @marcelaluzzio | marketing | Indireto (não confirmado) | Possível "Marcela Lúzio" (grafia com acento), produtora de conteúdo com IA |
| 39 | @gestordeaudiencia | marketing | Não | Termo tratado como genérico pela busca |
| 40 | @sebintel | ia | Indireto (não confirmado) | CreatorDB: Sebastien Jefferies, ~340,8k seguidores, comunidade "AI Creator Lab" |
| 41 | @avora.ai | agencia | Não | Nenhum resultado correspondente |
| 42 | @ogabrieeldias | creator | Não | Nenhum resultado correspondente |
| 43 | @rodrigobindes | founder | Não | Nenhum resultado correspondente |
| 44 | @franklim.gui | creator | Não | Nenhum resultado correspondente |
| 45 | @gabrielsamp.ai | ia | Não | Nenhum resultado correspondente |
| 46 | @maestrosdaia | ia | Não | Nenhum resultado correspondente |
| 47 | @brandsdecoded__ | marketing | Não | Nenhum resultado correspondente |
| 48 | @anatex | creator | Indireto (não confirmado) | CreatorDB/Reportei: educadora de IA para negócios, ~626k–717k seguidores (fontes divergem) |
| 49 | @larissagomes.ia | ia | Não | Nenhum resultado correspondente |
| 50 | @thiagozaao | creator | Não | Nenhum resultado correspondente |
| 51 | @neuwebstudio | agencia | Não | Nenhum resultado correspondente |
| 52 | @laschuk | founder | Indireto (não confirmado) | Possível "Lascha Kvitelashvili" (Favikon) — vínculo por semelhança de nome, não confirmado |
| 53 | @maestroptompts | ia | Não | Nenhum resultado correspondente |
| 54 | @faladantasmkt | marketing | Indireto (não confirmado) | Possível projeto "Fala Dantas" (Jéssica Dantas) — vínculo não confirmado |
| 55 | @lindsay.ia | ia | Não | Nenhum resultado correspondente |
| 56 | @andrevictor.m | marketing | Não | Nenhum resultado correspondente |
| 57 | @drisiano | creator | Não | Nenhum resultado correspondente |
| 58 | @brun0gpt | ia | Não | Nenhum resultado correspondente |
| 59 | @maxcarrau.ia | ia | Não | Nenhum resultado correspondente |
| 60 | @noevarner | creator | Não | Nenhum resultado correspondente |
| 61 | @yikchanltd | creator | Não | Nenhum resultado correspondente |

**Resumo:** 13/61 perfis (21%) tiveram algum indício indireto e não confirmado. 48/61 (79%) não tiveram absolutamente nenhum dado localizável. **Nenhum post real, hook, CTA ou número de engajamento oficial foi confirmado para nenhum dos 61 perfis** nesta execução.

---

## Perfis com Indícios Indiretos (não oficiais, não confirmados)

Nenhum destes é dado confirmado do perfil oficial do Instagram — são pistas de agregadores de terceiros (CreatorDB, Favikon, Heepsy, Reportei) ou páginas homônimas, listadas aqui apenas como contexto para investigação manual futura, não como análise de conteúdo (Fase 1 do instagram-content-cloner não foi possível para nenhum deles, por falta de posts reais).

### @nick_saraev (automacao)
Agregadores (Cake.me, CreatorDB) sugerem entre ~100k e ~693k seguidores (estimativas divergentes entre fontes, não confiáveis) e nicho de automação de negócios/IA (n8n, Make.com, Claude Code, GitHub Codex, monetização de agência). Nenhum hook, CTA ou legenda real foi encontrado.

### @nathanhodgson (ia)
Agregadores (Motionapp, CreatorDB — para o handle "nathanhodgson_"/"Nathanhodgson.Ai", sem certeza de ser o mesmo perfil exato) sugerem ~142–146k seguidores e formato de reels tutoriais sobre ferramentas de IA, com parcerias citadas (Perplexity, Suno, Anthropic, Google). Fontes divergem nos números. Nenhum post real encontrado.

### @gabriel.adamuchi (creator)
Uma página Gumroad homônima ("Gabriel Adamuchi") descreve um investidor/empreendedor de marketing digital com produtos digitais (guia de prompts ChatGPT/Midjourney). Não é a bio do Instagram — apenas indício indireto de nicho.

### @nikolassasso (creator)
CreatorDB descreve "Nikolas Sasso" como educador de marketing digital BR desde 2017, ~181k seguidores IG, ~68,5k YouTube, engajamento IG ~2,8%, foco em funis automatizados/produtos digitais. **Atenção:** o texto desta fonte é estruturalmente quase idêntico ao gerado para @jonylan (abaixo) — forte indício de conteúdo templado/pouco confiável do agregador.

### @jonylan (creator)
Mesma fonte (CreatorDB) descreve "estrategista de marketing digital e educador de IA" com ~346k seguidores IG (engajamento 5,4%) e ~63k YouTube. Mesmo alerta de confiabilidade do item acima — texto com estrutura quase idêntica entre os dois perfis.

### @leandroladeiran (marketing)
Possível confusão com "Leandro Ladeira" (grafia sem o "n" final, criador do método "Venda Todo Santo Dia"). Um agregador (creatordb.app) cita ~3,2M de seguidores agregados (IG+TikTok) para o handle exato, mas o conteúdo da página não pôde ser acessado (DNS bloqueado) para confirmar.

### @oneyaraujo (creator)
Fonte secundária (reportei.com) descreve "Oney Araújo", ex-YouTuber de humor fitness, hoje especialista em marketing viral, curso "Código Viral®" sobre Reels (~50 mil alunos, não verificado). Vínculo com o handle exato não confirmado.

### @human___academy (ia)
Pode se relacionar à marca maior "Human Academy" (braço de ensino do estúdio de IA "Human", CEO Nando Blum) — mas o handle com underscores triplos sugere possivelmente uma conta distinta/pessoal. Não confirmado.

### @marcelaluzzio (marketing)
Página de palestrante (mundodomarketing.com.br) descreve "Marcela Lúzio" (grafia com acento), produtora de conteúdo com IA, criadora desde 2019, audiência focada em tecnologia/IA com alcance relatado de +1M pessoas/mês. Grafia do nome não é idêntica ao handle — tratar como pista não verificada.

### @sebintel (ia)
CreatorDB descreve o perfil como administrado por "Sebastien Jefferies", educação sobre ferramentas de IA, agência "Haiven Agency", comunidade paga "AI Creator Lab" (Skool, ~1,6k membros). Métricas reportadas: ~340.751 seguidores IG (+20k em 30 dias), engajamento 4,5%, ~11 posts/semana, 67,8k TikTok. Dados de agregador, não oficiais.

### @anatex (creator)
CreatorDB e Reportei descrevem uma educadora digital BR de IA para negócios ("Meu Negócio com Inteligência Artificial", oferta de "GPT-bots"). Seguidores divergem entre fontes: ~717k (CreatorDB) vs. ~626k (Reportei). Engajamento reportado entre 1,2% e 1,6% (inconsistente mesmo dentro da mesma fonte).

### @laschuk (founder)
Possível vínculo com "Lascha Kvitelashvili", criador germano-georgiano com ~2,3M de seguidores agregados (TikTok/YouTube/Instagram) segundo Favikon — vínculo apenas por semelhança de nome, não confirmado.

### @faladantasmkt (marketing)
Possível vínculo com o projeto "Fala Dantas" de Jéssica Dantas (citado em artigo do Correio24horas sobre Reels como melhor formato de alcance) — vínculo não confirmado com o handle exato.

---

## Limitações de Dados

- **Todos os 61 perfis:** `WebFetch` em `instagram.com` falhou com erro de DNS (`getaddrinfo ENOTFOUND www.instagram.com`) em 100% das tentativas — o domínio está inacessível a partir desta sessão. Nenhuma bio, contagem de seguidores oficial ou metadado de página foi coletado por essa via para nenhum perfil.
- **48 perfis sem nenhum dado (nem indireto):** @charliehills, @yikC, @eujoaotorresz, @fabianocarvalhojr, @rafa.grandi, @brusantanna.ai, @vendedorglobal, @oluizmain, @ai, @ana.gsoares, @chase.h.ai, @leosoares.ia, @viverdeia.ai, @ninja.automacoes, @eduardocavalcanti, @allesinisgalli, @lonamkt, @gabrielbarbosa.oficial, @opensession.co, @christiantriad, @geracaotechs, @amandadinizmkt, @geiss11, @nelmoricalde, @rodrigotadewald, @sujeitoprogramador, @jonathan_kamargo, @marianatorre.s, @marketerhub.ai, @gestordeaudiencia, @avora.ai, @ogabrieeldias, @rodrigobindes, @franklim.gui, @gabrielsamp.ai, @maestrosdaia, @brandsdecoded__, @larissagomes.ia, @thiagozaao, @neuwebstudio, @maestroptompts, @lindsay.ia, @andrevictor.m, @drisiano, @brun0gpt, @maxcarrau.ia, @noevarner, @yikchanltd — WebSearch (3–5 variações de query por perfil: busca direta, "quem é"/nome provável, site:instagram.com, linktree/tiktok/youtube, agregadores) só retornou contas homônimas não relacionadas ou conteúdo genérico do nicho, sem nenhuma correspondência confirmada ao handle exato.
- **13 perfis com indício indireto não confirmado:** ver seção acima — nenhum é dado oficial do perfil, e nenhum hook/CTA/post real foi extraído para eles.
- Nenhum dado de post, hook, CTA, tom de voz ou engajamento foi inventado em nenhum caso, conforme regra do módulo 2.

---

## Perfis Sugeridos pelo Sistema

Não aplicável — a lista de perfis já tinha 61 entradas ativas em `config/profiles.json` (modo análise direto, sem modo descoberta).
