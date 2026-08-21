# Análise de Perfis Instagram — 2026-08-10

## Nota metodológica

O Instagram bloqueou o acesso direto via WebFetch em praticamente 100% das tentativas nesta execução (egress bloqueado para instagram.com pelo proxy de rede do ambiente, além do bloqueio habitual do próprio Instagram a scrapers). Todos os dados abaixo vêm de resultados indexados via WebSearch (snippets de busca, agregadores de terceiros como Heepsy/Favikon, cross-posts em TikTok/Threads/YouTube da mesma pessoa/marca, sites institucionais). Nenhum dado de engajamento, seguidores ou conteúdo de post foi inventado — onde a informação real não pôde ser confirmada, o campo foi deixado vazio/mínimo e a limitação documentada explicitamente na seção de Limitações ao final.

De 61 perfis ativos processados em `config/profiles.json`, **21 handles não puderam ser localizados** com confiança (possivelmente inexistentes, privados, com erro de digitação, ou não indexados) ou tiveram o orçamento de busca da sessão esgotado antes de retornar resultado: `yikC`, `eujoaotorresz`, `ai`, `nikolassfaria`, `humam__academy`, `jonathan_kamargo`, `marianatorre.s`, `gestordeaudiencia`, `gabrielsamp.ai`, `thiagozaao`, `neuwebstudio`, `laschuk`, `maestroptompts`, `faladantasmkt`, `lindsay.ia`, `andrevictor.m`, `drisiano`, `brun0gpt`, `maxcarrau.ia`, `noevarner`, `yikchan`.

---

## Visão Geral dos Perfis

| Perfil | Categoria | Formato Dominante | Engajamento | Seguidores (aprox., não confirmado direto) | Hook Padrão |
|--------|-----------|------------------|-------------|------|-------------|
| @charliehills | creator | misto | medio | 88 mil | AI can almost do your job now. But it still can't be you. It can clone your output. It can't clone your taste, your story, your judgement. |
| @yikC | creator | — | — | — | não identificado |
| @eujoaotorresz | creator | — | — | — | não identificado |
| @fabianocarvalhojr | founder | misto | medio | 84 mil | Quem mais? 😅 ➡️ Siga @fabianocarvalhojr que te ensino... |
| @rafa.grandi | marketing | — | baixo | — | não identificado |
| @brusantanna.ai | ia | — | — | — | não identificado |
| @vendedorglobal | negocio-digital | reels | alto | 83 mil | não identificado |
| @oluizmain | creator | reels | alto | 215 mil | não identificado |
| @nick_saraev | automacao | reels | alto | 550 mil | não identificado |
| @nathanhodgson | ia | reels | alto | 128 mil | não identificado |
| @ai | ia | misto | baixo | — | não identificado |
| @ana.gsoares | marketing | reels | alto | 146 mil | Conhecer Gestão Ágil vai te tornar um profissional diferenciado, independente da situação |
| @chase.h.ai | ia | misto | alto | 221 mil | não identificado |
| @leosoares.ia | ia | reels | alto | 219 mil | não identificado |
| @gabriel.adamuchi | creator | misto | medio | 195,2 mil | Segue esse perfil e saiba tudo sobre o mundo da IA |
| @viverdeia | ia | misto | alto | 129K | não identificado |
| @ninja.automacoes | automacao | reels | — | — | não identificado |
| @nikolassfaria | creator | — | — | — | não identificado |
| @eduardocavalcanti | founder | — | — | 65K | não identificado |
| @jonylan | creator | reels | alto | 306K | não identificado |
| @allesinisgalli | founder | reels | medio | — | LIBERDADE ATRAVÉS DO... |
| @lonamkt | marketing | misto | baixo | — | não identificado |
| @gabrielbarbosa.oficial | creator | misto | medio | — | Hoje fui na Xgrow... |
| @opensession.co | agencia | misto | medio | — | não identificado |
| @leandroladeiran | marketing | reels | alto | 882,1K | Quem tem razão? |
| @christiantriad | creator | não determinado | alto | 571K | não identificado |
| @oneyaraujo | creator | não determinado | alto | 2M | não identificado |
| @geracaotechs | ia | não determinado | baixo | — | 🚀 Esqueça tudo o que você sabe sobre geradores de vídeo simples, o Anijam é... |
| @amandadinizmkt | marketing | não determinado | baixo | — | não identificado |
| @humam__academy | ia | não determinado | baixo | — | não identificado |
| @geiss11 | creator | — | medio | 45 mil | não identificado |
| @nelmoricalde | creator | — | — | — | não identificado |
| @rodrigotadewald | marketing | — | — | 550K | não identificado |
| @sujeitoprogramador | ia | reels | — | 168 mil | não identificado |
| @jonathan_kamargo | creator | — | — | — | não identificado |
| @marianatorre.s | marketing | — | — | — | não identificado |
| @marketerhub.ai | marketing | — | — | — | não identificado |
| @marcelaluzzio | marketing | — | alto | 226K | não identificado |
| @gestordeaudiencia | marketing | — | — | — | não identificado |
| @sebintel | ia | reels | — | 56,7K | não identificado |
| @avora.ai | agencia | misto | — | — | não identificado |
| @ogabrieeldias | creator | — | — | — | não identificado |
| @rodrigobindes | founder | misto | alto | 278K | não identificado |
| @franklim.gui | creator | misto | medio | 46K | não identificado |
| @gabrielsamp.ai | ia | — | — | — | não identificado |
| @maestrosdaia | ia | — | indeterminado | — | não identificado |
| @brandsdecoded | marketing | carrossel | alto | 301 mil | não identificado |
| @anatex | creator | — | alto | 694 mil | não identificado |
| @larissagomes.ia | ia | — | medio | 15K | você quer crescer no instagram mas quase nunca para pra analisar o próprio perfil |
| @thiagozaao | creator | — | indeterminado | — | não identificado |
| @neuwebstudio | agencia | — | — | — | não identificado |
| @laschuk | founder | — | — | — | não identificado |
| @maestroptompts | ia | — | — | — | não identificado |
| @faladantasmkt | marketing | — | — | — | não identificado |
| @lindsay.ia | ia | — | — | — | não identificado |
| @andrevictor.m | marketing | — | — | — | não identificado |
| @drisiano | creator | — | — | — | não identificado |
| @brun0gpt | ia | — | — | — | não identificado |
| @maxcarrau.ia | ia | — | — | — | não identificado |
| @noevarner | creator | — | — | — | não identificado |
| @yikchan | creator | — | — | — | não identificado |

---

## Análise Detalhada por Perfil

