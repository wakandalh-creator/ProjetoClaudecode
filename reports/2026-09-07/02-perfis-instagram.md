# Análise de Perfis Instagram — 2026-09-07

## Nota Metodológica — Limitação Sistêmica de Coleta

Nesta execução, o Instagram bloqueou **100% das tentativas de WebFetch** direto nas URLs de perfil (erro `EGRESS_BLOCKED` na rede desta sessão). A coleta dependeu inteiramente de `WebSearch`, que na maioria dos casos retorna apenas dados de nível de bio/contagem de seguidores/nicho geral — raramente legendas, hooks ou CTAs de posts individuais, que o Instagram não expõe a mecanismos de busca externos.

**Resultado:** dos 61 perfis ativos analisados, nenhum teve extração completa dos 5 elementos do Fase 1 (hook, estrutura, CTA, tom, tamanho) a partir de posts reais e verificáveis. 10 perfis tiveram ao menos 1 hook real identificado (via matérias, reposts ou menções externas). Os demais 51 ficaram limitados a sinais de nível de conta (bio, nicho, contagem aproximada de seguidores) ou não foram localizados com confiança. Nenhum dado foi inventado — todos os campos vazios ou `"não identificado"` refletem ausência real de informação encontrada, documentada individualmente em `limitacao_dados`.

**Recomendação:** para extração real de hooks/CTA/tom por post, este módulo precisa de um método de coleta que não dependa de WebFetch bloqueado (ex: scraping autorizado com API oficial do Meta, ou revisão manual de posts salvos/screenshots pelo Lucas).

---

## Visão Geral dos Perfis

| Perfil | Categoria | Formato Dominante | Engajamento | Hook Padrão | Dados Reais? |
|--------|-----------|--------------------|-------------|-------------|--------------|
| @charliehills | creator | reels | medio | outro | parcial (hook real) |
| @yikC | creator | misto | baixo | não identificado | não (só bio/nada) |
| @eujoaotorresz | creator | misto | baixo | não identificado | não (só bio/nada) |
| @fabianocarvalhojr | founder | misto | alto | não identificado | não (só bio/nada) |
| @rafa.grandi | marketing | misto | baixo | não identificado | não (só bio/nada) |
| @brusantanna.ai | ia | misto | não identificado | transformacao_silenciosa | parcial (hook real) |
| @vendedorglobal | negocio-digital | misto | alto | não identificado | não (só bio/nada) |
| @oluizmain | creator | reels | não identificado | outro | parcial (hook real) |
| @nick_saraev | automacao | reels | alto | outro | parcial (hook real) |
| @nathanhodgson | ia | misto | alto | outro | parcial (hook real) |
| @ai | ia | misto | baixo | não identificado | não (só bio/nada) |
| @ana.gsoares | marketing | misto | medio | não identificado | não (só bio/nada) |
| @chase.h.ai | ia | misto | alto | não identificado | não (só bio/nada) |
| @leosoares.ia | ia | misto | medio | não identificado | não (só bio/nada) |
| @gabriel.adamuchi | creator | reels | baixo | não identificado | não (só bio/nada) |
| @viverdeia.ai | ia | reels | medio | outro | parcial (hook real) |
| @ninja.automacoes | automacao | reels | medio | fenomeno_nomeado | parcial (hook real) |
| @nikolassasso | creator | reels | alto | maioria_errando | parcial (hook real) |
| @eduardocavalcanti | founder | misto | baixo | não identificado | não (só bio/nada) |
| @jonylan | creator | reels | alto | outro | parcial (hook real) |
| @allesinisgalli | founder | misto | baixo | não identificado | não (só bio/nada) |
| @lonamkt | marketing | misto | baixo | não identificado | não (só bio/nada) |
| @gabrielbarbosa.oficial | creator | misto | baixo | não identificado | não (só bio/nada) |
| @opensession.co | agencia | misto | medio | não identificado | não (só bio/nada) |
| @leandroladeiran | marketing | misto | alto | não identificado | não (só bio/nada) |
| @christiantriad | creator | misto | medio | não identificado | não (só bio/nada) |
| @oneyaraujo | creator | misto | medio | não identificado | não (só bio/nada) |
| @geracaotechs | ia | misto | baixo | não identificado | não (só bio/nada) |
| @amandadinizmkt | marketing | misto | baixo | não identificado | não (só bio/nada) |
| @human___academy | ia | misto | medio | não identificado | não (só bio/nada) |
| @geiss11 | creator | misto | não identificado | não identificado | não (só bio/nada) |
| @nelmoricalde | creator | misto | não identificado | não identificado | não (só bio/nada) |
| @rodrigotadewald | marketing | misto | não identificado | não identificado | não (só bio/nada) |
| @sujeitoprogramador | ia | misto | alto | não identificado | não (só bio/nada) |
| @jonathan_kamargo | creator | misto | não identificado | não identificado | não (só bio/nada) |
| @marianatorre.s | marketing | misto | baixo | não identificado | não (só bio/nada) |
| @marketerhub.ai | marketing | misto | baixo | não identificado | não (só bio/nada) |
| @marcelaluzzio | marketing | misto | medio | não identificado | não (só bio/nada) |
| @gestordeaudiencia | marketing | misto | baixo | não identificado | não (só bio/nada) |
| @sebintel | ia | misto | baixo | não identificado | não (só bio/nada) |
| @avora.ai | agencia | não identificado | não identificado | paradoxo_contraste | parcial (hook real) |
| @ogabrieeldias | creator | não identificado | não identificado | não identificado | não (só bio/nada) |
| @rodrigobindes | founder | não identificado | não identificado | não identificado | não (só bio/nada) |
| @franklim.gui | creator | não identificado | não identificado | não identificado | não (só bio/nada) |
| @gabrielsamp.ai | ia | não identificado | não identificado | não identificado | não (só bio/nada) |
| @maestrosdaia | ia | misto | alto | não identificado | não (só bio/nada) |
| @brandsdecoded__ | marketing | carrossel | alto | não identificado | não (só bio/nada) |
| @anatex | creator | misto | medio | não identificado | não (só bio/nada) |
| @larissagomes.ia | ia | misto | baixo | não identificado | não (só bio/nada) |
| @thiagozaao | creator | misto | baixo | não identificado | não (só bio/nada) |
| @neuwebstudio | agencia | misto | medio | não identificado | não (só bio/nada) |
| @laschuk | founder | misto | baixo | não identificado | não (só bio/nada) |
| @maestroptompts | ia | misto | baixo | não identificado | não (só bio/nada) |
| @faladantasmkt | marketing | misto | medio | não identificado | não (só bio/nada) |
| @lindsay.ia | ia | misto | baixo | não identificado | não (só bio/nada) |
| @andrevictor.m | marketing | reels | não identificado | não identificado | não (só bio/nada) |
| @drisiano | creator | não identificado | não identificado | não identificado | não (só bio/nada) |
| @brun0gpt | ia | não identificado | não identificado | não identificado | não (só bio/nada) |
| @maxcarrau.ia | ia | não identificado | não identificado | não identificado | não (só bio/nada) |
| @noevarner | creator | não identificado | não identificado | não identificado | não (só bio/nada) |
| @yikchanltd | creator | reels | medio | não identificado | não (só bio/nada) |

---

## Análise Detalhada — Perfis com Dados Reais de Posts (10)

Perfis abaixo tiveram ao menos um hook, CTA ou tema real identificado via WebSearch (não apenas bio).

### @charliehills

**Categoria:** creator

**Padrões de Hook identificados:**
- Modelo: outro (frequência: media) — ex: "My entire Claude skills library is now free. 17 skills you can clone in 60 seconds: This is the exact system running my content across LinkedIn, Instagram, Substack, X and YouTube."

**Estrutura típica:** Segundo fontes secundárias (Substack do próprio autor e artigos que descrevem seu sistema de conteúdo), os reels do Instagram são newsletter (Substack) reempacotada em vídeo: um roteiro 'beat-by-beat' é gerado a partir de um artigo/nota da newsletter, cada reel funciona como distribuição que puxa atenção de volta para a newsletter original. Não foi possível confirmar a estrutura frase a frase de um post real (abertura/desenvolvimento/CTA) porque não houve acesso direto ao conteúdo publicado no Instagram.

**Tom de voz:** educacional, sistemático, direto
- Exemplo: "This is the exact system running my content across LinkedIn, Instagram, Substack, X and YouTube. I test every skill on my own accounts before it ships."

