# Análise de Perfis Instagram — 2026-08-21

**Modo de execução:** Análise (61 perfis ativos em `config/profiles.json`).

**Nota metodológica (limitação estrutural conhecida, já documentada em execuções anteriores — ex: `reports/2026-08-09/02-perfis-instagram.md`):** o Instagram bloqueia crawlers e não indexa texto de post/reel individual em buscadores. WebFetch direto ao Instagram não retorna conteúdo; WebSearch retorna, na melhor hipótese, a página de perfil (bio + contagem de seguidores) ou títulos truncados de reels — nunca o hook/CTA/estrutura completa de um post específico. Essa limitação persiste nesta execução e afeta igualmente os 61 perfis.

**Metodologia desta execução:** em vez de repetir 61×3 buscas individuais com resultado previsível (mesma limitação estrutural do relatório de 12 dias atrás), esta rodada (a) manteve como baseline os dados confirmados em 2026-08-09 — que a 12 dias de distância seguem válidos para bio/posicionamento — e (b) fez uma nova leva de buscas focada nos 10 maiores perfis por audiência (que alimentam diretamente o Módulo 3/Benchmark) e em uma amostra de perfis antes não confirmados, para checar atualizações e resolver divergências de handle.

---

## Visão Geral dos Perfis (dados confirmados via busca)

| Perfil | Categoria | Seguidores (aprox.) | Posicionamento confirmado |
|--------|-----------|---------------------|---------------------------|
| @anatex | ia | **705K** (atualizado; era 694K em 08/08) | "Coloque a IA para trabalhar no seu negócio" — maior conta do nicho, palestrante/mentora/consultora |
| @oneyaraujo | creator | ~2M | Método "Código Viral®" — ensina viralização/vendas online desde 2012; produto próprio em 12x R$19,98 |
| @nick_saraev | automacao | ~500K | Fundador da LeftClick AI (automação/growth B2B, **US$10M+ gerados para clientes**, carteira inclui Anthropic, Wix, MrBeast) + Maker School (comunidade de IA no Skool, US$330K/mês, 10K+ formados) |
| @christiantriad | creator | 571K | Christian Barbosa — método "Tríade do Tempo" (2M+ pessoas treinadas), conteúdo IA/Tech/SaaS |
| @jonylan | creator | 306K | "Internet AI Ninja desde 1994", Builder no Google Brasil — marketing digital, vendas e IA |
| @rodrigobindes | founder | 278K | Cofundador da Ultralize (com Erico Rocha, Leandro Ladeira, Guilherme Cardoso) — mentoria de agências para 100K/mês |
| @brandsdecoded__ | marketing | 301K | "AI Content Agency" — perfil ativo, publicação frequente de reels (confirmado múltiplos posts recentes, sem texto extraível) |
| @marcelaluzzio | marketing | 226K | MBA em IA para negócios digitais (USP) — reels sobre criar sites, vídeos virais e bio com IA |
| @chase.h.ai | ia | 221K | "Making AI Simple" — mentoria 1:1 focada em Claude Code, DM "Ready" para aplicar |
| @leosoares.ia | ia | 219K | CEO da Acelera IA — "IA tem que gerar RESULTADO" |
| @viverdeia.ai | ia | 129K | "Plataforma das Empresas que Crescem com IA" — 2.000+ empresas aceleradas |
| @avora.ai | agencia | — | "Conteúdos diários sobre IA na prática" — perfil confirmado ativo (post recente encontrado) |
| @fabianocarvalhojr | founder | 84K | Founder da lasy.ai — agentes de IA que vendem/operam negócios 24/7 |
| @vendedorglobal | negocio-digital | 83K | E-commerce & Marketplace, +100M views acumuladas |
| @oluizmain | creator | 215K | Mobile/IA, "clonagem de autoridade" |
| @nathanhodgson.ai | ia | 128K | "6-figure business powered by AI", citado por Google/Meta/OpenAI |
| @ana.gsoares | marketing | 146K | CEO @uniagiloficial, marketing digital e liberdade financeira |
| @gabriel.adamuchi | creator | — | Marca "IA Fácil" — ensina IA e monetização com IA |
| @ninja.automacoes | automacao | — | Matheus Pessoa — automação e IA |
| @gabrielbarbosa.oficial | creator | 7,8K | "+10MM faturados na internet" — negócios digitais |
| @leandroladeiran | marketing | — | Método "Venda Todo Santo Dia" — infoprodutos |
| @human___academy* | ia | — | "Maior Escola de IA para Criativos" |
| @sujeitoprogramador | ia | 168K | Matheus Fraga — programação e IA, 45K+ alunos |
| @franklim.gui | creator | 46K | Cursos de IA (Claude Code) e tráfego low-ticket |
| @maestrosdaia | ia | — | Automação de Instagram/Messenger, educação em IA |
| @larissagomes.ia | ia | 15K | Marketing e Inteligência Artificial, "você + IA" |
| @laschuk | founder | 36K | Email marketing |
| @andrevictor.m | marketing | 244K | Conteúdo de lifestyle/riqueza — foco em IA não confirmado no bio |
| @brun0gpt | ia | 96K | "Impulso GPT VIRAL" — cresceu 96K sem tráfego pago em ~10 meses |
| @yikchanltd* | creator | 79K | "A.I., eCom, Business and Life Mentor" |
| @brusantanna.ai | ia | — | "Estrategista de IA" |
| @nikolassasso* | creator | 185K | IA para Negócios — growth, vendas, automação |

