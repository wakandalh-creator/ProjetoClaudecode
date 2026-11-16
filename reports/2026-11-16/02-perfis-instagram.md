# Análise de Perfis Instagram — 2026-11-16

## Nota Metodológica Importante

Esta execução do Módulo 2 rodou em MODO ANÁLISE sobre os 61 perfis ativos de `config/profiles.json`, processados em 13 lotes de até 5 perfis via sub-agentes paralelos (general-purpose, WebSearch + tentativas de WebFetch), seguindo as regras de segurança do swarm do projeto (lotes de 5, concorrência máxima 3, anti-alucinação).

**instagram.com e a maioria dos agregadores de terceiros (creatordb.app, viralbrain.ai, motionapp.com, reportei.com, etc.) estão bloqueados na rede desta sessão de nuvem (`ENOTFOUND` em toda tentativa de WebFetch)** — todo o levantamento foi feito exclusivamente via WebSearch (snippets de resultados), sem acesso direto a nenhuma página do Instagram ou de agregador.

**Resultado é consistente com as execuções anteriores (2026-11-02, 2026-11-09):** a esmagadora maioria dos 61 handles monitorados não é indexada pelo WebSearch — nem posts, nem captions, nem métricas, nem sequer menções de terceiros. **12 de 61 perfis** retornaram algum indício real, sempre via snippets de agregadores/sites de terceiros não oficiais (creatordb.app, reportei.com, motionapp.com, thehandbook.com) — nunca uma caption ou hook literal visto diretamente em um post: **@charliehills, @nick_saraev, @nathanhodgson, @chase.h.ai, @nikolassasso, @leandroladeiran, @oneyaraujo, @geracaotechs, @human___academy, @anatex, @lindsay.ia, @noevarner**. Os demais **49 perfis** ficaram com `limitacao_dados` preenchido e nenhum dado real.

**Recomendação para o Lucas (reforçando execuções anteriores):** considerar conectar um MCP/skill de scraping de Instagram autorizado (API oficial ou serviço de terceiros com acesso de rede liberado para esta sessão) para que o Módulo 2 tenha dados reais em execuções futuras — WebSearch isoladamente continua insuficiente para a grande maioria dos perfis monitorados, mesmo após três execuções consecutivas.

---

## Visão Geral dos Perfis

| Perfil | Categoria | Formato Dominante | Engajamento | Hook Padrão / Status |
|--------|-----------|------------------|-------------|------------------------|
| @charliehills | creator | misto | baixo | outro (ver detalhes) |
| @yikC | creator | misto | baixo | dados insuficientes |
| @eujoaotorresz | creator | misto | baixo | dados insuficientes |
| @fabianocarvalhojr | founder | misto | baixo | dados insuficientes |
| @rafa.grandi | marketing | misto | baixo | dados insuficientes |
| @brusantanna.ai | ia | misto | baixo | dados insuficientes |
| @vendedorglobal | negocio-digital | misto | baixo | dados insuficientes |
| @oluizmain | creator | misto | baixo | dados insuficientes |
| @nick_saraev | automacao | misto | medio | outro (ver detalhes) |
| @nathanhodgson | ia | misto | baixo | outro (ver detalhes) |
| @ai | ia | misto | baixo | dados insuficientes |
| @ana.gsoares | marketing | misto | baixo | dados insuficientes |
| @chase.h.ai | ia | misto | medio | outro (ver detalhes) |
| @leosoares.ia | ia | misto | baixo | dados insuficientes |
| @gabriel.adamuchi | creator | misto | baixo | dados insuficientes |
| @viverdeia.ai | ia | misto | baixo | dados insuficientes |
| @ninja.automacoes | automacao | misto | baixo | dados insuficientes |
| @nikolassasso | creator | misto | baixo | outro (ver detalhes) |
| @eduardocavalcanti | founder | misto | baixo | dados insuficientes |
| @jonylan | creator | misto | baixo | dados insuficientes |
| @allesinisgalli | founder | misto | baixo | dados insuficientes |
| @lonamkt | marketing | misto | baixo | dados insuficientes |
| @gabrielbarbosa.oficial | creator | misto | baixo | dados insuficientes |
| @opensession.co | agencia | misto | baixo | dados insuficientes |
| @leandroladeiran | marketing | misto | medio | outro (ver detalhes) |
| @christiantriad | creator | misto | baixo | dados insuficientes |
| @oneyaraujo | creator | reels | medio | outro (ver detalhes) |
| @geracaotechs | ia | reels | alto | outro (ver detalhes) |
| @amandadinizmkt | marketing | misto | baixo | dados insuficientes |
| @human___academy | ia | misto | baixo | outro (ver detalhes) |
| @geiss11 | creator | misto | baixo | dados insuficientes |
| @nelmoricalde | creator | misto | baixo | dados insuficientes |
| @rodrigotadewald | marketing | misto | baixo | dados insuficientes |
| @sujeitoprogramador | ia | misto | baixo | dados insuficientes |
| @jonathan_kamargo | creator | misto | baixo | dados insuficientes |
| @marianatorre.s | marketing | misto | baixo | dados insuficientes |
| @marketerhub.ai | marketing | misto | baixo | dados insuficientes |
| @marcelaluzzio | marketing | misto | baixo | dados insuficientes |
| @gestordeaudiencia | marketing | misto | baixo | dados insuficientes |
| @sebintel | ia | misto | baixo | dados insuficientes |
| @avora.ai | agencia | misto | baixo | dados insuficientes |
| @ogabrieeldias | creator | misto | baixo | dados insuficientes |
| @rodrigobindes | founder | misto | baixo | dados insuficientes |
| @franklim.gui | creator | misto | baixo | dados insuficientes |
| @gabrielsamp.ai | ia | misto | baixo | dados insuficientes |
| @maestrosdaia | ia | misto | baixo | dados insuficientes |
| @brandsdecoded__ | marketing | misto | baixo | dados insuficientes |
| @anatex | creator | misto | baixo | outro (ver detalhes) |
| @larissagomes.ia | ia | misto | baixo | dados insuficientes |
| @thiagozaao | creator | misto | baixo | dados insuficientes |
| @neuwebstudio | agencia | misto | baixo | dados insuficientes |
| @laschuk | founder | misto | baixo | dados insuficientes |
| @maestroptompts | ia | misto | baixo | dados insuficientes |
| @faladantasmkt | marketing | misto | baixo | dados insuficientes |
| @lindsay.ia | ia | misto | baixo | outro (ver detalhes) |
| @andrevictor.m | marketing | misto | baixo | dados insuficientes |
| @drisiano | creator | misto | baixo | dados insuficientes |
| @brun0gpt | ia | misto | baixo | dados insuficientes |
| @maxcarrau.ia | ia | misto | baixo | dados insuficientes |
| @noevarner | creator | reels | medio | outro (ver detalhes) |
| @yikchanltd | creator | misto | baixo | dados insuficientes |

---

## Análise Detalhada por Perfil

### @charliehills

**Categoria:** creator

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post, caption ou hook original encontrado via WebSearch; apenas descrição de nicho/parcerias em agregador de terceiros"