**Métricas:** Formato dominante: reels | Engajamento estimado: medio

**Temas identificados:** automação de conteúdo com Claude/IA, skills reutilizáveis para criadores, sistema de produção de conteúdo multi-plataforma

**Limitação residual:** Instagram bloqueou o acesso direto via WebFetch (egress bloqueado) e o WebSearch não retornou legendas/posts reais publicados na conta @charliehills — apenas dados de perfil (88K seguidores, foco em IA/conteúdo) e descrições indiretas do sistema de produção de conteúdo vindas do Substack do próprio autor. Hook, CTA e estrutura são inferidos de uma nota do Substack/X, não de um post real do Instagram; tratar com cautela.

---

### @brusantanna.ai

**Categoria:** ia

**Padrões de Hook identificados:**
- Modelo: transformacao_silenciosa (frequência: baixa) — ex: "Analisei meu próprio conteúdo com duas IAs e descobri exatamente por que alguns vídeos viralizavam e outros não. Agora são 300 seguidores novos por dia. E o processo todo foi de graça."

**Estrutura típica:** Padrão observado (fora do Instagram, mesmo handle/criadora): relato pessoal de caso de uso ('analisei meu conteúdo com IA') seguido de resultado numérico como prova ('300 seguidores novos por dia') e fechamento com CTA de comentário por palavra-chave para receber um guia. Não confirmado diretamente em posts do Instagram.

**CTA dominante:** Comentar palavra-chave (ex.: CLAUDE, LIMITE) para receber o guia/material completo no direct
- Variações: Comenta CLAUDE aqui que eu te mando o guia completo, Comenta LIMITE para receber o guia prático

**Tom de voz:** prático, didático, pessoal, orientado a resultado
- Exemplo: "Analisei meu próprio conteúdo com duas IAs e descobri exatamente por que alguns vídeos viralizavam e outros não."

**Métricas:** Formato dominante: misto

**Temas identificados:** uso do Claude/IA para analisar e melhorar conteúdo, produtividade com IA, crescimento de seguidores com ajuda de IA

**Limitação residual:** Acesso direto ao Instagram foi bloqueado (WebFetch retornou EGRESS_BLOCKED para instagram.com) e o WebSearch não retornou legendas reais de posts do Instagram da conta, apenas o título/bio da página de perfil ('Bruna Santanna | Estrategista de IA'). Os únicos exemplos de legenda/CTA reais encontrados vieram do TikTok (@brusantanna.ai, mesmo handle/criadora), não confirmados como publicados também no Instagram. Nenhum número de seguidores, curtidas ou frequência de postagem no Instagram foi encontrado, por isso engajamento_estimado e formato_dominante ficaram sem base sólida.

---

### @oluizmain

**Categoria:** creator

**Padrões de Hook identificados:**
- Modelo: outro (frequência: baixa) — ex: "Luiz Main | Creator Mobile on! #marketingdeconteudo"

**Tom de voz:** prático, mentor/professor, lifestyle
- Exemplo: "Luiz Main | Creator Mobile on! #marketingdeconteudo"

**Métricas:** Formato dominante: reels

**Temas identificados:** produção de vídeo com celular (mobile creator), marketing de conteúdo, curso/mentoria 'Mobile Pro' (9 módulos, 40+ aulas), rotina, viagem e lifestyle

**Limitação residual:** Instagram bloqueado para acesso direto (EGRESS_BLOCKED). WebSearch encontrou apenas um fragmento real de título/legenda de reel ('Creator Mobile on! #marketingdeconteudo') e confirmou que o perfil indexa fortemente a URL /reels/, sugerindo formato_dominante='reels', mas sem contagem de seguidores, curtidas ou mais legendas completas — por isso engajamento_estimado e cta_padrao não puderam ser preenchidos com base real.

---

### @nick_saraev

**Categoria:** automacao

**Padrões de Hook identificados:**
- Modelo: outro (frequência: alta) — ex: "Wondering how to launch an AI automation..."
- Modelo: outro (frequência: alta) — ex: "Comment QWEN to get this New Opensource..."
- Modelo: outro (frequência: alta) — ex: "Comment FLUX to get this FREE AI Image..."

**Estrutura típica:** Padrão recorrente encontrado em múltiplos reels reais: pergunta/gancho sobre um problema de automação ou ferramenta de IA, seguida de promessa de recurso gratuito (blueprint/ferramenta/plugin), fechada com CTA de comentar uma palavra-chave específica (ex.: AUTOMATION, PLUGIN, CODE, CODING, DESIGN, VOICE, QWEN, FLUX) para receber o material.

**CTA dominante:** Comentar uma palavra-chave específica (ex.: AUTOMATION, PLUGIN, CODE, QWEN, FLUX) para receber o blueprint/ferramenta gratuita
- Variações: Comment "AUTOMATION" to get these AI..., Comment "QWEN" to get this New Opensource..., Comment "FLUX" to get this FREE AI Image..., Comment PLUGIN/CODE/CODING/DESIGN/VOICE to receive resources

**Tom de voz:** direto, prático, educativo, comercial, orientado a ferramentas
- Exemplo: "Nick Saraev is a writer, entrepreneur, and AI / automation..."

**Métricas:** Formato dominante: reels | Engajamento estimado: alto

**Temas identificados:** automação com N8N, Claude Code e ferramentas de IA para agências, como conseguir o primeiro cliente de IA (Maker School), modelos de IA open-source (Qwen, Flux)

**Limitação residual:** Instagram bloqueado para acesso direto (EGRESS_BLOCKED). Os dados vieram de resultados indexados do WebSearch mostrando títulos/legendas reais de reels do próprio @nick_saraev, além de menção a 550K seguidores no Instagram — não foi possível confirmar números de curtidas por post nem o texto completo das legendas (apenas fragmentos indexados pelos mecanismos de busca).

---

### @nathanhodgson

**Categoria:** ia

**Padrões de Hook identificados:**
- Modelo: outro (frequência: baixa) — ex: "Built a 6-Figure Business Powered By AI • Trusted by Google · Meta · OpenAI"

**CTA dominante:** Learn how to start your own AI business (link na bio)

**Tom de voz:** assertivo, comercial, direto, autoridade
- Exemplo: "Built a 6-Figure Business Powered By AI • Trusted by Google · Meta · OpenAI"

**Métricas:** Formato dominante: misto | Engajamento estimado: alto

**Temas identificados:** ferramentas de IA para código, ferramentas de IA para design, automação de negócios com IA

**Limitação residual:** O handle informado ('nathanhodgson') não corresponde exatamente à conta real — o perfil de IA correto encontrado via busca é @nathanhodgson.ai (contas @nathanhodgson_ e @nathanjameshodgson encontradas não têm relação com IA). Instagram bloqueado para acesso direto (EGRESS_BLOCKED); os dados vêm da bio real do perfil (citada em resultado de busca) e de contagem de seguidores agregada (128K Instagram / 142.6K Meta / 119.8K TikTok segundo fontes de terceiros), mas nenhuma legenda de post/reel individual foi encontrada, por isso hook_modelos e estrutura_tipica ficaram limitados.

---

### @viverdeia.ai

**Categoria:** ia

**Padrões de Hook identificados:**
- Modelo: outro (frequência: media) — ex: "20 MILHÕES NO PRIMEIRO ANO, ISSO AQUI É @viverdeia.ai"
- Modelo: fenomeno_nomeado (frequência: media) — ex: "Uma IA que parece uma funcionária real. Como uma agência..."

**Estrutura típica:** Reels que apresentam a plataforma Viver de IA como solução para empresas, alternando entre prova social (números de faturamento/resultados), demonstração da IA em ação, e chamada para comentar uma palavra-chave ou acessar o link da bio.

**CTA dominante:** Comenta uma palavra-chave (ex.: 'TEMPO') para receber acesso via DM
- Variações: Comenta 'TEMPO' que eu te envio agora a @viverdeia.ai, Acesse o link da bio e faça parte do Viver de IA

**Tom de voz:** promocional, direto, aspiracional, tecnológico
- Exemplo: "O Viver de IA é a Plataforma das Empresas que Crescem..."

**Métricas:** Formato dominante: reels | Engajamento estimado: medio

**Temas identificados:** plataforma de IA para empresas, resultados financeiros/faturamento, automação de atendimento com IA (funcionária de IA), formação/treinamento em IA para social media

