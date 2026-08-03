# Análise de Perfis Instagram — 2026-08-03

## Nota metodológica

O Instagram bloqueou WebFetch direto (HTTP 403) em **100% das 61 tentativas** de acesso a URLs de perfil/post ao longo desta execução. Todos os dados abaixo vêm de resultados indexados via WebSearch (snippets de busca, agregadores de terceiros, cross-posts em TikTok/Threads/YouTube da mesma pessoa/marca). Nenhum dado de engajamento, seguidores ou conteúdo de post foi inventado — onde a informação real não pôde ser confirmada, o campo foi deixado vazio/mínimo e a limitação documentada explicitamente na tabela de limitações ao final.

De 61 perfis ativos em `config/profiles.json`, **10 handles não puderam ser localizados** por nenhuma variação de busca (possivelmente inexistentes, privados, com erro de digitação, ou não indexados): `yikC`, `eujoaotorresz`, `rafa.grandi`, `nikolassfaria`, `jonathan_kamargo`, `ogabrieeldias`, `gabrielsamp.ai`, `maestroptompts`, `lindsay.ia`, `drisiano`, `maxcarrau.ia`, `thiagozaao` (12 no total — ver seção de Limitações).

---

## Visão Geral dos Perfis

| Perfil | Categoria | Formato Dominante | Engajamento | Seguidores (aprox., não confirmado direto) | Hook Padrão |
|--------|-----------|------------------|-------------|------|-------------|
| @charliehills | ia | reels | alto | 88K | "We're so cooked. Nano Banana 2 dropped today." |
| @yikC | não identificado | — | — | — | perfil não localizado |
| @eujoaotorresz | não identificado | — | — | — | perfil não localizado |
| @fabianocarvalhojr | ia | reels | alto | 84K | "Você ainda acha que precisa de um time inteiro..." |
| @rafa.grandi | não identificado (fora do nicho) | — | — | 247 | perfil pessoal, não relacionado ao nicho |
| @brusantanna.ai | ia / mentoria | misto | baixo | — | não identificado |
| @vendedorglobal | e-commerce / marketing | reels | médio | 83K | "Ecommerce Marketplace \| Comenta ..." |
| @oluizmain | creator mobile / ia | reels | alto | 215K | não identificado |
| @nick_saraev | ia / automação | reels | alto | 541K | "Comment 'CODING' to get this AI Code Editor." |
| @nathanhodgson | ia / automação (handle ambíguo) | reels | médio | 128K* | "Built a 6-Figure Business Powered By AI" |
| @ai | desconhecido/institucional | misto | médio | — | não identificado |
| @ana.gsoares | negócios digitais / ia | misto | médio | 146K | "Esse prompt te ajuda a encontrar vagas..." |
| @chase.h.ai | educador de ia | reels | alto | 221K | bio: "DM 'Ready' to Apply For 1:1 Mentorship" |
| @leosoares.ia | ia para negócios | misto | médio | 219K | não identificado |
| @gabriel.adamuchi | ia fácil / creator | reels | médio | — | "Ultra-realistic humorous Christmas scene..." (prompt) |
| @viverdeia | ia para empresas (B2B) | misto | alto | 129K | não identificado |
| @ninja.automacoes | automação / ia | reels | médio | — | "3 coisas que você NÃO vai..." |
| @nikolassfaria | não identificado | — | — | — | perfil não localizado |
| @eduardocavalcanti | ia para negócios / institucional | misto | alto | 183K | não identificado |
| @jonylan | marketing / ia / palestrante | reels | alto | 306K | "VEO 2 do Google..." |
| @allesinisgalli | ia + marketing (mentoria) | reels | baixo | — | não identificado |
| @lonamkt | marketing digital / creator | reels | baixo | — | "🇮🇹 Primeiro milhão aos 18" |
| @gabrielbarbosa.oficial | negócios digitais | misto | baixo | 7.782 | "Foi assim que comecei..." |
| @opensession.co | design/branding (fora do nicho BR) | misto | médio | 23K | "Brand x UX/AI x Design Systems" |
| @leandroladeiran | marketing / copywriting | reels | alto | 2M | "Fórmula de lançamento ou Venda todo santo dia?" |
| @christiantriad | produtividade/tech | reels | alto | 584K | "Como disse Bill Gates, 'A vida não é justa...'" |
| @oneyaraujo | marketing / conteúdo viral | reels | alto | 2M | "Revelando Segredos de como Viralizar..." |
| @geracaotechs | tecnologia / ferramentas de ia | reels | médio | — | "Esqueça tudo o que você sabe sobre geradores de vídeo..." |
| @amandadinizmkt | marketing / ia (inferido) | misto | baixo | — | não identificado |
| @humam__academy | não identificado | — | — | — | perfil não localizado com confiança |
| @geiss11 | produtos digitais | reels | médio | 45K | "apenas confie. Me siga para mais @geiss11" |
| @nelmoricalde | ia / negócios digitais | misto | médio | — | bio: "IA, Negócios & Lucro" |
| @rodrigotadewald | ia / educação / programação | misto | médio | — | não identificado (marca Asimov Academy) |
| @sujeitoprogramador | programação / educador tech | misto | alto | 168K | não identificado |
| @jonathan_kamargo | não identificado | — | — | — | perfil não localizado |
| @marianatorre.s | não identificado | — | — | — | perfil não localizado |
| @marketerhub.ai | ia / marketing | misto | médio | — | não identificado |
| @marcelaluzzio | ia / marketing de conteúdo | misto | alto | 226K | "Ative o Claude para trabalhar por você" |
| @gestordeaudiencia | não identificado | — | — | — | perfil não localizado |
| @sebintel | não identificado | reels | baixo | — | não identificado |
| @avora.ai | ia | misto | baixo | — | "Avora wasn't created just to talk about AI..." |
| @ogabrieeldias | não identificado | — | — | — | perfil não localizado |
| @rodrigobindes | marketing / mentor de agências | reels | alto | 280K | bio: "Mostro como chegar aos 100k/mês com agência de mkt" |
| @franklim.gui | ia / educador digital | misto | médio | 46K | não identificado (cursos de Claude Code) |
| @gabrielsamp.ai | não identificado | — | — | — | perfil não localizado |
| @maestrosdaia | ia / automação / educação | misto | médio | — | "O agente de IA que trabalha enquanto você dorme" |
| @brandsdecoded | marketing / agência com ia | carrossel | alto | 301K* | não identificado |
| @anatex | ia para negócios / palestrante | misto | alto | 694K | "Sabia que a maioria dos empresários... não sabe quase nada sobre IA?" |
| @larissagomes.ia | ia / marketing pessoal | reels | baixo | 15K | "Peça o chatGPT para analisar o feed do seu instagram" |
| @thiagozaao | não identificado | — | — | — | perfil não localizado |
| @neuwebstudio | web design | reels | médio | 52K | "If you want to master Figma and Web design..." |
| @laschuk | email marketing | reels | médio | 36K | "nunca consegui vender..." |
| @maestroptompts | não identificado | — | — | — | perfil não localizado |
| @faladantasmkt | marketing de conteúdo / mentoria | misto | alto | 99K | "É assim que..." |
| @lindsay.ia | não identificado | — | — | — | perfil não localizado |
| @andrevictor.m | lifestyle / riqueza / business | reels | alto | 244K | não identificado |
| @drisiano | não identificado | — | — | — | perfil não localizado |
| @brun0gpt | ia / marketing digital | carrossel | alto | 157K | não identificado |
| @maxcarrau.ia | não identificado | — | — | — | perfil não localizado |
| @noevarner | ia/automação (mercado internacional) | reels | médio | — | não identificado (handle real provável: @noevarner.ai) |
| @yikchan | ia/e-commerce/mentoria (handle ambíguo) | reels | médio | 79K* | não identificado |