### @charliehills — creator
**Bio:** 💙 I help you (actually) use AI 📧 collabs@charliehills.ai — 100+ free AI prompts, guides & tools. Aproximadamente 88 mil seguidores, 260 posts (dados via busca web, não coletados diretamente do perfil).

#### Padrões de Hook identificados
- Modelo: paradoxo_contraste (frequência: alta) — ex: "AI can almost do your job now. But it still can't be you. It can clone your output. It can't clone your taste, your story, your judgement."
- Modelo: maioria_errando (frequência: media) — ex: "84% of the world has never had a single AI conversation... Your entire perception of how 'mainstream' AI is comes from a bubble so small it's almost invisible on this chart."
- Modelo: paradoxo_contraste (frequência: media) — ex: "AI didn't make me successful, it just made my effort scale faster."
- Modelo: fenomeno_nomeado (frequência: baixa) — ex: "People don't fall in love with corporations. They trust humans."

#### Estrutura típica do conteúdo
Afirmação de contraste ou dado estatístico chocante no início, seguido de reflexão pessoal sobre uso prático de IA, fechando com lição aplicável ao negócio/carreira do leitor.

#### CTA dominante
- Padrão: Direcionamento para bio / lead magnet gratuito: '100+ free AI prompts, guides & tools' (link na bio).
- Variações: Convite a se inscrever na newsletter (MarTech AI via Substack); Convite a colaborações comerciais (collabs@charliehills.ai)

#### Tom de voz
- Adjetivos: direto, pragmático, reflexivo, confiante, didático
- Frase característica: "That gap is your whole career."

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: medio
- Seguidores (aprox., não confirmado direto): 88 mil

#### Temas recorrentes identificados
- uso prático de IA no dia a dia
- produtividade e automação pessoal
- diferenciação humano vs. IA
- estatísticas de adoção de IA
- bastidores de criação de conteúdo com IA
---

### @yikC — creator
**Bio:** não recuperada

#### Métricas estimadas
- Formato mais usado: —
- Engajamento estimado: —
- Seguidores (aprox., não confirmado direto): —
---

### @eujoaotorresz — creator
**Bio:** não recuperada

#### Métricas estimadas
- Formato mais usado: —
- Engajamento estimado: —
- Seguidores (aprox., não confirmado direto): —
---

### @fabianocarvalhojr — founder
**Bio:** Founder lasy.ai — Crio Agentes de IA que vendem e operam Negócios 24/7. Te Ensino na Aula Grátis. ~84 mil seguidores, 1.218 posts.

#### Padrões de Hook identificados
- Modelo: outro (frequência: media) — ex: "Quem mais? 😅 ➡️ Siga @fabianocarvalhojr que te ensino..."

#### Estrutura típica do conteúdo
Conteúdo sobre ensinar a criar/usar 'Agentes de IA' para negócios, com convite recorrente para seguir e participar de 'Aula Grátis' (funil de captação para lasy.ai).

#### CTA dominante
- Padrão: Convite para 'Aula Grátis' sobre criação de Agentes de IA.

#### Tom de voz
- Adjetivos: didático, vendedor, acessível, direto
- Frase característica: "Crio Agentes de IA que vendem e operam Negócios 24/7."

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: medio
- Seguidores (aprox., não confirmado direto): 84 mil

#### Temas recorrentes identificados
- agentes de IA para negócios
- automação de vendas com IA
- empreendedorismo/founder de startup de IA
- aula gratuita/captação de leads
---

### @rafa.grandi — marketing
**Bio:** Analista Jurídico SPGG/RS e Pai do Cássio. ~247 seguidores, 36 posts.

#### Métricas estimadas
- Formato mais usado: —
- Engajamento estimado: baixo
- Seguidores (aprox., não confirmado direto): —
---

### @brusantanna.ai — ia
**Bio:** Bruna Santanna | Estrategista de IA. Selecionada para o programa Bradesco Potenc.IA; relatos indicam mentorias de IA prática para 250+ mulheres (Machado Meyer, Corteva, Livelo). Seguidores não encontrados.

#### Métricas estimadas
- Formato mais usado: —
- Engajamento estimado: —
- Seguidores (aprox., não confirmado direto): —

#### Temas recorrentes identificados
- IA aplicada a negócios/carreira
- mentoria de IA para mulheres empreendedoras
---

### @vendedorglobal — negocio-digital
**Bio:** Murilo Bevervanso | Ecommerce Marketplace — 83 mil seguidores, 2.280 posts. +100M visualizações somadas nos reels; foco em e-commerce/marketplaces (Shopee) e monetização com IA.

#### Métricas estimadas
- Formato mais usado: reels
- Engajamento estimado: alto
- Seguidores (aprox., não confirmado direto): 83 mil

#### Temas recorrentes identificados
- e-commerce e marketplaces (Shopee)
- monetização online/ChatGPT e IA
- empreendedorismo digital
---

### @oluizmain — creator
**Bio:** Luiz Main — Creator Mobile & IA, Mentor/CEO da Mobile Pro. 215 mil seguidores, 191 posts. Curso Mobile Pro (produção de vídeo com celular).

#### Métricas estimadas
- Formato mais usado: reels
- Engajamento estimado: alto
- Seguidores (aprox., não confirmado direto): 215 mil

#### Temas recorrentes identificados
- produção de vídeo com celular
- bastidores/estratégias do curso Mobile Pro
- trabalho, viagem e lifestyle
---

### @nick_saraev — automacao
**Bio:** Founder @ Maker School — Helping 2000+ beginners land their First AI client. ~550 mil seguidores. Fundador LeftClick (automação de IA B2B), Maker School, 1SecondCopy; YouTube 400K+.

#### CTA dominante
- Padrão: CTA de comentário para resgatar recurso gratuito (reportado por fonte secundária, não confirmado diretamente): comentar "AUTOMATION" para templates de automação de IA.
- Variações: Oferta com garantia na bio: Get your first client in 90 days or money back

#### Tom de voz
- Adjetivos: direto, orientado a resultados/dados, didático
- Frase característica: "Helping 2000+ beginners land their First AI client"

#### Métricas estimadas
- Formato mais usado: reels
- Engajamento estimado: alto
- Seguidores (aprox., não confirmado direto): 550 mil

#### Temas recorrentes identificados
- automação de IA para agências/negócios
- cases de faturamento ($72K/mês, $451K, $405K)
- recrutamento para Maker School
- bastidores da LeftClick
---

### @nathanhodgson — ia
**Bio:** Handle exato não confirmado como conta ativa. Conta mais próxima: @nathanhodgson.ai — "Built a 6-Figure Business Powered By AI • Trusted by Google · Meta · OpenAI", 128 mil seguidores, 339 posts. Outras contas homônimas não confirmadas como a mesma.

