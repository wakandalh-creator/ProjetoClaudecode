# Análise de Perfis Instagram — 2026-07-20

> Executado em **Modo Análise** (Passo 2 do Módulo 2), a partir dos 61 perfis `active: true` em `config/profiles.json`. Coleta via WebSearch + WebFetch (fallback), em 12 lotes paralelos. O Instagram bloqueia scraping direto (WebFetch retornou HTTP 403 em praticamente 100% das tentativas de todos os lotes) — os dados abaixo vêm de snippets indexados por buscadores, frequentemente truncados. Nenhum dado foi inventado: onde a evidência real não existia, o campo `limitacao_dados` documenta exatamente o que faltou.

## Visão Geral dos Perfis

| Perfil | Categoria | Formato Dominante | Engajamento | Hook/Observação |
|--------|-----------|-------------------|-------------|------------------|
| @charliehills | creator | reels | baixo | "Did you know ChatGPT has 8 hidden personalities..." (fenômeno nomeado) |
| @yikC | creator | — | — | Handle não localizado/ambíguo |
| @eujoaotorresz | creator | — | — | Perfil não localizado |
| @fabianocarvalhojr | founder | misto | baixo | "Quem mais?... Siga @fabianocarvalhojr..." |
| @rafa.grandi | marketing | — | — | ⚠️ Handle aponta para pessoa física não relacionada (analista jurídico) |
| @brusantanna.ai | ia | — | — | Perfil Instagram não localizado (só achado no TikTok) |
| @vendedorglobal | negocio-digital | reels | médio | "Ganhe em DÓLAR sem precisar investir NADA!" |
| @oluizmain | creator | reels | médio | CTA "Salve/Siga @oluizmain" |
| @nick_saraev | automacao | reels | alto | "Comment [PALAVRA] to get this [ferramenta IA grátis]" |
| @nathanhodgson | ia | reels | médio | ⚠️ Handle correto provável: @nathanhodgson.ai |
| @ai | ia | — | — | Handle extremamente ambíguo, não identificável |
| @ana.gsoares | marketing | misto | baixo | "Por alguns anos, eu dava o meu máximo..." |
| @chase.h.ai | ia | reels | baixo | CTA "DM Ready to Apply For 1:1 Mentorship" |
| @leosoares.ia | ia | reels | baixo | CTA "Comenta [PALAVRA-CHAVE]" |
| @gabriel.adamuchi | creator | reels | baixo | "Não se fala em outra coisa a não ser CLAUDE..." |
| @viverdeia | ia | reels | médio | "20 MILHÕES NO PRIMEIRO ANO, ISSO AQUI É @viverdeia.ai" |
| @ninja.automacoes | automacao | reels | baixo | "Chega de 'automação Nutella'..." |
| @nikolassfaria | creator | — | — | Perfil não localizado |
| @eduardocavalcanti | founder | misto | médio | Sem legenda autoral confirmada, só bio |
| @jonylan | creator | reels | médio | "Aproveite 15 meses GRÁTIS do Google Gemini Pro..." |
| @allesinisgalli | founder | reels | baixo | Sem hook confirmado, só bio/temas |
| @lonamkt | marketing | misto | baixo | "🇮🇹 Primeiro milhão aos 18 👇" — ⚠️ possível mismatch de categoria |
| @gabrielbarbosa.oficial | creator | reels | baixo | Bio "+10MM faturados na internet" |
| @opensession.co | agencia | misto | médio | Bio institucional B2B (Brand x UX/AI) |
| @leandroladeiran | marketing | reels | alto | Sem post específico, só bio (2M seguidores, VTSD) |
| @christiantriad | creator | reels | alto | "❌ DESCONFIE TODA VEZ QUE VOCÊ..." |
| @oneyaraujo | creator | reels | alto | Estrutura confirmada: Gancho→Benefício→Mostre→CTA (curso Código Viral) |
| @geracaotechs | ia | misto | baixo | "Já imaginou modificar qualquer carro com IA?" (via Threads) |
| @amandadinizmkt | marketing | misto | baixo | Bio conflitante entre fontes, sem posts confirmados |
| @humam__academy | ia | — | — | ⚠️ Handle não localizado; achado @human___academy (grafia diferente) |
| @geiss11 | creator | misto | baixo | "Sem legenda… Me siga para mais @geiss11" |
| @nelmoricalde | creator | — | — | Só bio confirmada, sem posts |
| @rodrigotadewald | marketing | misto | baixo | Só bio confirmada (183K seguidores), sem posts |
| @sujeitoprogramador | ia | carrossel | baixo | "Se você vai criar Agent IA com n8n..." (via Threads) |
| @jonathan_kamargo | creator | — | — | Perfil não localizado |
| @marianatorre.s | marketing | misto | baixo | "Como treinar seu Claude em 15 segundos!" |
| @marketerhub.ai | marketing | misto | baixo | "Comment 'Free' for the link..." |
| @marcelaluzzio | marketing | reels | médio | "VENDA SEM APARECER COM IA 🔥" |
| @gestordeaudiencia | marketing | — | — | Perfil não localizado |
| @sebintel | ia | reels | baixo | "Comment 'Cut'/'AI'/'vibe'/'Design' and I'll send the link" (padrão consistente, 4+ posts) |
| @avora.ai | agencia | — | — | Perfil não localizado com dados |
| @ogabrieeldias | creator | — | — | Só snippet "SaaS Founder" (diverge da categoria) |
| @rodrigobindes | founder | reels | médio | "Dono de agência, quer espantar os seus clientes? Faça isto" |
| @franklim.gui | creator | reels | médio | "What is Claude Code? Comment CODE..." |
| @gabrielsamp.ai | ia | — | — | Perfil Instagram não localizado (só TikTok) |
| @maestrosdaia | ia | reels | baixo | "6 Ferramentas de IA Secretas Que Ninguém Te Conta" |
| @brandsdecoded | marketing | reels | baixo | ⚠️ Handle correto provável: @brandsdecoded__ |
| @anatex | creator | reels | baixo | "Salva esse post" (padrão confirmado em 4+ posts) |
| @larissagomes.ia | ia | reels | baixo | "Peça o chatGPT para analisar o feed do seu instagram" |
| @thiagozaao | creator | — | — | Perfil não localizado |
| @neuwebstudio | agencia | reels | médio | "Cinematic Web Design" (bio) |
| @laschuk | founder | reels | médio | "salva o vídeo pra não perder" + 6 hooks truncados |
| @maestroptompts | ia | — | — | Perfil não localizado/não indexado |
| @faladantasmkt | marketing | misto | médio | Sem post específico, só bio/produtos (MCV, Insta Poderoso) |
| @lindsay.ia | ia | — | — | Perfil não localizado/não indexado |
| @andrevictor.m | marketing | reels | baixo | "Como parar de procrastinar em 20 segundos" |
| @drisiano | creator | — | — | Perfil não localizado |
| @brun0gpt | ia | reels | baixo | Bio robusta, sem legenda de post confirmada |
| @maxcarrau.ia | ia | reels | baixo | Dados extremamente limitados (só site terceiro) |
| @noevarner | creator | reels | baixo | ⚠️ Handle correto provável: @noevarner.ai — "This is how you actually use Claude to go viral" |
| @yikchan | creator | misto | baixo | ⚠️ Handle correto provável: @yikchanltd |

