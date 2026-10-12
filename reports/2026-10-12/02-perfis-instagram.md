# Análise de Perfis Instagram — 2026-10-12

## ⚠️ Limitação estrutural identificada nesta execução

Execução automatizada via rotina agendada "Monitor Instagram - Módulo 2 semanal", seguindo a instrução de usar **WebSearch + WebFetch** (sem a skill `instagram-content-cloner`/Swarm, que dependem de um backend de execução não disponível nesta sessão) para coletar dados dos **61 perfis ativos** em `config/profiles.json`.

**Confirmado novamente nesta execução:** `www.instagram.com` continua **bloqueado a nível de rede** pelo proxy de egress deste ambiente (`getaddrinfo ENOTFOUND www.instagram.com` em teste direto de WebFetch). Agregadores de terceiros também falharam por DNS em pelo menos duas tentativas de WebFetch (`creatordb.app`, `buldrr.com` → `ENOTFOUND`) — ou seja, **todos os dados abaixo vêm exclusivamente de snippets do WebSearch**, sem confirmação direta em nenhuma página de origem.

O trabalho foi distribuído em 4 lotes paralelos (~15 perfis cada, via Agent/WebSearch) cobrindo os 61 perfis ativos, 1–2 buscas por handle, sem inventar dados.

**Resultado:** dos 61 perfis ativos, **61/61 (100%) têm `limitacao_dados` nos campos obrigatórios de hook/estrutura/CTA/tom/top_posts_temas** — nenhum post individual foi localizado via busca pública para nenhum perfil. **6 perfis (9,8%)** tiveram alguma informação agregada (seguidores, bio, nicho) recuperada de agregadores de terceiros via snippet — **não confirmada na fonte primária**. Os demais **55 perfis (90,2%)** não retornaram nenhum dado específico e verificável; buscas retornaram apenas conteúdo genérico ou perfis homônimos claramente distintos, descartados para evitar dado inventado.

**Recomendação para o Lucas (mantida de execuções anteriores):** os campos de extração profunda deste módulo (hook_modelos, cta_padrao, tom_exemplo_frase, top_posts_temas) dependem de acesso real aos posts do Instagram. Com o bloqueio de rede atual, isso só é viável por: (a) liberar `instagram.com` no proxy de egress deste ambiente, (b) usar a skill `instagram-content-cloner` a partir de uma sessão/ambiente com acesso ao Instagram e com o backend de execução (`swarm`) disponível, ou (c) importar dados manualmente (export/scraping feito fora deste ambiente). Sem isso, este módulo continuará retornando majoritariamente `limitacao_dados` nas próximas execuções agendadas.

---

## Visão Geral dos Perfis (com algum dado recuperável — não confirmado)

| Perfil | Categoria | Seguidores (IG, via agregador terceiro) | Nicho/Foco | Engajamento | Fonte |
|--------|-----------|-----------------------------------------|------------|-------------|-------|
| @charliehills | creator | ~70K–97K (duas fontes discordam) | LinkedIn/IA, agência de conteúdo, comunidade "AI Creators Club" | não quantificado | themarketingandaipodcast.alitu.com, creatordb.app |
| @nick_saraev | automacao | ~693.000 (IG) / ~531.000 (YouTube) | Automação de negócios com IA (n8n, Make.com, Claude Code), "Maker School" | não quantificado | creatordb.app, buldrr.com, iqfluence.io |
| @nathanhodgson | ia | ~146K–152K (handle indexado como "nathanhodgson.ai" — sufixo diferente do pedido, não confirmado ser o mesmo) | IA e produtividade, breakdowns de ferramentas Anthropic/Claude | não quantificado | creatordb.app |
| @chase.h.ai | ia | ~228.550 (IG) / ~163K (YouTube) / ~137,7K (TikTok) | Claude Code, mentoria 1:1 em IA | não quantificado | creatordb.app |
| @nikolassasso | creator | ~181.472 (dado de 22/09/2026, possível indício de inatividade — "último upload 7 meses atrás") | Marketing digital, estratégia de negócio online desde 2017 | 2,8% — baixo/médio | creatordb.app |
| @anatex | creator | ~717.000 (IG) | Educador de IA e negócios no Brasil | não quantificado (apenas +9K seguidores/30 dias) | creatordb.app (via snippet; WebFetch na página falhou por DNS) |

Os **55 perfis restantes** não retornaram nenhum dado específico verificável (ver seção "Limitações de Dados" abaixo) — todos marcados com `formato_dominante: indefinido`, `engajamento_estimado: indefinido` por ausência de dado real.

Nenhum dos 61 perfis teve hook, CTA, tom de voz ou tema de post real extraído — campo obrigatório `limitacao_dados` aplicado a 100% da amostra nesses campos.

---

## Análise Detalhada — Perfis com Dados Parciais

### @charliehills
**Categoria:** creator | **Tags:** ia, negocio-digital

- **Bio/posicionamento:** fundador da "Linked Agency" (agência de conteúdo para LinkedIn), da comunidade paga "AI Creators Club" e da ferramenta de infográficos com IA "Vislo".
- **Seguidores:** duas fontes terceiras discordam — ~70K (abr/2026) vs. ~97K (set/2026) — sem confirmação de qual reflete o handle exato.
- **Hook/estrutura/CTA/tom/top_posts_temas:** `limitacao_dados` — nenhum texto real de post encontrado.
- **Formato dominante:** indefinido

### @nick_saraev
**Categoria:** automacao | **Tags:** ia, automacao, agencia