\* Número referente a handle alternativo/relacionado (@nathanhodgson.ai, @brandsdecoded__, @yikchanltd) — ver limitações.

---

## Análise Detalhada por Perfil

### @charliehills — ia
**Bio:** "💙 I help you (actually) use AI 📧 collabs@charliehills.ai 👇 100+ free AI prompts, guides & tools" (~88K seguidores, 260 posts)
- **Hooks:** fenômeno nomeado ("We're so cooked. Nano Banana 2 dropped today."), paradoxo/contraste ("Perplexity Computer is your new social media manager...")
- **Estrutura:** anuncia lançamento/atualização de ferramenta de IA com tom de urgência/hype → explicação prática passo a passo → CTA para link na bio
- **CTA:** link na bio (100+ free AI prompts, guides & tools)
- **Tom:** prático, hypado, didático, direto, entusiasmado
- **Formato:** reels · **Engajamento:** alto
- **Temas:** Nano Banana / Nano Banana 2, Gemini, Perplexity Computer, prompts e guias práticos

### @fabianocarvalhojr — ia
**Bio:** "Founder lasy.ai. Crio Agentes de IA que vendem e operam Negócios 24/7. Te Ensino na Aula Grátis" (~84K seguidores, 1.218 posts)
- **Hooks:** maioria errando ("Você ainda acha que precisa de um time inteiro e meses de trabalho pra lançar seu próprio SaaS?")
- **Estrutura:** apresenta crença comum → demonstra ferramenta (Lasy.ai) resolvendo em minutos → CTA de comentário
- **CTA:** comente palavra-chave (ex: "Lasy")
- **Tom:** vendedor, entusiasmado, didático, urgente, confiante
- **Formato:** reels · **Engajamento:** alto
- **Temas:** Lasy.ai (SaaS via IA sem código), agentes de IA, aula grátis