---

## Análise Detalhada — Perfis com Dados Reais Relevantes

### @nick_saraev (automacao)
**Seguidores:** 529K · **Formato:** reels · **Engajamento:** alto (sinal indireto — múltiplas contas de fã/compilação dedicadas)

- **Hook recorrente:** paradoxo/contraste — "You don't have to be a genius to make money..."
- **CTA padrão (confirmado em 6+ posts):** `Comment [PALAVRA-CHAVE] to get this [ferramenta/automação de IA gratuita]` — variações: FLUX, OPENSOURCE, QWEN, VIDEO, SYSTEM, APIFY
- **Tom:** direto, técnico, confiante, orientado a ação. Bio: "I help make AI work for you 👇 | Get your first client in 90d or full refund"
- **Temas:** ferramentas IA opensource (Qwen, Flux), automação n8n/Apify, templates para agências, aquisição de clientes
- **Limitação:** legendas completas não recuperadas (apenas títulos truncados); frequência exata do padrão de CTA não medida com precisão.

### @sebintel (ia)
**Formato:** reels · **Engajamento:** baixo (sem seguidores confirmados, mas padrão de conteúdo é o mais consistente encontrado em todo o lote)

- **Estrutura confirmada em 4+ reels distintos:** demonstração rápida de ferramenta de IA → promessa de resultado imediato → CTA de comentário
- **CTA padrão:** `Comment [PALAVRA-CHAVE] and I'll send/DM you the link` — variações: "Cut", "AI", "vibe", "Design"
- **Tom:** direto, tutorial, orientado a ferramentas, promocional
- **Temas:** geração de sites/apps/imagens via IA, filtros de Stories, avatar de IA (fonte externa aponta pipeline 100% automatizado por Sebastien Jefferies)
- **Limitação:** número de seguidores não confirmado; legendas completas além da primeira frase não recuperadas.