#### Estrutura típica do conteúdo
```
Não identificada — nenhuma estrutura de post real encontrada; fontes de terceiros descrevem apenas o nicho do criador (educação prática sobre IA) e parcerias de marca, sem detalhar formato dos posts.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Temas identificados
- educação prática sobre IA
- parceria de marca com Zapier (#zapierpartner)
- parceria com ServiceNow
- ferramentas de geração de vídeo por IA

#### Limitação de dados
Queries tentadas: (1) '"charliehills" instagram posts reels 2026 site:instagram.com OR "charliehills" instagram conteúdo' e (2) WebFetch direto em instagram.com/charliehills e em creatordb.app/creatorstats/charliehills. Nenhum post, caption, hook ou CTA real foi encontrado. WebFetch falhou em ambas as URLs (ENOTFOUND — hosts fora da allowlist de rede desta sessão de nuvem). A única evidência disponível veio de snippets do WebSearch sobre páginas de terceiros: (a) creatordb.app (agregador, não post original) descreve o criador como britânico, focado em educação prática de IA, parceiro oficial Zapier e com menções a ServiceNow — dados datados de 5/set/2026, podem estar desatualizados; (b) artigo da theaireport.ai sobre a 'fórmula' do criador para crescer no LinkedIn/Instagram com IA, mas o conteúdo detalhado é sobre crescimento no LinkedIn (210k+ seguidores), sem descrever hooks, CTAs, estrutura ou engajamento específicos do Instagram. Nenhum hook, CTA, texto de post ou métrica de engajamento foi inventado.

---

### @yikC

**Categoria:** creator

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Temas identificados
- Nenhum tema real identificado (dados insuficientes)

#### Limitação de dados
Nenhuma conta, post, caption, hook ou menção de terceiro sobre @yikC foi encontrada em 2 queries WebSearch. Os resultados retornaram apenas perfis com nomes parecidos e não relacionados (ex.: @yk / Lee Yik Keat, yikfei99, yikes_cg, ykxc.skt), nenhum confirmado como o mesmo perfil. instagram.com está fora da allowlist de rede desta sessão (ENOTFOUND). Nenhum dado foi inventado.

---

### @eujoaotorresz

**Categoria:** creator

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Temas identificados
- Nenhum tema real identificado (dados insuficientes)

#### Limitação de dados
Nenhuma conta, post, caption, hook ou menção de terceiro sobre @eujoaotorresz foi encontrada em 2 queries WebSearch. Os resultados retornaram apenas perfis com nomes parecidos e não relacionados (ex.: @joanatorres_, @joeltorresstyle, @edimartorres, @eujoaomatheuus, @joaotanusz), nenhum confirmado como o mesmo perfil. Nenhum dado foi inventado.

---

### @fabianocarvalhojr

**Categoria:** founder

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Temas identificados
- Nenhum tema real identificado (dados insuficientes)

#### Limitação de dados
Nenhuma conta, post, caption, hook ou menção de terceiro sobre @fabianocarvalhojr foi encontrada em 2 queries WebSearch. Os resultados retornaram apenas perfis com nomes parecidos e não relacionados (ex.: @phabiogram, @fabiano.moraes, @fabiojroficial, @fabianobeltrame15, @fabianno_oliveira, @fabuusjunior), além de artigos genéricos sobre carrosséis e Reels em 2026. Nenhum dado foi inventado.

---

### @rafa.grandi

**Categoria:** marketing

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Temas identificados
- Nenhum tema real identificado (dados insuficientes)

#### Limitação de dados
Nenhuma conta, post, caption, hook ou menção de terceiro sobre @rafa.grandi foi encontrada em 2 queries WebSearch. Os resultados retornaram apenas perfis com nomes parecidos e não relacionados (ex.: @rafa_bf, @rafaavitti, @antoniograndiofficial, @rafa.pics, @rafamattei, @ppteamrafa), além de guias genéricos sobre como viralizar no Instagram em 2026. Nenhum dado foi inventado.

---

### @brusantanna.ai

**Categoria:** ia

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Temas identificados
- Nenhum tema real identificado (dados insuficientes)

#### Limitação de dados
Queries tentadas: '"brusantanna.ai" instagram posts reels 2026 site:instagram.com OR "brusantanna.ai" instagram conteúdo'; '"brusantanna.ai" instagram viral OR "brusantanna" instagram IA'; 'brusantanna instagram criadora conteúdo IA perfil'; 'brusantanna.ai favikon OR creatordb OR viralbrain'. WebFetch direto em instagram.com/brusantanna.ai falhou (host bloqueado na rede da sessão — fora do allowlist). Nenhuma menção ao handle, a conteúdo publicado ou a agregadores de criadores foi encontrada em nenhuma busca. Nenhum dado real disponível.

---

### @vendedorglobal

**Categoria:** negocio-digital

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Temas identificados
- Nenhum tema real identificado (dados insuficientes)

#### Limitação de dados
Queries tentadas: '"vendedorglobal" instagram posts reels 2026 site:instagram.com OR "vendedorglobal" instagram conteúdo'; '"vendedorglobal" site:instagram.com OR "vendedorglobal" instagram viral'; 'vendedorglobal instagram dropshipping negócio digital creator'. WebFetch direto ao perfil não foi tentado novamente após falha de rede confirmada em instagram.com (host bloqueado). Nenhuma menção ao handle exato foi encontrada em nenhum resultado — apenas conteúdo genérico sobre dropshipping/vendas no Instagram, sem relação confirmada com este perfil. Nenhum dado real disponível.

---

### @oluizmain

**Categoria:** creator

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Temas identificados
- Nenhum tema real identificado (dados insuficientes)

#### Limitação de dados
Queries tentadas: '"oluizmain" instagram posts reels 2026 site:instagram.com OR "oluizmain" instagram conteúdo'; '"oluizmain" site:instagram.com OR "o luiz main" instagram viral creator'; 'oluizmain instagram quem é criador conteúdo'. WebFetch direto ao perfil não foi tentado após confirmação de bloqueio de instagram.com na rede da sessão. Nenhum resultado mencionou este handle especificamente; o único quase-match ('mrolumaintain', criador nigeriano) é claramente um perfil diferente. Nenhum dado real disponível.

---

### @nick_saraev

**Categoria:** automacao

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum hook, caption ou post original encontrado; apenas descrições de terceiros sobre o nicho de conteúdo"

#### Estrutura típica do conteúdo
```
Dados insuficientes para estrutura de post. Segundo agregadores de terceiros (creatordb.app, automationatlas.io, viralbrain.ai — não verificados diretamente), o conteúdo gira em torno de automação com n8n, agências de IA e automação de atendimento/outbound, voltado para o público do programa 'Maker School' do criador.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: medio

#### Temas identificados
- automação com n8n
- agências de IA / outbound automation
- AI calling agents
- programa educacional (Maker School)

#### Limitação de dados
Queries tentadas: '"nick_saraev" instagram posts reels 2026 site:instagram.com OR "nick saraev" instagram automation content'. Encontradas menções em agregadores de terceiros (creatordb.app/creatorstats/nicksaraev, automationatlas.io/creators/nick-saraev, viralbrain.ai/heroes/nick-saraev) confirmando a existência do perfil (instagram.com/nick_saraev) e o nicho de conteúdo (automação/n8n/agências de IA), com audiência combinada YouTube+Instagram citada como >1M seguidores por uma fonte (não verificado). WebFetch direto a esses agregadores (creatordb.app, viralbrain.ai) e ao Instagram falhou — hosts bloqueados pela rede da sessão (fora do allowlist). Nenhum hook, caption, CTA ou número de engajamento específico do Instagram foi encontrado; os números citados são de audiência agregada entre plataformas, não de posts individuais, e vêm de agregadores não-oficiais, não de posts vistos diretamente.

---

### @nathanhodgson

**Categoria:** ia

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum hook, caption ou post original encontrado; apenas descrições de terceiros sobre temas de vídeo"

#### Estrutura típica do conteúdo
```
Dados insuficientes para estrutura de post. Segundo agregadores de terceiros (motionapp.com, creatordb.app — não verificados diretamente), o criador publica vídeos curtos demonstrando ferramentas de IA para código, design e automação de negócios (ex.: tutoriais de Claude, prototipagem interativa).
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Temas identificados
- tutoriais de IA (Claude, ferramentas de design/código)
- automação de negócios
- técnica de prompting 'Claude Council'
- parcerias com marcas (Descript, Perplexity AI, Arcads AI, Durable, Suno)

#### Limitação de dados
Queries tentadas: '"nathanhodgson" instagram posts reels OR "nathan hodgson" instagram AI content'. Encontradas menções em agregadores de terceiros (motionapp.com/creator/nathan-hodgson, creatordb.app/creatorstats/nathanhodgsonai) descrevendo temas de conteúdo (tutoriais de IA, ex. 'Claude Council', automação de CV/candidaturas) e handles possivelmente divergentes (@nathanhodgson_ no Motion vs. @nathanhodgson.ai no CreatorDB) — não confirmado qual é o atual. WebFetch direto a creatordb.app e ao Instagram falhou — hosts bloqueados pela rede da sessão. Claims de parcerias com Google/Meta/OpenAI/Anthropic citados pelo agregador não foram verificados. Nenhum hook, caption, CTA ou número de engajamento real do Instagram foi encontrado diretamente; tudo vem de descrições de terceiros, não de posts vistos.

---

### @ai

**Categoria:** ia

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Temas identificados
- Nenhum tema real identificado (dados insuficientes)

#### Limitação de dados
WebFetch direto em instagram.com/ai/ falhou (host não resolvido/bloqueado na rede da sessão). Tentei três buscas WebSearch variadas. Nenhuma resultou em identificação do dono do handle @ai, posts, captions ou menções de terceiros específicas a esse perfil — apenas artigos genéricos sobre IA no Instagram e outros handles parecidos (@artificialintelligence, @ai_breeeze). Handle de 2 caracteres é extremamente disputado/provavelmente institucional ou inativo; não há evidência pública acessível via busca.

---

### @ana.gsoares

**Categoria:** marketing

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Temas identificados
- Nenhum tema real identificado (dados insuficientes)

#### Limitação de dados
instagram.com bloqueado na rede da sessão. Três buscas WebSearch tentadas — nenhuma retornou qualquer página, post, agregador ou menção de terceiros para esse handle exato. Resultados trouxeram apenas perfis de nomes parecidos, não relacionados. Não há dado público acessível via busca para este perfil.

---

### @chase.h.ai

**Categoria:** ia

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes para hooks/captions — apenas dados agregados de audiência foram encontrados (ver limitacao_dados)"

#### Estrutura típica do conteúdo
```
Dados insuficientes (nenhuma transcrição de post/reel encontrada).
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: medio