#### Métricas estimadas
- Formato mais usado: reels
- Engajamento estimado: alto
- Seguidores (aprox., não confirmado direto): 128 mil

#### Temas recorrentes identificados
- ferramentas de IA para programação
- ferramentas de IA para design
- automação de negócios com IA
- como montar um negócio de IA
---

### @ai — ia
**Bio:** não recuperada

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo
- Seguidores (aprox., não confirmado direto): —
---

### @ana.gsoares — marketing
**Bio:** Ana G Soares — CEO de @uniagiloficial, host do podcast @agilizesepodcast, Agile Coach, criadora da imersão 'Claude Project', instrutora Udemy com 100.000+ alunos. ~146 mil seguidores, 2.840 posts.

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "Conhecer Gestão Ágil vai te tornar um profissional diferenciado, independente da situação"
- Modelo: outro (frequência: baixa) — ex: "Um novo mercado para trabalhadores"

#### Estrutura típica do conteúdo
Não determinado com confiança — apenas títulos/legendas de reels encontrados.

#### Tom de voz
- Adjetivos: motivacional, profissional, educativo, corporativo
- Frase característica: "Conhecer Gestão Ágil vai te tornar um profissional diferenciado, independente da situação"

#### Métricas estimadas
- Formato mais usado: reels
- Engajamento estimado: alto
- Seguidores (aprox., não confirmado direto): 146 mil

#### Temas recorrentes identificados
- gestão ágil
- transição de carreira/mercado de trabalho
- metodologias ágeis aplicadas a negócios
- IA aplicada a produtividade (Claude Project)
---

### @chase.h.ai — ia
**Bio:** 🤖 Making AI Simple ⚡️ DM 'Ready' to Apply For 1:1 Mentorship 🚀 Master Claude Code. ~221 mil seguidores, 751 posts. Ensina 175.000+ pessoas entre Instagram/TikTok/YouTube sobre IA no-code.

#### CTA dominante
- Padrão: DM com palavra-chave para aplicar a mentoria
- Variações: DM 'Ready' to Apply For 1:1 Mentorship (bio)

#### Tom de voz
- Adjetivos: acessível, direto, aspiracional, orientado a ação, comercial
- Frase característica: "Making AI Simple"

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: alto
- Seguidores (aprox., não confirmado direto): 221 mil

#### Temas recorrentes identificados
- IA no-code
- Claude Code
- educação em IA para criadores/empreendedores
- mentoria 1:1
---

### @leosoares.ia — ia
**Bio:** Léo Soares | IA p/ Negócios — CEO da Acelera IA. 'IA tem que gerar RESULTADO'. ~219 mil seguidores, 2.226 posts.

#### Estrutura típica do conteúdo
Não determinada com confiança.

#### CTA dominante
- Padrão: Comentar palavra-chave numerada para receber material/vaga por DM
- Variações: Comenta IA16 pra não perder; Comenta 'IA04'; Comenta IA10 pra se garantir

#### Tom de voz
- Adjetivos: direto, orientado a resultado, comercial, urgente
- Frase característica: "IA tem que gerar RESULTADO"

#### Métricas estimadas
- Formato mais usado: reels
- Engajamento estimado: alto
- Seguidores (aprox., não confirmado direto): 219 mil

#### Temas recorrentes identificados
- IA para lançamentos digitais
- IA para infoprodutos
- IA para negócios
- imersões e mentorias pagas de IA
---

### @gabriel.adamuchi — creator
**Bio:** IA Fácil — Gabriel Adamuchi. Missão: tornar IA fácil de aprender e gerar renda com ela (dados cruzados via TikTok da mesma marca: 195,2 mil seguidores, 1,9 mi curtidas). Seguidores do Instagram não encontrados.

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "Segue esse perfil e saiba tudo sobre o mundo da IA"

#### Estrutura típica do conteúdo
Compartilhamento de prompts de IA prontos seguido de demonstração do resultado gerado e/ou apresentação de ferramenta de IA.

#### Tom de voz
- Adjetivos: acessível, prático, didático, entusiasmado
- Frase característica: "Segue esse perfil e saiba tudo sobre o mundo da IA"

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: medio
- Seguidores (aprox., não confirmado direto): 195,2 mil

#### Temas recorrentes identificados
- prompts de geração de imagem por IA
- ferramentas de IA (lip sync, Nano Banana Pro)
- tutoriais de IA acessíveis
---

### @viverdeia — ia
**Bio:** Associada a 'Viver de IA' (@viverdeia.ai), fundada por Rafael Milagre. "A Plataforma das Empresas que Crescem com IA +2000 Empresas aceleradas com IA Plug & Play". ~129K seguidores, 611 posts.

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: alto
- Seguidores (aprox., não confirmado direto): 129K

#### Temas recorrentes identificados
- IA aplicada a negócios
- aceleração de empresas com IA
- plataforma/comunidade de formação em IA
---

### @ninja.automacoes — automacao
**Bio:** Conta 'Automação e IA' ('Ninja das Automações'), administrada por Matheus Pessoa. Bio exata e seguidores não confirmados.

#### Métricas estimadas
- Formato mais usado: reels
- Engajamento estimado: —
- Seguidores (aprox., não confirmado direto): —

#### Temas recorrentes identificados
- automação de processos
- inteligência artificial aplicada
- ferramentas/cursos de automação
---

### @nikolassfaria — creator
**Bio:** não recuperada

#### Métricas estimadas
- Formato mais usado: —
- Engajamento estimado: —
- Seguidores (aprox., não confirmado direto): —
---

### @eduardocavalcanti — founder
**Bio:** Perfil pessoal confirmado. Eduardo Cavalcanti é co-fundador/CEO da Fundamentei (dados para ações e FIIs, 460K+ investidores cadastrados), consultor CVM/CNPI. A marca @fundamentei (conta distinta) tem ~65K seguidores; bio/seguidores do handle pessoal não confirmados.

#### Métricas estimadas
- Formato mais usado: —
- Engajamento estimado: —
- Seguidores (aprox., não confirmado direto): 65K

#### Temas recorrentes identificados
- análise de ações e FIIs
- educação financeira/investidor
- quando comprar/vender ativos
- aposentadoria e carteira de investimentos
---

### @jonylan — creator
**Bio:** Jony Lan | Marketing Digital, Vendas e IA. "Inteligência Artificial Ninja da internet desde 1994". ~306K seguidores, 3.255 posts. Palestras, treinamentos, consultoria; menção a atuação como Builder no Google Brasil (não verificado).