### @oneyaraujo (creator)
**Seguidores:** ~2M (+66 mil alunos do curso) · **Formato:** reels · **Engajamento:** alto

- **Estrutura confirmada pelo próprio autor** (cross-post no TikTok): roteiro de 4 partes — Gancho → Benefício → Mostre → CTA (é o método que ensina no curso "Código Viral")
- **Hooks:** "🚨 JÁ CHEGOU PARA VOCÊ? 🚀"; "1 ano de Instagram em 40 segundos. Conheça o Código Viral..."
- **CTA:** link na bio (curso Código Viral) / "me conta nos comentários"
- **Tom:** urgente, promocional, energético, direto, didático
- **Temas:** como viralizar no Instagram, curso Código Viral, crescimento de seguidores, IA vs criação de conteúdo
- **Limitação:** não confirmado se ele de fato segue essa fórmula em 100% dos posts (apenas descrita pelo próprio autor em outro canal).

### @christiantriad (creator)
**Seguidores:** 349K–584K (fontes divergem) · **Formato:** reels · **Engajamento:** alto

- **Hooks:** "❌ DESCONFIE TODA VEZ QUE VOCÊ..." (maioria errando); "As empresas estão desesperadas por essa profissão!" (paradoxo/contraste); citação de autoridade (Bill Gates)
- **CTA:** pergunta reflexiva / "comente aqui"
- **Tom:** direto, provocador, motivacional, didático, confiante
- **Temas:** IA, produtividade/gestão do tempo, carreira, tecnologia/SaaS, citações motivacionais
- **Limitação:** contagem de seguidores inconsistente entre fontes; frequência de cada modelo de hook é estimativa de baixa confiança.

### @anatex (creator)
**Seguidores:** 688K · **Formato:** reels · **Engajamento:** baixo (sem taxa real, só seguidores)

- **Padrão de CTA confirmado em 4+ posts:** "Salva esse post" — variações: "Salva esse post e segue @anatex...", "Salva este post agora e nunca mais perca tempo...", "Já salva esse post para não perder o tutorial!"
- **Hook:** abertura numerada ("1️⃣ Já salva esse post...")
- **Tom:** didático, direto, urgência (escassez), prático
- **Temas:** tutoriais de IA para negócios, produtividade, dicas de ferramentas de IA

### @marcelaluzzio (marketing)
**Seguidores:** 226K · **Formato:** reels · **Engajamento:** médio

- **Hooks:** "VENDA SEM APARECER COM IA 🔥"; "20k novos seguidores com Claude 🔥"
- **CTA:** `Comente [PALAVRA-CHAVE] e receba o link/acesso por DM`
- **Tom:** direto, promocional, educativo, orientado a resultado. Bio: MBA em IA pela USP
- **Temas:** IA aplicada a vendas/marketing, ferramentas de IA, crescimento de seguidores com Claude