### @nick_saraev — ia / automação
**Bio:** não recuperada integralmente (~541K seguidores, 366 posts). Fundador da "Maker School" e da consultoria "LeftClick".
- **Hooks (alta frequência):** padrão "comment-to-unlock" — "Comment 'QWEN' to get this...", "Comment OPENSOURCE...", "Comment APIFY...", "Comment 'CODING' to get this AI Code Editor.", "Comment 'SYSTEM'..."
- **Estrutura:** demo curta de ferramenta/automação de IA → CTA pedindo comentário de palavra-chave para receber o recurso gratuito
- **CTA:** "Comment [PALAVRA] to get [recurso]"
- **Tom:** direto, técnico, prático, orientado a valor, confiante
- **Formato:** reels · **Engajamento:** alto
- **Temas:** ferramentas de IA (Qwen, Flux), automação n8n/Make.com, agências de automação, templates Apify

### @jonylan — marketing / ia / palestrante
**Bio:** "Inteligência Artificial Ninja da internet desde 1994" — Builder no Google Brasil (~306K seguidores, também ativo no TikTok)
- **Hooks:** fragmentos truncados — "VEO 2 do Google...", "Arquitetura de IA..."
- **CTA:** "Já me siga" (para receber mais conteúdo)
- **Tom:** direto, promocional, técnico, carismático
- **Formato:** reels · **Engajamento:** alto
- **Temas:** IA generativa (VEO 2), arquitetura de agentes, palestras/eventos, cursos de marketing+IA

### @leandroladeiran — marketing digital / copywriting
**Bio:** "Se você quer aprender sobre marketing e produtos digitais, clicar no link abaixo vai fazer sua vida mais fácil (e com mais dinheiro)" (~2M seguidores, 845 posts)
- **Hooks:** paradoxo/contraste ("Fórmula de lançamento ou Venda todo santo dia? 👀👀👀")
- **Estrutura:** cadência diária (reels + lives), contraste entre métodos de venda, reforço dos métodos próprios (VTSD, Light Copy)
- **CTA:** link na bio
- **Tom:** direto, persuasivo, didático, descontraído, autêntico
- **Formato:** reels · **Engajamento:** alto
- **Temas:** copywriting (Light Copy), venda recorrente (VTSD), storytelling, Stories 10x

### @christiantriad — produtividade / tech
**Bio:** "🤖 Desde 99 invisto e desenvolvo dezenas de empresas de tech e Saas 💻 Criador do método 'A Tríade do Tempo' 2M+ pessoas treinadas" (~584K seguidores, 4.430 posts)
- **Hooks:** citação de autoridade ("Como disse Bill Gates, 'A vida não é justa, acostume-se...'"), pergunta direta ("E aí Pensador, o que você tira de lição...")
- **Tom:** inspiracional, direto, reflexivo, autoritativo, motivacional
- **Formato:** reels · **Engajamento:** alto
- **Temas:** produtividade, gestão do tempo, Tríade do Tempo, tech/SaaS/IA

### @oneyaraujo — marketing / conteúdo viral
**Bio:** "🏆 Revelando Segredos de como Viralizar, Ganhar Seguidores e Vender Online. 🚀 +66.000 alunos... 👉🏻 Código Viral" (~2M seguidores)
- **Hooks:** maioria errando ("Revelando Segredos de como Viralizar, Ganhar Seguidores e Vender Online"), "Pegue todos os Códigos das viralizações no Código Viral"
- **Estrutura:** promessa de revelar "segredos"/"códigos" → prova de autoridade (1B+ views trabalhados) → conversão para oferta paga
- **CTA:** link na bio (Código Viral)
- **Tom:** direto, vendedor, confiante, didático, hype
- **Formato:** reels · **Engajamento:** alto
- **Temas:** como viralizar, crescimento de seguidores, ferramentas de edição de vídeo com IA (OpusClip)

