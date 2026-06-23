# Análise de Perfis Instagram — 2026-06-23

## Nota Metodológica (leia antes do restante do relatório)

A skill `instagram-content-cloner` (que normalmente executa a Fase 1 — extração profunda de hook/estrutura/tom/CTA) **não está instalada neste ambiente**, e o runtime Swarm (`swarm_task` / code interpreter QuickJS) exigido por `02-instagram.md` também **não está disponível** nesta sessão. Como substituto, a análise dos 61 perfis ativos de `config/profiles.json` foi feita por **3 agentes de pesquisa em paralelo** (respeitando o limite `concurrency: 3`), cada um cobrindo ~20 perfis via WebSearch direto, com instrução explícita de nunca inventar dados e marcar "dados insuficientes" quando nada de verificável foi encontrado.

Consequência prática: os campos profundos do template original (`hook_modelos` com frequência, `tom_adjetivos`, diagrama de `estrutura_tipica`, tabela de top 3 conteúdos por perfil) **não puderam ser preenchidos com confiabilidade** para a maioria dos perfis — Instagram bloqueia indexação de conteúdo textual completo via busca. Os campos abaixo refletem exatamente o que foi encontrado, nem mais nem menos.

**Resultado agregado:** 41/61 perfis com dados mínimos verificáveis (nicho + 1 evidência de formato/engajamento/hook). 20/61 com dados insuficientes (handle não localizado, conta homônima, ou zero conteúdo indexado).

---

## Visão Geral dos Perfis

