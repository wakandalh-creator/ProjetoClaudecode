# Análise de Perfis Instagram — 2026-11-09

## Nota Metodológica Importante

Esta execução do Módulo 2 rodou em MODO ANÁLISE sobre os 61 perfis ativos de `config/profiles.json`, processados em 13 lotes de até 5 perfis via sub-agentes paralelos (fork, WebSearch apenas — WebFetch não foi tentado em instagram.com, confirmado bloqueado por rede nesta sandbox na execução anterior de 2026-11-02), seguindo as regras de segurança do swarm do projeto (lotes de 5, concorrência máxima 3, anti-alucinação).

**Resultado é praticamente idêntico ao da semana passada (2026-11-02):** a esmagadora maioria dos 61 handles monitorados (a maior parte contas pequenas/nicho em português) não é indexada pelo WebSearch — nem posts, nem captions, nem métricas, nem sequer menções de terceiros. Apenas **9 de 61 perfis** retornaram algum indício real (sempre via agregadores/sites de terceiros não oficiais — creatordb.app, reportei.com, motionapp.com, viralbrain.ai, theaireport.ai, mundodomarketing.com.br — nunca uma caption ou hook literal visto diretamente em um post): **@charliehills, @nick_saraev, @leandroladeiran, @oneyaraujo, @geracaotechs, @human___academy, @marcelaluzzio (baixa confiança — nome não confere exatamente), @lindsay.ia e @noevarner**. Os demais **52 perfis** ficaram com `limitacao_dados` preenchido e nenhum dado real.

**Divergências de handle encontradas nesta execução (recomendo revisão do Lucas em `config/profiles.json`):**
- `nathanhodgson` → agregador só encontra dados para `nathanhodgson.ai`
- `noevarner` → agregador só encontra dados para `noevarner.ai`
- `lindsay.ia` → agregador só encontra dados para `lindsay.ai` (sem o segundo "i")
- `maestroptompts` → possível erro de digitação (não foi possível confirmar nome correto)
- `yikC` e `yikchanltd` → ambos sem nenhum dado encontrado; não há evidência de que sejam a mesma pessoa/empresa (nota original em profiles.json pedia verificação)

**Recomendação para o Lucas:** considerar conectar um MCP/skill de scraping de Instagram autorizado (API oficial ou serviço de terceiros com acesso de rede liberado) para que o Módulo 2 tenha dados reais em execuções futuras — WebSearch isoladamente continua insuficiente para a grande maioria dos perfis monitorados, mesmo na segunda execução consecutiva.

---

## Visão Geral dos Perfis

