# Análise de Perfis Instagram — 2026-06-25

## Nota de metodologia

A skill `instagram-content-cloner` não está instalada nesta sessão e a API nativa Swarm (`create()`/`run()`/`rows()`) não está disponível neste ambiente. Como substituto, os 16 perfis ativos em `config/profiles.json` foram divididos em 3 grupos (6/5/5) e processados por 3 sub-agentes paralelos (equivalente a `concurrency: 3`, `batchSize: 5`), cada um instruído explicitamente a:
- responder apenas com base em dados encontrados via busca real (WebSearch — Instagram bloqueia WebFetch direto, confirmado nesta sessão);
- nunca inventar números, bios, hooks ou CTAs;
- sinalizar explicitamente qualquer dado não encontrado como `limitacao_dados`, em vez de estimar.

Nenhum dado de seguidores, posts, hooks, CTAs ou tom de voz abaixo foi inventado. Onde a busca não retornou informação confiável, isso está marcado explicitamente na seção "Limitações de Dados" e dentro de cada perfil.

## Visão Geral dos Perfis

| Perfil | Categoria | Formato Dominante | Engajamento | Frequência (posts) | Hook Padrão |
|---|---|---|---|---|---|
| @charliehills | creator | Reels | Alto (74K seguidores) | Alta (202 posts) | Fenômeno nomeado / paradoxo-contraste |
| @nathanhodgson.ai | ia | Não confirmado | Não determinável (141K seguidores) | Alta (430 posts) | Não confirmado (limitacao_dados) |
| @chase.h.ai | ia | Reels | Alto (201K seguidores) | Alta (695 posts) | Transformação silenciosa / utilidade prática |
| @leosoares.ia | ia | Reels | Alto (219K seguidores) | Muito alta (2.226 posts) | Palavra-chave em comentário + resultado de negócio |
| @geracaotechs | ia | Reels | Não determinável (seguidores não encontrados) | Não confirmado | Demonstração de ferramenta ("outro") |
| @lonamkt | marketing | Não determinável | Baixo/inconsistente (4.316 seguidores, só 2 posts indexados) | Não confirmado | Paradoxo/contraste (inferência fraca) |
| @nikolassfaria | creator | — | — (perfil não localizado) | — | — |
| @jonylan | creator | Não confirmado | Médio-baixo (306K seguidores) | Alta (3.255 posts) | Não confirmado (limitacao_dados) |
| @oneyaraujo | creator | Reels + Carrossel | Alto (2M seguidores) | Alta (1.281 posts) | Pergunta retórica / "maioria errando" |
| @laschuk | founder | Reels | Médio (36K seguidores) | Média (200 posts) | Transformação silenciosa / dor do público |
| @anatex | creator | Não confirmado | Alto (682K seguidores) | Alta (1.318 posts) | Não confirmado (limitacao_dados) |
| @leandroladeiran | marketing | Misto (reels + carrossel) | Alto (2M seguidores) | Alta (834 posts) | Transformação silenciosa / reflexão pessoal (inferência) |
| @marianatorre.s | marketing | — | — (perfil não localizado) | — | — |
| @amandadinizmkt | marketing | Misto (inferência) | Não determinável | Não confirmado | Não confirmado (limitacao_dados) |
| @eujoaotorresz | creator | — | Inconclusivo (handle divergente — ver limitação) | — | — |
| @gabriel.adamuchi | creator | Reels | Médio-alto (inferência via TikTok, sem nº do IG) | Alta (inferência) | Palavra-chave em comentário |

## Análise Detalhada por Perfil

### @charliehills

**Categoria:** creator (tags: ia, negocio-digital) · **Bio:** "💙 I help you (actually) use AI 📧 collabs@charliehills.ai 👇 Free Claude guides"

#### Padrões de Hook identificados (Fase 1 — instagram-content-cloner)
- "Did you know that ChatGPT has 8 hidden personalities..." → **fenômeno nomeado** (revelação de algo "escondido"/numerado)
- "We're so cooked. Nano Banana 2 dropped today. Look at this..." → **paradoxo/contraste** (alarme bem-humorado + novidade de produto)

#### Estrutura típica do conteúdo
Padrão consistente com semanas anteriores: abertura de impacto/humor seguida de demonstração de ferramenta de IA. Sem mudança detectável nesta janela (seguidores/posts idênticos à última verificação).

