# Análise de Perfis Instagram — 2026-10-05

## ⚠️ Limitação estrutural identificada nesta execução

Esta execução do Módulo 2 rodou em modo automatizado (via rotina agendada "Monitor Instagram - Módulo 2 semanal"), seguindo a instrução de usar **WebSearch + WebFetch** (sem a skill `instagram-content-cloner`/Swarm) para coletar dados dos 61 perfis ativos em `config/profiles.json`.

**Achado crítico:** neste ambiente de execução, `www.instagram.com` está **bloqueado a nível de rede** pelo proxy de egress (`EGRESS_BLOCKED`), confirmado em teste direto (`WebFetch` em `instagram.com/charliehills` retornou erro de bloqueio de domínio, não um bloqueio específico de scraping do Instagram). Ou seja, **WebFetch não pôde ser usado em nenhum dos 61 perfis** — não é uma limitação "por perfil", é total.

Restou apenas `WebSearch`, que **não indexa posts individuais do Instagram**. Na prática, para a esmagadora maioria dos handles monitorados (contas pequenas/médias, nichos BR de IA/marketing/automação), a busca geral na web não retorna nada específico — apenas artigos genéricos sobre Instagram ou perfis homônimos irrelevantes. Para alguns criadores maiores/mais conhecidos (principalmente com presença multi-plataforma indexada por agregadores como `creatordb.app`, `reportei.com`, `hypeauditor.com`), foi possível recuperar **metadados agregados** (contagem de seguidores, bio resumida, foco de conteúdo) — mas em **nenhum caso** foi possível recuperar exemplos reais de hooks, CTAs, tom de voz ou temas de posts específicos, porque isso exige visualizar os posts, e os posts em si são inacessíveis.

**Resultado:** dos 61 perfis ativos, **61/61 (100%) têm `limitacao_dados` nos campos de hook/estrutura/CTA/tom/top_posts_temas** (campos obrigatórios do schema do módulo). 8 perfis tiveram metadados parciais de audiência/nicho recuperados; os demais 53 não retornaram nenhum dado utilizável.

**Recomendação para o Lucas:** os campos de extração profunda deste módulo (hook_modelos, cta_padrao, tom_exemplo_frase, top_posts_temas) dependem de acesso real aos posts do Instagram. Com o bloqueio de rede atual, isso só é viável por: (a) liberar `instagram.com` no proxy de egress deste ambiente, (b) usar a skill `instagram-content-cloner` a partir de uma sessão/ambiente com acesso ao Instagram, ou (c) importar dados manualmente (export/scraping feito fora deste ambiente). Sem isso, este módulo continuará retornando majoritariamente `limitacao_dados` nas próximas execuções agendadas.

---

## Visão Geral dos Perfis (com algum dado recuperável)

| Perfil | Categoria | Seguidores (IG) | Nicho/Foco | Engajamento | Fonte |
|--------|-----------|-----------------|------------|-------------|-------|
| @nick_saraev | automacao | ~635.899 | Claude Code, n8n, AI agency, vibe coding | não quantificado | creatordb.app, buldrr.com |
| @nathanhodgson.ai | ia | ~145.933 | IA & produtividade, dicas diárias | não quantificado | creatordb.app |
| @chase.h.ai | ia | ~228.550 | Claude Code, AI agents, mentoria 1:1 | 3,0% (vs 1,5% mediana categoria) — alto | creatordb.app |
| @nikolassasso | creator | ~69.000 | Marketing digital, estratégia de negócio online | 12,3% — alto | creatordb.app |
| @jonylan | creator | ~346.474 | IA, estratégia de marketing, tecnologia | 5,4% | creatordb.app |
| @oneyaraujo | creator | ~1.300.000 | Viralização, Reels, monetização de audiência | não quantificado | reportei.com |
| @anatex | ia | ~717.000 (IG) | Hacks de marketing/IA, automação de negócio, mentoria digital | não quantificado | reportei.com, creatordb.app |
| @rodrigobindes | founder | não encontrado | Mentoria de agências, marketing para restaurantes | não encontrado | reportei.com |