#### Temas identificados
- IA e tecnologia (geral, segundo agregador)
- estratégias práticas de uso de ferramentas de IA/Claude Code (segundo agregador)

#### Limitação de dados
Nenhum post, caption ou hook original foi encontrado ou visto diretamente — WebFetch em instagram.com/chase.h.ai e em creatordb.app/creatorstats/chase.h.ai falhou (hosts bloqueados/não resolvidos). Via WebSearch, encontrei apenas dados de TERCEIRO/AGREGADOR (creatordb.app via snippets): nicho 'IA & Tecnologia', ~228.550 seguidores Instagram, ~163.000 YouTube, ~137.700 TikTok, 'designação ChatGPT Partner'. Esses números não foram verificados diretamente no Instagram e o próprio agregador avisa que parte do conteúdo é gerado por IA — tratar com cautela. Nenhum hook, CTA, estrutura de post ou taxa de engajamento real foi encontrado; valores de 'engajamento_estimado'/'formato_dominante' são estimativas de baixa confiança.

---

### @leosoares.ia

**Categoria:** ia

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Temas identificados
- Nenhum tema real identificado (dados insuficientes)

#### Limitação de dados
Três buscas WebSearch tentadas. Nenhuma retornou qualquer resultado contendo o handle exato — nem posts, nem agregadores (creatordb/favikon/hypeauditor), nem menções de terceiros. Resultados trouxeram apenas perfis de outros 'Leo/Léo' não relacionados e artigos genéricos sobre Reels/IA em 2026. Não há dado público acessível via busca para este perfil.

---

### @gabriel.adamuchi

**Categoria:** creator

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Temas identificados
- Nenhum tema real identificado (dados insuficientes)

#### Limitação de dados
Duas buscas WebSearch tentadas. Nenhuma retornou qualquer resultado contendo esse nome/handle exato — nem posts, nem agregadores (creatordb/favikon/socialveins/hypeauditor), nem menções de terceiros. Resultados trouxeram apenas outros criadores chamados 'Gabriel' sem relação. Não há dado público acessível via busca para este perfil.

---

### @viverdeia.ai

**Categoria:** ia

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Não identificado — nenhuma informação real encontrada sobre o perfil.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Temas identificados
- Nenhum tema real identificado (dados insuficientes)

#### Limitação de dados
WebSearch padrão + ampliada retornaram apenas artigos genéricos sobre IA/Reels/2026 sem menção ao perfil ou domínio. WebFetch direto em instagram.com/viverdeia.ai falhou (ENOTFOUND). Nenhum dado real encontrado.

---

### @ninja.automacoes

**Categoria:** automacao

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Não identificado — nenhuma informação real encontrada sobre o perfil.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Temas identificados
- Nenhum tema real identificado (dados insuficientes)

#### Limitação de dados
Resultados foram apenas guias genéricos de automação de Instagram com n8n e um produto não relacionado ('Insta Ninja'). Nenhuma menção direta ou de terceiros ao perfil @ninja.automacoes foi encontrada.

---

### @nikolassasso

**Categoria:** creator

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum hook, caption ou texto de post real encontrado; apenas descrição de nicho via agregador de terceiros"

#### Estrutura típica do conteúdo
```
Não identificado — nenhum post individual encontrado. Segundo descrição agregada de terceiro (creatordb.app, via snippet de busca), o criador é descrito como educador de marketing digital/negócio online, com conteúdo associado a um método de 'vender sem aparecer' e vídeos gerados com IA.
```

#### CTA dominante
- Padrão: Dados insuficientes — nenhuma CTA real encontrada.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Temas identificados
- marketing digital
- negócio online
- método 'vender sem aparecer'
- vídeo gerado com IA

#### Limitação de dados
Snippet de busca referente a creatordb.app/creatorstats/nikolassasso/, descrevendo educador de marketing digital brasileiro (~250K seguidores combinados YouTube+Instagram), com bio mencionando vídeo gerado por IA e método 'sem aparecer', nota de que atividade no Instagram 'diminuiu consideravelmente'. WebFetch direto em creatordb.app falhou (ENOTFOUND). Nenhum número de engajamento, hook ou CTA real foi visto — temas vêm da descrição de nicho do agregador, não de posts específicos.

---

### @eduardocavalcanti

**Categoria:** founder

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção confirmada encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Não identificado — nenhuma informação real e confirmada encontrada sobre este perfil específico.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Temas identificados
- Nenhum tema real identificado (dados insuficientes)

#### Limitação de dados
Listagem em thehandbook.com (agregador de influenciadores) para um 'Eduardo Cavalcanti' com alcance de 25.996 e taxa de engajamento de 1,3%, mas sem expor @handle nem confirmar vínculo com este perfil (nome comum; outros resultados trazem homônimos não relacionados). Tratado como dado não verificado/insuficiente. Nenhum post, hook, CTA ou conteúdo real foi encontrado.

---

### @jonylan

**Categoria:** creator

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Não identificado — nenhuma informação real encontrada sobre o perfil.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Temas identificados
- Nenhum tema real identificado (dados insuficientes)

#### Limitação de dados
Retornos apenas conteúdo genérico sobre tendências de Reels em 2026 e perfis de terceiros com nomes parecidos mas não correspondentes (jonahwasylak, jonathanhlyon, jonwands). Nenhuma menção real ao handle @jonylan foi encontrada.

---

### @allesinisgalli

**Categoria:** founder

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Temas identificados
- Nenhum tema real identificado (dados insuficientes)

#### Limitação de dados
Duas queries WebSearch tentadas. Nenhum resultado retornou o handle exato — apenas correspondências soltas de nomes parecidos (Alessia Galli fotógrafa, LuisaGallia, playgalliano, etc.), sem relação confirmada. Nenhum post, menção de terceiro ou dado de agregador encontrado. WebFetch não tentado (bloqueio de rede conhecido).

---

### @lonamkt

**Categoria:** marketing

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Temas identificados
- Nenhum tema real identificado (dados insuficientes)

#### Limitação de dados
Duas queries WebSearch tentadas. Nenhum resultado mencionou o handle — apenas artigos genéricos de tendências de Instagram/Reels 2026 em português. Nenhum post, menção de terceiro ou dado de agregador encontrado para esse perfil.

---

### @gabrielbarbosa.oficial

**Categoria:** creator

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Temas identificados
- Nenhum tema real identificado (dados insuficientes)

#### Limitação de dados
Duas queries WebSearch tentadas. Resultados retornaram apenas conteúdo sobre o jogador de futebol Gabriel 'Gabigol' Barbosa, mas NENHUMA fonte confirmou que esse handle pertence a ele ou a qualquer pessoa específica — sem confirmação de vínculo. Nenhum post original, caption real ou dado de engajamento encontrado para o handle exato.

---

### @opensession.co

**Categoria:** agencia

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Temas identificados
- Nenhum tema real identificado (dados insuficientes)

