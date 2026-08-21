# Análise de Perfis Instagram — 2026-08-09

**Modo de execução:** Análise (61 perfis ativos em `config/profiles.json`).

**Nota metodológica importante:** o Instagram bloqueia crawlers e não é indexado por buscadores em nível de post. Para todos os 61 perfis, a coleta foi feita via WebSearch (WebFetch direto ao Instagram não retorna conteúdo). Isso permitiu confirmar **bio, posicionamento, nicho e faixa de seguidores para 33 dos 61 perfis** — mas **não foi possível extrair hooks exatos, estrutura de post, CTA literal ou tom de voz com exemplos de frase para nenhum dos 61 perfis**, porque texto de posts/reels individuais não aparece nos resultados de busca (apenas a página de perfil, sem conteúdo). Esse é um limite estrutural da fonte, não uma falha pontual — documentado integralmente na seção "Limitações de Dados" em vez de preenchido com dados inventados.

---

## Visão Geral dos Perfis (dados confirmados via busca)

| Perfil | Categoria | Seguidores (aprox.) | Posicionamento confirmado |
|--------|-----------|---------------------|---------------------------|
| @fabianocarvalhojr | founder | 84K | Founder da lasy.ai — agentes de IA que vendem/operam negócios 24/7 |
| @vendedorglobal | negocio-digital | 83K | E-commerce & Marketplace, +100M views acumuladas |
| @oluizmain | creator | 215K | Mobile/IA, "clonagem de autoridade" |
| @nick_saraev | automacao | ~500K | Fundador da LeftClick (agência de automação IA B2B), Maker School |
| @nathanhodgson.ai | ia | 128K | "6-figure business powered by AI", citado por Google/Meta/OpenAI |
| @ana.gsoares | marketing | 146K | CEO @uniagiloficial, marketing digital e liberdade financeira |
| @chase.h.ai | ia | 221K | "Making AI Simple", foco em Claude Code, mentoria 1:1 |
| @leosoares.ia | ia | 219K | "CEO Acelera IA" — "IA tem que gerar RESULTADO" |
| @gabriel.adamuchi | creator | — | Marca "IA Fácil" — ensina IA e monetização com IA |
| @viverdeia.ai | ia | 129K | "Plataforma das empresas que crescem com IA", 2.000+ empresas aceleradas |
| @ninja.automacoes | automacao | — | Matheus Pessoa — automação e IA |
| @nikolassasso* | creator | 185K | IA para Negócios — growth, vendas, automação (*handle monitorado é "nikolassfaria"; possível variação/erro de handle — ver limitações) |
| @jonylan | creator | 306K | "Marketing Digital, Vendas e IA", Builder no Google Brasil |
| @gabrielbarbosa.oficial | creator | 7,8K | "+10MM faturados na internet" — negócios digitais |
| @leandroladeiran | marketing | — | Método "Venda Todo Santo Dia" — infoprodutos |
| @christiantriad | creator | 571K | "IA, Tech & SaaS", método "Tríade do Tempo", 2M+ pessoas treinadas |
| @oneyaraujo | creator | ~2M | Método "Código Viral®", 50K+ alunos, foco total em Reels |
| @human___academy* | ia | — | "Maior Escola de IA para Criativos" (*handle monitorado "humam__academy" — possível grafia diferente) |
| @sujeitoprogramador | ia | 168K | Matheus Fraga — programação e IA, 45K+ alunos |
| @marcelaluzzio | marketing | 226K | "Marketing de Conteúdo & I.A", MBA IA (USP) |
| @rodrigobindes | founder | 278K | Mentor de agências de marketing digital — "100k/mês com agência" |
| @franklim.gui | creator | 46K | Cursos de IA (Claude Code) e tráfego low-ticket |
| @maestrosdaia | ia | — | Automação de Instagram/Messenger, educação em IA |
| @brandsdecoded__* | marketing | 301K | "AI Content Agency" — "decodificando o futuro do marketing com AI" (*handle monitorado "brandsdecoded", conta real usa `__` no fim) |
| @anatex | ia | 694K | "Inteligência Artificial para Negócios" — maior conta confirmada da lista |
| @larissagomes.ia | ia | 15K | Marketing e Inteligência Artificial, "você + IA" |
| @laschuk | founder | 36K | Email marketing |
| @andrevictor.m | marketing | 244K | Conteúdo de lifestyle/riqueza — foco em IA não confirmado no bio encontrado |
| @brun0gpt | ia | 96K | "Impulso GPT VIRAL" — cresceu 96K sem tráfego pago em ~10 meses |
| @yikchanltd* | creator | 79K | "A.I., eCom, Business and Life Mentor" (*handle monitorado "yikchan" — conta real é "yikchanltd") |
| @brusantanna.ai | ia | — | "Estrategista de IA" — perfil confirmado, sem dados de conteúdo |
| @viverdeia | ia | (ver acima) | Registrado em profiles.json sem sufixo `.ai` — handle real da conta é `@viverdeia.ai` |

*Perfis marcados com \* têm indício de divergência entre o handle salvo em `config/profiles.json` e o handle real encontrado nas buscas — recomendado revisar manualmente (ver "Próximos Passos" no Módulo 6).

### Perfis sem dados suficientes (28 de 61)