Os 53 perfis restantes não retornaram nenhum dado específico verificável (ver seção "Limitações de Dados" abaixo) — todos marcados com `formato_dominante: indefinido`, `engajamento_estimado: indefinido` por ausência de dado real (não se deve inventar um valor do enum sem evidência).

---

## Análise Detalhada — Perfis com Dados Parciais

### @nick_saraev
**Categoria:** automacao | **Tags:** ia, automacao, agencia

- **Bio/posicionamento:** educador canadense, ensina automação de negócios com IA para >100K pessoas no Instagram (+79K no YouTube). Fundador de duas agências (1SecondCopy, LeftClick/AAA).
- **Conteúdo:** Claude Code & Anthropic Developer Tools, AI Agency (AAA) business & aquisição de clientes, n8n & workflows agênticos low-code, carreira em IA, cold outreach/lead gen.
- **Hook/estrutura/CTA/tom:** `limitacao_dados` — WebSearch não retornou texto de posts reais; apenas descrição de catálogo de conteúdo via newsletter/fóruns de terceiros.
- **Formato dominante:** indefinido (perfil multi-plataforma; proporção Reels vs. carrossel não verificável)
- **Engajamento estimado:** indefinido (seguidores altos, mas sem dado de ER específico do Instagram)

### @nathanhodgson.ai
**Categoria:** ia | **Tags:** ia, automacao

- **Bio:** "Daily tips & tools to master AI & 10x your productivity • Worked with Google, Meta, OpenAI, Anthropic"
- **Conteúdo:** IA e produtividade; ativado via Reels e Stories; patrocínios históricos em AI/Tech e SaaS/Finance (parceiros citados: Anthropic, Google).
- **Hook/estrutura/CTA/tom:** `limitacao_dados`.
- **Formato dominante:** reels (inferido da descrição de ativação, não confirmado por post real)
- **Engajamento estimado:** indefinido

### @chase.h.ai
**Categoria:** ia | **Tags:** ia, automacao

- **Bio:** "🤖 | Making AI Simple ⚡️ | DM 'Ready' to Apply For 1:1 Mentorship 🚀 | Master Claude Code 👇"
- **CTA padrão (único dado quase-literal recuperado):** DM com palavra-chave "Ready" para aplicar à mentoria — **isto é um padrão de CTA real, extraído da bio**, não de um post.
- **Conteúdo:** Claude Code workflows, AI agent deployment; audiência concentrada em EUA/UK/Canadá.
- **Engajamento:** 3,0% (vs. 1,5% mediana da categoria) — **alto relativo**, segundo creatordb.app.
- **Hook/estrutura/tom/top_posts_temas:** `limitacao_dados`.
- **Formato dominante:** indefinido

### @nikolassasso
**Categoria:** creator | **Tags:** ia, negocio-digital

- **Bio/posicionamento:** educador de marketing digital e estratégia de negócio online, atuando desde 2017.
- **Engajamento:** 12,3% — alto.
- **Hook/estrutura/CTA/tom/top_posts_temas:** `limitacao_dados`.
- **Formato dominante:** indefinido

### @jonylan
**Categoria:** creator | **Tags:** ia, negocio-digital

- **Bio/posicionamento:** estrategista de marketing digital e educador de IA no Brasil.
- **Frequência:** ~5,4 posts/semana no Instagram (maior base de seguidores entre as plataformas dele).
- **Engajamento:** 5,4%.
- **Audiência:** majoritariamente brasileira, masculina, profissionais 35+.
- **Hook/estrutura/CTA/tom/top_posts_temas:** `limitacao_dados`.
- **Formato dominante:** indefinido

### @oneyaraujo
**Categoria:** creator | **Tags:** negocio-digital, marketing