#### CTA dominante (Padrão + Variações)
Confirmado apenas via bio: "link na bio" (Free Claude guides). **limitacao_dados:** nenhum exemplo textual exato de CTA em comentário/DM foi encontrado nesta rodada.

#### Tom de voz (adjetivos + frases exemplo)
Direto, bem-humorado, "inseridor no fenômeno". Frase exemplo: "We're so cooked."

#### Métricas estimadas (tamanho médio, formato, frequência)
74K seguidores, 274 seguindo, 202 posts. Formato dominante: Reels (3/3 exemplos encontrados).

#### Top conteúdos identificados

| # | Tipo | Tema | Hook | Performance Est. |
|---|---|---|---|---|
| 1 | Reels | Personalidades ocultas do ChatGPT | "Did you know that ChatGPT has 8 hidden personalities..." | Não determinável |
| 2 | Reels | Lançamento Nano Banana 2 | "We're so cooked. Nano Banana 2 dropped today..." | Não determinável |

---

### @nathanhodgson.ai

**Categoria:** ia (tags: ia, automacao) · **Bio:** "Built a 6-Figure Business Powered By AI • Trusted by Google · Meta · OpenAI • Anthropic • hello@nathanhodgson.co.uk • Free AI community"

**Nota de divergência de handle:** o perfil cadastrado em `config/profiles.json` é "@nathanhodgson" (sem ".ai"), mas esse handle não retornou resultados relevantes no nicho de IA — apenas perfis não relacionados (@nathanhodgson_, 3K seguidores; @nathanjameshodgson, eletricista). O perfil correspondente ao briefing (IA/automação, autoridade Google/Meta/OpenAI/Anthropic) é **@nathanhodgson.ai**. Recomenda-se atualizar o handle em `config/profiles.json`.

#### Padrões de Hook identificados (Fase 1 — instagram-content-cloner)
**limitacao_dados:** nenhum exemplo textual exato de hook/primeira linha de post foi encontrado. Buscas retornaram apenas conteúdo genérico de terceiros sobre "viral hooks", não falas reais do perfil.

#### Estrutura típica do conteúdo
Inferência fraca a partir da bio: posicionamento de autoridade/credibilidade corporativa ("trusted by Google/Meta/OpenAI/Anthropic"); indício não confirmado de conteúdo sobre automação de redes sociais (scraping de tweets + ChatGPT para repurposing) — **não confirmado como informação do perfil exato**.

#### CTA dominante (Padrão + Variações)
Bio indica "Free AI community" como CTA de link na bio. **limitacao_dados:** sem exemplo textual de CTA em post.

#### Tom de voz (adjetivos + frases exemplo)
Inferência a partir da bio: autoridade, prova social, corporativo-aspiracional. Sem frase de post para validar.

#### Métricas estimadas (tamanho médio, formato, frequência)
141K seguidores, 108 seguindo, 430 posts. Formato dominante: limitacao_dados (não confirmado).

#### Top conteúdos identificados
**limitacao_dados:** nenhum post específico pôde ser confirmado com confiança suficiente para listar nesta tabela.

---

### @chase.h.ai

**Categoria:** ia (tags: ia, automacao) · **Bio:** "🤖 | Making AI Simple ⚡️ | DM 'Ready' to Apply For 1:1 Mentorship 🚀 | Master Claude Code👇"

#### Padrões de Hook identificados (Fase 1 — instagram-content-cloner)
- "My newest lead generation tool for my AI agents..." → **transformação silenciosa/utilidade prática** (foco em ferramenta/resultado, não em revelação dramática)

#### Estrutura típica do conteúdo
Inferência a partir de menções externas (site institucional chaseai.io/mentorship): "AI agents running in Chase's business, some agents generating $40K/month", "90-day roadmap" — tratado como contexto de oferta, não confirmado como texto literal de post do Instagram.

#### CTA dominante (Padrão + Variações)
**Confirmado e bem definido**, direto da bio: `DM "Ready" to Apply For 1:1 Mentorship`. Classificação: palavra-chave em DM.

#### Tom de voz (adjetivos + frases exemplo)
Direto, prático, orientado a prova social numérica. Frase exemplo: "Making AI Simple" (bio).

#### Métricas estimadas (tamanho médio, formato, frequência)
201K seguidores, 260 seguindo, 695 posts. Formato dominante: Reels. Engajamento qualitativamente alto pelo volume de seguidores/posts (sinal indireto; sem dados reais de likes/comentários).

#### Top conteúdos identificados