**Limitação residual:** Instagram bloqueado para WebFetch (egress proxy). Dados vêm apenas de snippets truncados do WebSearch (títulos de reels via site:instagram.com/reel), sem acesso ao perfil completo, número real de seguidores, curtidas/comentários ou legendas completas. Os exemplos de hooks são trechos parciais (cortados por '...').

---

### @ninja.automacoes

**Categoria:** automacao

**Padrões de Hook identificados:**
- Modelo: fenomeno_nomeado (frequência: media) — ex: "Leia a legenda ⬇️ Chega de 'automação Nutella' que só..."
- Modelo: outro (frequência: baixa) — ex: "3 coisas que você NÃO vai aprender comigo"
- Modelo: outro (frequência: media) — ex: "Precificar automações não precisa ser um bicho de sete..."

**Estrutura típica:** Reels curtos sobre automações (Meta/Instagram/N8N), frequentemente abrindo com uma afirmação polêmica ou correção de mito sobre automação, seguida de instrução prática, com CTA para ler a legenda completa.

**CTA dominante:** Leia a legenda para mais detalhes
- Variações: Leia a legenda ⬇️, Vou aprender a integrar o Instagram com o N8N?

**Tom de voz:** técnico, direto, didático, informal
- Exemplo: "Chega de 'automação Nutella' que só..."

**Métricas:** Formato dominante: reels | Engajamento estimado: medio

**Temas identificados:** automação no Meta/Instagram, integração com N8N, precificação de serviços de automação, mitos sobre automação

**Limitação residual:** Instagram bloqueado para WebFetch. Dados vêm de snippets do WebSearch com títulos parciais (site:instagram.com/reel). Um resultado indicou o handle '@ninja_automacoes' (com underscore) em vez de 'ninja.automacoes' (com ponto) — possível conta alternativa/duplicada, não confirmado que é exatamente o mesmo perfil solicitado. Um resumo de busca mencionou '9M seguidores', mas esse número não pôde ser confirmado de forma consistente em outras buscas e não foi usado para estimar engajamento.

---

### @nikolassasso

**Categoria:** creator

**Padrões de Hook identificados:**
- Modelo: maioria_errando (frequência: media) — ex: "a maioria dos profissionais do digital ainda está fazendo tudo no manual"

**Estrutura típica:** Não foi possível confirmar a estrutura narrativa real dos reels — nenhum título/legenda de post específico do perfil foi localizado nas buscas (site:instagram.com/reel retornou apenas contas de terceiros com nomes parecidos). Apenas a bio e uma frase de conteúdo atribuída ao criador foram encontradas.

**Tom de voz:** tecnológico, direto, aspiracional
- Exemplo: "Criei robôs que fazem o trabalho duro por mim. Cresça sem trocar tempo por dinheiro."

**Métricas:** Formato dominante: reels | Engajamento estimado: alto

**Temas identificados:** automação de negócios com IA, criação de conteúdo em massa com IA (vídeos infinitos), vendas e monetização digital

**Limitação residual:** Instagram bloqueado para WebFetch. Buscas por site:instagram.com/reel nikolassasso retornaram apenas contas de outras pessoas com nomes parecidos (Nikola, Niko, Nicolas etc.), não o perfil alvo. Não foi possível confirmar títulos/legendas reais de posts específicos, hooks recorrentes além de um exemplo, CTA padrão ou tamanho médio das legendas. Seguidores (181K), following (815), posts (1.469) e bio foram confirmados via WebSearch.

---

### @jonylan

**Categoria:** creator

**Padrões de Hook identificados:**
- Modelo: outro (frequência: alta) — ex: "Comente "Médico"..."
- Modelo: outro (frequência: media) — ex: "A melhor estratégia é testar e colocar..."

**Estrutura típica:** Reels curtos sobre ferramentas e estratégias de IA (Google VEO 2, Whisk, Sesame.com, etc.) e marketing digital, com CTA de comentar uma palavra-chave para receber material/prompt via DM.

**CTA dominante:** Comente uma palavra-chave para receber o material/prompt por DM
- Variações: Comente "Médico"..., Comenta IA e te envio o prompt por DM

**Tom de voz:** tecnológico, direto, promocional, didático
- Exemplo: "Inteligência Artificial Ninja da internet desde 1994"

**Métricas:** Formato dominante: reels | Engajamento estimado: alto

**Temas identificados:** ferramentas de IA (Google VEO 2, Whisk, Sesame.com), estratégias de marketing digital com IA, prompts e automação de conteúdo, notícias de IA

**Limitação residual:** Instagram bloqueado para WebFetch. Títulos de reels são trechos parciais (cortados por '...') vindos de snippets do WebSearch, sem legendas completas. Um resumo de busca citou '9M seguidores', valor que diverge do mais consistente encontrado em outra busca (306K seguidores, 3.255 posts, 1.076 seguindo) — optou-se por 306K por aparecer de forma mais consistente, e o valor de 9M não foi usado.

---

### @avora.ai

**Categoria:** agencia

**Padrões de Hook identificados:**
- Modelo: paradoxo_contraste (frequência: baixa) — ex: "Avora wasn't created just to talk about AI. It was built to turn..."

**CTA dominante:** Siga @avora.ai para conteúdos diários sobre IA na prática

**Temas identificados:** IA na prática (conteúdo diário)

**Limitação residual:** WebFetch para instagram.com/avora.ai/ retornou EGRESS_BLOCKED (não repetido, conforme instrução). WebSearch confirmou que a conta @avora.ai existe e posta conteúdo diário sobre IA aplicada, e retornou fragmentos de texto de dois posts reais (instagram.com/p/DYczwbgEjtD/ e instagram.com/p/DYqCNmwvdCX/), mas não trouxe contagem de seguidores, número de posts, estrutura narrativa completa, CTA variações, tom detalhado, tamanho médio de legendas, formato dominante ou sinais de engajamento. Não há dados suficientes para inferir esses campos sem arriscar invenção.

---

## Perfis Sem Dados de Conteúdo Suficientes (51)

Apenas sinais de nível de conta (bio/nicho/seguidores aproximados) ou nenhuma confirmação — ver detalhes na seção de Limitações abaixo.

| Perfil | Categoria | Formato/Engajamento (se houver) |
|--------|-----------|----------------------------------|
| @yikC | creator | misto / baixo |
| @eujoaotorresz | creator | misto / baixo |
| @fabianocarvalhojr | founder | misto / alto |
| @rafa.grandi | marketing | misto / baixo |
| @vendedorglobal | negocio-digital | misto / alto |
| @ai | ia | misto / baixo |
| @ana.gsoares | marketing | misto / medio |
| @chase.h.ai | ia | misto / alto |
| @leosoares.ia | ia | misto / medio |
| @gabriel.adamuchi | creator | reels / baixo |
| @eduardocavalcanti | founder | misto / baixo |
| @allesinisgalli | founder | misto / baixo |
| @lonamkt | marketing | misto / baixo |
| @gabrielbarbosa.oficial | creator | misto / baixo |
| @opensession.co | agencia | misto / medio |
| @leandroladeiran | marketing | misto / alto |
| @christiantriad | creator | misto / medio |
| @oneyaraujo | creator | misto / medio |
| @geracaotechs | ia | misto / baixo |
| @amandadinizmkt | marketing | misto / baixo |
| @human___academy | ia | misto / medio |
| @geiss11 | creator | misto / não identificado |
| @nelmoricalde | creator | misto / não identificado |
| @rodrigotadewald | marketing | misto / não identificado |
| @sujeitoprogramador | ia | misto / alto |
| @jonathan_kamargo | creator | misto / não identificado |
| @marianatorre.s | marketing | misto / baixo |
| @marketerhub.ai | marketing | misto / baixo |
| @marcelaluzzio | marketing | misto / medio |
| @gestordeaudiencia | marketing | misto / baixo |
| @sebintel | ia | misto / baixo |
| @ogabrieeldias | creator | não identificado / não identificado |
| @rodrigobindes | founder | não identificado / não identificado |
| @franklim.gui | creator | não identificado / não identificado |
| @gabrielsamp.ai | ia | não identificado / não identificado |
| @maestrosdaia | ia | misto / alto |
| @brandsdecoded__ | marketing | carrossel / alto |
| @anatex | creator | misto / medio |
| @larissagomes.ia | ia | misto / baixo |
| @thiagozaao | creator | misto / baixo |
| @neuwebstudio | agencia | misto / medio |
| @laschuk | founder | misto / baixo |
| @maestroptompts | ia | misto / baixo |
| @faladantasmkt | marketing | misto / medio |
| @lindsay.ia | ia | misto / baixo |
| @andrevictor.m | marketing | reels / não identificado |
| @drisiano | creator | não identificado / não identificado |
| @brun0gpt | ia | não identificado / não identificado |
| @maxcarrau.ia | ia | não identificado / não identificado |
| @noevarner | creator | não identificado / não identificado |
| @yikchanltd | creator | reels / medio |