Nenhuma informação de bio, seguidores ou posicionamento foi confirmada via busca para: `charliehills`, `yikC`, `eujoaotorresz`, `rafa.grandi`, `ai`, `eduardocavalcanti`, `allesinisgalli`, `lonamkt`, `opensession.co`, `geracaotechs`, `amandadinizmkt`, `geiss11`, `nelmoricalde`, `rodrigotadewald`, `jonathan_kamargo`, `marianatorre.s`, `marketerhub.ai`, `gestordeaudiencia`, `sebintel`, `avora.ai`, `ogabrieeldias`, `gabrielsamp.ai`, `thiagozaao`, `neuwebstudio`, `maestroptompts`, `faladantasmkt`, `lindsay.ia`, `drisiano`, `maxcarrau.ia`, `noevarner`.

(`marketerhub.ai` tem site institucional confirmado — comunidade de marketing com IA — mas sem confirmação de conta Instagram ativa correspondente.)

---

## Análise Detalhada por Perfil

Como nenhum hook, CTA ou trecho de post pôde ser extraído de nenhum perfil (ver nota metodológica), esta seção traz apenas o que foi **efetivamente confirmado**: posicionamento e proxy de porte de audiência. Os campos de Fase 1 do `instagram-content-cloner` (hook_modelos, estrutura_tipica, cta_padrao, tom_adjetivos com exemplos de frase) **não puderam ser preenchidos com dados reais para nenhum perfil** e foram deixados de fora do relatório em vez de inventados.

### Maiores contas confirmadas (proxy de relevância/autoridade)
1. **@oneyaraujo** — ~2M seguidores, "Código Viral®" (curso com IA própria — Chat Viral®)
2. **@anatex** — 694K seguidores, maior conta focada 100% em "IA para Negócios"
3. **@nick_saraev** — ~500K seguidores, referência internacional em AI automation agency
4. **@christiantriad** — 571K seguidores, IA/Tech/SaaS + método "Tríade do Tempo"
5. **@jonylan** — 306K seguidores, Marketing Digital + Vendas + IA
6. **@brandsdecoded__** — 301K seguidores, agência de conteúdo com IA
7. **@rodrigobindes** — 278K seguidores, mentoria de agências digitais
8. **@andrevictor.m** — 244K seguidores (posicionamento de riqueza/lifestyle, não IA pura)
9. **@marcelaluzzio** — 226K seguidores, marketing de conteúdo + IA (MBA USP)
10. **@chase.h.ai** — 221K seguidores, IA aplicada + Claude Code

### Frameworks/métodos nomeados identificados (sinal de produto de conteúdo estruturado)
- **Código Viral®** (@oneyaraujo) — treinamento de Reels virais, inclui IA própria (Chat Viral®) para gerar estrutura e copy
- **Tríade do Tempo** (@christiantriad) — método de produtividade aplicado a tech/IA
- **Impulso GPT VIRAL** (@brun0gpt) — curso de "bots" de Reels/Carrossel/Stories com IA, crescimento orgânico documentado (96K seguidores em ~10 meses sem tráfego pago)
- **Venda Todo Santo Dia** (@leandroladeiran) — método de vendas via infoproduto

---

## Perfis Sugeridos pelo Sistema

Não aplicável nesta execução — `config/profiles.json` já tem 61 perfis ativos (Modo Análise).

---

## Limitações de Dados

- **Limitação estrutural principal:** o Instagram bloqueia indexação de conteúdo de post/reel por buscadores. WebSearch retornou, na melhor hipótese, a página de perfil (bio + contagem de seguidores/posts) — nunca o texto de um hook, CTA ou estrutura narrativa de um post específico. Isso afeta os 61 perfis igualmente e é a razão pela qual os campos `hook_modelos`, `cta_padrao`, `tom_adjetivos` (com exemplo de frase) e `top_posts_temas` da Fase 1 do `instagram-content-cloner` não puderam ser preenchidos com dados reais para nenhum perfil.
- **28 de 61 perfis** não retornaram nenhuma informação confirmável (nem bio, nem contagem de seguidores) — listados acima em "Perfis sem dados suficientes". Handles genéricos ou pouco indexados (`ai`, `yikC`, `charliehills`) são os mais afetados.
- **Possível divergência de handle** em 4 contas (`nikolassfaria`→`nikolassasso`, `humam__academy`→`human___academy`, `brandsdecoded`→`brandsdecoded__`, `yikchan`→`yikchanltd`) — os nomes de usuário salvos em `config/profiles.json` podem estar desatualizados ou com erro de digitação. Recomendado validar manualmente antes da próxima execução.
- **`@viverdeia`** em `profiles.json` provavelmente deveria ser `@viverdeia.ai` (o handle real confirmado da marca "Viver de IA").
- Nenhum dado de engajamento (curtidas, comentários, taxa de engajamento real) foi encontrado ou inventado para qualquer perfil — todo dado de "formato dominante" ou "engajamento estimado" exigido pelo template foi omitido por falta de base real, seguindo a regra "nunca inventar dados".

**Impacto nos módulos seguintes:** os Módulos 3 (Benchmark) e 4 (Top 10) dependem de `top_posts_temas` deste relatório, que não pôde ser preenchido com posts específicos. Esses módulos serão adaptados para trabalhar com o sinal real disponível — porte de audiência, posicionamento e frameworks nomeados — em vez de posts individuais, com a limitação registrada explicitamente em cada um.