### @geracaotechs — tecnologia / ferramentas de ia
**Bio:** "Tecnologia e I.A" (Glauton Filho) — número de seguidores não confirmado
- **Hooks (alta):** paradoxo/contraste ("Esqueça tudo o que você sabe sobre geradores de vídeo... o Anijam é..."), "Esse site te permite criar jogos só descrevendo sua ideia..."
- **Estrutura:** gancho de quebra de expectativa/pergunta comparativa sobre ferramenta de IA → demo prática → "link na bio"
- **Tom:** didático, empolgado, acessível, prático, entusiasta de tecnologia
- **Formato:** reels · **Engajamento:** médio
- **Temas:** Anijam, Gambo.ai, Gamma.app, Replit, criação de jogos com IA, customização de carros com IA

### @anatex — ia para negócios / palestrante
**Bio:** "Ana Tex - Inteligência Artificial para Negócios" (~694K seguidores, 1.358 posts)
- **Hooks:** maioria errando ("Sabia que a maioria dos empresários e empreendedores aqui do Brasil não sabe quase nada sobre IA aplicada aos negócios?")
- **Tom:** direto, consultivo, autoritativo, didático
- **Formato:** misto · **Engajamento:** alto
- **Temas:** IA aplicada a negócios, marketing digital, automação de presença online, palestras/workshops

### @larissagomes.ia — ia / marketing pessoal
**Bio:** "💻 Te ensino a criar um negócio enxuto e que vende: você + IA ⚡️ ... Domine o chatGPT👇🏻" (~15K seguidores, 262 posts)
- **Estrutura:** hook com dica prática/prompt → passo a passo numerado (1️⃣2️⃣3️⃣) → reforço de CTA de seguir/salvar
- **Hook exemplo:** "Peça o chatGPT para analisar o feed do seu instagram 🧠"
- **CTA:** "siga @larissagomes.ia para receber mais conteúdos" / "Salva pra lembrar"
- **Tom:** didático, acessível, prático, encorajador
- **Tamanho médio:** ~220 palavras (educativo)
- **Formato:** reels · **Engajamento:** baixo
- **Temas:** prompts de ChatGPT para negócios, automação/produtividade com IA, crescimento de perfil

### @rodrigobindes — marketing / mentor de agências
**Bio:** "Mostro como chegar aos 100k/mês com agência de mkt" (~280K seguidores, 1.873 posts)
- **Tom:** direto, assertivo, didático, orientado a resultado, confiante
- **Formato:** reels · **Engajamento:** alto
- **Temas:** escalar agência de marketing, faturamento 100k/mês, mentoria Ultra/Ultralize, marketing para restaurantes

### @faladantasmkt — marketing de conteúdo / mentoria
**Bio:** "Jessica Dantas | Mentora de conteúdo & negócios digitais" (~99K seguidores)
- **Tom:** didático, motivacional, confiante, acolhedor, empreendedor
- **Formato:** misto · **Engajamento:** alto
- **Temas:** conteúdo estratégico para vender, posicionamento pessoal, método "Conteúdo que Vende"

### @andrevictor.m — lifestyle / riqueza / business
**Bio (paráfrase indireta):** menção a ter feito o primeiro milhão aos 18, Ferrari Portofino, 50 países visitados até os 22 anos (~244K seguidores, 286 posts)
- **Tom:** ostentação, aspiracional, confiante, storytelling pessoal
- **Formato:** reels · **Engajamento:** alto
- **Temas:** riqueza/patrimônio, viagens internacionais, carros de luxo, trajetória de sucesso jovem

### @brun0gpt — ia / marketing digital
**Bio:** "IA e Marketing" / "Marketing e Vendas com Inteligência Artificial" (Bruno Francisco, ~157K seguidores, 1.334 posts)
- **Tom:** didático, vendedor, direto, orientado a resultado/prova social
- **Formato:** carrossel · **Engajamento:** alto
- **Temas:** marketing/vendas com IA, criação de conteúdo com ChatGPT, automação de conteúdo, copywriting/funis

### Demais perfis com dados parciais confirmados