#### Limitação de dados
Duas queries WebSearch tentadas. Nenhum resultado mencionou o domínio/handle — apenas artigos genéricos sobre tendências de Reels 2026 e páginas de agências de marketing não relacionadas. Nenhum post, menção de terceiro ou dado de agregador encontrado.

---

### @leandroladeiran

**Categoria:** marketing

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post, caption ou hook real encontrado; apenas descrição genérica de nicho via agregador de terceiros (CreatorDB)"

#### Estrutura típica do conteúdo
```
Dados insuficientes — nenhum post real analisado; apenas descrição de nicho via agregador de terceiros.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: medio

#### Temas identificados
- marketing digital e produtos digitais
- estratégias para ganhar dinheiro online
- empreendedorismo

#### Limitação de dados
Duas queries WebSearch retornaram a mesma fonte secundária: creatordb.app/creatorstats/leandroladeiran/ (agregador de terceiros, dados de 08/10/2026), descrevendo o criador como brasileiro focado em marketing digital/produtos digitais, com mais de 2 milhões de seguidores no Instagram. WebFetch direto em creatordb.app falhou (ENOTFOUND — host bloqueado na rede da sessão). Nenhum post original, caption, hook, CTA ou métrica de engajamento real foi encontrado — apenas essa descrição de nicho/alcance via agregador. engajamento_estimado marcado 'medio' apenas pela escala de seguidores reportada (>2M), sem confirmação de taxa de engajamento real.

---

### @christiantriad

**Categoria:** creator

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Temas identificados
- Nenhum tema real identificado (dados insuficientes)

#### Limitação de dados
Três queries WebSearch tentadas. Nenhuma trouxe qualquer página, perfil, agregador ou menção de terceiros sobre essa handle especificamente. WebFetch direto em instagram.com/christiantriad falhou (ENOTFOUND, host bloqueado nesta sessão). Nenhum dado real encontrado para este perfil.

---

### @oneyaraujo

**Categoria:** creator

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "Nenhum hook literal (caption/post original) encontrado. Fonte secundária (reportei.com, via snippet do WebSearch) descreve o perfil como focado em Reels virais, crescimento de seguidores e monetização de audiência."

#### Estrutura típica do conteúdo
```
Não identificada a partir de posts reais. Fonte de terceiros descreve conteúdo educativo sobre como viralizar, ganhar seguidores e monetizar via Reels, associado a um treinamento próprio chamado 'Código Viral®'.
```

#### CTA dominante
- Padrão: Dados insuficientes — nenhuma caption ou CTA original encontrado.

#### Tom de voz
- Adjetivos: educativo (inferido de fonte secundária), estratégico (inferido de fonte secundária)
- Exemplo de frase característica: "Dados insuficientes — nenhuma frase original de post encontrada."

#### Métricas estimadas
- Formato mais usado: reels
- Engajamento estimado: medio

#### Temas identificados
- viralização no Instagram
- crescimento de seguidores
- monetização de audiência
- Reels estratégicos (treinamento 'Código Viral®')

#### Limitação de dados
Nenhum post original visto diretamente — WebFetch em reportei.com/oney-araujo-quem-e/ e www.instagram.com falhou (ENOTFOUND, hosts bloqueados nesta sessão). Toda informação vem do snippet do WebSearch sobre reportei.com (agregador/artigo de terceiro), que cita '+1,3 milhão de seguidores' e o treinamento 'Código Viral®' — sem hooks, CTAs ou captions reais confirmados. Formato e engajamento são estimativas baseadas em descrição de terceiro, não em métricas verificadas.

---

### @geracaotechs

**Categoria:** ia

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "Nenhum hook literal encontrado. Agregador (motionapp.com, via snippet) descreve o perfil como voltado a plataformas online, ferramentas digitais e recomendações de sites para simplificar projetos DIY, design e tarefas do dia a dia."

#### Estrutura típica do conteúdo
```
Não identificada a partir de posts reais. Fonte de terceiros indica foco em dicas/ferramentas de tecnologia apresentadas em Reels.
```

#### CTA dominante
- Padrão: Dados insuficientes — nenhuma caption ou CTA original encontrado.

#### Tom de voz
- Adjetivos: prático (inferido de fonte secundária), utilitário (inferido de fonte secundária)
- Exemplo de frase característica: "Dados insuficientes — nenhuma frase original de post encontrada."

#### Métricas estimadas
- Formato mais usado: reels
- Engajamento estimado: alto

#### Temas identificados
- ferramentas digitais/apps
- recomendações de sites
- dicas de DIY e design

#### Limitação de dados
Nenhum post original visto diretamente — WebFetch em motionapp.com/creator/geracaotechs/ e www.instagram.com falhou (ENOTFOUND, hosts bloqueados). Dados vêm só do snippet do WebSearch sobre motionapp.com, que cita ~218.4K seguidores e 4 reels em destaque com 5,5M/4,7M/4,7M/3,8M visualizações (sem data confirmada). 'engajamento_estimado: alto' é estimativa baseada em números de visualização de terceiro, não em taxa de engajamento real medida.

---

### @amandadinizmkt

**Categoria:** marketing

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Temas identificados
- Nenhum tema real identificado (dados insuficientes)

#### Limitação de dados
Duas queries WebSearch tentadas. Nenhuma trouxe qualquer página, perfil, agregador ou menção de terceiros sobre essa handle exata — resultados mostraram apenas contas parecidas de outras 'Amandas' sem relação confirmada. WebFetch direto em instagram.com/amandadinizmkt falhou (ENOTFOUND, host bloqueado). Nenhum dado real encontrado para este perfil.

---

### @human___academy

**Categoria:** ia

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "Nenhum hook literal de post do Instagram encontrado. Um artigo de terceiro (acontecendoaqui.com.br, visto só via snippet) menciona que a marca Human Academy lançou um curso 'AI Video Creator' sobre criação audiovisual com IA."

#### Estrutura típica do conteúdo
```
Não identificada a partir de posts reais. Marca associada a cursos/treinamentos sobre produção audiovisual e vídeos com IA; não foi possível confirmar diretamente que o conteúdo do Instagram segue essa mesma linha ponto a ponto.
```

#### CTA dominante
- Padrão: Dados insuficientes — nenhuma caption ou CTA original encontrado.

#### Tom de voz
- Adjetivos: educativo (inferido), focado em IA/tecnologia (inferido)
- Exemplo de frase característica: "Dados insuficientes — nenhuma frase original de post encontrada."

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Temas identificados
- cursos de criação audiovisual com IA
- vídeos com IA (ex: curso 'AI Video Creator')

#### Limitação de dados
Nenhum post original do Instagram visto diretamente — WebFetch em www.humanacademy.ai, acontecendoaqui.com.br e www.instagram.com falhou (ENOTFOUND, hosts bloqueados). Toda informação vem de snippets do WebSearch sobre páginas de terceiros/da própria marca, sem confirmação de que sejam o conteúdo real postado em @human___academy. Não há métricas de engajamento, seguidores ou captions confirmadas.

---

### @geiss11

**Categoria:** creator

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Temas identificados
- Nenhum tema real identificado (dados insuficientes)

#### Limitação de dados
Duas queries WebSearch tentadas. Nenhum resultado correspondeu ao handle; retornaram apenas guias genéricos de Reels/viralização e perfis de terceiros não relacionados (ex.: robertgeiss_1964). instagram.com bloqueado na rede desta sessão (ENOTFOUND). Nenhum dado real encontrado.

---

### @nelmoricalde

**Categoria:** creator

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Temas identificados
- Nenhum tema real identificado (dados insuficientes)

#### Limitação de dados
Duas queries WebSearch tentadas. Nenhum resultado correspondeu ao handle; apenas perfis de terceiros com nomes parecidos (nelsonmoralesmx, nellcarmo, nelzaion, nelfaofficial) e páginas genéricas não relacionadas. Nenhum dado real encontrado.

---

### @rodrigotadewald

**Categoria:** marketing

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Temas identificados
- Nenhum tema real identificado (dados insuficientes)

#### Limitação de dados
Query padrão + busca ampliada 'Rodrigo Tadewald instagram'. Nenhum resultado correspondeu à pessoa/handle; apenas perfis homônimos/parecidos (Rodrigo Tadeu Lopes no LinkedIn, Rodrigo Trussardi, Rodrigo Teaser no HypeAuditor), nenhum confirmado como o mesmo perfil. Nenhum dado real encontrado.

---

### @sujeitoprogramador

**Categoria:** ia

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Temas identificados
- Nenhum tema real identificado (dados insuficientes)

#### Limitação de dados
Query padrão + 'sujeitoprogramador instagram viral reels'. Nenhum resultado correspondeu ao handle; apenas artigos genéricos sobre Reels/algoritmo do Instagram. WebFetch direto em instagram.com/sujeitoprogramador falhou com ENOTFOUND (confirmando bloqueio de rede). Nenhum dado real encontrado.

---

### @jonathan_kamargo

**Categoria:** creator

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Temas identificados
- Nenhum tema real identificado (dados insuficientes)

#### Limitação de dados
Duas queries WebSearch tentadas. Nenhum resultado correspondeu ao handle; apenas perfis homônimos parecidos (jonathan.maicelo2, ig_jonathangaming, jonathanheres). Nenhum dado real encontrado.

---

### @marianatorre.s

**Categoria:** marketing

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Temas identificados
- Nenhum tema real identificado (dados insuficientes)

#### Limitação de dados
Duas queries WebSearch tentadas + WebFetch direto em instagram.com/marianatorre.s (ENOTFOUND, host bloqueado). Nenhuma busca retornou resultados correspondentes a este handle; apenas contas de terceiros com nomes parecidos (@marianateranr, @maritorreblanca) em agregadores de analytics. Nenhum post, caption ou menção real foi encontrado.

---

### @marketerhub.ai

**Categoria:** marketing

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Temas identificados
- Nenhum tema real identificado (dados insuficientes)

#### Limitação de dados
Duas queries WebSearch tentadas. Nenhum resultado mencionou o domínio/handle ou seu conteúdo no Instagram; retornaram apenas guias genéricos de Reels/marketing 2026 e um perfil de ad-library de marca diferente ('Marketer HQ'). Nenhum dado real encontrado.

---

### @marcelaluzzio

**Categoria:** marketing

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Temas identificados
- Nenhum tema real identificado (dados insuficientes)

#### Limitação de dados
Duas queries WebSearch tentadas. Nenhum resultado correspondeu ao handle; apenas contas de terceiros com nomes parecidos (@marcelamarenco19, @marcelavacarezza_, @marcelotega) em agregadores de analytics, e artigos genéricos sobre viralização no Instagram.

---

### @gestordeaudiencia

**Categoria:** marketing

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Temas identificados
- Nenhum tema real identificado (dados insuficientes)

#### Limitação de dados
Duas queries WebSearch tentadas. Nenhum resultado correspondeu ao handle; apenas um perfil de terceiro com nome parecido (@gestordeperformance) em agregador, e artigos genéricos sobre engajamento/viralização no Instagram em 2026.

---

### @sebintel

**Categoria:** ia

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Temas identificados
- Nenhum tema real identificado (dados insuficientes)

#### Limitação de dados
Duas queries WebSearch tentadas. Nenhum resultado mencionou este termo/handle; retornaram apenas artigos genéricos sobre algoritmo/tendências de Reels em 2026 e contas de terceiros com nomes parecidos (@seblafrite, @sebas) sem relação.

---

### @avora.ai

**Categoria:** agencia

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Temas identificados
- Nenhum tema real identificado (dados insuficientes)

#### Limitação de dados
Duas queries WebSearch tentadas + WebFetch direto em instagram.com/avora.ai (ENOTFOUND). Nenhum resultado retornou o perfil, posts ou menções de terceiros sobre esse handle especificamente; resultados foram guias genéricos de Reels/IA ou perfis não relacionados. Nenhum dado real de conteúdo, hooks, CTAs ou engajamento foi encontrado.

---

### @ogabrieeldias

**Categoria:** creator

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Temas identificados
- Nenhum tema real identificado (dados insuficientes)

#### Limitação de dados
Duas queries WebSearch tentadas + WebFetch direto em instagram.com/ogabrieeldias (ENOTFOUND). Nenhum resultado correspondeu a esse handle; apareceram apenas contas com nomes parecidos (@ogabeoliveira, @gabriel, @gabrielfarias), descartadas. Nenhum dado real encontrado.

---

### @rodrigobindes

**Categoria:** founder

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Temas identificados
- Nenhum tema real identificado (dados insuficientes)

#### Limitação de dados
Duas queries WebSearch tentadas + WebFetch direto em instagram.com/rodrigobindes (ENOTFOUND). Nenhum resultado correspondeu ao handle; apenas contas com nomes parecidos (@rodrigobuenoms, @rodrigoamgoes, @rodrigocintra, @rodrigobocardi), descartadas. Nenhum dado real encontrado — possível que o handle esteja com grafia diferente, seja privado ou pouco indexado.

---

### @franklim.gui

**Categoria:** creator

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Temas identificados
- Nenhum tema real identificado (dados insuficientes)

#### Limitação de dados
Duas queries WebSearch tentadas + WebFetch direto em instagram.com/franklim.gui (ENOTFOUND). Nenhum resultado correspondeu ao handle; apenas contas parecidas (@franklindavid, @franklingt, @frankie729, @guiiclaudino), descartadas. Nenhum dado real encontrado.

---

### @gabrielsamp.ai

**Categoria:** ia

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Temas identificados
- Nenhum tema real identificado (dados insuficientes)

#### Limitação de dados
Duas queries WebSearch tentadas + WebFetch direto em instagram.com/gabrielsamp.ai (ENOTFOUND). Nenhum resultado correspondeu ao handle; apareceram apenas perfis de pessoas com nomes parecidos via Socialveins/HypeAuditor/Heepsy (@gabrielputh, @gabemichael_ai, @gabrielramos456), descartados. Nenhum dado real encontrado.

---

### @maestrosdaia

**Categoria:** ia

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Temas identificados
- Nenhum tema real identificado (dados insuficientes)

#### Limitação de dados
Duas queries WebSearch tentadas. Nenhuma retornou qualquer resultado relacionado ao handle — só perfis de nome parecido (@maestriasabia, @maestramieldemaple) em agregadores, sem relação confirmada. instagram.com bloqueado na rede (ENOTFOUND).

---

### @brandsdecoded__

**Categoria:** marketing

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Temas identificados
- Nenhum tema real identificado (dados insuficientes)

#### Limitação de dados
Duas queries WebSearch tentadas. Nenhuma retornou o perfil do Instagram. Único achado tangencial foi um Substack 'Decoding Brands' sem confirmação de vínculo com o handle — não usado como evidência. Nenhum post, hook, CTA ou métrica real encontrado.

---

### @anatex

**Categoria:** creator

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum hook/caption original encontrado via WebSearch; apenas descrição de nicho via agregador (CreatorDB): educador de IA que ensina profissionais a automatizar negócios e aumentar renda"

#### Estrutura típica do conteúdo
```
Dados insuficientes.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Temas identificados
- IA aplicada a negócios/automação (segundo descrição de nicho em agregador, não confirmado por post real)