| Perfil | Categoria | Formato Dominante | Engajamento | Hook Padrão / Status |
|--------|-----------|------------------|-------------|------------------------|
| @charliehills | creator | misto | medio | outro |
| @yikC | creator | misto | baixo | dados insuficientes |
| @eujoaotorresz | creator | misto | baixo | dados insuficientes |
| @fabianocarvalhojr | founder | misto | baixo | dados insuficientes |
| @rafa.grandi | marketing | misto | baixo | dados insuficientes |
| @brusantanna.ai | ia | misto | baixo | dados insuficientes |
| @vendedorglobal | negocio-digital | misto | baixo | dados insuficientes |
| @oluizmain | creator | misto | baixo | dados insuficientes |
| @nick_saraev | automacao | misto | baixo | outro |
| @nathanhodgson | ia | misto | baixo | dados insuficientes |
| @ai | ia | misto | baixo | dados insuficientes |
| @ana.gsoares | marketing | misto | baixo | dados insuficientes |
| @chase.h.ai | ia | misto | baixo | dados insuficientes |
| @leosoares.ia | ia | misto | baixo | dados insuficientes |
| @gabriel.adamuchi | creator | misto | baixo | dados insuficientes |
| @viverdeia.ai | ia | misto | baixo | dados insuficientes |
| @ninja.automacoes | automacao | misto | baixo | dados insuficientes |
| @nikolassasso | creator | misto | baixo | outro |
| @eduardocavalcanti | founder | misto | baixo | dados insuficientes |
| @jonylan | creator | misto | baixo | dados insuficientes |
| @allesinisgalli | founder | misto | baixo | dados insuficientes |
| @lonamkt | marketing | misto | baixo | dados insuficientes |
| @gabrielbarbosa.oficial | creator | misto | baixo | dados insuficientes |
| @opensession.co | agencia | misto | baixo | dados insuficientes |
| @leandroladeiran | marketing | misto | medio | outro |
| @christiantriad | creator | misto | baixo | dados insuficientes |
| @oneyaraujo | creator | reels | medio | outro |
| @geracaotechs | ia | reels | alto | outro |
| @amandadinizmkt | marketing | misto | baixo | dados insuficientes |
| @human___academy | ia | reels | baixo | outro |
| @geiss11 | creator | misto | baixo | dados insuficientes |
| @nelmoricalde | creator | misto | baixo | dados insuficientes |
| @rodrigotadewald | marketing | misto | baixo | dados insuficientes |
| @sujeitoprogramador | ia | misto | baixo | dados insuficientes |
| @jonathan_kamargo | creator | misto | baixo | dados insuficientes |
| @marianatorre.s | marketing | misto | baixo | dados insuficientes |
| @marketerhub.ai | marketing | misto | baixo | dados insuficientes |
| @marcelaluzzio | marketing | misto | baixo | outro |
| @gestordeaudiencia | marketing | misto | baixo | dados insuficientes |
| @sebintel | ia | misto | baixo | dados insuficientes |
| @avora.ai | agencia | misto | baixo | dados insuficientes |
| @ogabrieeldias | creator | misto | baixo | dados insuficientes |
| @rodrigobindes | founder | misto | baixo | dados insuficientes |
| @franklim.gui | creator | misto | baixo | dados insuficientes |
| @gabrielsamp.ai | ia | misto | baixo | dados insuficientes |
| @maestrosdaia | ia | misto | baixo | dados insuficientes |
| @brandsdecoded__ | marketing | misto | baixo | dados insuficientes |
| @anatex | creator | misto | baixo | dados insuficientes |
| @larissagomes.ia | ia | misto | baixo | dados insuficientes |
| @thiagozaao | creator | misto | baixo | dados insuficientes |
| @neuwebstudio | agencia | misto | baixo | dados insuficientes |
| @laschuk | founder | misto | baixo | dados insuficientes |
| @maestroptompts | ia | misto | baixo | dados insuficientes |
| @faladantasmkt | marketing | misto | baixo | dados insuficientes |
| @lindsay.ia | ia | reels | medio | outro |
| @andrevictor.m | marketing | misto | baixo | dados insuficientes |
| @drisiano | creator | misto | baixo | dados insuficientes |
| @brun0gpt | ia | misto | baixo | dados insuficientes |
| @maxcarrau.ia | ia | misto | baixo | dados insuficientes |
| @noevarner | creator | reels | baixo | outro |
| @yikchanltd | creator | misto | baixo | dados insuficientes |

---

## Análise Detalhada por Perfil

### @charliehills

**Categoria:** creator

#### Padrões de Hook identificados
- Modelo: outro (frequência: media) — ex: "Hooks descritos por fontes secundárias (viralbrain.ai, theaireport.ai) como 'blocos modulares reutilizáveis' ligados a um framework chamado 'CHEF', usado para conteúdo educacional sobre IA/automação (Claude Code, Gemini). Nenhuma frase literal de post foi encontrada, apenas descrição de terceiros."

#### Estrutura típica do conteúdo
```
Dados insuficientes para determinar estrutura diretamente dos posts. Fontes secundárias descrevem um 'sistema de conteúdo first-AI' com formato educacional (tutoriais práticos de ferramentas de IA), mas sem detalhamento de blocos/fluxo.
```

#### CTA dominante
- Padrão: Dados insuficientes — nenhuma citação literal de CTA encontrada.

#### Tom de voz
- Adjetivos: didático, prático, educacional

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: medio