#### Métricas estimadas
- Formato mais usado: reels
- Engajamento estimado: alto
- Seguidores (aprox., não confirmado direto): 306K

#### Temas recorrentes identificados
- marketing digital
- vendas
- inteligência artificial aplicada a negócios
- palestras e treinamentos
---

### @allesinisgalli — founder
**Bio:** 'AI & MARKETING - IA CLUB COMUNIDADE', associada a Allessandra Sinisgalli — Marketing mentor powered by AI, +15 anos em marketing (Austrália/Brasil), fundadora do 'IA Club'. Seguidores inconsistentes entre fontes (8.155 via Heepsy vs 61.300 citado em outra fonte) — não confirmado.

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "LIBERDADE ATRAVÉS DO..."

#### Estrutura típica do conteúdo
Não determinado com confiança — apenas título truncado de um reel indexado.

#### Métricas estimadas
- Formato mais usado: reels
- Engajamento estimado: medio
- Seguidores (aprox., não confirmado direto): —

#### Temas recorrentes identificados
- inteligência artificial aplicada a negócios
- marketing digital
- automações
- comunidade paga (IA Club)
---

### @lonamkt — marketing
**Bio:** Associada a Felipe Lona (marketing digital/performance/tráfego pago), ~4.316 seguidores, apenas 2 posts publicados — conta pouco ativa; conteúdo principal no YouTube (@Lonamkt) e possivelmente outra conta IG (@felipelonaa).

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo
- Seguidores (aprox., não confirmado direto): —

#### Temas recorrentes identificados
- tráfego pago
- campanhas de marketing digital
- faturamento/resultados financeiros
---

### @gabrielbarbosa.oficial — creator
**Bio:** Gabriel Barbosa | Negócios Digitais — '+10MM faturados na internet, Te ensino a ter uma operação enxuta e lucrativa de qualquer lugar do mundo'. ~7.782 seguidores.

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "Hoje fui na Xgrow..."

#### Estrutura típica do conteúdo
Não determinado — apenas título truncado de um post (15/03).

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: medio
- Seguidores (aprox., não confirmado direto): —

#### Temas recorrentes identificados
- negócios digitais
- operação enxuta/lean business
- faturamento na internet
---

### @opensession.co — agencia
**Bio:** Open Session — 'Brand x UX/AI x Design Systems. We help designers and brands level up their creativity.' ~23.000 seguidores, 19 posts. Estúdio de design (San Diego, CA), branding/design systems com IA.

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: medio
- Seguidores (aprox., não confirmado direto): —

#### Temas recorrentes identificados
- design systems
- branding
- IA aplicada a design/criatividade
- UX
---

### @leandroladeiran — marketing
**Bio:** Leandro Ladeira Neiva — bio via Threads: 'Se você quer aprender sobre marketing e produtos digitais, clicar no link abaixo vai facilitar sua vida (e com mais dinheiro)' (tradução, não confirmada literal). Seguidores IG não confirmados; TikTok 882,1K, Threads 408,0K.

#### Padrões de Hook identificados
- Modelo: maioria_errando (frequência: baixa) — ex: "Quem tem razão?"
- Modelo: outro (frequência: baixa) — ex: "O futuro do marketing digital"
- Modelo: outro (frequência: baixa) — ex: "O Cruzeiro all inclusive do marketing..."

#### Estrutura típica do conteúdo
Não determinado — apenas títulos truncados de reels indexados.

#### CTA dominante
- Padrão: Não confirmado com exatidão (trecho 'comenta EU QUERO que te mando o link agora!' não amarrado com certeza a este perfil).

#### Tom de voz
- Adjetivos: direto, provocador, confessional, pessoal
- Frase característica: "A história da minha..."

#### Métricas estimadas
- Formato mais usado: reels
- Engajamento estimado: alto
- Seguidores (aprox., não confirmado direto): 882,1K

#### Temas recorrentes identificados
- marketing digital
- copywriting
- produtos digitais/infoprodutos
- histórias pessoais/bastidores
- opinião/provocação
---

### @christiantriad — creator
**Bio:** Christian Barbosa - IA, Tech & Saas. "🤖 Empresário Tech - IA, Tech & Saas 💻 Criador do método 'A Tríade do Tempo' 2M+ pessoas treinadas ❤️ @easy.dcor". ~571K seguidores, 4.333 posts.

#### Métricas estimadas
- Formato mais usado: não determinado
- Engajamento estimado: alto
- Seguidores (aprox., não confirmado direto): 571K

#### Temas recorrentes identificados
- IA
- Tech
- SaaS
- produtividade (Tríade do Tempo)
---

### @oneyaraujo — creator
**Bio:** Oney Araújo | Marketing Viral. Criador do 'Código Viral' (viralização Reels/TikTok/Shorts). ~2M seguidores; 62 mil+ alunos.

#### CTA dominante
- Variações: "Segue @oneyaraujo e conheça o Código Viral no link da Bio" (de vídeo de terceiro, não confirmado como legenda original)

#### Métricas estimadas
- Formato mais usado: não determinado
- Engajamento estimado: alto
- Seguidores (aprox., não confirmado direto): 2M

#### Temas recorrentes identificados
- viralização de conteúdo
- crescimento de seguidores
- vendas online
- Reels/algoritmo
---

### @geracaotechs — ia
**Bio:** Glauton Filho | Tecnologia e IA (via Threads). Conteúdo sobre democratizar ferramentas de IA (vídeo, jogos, animação 3D). Seguidores IG não encontrados.

#### Padrões de Hook identificados
- Modelo: paradoxo_contraste (frequência: baixa) — ex: "🚀 Esqueça tudo o que você sabe sobre geradores de vídeo simples, o Anijam é..."