| # | Tipo | Tema | Hook | Performance Est. |
|---|---|---|---|---|
| 1 | Reels | Ferramenta de geração de leads para agentes de IA | "My newest lead generation tool for my AI agents..." | Não determinável |

---

### @leosoares.ia

**Categoria:** ia (tags: ia, automacao) · **Bio:** "🔹 CEO Acelera IA 🤖 Inteligência Artificial p/ Negócios 💰 IA tem que gerar RESULTADO ❇️ Conheça a Plataforma Acelera IA 👇"

#### Padrões de Hook identificados (Fase 1 — instagram-content-cloner)
- "Com essa IA eu coloco muito mais leads nos funis dos meus..." → **transformação silenciosa** (resultado de negócio via ferramenta de IA)
- Combinação de palavra-chave/CTA numerada (ex: "IA7") com foco em resultado de negócio, reforçada pela própria bio ("IA tem que gerar RESULTADO")

#### Estrutura típica do conteúdo
Inferência baseada em padrão comum de creators de IA-para-negócios no BR: demonstração de ferramenta → promessa de resultado → CTA de comentário com palavra-chave.

#### CTA dominante (Padrão + Variações)
**Confirmado com exemplo exato** — reel real indexado (instagram.com/reel/DJ7gDS_sym0/) com legenda **"Comenta 'IA7'"**. Classificação: palavra-chave em comentário (padrão clássico de automação comentário→DM).

#### Tom de voz (adjetivos + frases exemplo)
Assertivo, orientado a resultado/ROI, autoridade ("CEO Acelera IA"). Frase exemplo: "IA tem que gerar RESULTADO" (bio).

#### Métricas estimadas (tamanho médio, formato, frequência)
219K seguidores, 1.905 seguindo, 2.226 posts (volume alto sugere cadência intensa/operação profissionalizada). Formato dominante: Reels.

#### Top conteúdos identificados

| # | Tipo | Tema | Hook | Performance Est. |
|---|---|---|---|---|
| 1 | Reels | CTA de palavra-chave para leads | "Comenta 'IA7'" | Alta (sinal indireto: conta madura, 219K seguidores) |
| 2 | Reels | Ferramenta de IA para geração de leads | "Com essa IA eu coloco muito mais leads nos funis dos meus..." | Não determinável |

---

### @geracaotechs

**Categoria:** ia (tags: ia, tech, negocio-digital) · **Bio/Nome:** "Glauton Filho | Tecnologia e I.A" (presença cruzada confirmada em Threads e Instagram)

**limitacao_dados:** número de seguidores e de posts não encontrado em nenhuma busca.

#### Padrões de Hook identificados (Fase 1 — instagram-content-cloner)
Padrão dominante claro — showcases de ferramentas de IA específicas, hook tipo pergunta retórica + emoji + nome da ferramenta/ação:
- "🎮 Esse site te permite criar jogos só descrevendo sua ideia..." → **outro** (demonstração de ferramenta)
- "Customize seu carro dos sonhos online, já imaginou modificar qualquer carro com p[hotos]?" → **outro**
- "Como criar seu bonequinho..." → **outro** (tutorial de tendência, provável trend de "action figures" de IA)
- "✅️Precisa de uma IA (ou..." → **maioria errando/necessidade não percebida** (potencial)
- "Qual das 2 IAs você..." → **paradoxo/contraste** (comparação A vs B)
- "👕 Troque Suas Roupas com..." → **outro**
- "🌐 Quer criar sites com IA..." → **outro**
- "🎨 Crie thumbnails virais para..." → **outro**

#### Estrutura típica do conteúdo
Foco forte em showcases de ferramentas de IA específicas (geração de jogos, customização 3D de carro, troca de roupa por IA, criação de sites, thumbnails) — não narrativa pessoal de negócio.

#### CTA dominante (Padrão + Variações)
**limitacao_dados:** nenhum texto exato de CTA encontrado. Menção indireta a "Comunidade Geração Techs" com links para ferramentas de IA, não confirmada como CTA literal de post.

#### Tom de voz (adjetivos + frases exemplo)
Inferência a partir do padrão de títulos: didático, prático, entusiasmado (uso de emojis ✅🎮🌐🎨👕). Frase exemplo: "🌐 Quer criar sites com IA..."

#### Métricas estimadas (tamanho médio, formato, frequência)
Seguidores/posts: limitacao_dados. Formato dominante: Reels (8/8 exemplos encontrados).

#### Top conteúdos identificados