#### Temas identificados
- tutoriais de ferramentas de IA
- automação com Claude/Gemini
- parceria com Zapier (#zapierpartner)

#### Limitação de dados
WebSearch não retornou posts, captions ou métricas diretas do Instagram (site:instagram.com não indexado). As fontes encontradas (CreatorDB, ViralBrain, TheAIReport, Favikon) parecem descrever DUAS pessoas distintas com nome similar — uma focada em LinkedIn (210K+ seguidores, reel citado com ~11M views, mas contexto da plataforma do reel é ambíguo) e outra (CreatorDB) descrita como criador micro-tier Instagram/YouTube baseado no Reino Unido. Não foi possível confirmar qual corresponde exatamente ao handle @charliehills nem verificar diretamente nenhuma métrica. Tratado como dado de baixa confiança — não usado para 'alto' engajamento.

---

### @yikC

**Categoria:** creator

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes para determinar estrutura.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Limitação de dados
WebSearch não indexa posts, captions ou métricas deste perfil em 2 queries tentadas. Resultados retornaram apenas handles parecidos mas distintos (yikes_cg, @yk, yikfei99, ykxc.skt) — nenhum correspondia ao handle exato @yikC. Nenhuma menção de terceiros encontrada.

---

### @eujoaotorresz

**Categoria:** creator

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes para determinar estrutura.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Limitação de dados
WebSearch não indexa posts, captions ou métricas deste perfil em 2 queries tentadas. Apenas handles parecidos (joanatorres_, eufernandotorquatto, eujoaodesign) apareceram, nenhum correspondendo ao handle exato @eujoaotorresz.

---

### @fabianocarvalhojr

**Categoria:** founder

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes para determinar estrutura.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Limitação de dados
WebSearch não indexa posts, captions ou métricas deste perfil em 2 queries tentadas. Resultados retornaram apenas pessoas homônimas não relacionadas (jogador de futebol Fabinho/Fábio Carvalho, artista plástico, GitHub de terceiros) e handles parecidos (fabianno_oliveira, fabuusjunior) — nenhum correspondia ao handle exato @fabianocarvalhojr.

---

### @rafa.grandi

**Categoria:** marketing

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes para determinar estrutura.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Limitação de dados
WebSearch não indexa posts, captions ou métricas deste perfil em 2 queries tentadas. Apenas handles parecidos (rafa_fae, rafamattei, rafaavitti, antoniograndiofficial) apareceram, nenhum correspondendo ao handle exato @rafa.grandi.

---

### @brusantanna.ai

**Categoria:** ia

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes para determinar estrutura.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Limitação de dados
WebSearch não retornou nenhuma menção ao handle, posts, captions ou métricas; apenas artigos genéricos de marketing de Instagram para 2026 sem relação com o perfil. Nenhuma fonte secundária (agregadores) encontrada.

---

### @vendedorglobal

**Categoria:** negocio-digital

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes para determinar estrutura.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Limitação de dados
WebSearch não retornou nenhuma menção ao handle; apenas artigos genéricos brasileiros sobre 'vender pelo Instagram' sem relação direta com o perfil monitorado.

---

### @oluizmain

**Categoria:** creator

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes para determinar estrutura.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Limitação de dados
WebSearch não retornou nenhuma menção ao handle em nenhuma das tentativas; apenas artigos genéricos sobre tendências de Reels em 2026.

---

### @nick_saraev

**Categoria:** automacao

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "Nenhuma caption/hook literal encontrado; agregadores de terceiros (creatordb.app, iqfluence.io, outlierkit.com) descrevem apenas estratégia de engajamento, não texto de hook."

#### Estrutura típica do conteúdo
```
Dados insuficientes para determinar estrutura narrativa real; nenhuma caption vista diretamente.
```

#### CTA dominante
- Padrão: Pedir comentário de palavra-chave no post (gatilho de engajamento + captura de lead para DM), segundo descrição de agregador de terceiros (iqfluence.io) — não confirmado por caption vista diretamente.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Temas identificados
- Promoção do programa 'Maker School' (automação de negócios/AI agency) — inferido de fonte secundária, não visto em post direto

#### Limitação de dados
Instagram em si não indexado. Dados vêm só de agregadores de terceiros (creatordb.app, iqfluence.io, outlierkit.com), que mencionam handle @nicksaraev/@nick_saraev, base de seguidores combinada YouTube+Instagram estimada em >1M (não verificado, não é métrica de engajamento de post), e a tática de pedir comentário de palavra-chave para promover o 'Maker School'. Nenhuma caption, hook ou post individual foi visto diretamente.

---

### @nathanhodgson

**Categoria:** ia

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhuma caption ou post individual encontrado via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes para determinar estrutura.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Temas identificados
- IA e produtividade — categoria atribuída pelo agregador CreatorDB, não confirmada por post direto

#### Limitação de dados
Perfil monitorado é 'nathanhodgson' (url instagram.com/nathanhodgson/), mas o agregador de terceiros CreatorDB só encontra dados reais para o handle '@nathanhodgson.ai' (~145.900 seguidores Instagram, estimativa não verificada) — possível divergência de handle no config/profiles.json a revisar com o Lucas. Há também um '@nathanhodgson_' (Motion, ~142,6K seguidores Meta) que pode ser pessoa diferente. Nenhuma caption ou conteúdo de post foi visto diretamente em nenhum dos dois handles.

---

### @ai

**Categoria:** ia

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes para determinar estrutura.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Limitação de dados
WebSearch não retornou nenhuma página de instagram.com nem menção de terceiros ao handle '@ai' (handle genérico, resultados dominados por artigos sobre 'IA no Instagram' em geral, não a conta). Nenhum post, caption ou métrica real identificada nas 3 queries tentadas.

---

### @ana.gsoares

**Categoria:** marketing

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes para determinar estrutura.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Limitação de dados
WebSearch confirmou explicitamente que nenhum dos resultados vinha do perfil 'ana.gsoares'; apenas artigos genéricos de terceiros sobre tendências de Reels 2026. Nenhum post, caption ou métrica real identificada.

---

### @chase.h.ai

**Categoria:** ia

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes para determinar estrutura.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Limitação de dados
WebSearch não encontrou nada associado ao handle 'chase.h.ai'; resultados eram sobre o recurso 'Reels Chaining' da Meta e cobertura genérica de IA no Instagram, sem relação com a conta. Nenhum post, caption ou métrica real identificada.

---

### @leosoares.ia

**Categoria:** ia

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes para determinar estrutura.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Limitação de dados
WebSearch confirmou que nenhum dos resultados retornados vinha do perfil '@leosoares.ia'; apenas blogs de marketing BR sobre tendências de Reels em 2026. Nenhum post, caption ou métrica real identificada.

---

### @gabriel.adamuchi

**Categoria:** creator

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes para determinar estrutura.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Limitação de dados
WebSearch não retornou nenhuma página do perfil 'gabriel.adamuchi'; resultados eram ferramentas de scraping de Reels genéricas e perfis de outros 'Gabriel' não relacionados (@mjteo, @bientic, @gabrish_doc_off). Nenhum post, caption ou métrica real identificada.

---

### @viverdeia.ai

**Categoria:** ia

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes para determinar estrutura.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Limitação de dados
2 queries tentadas ('viverdeia.ai instagram posts reels 2026', 'viverdeia.ai instagram'). Nenhum resultado mencionou o domínio/handle; apenas conteúdo genérico sobre IA e Reels em 2026 e um perfil homônimo não relacionado. Nenhum post, caption ou métrica real identificada.

---

### @ninja.automacoes

**Categoria:** automacao

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes para determinar estrutura.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Limitação de dados
2 queries tentadas. Nenhum resultado corresponde ao handle; apenas artigos genéricos de terceiros sobre ferramentas de automação de Instagram (n8n, Spur, Kommo) e um produto não relacionado chamado 'Insta Ninja' no Product Hunt. Nenhum post, caption ou métrica real identificada.

---

### @nikolassasso

**Categoria:** creator

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "Nenhuma caption/hook literal encontrado; página de terceiros (creatordb.app) descreve apenas o perfil como 'creator educacional com audiência concentrada no Brasil, ativado via YouTube + Instagram Reels/Stories', sem citar texto de post."

#### Estrutura típica do conteúdo
```
Dados insuficientes para determinar estrutura narrativa real; nenhuma caption vista diretamente.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Limitação de dados
Único hit relevante foi a página creatordb.app/creatorstats/nikolassasso/ (dados de 22/set/2026, ~7 semanas desatualizados), que classifica o criador como 'educacional' com audiência BR, mas não lista posts, captions ou reels específicos. Nenhum resultado veio de instagram.com diretamente.

---

### @eduardocavalcanti

**Categoria:** founder

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes para determinar estrutura.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Limitação de dados
1 query tentada (resultados já cobriram o escopo da query ampla). Nenhum resultado correspondeu ao handle exato; apenas páginas de analytics de terceiros (hypeauditor.com) para handles homônimos não relacionados e artigos genéricos sobre o algoritmo do Instagram em 2026.

---

### @jonylan

**Categoria:** creator

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes para determinar estrutura.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Limitação de dados
2 queries tentadas. Nenhum resultado mencionou o handle exato @jonylan; apenas homônimos distantes. Nenhum post, caption ou métrica real identificada.

---

### @allesinisgalli

**Categoria:** founder

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes para determinar estrutura.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Limitação de dados
WebSearch não retornou nenhum post, caption, métrica ou menção de terceiros ao handle exato @allesinisgalli em 2 queries (específica e ampla). Apenas homônimos não relacionados (Alessia Galli, Alessandro Galli, Alessio Galli, Cristian Galliani) apareceram.

---

### @lonamkt

**Categoria:** marketing

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes para determinar estrutura.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Limitação de dados
WebSearch não confirmou nenhum post, caption ou métrica do handle @lonamkt. Um possível falso-positivo apareceu ('Loner Marketing', produto 'The Faceless Instagram Guide' no Gumroad) mas não há confirmação de que seja a mesma conta/pessoa — tratado como não confiável e não usado.

---

### @gabrielbarbosa.oficial

**Categoria:** creator

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes para determinar estrutura.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Limitação de dados
WebSearch não retornou nenhum post, caption ou métrica do handle exato @gabrielbarbosa.oficial em 2 queries. Resultados dominados pelo jogador de futebol Gabriel Barbosa ('Gabigol', conta oficial diferente) e homônimos não relacionados em diretórios de influenciadores.

---

### @opensession.co

**Categoria:** agencia

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes para determinar estrutura.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Limitação de dados
WebSearch não retornou nenhum post, caption, métrica ou site institucional correspondente a 'opensession.co' em 2 queries (incluindo variação 'open session agência IA'). Apenas resultados genéricos sobre agências e agentes de IA para Instagram, sem relação direta com este perfil/empresa.

---

### @leandroladeiran

**Categoria:** marketing

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "Nenhuma caption/hook literal encontrada; fonte secundária (CreatorDB) descreve apenas foco temático, não texto de post."

#### Estrutura típica do conteúdo
```
Dados insuficientes para determinar estrutura narrativa real; nenhuma caption vista diretamente.
```

#### CTA dominante
- Padrão: Dados insuficientes — nenhuma citação literal de CTA encontrada.

#### Tom de voz
- Adjetivos: prático, bem-humorado

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: medio

#### Temas identificados
- marketing digital
- produtos digitais

#### Limitação de dados
Instagram não indexado diretamente. Única fonte foi uma página de estatísticas de terceiros (CreatorDB, atualizada em 08/10/2026) que descreve o criador como focado em marketing digital e produtos digitais, com conteúdo misto de dicas práticas e humor, audiência >2 milhões de seguidores no Instagram (sua maior plataforma) e presença no TikTok em desaceleração. Esses números e descrições são estimativas de terceiro não verificadas, não vistas em posts/captions diretos — por isso engajamento foi marcado apenas 'medio' (não 'alto') e nenhum hook/CTA literal foi atribuído.

---

### @christiantriad

**Categoria:** creator

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes para determinar estrutura.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Limitação de dados
WebSearch não retornou nenhum post, caption ou menção de terceiros ao handle @christiantriad. Resultados foram apenas artigos genéricos sobre Instagram/Reels em 2026 e conteúdo de perfis cristãos/igrejas não relacionados.

---

### @oneyaraujo

**Categoria:** creator

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "Nenhuma caption literal encontrada; fonte secundária (reportei.com) descreve-o como referência em marketing viral no Instagram desde 2012, criador do curso 'Código Viral'."

#### Estrutura típica do conteúdo
```
Dados insuficientes para determinar estrutura narrativa real a partir de posts — nenhuma caption vista diretamente.
```

#### CTA dominante
- Padrão: Venda de produtos digitais (curso 'Código Viral', guia 'Checklist Viral', 'Carrossel Viral', pack 'Oney Viral Pack' no Gumroad) — inferido de fontes secundárias, não de caption vista diretamente.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: reels
- Engajamento estimado: medio

#### Temas identificados
- estratégias para viralizar Reels
- crescimento de seguidores
- monetização de audiência

#### Limitação de dados
Instagram não indexado diretamente. Fonte secundária (reportei.com) afirma >1,3 milhão de seguidores e foco total em Reels/viralização, mas nenhuma caption, hook ou métrica de post individual foi vista diretamente — por isso engajamento marcado como 'medio' (conservador) em vez de 'alto'.

---

### @geracaotechs

**Categoria:** ia

#### Padrões de Hook identificados
- Modelo: outro (frequência: media) — ex: "Nenhuma caption literal vista; página de terceiros (motionapp.com/creator/geracaotechs) descreve o perfil como foco em plataformas online, ferramentas digitais e recomendações de sites para DIY, design e tarefas do dia a dia."

#### Estrutura típica do conteúdo
```
Dados insuficientes para determinar estrutura narrativa real a partir de posts — apenas descrição de categoria por agregador de terceiros.
```

#### CTA dominante
- Padrão: Dados insuficientes — nenhuma caption ou CTA literal encontrado.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: reels
- Engajamento estimado: alto

#### Temas identificados
- plataformas online e ferramentas digitais
- recomendações de sites para DIY e design

#### Limitação de dados
Instagram não indexado diretamente. Fonte secundária (motionapp.com) lista ~218,4K seguidores e 4 reels em destaque com 3,8M-5,5M visualizações cada (proporção visualização/seguidor muito alta, por isso 'alto' engajamento) e 7 parcerias de marca — números não verificados de forma independente, nenhuma caption ou data de 2026 confirmada.

---

### @amandadinizmkt

**Categoria:** marketing

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes para determinar estrutura.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Limitação de dados
WebSearch não retornou nada para o handle exato @amandadinizmkt. O hit mais próximo foi um perfil Behance distinto, não relacionado. Nenhum post, caption ou métrica real identificada.

---

### @human___academy

**Categoria:** ia

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "Nenhuma caption de post do Instagram encontrada; o próprio site humanacademy.ai publica material educacional sobre 'reels com potencial de alcance' (legibilidade de texto, hashtags, incentivo a compartilhamentos/salvamentos/comentários)."

#### Estrutura típica do conteúdo
```
Dados insuficientes para determinar estrutura real de posts do Instagram — apenas material educacional do próprio site sobre boas práticas de Reels.
```

#### CTA dominante
- Padrão: Dados insuficientes — nenhuma caption ou CTA literal de post encontrado.

#### Tom de voz
- Adjetivos: didático, educacional

#### Métricas estimadas
- Formato mais usado: reels
- Engajamento estimado: baixo

#### Temas identificados
- boas práticas de reels com potencial de alcance
- posts orgânicos para Instagram

#### Limitação de dados
Instagram não indexado diretamente. Único material encontrado foi do próprio site humanacademy.ai, confirmando foco educacional em IA/automação, mas sem nenhum post, caption ou métrica real do perfil @human___academy em si.

---

### @geiss11

**Categoria:** creator

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes para determinar estrutura.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Limitação de dados
2 queries tentadas. Nenhum resultado mencionou o handle exato @geiss11; apenas artigos genéricos sobre Reels/viralização em 2026 e conteúdo não relacionado sobre a família alemã 'Die Geissens'. Nenhum post, caption ou métrica real identificada.

---

### @nelmoricalde

**Categoria:** creator

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes para determinar estrutura.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Limitação de dados
2 queries tentadas. Nenhum resultado corresponde ao handle exato @nelmoricalde; apenas homônimos distantes não relacionados. Nenhum post, caption ou métrica real identificada.

---

### @rodrigotadewald

**Categoria:** marketing

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes para determinar estrutura.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Limitação de dados
2 queries tentadas. Nenhum resultado corresponde ao handle exato @rodrigotadewald; apenas homônimos não relacionados. Nenhum post, caption ou métrica real identificada.

---

### @sujeitoprogramador

**Categoria:** ia

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes para determinar estrutura.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Limitação de dados
2 queries tentadas. Nenhum resultado trouxe o perfil do Instagram @sujeitoprogramador diretamente (apenas a hashtag #souprogramador e artigos acadêmicos BR genéricos). A marca 'Sujeito Programador' é conhecida por outros canais (site/YouTube), mas isso não foi confirmado para o Instagram via busca.

---

### @jonathan_kamargo

**Categoria:** creator

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes para determinar estrutura.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Limitação de dados
2 queries tentadas. Nenhum resultado corresponde ao handle exato @jonathan_kamargo; achados foram um pesquisador 'Jonathan Camargo' (GitHub, PhD Georgia Tech — handle diferente) e outros homônimos não relacionados. Nenhum post, caption ou métrica real identificada.

---

### @marianatorre.s

**Categoria:** marketing

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes para determinar estrutura.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Limitação de dados
3 queries tentadas. Nenhum resultado correspondeu ao handle exato @marianatorre.s; apenas homônimos não relacionados e artigos genéricos sobre tendências de Instagram 2026. Nenhum post, caption ou métrica real identificada.

---

### @marketerhub.ai

**Categoria:** marketing

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes para determinar estrutura.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Limitação de dados
3 queries tentadas. Nenhum resultado menciona o domínio/handle marketerhub.ai; apenas guias genéricos de marketing/IA no Instagram. Nenhum post, caption ou métrica real identificada.

---

### @marcelaluzzio

**Categoria:** marketing

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "Nenhuma caption literal encontrada; página de palestrante (mundodomarketing.com.br) descreve uma 'Marcela Lúzio' (grafia distinta) como produtora de conteúdo com IA desde 2019, que migrou de vídeos/lives sobre NFT para ensinar conteúdo orgânico e resultados com IA."

#### Estrutura típica do conteúdo
```
Dados insuficientes para determinar estrutura narrativa real de posts — apenas bio de palestrante.
```

#### CTA dominante
- Padrão: Dados insuficientes — nenhuma citação literal de CTA encontrada.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Temas identificados
- IA aplicada a marketing/conteúdo orgânico — inferido de bio de palestrante, não confirmado como o mesmo handle

#### Limitação de dados
Instagram não indexado diretamente. Único achado foi uma bio de palestrante para 'Marcela Lúzio' (grafia divergente de @marcelaluzzio) — correspondência de nome não confirmada como a mesma pessoa/conta. Tratado como dado de baixíssima confiança.

---

### @gestordeaudiencia

**Categoria:** marketing

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes para determinar estrutura.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Limitação de dados
3 queries tentadas. Nenhum resultado correspondeu ao handle exato; apenas um homônimo não relacionado (@gestordeperformance). Nenhum post, caption ou métrica real identificada.

---

### @sebintel

**Categoria:** ia

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes para determinar estrutura.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Limitação de dados
3 queries tentadas. Nenhum resultado correspondeu ao handle exato @sebintel; apenas homônimos não relacionados. Nenhum post, caption ou métrica real identificada.

---

### @avora.ai

**Categoria:** agencia

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes para determinar estrutura.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Limitação de dados
2 queries tentadas. Nenhum resultado mencionou o domínio/handle; apenas artigos genéricos sobre Instagram/IA em 2026 e agências não relacionadas. Nenhum post, caption ou métrica real identificada.

---

### @ogabrieeldias

**Categoria:** creator

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes para determinar estrutura.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Limitação de dados
2 queries tentadas. Nenhum resultado correspondeu ao handle exato @ogabrieeldias; apenas homônimos distintos. Nenhum post, caption ou métrica real identificada.

---

### @rodrigobindes

**Categoria:** founder

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes para determinar estrutura.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Limitação de dados
2 queries tentadas. Nenhum resultado correspondeu ao handle exato @rodrigobindes; apenas homônimos distintos em agregadores de terceiros. Conta pode ser privada, renomeada ou não indexada. Nenhum post, caption ou métrica real identificada.

---

### @franklim.gui

**Categoria:** creator

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes para determinar estrutura.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Limitação de dados
2 queries tentadas. Nenhum resultado correspondeu ao handle exato @franklim.gui; apenas homônimos parciais e guias genéricos de Reels 2026. Nenhum post, caption ou métrica real identificada.

---

### @gabrielsamp.ai

**Categoria:** ia

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes para determinar estrutura.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Limitação de dados
2 queries tentadas. Nenhum resultado correspondeu ao handle exato @gabrielsamp.ai; único hit tematicamente próximo foi @gabemichael_ai (cineasta de IA nos EUA, não relacionado). Nenhum post, caption ou métrica real identificada.

---

### @maestrosdaia

**Categoria:** ia

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes para determinar estrutura.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Limitação de dados
WebSearch não retornou nenhum post, caption ou perfil correspondente ao handle exato @maestrosdaia. Único hit tematicamente próximo foi um homônimo distinto não confirmado. Nenhum post, caption ou métrica real identificada.

---

### @brandsdecoded__

**Categoria:** marketing

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes para determinar estrutura.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Limitação de dados
WebSearch não retornou nenhuma menção ao handle @brandsdecoded__; apenas artigos genéricos sobre marketing de Reels/Instagram em 2026. Nenhum post, caption ou métrica real identificada.

---

### @anatex

**Categoria:** creator

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes para determinar estrutura.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Limitação de dados
WebSearch não retornou nada para o handle exato @anatex. Único hit parecido foi um perfil não confirmado e distinto, tratado como não relacionado. Nenhum post, caption ou métrica real identificada.

---

### @larissagomes.ia

**Categoria:** ia

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes para determinar estrutura.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Limitação de dados
WebSearch não retornou nada para o handle exato @larissagomes.ia. Vários homônimos distintos apareceram, nenhum confirmado como o mesmo perfil. Nenhum post, caption ou métrica real identificada.

---

### @thiagozaao

**Categoria:** creator

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes para determinar estrutura.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Limitação de dados
WebSearch não retornou nada para o handle exato @thiagozaao. Apenas homônimos parciais distintos em agregadores HypeAuditor. Nenhum post, caption ou métrica real identificada.

---

### @neuwebstudio

**Categoria:** agencia

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes para determinar estrutura.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Limitação de dados
2 queries tentadas. Nenhum resultado trouxe o perfil do Instagram; único achado tangencial foi uma página BuiltWith sobre o site neuwebstudio.com (sem links sociais). Nenhum post, caption ou métrica real identificada.

---

### @laschuk

**Categoria:** founder

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes para determinar estrutura.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Limitação de dados
2 queries tentadas. Nenhum resultado corresponde ao handle exato @laschuk; apenas homônimos distantes. Nenhum post, caption ou métrica real identificada.

---

### @maestroptompts

**Categoria:** ia

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes para determinar estrutura.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Limitação de dados
2 queries tentadas. Nenhum resultado corresponde ao handle; apenas guias genéricos de prompts de IA para Instagram (possível erro de digitação do handle real — 'prompts' vs 'ptompts' — a confirmar com o Lucas). Nenhum post, caption ou métrica real identificada.

---

### @faladantasmkt

**Categoria:** marketing

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes para determinar estrutura.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Limitação de dados
2 queries tentadas. Nenhum resultado corresponde ao handle exato @faladantasmkt; apenas homônimos parciais não relacionados. Nenhum post, caption ou métrica real identificada.

---

### @lindsay.ia

**Categoria:** ia

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "Nenhuma caption literal vista; agregador de terceiros (creatordb.app) descreve uma CTA de 'comentar palavra-chave' para liberar um guia de '29 habilidades práticas do Claude' — mesma tática documentada em outros perfis de IA desta lista (ex.: nick_saraev)."

#### Estrutura típica do conteúdo
```
Dados insuficientes para determinar estrutura narrativa real de posts — apenas descrição de agregador.
```

#### CTA dominante
- Padrão: Comentar palavra-chave no post para receber via DM um guia de '29 habilidades práticas do Claude' — inferido de fonte secundária (creatordb.app), não visto em caption direta.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: reels
- Engajamento estimado: medio

#### Temas identificados
- automação com Claude/IA
- serviços de automação para marcas

#### Limitação de dados
Instagram não indexado diretamente. Fonte única foi creatordb.app para handle 'lindsay.ai' (nota: config/profiles.json lista 'lindsay.ia' — possível divergência de handle a confirmar com o Lucas), com ~44K seguidores, taxa de engajamento de cabeçalho 5,5% (não verificada, estimativa de terceiro) e atração primária via YouTube/Reels/Stories. Nenhuma caption ou post individual visto diretamente; engajamento marcado 'medio' (conservador) em vez de 'alto' apesar da taxa citada pelo agregador.

---

### @andrevictor.m

**Categoria:** marketing

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes para determinar estrutura.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Limitação de dados
2 queries tentadas. Nenhum resultado correspondeu ao handle exato @andrevictor.m; apenas homônimos distintos em agregadores de terceiros. Nenhum post, caption ou métrica real identificada.

---

### @drisiano

**Categoria:** creator

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes para determinar estrutura.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Limitação de dados
2 queries tentadas. Nenhum resultado correspondeu ao handle exato @drisiano; apenas homônimos distintos não relacionados. Nenhum post, caption ou métrica real identificada.

---

### @brun0gpt

**Categoria:** ia

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes para determinar estrutura.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Limitação de dados
2 queries tentadas. Nenhum resultado correspondeu ao handle exato @brun0gpt; lead mais próximo (@brunobelissimo.ai) sem ligação confirmada. Nenhum post, caption ou métrica real identificada.

---

### @maxcarrau.ia

**Categoria:** ia

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes para determinar estrutura.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Limitação de dados
2 queries tentadas. Nenhum resultado correspondeu ao handle exato @maxcarrau.ia; apenas homônimos distintos de agregadores de terceiros. Nenhum post, caption ou métrica real identificada.

---

### @noevarner

**Categoria:** creator

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "Nenhuma caption literal encontrada; agregador de terceiros (CreatorDB) descreve o perfil, sob o handle variante 'noevarner.ai', como educador/consultor de negócios com IA, ativado principalmente via Reels/Stories, com YouTube como canal de maior alcance."

#### Estrutura típica do conteúdo
```
Dados insuficientes para determinar estrutura narrativa real de posts — apenas descrição de categoria por agregador de terceiros.
```

#### CTA dominante
- Padrão: Dados insuficientes — nenhuma citação literal de CTA encontrada.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: reels
- Engajamento estimado: baixo

#### Temas identificados
- educação em IA aplicada a negócios/consultoria — inferido de agregador de terceiros

#### Limitação de dados
Instagram não indexado diretamente. Único achado foi CreatorDB (dados de 22/set/2026), sob o handle 'noevarner.ai' — possível divergência de handle no config/profiles.json (perfil monitorado é 'noevarner', sem '.ai'), no mesmo padrão já visto em @nathanhodgson (lote 2). Nenhuma caption, hook ou métrica de engajamento real de post foi vista diretamente.

---

### @yikchanltd

**Categoria:** creator

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "dados insuficientes — nenhum post ou menção encontrada via WebSearch"

#### Estrutura típica do conteúdo
```
Dados insuficientes para determinar estrutura.
```

#### CTA dominante
- Padrão: Dados insuficientes.

#### Tom de voz
- Adjetivos: dados insuficientes

#### Métricas estimadas
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Limitação de dados
2 queries tentadas. Nenhum resultado mencionou o handle exato @yikchanltd. Achados mais próximos foram homônimos distintos e não relacionados (@yk fotógrafo de Singapura, @yikfei99, @yicheng.0227). Não há indício de que @yikchanltd seja a mesma pessoa/empresa que @yikC (lote 1, também sem dados) — tratar como perfis possivelmente distintos até confirmação do Lucas. Nenhum post, caption ou métrica real identificada.

---

## Perfis Sugeridos pelo Sistema
<!-- lista de perfis já populada (modo análise) — sem novas sugestões nesta execução -->

---

## Limitações de Dados (resumo)