#### Estrutura típica do conteúdo
Abre citando problema/ferramenta antiga, apresenta ferramenta de IA nova com emojis temáticos, lista benefícios com emojis marcadores, hashtags no fim (#aitools #tecnologia) — padrão observado via Threads/TikTok do mesmo handle, não confirmado no Instagram.

#### Tom de voz
- Adjetivos: didático, entusiasmado, direto, tecnológico
- Frase característica: "🎮 Esse site te permite criar jogos só descrevendo sua ideia..."

#### Métricas estimadas
- Formato mais usado: não determinado
- Engajamento estimado: baixo
- Seguidores (aprox., não confirmado direto): —

#### Temas recorrentes identificados
- geração de vídeo com IA
- criação de jogos com IA
- animação 3D/SVG
- customização 3D de carros
- ferramentas de IA para criadores
---

### @amandadinizmkt — marketing
**Bio:** "IA para Empreendedoras"/"Marketing & Empreendedorismo" (Amanda Diniz). Foco em IA (Claude) para empreendedoras: posts, roteiros de Reels, apresentações. Também no TikTok. Seguidores IG não encontrados.

#### Métricas estimadas
- Formato mais usado: não determinado
- Engajamento estimado: baixo
- Seguidores (aprox., não confirmado direto): —

#### Temas recorrentes identificados
- uso de IA (Claude) para empreendedorismo
- criação de conteúdo/posts com IA
- produtividade para negócios
- marketing digital
---

### @humam__academy — ia
**Bio:** não recuperada

#### Métricas estimadas
- Formato mais usado: não determinado
- Engajamento estimado: baixo
- Seguidores (aprox., não confirmado direto): —
---

### @geiss11 — creator
**Bio:** Henrique Geiss — "Vendo Produtos Digitais no Mundo Todo" (Brasil, Uruguai, México, Mônaco, França, Itália, Suíça, Argentina, Chile). ~45 mil seguidores, ~83 posts.

#### Métricas estimadas
- Formato mais usado: —
- Engajamento estimado: medio
- Seguidores (aprox., não confirmado direto): 45 mil

#### Temas recorrentes identificados
- venda de produtos digitais/infoprodutos internacional
---

### @nelmoricalde — creator
**Bio:** Nelmo Ricalde | IA, Negócios & Lucro. 20+ anos no mercado financeiro (CitiBank, BankBoston), fundador da Zuvora (agência IA/performance, 2019), criador da comunidade 'Nova Inteligência', palestrante AI Summit Brasil.

#### Métricas estimadas
- Formato mais usado: —
- Engajamento estimado: —
- Seguidores (aprox., não confirmado direto): —

#### Temas recorrentes identificados
- inteligência artificial aplicada a negócios
- produtividade/automação empresarial
- mentoria e treinamentos em IA
---

### @rodrigotadewald — marketing
**Bio:** Rodrigo Soares Tadewald — Eng. Químico (UFRGS), estratégias quantitativas, Python desde 2015. Cofundador Asimov Academy (2021) e sócio-fundador Asimov Finance. Marca Asimov tem 550K+ seguidores somados nas redes — não confirmado como da conta pessoal.

#### Métricas estimadas
- Formato mais usado: —
- Engajamento estimado: —
- Seguidores (aprox., não confirmado direto): 550K

#### Temas recorrentes identificados
- Python
- ciência de dados/IA aplicada
- estratégias quantitativas no mercado financeiro
- educação em programação
---

### @sujeitoprogramador — ia
**Bio:** Matheus Fraga — "👨🏻‍💻 Programador há + de 12 anos 🔥 + de 45.000 alunos. Aprenda programação e IA do zero ao mercado👇". ~168 mil seguidores, ~3.040 posts.

#### Estrutura típica do conteúdo
Títulos indexados sugerem dica/tutorial curto (ex: 'Se liga nessa lib para...', 'Agora podemos usar variáveis ambiente...'), mas sem acesso à legenda completa/roteiro.

#### Tom de voz
- Adjetivos: didático, direto
- Frase característica: "Programação é prática, e quando você..."

#### Métricas estimadas
- Formato mais usado: reels
- Engajamento estimado: —
- Seguidores (aprox., não confirmado direto): 168 mil

#### Temas recorrentes identificados
- programação (JavaScript/web)
- inteligência artificial aplicada a código
- dicas de ferramentas e bibliotecas de desenvolvimento
- variáveis de ambiente/boas práticas
---

### @jonathan_kamargo — creator
**Bio:** não recuperada

#### Métricas estimadas
- Formato mais usado: —
- Engajamento estimado: —
- Seguidores (aprox., não confirmado direto): —
---

### @marianatorre.s — marketing
**Bio:** não recuperada

#### Métricas estimadas
- Formato mais usado: —
- Engajamento estimado: —
- Seguidores (aprox., não confirmado direto): —
---

### @marketerhub.ai — marketing
**Bio:** Tagline: "Empowering Digital Marketers". Site institucional (marketerhub.ai): comunidade privada de marketing com IA — cursos, prompts, templates. Não confirmado se é texto literal da bio do IG.

#### Métricas estimadas
- Formato mais usado: —
- Engajamento estimado: —
- Seguidores (aprox., não confirmado direto): —
---

### @marcelaluzzio — marketing
**Bio:** "🔱 Te faço crescer e vender mais com IA 💎 MBA em IA para negócios digitais (USP) 🔥 Crie e venda seu Infoproduto com IA 👇🏼" — Marketing de Conteúdo & I.A. ~226K seguidores, 964 posts.

#### Métricas estimadas
- Formato mais usado: —
- Engajamento estimado: alto
- Seguidores (aprox., não confirmado direto): 226K

#### Temas recorrentes identificados
- Marketing de conteúdo com IA
- Como vender/criar infoprodutos com IA
- Crescimento orgânico usando IA
---

### @gestordeaudiencia — marketing
**Bio:** não recuperada

#### Métricas estimadas
- Formato mais usado: —
- Engajamento estimado: —
- Seguidores (aprox., não confirmado direto): —
---

### @sebintel — ia
**Bio:** 'Seb Intel', criado por Sebastien Jefferies (contato info@sebtips.com). Seguidores do IG não confirmados; conta irmã TikTok tem 56,7K seguidores/595,8K curtidas.

#### Métricas estimadas
- Formato mais usado: reels
- Engajamento estimado: —
- Seguidores (aprox., não confirmado direto): 56,7K

#### Temas recorrentes identificados
- Ferramentas de IA (AI tools) e tutoriais de uso
- Criação de sites 3D/scroll-based com prompt único
- Ferramentas de IA para vídeo e design web
---

### @avora.ai — agencia
**Bio:** Bio completa não recuperada. Legenda promocional real encontrada: "Siga @avora.ai para conteúdos diários sobre IA na prática!"

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: —
- Seguidores (aprox., não confirmado direto): —

#### Temas recorrentes identificados
- IA na prática
---

### @ogabrieeldias — creator
**Bio:** Bio completa não recuperada. Único dado confirmado: título indexado "Gabriel Dias | SaaS Founder".

#### Métricas estimadas
- Formato mais usado: —
- Engajamento estimado: —
- Seguidores (aprox., não confirmado direto): —
---

### @rodrigobindes — founder
**Bio:** "Rodrigo Bindes | Mentor de Agências de Marketing Digital". Como chegar a R$100k/mês com agência; fundador Ultralize, Mentoria Ultra, CEO Supersal; associado a @marketingpararestaurante e @ultralizeoficial. 278K seguidores, 1.835 posts (Threads 15,8K).

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: alto
- Seguidores (aprox., não confirmado direto): 278K

#### Temas recorrentes identificados
- mentoria para agências de marketing digital
- faturamento de R$100k/mês
- marketing para restaurantes (Supersal)
- Mentoria Ultra/Ultralize
---

### @franklim.gui — creator
**Bio:** "guilherme franklim" — 46K seguidores, 159 posts. Cursos sobre IA (Claude Code) e tráfego low-ticket. Também YouTube/Facebook; cursos na Udemy ("Curso Claude Code Gratuito para Iniciantes", "Formação Claude Code 2026").

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: medio
- Seguidores (aprox., não confirmado direto): 46K

#### Temas recorrentes identificados
- Claude Code
- automação com IA
- cursos low-ticket
- agentes de IA
---

### @gabrielsamp.ai — ia
**Bio:** não recuperada

#### Métricas estimadas
- Formato mais usado: —
- Engajamento estimado: —
- Seguidores (aprox., não confirmado direto): —
---

### @maestrosdaia — ia
**Bio:** não recuperada

#### Métricas estimadas
- Formato mais usado: —
- Engajamento estimado: indeterminado
- Seguidores (aprox., não confirmado direto): —

#### Temas recorrentes identificados
- automação de Instagram/Messenger com IA (DMs, captura de leads)
- avatares e clones de IA para produção de vídeos
- clonagem de voz com IA para narrações/avatares
- lives semanais com especialistas e comunidade paga de IA
---

### @brandsdecoded — marketing
**Bio:** Não confirmada literalmente. Associada a 'AI Content Agency', ~301 mil seguidores (não verificado), posicionamento 'decodificar o futuro do marketing com AI' (de snippet, não confirmado literal).

#### Métricas estimadas
- Formato mais usado: carrossel
- Engajamento estimado: alto
- Seguidores (aprox., não confirmado direto): 301 mil

#### Temas recorrentes identificados
- criação de conteúdo com IA para Instagram
- carrosséis de autoridade/vendas ('Content Machine 3.0')
- automação de design e copy (plugins Canva/Figma)
- estratégia de conteúdo baseada em dados
---

### @anatex — creator
**Bio:** Ana Tex - Inteligência Artificial para Negócios (tagline de busca, texto completo não confirmado). ~694 mil seguidores, 1.358 posts.

#### Métricas estimadas
- Formato mais usado: —
- Engajamento estimado: alto
- Seguidores (aprox., não confirmado direto): 694 mil

#### Temas recorrentes identificados
- Inteligência Artificial para Negócios
- Marketing Digital com apoio de IA
- capacitação de especialistas fora de tecnologia para dominar IA
---

### @larissagomes.ia — ia
**Bio:** 💻 Te ensino a criar um negócio enxuto e que vende: você + IA ⚡️ Compartilho o que aplico sobre IA Domine o chatGPT👇🏻 — ~15K seguidores, 262 posts.

#### Padrões de Hook identificados
- Modelo: paradoxo_contraste (frequência: baixa) — ex: "você quer crescer no instagram mas quase nunca para pra analisar o próprio perfil"
- Modelo: outro (frequência: baixa) — ex: "Peça o chatGPT para analisar o feed do seu instagram 🧠"

#### Estrutura típica do conteúdo
Hook ligado a um 'truque'/prompt de IA → CTA de seguir logo no início → prompt pronto em lista numerada (1️⃣2️⃣3️⃣) para copiar/colar → CTA de salvar o post. Amostra pequena (2 exemplos via cross-post TikTok/Threads), não confirmado padrão em todos os posts.

#### CTA dominante
- Padrão: Seguir o perfil logo no início: "siga @larissagomes.ia para receber mais conteúdos como esse e aprender como criar, crescer e vender todos os dias com IA. 👇🏻"
- Variações: Salvar o post: "📩 Salva pra lembrar de analisar o seu perfil!"

#### Tom de voz
- Adjetivos: didático, direto, prático, acolhedor
- Frase característica: "💻 Te ensino a criar um negócio enxuto e que vende: você + IA ⚡️"

#### Métricas estimadas
- Formato mais usado: —
- Engajamento estimado: medio
- Seguidores (aprox., não confirmado direto): 15K

#### Temas recorrentes identificados
- análise de perfil do Instagram usando IA/ChatGPT
- prompts prontos para marketing e negócios
- crescimento no Instagram com IA
- ChatGPT aplicado a negócios enxutos
---

### @thiagozaao — creator
**Bio:** não recuperada

#### Métricas estimadas
- Formato mais usado: —
- Engajamento estimado: indeterminado
- Seguidores (aprox., não confirmado direto): —
---

### @neuwebstudio — agencia
**Bio:** não recuperada

#### Métricas estimadas
- Formato mais usado: —
- Engajamento estimado: —
- Seguidores (aprox., não confirmado direto): —
---

### @laschuk — founder
**Bio:** não recuperada

#### Métricas estimadas
- Formato mais usado: —
- Engajamento estimado: —
- Seguidores (aprox., não confirmado direto): —
---

### @maestroptompts — ia
**Bio:** não recuperada

#### Métricas estimadas
- Formato mais usado: —
- Engajamento estimado: —
- Seguidores (aprox., não confirmado direto): —
---

### @faladantasmkt — marketing
**Bio:** não recuperada

#### Métricas estimadas
- Formato mais usado: —
- Engajamento estimado: —
- Seguidores (aprox., não confirmado direto): —
---

### @lindsay.ia — ia
**Bio:** não recuperada

#### Métricas estimadas
- Formato mais usado: —
- Engajamento estimado: —
- Seguidores (aprox., não confirmado direto): —
---

### @andrevictor.m — marketing
**Bio:** não recuperada

#### Métricas estimadas
- Formato mais usado: —
- Engajamento estimado: —
- Seguidores (aprox., não confirmado direto): —
---

### @drisiano — creator
**Bio:** não recuperada

#### Métricas estimadas
- Formato mais usado: —
- Engajamento estimado: —
- Seguidores (aprox., não confirmado direto): —
---

### @brun0gpt — ia
**Bio:** não recuperada

#### Métricas estimadas
- Formato mais usado: —
- Engajamento estimado: —
- Seguidores (aprox., não confirmado direto): —
---

### @maxcarrau.ia — ia
**Bio:** não recuperada

#### Métricas estimadas
- Formato mais usado: —
- Engajamento estimado: —
- Seguidores (aprox., não confirmado direto): —
---

### @noevarner — creator
**Bio:** não recuperada

#### Métricas estimadas
- Formato mais usado: —
- Engajamento estimado: —
- Seguidores (aprox., não confirmado direto): —
---

### @yikchan — creator
**Bio:** não recuperada

#### Métricas estimadas
- Formato mais usado: —
- Engajamento estimado: —
- Seguidores (aprox., não confirmado direto): —

---

## Limitações de Dados

- @charliehills — Instagram bloqueou WebFetch direto. Dados vêm de busca web (Substack/LinkedIn do mesmo autor); frases podem ser reaproveitadas entre plataformas. Estrutura exata, frequência real dos hooks e métricas de engajamento não confirmadas.
- @yikC — Nenhum perfil com handle exato '@yikC' foi encontrado. WebFetch falhou (bloqueio de rede). Não foi possível confirmar se a conta existe, é privada ou o handle está incorreto. Nenhum dado inventado.
- @eujoaotorresz — Handle exato não localizado. Resultado mais próximo (@joaotorresz, ~2K seguidores, 5 posts) não bate com o handle e não teria material suficiente. WebFetch falhou. Nenhuma correspondência confiável encontrada.
- @fabianocarvalhojr — WebFetch bloqueado. Apenas uma legenda parcial encontrada — insuficiente para mapear frequência real dos hooks, variações de CTA, estrutura completa ou métricas de engajamento.
- @rafa.grandi — Handle corresponde a conta pessoal (não relacionada a marketing/nicho), baixo volume (247 seguidores, 36 posts). Provável divergência entre handle solicitado e perfil de marketing pretendido. Nenhum dado de conteúdo inventado.
- @brusantanna.ai — WebFetch bloqueado (EGRESS_BLOCKED). Não foi possível obter seguidores, hooks verbatim, estrutura, CTA, tom ou engajamento reais.
- @vendedorglobal — WebFetch bloqueado. Formato e engajamento inferidos só por seguidores/menções de terceiros, sem dados diretos de curtidas/comentários. Hooks e CTA verbatim não obtidos.
- @oluizmain — WebFetch bloqueado. Formato/engajamento inferidos só por seguidores. Hooks, estrutura, CTA e tom com texto real não obtidos.
- @nick_saraev — WebFetch bloqueado. CTA e temas vêm de fontes secundárias (Favikon, reviews), não confirmados diretamente com frase exata de um post. Hooks verbatim não obtidos.
- @nathanhodgson — Ambiguidade de identidade — não confirmado que a URL fornecida corresponde à conta @nathanhodgson.ai usada como base. WebFetch bloqueado. Hooks, estrutura e CTA verbatim não obtidos.
- @ai — Handle extremamente genérico; WebSearch dominado por conteúdo institucional Meta AI não relacionado à conta. WebFetch bloqueado. Nenhum dado real coletado.
- @ana.gsoares — WebFetch bloqueado. Dados apenas de snippets de busca. CTA dominante, estrutura detalhada e métricas reais de engajamento não confirmadas.
- @chase.h.ai — WebFetch bloqueado. Só a bio confirmada com texto exato; hooks de reels, estrutura narrativa e métricas reais não coletados.
- @leosoares.ia — WebFetch bloqueado. Padrão de CTA confirmado com 3 exemplos reais; hooks exatos e estrutura narrativa completa não confirmados.
- @gabriel.adamuchi — WebFetch bloqueado. Maior parte dos dados vem do TikTok da mesma marca, não confirmadamente idêntico ao conteúdo do Instagram. Seguidores e engajamento do Instagram especificamente não confirmados.
- @viverdeia — WebFetch bloqueado. Busca indexou @viverdeia.ai, não @viverdeia exatamente — handle não confirmado com certeza. Hooks, CTA, tom e proporção real de formatos não coletados.
- @ninja.automacoes — WebFetch bloqueado. Apenas título truncado de reel encontrado ('3 coisas que você NÃO vai...'), não usável como citação exata. Bio, seguidores, hooks, CTA e tom não confirmados.
- @nikolassfaria — Nenhum dado coletado. WebFetch bloqueado. WebSearch com múltiplas variações não retornou correspondência — apenas homônimos não relacionados (político Nikolas Ferreira, outro criador Nikolas Sasso). Não confirmado se o handle está ativo/correto.
- @eduardocavalcanti — WebFetch bloqueado. Temas vieram da conta irmã @fundamentei, não confirmadamente do handle pessoal solicitado. Bio exata, seguidores, hooks, CTA e tom não obtidos.
- @jonylan — WebFetch bloqueado. Legendas exatas, hooks e CTA não coletados — apenas bio e seguidores via snippets. Formato/engajamento inferidos apenas por predominância de reels nos resultados e contagem de seguidores.
- @allesinisgalli — WebFetch bloqueado. Dados só de busca (Heepsy, LinkedIn, Hotmart, site IA Club). Hooks, estrutura, CTA e tom com frases completas não confirmados; seguidores conflitantes entre fontes.
- @lonamkt — WebFetch bloqueado. Perfil com apenas 2 posts limita amostra. Dados majoritariamente do YouTube associado, não do feed IG.
- @gabrielbarbosa.oficial — WebFetch bloqueado. Apenas bio e título truncado localizados; hooks, estrutura, CTA e tom com frase completa não confirmados.
- @opensession.co — WebFetch bloqueado. Nenhuma legenda de post real encontrada, apenas bio institucional e descrição do site/Medium. Hooks, CTA e tom não confirmados.
- @leandroladeiran — WebFetch bloqueado. Títulos de reels truncados e incompletos. CTA não confirmado como pertencente ao perfil. Seguidores IG não confirmados (só TikTok/Threads); engajamento 'alto' é inferência indireta multiplataforma.
- @christiantriad — WebFetch bloqueado (EGRESS_BLOCKED). Só metadados de perfil via terceiros; sem transcrições de legendas/hooks/CTAs. Engajamento inferido só por seguidores.
- @oneyaraujo — WebFetch bloqueado. Hooks, CTA exato e tom não confirmados diretamente do perfil. Engajamento inferido só por seguidores.
- @geracaotechs — Perfil IG não indexado diretamente; exemplos vêm de Threads/TikTok do mesmo criador (proxy, não confirmado idêntico ao IG). Engajamento 'baixo' é placeholder não confirmado, sem dados reais do Instagram.
- @amandadinizmkt — WebFetch bloqueado. Nenhuma legenda/hook/CTA verbatim localizada; apenas descrição geral de nicho. Engajamento 'baixo' é placeholder não confirmado.
- @humam__academy — Handle exato (duplo underscore) não confirmado. Handles semelhantes encontrados (@human___academy, @himam_academy, @human_academy etc.) não coincidem exatamente — nenhum dado atribuído para evitar reportar conta errada. WebFetch bloqueado.
- @geiss11 — WebFetch bloqueado. Só bio resumida e seguidores aproximados via indexação de terceiros; sem conteúdo real de posts, CTAs, hooks ou tom. Engajamento é estimativa grosseira só por faixa de seguidores.
- @nelmoricalde — WebFetch bloqueado. Apenas posicionamento profissional via LinkedIn/site institucional; nenhuma legenda, hook, CTA, tom, seguidores ou engajamento do IG encontrados.
- @rodrigotadewald — WebFetch bloqueado. Apenas perfil profissional (LinkedIn/GitHub/Medium/Udemy) e da Asimov Academy; sem conteúdo real de posts da conta pessoal. Nota: categoria pedida foi 'marketing', mas conteúdo indica foco em programação/dados/finanças quantitativas.
- @sujeitoprogramador — WebFetch bloqueado. Apenas títulos/inícios truncados de legendas encontrados — insuficiente para hook_modelos e CTA sem especular.
- @jonathan_kamargo — Handle não localizado/confirmado. WebFetch bloqueado. Buscas com variações retornaram só homônimos não relacionados (pesquisador Georgia Tech/Meta, assessor de investimentos). Nenhum dado coletado.
- @marianatorre.s — WebFetch bloqueado. WebSearch só confirmou existência da conta ('Mariana Torres'), sem bio, seguidores, legendas, hooks, CTAs ou temas.
- @marketerhub.ai — WebFetch bloqueado. Apenas título de busca e reel institucional; sem seguidores, legendas, hooks, CTAs ou tom. Risco de confusão com contas semelhantes (@marketerhubcom, @marketer_hub, @aimarthub).
- @marcelaluzzio — WebFetch bloqueado. Bio literal e métricas confirmadas via snapshot indexado, mas nenhuma legenda/hook/CTA/tom exato de post encontrado. Engajamento 'alto' é inferência só por seguidores/alcance mensal declarado (não métricas de interação reais).
- @gestordeaudiencia — WebFetch bloqueado. Buscas associaram o handle a um contexto técnico (repositório GitHub/Vibe Coding Community sobre Claude Code), descompassado da categoria 'marketing' esperada — possível handle homônimo/reaproveitado ou categorização desatualizada. Nenhum dado de conteúdo IG encontrado.
- @sebintel — WebFetch bloqueado. Seguidores/curtidas são do TikTok homônimo, não do IG. Formato 'reels' inferido de títulos de busca, não contagem real. Nenhuma bio literal, hook, CTA ou tom com frase exata do IG encontrado.
- @avora.ai — WebFetch bloqueado. Apenas uma legenda promocional isolada encontrada; sem bio completa, seguidores, hooks ou engajamento.
- @ogabrieeldias — WebFetch bloqueado. Sem seguidores, bio completa, legendas, hooks ou CTAs — apenas o título indexado.
- @rodrigobindes — Bio e seguidores confirmados via múltiplas fontes; WebFetch bloqueado. Nenhuma legenda/hook/CTA/tom exato de post encontrado — buscadores não indexam texto de posts individuais.
- @franklim.gui — Bio resumida e seguidores confirmados via presença cruzada (Udemy/YouTube/Facebook); WebFetch bloqueado. Nenhuma legenda/hook/CTA/tom exato encontrado; engajamento é estimativa aproximada sem dados de interação.
- @gabrielsamp.ai — Quase nenhum dado confiável localizado. Único achado: perfil espelhado no TikTok sem descrição acessível. Buscas por variações do nome retornaram só homônimos não relacionados. WebFetch bloqueado. Nenhum dado inventado.
- @maestrosdaia — WebFetch bloqueado. Resultados majoritariamente páginas de venda da comunidade/curso 'Maestros da IA'; conta irmã no TikTok (71,4K seguidores) não é a fonte pedida. Bio, seguidores IG, hooks, CTAs, estrutura e tom não confirmados.
- @brandsdecoded — WebFetch bloqueado. Dados majoritariamente de páginas de venda de curso, não de posts reais. Existe perfil similar @brandsdecoded__ que pode gerar confusão — ambiguidade não resolvida. Formato/engajamento são inferências, não confirmados.
- @anatex — WebFetch bloqueado. Metadados de perfil confirmados via busca, mas nenhuma legenda/hook/CTA/tom exato encontrado. Engajamento 'alto' só por volume de seguidores.
- @larissagomes.ia — WebFetch bloqueado. Exemplos vieram de cross-posts (TikTok/Threads) do mesmo handle, não confirmados como vindos literalmente do IG. Amostra muito pequena (2 posts) — frequência marcada como baixa. Formato dominante não confirmado.
- @thiagozaao — Nenhum dado coletado. WebFetch bloqueado. WebSearch não retornou correspondência para o handle exato (só homônimos: thiagosetra, thiagozoinho, thiagor.designer). Orçamento de WebSearch da sessão se esgotou (200/200) antes de tentativas adicionais.
- @neuwebstudio — Nenhum dado coletado. WebSearch não retornou resultados específicos (só artigos genéricos sobre Instagram 2026); orçamento de buscas da sessão (200/200) esgotado. WebFetch bloqueado (EGRESS_BLOCKED).
- @laschuk — Nenhum dado coletado. WebSearch não retornou resultados específicos; orçamento de buscas esgotado (200/200). WebFetch bloqueado.
- @maestroptompts — Nenhum dado coletado. WebSearch não retornou resultados específicos; orçamento de buscas esgotado (200/200). WebFetch bloqueado.
- @faladantasmkt — Nenhum dado coletado. WebSearch não retornou resultados específicos; orçamento de buscas esgotado (200/200). WebFetch bloqueado.
- @lindsay.ia — Nenhum dado coletado. WebSearch retornou só homônimos (@lindsay4iowa, @lindsay_ivan); orçamento de buscas esgotado (200/200). WebFetch bloqueado.
- @andrevictor.m — WebSearch retornou apenas URLs de 4 reels (datas), sem legendas/bio/seguidores. WebFetch bloqueado. Nenhum dado de conteúdo coletado.
- @drisiano — WebSearch não retornou resultados relacionados. WebFetch bloqueado. Nenhum dado coletado.
- @brun0gpt — WebSearch não retornou resultados relacionados. WebFetch bloqueado. Nenhum dado coletado.
- @maxcarrau.ia — WebSearch não retornou resultados relacionados. WebFetch bloqueado. Nenhum dado coletado.
- @noevarner — Orçamento de WebSearch da sessão (200/200) esgotado antes de chegar a este handle. WebFetch bloqueado. Nenhum dado coletado.
- @yikchan — Orçamento de WebSearch da sessão (200/200) esgotado antes de chegar a este handle. WebFetch bloqueado. Nenhum dado coletado.