#### Limitação de dados
Dados vieram SOMENTE de agregadores de terceiros (reportei.com: ~626 mil seguidores no Instagram; CreatorDB, dados de 22/09/2026: educador brasileiro de IA, ~1 milhão de seguidores somando Instagram+TikTok, YouTube citado como plataforma principal declarada mas Instagram com maior base/atividade). Nenhum post, caption, hook real, CTA ou métrica de engajamento de post específico foi encontrado ou visto diretamente. instagram.com bloqueado na rede (ENOTFOUND).

---

### @larissagomes.ia

**Categoria:** ia

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Temas identificados
- Nenhum tema real identificado (dados insuficientes)

#### Limitação de dados
Duas queries WebSearch tentadas. Nenhuma retornou qualquer página, post ou menção ao handle — apenas perfis de nome parecido (Larissa Tomásia, Larissa Guedes, Larissa Proença) via agregadores, e notícias genéricas sobre IA no Instagram. instagram.com bloqueado na rede (ENOTFOUND).

---

### @thiagozaao

**Categoria:** creator

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Temas identificados
- Nenhum tema real identificado (dados insuficientes)

#### Limitação de dados
Duas queries WebSearch tentadas. Nenhuma retornou o perfil ou qualquer menção ao handle — apenas perfis de nome parecido (@thiagaoofficial, @thiagotubao, @thiagoreis) via agregadores, sem relação confirmada. instagram.com bloqueado na rede (ENOTFOUND).