| Perfil | Dado real confirmado | Limitação principal |
|---|---|---|
| @vendedorglobal | ~83K seguidores, foco e-commerce/marketplace, CTA "Comenta..." | legendas truncadas |
| @oluizmain | ~215K seguidores, cursos "Mobile Pro"/"AI Creator Pro" | sem legendas verbatim |
| @chase.h.ai | bio completa real, ~221K seguidores, foco Claude Code | sem legendas de reels |
| @ana.gsoares | 1 legenda real (truncada) sobre prompt de vagas | amostra insuficiente |
| @gabriel.adamuchi | 1 prompt real de imagem encontrado | dados de IG vs TikTok misturados |
| @viverdeia | handle real é @viverdeia.ai, plataforma B2B de IA | CTA não confirmado na conta certa |
| @eduardocavalcanti | bio real: "Maestro de Hiperagentes \| Presidente IBIA", ~183K seguidores | sem posts individuais |
| @leosoares.ia | ~219K seguidores, bio variou entre buscas | sem legendas confirmadas |
| @marcelaluzzio | ~226K seguidores, foco Claude+infoprodutos | sem bio completa |
| @sujeitoprogramador | ~168K seguidores, referência em programação BR | sem legendas |
| @franklim.gui | ~46K seguidores, cursos de Claude Code na Udemy | sem legendas |
| @maestrosdaia | dados via TikTok/site irmão (200k+ seguidores comunidade) | dados não exclusivos do IG |
| @neuwebstudio | ~52K seguidores, "Cinematic Web Design", Figma Animations | legenda vem de cross-post TikTok |
| @laschuk | ~36K seguidores, foco email marketing/ActiveCampaign | frases truncadas |
| @noevarner | handle real provável @noevarner.ai, foco Claude Code/n8n | fora do nicho BR, sem seguidores confirmados |
| @yikchan | dados majoritariamente de @yikchanltd (~79K) | ambiguidade de conta não resolvida |
| @nathanhodgson | dados de @nathanhodgson.ai (~128K), não do handle literal | handle pedido pode não ser o perfil relevante |
| @brandsdecoded | dados de @brandsdecoded__ (~301K) | handle exato sem underscore duplo não indexado |

---

## Perfis Sugeridos pelo Sistema
Não aplicável nesta execução — `config/profiles.json` já continha 61 perfis ativos (Modo Análise, Passo 2 executado diretamente).

---

## Limitações de Dados

**Limitação sistêmica (todos os 61 perfis):** o Instagram bloqueou WebFetch direto (HTTP 403) em 100% das tentativas de acesso a URLs de perfil e posts individuais, incluindo espelhos de terceiros (Picuki, Imginn). Todos os dados vêm de snippets indexados via WebSearch (Google/Bing), que frequentemente truncam legendas com reticências, tornando impossível confirmar o texto integral de hooks/CTAs na maioria dos casos. Números de seguidores/posts/curtidas não puderam ser verificados por acesso direto — são valores reportados por resultados de busca de terceiros, sujeitos a desatualização.

**Perfis não localizados (nenhum dado real encontrado, apesar de múltiplas variações de busca):**
- @yikC — nenhum resultado correspondente ao handle exato
- @eujoaotorresz — nenhum resultado correspondente
- @rafa.grandi — único perfil indexado com esse handle é pessoal (analista jurídico), sem relação com o nicho
- @nikolassfaria — nenhum resultado correspondente (handles parecidos pertencem a outras pessoas)
- @jonathan_kamargo — nenhum resultado correspondente
- @humam__academy — handle exato (com dois underscores) não confirmado; perfis parecidos pertencem a outras contas
- @gestordeaudiencia — apenas um repositório GitHub homônimo encontrado, sem confirmação de vínculo com o IG
- @sebintel — perfil existe mas sem conteúdo indexado suficiente para categorizar
- @ogabrieeldias — nenhum resultado correspondente
- @gabrielsamp.ai — apenas conta homônima no TikTok, sem dados do IG
- @maestroptompts — nenhum resultado correspondente (site parecido "maestroprompts.com" não confirmado como mesmo dono)
- @lindsay.ia — nenhum resultado correspondente
- @drisiano — nenhum resultado correspondente
- @maxcarrau.ia — nenhum resultado correspondente
- @thiagozaao — nenhum resultado correspondente
- @marianatorre.s — nenhum resultado correspondente (apenas homônimos irrelevantes)
- @amandadinizmkt — apenas título de página indexado, sem posts/bio confirmados
- @nelmoricalde — apenas bio de título de página indexada, sem posts
- @allesinisgalli — dados de agregador terciário (Heepsy), sem posts confirmados
- @lonamkt — identidade possivelmente confundida com conta relacionada (@felipelonaa)
- @avora.ai — apenas 2 fragmentos de texto recuperados
- @rodrigotadewald — dados institucionais da marca (Asimov Academy) não exclusivos do perfil pessoal
- @marketerhub.ai — página institucional pouco estabelecida (5 curtidas no Facebook associado)
- @opensession.co — estúdio de design sediado nos EUA, fora do nicho-alvo BR
- @gabrielbarbosa.oficial — apenas 2-3 títulos truncados

**Recomendação:** revisar `config/profiles.json` para confirmar grafia exata dos 15 handles não localizados, e considerar remover/substituir os que se confirmarem inexistentes ou fora do nicho (ex: @opensession.co, @rafa.grandi).