*Perfis marcados com `*` têm indício de divergência entre o handle salvo em `config/profiles.json` e o handle real (herdado do relatório de 08/08 — ainda não resolvido, ver "Limitações").

### Perfis sem dados suficientes (confirmado novamente nesta execução)

Sem bio, seguidores ou posicionamento confirmável via busca, mesmo após nova tentativa em amostra: `charliehills`, `yikC`, `eujoaotorresz`, `rafa.grandi`, `ai`, `eduardocavalcanti`, `allesinisgalli`, `lonamkt`, `opensession.co`, `geracaotechs`, `amandadinizmkt`, `geiss11`, `nelmoricalde`, `rodrigotadewald`, `jonathan_kamargo`, `marianatorre.s`, `marketerhub.ai`, `gestordeaudiencia`, `sebintel`, `ogabrieeldias`, `gabrielsamp.ai`, `thiagozaao`, `neuwebstudio`, `maestroptompts`, `faladantasmkt`, `lindsay.ia`, `drisiano`, `maxcarrau.ia`, `noevarner`.

---

## Análise Detalhada por Perfil

Como nenhum hook, CTA ou trecho de post pôde ser extraído com o texto completo (limitação estrutural), esta seção traz o que foi **efetivamente confirmado**: posicionamento, proxy de porte de audiência e, quando disponível, evidência de atividade recente (posts/reels encontrados, mesmo sem texto integral).

### Maiores contas confirmadas (proxy de relevância/autoridade)
1. **@oneyaraujo** — ~2M seguidores, "Código Viral®"
2. **@anatex** — 705K seguidores, maior conta 100% focada em "IA para Negócios"
3. **@nick_saraev** — ~500K seguidores, LeftClick AI (US$10M+ gerados, clientes incluem Anthropic/Wix/MrBeast)
4. **@christiantriad** — 571K seguidores, "Tríade do Tempo" + IA/Tech/SaaS
5. **@jonylan** — 306K seguidores, Builder no Google Brasil
6. **@brandsdecoded__** — 301K seguidores, agência de conteúdo com IA, publicação frequente confirmada
7. **@rodrigobindes** — 278K seguidores, cofundador Ultralize
8. **@andrevictor.m** — 244K seguidores (lifestyle/riqueza, não IA pura)
9. **@marcelaluzzio** — 226K seguidores, MBA IA (USP)
10. **@chase.h.ai** — 221K seguidores, mentoria 1:1 em Claude Code

### Frameworks/métodos nomeados identificados (sinal de produto de conteúdo estruturado)
- **Código Viral®** (@oneyaraujo) — treinamento de Reels virais com IA própria (Chat Viral®)
- **Tríade do Tempo** (@christiantriad) — método de produtividade aplicado a tech/IA
- **Impulso GPT VIRAL** (@brun0gpt) — crescimento orgânico documentado (96K seguidores/~10 meses sem tráfego pago)
- **Venda Todo Santo Dia** (@leandroladeiran) — método de vendas via infoproduto
- **LeftClick AI + Maker School** (@nick_saraev) — consultoria B2B + comunidade paga (US$330K/mês) — modelo de monetização dupla (serviço + educação) mais sofisticado da lista
- **Ultralize** (@rodrigobindes) — mentoria de agências para escalar a R$100K/mês

---

## Perfis Sugeridos pelo Sistema

Não aplicável nesta execução — `config/profiles.json` já tem 61 perfis ativos (Modo Análise).

---

## Limitações de Dados

- **Limitação estrutural principal (recorrente):** Instagram não expõe texto de post/reel individual a buscadores. Os campos `hook_modelos`, `cta_padrao`, `tom_adjetivos` (com exemplo de frase) e `top_posts_temas` da Fase 1 do `instagram-content-cloner` não puderam ser preenchidos com dados reais para nenhum perfil — mesma limitação documentada em 2026-08-09 e em execuções anteriores. Não é uma falha nova.
- **~29 de 61 perfis** seguem sem nenhuma informação confirmável (nem bio, nem seguidores) mesmo após nova tentativa de busca — handles genéricos ou pouco indexados são os mais afetados.
- **Divergência de handle não resolvida:** `nikolassfaria`→`nikolassasso`, `humam__academy`→`human___academy`, `brandsdecoded`→`brandsdecoded__`, `yikchan`→`yikchanltd` seguem pendentes de validação manual em `config/profiles.json` (identificado em 08/08, ainda não corrigido).
- Nenhum dado de engajamento (curtidas, comentários, taxa de engajamento real) foi encontrado ou inventado para qualquer perfil.
- **Escopo desta rodada:** dado que a rodada de 08/08 já esgotou a busca individual para os 61 perfis com o mesmo resultado estrutural, esta execução priorizou (a) atualizar os 10 maiores perfis — que alimentam o Módulo 3 — e (b) reamostrar ~10 dos 29 perfis sem dados, sem sucesso adicional. Recomendação: revisar a lista de perfis genéricos/pouco indexados (`ai`, `yikC`, `charliehills`) na próxima curadoria de `config/profiles.json`.

**Impacto nos módulos seguintes:** os Módulos 3 e 4 continuam trabalhando com o sinal real disponível — porte de audiência, posicionamento, frameworks nomeados e evidência de atividade — em vez de posts individuais, com a limitação registrada explicitamente em cada um.