### @gabriel.adamuchi (creator)
**Formato:** reels · **Engajamento:** baixo

- **Hook:** "Não se fala em outra coisa a não ser CLAUDE, né? 😮‍💨"
- **CTA (padrão claro, 3 variações):** `Comenta "[PALAVRA]" que te mando/envio pela DM` — ex.: "CURSO", "MINE", "IA"
- **Tom:** descomplicado, didático, acessível, informal
- **Temas:** tutoriais de IA para iniciantes, prompts prontos, cursos/guias de IA, Claude

### @rodrigobindes (founder)
**Seguidores:** ~280K · **Formato:** reels · **Engajamento:** médio

- **Hooks:** "Dono de agência, quer espantar os seus clientes? Faça isto"; "Essa é a melhor maneira de continuar pobre..."
- **Tom:** direto, provocativo, mentor-consultivo, assertivo. Bio: "Mentor de Agências de Marketing Digital"
- **Temas:** gestão de agências, aquisição/retenção de clientes, faturamento/escala, mentoria Ultralize

### @franklim.gui (creator)
**Seguidores:** ~46K · **Formato:** reels · **Engajamento:** médio

- **Hooks:** "Subiu uma oferta e deu prejuízo? Relaxa..."; "What is Claude Code? Comment CODE and I'll send you a..."
- **Tom:** didático, direto, casual, vendedor. Bio: "Meus cursos sobre IA (principalmente Claude Code)"
- **Temas:** cursos sobre Claude Code, tráfego direto low-ticket, funis de venda

### @noevarner (creator) ⚠️
**Formato:** reels · **Engajamento:** baixo

- ⚠️ **Divergência de handle:** conta ativa com conteúdo é `@noevarner.ai`, não `@noevarner` — não confirmado se é o mesmo perfil ou um handle diferente.
- **Hook (real, confirmado):** "This is how you actually use Claude to go viral"
- **Tom:** prático, tutorial, direto, voltado a automação. Bio: "Claude Code Junkie"
- **Temas:** automação de conteúdo com Claude, tutoriais Claude Code, geração de carrosséis virais

---

## Perfis com Dados Mínimos ou Inexistentes (ver detalhes completos em Limitações)

Os seguintes 41 perfis tiveram coleta tentada mas retornaram dados insuficientes para uma análise de padrão confiável (bio isolada, 0-1 fragmento de legenda truncado, ou perfil não localizado): @yikC, @eujoaotorresz, @fabianocarvalhojr, @rafa.grandi, @brusantanna.ai, @vendedorglobal, @oluizmain, @nathanhodgson, @ai, @ana.gsoares, @chase.h.ai, @leosoares.ia, @viverdeia, @ninja.automacoes, @nikolassfaria, @eduardocavalcanti, @jonylan, @allesinisgalli, @lonamkt, @gabrielbarbosa.oficial, @opensession.co, @leandroladeiran, @geracaotechs, @amandadinizmkt, @humam__academy, @geiss11, @nelmoricalde, @rodrigotadewald, @sujeitoprogramador, @jonathan_kamargo, @marianatorre.s, @marketerhub.ai, @gestordeaudiencia, @avora.ai, @ogabrieeldias, @gabrielsamp.ai, @maestrosdaia, @brandsdecoded, @larissagomes.ia, @thiagozaao, @neuwebstudio, @laschuk, @maestroptompts, @faladantasmkt, @lindsay.ia, @andrevictor.m, @drisiano, @brun0gpt, @maxcarrau.ia, @yikchan.

Charliehills teve 2 fragmentos reais de hook mas insuficientes para padrão. Detalhes completos de cada limitação estão na seção abaixo.

---

## Perfis Sugeridos pelo Sistema

Não aplicável nesta execução — o sistema operou em **Modo Análise** (lista de `config/profiles.json` já continha 61 perfis ativos), não em Modo Descoberta.

---

## ⚠️ Ação Recomendada: Handles a Verificar em `config/profiles.json`

Os seguintes perfis apresentaram forte indício de handle incorreto, inexistente ou ambíguo — recomenda-se conferência manual antes da próxima execução:

| Handle configurado | Problema identificado | Achado alternativo |
|---|---|---|
| `rafa.grandi` | Aponta para pessoa física não relacionada ao nicho (analista jurídico, 247 seguidores) | — |
| `nathanhodgson` | Perfil não confirmado | Provável: `nathanhodgson.ai` (144K seguidores, nicho IA) |
| `humam__academy` | Não localizado (grafia com 2 underscores) | Encontrado: `human___academy` (3 underscores, 303K seguidores) — grafia diferente, não confirmado ser o mesmo |
| `brandsdecoded` | Não localizado exatamente | Encontrado: `brandsdecoded__` (underscores duplos, 301K seguidores) |
| `noevarner` | Perfil sem conteúdo indexado | Provável: `noevarner.ai` |
| `yikchan` | Perfil sem conteúdo indexado | Provável: `yikchanltd` (78K seguidores) |
| `yikC` | Handle ambíguo, nenhuma conta correspondente localizada | — |
| `eujoaotorresz` | Não localizado (possível erro de digitação) | — |
| `nikolassfaria` | Não localizado | — |
| `jonathan_kamargo` | Não localizado | — |
| `thiagozaao` | Não localizado | — |
| `drisiano` | Não localizado | — |
| `maestroptompts` | Não localizado/não indexado | — |
| `lindsay.ia` | Não localizado/não indexado | — |
| `gestordeaudiencia` | Não localizado | — |
| `avora.ai` | Não localizado com dados | — |
| `gabrielsamp.ai` | Só localizado no TikTok, não no Instagram | — |
| `brusantanna.ai` | Só localizado no TikTok, não no Instagram | — |
| `ai` | Handle de 1 palavra, extremamente ambíguo | — |
| `lonamkt` | Conteúdo real (storytelling pessoal "primeiro milhão aos 18") não bate com categoria "marketing" | — |

---

## Limitações de Dados

**Causa raiz comum a todos os perfis:** o Instagram retorna HTTP 403 a qualquer WebFetch não autenticado (bloqueio padrão anti-scraping), então nenhum dado veio de acesso direto ao perfil ou aos posts — tudo foi reconstruído a partir de snippets indexados por buscadores (WebSearch), que costumam vir truncados ("...") e sem métricas reais de curtidas/comentários/taxa de engajamento. Onde `engajamento_estimado` aparece como "médio" ou "alto", isso reflete apenas contagem de seguidores ou sinais indiretos (contas de fã, menções de audiência), nunca uma taxa de engajamento medida.