| Handle | Categoria (config) | Formato Dominante | Engajamento | Hook/Sinal Padrão |
|--------|--------------------|--------------------|-------------|--------------------|
| @charliehills | creator | reels | médio (74K) | "Did you know ChatGPT has 8 hidden personalities" |
| @yikC | creator | indeterminado | indeterminado | dados insuficientes |
| @eujoaotorresz | creator | indeterminado | baixo (não confirmado) | dados insuficientes |
| @fabianocarvalhojr | founder | misto | médio-alto (66K) | "O Brasil tem 24 milhões de empresas... 7 ideias de Micro-SaaS" |
| @rafa.grandi | marketing | indeterminado | baixo (247) | conta pessoal, não corresponde ao nicho |
| @brusantanna.ai | ia | indeterminado (TikTok) | indeterminado | "Analisei meu próprio conteúdo com duas IAs..." |
| @vendedorglobal | negocio-digital | reels | alto (83K) | "Ganhe em DÓLAR sem precisar investir NADA!" |
| @oluizmain | creator | reels | alto (215K) | "Salve para fazer seus stories criativos" |
| @nick_saraev | automacao | reels | alto (508K) | "Comment 'SYSTEM' to get..." |
| @nathanhodgson | ia | reels | alto (141K) | "Comment 'AGENT' to get this Free General AI..." |
| @ai | ia | indeterminado | indeterminado | dados insuficientes |
| @ana.gsoares | marketing | misto | alto (146K) | "Esse prompt te ajuda a encontrar vagas..." |
| @chase.h.ai | ia | reels | alto (201K) | "My newest lead generation tool for my AI agents..." |
| @leosoares.ia | ia | reels | alto (219K) | "Com essa IA eu coloco muito mais leads..." |
| @gabriel.adamuchi | creator | reels | indeterminado | "Comenta 'CURSO' que te mando os links na DM" |
| @viverdeia | ia | misto | alto (121K) | "A plataforma completa de IA usada por +800 empresas" |
| @ninja.automacoes | automacao | misto | indeterminado | "Chega de 'automação Nutella'..." |
| @nikolassfaria | creator | indeterminado | indeterminado | dados insuficientes (confundido com figura pública homônima) |
| @eduardocavalcanti | founder | indeterminado | médio (138K) | nicho real é finanças, não IA |
| @jonylan | creator | indeterminado | alto (306K) | sem exemplo de post recuperado |
| @allesinisgalli | founder | indeterminado | baixo-médio (8.155) | dados insuficientes (parece perfil pessoal) |
| @lonamkt | marketing | indeterminado | baixo (4.316, IG pouco ativo) | atividade real no YouTube |
| @gabrielbarbosa.oficial | creator | reels | médio (7.782) | "Vivendo a vida do..." / "Foi assim que comecei..." |
| @opensession.co | agencia | indeterminado | médio (23K) | agência de design EUA, fora do nicho BR |
| @leandroladeiran | marketing | misto | alto (2M) | "Como VENDER para quem NÃO GOSTA de ler" |
| @christiantriad | creator | reels | alto (349K-585K, inconsistente) | "Transforme seu dia a dia com IA agora mesmo!" |
| @oneyaraujo | creator | reels | alto (2M) | "Já apareceu para você? Por isso..." |
| @geracaotechs | ia | indeterminado (Threads) | indeterminado | "Esse site te permite criar jogos só descrevendo sua ideia" |
| @amandadinizmkt | marketing | reels | indeterminado | sem post específico recuperado |
| @humam__academy | ia | indeterminado | indeterminado | dados insuficientes (handle exato não confirmado) |
| @geiss11 | creator | reels | médio (45K) | "O ambiente te molda!" |
| @nelmoricalde | creator | indeterminado | indeterminado | dados insuficientes |
| @rodrigotadewald | marketing | indeterminado | médio-alto (174K) | nicho real é IA/educação tech |
| @sujeitoprogramador | ia | misto | alto (167K) | "Se você ainda não passou por isso então ainda não é dev..." |
| @jonathan_kamargo | creator | indeterminado | indeterminado | dados insuficientes (handle não localizado) |
| @marianatorre.s | marketing | indeterminado | indeterminado | dados insuficientes (handle não localizado) |
| @marketerhub.ai | marketing | indeterminado | indeterminado | comunidade privada de marketing com IA |
| @marcelaluzzio | marketing | reels | alto (226K) | sem post específico recuperado |
| @gestordeaudiencia | marketing | indeterminado | indeterminado | dados insuficientes/possível confusão |
| @sebintel | ia | reels | indeterminado | "Comment 'Cut' and I'll send you the full guide..." (conteúdo em inglês) |
| @avora.ai | agencia | indeterminado | indeterminado | dados insuficientes (múltiplas entidades homônimas) |
| @ogabrieeldias | creator | indeterminado | indeterminado | bio indica "SaaS Founder" |
| @rodrigobindes | founder | reels | alto (278K) | "Dono de agência, quer espantar os seus clientes? Faça isto" |
| @franklim.gui | creator | indeterminado | médio (46K) | foco real em cursos de IA/Claude Code, não recuperado em posts |
| @gabrielsamp.ai | ia | indeterminado (TikTok) | indeterminado | automação com n8n, foco em "canais dark" |
| @maestrosdaia | ia | indeterminado | indeterminado | automação Make/n8n/Lovable |
| @brandsdecoded | marketing | carrossel | alto (301K) | "Apresentando... Content Machine 3.0" |
| @anatex | creator | reels | alto (682K) | títulos truncados, sem hook completo |
| @larissagomes.ia | ia | reels | baixo-médio (15K) | "Peça ao chatGPT para analisar o feed do seu Instagram" |
| @thiagozaao | creator | indeterminado | indeterminado | dados insuficientes (handle não localizado) |
| @neuwebstudio | agencia | misto | médio (52K IG / 1.7M TikTok) | nicho real é web design, não IA/negócio |
| @laschuk | founder | reels | médio (36K) | "5 modelos aqui 👇" — nicho real é email marketing |
| @maestroptompts | ia | indeterminado | indeterminado | dados insuficientes (handle não confirmado) |
| @faladantasmkt | marketing | reels | alto (99-109K) | sem hook literal recuperado |
| @lindsay.ia | ia | indeterminado | indeterminado | dados insuficientes (handle não localizado) |
| @andrevictor.m | marketing | reels | indeterminado | "Prazer, André Victor!" |
| @drisiano | creator | indeterminado | indeterminado | dados insuficientes (handle não localizado) |
| @brun0gpt | ia | misto | alto (157K) | "Primeiro, peça ao ChatGPT para analisar suas métricas..." |
| @maxcarrau.ia | ia | indeterminado | indeterminado | conteúdo sobre IA e Claude Code |
| @noevarner | creator | reels | baixo taxa (91.740, 0,45% eng.) | "This is how you actually use Claude to go viral" |
| @yikchan | creator | indeterminado | médio (78K) | handle real @yikchanltd — eCom/Business mentor |

---

## Discrepâncias de Categoria Identificadas

Vários perfis têm conteúdo real divergente da categoria atribuída em `config/profiles.json`. Vale revisão manual:

| Handle | Categoria config | Nicho real observado |
|--------|-------------------|------------------------|
| @rafa.grandi | marketing | conta pessoal sem relação com marketing |
| @ana.gsoares | marketing | carreira/agile/IA, não marketing tradicional |
| @eduardocavalcanti | founder | finanças/investimentos |
| @christiantriad | creator | IA, Tech & SaaS / produtividade |
| @oneyaraujo | creator | growth de Reels/Instagram ("Código Viral") |
| @nelmoricalde | creator | "IA, Negócios & Lucro" |
| @rodrigotadewald | marketing | IA/educação tech (professor Asimov Academy) |
| @brandsdecoded | marketing | AI Content Agency (carrosséis com IA) |
| @anatex | creator | "IA para Negócios" (mentoria B2B) |
| @neuwebstudio | agencia | web design/dev, não IA/negócio digital |
| @laschuk | founder | email marketing |
| @noevarner | creator | handle real `.ai`, conteúdo específico Claude/IA |
| @yikchan | creator | handle real `yikchanltd`, eCom/Business mentor |
| @opensession.co | agencia | agência de branding/UX dos EUA, fora do nicho BR |
| @gabrielbarbosa.oficial | creator | negócios digitais (não creator genérico) |
| @ogabrieeldias | creator | "SaaS Founder" |

---

## Padrões de CTA Observados (cross-perfil)

- **"Comment [PALAVRA] to get/para receber..."** — padrão dominante em contas de IA/automação em inglês e português (@nick_saraev, @nathanhodgson, @leosoares.ia, @gabriel.adamuchi, @sebintel).
- **Link na bio para produto/curso próprio** — comum em founders/infoprodutores (@oneyaraujo "Código Viral", @brandsdecoded "Content Machine 3.0").
- **"Siga para mais conteúdo como esse"** — @larissagomes.ia.
- Vários perfis com alto número de seguidores não tiveram CTA textual exato recuperável via busca (limitação de indexação, não ausência de CTA).

---

## Limitações de Dados

**20 de 61 perfis sem dados suficientes** (handle não localizado, conta homônima não confirmada, ou zero conteúdo indexável via WebSearch):

| Handle | Motivo da limitação |
|--------|----------------------|
| @yikC | nenhuma conta correspondente localizada (resultados: YWCA Kids Club, app Yik Yak) |
| @ai | handle de 2 caracteres, impossível isolar via busca textual |
| @eujoaotorresz | possível conta @joaotorresz (sem "eu" no handle) mas não confirmado ser o mesmo perfil |
| @nikolassfaria | resultados dominados por figura pública homônima parcial (deputado Nikolas Ferreira) |
| @allesinisgalli | perfil parece pessoal/lifestyle, sem evidência de atividade "founder" |
| @brusantanna.ai | única atividade localizada foi cross-platform no TikTok, não no Instagram |
| @jonathan_kamargo | handle não localizado; variações próximas não coincidem |
| @marianatorre.s | handle não localizado; variações próximas não confirmam nicho |
| @humam__academy | handle exato (2 underscores) não encontrado; correspondência mais próxima usa 3 underscores |
| @gestordeaudiencia | handle não confirmado com certeza nos resultados |
| @sebintel | perfil existe mas sem bio/tema de conteúdo recuperável; único achado sugere conteúdo em inglês |
| @avora.ai | múltiplas entidades homônimas (agência BR, empresa odonto EUA, agência de branding) |
| @thiagozaao | handle não encontrado em nenhuma plataforma (IG, TikTok, YouTube, X) |
| @maestroptompts | handle não confirmado; possível erro de grafia |
| @lindsay.ia | handle não localizado; resultados retornam perfis "Lindsay" não relacionados |
| @drisiano | handle não encontrado; apenas variações não relacionadas (@driano, @drisansone) |
| @ogabrieeldias | apenas bio/título confirmado, nenhum post indexado |
| @maxcarrau.ia | conteúdo do tema confirmado mas sem métricas nem texto literal de post |
| @gabrielsamp.ai | presença mais forte parece ser TikTok; perfil do Instagram não indexado diretamente |
| @franklim.gui | conteúdo principal (cursos IA/Claude Code) não apareceu nos resultados de busca |

---

## Perfis Sugeridos pelo Sistema

Não aplicável nesta execução — `config/profiles.json` já contém 61 perfis ativos (Modo Análise), então o Modo Descoberta do Passo 1A não foi executado.

---

## Resumo da Limitação Estrutural

Esta análise é um substituto funcional, não equivalente, à Fase 1 do `instagram-content-cloner` rodando sobre Swarm. Os dados aqui (nicho, formato dominante, 1 exemplo de hook, evidência de engajamento, CTA quando encontrado) são suficientes para alimentar comparações de alto nível no Módulo 3 (Benchmark), mas **não** sustentam afirmações detalhadas sobre frequência de modelos de hook, tom de voz com adjetivos, ou tamanho médio de post por tipo — esses campos exigiriam acesso direto ao Instagram (scraping autorizado ou API oficial), fora do alcance desta sessão.