---

### @neuwebstudio

**Categoria:** agencia

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Temas identificados
- Nenhum tema real identificado (dados insuficientes)

#### Limitação de dados
Duas queries WebSearch tentadas. Nenhum resultado mencionou o handle; apenas artigos genéricos sobre Reels/2026. WebFetch direto em instagram.com/neuwebstudio falhou com ENOTFOUND (host bloqueado). Nenhum dado real de conteúdo foi encontrado.

---

### @laschuk

**Categoria:** founder

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Temas identificados
- Nenhum tema real identificado (dados insuficientes)

#### Limitação de dados
Duas queries WebSearch tentadas. Nenhum resultado exato; apenas perfis com nomes parecidos (@rxn_offpage, @shewchuk, @annchuk) em diretórios automatizados (Socialveins), sem relação confirmada. WebFetch direto em instagram.com/laschuk falhou com ENOTFOUND. Nenhum dado real de conteúdo foi encontrado.

---

### @maestroptompts

**Categoria:** ia

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Temas identificados
- Nenhum tema real identificado (dados insuficientes)

#### Limitação de dados
Duas queries WebSearch tentadas. Nenhum resultado mencionou o handle; apenas artigos genéricos sobre prompts de IA para Reels em 2026. Nenhum dado real de conteúdo foi encontrado.

---

### @faladantasmkt

**Categoria:** marketing

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Temas identificados
- Nenhum tema real identificado (dados insuficientes)

#### Limitação de dados
Duas queries WebSearch tentadas. Nenhum resultado mencionou o handle; apenas perfis parecidos (@falagabes, @falatcheoficial, @falavertao) em diretórios de influenciadores, sem relação confirmada. Nenhum dado real de conteúdo foi encontrado.

---

### @lindsay.ia

**Categoria:** ia

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post original ou caption real encontrado; apenas bio agregada de terceiro (creatordb.app) descrevendo o perfil como educadora de IA/automação"

#### Estrutura típica do conteúdo
```
Dados insuficientes — nenhum post real analisado. Agregador (creatordb.app) descreve apenas uma estratégia geral de 'comentário → DM': seguidor comenta uma palavra-gatilho no post e recebe por DM um guia ('29 Claude skills').
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Temas identificados
- Nenhum tema real identificado (dados insuficientes)

#### Limitação de dados
Único sinal real veio de duas páginas do agregador de terceiros creatordb.app, que descrevem o perfil como educadora de IA aplicada/automação sob a marca 'AI Money Hub', com ~40-45K seguidores (os dois números divergem entre si), consultoria 'Automate AI Consulting' e comunidade de +3.000 membros; e uma estratégia geral de funil comentário→DM (sem exemplo literal de hook ou CTA). WebFetch direto em creatordb.app falhou com ENOTFOUND. Todos os dados são de agregador/terceiro, não de um post original visto diretamente — tratar com cautela.

---

### @andrevictor.m

**Categoria:** marketing

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Temas identificados
- Nenhum tema real identificado (dados insuficientes)

#### Limitação de dados
Duas queries WebSearch tentadas. Nenhum resultado mencionou o handle exato; apenas contas com nomes parecidos (andrepiva, andrebellos, loud_victor). WebFetch em instagram.com/andrevictor.m falhou com ENOTFOUND. Nenhum dado real encontrado.

---

### @drisiano

**Categoria:** creator

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Temas identificados
- Nenhum tema real identificado (dados insuficientes)

#### Limitação de dados
Duas queries WebSearch tentadas. Nenhum resultado mencionou o handle exato; apenas perfis de nomes parecidos (dreiros, dri69, dresvi). Nenhum dado real encontrado.

---

### @brun0gpt

**Categoria:** ia

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Temas identificados
- Nenhum tema real identificado (dados insuficientes)

#### Limitação de dados
Duas queries WebSearch tentadas. Nenhum resultado mencionou o handle exato; apenas perfis de nomes parecidos com 'bruno/brun' e um perfil 'Brunobelissimo.Ai' não confirmadamente relacionado. Nenhum dado real encontrado.

---

### @maxcarrau.ia

**Categoria:** ia

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Temas identificados
- Nenhum tema real identificado (dados insuficientes)

#### Limitação de dados
Duas queries WebSearch tentadas. Nenhum resultado mencionou o handle exato; apenas perfis de nomes parecidos (max_true, maxprice3, the_max_ofc). Nenhum dado real encontrado.

---

### @noevarner

**Categoria:** creator

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post, caption ou hook real encontrado; apenas descrição genérica de perfil em agregador de terceiros (creatordb.app)"

#### Estrutura típica do conteúdo
```
Dados insuficientes — nenhum post real analisado.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: reels
- Engajamento estimado: medio

#### Temas identificados
- IA para negócios (educação/consultoria)

#### Limitação de dados
Página de agregador de terceiros (creatordb.app/creatorstats/noevarner.ai) descreve o perfil como educador/consultor de IA para negócios, audiência de nível médio e engajamento 'acima da média' (não verificado), ativo via Reels/Stories, também no YouTube. WebFetch direto nessa página falhou com ENOTFOUND. Nenhum hook, CTA ou caption real foi visto diretamente — formato_dominante e engajamento_estimado refletem apenas afirmação não verificada do agregador.

---

### @yikchanltd

**Categoria:** creator

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes — nenhum post real localizado.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Temas identificados
- Nenhum tema real identificado (dados insuficientes)

#### Limitação de dados
instagram.com bloqueado na rede desta sessão (ENOTFOUND). Via WebSearch, 4 queries tentadas (incluindo o termo isolado) — zero resultados sobre o handle, apenas handles parecidos de pessoas/empresas distintas (@yk, @yikfei99, @yicheng.0227) e empresas registradas no Reino Unido com grafia parecida (Ys Chan Ltd, YIKINC LTD, Yik Ho Holdings), sem vínculo confirmado. Não foi encontrado nenhum indício, positivo ou negativo, de relação entre @yikchanltd e o handle @yikC (já analisado em outro lote) — não há base para confirmar ou descartar essa hipótese.

---

## Perfis Sugeridos pelo Sistema
<!-- lista de perfis não estava vazia nesta execução — modo análise direto, sem descoberta -->

Não aplicável nesta execução (modo ANÁLISE — `config/profiles.json` já tinha perfis ativos).

---

## Limitações de Dados

- **instagram.com e agregadores de terceiros bloqueados na rede desta sessão** (`ENOTFOUND` em toda tentativa de WebFetch) — todo o levantamento desta execução foi feito exclusivamente via snippets de WebSearch, sem acesso direto a nenhuma página.