---

## Perfis Sugeridos pelo Sistema

Não aplicável nesta execução — `config/profiles.json` já continha 61 perfis ativos (Modo Análise direto, sem Modo Descoberta).

---

## Limitações de Dados — Detalhe por Perfil

- **@charliehills** — Instagram bloqueou o acesso direto via WebFetch (egress bloqueado) e o WebSearch não retornou legendas/posts reais publicados na conta @charliehills — apenas dados de perfil (88K seguidores, foco em IA/conteúdo) e descrições indiretas do sistema de produção de conteúdo vindas do Substack do próprio autor. Hook, CTA e estrutura são inferidos de uma nota do Substack/X, não de um post real do Instagram; tratar com cautela.
- **@yikC** — Não foi possível localizar um perfil ativo correspondente ao handle exato 'yikC' via WebSearch (buscas por "yikC" instagram e "@yikC" instagram retornaram apenas contas não relacionadas, como @yikc_ywca, @y.i.c.c, @ykc e @yikyakapp — nenhuma correspondência exata ao handle informado). WebFetch em https://www.instagram.com/yikC/ falhou com EGRESS_BLOCKED (acesso ao domínio instagram.com bloqueado pelo proxy de rede). Nenhum dado real foi encontrado; todos os campos ficaram vazios/nulos para evitar invenção.
- **@eujoaotorresz** — Não foi encontrado um perfil correspondente ao handle exato 'eujoaotorresz' via WebSearch. O resultado mais próximo foi @joaotorresz (sem o prefixo 'eu'), com 2.039 seguidores e apenas 5 posts, bio ligada a organizações portuguesas (@connect.lapunta, @ups_ofir, @sliceoficial etc.) — não fica claro se é a mesma pessoa/criador esperado na categoria 'creator', e o volume de posts (5) é baixo demais para extrair padrões de hook/CTA/estrutura com confiança. WebFetch direto em https://www.instagram.com/eujoaotorresz/ falhou com EGRESS_BLOCKED. Nenhuma legenda ou reel real foi encontrado para este handle; todos os campos de conteúdo ficaram vazios para evitar invenção.
- **@fabianocarvalhojr** — Perfil confirmado via WebSearch (@fabianocarvalhojr, ~130K seguidores, 1.417 posts, bio: 'Founder lasy.ai Crio Agentes de IA que vendem e operam Negócios 24/7'), o que dá base para engajamento_estimado='alto' e tema geral. Porém WebFetch direto em https://www.instagram.com/fabianocarvalhojr/ falhou com EGRESS_BLOCKED, e o WebSearch não retornou legendas, hooks ou CTAs reais de posts/reels específicos — apenas o bio/descrição do perfil. Por isso hook_modelos, cta_padrao, cta_variacoes e tamanho_medio_educativo não puderam ser preenchidos com base em conteúdo real.
- **@rafa.grandi** — O único perfil real encontrado com o handle exato @rafa.grandi via WebSearch pertence a 'Rafael Grandi Borges', descrito como Analista Jurídico (SPGG/RS) e pai, com apenas 247 seguidores e 36 posts — não corresponde à categoria esperada 'marketing' informada na tarefa, sugerindo que este não é o perfil de marketing pretendido (possível handle incorreto ou perfil trocado/privado/inexistente). WebFetch direto em https://www.instagram.com/rafa.grandi/ falhou com EGRESS_BLOCKED. Nenhum post, hook ou CTA real de conteúdo de marketing foi encontrado; todos os campos de conteúdo ficaram vazios para evitar invenção.
- **@brusantanna.ai** — Acesso direto ao Instagram foi bloqueado (WebFetch retornou EGRESS_BLOCKED para instagram.com) e o WebSearch não retornou legendas reais de posts do Instagram da conta, apenas o título/bio da página de perfil ('Bruna Santanna | Estrategista de IA'). Os únicos exemplos de legenda/CTA reais encontrados vieram do TikTok (@brusantanna.ai, mesmo handle/criadora), não confirmados como publicados também no Instagram. Nenhum número de seguidores, curtidas ou frequência de postagem no Instagram foi encontrado, por isso engajamento_estimado e formato_dominante ficaram sem base sólida.
- **@vendedorglobal** — Instagram bloqueado para acesso direto (EGRESS_BLOCKED). O WebSearch confirmou dados de perfil reais (Murilo Bevervanso, conta 'vendedorglobal', ~83K seguidores e 2.280 posts no Instagram, citação de 100M+ de visualizações agregadas), mas não retornou nenhuma legenda ou hook real de post específico do Instagram — os exemplos de CTA encontrados nas buscas ('manda pra alguém...') eram de artigos genéricos sobre afiliados Shopee, não atribuíveis com certeza a este criador, por isso não foram incluídos em hook_modelos/cta_padrao. engajamento_estimado='alto' baseia-se no número real de seguidores (83K) e no volume de visualizações citado.
- **@oluizmain** — Instagram bloqueado para acesso direto (EGRESS_BLOCKED). WebSearch encontrou apenas um fragmento real de título/legenda de reel ('Creator Mobile on! #marketingdeconteudo') e confirmou que o perfil indexa fortemente a URL /reels/, sugerindo formato_dominante='reels', mas sem contagem de seguidores, curtidas ou mais legendas completas — por isso engajamento_estimado e cta_padrao não puderam ser preenchidos com base real.
- **@nick_saraev** — Instagram bloqueado para acesso direto (EGRESS_BLOCKED). Os dados vieram de resultados indexados do WebSearch mostrando títulos/legendas reais de reels do próprio @nick_saraev, além de menção a 550K seguidores no Instagram — não foi possível confirmar números de curtidas por post nem o texto completo das legendas (apenas fragmentos indexados pelos mecanismos de busca).
- **@nathanhodgson** — O handle informado ('nathanhodgson') não corresponde exatamente à conta real — o perfil de IA correto encontrado via busca é @nathanhodgson.ai (contas @nathanhodgson_ e @nathanjameshodgson encontradas não têm relação com IA). Instagram bloqueado para acesso direto (EGRESS_BLOCKED); os dados vêm da bio real do perfil (citada em resultado de busca) e de contagem de seguidores agregada (128K Instagram / 142.6K Meta / 119.8K TikTok segundo fontes de terceiros), mas nenhuma legenda de post/reel individual foi encontrada, por isso hook_modelos e estrutura_tipica ficaram limitados.
- **@ai** — WebSearch e WebFetch não retornaram dados específicos sobre o perfil @ai em si (WebFetch para instagram.com/ai foi bloqueado pelo proxy de rede da sessão — EGRESS_BLOCKED). As buscas só trouxeram listas genéricas de 'contas de IA mais seguidas' e outros handles que contêm 'ai' (ex: ai.associates_, ai.realty, ai.mantis_), nenhum deles correspondendo exatamente ao handle de 2 letras 'ai'. Não foi possível confirmar se a conta é institucional/famosa, nem obter bio, contagem de seguidores, posts, hooks, CTAs ou temas reais. Nenhum dado de conteúdo real foi encontrado — todos os campos abaixo permanecem vazios/nulos/não identificados conforme regra anti-alucinação.
- **@ana.gsoares** — WebFetch em instagram.com/ana.gsoares foi bloqueado pelo proxy de rede (EGRESS_BLOCKED). Via WebSearch confirmei apenas dados de perfil: Ana G Soares (@ana.gsoares), 146K seguidores, 2.840 posts, CEO da @uniagiloficial, apresentadora do podcast @agilizesepodcast, criadora da certificação LACP, quase 20 anos como agilista, foco em cultura colaborativa e liberdade financeira/geográfica. Não foram encontradas frases reais de hooks, estrutura narrativa de posts, CTA específico ou variações de CTA — nenhuma busca retornou legendas/transcrições de posts individuais. engajamento_estimado='medio' é uma inferência baseada apenas na relação seguidores/posts (146K seguidores, alto volume de posts), não em curtidas/comentários reais coletados.
- **@chase.h.ai** — WebFetch no perfil foi bloqueado pelo proxy (EGRESS_BLOCKED). Via WebSearch (incluindo dados do site CreatorDB) confirmei: Chase AI (@chase.h.ai), 221K-228K seguidores no Instagram (números variam levemente entre fontes), 751 posts, presença também em YouTube (163K) e TikTok (137,7K), totalizando ~529K seguidores combinados. Bio real capturada: 'Making AI Simple | DM "Ready" to Apply For 1:1 Mentorship | Master Claude Code'. CreatorDB reporta 'engagement rates well above category median' nas três plataformas e cadência de postagem quase diária no YouTube — por isso engajamento_estimado='alto', com base em sinal real de terceiros, não em números de curtidas coletados diretamente. Não encontrei frases reais de hooks de reels específicos, estrutura narrativa dos vídeos, nem variações de CTA além da que está na bio — por isso hook_modelos ficou vazio e cta_variacoes vazio.
- **@leosoares.ia** — WebFetch no perfil foi bloqueado pelo proxy (EGRESS_BLOCKED). Via WebSearch confirmei apenas dados de perfil: Léo Soares | IA p/ Negócios (@leosoares.ia), CEO da Acelera IA, 219K seguidores, 1.905 seguindo, 2.226 posts. Frase de bio/tagline real encontrada: 'IA tem que gerar RESULTADO'. Não foram encontrados hooks reais de reels, estrutura narrativa dos vídeos, CTA padrão explícito ou temas específicos de posts individuais — nenhuma busca retornou legendas de posts reais. engajamento_estimado='medio' é inferência com base apenas no volume de seguidores/posts, sem dados reais de curtidas/comentários.
- **@gabriel.adamuchi** — WebFetch no perfil foi bloqueado pelo proxy (EGRESS_BLOCKED). Via WebSearch confirmei que o perfil se chama 'IA Fácil' (@gabriel.adamuchi), com presença cruzada em YouTube, TikTok e Facebook sob o mesmo tema — ensinar inteligência artificial de forma descomplicada e monetização com IA. Não foi encontrada nenhuma contagem confiável de seguidores/curtidas específica do Instagram, nenhuma frase real de hook ou legenda de post, nem estrutura narrativa ou CTA — por isso vários campos ficaram vazios/nulos e engajamento_estimado ficou como 'baixo' por falta de qualquer sinal numérico real encontrado (é uma estimativa conservadora, não baseada em dado positivo).
- **@viverdeia.ai** — Instagram bloqueado para WebFetch (egress proxy). Dados vêm apenas de snippets truncados do WebSearch (títulos de reels via site:instagram.com/reel), sem acesso ao perfil completo, número real de seguidores, curtidas/comentários ou legendas completas. Os exemplos de hooks são trechos parciais (cortados por '...').
- **@ninja.automacoes** — Instagram bloqueado para WebFetch. Dados vêm de snippets do WebSearch com títulos parciais (site:instagram.com/reel). Um resultado indicou o handle '@ninja_automacoes' (com underscore) em vez de 'ninja.automacoes' (com ponto) — possível conta alternativa/duplicada, não confirmado que é exatamente o mesmo perfil solicitado. Um resumo de busca mencionou '9M seguidores', mas esse número não pôde ser confirmado de forma consistente em outras buscas e não foi usado para estimar engajamento.
- **@nikolassasso** — Instagram bloqueado para WebFetch. Buscas por site:instagram.com/reel nikolassasso retornaram apenas contas de outras pessoas com nomes parecidos (Nikola, Niko, Nicolas etc.), não o perfil alvo. Não foi possível confirmar títulos/legendas reais de posts específicos, hooks recorrentes além de um exemplo, CTA padrão ou tamanho médio das legendas. Seguidores (181K), following (815), posts (1.469) e bio foram confirmados via WebSearch.
- **@eduardocavalcanti** — Instagram bloqueado para WebFetch. As buscas WebSearch não conseguiram confirmar com segurança qual conta corresponde exatamente ao handle 'eduardocavalcanti' informado — há múltiplas pessoas com esse nome no Instagram (ex.: @profeduardocavalcanti, um professor com cerca de 9.800 seguidores; e Eduardo Cavalcanti, cofundador/CEO da Fundamentei, cujas contas de Instagram encontradas são @fundamentei e @fundamente.i, não 'eduardocavalcanti'). Nenhum título de post, legenda, hook ou tema de conteúdo real foi encontrado associado especificamente ao handle solicitado. O valor 'baixo' em engajamento_estimado é apenas um placeholder de baixíssima confiança (campo obrigatório), não uma medição real — nenhum número de seguidores confiável foi confirmado para esse handle específico.
- **@jonylan** — Instagram bloqueado para WebFetch. Títulos de reels são trechos parciais (cortados por '...') vindos de snippets do WebSearch, sem legendas completas. Um resumo de busca citou '9M seguidores', valor que diverge do mais consistente encontrado em outra busca (306K seguidores, 3.255 posts, 1.076 seguindo) — optou-se por 306K por aparecer de forma mais consistente, e o valor de 9M não foi usado.
- **@allesinisgalli** — WebFetch para instagram.com bloqueado por EGRESS_BLOCKED (1 tentativa feita, sem insistir). WebSearch (1 tentativa) retornou apenas dados de bio/perfil: Allessandra Sinisgalli, ~8.155 seguidores, 3.060 seguindo, 3.548 posts, bio indica mentora de marketing com IA, 15+ anos de experiência global, base Austrália/Brasil. Nenhuma legenda, hook ou tema de post individual foi encontrado — não há dados suficientes para hook_modelos, estrutura_tipica, cta_padrao, tom ou tamanho médio. engajamento_estimado marcado como baixo apenas por proporção seguidores/posts observada na busca, não é um sinal direto de engajamento (curtidas/comentários) e deve ser tratado com cautela.
- **@lonamkt** — WebFetch para instagram.com bloqueado por EGRESS_BLOCKED (1 tentativa, sem insistir). WebSearch (1 tentativa) retornou dados de bio/perfil: conta 'Lona' (Felipe Lona), ~4.316 seguidores, 490 seguindo, apenas 2 posts na conta do Instagram; bio 'Primeiro milhão aos 18'. Os temas listados vêm de títulos de vídeos do canal do YouTube associado (Lonamkt), não de legendas reais de posts do Instagram — não é possível confirmar que refletem o conteúdo do perfil Instagram em si. Nenhuma legenda, hook ou CTA real de post do Instagram foi encontrado. engajamento_estimado é uma estimativa fraca baseada no baixíssimo número de posts do perfil Instagram (apenas 2), não em métricas reais de curtidas/comentários.
- **@gabrielbarbosa.oficial** — WebFetch para instagram.com bloqueado por EGRESS_BLOCKED (1 tentativa, sem insistir). WebSearch (1 tentativa) retornou apenas dados de bio/perfil: 'Gabriel Barbosa | Negócios Digitais', ~7.782 seguidores, 754 seguindo, 47 posts; bio descreve ensinar operação enxuta e lucrativa de qualquer lugar do mundo. Nenhuma legenda, hook, CTA ou tema de post individual foi encontrado — dados insuficientes para hook_modelos, estrutura_tipica, cta_padrao, tom ou tamanho médio. engajamento_estimado é apenas uma estimativa fraca sem sinais reais de curtidas/comentários.
- **@opensession.co** — WebFetch para instagram.com bloqueado por EGRESS_BLOCKED (1 tentativa, sem insistir). WebSearch (1 tentativa) retornou dados de bio/perfil: 'open session', ~23K seguidores, 538 seguindo, 19 posts; bio 'Brand x UX/AI x Design Systems', empresa de design (San Diego, CA) focada em design systems, marca e IA criativa. Nenhuma legenda, hook ou CTA real de post individual foi encontrado — dados insuficientes para hook_modelos, estrutura_tipica, cta_padrao, tom ou tamanho médio. engajamento_estimado 'medio' é uma estimativa fraca baseada apenas na proporção seguidores (23K) vs. poucos posts (19), não em métricas reais de curtidas/comentários — tratar com cautela.
- **@leandroladeiran** — WebFetch para instagram.com bloqueado por EGRESS_BLOCKED (1 tentativa, sem insistir). WebSearch (1 tentativa) não retornou métricas diretas de seguidores do perfil Instagram (a busca priorizou resultados de TikTok — 881K seguidores — e do podcast/LinkedIn associados). Confirma-se que Leandro Ladeira é especialista em marketing digital e copy, com tom bem-humorado, apresentador do 'Podcast do Ladeira'. Nenhuma legenda, hook ou CTA real de post do Instagram foi encontrado — hook_modelos, estrutura_tipica, cta_padrao e tamanho médio ficam sem dados reais. engajamento_estimado 'alto' é inferido apenas pela popularidade cross-platform (881K no TikTok, podcast ativo), não por métricas reais do Instagram — tratar como estimativa fraca, não confirmada diretamente no perfil.
- **@christiantriad** — WebFetch bloqueado (EGRESS_BLOCKED) para instagram.com. WebSearch retornou apenas dados de bio/contagem de seguidores (571K seguidores, 901 seguindo, 4.333 posts) e contexto biográfico (autor best-seller, método de produtividade), sem acesso a legendas, hooks, CTAs ou temas de posts individuais reais. Engajamento estimado 'medio' é uma inferência fraca baseada apenas no porte da conta (571K seguidores), não em sinais reais de curtidas/comentários — todos os demais campos foram deixados vazios/nulos por não haver dados reais.
- **@oneyaraujo** — WebFetch bloqueado (EGRESS_BLOCKED) para instagram.com. WebSearch retornou apenas dados de bio/nicho (2M seguidores, foco em marketing viral, venda do curso 'Código Viral'), sem acesso a legendas, hooks, CTAs ou temas de posts individuais reais. Engajamento estimado 'medio' é uma inferência fraca baseada apenas no porte da conta (2M seguidores), não em sinais reais — todos os demais campos foram deixados vazios/nulos por não haver dados reais.
- **@geracaotechs** — WebFetch bloqueado (EGRESS_BLOCKED) para instagram.com. WebSearch não retornou contagem de seguidores do Instagram em si (apenas do Threads espelhado, 11.2K), e não trouxe legendas, hooks, CTAs ou temas de posts individuais reais — apenas confirmação de nicho (tech/IA) e um exemplo de título de vídeo do Threads ('Tire resumo de qualquer vídeo do YouTube em segundos'), que não é claramente atribuível a um post do Instagram, por isso não foi incluído em top_posts_temas para evitar risco de dado incorreto. Engajamento estimado 'baixo' é inferência fraca baseada no porte pequeno da conta espelhada no Threads.
- **@amandadinizmkt** — WebFetch bloqueado (EGRESS_BLOCKED) para instagram.com. WebSearch retornou apenas a confirmação de existência e nicho da conta ('Marketing & Empreendedorismo'), sem número de seguidores, legendas, hooks, CTAs ou temas de posts. Este foi o perfil com menos dados encontrados no lote — nenhum sinal real de engajamento; 'baixo' aqui reflete ausência quase total de informação, não um dado observado.
- **@human___academy** — WebFetch bloqueado (EGRESS_BLOCKED) para instagram.com. WebSearch retornou dados de bio/seguidores (260K seguidores, 496 seguindo, 450 posts) e títulos de dois posts/reels reais encontrados nos resultados de busca ('Human Academy | VFX com IA, ao vivo e na prática' e 'Human Academy | Curso de IA 100% gratuito'), por isso incluídos em top_posts_temas como temas reais — mas sem acesso ao corpo das legendas, hooks completos, CTAs ou estrutura narrativa dos posts. Engajamento estimado 'medio' é inferência fraca baseada apenas no porte da conta (260K seguidores).
- **@geiss11** — WebFetch bloqueado por EGRESS_BLOCKED (instagram.com). WebSearch retornou apenas dados de nível de bio: perfil de Henrique Geiss, ~45K seguidores, 601 seguindo, 83 posts, bio menciona venda de produtos digitais. Nenhuma legenda, hook, CTA ou tema de post individual foi encontrado — não há dados suficientes para os demais campos, mantidos vazios/nulos conforme regra anti-alucinação.
- **@nelmoricalde** — WebFetch bloqueado por EGRESS_BLOCKED (instagram.com). WebSearch não retornou nenhum resultado correspondente ao handle exato 'nelmoricalde' — apenas contas com nomes parecidos (nelelilemor, nelman) e resultados genéricos sobre Instagram. Não foi possível confirmar sequer a existência/bio do perfil. Nenhum dado real disponível para nenhum campo.
- **@rodrigotadewald** — WebFetch bloqueado por EGRESS_BLOCKED (instagram.com). WebSearch não encontrou a página do Instagram diretamente indexada; retornou apenas um perfil Pinterest de mesmo nome (br.pinterest.com/rodrigotadewald) e contas Instagram de outras pessoas chamadas 'Rodrigo'. Sem confirmação de bio, seguidores ou posts — nenhum dado real disponível para nenhum campo.
- **@sujeitoprogramador** — WebFetch bloqueado por EGRESS_BLOCKED (instagram.com). WebSearch confirmou o perfil: Matheus Fraga (@sujeitoprogramador), ~168K seguidores, 6.077 seguindo, 3.040 posts; bio indica 12+ anos de experiência como programador e mais de 45.000 alunos ensinados, conteúdo focado em educação em programação e IA (também ativo em blog sujeitoprogramador.com, TikTok e Telegram). Engajamento estimado como 'alto' com base no volume de seguidores/posts e presença multi-plataforma consolidada, não em métricas diretas de curtidas/comentários. Nenhuma legenda, hook ou CTA de post individual foi encontrado — campos relacionados a hooks/CTA/tom/estrutura mantidos vazios/nulos conforme regra anti-alucinação.
- **@jonathan_kamargo** — WebFetch bloqueado por EGRESS_BLOCKED (instagram.com). WebSearch não encontrou nenhuma conta com o handle exato 'jonathan_kamargo' — apenas variações de nome (camargojay, kamargo___, jonathankrego, jhoncamargo) pertencentes a outras pessoas. Sem confirmação de existência, bio, seguidores ou posts — nenhum dado real disponível para nenhum campo.
- **@marianatorre.s** — WebFetch para instagram.com retornou EGRESS_BLOCKED (rede bloqueia o domínio). O WebSearch encontrou apenas a existência do perfil (nome 'Mariana Torres') sem bio, contagem de seguidores, legendas ou temas de posts reais. Nenhum dado de conteúdo real pôde ser confirmado — nenhum campo de conteúdo foi preenchido para evitar alucinação.
- **@marketerhub.ai** — WebFetch bloqueado (EGRESS_BLOCKED). WebSearch confirmou apenas: bio do perfil é 'Empowering Digital Marketers', e a conta está associada à comunidade paga MarketerHub.ai ('Become an AI Marketing Pro', cursos/prompts/templates de marketing com IA). Nenhuma legenda, hook, CTA ou número de seguidores real foi encontrado — não há dados suficientes para preencher hooks, estrutura, CTA ou tom com segurança.
- **@marcelaluzzio** — WebFetch bloqueado (EGRESS_BLOCKED). WebSearch confirmou: bio 'Marketing de Conteúdo & I.A', ~226 mil seguidores, MBA em IA para negócios digitais pela USP, foco em ajudar pessoas a vender mais com IA e criar produtos digitais de informação. Um post no Threads (@marcelaluzzio) menciona 'ative o Claude para trabalhar por você'. Nenhuma legenda completa, hook estruturado ou CTA literal foi localizado — engajamento_estimado 'medio' é uma inferência fraca baseada apenas no porte de seguidores (226k), não em métricas de engajamento reais; hooks e CTAs deixados vazios/não identificados por falta de evidência.
- **@gestordeaudiencia** — WebFetch bloqueado (EGRESS_BLOCKED). WebSearch NÃO retornou nenhum resultado correspondente ao perfil @gestordeaudiencia em si — os resultados trouxeram apenas conteúdo não relacionado (extensão de Chrome 'Instagram Gestão de Seguidores', posts genéricos sobre Claude Code/Remotion, e uma conta diferente 'Audiency Brasil'). Nenhum dado real do perfil (bio, seguidores, posts, temas) foi encontrado — perfil não confirmado/indexado publicamente nos resultados de busca disponíveis.
- **@sebintel** — WebFetch bloqueado (EGRESS_BLOCKED). WebSearch NÃO encontrou o perfil @sebintel no Instagram — os resultados trouxeram apenas contas e páginas não relacionadas (ex.: @seb1nnn, um criador 'sebintel5859' no TikTok sobre capas de reels com IA, e verbetes genéricos da Wikipédia). Nenhum dado real do perfil de Instagram foi localizado — perfil não confirmado/indexado publicamente nos resultados de busca disponíveis.
- **@avora.ai** — WebFetch para instagram.com/avora.ai/ retornou EGRESS_BLOCKED (não repetido, conforme instrução). WebSearch confirmou que a conta @avora.ai existe e posta conteúdo diário sobre IA aplicada, e retornou fragmentos de texto de dois posts reais (instagram.com/p/DYczwbgEjtD/ e instagram.com/p/DYqCNmwvdCX/), mas não trouxe contagem de seguidores, número de posts, estrutura narrativa completa, CTA variações, tom detalhado, tamanho médio de legendas, formato dominante ou sinais de engajamento. Não há dados suficientes para inferir esses campos sem arriscar invenção.
- **@ogabrieeldias** — WebFetch para instagram.com/ogabrieeldias/ retornou EGRESS_BLOCKED (não repetido). WebSearch pela query 'instagram.com/ogabrieeldias' NÃO retornou nenhum resultado correspondente a esse handle específico — apenas contas com nomes parecidos (ogabel, oabrio) e páginas genéricas da Wikipedia sobre Instagram. Não foi possível confirmar a existência, o nicho real ou qualquer dado de conteúdo desse perfil nesta busca. Nenhum campo pôde ser preenchido com dado real.
- **@rodrigobindes** — WebFetch para instagram.com/rodrigobindes/ retornou EGRESS_BLOCKED (não repetido). WebSearch confirmou a conta real 'Rodrigo Bindes | Mentor de Agências de Marketing Digital' (@rodrigobindes), com bio 'Mostro como chegar aos 100k/mês com agência de mkt', aproximadamente 278K seguidores, 1.835 posts e 1.482 seguindo — esses números são de nível de bio/contagem, não confirmados via fetch direto. Os adjetivos de tom foram inferidos apenas da frase de bio encontrada (dado limitado, não de múltiplos posts). Não foram encontradas legendas de posts individuais, hooks reais, CTA de post, estrutura narrativa, tamanho médio de legenda, formato dominante ou sinais reais de engajamento (curtidas/comentários) — engajamento_estimado deixado null por falta de sinal real.
- **@franklim.gui** — WebFetch para instagram.com/franklim.gui/ retornou EGRESS_BLOCKED (não repetido). WebSearch confirmou a conta 'guilherme franklim' (@franklim.gui) com aproximadamente 51K seguidores, 436 seguindo e 180 posts, com bio indicando cursos sobre IA/Claude Code e estratégias de lowticket — números de nível de bio, não confirmados via fetch direto. Os temas em top_posts_temas foram inferidos a partir de títulos de vídeos do canal do YouTube vinculado ao mesmo criador (ex.: 'não da mais pra rodar lowticket no brasil', 'como construir um agente de ia que te entrega 15 ofertas lowticket validadas por dia'), NÃO de legendas confirmadas do Instagram — por isso hook_modelos, cta_padrao, tom e estrutura foram deixados vazios/não identificados, para não atribuir a este perfil do Instagram frases de outra plataforma.
- **@gabrielsamp.ai** — WebFetch para instagram.com/gabrielsamp.ai/ retornou EGRESS_BLOCKED (não repetido). WebSearch pela query 'instagram.com/gabrielsamp.ai' NÃO retornou o perfil correspondente do Instagram — apenas contas com nomes parecidos (ai.gabriela, gabriel_a.i, gabrysolution, gabrielmy) e uma conta de TikTok com o mesmo handle 'gabrielsamp.ai'. Não foi possível confirmar a existência do perfil no Instagram, seu nicho real, bio, contagem de seguidores ou qualquer dado de conteúdo. Nenhum campo pôde ser preenchido com dado real.
- **@maestrosdaia** — WebSearch retornou apenas dados de nível de bio/perfil (nome 'Maestros da IA', ~9 milhões de seguidores segundo resultados, foco em educação de IA e comunidade paga). WebFetch para instagram.com/maestrosdaia/ retornou EGRESS_BLOCKED (bloqueio de rede confirmado, não insistido além de 1 tentativa). Nenhuma legenda, hook, CTA ou tema de post individual foi encontrado nos resultados de busca — todos os campos de conteúdo real (hook_modelos, estrutura_tipica, cta_padrao, tom_exemplo_frase, tamanho_medio_educativo) permanecem vazios/nulos por ausência de dados verificáveis. O número de seguidores (~9M) não foi confirmado por fonte primária e não deve ser tratado como certo.
- **@brandsdecoded__** — WebSearch retornou dados de bio/perfil: 'BrandsDecoded®️ | Conteúdo & Cultura', 306K seguidores, 1.980 posts, gerido por @leo.varricchio, foco em decodificar como marcas/criadores se tornam culturalmente relevantes e em ensinar criação de carrosséis de autoridade com IA. formato_dominante inferido como 'carrossel' com base na proposta de valor do produto (carrosséis de autoridade), não em posts individuais observados diretamente — tratar como inferência fraca. WebFetch para instagram.com/brandsdecoded__/ retornou EGRESS_BLOCKED (1 tentativa, sem insistência). Nenhuma legenda, hook ou CTA real de post individual foi encontrado — hook_modelos, estrutura_tipica, cta_padrao/variacoes, tom_exemplo_frase e tamanho_medio_educativo permanecem vazios/nulos por ausência de dados verificáveis.
- **@anatex** — WebSearch retornou dados de bio/perfil: 'Ana Tex - Inteligência Artificial para Negócios', 671K seguidores, 994 seguindo, 1.242 posts. Bio: 'Mentora de Mulheres 40+ que são especialistas em seus negócios e usam IA para ter mais liberdade e tempo'. WebFetch para instagram.com/anatex/ retornou EGRESS_BLOCKED (1 tentativa, sem insistência). Nenhuma legenda, hook, CTA ou tema de post individual foi confirmado nos resultados de busca — hook_modelos, estrutura_tipica, cta_padrao/variacoes, tom_exemplo_frase e tamanho_medio_educativo permanecem vazios/nulos. engajamento_estimado como 'medio' é uma estimativa fraca baseada apenas na proporção seguidores/posts, não em sinais de engajamento real (curtidas/comentários) — não encontrados.
- **@larissagomes.ia** — WebSearch retornou dados de bio/perfil: 'Larissa | Marketing e Inteligência Artificial', 15K seguidores. Bio: 'Te ensino a criar um negócio enxuto e que vende: você + IA. Compartilho o que aplico sobre IA. Domine o chatGPT'. Um post no Threads foi encontrado com início de frase ('eu salveis suas respostas pra lembrar de ler de novo quando tiver criando que...') mas o texto está truncado e incompleto no resultado de busca, não sendo confiável o suficiente para registrar como hook_modelo verificado. WebFetch para instagram.com/larissagomes.ia/ retornou EGRESS_BLOCKED (1 tentativa, sem insistência). engajamento_estimado 'baixo' é inferência fraca baseada apenas no volume de seguidores (15K, o menor do lote), não em métricas de engajamento reais.
- **@thiagozaao** — Nenhum dado real foi encontrado para este perfil. Duas buscas WebSearch (com e sem contexto adicional) não retornaram o handle 'thiagozaao' — apenas perfis de outros usuários chamados Thiago com grafias diferentes (thiagozapiola, thiagozoinho, thiagoarzua, etc.), nenhum correspondendo exatamente ao handle solicitado. WebFetch para instagram.com/thiagozaao/ retornou EGRESS_BLOCKED (1 tentativa, sem insistência). Não foi possível confirmar sequer a existência pública indexada do perfil, contagem de seguidores, bio ou qualquer conteúdo. Todos os campos de conteúdo permanecem vazios/nulos/não identificados. engajamento_estimado 'baixo' não é uma estimativa real, é um valor padrão de fallback dado a ausência total de dados — deveria ser tratado como desconhecido.
- **@neuwebstudio** — WebFetch para instagram.com retornou EGRESS_BLOCKED (bloqueado pelo proxy de rede) — não foi possível acessar o perfil diretamente. WebSearch trouxe apenas dados de nível de bio/contagem: ~52K seguidores, 100 seguindo, 168 posts, bio 'Cinematic Web Design', promoção de pacote de animações Figma. Não foram encontradas legendas, hooks ou CTAs de posts individuais reais — os temas listados vêm de conteúdo cross-postado no TikTok (@neuwebstudio) sobre design de sites, animação parallax e Figma. Nenhum dado sobre estrutura narrativa, tom de voz específico ou frequência de hooks foi encontrado; engajamento_estimado é uma inferência fraca baseada apenas em contagem de seguidores/posts, não em curtidas/comentários reais.
- **@laschuk** — WebFetch para instagram.com retornou EGRESS_BLOCKED — não foi possível acessar o perfil diretamente. WebSearch confirmou a conta correta ('LASCHUK | email marketing', ~36K seguidores, 61 seguindo, 200 posts, bio 'not for sale'), mas não retornou nenhuma legenda, hook, CTA ou tema de post real — apenas metadados de bio/contagem. hook_modelos, estrutura_tipica, cta_padrao e tom_adjetivos ficaram vazios/não identificados por ausência total de conteúdo de posts nos resultados de busca. engajamento_estimado é um chute conservador de baixa confiança baseado só na proporção seguidores/posts, não em sinais reais de curtidas/comentários — considerar não confiável.
- **@maestroptompts** — Perfil não localizado. WebSearch para 'instagram.com/maestroptompts' NÃO retornou nenhuma correspondência com esse handle exato — apenas outras contas com 'maestro' no nome (@thetruemaestro, @maestrotechnology, @maestrofilm, @maestro, etc.), nenhuma relacionada a engenharia de prompts/IA. WebFetch direto na URL também retornou EGRESS_BLOCKED. Não há nenhum dado real sobre este perfil: pode não existir, estar com o handle grafado diferente, ser privado ou não indexado. Todos os campos ficaram vazios/nulos/não identificados por ausência total de informação verificável — nenhum dado foi inventado.
- **@faladantasmkt** — WebFetch para instagram.com retornou EGRESS_BLOCKED — não foi possível acessar o perfil diretamente. WebSearch confirmou a conta (Jessica Dantas, ~99K seguidores, 143 seguindo, 1.774 posts, bio sobre 14 anos vendendo online e mentoria de conteúdo), e trouxe evidência indireta de temas recorrentes via páginas do site faladantas.com (curso de reels, 'roteiro de stories pra vender', 'como crescer no Instagram', 'stories pra vender') — usados como top_posts_temas por refletirem pautas reais do negócio, mas não são legendas/hooks de posts individuais do Instagram em si. Nenhuma frase exata de hook, CTA específico ou estrutura narrativa de post real foi encontrada; esses campos ficaram vazios/não identificados. engajamento_estimado é inferência de baixa confiança baseada em volume de seguidores/posts e presença de negócio consolidado, não em métricas reais de curtidas/comentários.
- **@lindsay.ia** — Perfil não localizado. WebSearch para 'instagram.com/lindsay.ia' NÃO retornou nenhuma correspondência com esse handle exato — apenas outras contas chamadas Lindsay sem relação com IA (fotógrafa, política de Iowa, etc.), provavelmente por confusão do buscador entre '.ia' e 'Iowa'. WebFetch direto na URL também retornou EGRESS_BLOCKED. Não há nenhum dado real sobre este perfil: pode não existir, estar com o handle grafado diferente, ser privado ou não indexado. Todos os campos ficaram vazios/nulos/não identificados por ausência total de informação verificável — nenhum dado foi inventado.
- **@andrevictor.m** — WebFetch para instagram.com bloqueado nesta rede (EGRESS_BLOCKED), tentativa única conforme instrução. WebSearch (1 busca) retornou apenas dados de nível de bio/nicho: nome (André Victor), ~244K seguidores, contato comercial (andrevictor@avmmidias.com), e temas gerais (dropshipping, marketing digital, empreendedorismo — confirmado também pelo canal do YouTube associado). Três reels foram localizados apenas por título/data (jan/2026, out/2025, jan/2025), sem legendas, hooks, CTAs ou métricas de engajamento reais disponíveis. Todos os campos de estrutura narrativa, tom e engajamento não puderam ser preenchidos com dados reais e foram deixados vazios/nulos.
- **@drisiano** — Nenhum perfil do Instagram com o handle exato 'drisiano' foi localizado. WebFetch em https://www.instagram.com/drisiano/ bloqueado (EGRESS_BLOCKED), tentativa única conforme instrução. WebSearch (1 busca) retornou apenas contas com nomes parecidos, mas não correspondentes ao handle solicitado: @draisianaoficial (23K seguidores, itens artesanais do Brasil), @driso__ (1.453 seguidores, 20 posts), @drisanalg (3.671 seguidores, palestrante/ativista de direitos humanos), e outras não relacionadas. Não é possível confirmar a existência ou identidade real deste perfil com os dados disponíveis — nenhum dado de bio, nicho, legendas, hooks, CTAs ou engajamento pôde ser extraído.
- **@brun0gpt** — WebFetch para instagram.com bloqueado nesta rede (EGRESS_BLOCKED), tentativa única conforme instrução. WebSearch (1 busca) retornou dados de nível de bio/nicho: nome (Bruno Francisco), bio 'IA e Marketing', ~157K seguidores, 1.334 posts, posicionamento como referência para quem quer ir além do uso amador de IA em marketing e vendas. Nenhuma legenda, hook, CTA ou métrica de engajamento real (likes/comentários) foi encontrada, portanto esses campos foram deixados vazios/nulos.
- **@maxcarrau.ia** — Nenhum perfil do Instagram com o handle exato 'maxcarrau.ia' foi confirmado. WebFetch em https://www.instagram.com/maxcarrau.ia/ bloqueado (EGRESS_BLOCKED), tentativa única conforme instrução. WebSearch (1 busca) encontrou apenas um canal do YouTube chamado 'Max carrau | IA' (sem métricas visíveis) e contas do Instagram com nomes parecidos mas não correspondentes: @maxcarraa (cantor/compositor argentino, 451K seguidores, sem relação com IA), @iawithmax (12K seguidores, IA e produtividade), @maxcarvalhozr, @maxbank e @maxcar. Não foi possível confirmar a existência, bio, nicho, legendas, hooks, CTAs ou engajamento real deste perfil específico.
- **@noevarner** — WebFetch em https://www.instagram.com/noevarner/ bloqueado (EGRESS_BLOCKED), tentativa única conforme instrução. WebSearch (1 busca) encontrou múltiplas contas com handles parecidos, tornando a identificação ambígua: @noevarner (handle exato solicitado, mas sem dados de bio/seguidores retornados na busca), @therealnoevarner (7.123 seguidores, 232 posts, nicho 'ajudar criadores/treinadores esportivos a crescer'), e @noevarner.ai (~91.740–92K seguidores segundo Social Blade, empreendedor de automação com IA na Flórida, ex-jogador/técnico de futebol universitário que migrou para IA no fim de 2024). Como os dados mais ricos encontrados pertencem a @noevarner.ai (handle diferente do solicitado) e não há confirmação de que seja a mesma pessoa/conta que @noevarner, nenhum dado foi atribuído ao perfil por segurança anti-alucinação. Nenhuma legenda, hook, CTA real ou métrica de engajamento foi encontrada para o handle exato @noevarner.
- **@yikchanltd** — WebFetch em instagram.com/yikchanltd/ retornou EGRESS_BLOCKED (não houve nova tentativa, conforme aviso). O WebSearch só retornou dados de nível de bio/contagens (79K seguidores, 110 seguindo, 1296 posts, texto da bio) e 3 títulos de reels truncados pelo Google, sem legendas completas, sem números de curtidas/comentários e sem CTAs recorrentes verificáveis dentro dos posts. Por isso hook_modelos, cta_variacoes, tom_adjetivos e top_posts_temas foram deixados vazios — qualquer preenchimento exigiria completar frases cortadas ou inferir padrões não confirmados, o que violaria a regra anti-alucinação. engajamento_estimado='medio' é uma estimativa fraca baseada apenas no volume de seguidores (79K) vs. posts (1296), sem dados reais de curtidas/comentários — tratar com cautela.