| # | Tipo | Tema | Hook | Performance Est. |
|---|---|---|---|---|
| 1 | Reels | Criação de jogos com IA | "🎮 Esse site te permite criar jogos só descrevendo sua ideia..." | Não determinável |
| 2 | Reels | Customização 3D de carro | "Customize seu carro dos sonhos online..." | Não determinável |
| 3 | Reels | Geração de "action figures"/bonecos | "Como criar seu bonequinho..." | Não determinável |
| 4 | Reels | Criação de sites com IA | "🌐 Quer criar sites com IA..." | Não determinável |
| 5 | Reels | Thumbnails virais com IA | "🎨 Crie thumbnails virais para..." | Não determinável |

---

### @lonamkt

**Categoria:** marketing (tags: marketing, growth) · **Bio atual:** "🇮🇹 Primeiro milhão aos 18 👇 Me acompanhe aqui"

**Divergência importante de dados:** a busca retornou apenas 4.316 seguidores, 490 seguindo e **2 posts** — incompatível com o perfil de criador estabelecido (Felipe Lona, referência externa em "história de milhões", Head Comercial & Marketing em cosméticos, também aparece como @felipelonaa). Sugere conta resetada/recriada recentemente ou snapshot de busca desatualizado/parcial. **Recomenda-se reverificação manual deste perfil.**