- @yikC — Nenhuma conta, post, caption, hook ou menção de terceiro sobre @yikC foi encontrada em 2 queries WebSearch. Os resultados retornaram apenas perfis com nomes parecidos e não relacionados (ex.: @yk / Lee Yik Keat, yikfei99, yikes_cg, ykxc.skt), nenhum confirmado como o mesmo perfil. instagram.com está fora da allowlist de rede desta sessão (ENOTFOUND). Nenhum dado foi inventado.
- @eujoaotorresz — Nenhuma conta, post, caption, hook ou menção de terceiro sobre @eujoaotorresz foi encontrada em 2 queries WebSearch. Os resultados retornaram apenas perfis com nomes parecidos e não relacionados (ex.: @joanatorres_, @joeltorresstyle, @edimartorres, @eujoaomatheuus, @joaotanusz), nenhum confirmado como o mesmo perfil. Nenhum dado foi inventado.
- @fabianocarvalhojr — Nenhuma conta, post, caption, hook ou menção de terceiro sobre @fabianocarvalhojr foi encontrada em 2 queries WebSearch. Os resultados retornaram apenas perfis com nomes parecidos e não relacionados (ex.: @phabiogram, @fabiano.moraes, @fabiojroficial, @fabianobeltrame15, @fabianno_oliveira, @fabuusjunior), além de artigos genéricos sobre carrosséis e Reels em 2026. Nenhum dado foi inventado.
- @rafa.grandi — Nenhuma conta, post, caption, hook ou menção de terceiro sobre @rafa.grandi foi encontrada em 2 queries WebSearch. Os resultados retornaram apenas perfis com nomes parecidos e não relacionados (ex.: @rafa_bf, @rafaavitti, @antoniograndiofficial, @rafa.pics, @rafamattei, @ppteamrafa), além de guias genéricos sobre como viralizar no Instagram em 2026. Nenhum dado foi inventado.
- @brusantanna.ai — Queries tentadas: '"brusantanna.ai" instagram posts reels 2026 site:instagram.com OR "brusantanna.ai" instagram conteúdo'; '"brusantanna.ai" instagram viral OR "brusantanna" instagram IA'; 'brusantanna instagram criadora conteúdo IA perfil'; 'brusantanna.ai favikon OR creatordb OR viralbrain'. WebFetch direto em instagram.com/brusantanna.ai falhou (host bloqueado na rede da sessão — fora do allowlist). Nenhuma menção ao handle, a conteúdo publicado ou a agregadores de criadores foi encontrada em nenhuma busca. Nenhum dado real disponível.
- @vendedorglobal — Queries tentadas: '"vendedorglobal" instagram posts reels 2026 site:instagram.com OR "vendedorglobal" instagram conteúdo'; '"vendedorglobal" site:instagram.com OR "vendedorglobal" instagram viral'; 'vendedorglobal instagram dropshipping negócio digital creator'. WebFetch direto ao perfil não foi tentado novamente após falha de rede confirmada em instagram.com (host bloqueado). Nenhuma menção ao handle exato foi encontrada em nenhum resultado — apenas conteúdo genérico sobre dropshipping/vendas no Instagram, sem relação confirmada com este perfil. Nenhum dado real disponível.
- @oluizmain — Queries tentadas: '"oluizmain" instagram posts reels 2026 site:instagram.com OR "oluizmain" instagram conteúdo'; '"oluizmain" site:instagram.com OR "o luiz main" instagram viral creator'; 'oluizmain instagram quem é criador conteúdo'. WebFetch direto ao perfil não foi tentado após confirmação de bloqueio de instagram.com na rede da sessão. Nenhum resultado mencionou este handle especificamente; o único quase-match ('mrolumaintain', criador nigeriano) é claramente um perfil diferente. Nenhum dado real disponível.
- @ai — WebFetch direto em instagram.com/ai/ falhou (host não resolvido/bloqueado na rede da sessão). Tentei três buscas WebSearch variadas. Nenhuma resultou em identificação do dono do handle @ai, posts, captions ou menções de terceiros específicas a esse perfil — apenas artigos genéricos sobre IA no Instagram e outros handles parecidos (@artificialintelligence, @ai_breeeze). Handle de 2 caracteres é extremamente disputado/provavelmente institucional ou inativo; não há evidência pública acessível via busca.
- @ana.gsoares — instagram.com bloqueado na rede da sessão. Três buscas WebSearch tentadas — nenhuma retornou qualquer página, post, agregador ou menção de terceiros para esse handle exato. Resultados trouxeram apenas perfis de nomes parecidos, não relacionados. Não há dado público acessível via busca para este perfil.
- @leosoares.ia — Três buscas WebSearch tentadas. Nenhuma retornou qualquer resultado contendo o handle exato — nem posts, nem agregadores (creatordb/favikon/hypeauditor), nem menções de terceiros. Resultados trouxeram apenas perfis de outros 'Leo/Léo' não relacionados e artigos genéricos sobre Reels/IA em 2026. Não há dado público acessível via busca para este perfil.
- @gabriel.adamuchi — Duas buscas WebSearch tentadas. Nenhuma retornou qualquer resultado contendo esse nome/handle exato — nem posts, nem agregadores (creatordb/favikon/socialveins/hypeauditor), nem menções de terceiros. Resultados trouxeram apenas outros criadores chamados 'Gabriel' sem relação. Não há dado público acessível via busca para este perfil.
- @viverdeia.ai — WebSearch padrão + ampliada retornaram apenas artigos genéricos sobre IA/Reels/2026 sem menção ao perfil ou domínio. WebFetch direto em instagram.com/viverdeia.ai falhou (ENOTFOUND). Nenhum dado real encontrado.
- @ninja.automacoes — Resultados foram apenas guias genéricos de automação de Instagram com n8n e um produto não relacionado ('Insta Ninja'). Nenhuma menção direta ou de terceiros ao perfil @ninja.automacoes foi encontrada.
- @eduardocavalcanti — Listagem em thehandbook.com (agregador de influenciadores) para um 'Eduardo Cavalcanti' com alcance de 25.996 e taxa de engajamento de 1,3%, mas sem expor @handle nem confirmar vínculo com este perfil (nome comum; outros resultados trazem homônimos não relacionados). Tratado como dado não verificado/insuficiente. Nenhum post, hook, CTA ou conteúdo real foi encontrado.
- @jonylan — Retornos apenas conteúdo genérico sobre tendências de Reels em 2026 e perfis de terceiros com nomes parecidos mas não correspondentes (jonahwasylak, jonathanhlyon, jonwands). Nenhuma menção real ao handle @jonylan foi encontrada.
- @allesinisgalli — Duas queries WebSearch tentadas. Nenhum resultado retornou o handle exato — apenas correspondências soltas de nomes parecidos (Alessia Galli fotógrafa, LuisaGallia, playgalliano, etc.), sem relação confirmada. Nenhum post, menção de terceiro ou dado de agregador encontrado. WebFetch não tentado (bloqueio de rede conhecido).
- @lonamkt — Duas queries WebSearch tentadas. Nenhum resultado mencionou o handle — apenas artigos genéricos de tendências de Instagram/Reels 2026 em português. Nenhum post, menção de terceiro ou dado de agregador encontrado para esse perfil.
- @gabrielbarbosa.oficial — Duas queries WebSearch tentadas. Resultados retornaram apenas conteúdo sobre o jogador de futebol Gabriel 'Gabigol' Barbosa, mas NENHUMA fonte confirmou que esse handle pertence a ele ou a qualquer pessoa específica — sem confirmação de vínculo. Nenhum post original, caption real ou dado de engajamento encontrado para o handle exato.
- @opensession.co — Duas queries WebSearch tentadas. Nenhum resultado mencionou o domínio/handle — apenas artigos genéricos sobre tendências de Reels 2026 e páginas de agências de marketing não relacionadas. Nenhum post, menção de terceiro ou dado de agregador encontrado.
- @christiantriad — Três queries WebSearch tentadas. Nenhuma trouxe qualquer página, perfil, agregador ou menção de terceiros sobre essa handle especificamente. WebFetch direto em instagram.com/christiantriad falhou (ENOTFOUND, host bloqueado nesta sessão). Nenhum dado real encontrado para este perfil.
- @amandadinizmkt — Duas queries WebSearch tentadas. Nenhuma trouxe qualquer página, perfil, agregador ou menção de terceiros sobre essa handle exata — resultados mostraram apenas contas parecidas de outras 'Amandas' sem relação confirmada. WebFetch direto em instagram.com/amandadinizmkt falhou (ENOTFOUND, host bloqueado). Nenhum dado real encontrado para este perfil.
- @geiss11 — Duas queries WebSearch tentadas. Nenhum resultado correspondeu ao handle; retornaram apenas guias genéricos de Reels/viralização e perfis de terceiros não relacionados (ex.: robertgeiss_1964). instagram.com bloqueado na rede desta sessão (ENOTFOUND). Nenhum dado real encontrado.
- @nelmoricalde — Duas queries WebSearch tentadas. Nenhum resultado correspondeu ao handle; apenas perfis de terceiros com nomes parecidos (nelsonmoralesmx, nellcarmo, nelzaion, nelfaofficial) e páginas genéricas não relacionadas. Nenhum dado real encontrado.
- @rodrigotadewald — Query padrão + busca ampliada 'Rodrigo Tadewald instagram'. Nenhum resultado correspondeu à pessoa/handle; apenas perfis homônimos/parecidos (Rodrigo Tadeu Lopes no LinkedIn, Rodrigo Trussardi, Rodrigo Teaser no HypeAuditor), nenhum confirmado como o mesmo perfil. Nenhum dado real encontrado.
- @sujeitoprogramador — Query padrão + 'sujeitoprogramador instagram viral reels'. Nenhum resultado correspondeu ao handle; apenas artigos genéricos sobre Reels/algoritmo do Instagram. WebFetch direto em instagram.com/sujeitoprogramador falhou com ENOTFOUND (confirmando bloqueio de rede). Nenhum dado real encontrado.
- @jonathan_kamargo — Duas queries WebSearch tentadas. Nenhum resultado correspondeu ao handle; apenas perfis homônimos parecidos (jonathan.maicelo2, ig_jonathangaming, jonathanheres). Nenhum dado real encontrado.
- @marianatorre.s — Duas queries WebSearch tentadas + WebFetch direto em instagram.com/marianatorre.s (ENOTFOUND, host bloqueado). Nenhuma busca retornou resultados correspondentes a este handle; apenas contas de terceiros com nomes parecidos (@marianateranr, @maritorreblanca) em agregadores de analytics. Nenhum post, caption ou menção real foi encontrado.
- @marketerhub.ai — Duas queries WebSearch tentadas. Nenhum resultado mencionou o domínio/handle ou seu conteúdo no Instagram; retornaram apenas guias genéricos de Reels/marketing 2026 e um perfil de ad-library de marca diferente ('Marketer HQ'). Nenhum dado real encontrado.
- @marcelaluzzio — Duas queries WebSearch tentadas. Nenhum resultado correspondeu ao handle; apenas contas de terceiros com nomes parecidos (@marcelamarenco19, @marcelavacarezza_, @marcelotega) em agregadores de analytics, e artigos genéricos sobre viralização no Instagram.
- @gestordeaudiencia — Duas queries WebSearch tentadas. Nenhum resultado correspondeu ao handle; apenas um perfil de terceiro com nome parecido (@gestordeperformance) em agregador, e artigos genéricos sobre engajamento/viralização no Instagram em 2026.
- @sebintel — Duas queries WebSearch tentadas. Nenhum resultado mencionou este termo/handle; retornaram apenas artigos genéricos sobre algoritmo/tendências de Reels em 2026 e contas de terceiros com nomes parecidos (@seblafrite, @sebas) sem relação.
- @avora.ai — Duas queries WebSearch tentadas + WebFetch direto em instagram.com/avora.ai (ENOTFOUND). Nenhum resultado retornou o perfil, posts ou menções de terceiros sobre esse handle especificamente; resultados foram guias genéricos de Reels/IA ou perfis não relacionados. Nenhum dado real de conteúdo, hooks, CTAs ou engajamento foi encontrado.
- @ogabrieeldias — Duas queries WebSearch tentadas + WebFetch direto em instagram.com/ogabrieeldias (ENOTFOUND). Nenhum resultado correspondeu a esse handle; apareceram apenas contas com nomes parecidos (@ogabeoliveira, @gabriel, @gabrielfarias), descartadas. Nenhum dado real encontrado.
- @rodrigobindes — Duas queries WebSearch tentadas + WebFetch direto em instagram.com/rodrigobindes (ENOTFOUND). Nenhum resultado correspondeu ao handle; apenas contas com nomes parecidos (@rodrigobuenoms, @rodrigoamgoes, @rodrigocintra, @rodrigobocardi), descartadas. Nenhum dado real encontrado — possível que o handle esteja com grafia diferente, seja privado ou pouco indexado.
- @franklim.gui — Duas queries WebSearch tentadas + WebFetch direto em instagram.com/franklim.gui (ENOTFOUND). Nenhum resultado correspondeu ao handle; apenas contas parecidas (@franklindavid, @franklingt, @frankie729, @guiiclaudino), descartadas. Nenhum dado real encontrado.
- @gabrielsamp.ai — Duas queries WebSearch tentadas + WebFetch direto em instagram.com/gabrielsamp.ai (ENOTFOUND). Nenhum resultado correspondeu ao handle; apareceram apenas perfis de pessoas com nomes parecidos via Socialveins/HypeAuditor/Heepsy (@gabrielputh, @gabemichael_ai, @gabrielramos456), descartados. Nenhum dado real encontrado.
- @maestrosdaia — Duas queries WebSearch tentadas. Nenhuma retornou qualquer resultado relacionado ao handle — só perfis de nome parecido (@maestriasabia, @maestramieldemaple) em agregadores, sem relação confirmada. instagram.com bloqueado na rede (ENOTFOUND).
- @brandsdecoded__ — Duas queries WebSearch tentadas. Nenhuma retornou o perfil do Instagram. Único achado tangencial foi um Substack 'Decoding Brands' sem confirmação de vínculo com o handle — não usado como evidência. Nenhum post, hook, CTA ou métrica real encontrado.
- @larissagomes.ia — Duas queries WebSearch tentadas. Nenhuma retornou qualquer página, post ou menção ao handle — apenas perfis de nome parecido (Larissa Tomásia, Larissa Guedes, Larissa Proença) via agregadores, e notícias genéricas sobre IA no Instagram. instagram.com bloqueado na rede (ENOTFOUND).
- @thiagozaao — Duas queries WebSearch tentadas. Nenhuma retornou o perfil ou qualquer menção ao handle — apenas perfis de nome parecido (@thiagaoofficial, @thiagotubao, @thiagoreis) via agregadores, sem relação confirmada. instagram.com bloqueado na rede (ENOTFOUND).
- @neuwebstudio — Duas queries WebSearch tentadas. Nenhum resultado mencionou o handle; apenas artigos genéricos sobre Reels/2026. WebFetch direto em instagram.com/neuwebstudio falhou com ENOTFOUND (host bloqueado). Nenhum dado real de conteúdo foi encontrado.
- @laschuk — Duas queries WebSearch tentadas. Nenhum resultado exato; apenas perfis com nomes parecidos (@rxn_offpage, @shewchuk, @annchuk) em diretórios automatizados (Socialveins), sem relação confirmada. WebFetch direto em instagram.com/laschuk falhou com ENOTFOUND. Nenhum dado real de conteúdo foi encontrado.
- @maestroptompts — Duas queries WebSearch tentadas. Nenhum resultado mencionou o handle; apenas artigos genéricos sobre prompts de IA para Reels em 2026. Nenhum dado real de conteúdo foi encontrado.
- @faladantasmkt — Duas queries WebSearch tentadas. Nenhum resultado mencionou o handle; apenas perfis parecidos (@falagabes, @falatcheoficial, @falavertao) em diretórios de influenciadores, sem relação confirmada. Nenhum dado real de conteúdo foi encontrado.
- @andrevictor.m — Duas queries WebSearch tentadas. Nenhum resultado mencionou o handle exato; apenas contas com nomes parecidos (andrepiva, andrebellos, loud_victor). WebFetch em instagram.com/andrevictor.m falhou com ENOTFOUND. Nenhum dado real encontrado.
- @drisiano — Duas queries WebSearch tentadas. Nenhum resultado mencionou o handle exato; apenas perfis de nomes parecidos (dreiros, dri69, dresvi). Nenhum dado real encontrado.
- @brun0gpt — Duas queries WebSearch tentadas. Nenhum resultado mencionou o handle exato; apenas perfis de nomes parecidos com 'bruno/brun' e um perfil 'Brunobelissimo.Ai' não confirmadamente relacionado. Nenhum dado real encontrado.
- @maxcarrau.ia — Duas queries WebSearch tentadas. Nenhum resultado mencionou o handle exato; apenas perfis de nomes parecidos (max_true, maxprice3, the_max_ofc). Nenhum dado real encontrado.
- @yikchanltd — instagram.com bloqueado na rede desta sessão (ENOTFOUND). Via WebSearch, 4 queries tentadas (incluindo o termo isolado) — zero resultados sobre o handle, apenas handles parecidos de pessoas/empresas distintas (@yk, @yikfei99, @yicheng.0227) e empresas registradas no Reino Unido com grafia parecida (Ys Chan Ltd, YIKINC LTD, Yik Ho Holdings), sem vínculo confirmado. Não foi encontrado nenhum indício, positivo ou negativo, de relação entre @yikchanltd e o handle @yikC (já analisado em outro lote) — não há base para confirmar ou descartar essa hipótese.