- @charliehills — apenas 2 trechos truncados de hook; sem CTA nem legendas completas.
- @yikC — handle não confirmado; múltiplas contas parecidas mas nenhuma coincidente.
- @eujoaotorresz — perfil não localizado; possível handle incorreto.
- @fabianocarvalhojr — 1 trecho truncado real; sem estrutura/CTA completos.
- @rafa.grandi — conta encontrada é de outra pessoa (analista jurídico), incompatível com o nicho esperado.
- @brusantanna.ai — Instagram não localizado; único achado real foi no TikTok, não usado para não misturar plataformas.
- @vendedorglobal — dados via snippets truncados; sem legendas completas.
- @oluizmain — apenas CTAs de encerramento localizados, sem hooks de abertura.
- @nathanhodgson — divergência de handle (ver seção de Ação Recomendada); dados atribuídos são uma suposição.
- @ai — handle de 1 palavra impossível de desambiguar via busca.
- @ana.gsoares — hooks truncados; nenhuma taxa de engajamento real.
- @chase.h.ai — 1 título de reel real; sem hooks adicionais confirmados.
- @leosoares.ia — apenas padrões de CTA localizados, sem hook de abertura completo.
- @viverdeia — legendas truncadas pelos snippets; sem métricas reais.
- @ninja.automacoes — possível ambiguidade entre `.automacoes` e `_automacoes`; nenhuma contagem de seguidores encontrada.
- @nikolassfaria — perfil não localizado; apenas homônimos não relacionados.
- @eduardocavalcanti — textos localizados parecem alt-text automático, não legenda autoral.
- @jonylan — CTA não confirmado (buscas por termos de CTA retornaram reels de outros perfis).
- @allesinisgalli — nenhum hook/CTA real encontrado; contagem de seguidores inconsistente entre fontes.
- @lonamkt — perfil com baixíssima indexação (só 2 posts aparentes); conteúdo real diverge da categoria "marketing".
- @gabrielbarbosa.oficial — apenas títulos truncados, não usados como hook por falta de confiabilidade.
- @opensession.co — apenas bio institucional, sem posts específicos.
- @leandroladeiran — apenas bio, nenhum post específico encontrado apesar do alto volume de seguidores.
- @geracaotechs — dados vieram de cross-post no Threads, não do Instagram diretamente.
- @amandadinizmkt — bio conflitante entre fontes de busca; nenhum post confirmado.
- @humam__academy — divergência de grafia de handle (ver Ação Recomendada); dados não atribuídos por segurança.
- @geiss11 — apenas 1 legenda real via indexação de reel.
- @nelmoricalde — apenas bio confirmada, nenhum post.
- @rodrigotadewald — apenas bio confirmada (183K seguidores), nenhuma legenda de post encontrada.
- @sujeitoprogramador — única frase real veio do Threads, não confirmada como publicada no Instagram.
- @jonathan_kamargo — perfil não localizado; apenas homônimos não relacionados.
- @marianatorre.s — apenas 2 títulos de post reais, amostra insuficiente para padrão.
- @marketerhub.ai — apenas 1 legenda real; contas parecidas (@marketerhubcom, @marketer_hub) descartadas por não serem o mesmo perfil.
- @marcelaluzzio — títulos truncados; engajamento estimado só por contagem de seguidores.
- @gestordeaudiencia — nenhum dado real do Instagram; atribuição a "Daniel Feitosa" encontrada via GitHub não foi usada por não ter fonte no Instagram.
- @sebintel — sem contagem de seguidores confirmada; legendas completas não recuperadas.
- @avora.ai — apenas confirmação de existência do perfil, nenhum conteúdo.
- @ogabrieeldias — apenas snippet "SaaS Founder" (categoria diverge de "creator" informada).
- @rodrigobindes — apenas 3 títulos de reels reais; corpo dos vídeos não acessível.
- @franklim.gui — CTA inferido de 1 título parcial em inglês, frequência não confirmada.
- @gabrielsamp.ai — perfil Instagram não localizado; apenas TikTok confirmado.
- @maestrosdaia — hook e CTA baseados em apenas 1 exemplo cada.
- @brandsdecoded — divergência de handle (`brandsdecoded__`); hooks truncados.
- @larissagomes.ia — legenda completa veio de cross-post no TikTok, presumida (não confirmada) como idêntica no Instagram.
- @thiagozaao — perfil não localizado em nenhuma busca ou plataforma.
- @neuwebstudio — nenhuma legenda de post encontrada, apenas bio e dados cruzados do TikTok.
- @laschuk — hooks/CTAs truncados por snippets; frequência real não confirmada.
- @maestroptompts — perfil não localizado/não indexado em nenhuma busca.
- @faladantasmkt — dados vêm de página de vendas de cursos (faladantas.com), não de posts reais do Instagram.
- @lindsay.ia — perfil não localizado/não indexado em nenhuma busca.
- @andrevictor.m — apenas 1 título de reel confirmado com segurança; outros fragmentos descartados por falta de atribuição confiável.
- @drisiano — perfil não localizado em nenhuma busca ou plataforma.
- @brun0gpt — bio robusta confirmada, mas nenhuma legenda de post específica confirmada como pertencente ao perfil.
- @maxcarrau.ia — dados extremamente limitados; único sinal é um site de terceiros associado ao nome do criador.
- @noevarner — divergência de handle (`noevarner.ai`); apenas 1 legenda real confirmada.
- @yikchan — divergência de handle (`yikchanltd`); nenhuma legenda ou hook específico encontrado, apenas bio.