- **Bio/posicionamento:** educador canadense, ensina automação de negócios com IA; fundador do programa "Maker School"; fundador de agências de serviço antes de migrar para educação.
- **Conteúdo:** Claude Code & Anthropic Developer Tools, AI Agency business, n8n & workflows agênticos, carreira em IA.
- **Hook/estrutura/CTA/tom/top_posts_temas:** `limitacao_dados`.
- **Formato dominante:** indefinido
- **Engajamento estimado:** indefinido (seguidores altos, sem dado de ER específico do Instagram)

### @nathanhodgson
**Categoria:** ia | **Tags:** ia, automacao

- **Bio:** segundo agregador, afirma ter trabalhado com Google, Meta, OpenAI e Anthropic — **não verificado por fonte independente**.
- **Conteúdo:** IA e produtividade; breakdowns de recursos Anthropic/Claude Code.
- **Observação:** handle indexado no agregador como "nathanhodgson.ai" (sufixo diferente do handle exato `nathanhodgson` configurado) — correspondência não confirmada.
- **Hook/estrutura/CTA/tom/top_posts_temas:** `limitacao_dados`.
- **Formato dominante:** indefinido

### @chase.h.ai
**Categoria:** ia | **Tags:** ia, automacao

- **Bio:** menção a "1:1 Mentorship" e "Claude Code" — negócio de mentoria em IA; criador baseado nos EUA.
- **Seguidores:** ~228.550 (IG), ~163K (YouTube), ~137,7K (TikTok) — snapshot único de agregador, sem checagem cruzada.
- **Hook/estrutura/CTA/tom/top_posts_temas:** `limitacao_dados`.
- **Formato dominante:** indefinido

### @nikolassasso
**Categoria:** creator | **Tags:** ia, negocio-digital

- **Bio/posicionamento:** educador de marketing digital e estratégia de negócio online, ativo desde 2017.
- **Seguidores:** ~181.472 (dado de 22/09/2026).
- **Engajamento:** 2,8% — baixo/médio (fonte: creatordb.app). Possível sinal de inatividade: "último upload 7 meses atrás" segundo a mesma fonte.
- **Hook/estrutura/CTA/tom/top_posts_temas:** `limitacao_dados`.
- **Formato dominante:** indefinido

### @anatex
**Categoria:** creator | **Tags:** negocio-digital

- **Bio/posicionamento:** descrito por agregador terceiro como educador de IA e negócios no Brasil — não confirmado na página de origem (WebFetch falhou por DNS).
- **Seguidores:** ~717.000 (IG), crescimento de +9K/30 dias.
- **Hook/estrutura/CTA/tom/top_posts_temas:** `limitacao_dados`.
- **Formato dominante:** indefinido
- **Engajamento estimado:** indefinido

---

## Limitações de Dados — Perfis sem nenhum dado recuperado (55)

Todos os campos do schema (hook_modelos, estrutura_tipica, cta_padrao, tom_adjetivos, formato_dominante, engajamento_estimado, top_posts_temas) estão em `limitacao_dados` para os perfis abaixo. WebSearch não retornou nenhuma informação específica e confiável sobre o handle exato — apenas conteúdo genérico de Instagram/marketing/IA, ou perfis homônimos claramente diferentes (descartados para evitar dado inventado):

@yikC, @eujoaotorresz, @fabianocarvalhojr, @rafa.grandi, @brusantanna.ai, @vendedorglobal, @oluizmain, @ai, @ana.gsoares, @leosoares.ia, @gabriel.adamuchi, @viverdeia.ai, @ninja.automacoes, @eduardocavalcanti, @jonylan, @allesinisgalli, @lonamkt, @gabrielbarbosa.oficial, @opensession.co, @leandroladeiran, @christiantriad, @oneyaraujo, @geracaotechs, @amandadinizmkt, @human___academy, @geiss11, @nelmoricalde, @rodrigotadewald, @sujeitoprogramador, @jonathan_kamargo, @marianatorre.s, @marketerhub.ai, @marcelaluzzio, @gestordeaudiencia, @sebintel, @avora.ai, @ogabrieeldias, @rodrigobindes, @franklim.gui, @gabrielsamp.ai, @maestrosdaia, @brandsdecoded__, @larissagomes.ia, @thiagozaao, @neuwebstudio, @laschuk, @maestroptompts, @faladantasmkt, @lindsay.ia, @andrevictor.m, @drisiano, @brun0gpt, @maxcarrau.ia, @noevarner, @yikchanltd

Casos notáveis descartados por ambiguidade/risco de confusão com homônimos (resultado existia mas apontava claramente para pessoa diferente): @eujoaotorresz (jogador João Torres, cantor "Jão"), @brusantanna.ai (confundido com Bruna Santana, irmã do cantor Luan Santana — handle/temática diferentes), @gabrielbarbosa.oficial (confundido com o jogador "Gabigol"), @geiss11 (confundido com a família "Die Geissens"), @ogabrieeldias (confundido com piloto/jogadores de futebol homônimos), @maestrosdaia (confundido com perfis "maestriasabia"/"maestrafede_"), @noevarner (confundido com @noyavner/@noedewitt), @yikchanltd (confundido com "Yik Keat"/"Yicheng").

**Observação comparativa com a execução de 2026-10-05:** 3 perfis que haviam retornado dado parcial na semana passada (@jonylan, @oneyaraujo, @rodrigobindes) não retornaram nada nesta execução, e 1 novo perfil (@charliehills) passou a retornar dado parcial que não havia aparecido antes — reflexo da natureza instável/não-determinística da indexação por WebSearch, não de mudança real nos perfis.

---

## Perfis Sugeridos pelo Sistema
Não aplicável nesta execução — `config/profiles.json` já tinha 61 perfis ativos (Modo Análise, não Modo Descoberta).