#### Padrões de Hook identificados (Fase 1 — instagram-content-cloner)
- "Foram poucos..." (reel com #marketingdigital #marketing) → tentativa de classificação: **paradoxo/contraste** (poucos vs. muitos, comum em storytelling de escassez/elite). **Fonte incerta** — pode pertencer a @felipelonaa ou ser repost, não confirmado como do perfil atual @lonamkt.

#### Estrutura típica do conteúdo
Inferência (baseada em descrições de terceiros, não em post direto): storytelling de jornada pessoal + prova de resultado + CTA de produto/mentoria. Frase exemplo da bio atual: "Primeiro milhão aos 18".

#### CTA dominante (Padrão + Variações)
**limitacao_dados:** nenhum CTA textual exato e confirmável do perfil atual foi encontrado.

#### Tom de voz (adjetivos + frases exemplo)
Inferência: storytelling de ascensão pessoal, aspiracional/prova social. Frase exemplo: "Primeiro milhão aos 18".

#### Métricas estimadas (tamanho médio, formato, frequência)
4.316 seguidores, 490 seguindo, 2 posts (dado provavelmente incompleto/desatualizado — ver nota acima). Formato dominante: limitacao_dados.

#### Top conteúdos identificados
**limitacao_dados:** apenas 1 post de fonte incerta foi indexado — insuficiente para tabela confiável.

---

### @nikolassfaria

**Categoria:** creator (tags: ia, negocio-digital)

**limitacao_dados — perfil não localizado.** Handle não encontrado via WebSearch em nenhuma variação testada. Resultados retornaram perfis de pessoas diferentes (ex.: Nikolas Ferreira, deputado federal — sem relação com IA/automação). Busca por similaridade fonética encontrou **@nikolassasso** ("Nikolas Sasso | IA para Negócios", ~185K seguidores, foco em IA para negócios/automação), possível erro de digitação do handle original, **mas sem confirmação de que é o mesmo perfil**. Nenhum dado confiável (bio, hooks, CTA, tom de voz, formato) pôde ser reportado. **Recomendação: validar o handle exato antes da próxima execução** (candidato mais provável: @nikolassasso).

---

### @jonylan

**Categoria:** creator (tags: ia, negocio-digital) · **Nome:** "Jony Lan | Marketing Digital, Vendas e IA"

#### Padrões de Hook identificados (Fase 1 — instagram-content-cloner)
**limitacao_dados:** não foi possível extrair frase exata de abertura de reel/post — resultados retornaram apenas conteúdo institucional/perfil, não transcrições.

#### Estrutura típica do conteúdo
Inferência baseada em descrições de terceiros (cross-platform, mesma marca no TikTok): conteúdo educativo sobre ferramentas de IA para marketing digital, dicas de Instagram/Reels, listagem de "+200 ferramentas de IA". Não confirmado diretamente no Instagram.

#### CTA dominante (Padrão + Variações)
Inferência a partir de conteúdo cross-platform: direciona para "link na bio" para acessar lista de ferramentas. **limitacao_dados:** sem exemplo exato confirmado no Instagram.

#### Tom de voz (adjetivos + frases exemplo)
Inferência: didático, informal, "ninja"/tech-entusiasta (bio: "Inteligência Artificial Ninja da internet desde 1994"). Sem frase-exemplo exata confirmada de post.

#### Métricas estimadas (tamanho médio, formato, frequência)
~306K seguidores, 1.076 seguindo, 3.255 posts. Contato: falecomjony@outlook.com; menção a ser "Builder" no Google Brasil. Formato dominante: limitacao_dados (sem dados quantitativos de proporção reels/carrossel/foto).

#### Top conteúdos identificados
**limitacao_dados:** nenhum post específico com hook/texto exato confirmado.

---

### @oneyaraujo

**Categoria:** creator (tags: negocio-digital, marketing) · **Nome:** "Oney Araújo | Marketing Viral" · **Bio:** "🏆 Revelando Segredos de como Viralizar, Ganhar Seguidores e Vender Online. 🚀 +63.000 alunos e contando... 👉🏻 Código Viral por 12x de R$ 19,98"

#### Padrões de Hook identificados (Fase 1 — instagram-content-cloner)
- "Já apareceu para você? Por isso..." → **pergunta retórica/maioria errando**
- "E aí você fala bem ou mal..." → **pergunta retórica/maioria errando**
- "🚨 JÁ CHEGOU PARA VOCÊ? 🚀" → **fenômeno nomeado/gatilho de FOMO**

#### Estrutura típica do conteúdo
Abre com pergunta ou afirmação de urgência (🚨), explica um "segredo"/padrão do algoritmo, fecha direcionando para o produto "Código Viral".

#### CTA dominante (Padrão + Variações)
**Confirmado com múltiplos exemplos exatos:** "conheça o Código Viral no link da bio", "Código Viral no link da Bio!". Variação: pergunta reflexiva ("Me conta nos comentários"). Classificação: link na bio + pergunta reflexiva.

#### Tom de voz (adjetivos + frases exemplo)
Direto, vendedor, urgente, didático, emojis de alerta (🚨🔥🚀). Frase exemplo: "🔥 O Instagram não é mais uma rede social, é uma rede de entretenimento."

#### Métricas estimadas (tamanho médio, formato, frequência)
~2M seguidores, 517 seguindo, 1.281 posts. Criador de conteúdo desde 2012. Formato dominante: Reels + Carrossel ("Carrossel Viral" como estratégia/produto separado). Engajamento qualitativamente alto (base grande + "+63.000 alunos").

#### Top conteúdos identificados

| # | Tipo | Tema | Hook | Performance Est. |
|---|---|---|---|---|
| 1 | Reels | Algoritmo do Instagram/Reels | "🚨 JÁ CHEGOU PARA VOCÊ? 🚀" | Alta (sinal indireto: 2M seguidores) |
| 2 | Reels | Viralização/crescimento de seguidores | "Já apareceu para você? Por isso..." | Não determinável |
| 3 | Reels/Carrossel | Comparação algoritmo vs. IA | "E aí você fala bem ou mal..." | Não determinável |

---

### @laschuk

**Categoria:** founder (tags: negocio-digital, saas, growth) · **Nome:** "Guilherme Laschuk | EmailHacker" · **Bio:** "not for sale"

**Nota de categorização:** dados encontrados indicam foco real em **marketing por email/infoprodutos** (comunidade/curso "EmailHackers"), não SaaS de produto próprio como sugere a categoria cadastrada.

#### Padrões de Hook identificados (Fase 1 — instagram-content-cloner)
- "nunca consegui vender..." → **transformação silenciosa/dor do público**
- "Laschuk, tento vender por email mas só cai na caixa de [spam]..." (citação parcial, cortada) → **transformação silenciosa/dor do público** (objeção de cliente sendo respondida)
- "essa é a melhor forma para vender mais. usar o email para se..." (frase cortada)

#### Estrutura típica do conteúdo
Inferência: formato "pergunta/objeção do seguidor" seguida de resposta prática/tática (estilo P&R), finalizando com prova social ("vendeu +10 milhões via email").

#### CTA dominante (Padrão + Variações)
Inferência (padrão de bio/reels sugere link na bio / comunidade "EmailHackers"). **limitacao_dados:** texto exato de CTA não encontrado.

#### Tom de voz (adjetivos + frases exemplo)
Direto, técnico-vendedor, confiante. Frase confirmada (bio): "not for sale".

#### Métricas estimadas (tamanho médio, formato, frequência)
~36K seguidores, 61 seguindo, 200 posts. Formato dominante: Reels (formato "modelo pronto", ex.: "5 modelos aqui 👇").

**Atenção sobre métricas de terceiros:** os números "25% open rate, 4% CTR, 42 ROAS" encontrados em fontes externas vêm de uma **página de vendas de curso**, NÃO do perfil Instagram — não devem ser atribuídos como dados do Instagram neste ou em relatórios futuros.

#### Top conteúdos identificados

| # | Tipo | Tema | Hook | Performance Est. |
|---|---|---|---|---|
| 1 | Reels | Objeção de vendas por email (spam) | "Laschuk, tento vender por email mas só cai na caixa de [spam]..." | Não determinável |
| 2 | Reels | Modelos de email prontos | "essa é a melhor forma para vender mais..." | Não determinável |

---

### @anatex

**Categoria:** creator (tags: negocio-digital) · **Nome:** "Ana Tex | Ana Paula Teixeira — IA para Negócios" · **Bio:** "🥇 Mentora de Inteligência Artificial para Especialistas — Inove no seu mercado, tenha reconhecimento, produtividade e mais lucro"

#### Padrões de Hook identificados (Fase 1 — instagram-content-cloner)
**limitacao_dados:** nenhuma citação exata de abertura de reel/post encontrada — apenas paráfrases de terceiros (ex.: menção a "80% das profissões vão mudar a forma de serem conduzidas" como dado citado por ela, não confirmado como frase literal de abertura).

#### Estrutura típica do conteúdo
Inferência: conteúdo de autoridade/mentoria — apresenta dado/tendência sobre IA, conecta a oportunidade de negócio, oferece metodologia própria ("método exclusivo de cinco etapas").

#### CTA dominante (Padrão + Variações)
Inferência: perfil de mentoria de alto ticket sugere DM implícita/candidatura para mentoria. **limitacao_dados:** sem exemplo de texto exato confirmado.

#### Tom de voz (adjetivos + frases exemplo)
Autoridade, estratégico, inspirador-corporativo. Frase confirmada (bio): "Inove no seu mercado, tenha reconhecimento, produtividade e mais lucro."

#### Métricas estimadas (tamanho médio, formato, frequência)
~682K seguidores, 1.031 seguindo, 1.318 posts. +16 anos de empreendedorismo digital, pós-graduação FGV, +40 mil alunos formados. Formato dominante: limitacao_dados.

#### Top conteúdos identificados
**limitacao_dados:** nenhum post específico com hook exato confirmado.

---

### @leandroladeiran

**Categoria:** marketing (tags: marketing, growth, negocio-digital) · **Nome:** Leandro Ladeira Neiva · **Bio:** "Se você quer aprender sobre marketing e produtos digitais, clicar no link abaixo vai fazer sua vida mais fácil (e com mais dinheiro)."

#### Padrões de Hook identificados (Fase 1 — instagram-content-cloner)
- "O mundo não é de quem sabe..." → sugestão de **transformação silenciosa/reflexão pessoal** (título truncado no índice, não a frase de abertura completa)
- "Sinto que tenho tudo, mas no final..." → mesma classificação tentativa
- **limitacao_dados:** ambos são legendas truncadas no índice de busca — não foi possível confirmar a frase de abertura completa nem classificar com certeza o tipo de hook.

#### Estrutura típica do conteúdo
Temas confirmados: copywriting ("Como ficar bom de copy", "Que copy eu usei para convencer..."), humor/relacionamentos pessoais ("Pai de pet"), anúncios no Instagram/Meta. Existe GPT customizado de terceiros ("Ladeira Method Copywriting Prompt") inspirado no método dele — sinal de autoridade reconhecida no nicho.

#### CTA dominante (Padrão + Variações)
**limitacao_dados:** não foi encontrado exemplo exato de CTA de comentário atribuído a este perfil especificamente (CTAs do tipo "comenta X" encontrados nas buscas pertencem a outro perfil do grupo, @gabriel.adamuchi).

#### Tom de voz (adjetivos + frases exemplo)
Inferência: direto, motivacional, mistura humor pessoal com autoridade em marketing. Sem fonte para frase exemplo completa e verificada.

#### Métricas estimadas (tamanho médio, formato, frequência)
~2 milhões de seguidores, 1.623 seguindo, 834 posts (fonte: snapshot indexado, não verificado em tempo real). Multiplataforma (TikTok, YouTube via Linktree). Formato dominante: misto (reels e fotos/carrossel).

#### Top conteúdos identificados

| # | Tipo | Tema | Hook | Performance Est. |
|---|---|---|---|---|
| 1 | Misto | Copywriting | "Como ficar bom de copy" | Alta (sinal indireto: 2M seguidores, GPTs de terceiros replicando método) |
| 2 | Misto | Reflexão pessoal | "Sinto que tenho tudo, mas no final..." | Não determinável |

---

### @marianatorre.s

**Categoria:** marketing (tags: marketing, ia)

**limitacao_dados — perfil não localizado.** Buscas com o handle exato e variações (`instagram.com/marianatorre.s`, termos "marketing ia") não retornaram nenhuma correspondência. Resultados trouxeram apenas perfis de nomes parecidos mas claramente diferentes (@marionateres, @_mariatorress_, @mariatorresi, @maria_latorre_ — esta última tatuadora/ilustradora espanhola, sem relação com marketing/IA no Brasil). Nenhum dado confiável sobre bio, seguidores, hooks, CTA, tom de voz ou formato. **Recomendação: verificação manual direta do handle** (possível erro de digitação ou perfil pequeno/recente não indexado).

---

### @amandadinizmkt

**Categoria:** marketing (tags: marketing, ia) · **Posicionamento:** "Marketing & Empreendedorismo" / "IA para Empreendedoras"

#### Padrões de Hook identificados (Fase 1 — instagram-content-cloner)
**limitacao_dados:** nenhum hook completo de reel encontrado. Buscas adicionais sobre "reel viral comenta" não retornaram resultados específicos deste perfil.

#### Estrutura típica do conteúdo
Inferência (não confirmada): formato misto reels + conteúdo em série — título de episódio encontrado: "EP 06: Profissionais da saúde não precisam de mais do...", sugerindo segmentação por nicho (ex. saúde). Post recente identificado: "Gente, nona edição da minha imersão. Já entrei com cento..." — sugere realização de imersões/eventos pagos.

#### CTA dominante (Padrão + Variações)
**limitacao_dados:** nenhum exemplo exato de CTA encontrado.

#### Tom de voz (adjetivos + frases exemplo)
**limitacao_dados:** nenhuma frase de tom de voz verificada.

#### Métricas estimadas (tamanho médio, formato, frequência)
**limitacao_dados:** número de seguidores/posts não encontrado. Multiplataforma confirmada (TikTok com mesmo handle).

#### Top conteúdos identificados

| # | Tipo | Tema | Hook | Performance Est. |
|---|---|---|---|---|
| 1 | Série/Reels | Nicho saúde | "EP 06: Profissionais da saúde não precisam de mais do..." | Não determinável |
| 2 | Reels | Imersão/evento pago | "Gente, nona edição da minha imersão..." | Não determinável |

---

### @eujoaotorresz

**Categoria:** creator (tags: negocio-digital)

**limitacao_dados parcial/relevante:** o handle exato "@eujoaotorresz" não retornou resultados. As buscas convergiram para **@joaotorresz** (sem o prefixo "eu"), perfil de "João Torres" indicado como sendo de **Portugal**, com ~2.039 seguidores, 1.038 seguindo, apenas 5 posts, bio listando afiliações a marcas/eventos portugueses (@connect.lapunta, @ups_ofir, @sliceoficial, @clyma.pt, @auraproject__, @finalexam.pt, @unlockeventos, @thepromoficial).

**Não há evidência de que @joaotorresz (Portugal, 5 posts, sem menção a negócio digital/IA/marketing) seja o mesmo perfil que @eujoaotorresz** (Brasil, categoria creator, tag negócio-digital) cadastrado em `config/profiles.json`. Podem ser homônimos diferentes, ou o handle pode ter mudado. Nenhum dado confiável (bio, hook, CTA, tom de voz, formato, engajamento) pôde ser atribuído com confiança ao perfil pedido. **Recomendação: verificação manual do handle exato antes de qualquer inferência adicional.**

---

### @gabriel.adamuchi

**Categoria:** creator (tags: ia, negocio-digital) · **Nome:** "IA Fácil" · **Bio (fonte indireta/TikTok espelhado):** "Aprenda IA de forma descomplicada!"

#### Padrões de Hook identificados (Fase 1 — instagram-content-cloner)
**limitacao_dados:** nenhum hook de abertura de reel completo encontrado. Conteúdo confirmado: prompts de IA prontos para uso (ex.: prompt de Natal "Ultra-realistic humorous Christmas scene..."), guias e cursos.

#### Estrutura típica do conteúdo
Posicionamento: ensinar IA de forma simples e monetização com IA. Temas confirmados: guias sobre Claude ("Não se fala em outra coisa a não ser CLAUDE, né?"), conteúdo institucional sobre uso prático de ferramentas de IA.

#### CTA dominante (Padrão + Variações)
**Confirmado com múltiplos exemplos exatos** — padrão claro e repetido de palavra-chave em comentário:
- "Comenta 'CURSO' que te mando os links na DM."
- "🤖 Comenta 'MINE' que te envio todos os prompts pela DM."
- "⚠️Comenta 'PROMPT' para receber na DM."
- "Comenta 'CLAUDE' que te mando o guia completo pela DM."
- "⚠️Comenta 'IA' para receber o guia pela DM."

Classificação: palavra-chave em comentário (engagement bait para DM automatizada/funil de mensagens).

#### Tom de voz (adjetivos + frases exemplo)
**limitacao_dados:** nenhuma frase encontrada que permita atribuir tom de voz com 3-5 adjetivos com confiança.

#### Métricas estimadas (tamanho médio, formato, frequência)
**limitacao_dados:** número exato de seguidores/posts do Instagram não encontrado (apenas TikTok com a mesma marca, ~195,2K seguidores — não deve ser usado como proxy direto do IG). Multiplataforma: YouTube (@GabrielAdamuchi), Facebook. Formato dominante: Reels (todos os exemplos de CTA vêm de reel/post em vídeo curto). Engajamento provavelmente médio-alto (sinal indireto: marca replicada em múltiplas plataformas, funil de captura de leads estruturado).

#### Top conteúdos identificados

| # | Tipo | Tema | Hook | Performance Est. |
|---|---|---|---|---|
| 1 | Reels | Prompt de Natal (geração de imagem) | "Ultra-realistic humorous Christmas scene..." | Não determinável |
| 2 | Reels | Guia sobre Claude | "Não se fala em outra coisa a não ser CLAUDE, né?" | Não determinável |
| 3 | Reels | Captura de leads via DM | "Comenta 'CLAUDE' que te mando o guia completo pela DM." | Médio-alto (sinal indireto: funil estruturado, replicado em 3 plataformas) |

## Perfis Sugeridos pelo Sistema

N/A — `config/profiles.json` já contém 58 perfis ativos cadastrados (16 processados nesta rodada conforme divisão de lote); modo de descoberta automática não foi acionado.

## Limitações de Dados

- **@nathanhodgson** — handle cadastrado em `config/profiles.json` não corresponde a nenhum perfil ativo no nicho de IA; o perfil correto identificado é @nathanhodgson.ai. Hook, CTA e formato não confirmados.
- **@geracaotechs** — seguidores e número de posts não encontrados em nenhuma busca. CTA não encontrado.
- **@lonamkt** — dados fortemente inconsistentes (4.316 seguidores, apenas 2 posts indexados) vs. notoriedade externa de Felipe Lona. Recomenda-se reverificação manual.
- **@nikolassfaria** — perfil não localizado via WebSearch. Possível candidato por similaridade fonética: @nikolassasso (não confirmado como o mesmo perfil).
- **@jonylan** — nenhum hook exato encontrado; CTA e formato dominante são apenas inferência cross-platform (TikTok).
- **@laschuk** — hook parcial/cortado nas fontes; CTA exato não encontrado. Métricas "25% open rate, 4% CTR, 42 ROAS" pertencem a uma página de vendas de curso, não ao Instagram — não devem ser confundidas com dados do perfil.
- **@anatex** — nenhum hook exato nem CTA exato encontrado; formato dominante não confirmado.
- **@marianatorre.s** — perfil não localizado via WebSearch em nenhuma variação testada. Recomenda-se verificação manual do handle.
- **@amandadinizmkt** — dados mínimos: sem seguidores, hook, CTA ou tom de voz confirmados.
- **@eujoaotorresz** — o resultado mais próximo encontrado (@joaotorresz, Portugal, 5 posts) provavelmente não é o mesmo perfil cadastrado (Brasil, negócio digital). Recomenda-se verificação manual do handle antes de qualquer inferência futura.
- **@leandroladeiran** — hook e CTA exatos não confirmados (CTAs do tipo "comenta X" encontrados pertencem a outro perfil do grupo).
- **@gabriel.adamuchi** — número de seguidores/posts do Instagram não encontrado (apenas proxy via TikTok); tom de voz não confirmado.