- **Bio/posicionamento:** produtor de conteúdo desde 2012, especialista em marketing viral (começou no YouTube com humor fitness, "Canal Ironia").
- **Conteúdo:** estratégias de viralização, crescimento de seguidores, monetização de audiência — foco declarado em Reels.
- **Formato dominante:** reels (único caso com confirmação razoável via fonte terceira).
- **Hook/estrutura/CTA/tom/top_posts_temas:** `limitacao_dados`.
- **Engajamento estimado:** indefinido (apesar de +1,3M seguidores)

### @anatex
**Categoria:** creator | **Tags:** negocio-digital

- **Bio/posicionamento:** educador de IA brasileiro, quase 1M seguidores combinados (IG+TikTok+YouTube). Instagram é a plataforma principal (74% da audiência).
- **Conteúdo:** "hacks" rápidos de marketing e IA, automação de negócios, geração de imagens com IA, mentoria digital — público-alvo: freelancers, consultores, empreendedores digitais.
- **Hook/estrutura/CTA/tom/top_posts_temas:** `limitacao_dados`.
- **Formato dominante:** indefinido

### @rodrigobindes
**Categoria:** founder | **Tags:** negocio-digital, saas, growth

- **Bio/posicionamento:** mentor de agências e expert em marketing para restaurantes; fundador da Mentoria Ultra; canal "Ultralize" (organização, eficiência, crescimento de agência).
- **Hook/estrutura/CTA/tom/top_posts_temas/engajamento/seguidores:** `limitacao_dados` (nenhum número confirmado).

---

## Limitações de Dados — Perfis sem nenhum dado recuperado (53)

Todos os campos do schema (hook_modelos, estrutura_tipica, cta_padrao, tom_adjetivos, formato_dominante, engajamento_estimado, top_posts_temas) estão em `limitacao_dados` para os perfis abaixo. WebSearch não retornou nenhuma informação específica e confiável sobre o handle (apenas artigos genéricos de Instagram/marketing, ou perfis homônimos claramente diferentes — descartados para evitar dado inventado):

@charliehills, @yikC, @eujoaotorresz, @fabianocarvalhojr, @rafa.grandi, @brusantanna.ai, @vendedorglobal, @oluizmain, @ai, @ana.gsoares, @leosoares.ia, @gabriel.adamuchi, @viverdeia.ai, @ninja.automacoes, @eduardocavalcanti, @allesinisgalli, @lonamkt, @gabrielbarbosa.oficial, @opensession.co, @leandroladeiran, @christiantriad, @geracaotechs, @amandadinizmkt, @human___academy, @geiss11, @nelmoricalde, @rodrigotadewald, @sujeitoprogramador, @jonathan_kamargo, @marianatorre.s, @marketerhub.ai, @marcelaluzzio, @gestordeaudiencia, @sebintel, @avora.ai, @ogabrieeldias, @franklim.gui, @gabrielsamp.ai, @maestrosdaia, @brandsdecoded__, @larissagomes.ia, @thiagozaao, @neuwebstudio, @laschuk, @maestroptompts, @faladantasmkt, @lindsay.ia, @andrevictor.m, @drisiano, @brun0gpt, @maxcarrau.ia, @noevarner, @yikchanltd

Casos notáveis descartados por ambiguidade (resultado existia mas apontava para pessoa/perfil diferente, não confirmado como o mesmo handle): @eduardocavalcanti (confundido com "eduardocabadaa", Lima/Peru), @gabrielbarbosa.oficial (confundido com o jogador Gabigol), @geiss11 (confundido com Carmen Geiss), @marianatorre.s (LinkedIn homônimo não confirmado), @thiagozaao (perfil "thiagaoofficial" não confirmado), @laschuk (associação a "GROWTHDOT" não confirmada), @maestrosdaia (confundido com "Maestra Genia"/Carol Savioli), @sujeitoprogramador (criador BR conhecido, mas busca não retornou dado específico do perfil Instagram).

---

## Perfis Sugeridos pelo Sistema
Não aplicável nesta execução — `config/profiles.json` já tinha 61 perfis ativos (Modo Análise, não Modo Descoberta).
