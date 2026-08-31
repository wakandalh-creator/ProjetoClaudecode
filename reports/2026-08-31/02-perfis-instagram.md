# Análise de Perfis Instagram — 2026-08-31

## Nota de metodologia (leia antes de usar os dados abaixo)

- Execução do **Módulo 2, Passo 2 (Modo Análise)** — `config/profiles.json` já tinha 61 perfis ativos, então o Modo Descoberta foi pulado.
- **WebFetch direto em `instagram.com` foi bloqueado pelo proxy de rede do ambiente (`EGRESS_BLOCKED`) em 100% das tentativas**, para os 61 perfis. Todos os dados abaixo vêm de **WebSearch** (snippets indexados, bios resumidas por agregadores tipo Social Blade/Hafi.pro, cross-posts em TikTok/YouTube/Threads do mesmo criador).
- Isso limita fortemente o que dá pra confirmar: número de seguidores, bio e posicionamento geral costumam aparecer; **legendas completas de posts, CTAs literais e estrutura exata de Reels raramente aparecem** — quando não há uma citação real, o campo foi preenchido com `"não encontrado"` ou `"Dados insuficientes..."`, nunca inventado.
- Quando um exemplo de hook/frase veio de uma plataforma-irmã (TikTok/YouTube) do mesmo criador em vez do Instagram propriamente, isso está sinalizado explicitamente na limitação de cada perfil.
- **13 dos 61 handles têm problema de resolução** (não existem, apontam para pessoa/conta errada, ou são ambíguos com outro handle parecido) — ver seção final "Perfis com Problema de Resolução" para ação recomendada no `config/profiles.json`.

---

## Visão Geral dos 61 Perfis

| Perfil | Categoria | Formato Dominante | Engajamento | Hook/Posicionamento identificado |
|--------|-----------|--------------------|--------------|-----------------------------------|
| @charliehills | creator | misto | alto | "I help you (actually) use AI" (bio) |
| @yikC | creator | misto | baixo | ⚠️ handle não resolvido |
| @eujoaotorresz | creator | misto | baixo | ⚠️ handle não resolvido / possível pessoa errada |
| @fabianocarvalhojr | founder | misto | alto | "Crio Agentes de IA que vendem e operam Negócios 24/7" |
| @rafa.grandi | marketing | misto | baixo | ⚠️ conta real, mas de analista jurídico — mismatch |
| @brusantanna.ai | ia | misto | médio | "Comenta CLAUDE aqui que eu te mando o guia completo" |
| @vendedorglobal | negocio-digital | reels | alto | E-commerce/marketplace + IA aplicada a vendas |
| @oluizmain | creator | reels | baixo | Treinamento "Mobile Pro" (produção de vídeo mobile) |
| @nick_saraev | automacao | reels | alto | Maker School — garantia "1º cliente em 90 dias" |
| @nathanhodgson | ia | misto | alto | ⚠️ handle pode ser `nathanhodgson.ai` |
| @ai | ia | misto | baixo | ⚠️ não identificável/não verificável |
| @ana.gsoares | marketing | misto | médio | Prompts de IA p/ vagas de emprego; CEO Uniagil |
| @chase.h.ai | ia | reels | alto | "Making AI Simple" — mentoria 1:1, Claude Code |
| @leosoares.ia | ia | misto | alto | IA para negócios/lançamentos — CEO Acelera IA |
| @gabriel.adamuchi | creator | reels | baixo | Prompts de imagem IA prontos ("IA Fácil") |
| @viverdeia.ai | ia | misto | médio | "A Plataforma das Empresas que Crescem com IA" |
| @ninja.automacoes | automacao | misto | baixo | Infoproduto "Ninja Academy" (automação/Hotmart) |
| @nikolassasso | creator | misto | médio | "Criei robôs que fazem o trabalho duro por mim" |
| @eduardocavalcanti | founder | misto | médio | "Maestro de Hiperagentes" — Presidente IBIA |
| @jonylan | creator | reels | alto | "AI Ninja of the internet since 1994" |
| @allesinisgalli | founder | misto | baixo | "AI & MARKETING — IA CLUB COMUNIDADE" |
| @lonamkt | marketing | misto | baixo | "Primeiro milhão aos 18" (só 2 posts indexados) |
| @gabrielbarbosa.oficial | creator | misto | baixo | "+10MM faturados na internet" |
| @opensession.co | agencia | misto | médio | Agência de design "Brand x UX/AI x Design Systems" |
| @leandroladeiran | marketing | reels | alto | Copywriting, ROI vs ROAS, tráfego pago |
| @christiantriad | creator | reels | alto | Meta-conteúdo: "Importância dos Ganchos nos Reels" |
| @oneyaraujo | creator | reels | alto | "Código Viral" — estrutura Gancho→Benefício→Mostre→CTA |
| @geracaotechs | ia | misto | baixo | Descoberta de ferramentas de IA ("esse site permite...") |
| @amandadinizmkt | marketing | misto | baixo | Conta confirmada, sem conteúdo indexado |
| @human___academy | ia | misto | alto | "A Maior Escola de IA para Criativos" |
| @geiss11 | creator | reels | médio | Venda de produtos digitais (BR/UY/MX/Europa) |
| @nelmoricalde | creator | misto | baixo | IA + negócios — fundador Zuvora |
| @rodrigotadewald | marketing | reels | baixo | ⚠️ é cientista de dados (Asimov Finance/Academy) — mismatch de categoria |
| @sujeitoprogramador | ia | reels | alto | "IA dentro do seu VSCode" — 168K seguidores |
| @jonathan_kamargo | creator | misto | baixo | ⚠️ handle não resolvido |
| @marianatorre.s | marketing | misto | baixo | Conta confirmada, sem conteúdo indexado |
| @marketerhub.ai | marketing | misto | baixo | Comunidade paga de marketing com IA |
| @marcelaluzzio | marketing | reels | alto | "Marketing de Conteúdo & I.A" — MBA USP, 226K seguidores |
| @gestordeaudiencia | marketing | misto | baixo | ⚠️ handle não confirmado (dado contaminado) |
| @sebintel | ia | reels | baixo | Existe em 3 plataformas, sem conteúdo indexado |
| @avora.ai | agencia | misto | baixo | "Conteúdos diários sobre IA na prática" (marca ambígua) |
| @ogabrieeldias | creator | misto | baixo | "SaaS Founder" — mismatch de categoria (é founder) |
| @rodrigobindes | founder | reels | alto | "Dono de agência, quer espantar seus clientes? Faça isto" |
| @franklim.gui | creator | misto | médio | Storytelling low-ticket + Claude Code |
| @gabrielsamp.ai | ia | misto | baixo | ⚠️ Instagram não encontrado (só TikTok) |
| @maestrosdaia | ia | reels | médio | "Junte-se à Comunidade Maestros da IA" |
| @brandsdecoded__ | marketing | carrossel | alto | "Esse carrossel foi feito no Claude." — Content Machine 3.0 |
| @anatex | creator | reels | alto | "Coloque a IA para trabalhar no seu negócio" — 708K seguidores |
| @larissagomes.ia | ia | reels | baixo | "Peça o chatGPT para analisar o feed do seu Instagram" |
| @thiagozaao | creator | misto | baixo | ⚠️ handle não encontrado |
| @neuwebstudio | agencia | reels | médio | "Cinematic Web Design" — animações Figma/Webflow |
| @laschuk | founder | misto | médio | ⚠️ email marketing/ActiveCampaign — mismatch de categoria |
| @maestroptompts | ia | misto | baixo | ⚠️ handle não resolvido |
| @faladantasmkt | marketing | misto | alto | "Living & Selling +10k clients" — mentoria de vendas |
| @lindsay.ia | ia | misto | baixo | ⚠️ handle não resolvido |
| @andrevictor.m | marketing | reels | alto | "Fiz meu Primeiro Milhão aos 18 anos" — dropshipping |
| @drisiano | creator | misto | baixo | ⚠️ handle não resolvido |
| @brun0gpt | ia | misto | alto | "Bruno Francisco \| IA e Marketing" — 157K seguidores |
| @maxcarrau.ia | ia | misto | baixo | ⚠️ handle não resolvido |
| @noevarner | creator | misto | baixo | ⚠️ ambíguo (3 contas distintas possíveis) |
| @yikchanltd | creator | reels | alto | "8 Figure eCom Expert & A.I. Coach" — possível dup de @yikC |

---

## Análise Detalhada por Perfil

### @charliehills — creator
**Hook:** bio "I help you (actually) use AI" (outro / baixa freq.)
**Estrutura:** dados insuficientes.
**CTA:** prompts/ferramentas grátis via link na bio; contato `collabs@charliehills.ai`.
**Tom:** direto, didático, descontraído, prático — "I help you (actually) use AI".
**Formato dominante:** misto · **Engajamento:** alto (~88K seguidores).
**Temas:** IA prática, prompts de IA, ferramentas de IA.
**Limitação:** Instagram bloqueado; nenhuma legenda de post individual indexada, apenas bio.

### @yikC — creator
**Limitação:** ⚠️ Nenhuma conta correspondente a "yikC" foi localizada via WebSearch (nem `site:instagram.com`). Só apareceram contas não relacionadas (YWCA Kids Club, Yik Café, Yik Yak app). Possível handle inexistente, privado ou não indexado — **recomenda-se verificar manualmente no app e corrigir/remover em `config/profiles.json`**. Nota: pode ser a mesma pessoa de @yikchanltd (ver perfil #61) — checar antes de tratar como perfis distintos.

### @eujoaotorresz — creator
**Limitação:** ⚠️ Handle exato não aparece em nenhum resultado. A variante mais próxima indexada é @joaotorresz (perfil pequeno, ~2K seguidores, ligado a projetos em Portugal) — provavelmente pessoa diferente da esperada como "creator" do nicho. Nenhum conteúdo real encontrado.

### @fabianocarvalhojr — founder
**Hook:** bio "Founder lasy.ai — Crio Agentes de IA que vendem e operam Negócios 24/7 — Te Ensino na Aula Grátis".
**CTA:** convite para aula gratuita sobre agentes de IA.
**Tom:** empreendedor, didático, comercial, aspiracional.
**Formato:** misto · **Engajamento:** alto (~130K seguidores, 1.417 posts).
**Temas:** agentes de IA, automação de negócios, aula gratuita.
**Limitação:** perfil confirmado real/ativo; nenhuma legenda de post específica indexada além da bio.

### @rafa.grandi — marketing
**Limitação:** ⚠️ Conta real localizada (Rafael Grandi Borges, ~247 seguidores, 36 posts), mas a bio identifica um **Analista Jurídico do SPGG/RS**, não um perfil de marketing — **mismatch de handle/categoria**. Nenhum conteúdo de marketing encontrado. Recomenda-se revisar este perfil em `config/profiles.json`.

### @brusantanna.ai — ia
**Hook:** (transformação silenciosa) "Analisei meu próprio conteúdo com duas IAs e descobri exatamente por que alguns vídeos viralizavam... Agora são 300 seguidores novos por dia" (cross-post TikTok, mesmo handle).
**CTA:** "Comenta CLAUDE aqui que eu te mando o guia completo".
**Tom:** casual, didático, confiante, acessível.
**Formato:** misto · **Engajamento:** médio.
**Temas:** estratégia de IA para conteúdo, análise de vídeos, crescimento de seguidores.
**Limitação:** exemplo de legenda vem de cross-post no TikTok, não confirmado como publicado idêntico no Instagram; sem contagem de seguidores do IG.

### @vendedorglobal — negocio-digital
**Estrutura:** reels dominante, tema e-commerce/IA.
**CTA:** direcionamento a treinamento/site vendedorglobal.com.br.
**Tom:** motivacional, direto, comercial, didático.
**Formato:** reels · **Engajamento:** alto (Murilo Bevervanso, ~83–100K seguidores, +50K alunos).
**Temas:** e-commerce/marketplace, IA aplicada a vendas, AI influencer/deepfake.
**Limitação:** nenhuma legenda/hook literal capturada, apenas bio e menções de terceiros.

### @oluizmain — creator
**CTA:** divulgação do treinamento "Mobile Pro".
**Tom:** didático, profissional, técnico.
**Formato:** reels · **Engajamento:** baixo.
**Temas:** produção de vídeo mobile, treinamento Mobile Pro, redes sociais para negócios.
**Limitação:** nenhum número de seguidores nem legenda de post encontrado; apenas descrição de bio/site (luizmain.com).

### @nick_saraev — automacao
**CTA:** inscrição na Maker School, garantia "get your first client in 90 days or money back".
**Tom:** confiante, direto, orientado a resultados, comercial.
**Formato:** reels · **Engajamento:** alto.
**Temas:** automação com IA (n8n/Make), agência de automação, conseguir o 1º cliente.
**Limitação:** ⚠️ ambiguidade entre @nick_saraev e @nick.saraev nos resultados (mesma pessoa, handles parecidos) — verificar qual é o canônico com ~550K seguidores citado.

### @nathanhodgson — ia
**Hook:** bio "Built a 6-Figure Business Powered By AI • Trusted by Google · Meta · OpenAI".
**Tom:** aspiracional, autoritativo, direto.
**Formato:** misto · **Engajamento:** alto.
**Temas:** negócio de 6 dígitos com IA, cases citando Google/Meta/OpenAI.
**Limitação:** ⚠️ o handle exato "nathanhodgson" não corresponde a conta ativa relevante (achado: conta com 0 posts, aviso de mudança de usuário). O perfil real e ativo parece ser **@nathanhodgson.ai** (~128K seguidores) — recomenda-se corrigir o handle em `config/profiles.json`.

### @ai — ia
**Limitação:** ⚠️ WebSearch não retornou nenhum resultado correspondente exatamente a "instagram.com/ai/". Não é a conta oficial @meta.ai da Meta (essa tem 4M seguidores). Não foi possível confirmar quem controla este handle hoje — **não deve ser tratado como concorrente de nicho de IA sem verificação manual direta no app**.

### @ana.gsoares — marketing
**Hook:** fragmento real de legenda sobre "prompt de IA para encontrar vagas, mesmo..." (texto completo não acessível).
**Tom:** aspiracional, prático, empreendedor, direto.
**Formato:** misto · **Engajamento:** médio (Ana G Soares, CEO @uniagiloficial, host @agilizesepodcast, ~146K seguidores).
**Temas:** prompts de IA para currículo/vagas, liberdade financeira/geográfica, negócios digitais.
**Limitação:** apenas um fragmento de legenda real localizado; nenhum hook completo, CTA ou estrutura identificável.

### @chase.h.ai — ia
**CTA:** bio real "🤖 | Making AI Simple ⚡️ | DM 'Ready' to Apply For 1:1 Mentorship 🚀 | Master Claude Code".
**Tom:** direto, energético, simplificador, motivacional.
**Formato:** reels · **Engajamento:** alto (~221–228K seguidores, 751 posts).
**Temas:** ferramentas de IA no-code, Claude Code, mentoria 1:1.
**Limitação:** bio real capturada integralmente; nenhum hook/legenda de post específico localizado.

### @leosoares.ia — ia
**Tom:** pragmático, resultados-orientado, direto, empresarial.
**Formato:** misto · **Engajamento:** alto (Léo Soares, CEO Acelera IA, ~219K seguidores, 2.226 posts).
**Temas:** IA para negócios, lançamentos digitais, infoprodutos.
**Limitação:** posicionamento geral confirmado por múltiplas fontes (LinkedIn, YouTube), mas nenhuma legenda, hook ou CTA literal de post localizado.

### @gabriel.adamuchi — creator
**Hook:** prompt real compartilhado (via Threads) — "Ultra-realistic humorous Christmas scene of [INSERT MY FACE REFERENCE]...".
**Estrutura:** compartilhamento de prompts de imagem/IA prontos para copiar.
**Tom:** acessível, didático, descontraído, criativo.
**Formato:** reels · **Engajamento:** baixo.
**Temas:** prompts de imagem com IA, "IA Fácil — aprender e ganhar com IA".
**Limitação:** nenhum número de seguidores localizado; exemplo de prompt veio de repost no Threads.

### @viverdeia.ai — ia
**Hook:** tagline real da bio — "A Plataforma das Empresas que Crescem com IA".
**Tom:** corporativo, aspiracional, tecnológico, direto.
**Formato:** misto · **Engajamento:** médio ("Viver de IA", ~129K seguidores, fundado por Rafael Milagre, +2.000 empresas aceleradas).
**Temas:** automação de empresas com IA, aceleração de negócios "Plug & Play".
**Limitação:** tagline real capturada; nenhuma legenda/hook/CTA de post específico localizado.

### @ninja.automacoes — automacao
**Tom:** vendedor, direto, promocional, técnico.
**Formato:** misto · **Engajamento:** baixo.
**Temas:** automação de Instagram, IA para negócios, curso "Ninja Academy" (Hotmart, associado a Matheus Pessoa).
**Limitação:** nenhum número de seguidores, legenda ou hook localizado — sinal de baixa indexação pública.

### @nikolassasso — creator
**Hook:** bio real — "Criei robôs que fazem o trabalho duro por mim".
**Tom:** irreverente, aspiracional, direto, confiante.
**Formato:** misto · **Engajamento:** médio (~185K seguidores, 1.469 posts, +50.000 alunos desde 2017).
**Temas:** automação de vendas, robôs/agentes de IA, marketing digital.
**Limitação:** frase de bio real capturada; nenhuma legenda de post/reel específica localizada.

### @eduardocavalcanti — founder
**Hook:** bio real — "Maestro de Hiperagentes" / "Presidente IBIA".
**Tom:** institucional, autoritativo, técnico, aspiracional.
**Formato:** misto · **Engajamento:** médio (~184K seguidores).
**Temas:** hiperagentes de IA, IBIA, agentes autônomos.
**Limitação:** existem múltiplos "Eduardo Cavalcanti" no Brasil — confirmado que este perfil é distinto de outros homônimos, mas nenhuma legenda de post além da bio foi localizada.

### @jonylan — creator
**Hook:** bio aproximada — "Artificial Intelligence Ninja of the internet since 1994".
**Tom:** bem-humorado, experiente, direto, confiante.
**Formato:** reels · **Engajamento:** alto (Jony Lan, ~306K seguidores, 3.255 posts, "Builder" no programa Google Brasil).
**Temas:** marketing digital com IA, vendas, palestras/consultoria.
**Limitação:** nenhuma legenda de reel específica acessível, apenas resumo de bio.

### @allesinisgalli — founder
**Tom:** educativo, comunitário, tech-focado — bio "AI & MARKETING — IA CLUB COMUNIDADE".
**Formato:** misto · **Engajamento:** baixo.
**Limitação:** contagens de seguidores conflitantes entre fontes (8.155 vs. 61,3K de agregador) — possivelmente medindo perfis diferentes. Nenhuma caption, hook ou post específico encontrado.

### @lonamkt — marketing
**Hook:** "Primeiro milhão aos 18" (freq. média).
**Estrutura:** não identificável a partir dos 2 posts indexados no IG; títulos do YouTube do mesmo criador (Felipe Lona) sugerem storytelling de resultados financeiros.
**Tom:** ambicioso, direto, resultados-orientado.
**Formato:** misto · **Engajamento:** baixo (apenas 2 posts públicos indexados, 4.316 seguidores).
**Limitação:** maior parte do conteúdo temático vem do YouTube do mesmo criador, não confirmado como replicado no IG.

### @gabrielbarbosa.oficial — creator
**Hook:** bio real — "+10MM faturados na internet 🌎 Te ensino a ter uma operação enxuta e lucrativa de qualquer lugar do mundo".
**Tom:** aspiracional, direto, autoridade.
**Formato:** misto · **Engajamento:** baixo (7.782 seguidores, 47 posts).
**Limitação:** apenas bio e contagens identificadas; sem captions de posts específicas.

### @opensession.co — agencia
**Hook:** bio real — "✱ Brand x UX/AI x Design Systems — We help designers and brands level up their creativity."
**Tom:** criativo, profissional, minimalista, tech-orientado.
**Formato:** misto · **Engajamento:** médio (23K seguidores, 19 posts — agência de design em San Diego).
**Limitação:** apenas bio e contagem de seguidores; sem captions de posts específicas.

### @leandroladeiran — marketing
**Hook:** paráfrase de conteúdo indexado — "Copywriting não é escrever bonito, é escrever com intenção e estratégia para gerar uma ação específica".
**Estrutura:** conteúdo educativo com pattern-interrupt inicial, explicação de conceito (ex. ROI vs ROAS), CTA para vídeo completo/material grátis.
**CTA:** "Assista ao vídeo completo"; link no Linktree para curso grátis/mentoria/podcast.
**Tom:** didático, direto, estratégico, descontraído.
**Formato:** reels · **Engajamento:** alto.
**Temas:** copywriting, tráfego pago, ROI vs ROAS, stories/engajamento.
**Limitação:** audiência agregada (~4,32M) soma IG+YouTube+TikTok (estimativa de terceiros), não isolada para o IG; vários exemplos vêm do TikTok do mesmo criador.

### @christiantriad — creator
**Hook:** título real de post (truncado) — "📈 Importância dos Ganchos nos Reels do...".
**Estrutura:** conteúdo educativo sobre IA/tech/produtividade, incluindo posts meta sobre técnica de ganchos, alinhado ao método "Tríade do Tempo" (Christian Barbosa).
**Tom:** educativo, autoridade, tech-focado, direto.
**Formato:** reels · **Engajamento:** alto (571K seguidores).
**Limitação:** conteúdo completo do post sobre ganchos não foi acessível, apenas o título truncado.

### @oneyaraujo — creator
**Hook:** "Código Viral" (fenômeno nomeado, freq. alta) + estrutura ensinada em 4 partes: Gancho → Benefício → Mostre → CTA (freq. média).
**CTA:** link na bio para curso "Código Viral"; variações "Comenta seu nicho que te dou um help", "Salve esse vídeo para consultar depois".
**Tom:** didático, vendedor, direto, engajador.
**Formato:** reels · **Engajamento:** alto (~2M seguidores segundo estimativa de terceiros, 1.289 posts).
**Temas:** como viralizar Reels, estrutura de roteiro, curso Código Viral, algoritmo do Instagram.
**Limitação:** dados relativamente robustos, mas contagem de seguidores vem de fonte de análise de terceiros, não confirmada diretamente no IG. **Perfil com maior qualidade de dados do lote.**

### @geracaotechs — ia
**Hook:** "🎮 Esse site te permite criar jogos só descrevendo sua ideia...".
**Estrutura:** posts curtos de "descoberta de ferramenta" de IA.
**Tom:** curioso, acessível, entusiasta de tech, direto.
**Formato:** misto · **Engajamento:** baixo.
**Limitação:** busca não confirmou seguidores/posts especificamente para o IG; dados vêm do Threads espelhado do mesmo criador (Glauton Filho, 11,2K seguidores lá).

### @amandadinizmkt — marketing
**Limitação:** conta confirmada existir (título indexado "Marketing & Empreendedorismo") e perfil correspondente no TikTok, mas nenhum dado de seguidores, posts, captions ou hooks encontrado.

### @human___academy — ia
**Hook:** bio real — "A Maior Escola de IA para Criativos".
**Estrutura:** site institucional (humanacademy.ai) indica módulos práticos de imagem/vídeo com IA e workshops (AI Videolab).
**Tom:** aspiracional, educativo, criativo, tech-forward.
**Formato:** misto · **Engajamento:** alto (~260K seguidores).
**Limitação:** nenhuma caption de post individual ou hook específico encontrado.

### @geiss11 — creator
**Tom:** comercial, internacional.
**Formato:** reels · **Engajamento:** médio (Henrique Geiss, ~45K seguidores, 83 posts).
**Temas:** venda de produtos digitais para múltiplos países (BR, Uruguai, México, Europa).
**Limitação:** nenhuma legenda, gancho ou CTA real encontrado, apenas metadados de bio.

### @nelmoricalde — creator
**Tom:** estratégico, técnico, empresarial.
**Formato:** misto · **Engajamento:** baixo.
**Temas:** IA aplicada a negócios, automação de processos, comunidade "A Nova Inteligência" (fundador da Zuvora, ex-Citibank/BankBoston).
**Limitação:** nenhuma contagem de seguidores, legenda ou CTA real — dados só de resumos de busca/LinkedIn.

### @rodrigotadewald — marketing
**Limitação:** ⚠️ **mismatch de categoria** — resolve a Rodrigo Soares Tadewald, cientista de dados, cofundador da Asimov Finance/Academy — perfil pessoal de educação em IA/finanças quantitativas, não um perfil de "marketing". Reels sobre IA encontrados pertencem à conta de marca separada @asimov.academy, não confirmadamente ao perfil pessoal. Recomenda-se revisar categoria/handle em `config/profiles.json`.

### @sujeitoprogramador — ia
**Hook:** título real de reel (truncado) — "IA dentro do seu VsCode para ajudar na...".
**Tom:** educativo, técnico, didático.
**Formato:** reels · **Engajamento:** alto (Matheus Fraga, 168K seguidores, 3.040 posts, +45 mil alunos).
**Temas:** IA aplicada à produtividade em programação, cursos de dev web/mobile, React Native/Next.js.
**Limitação:** título de reel truncado; sem acesso ao conteúdo completo ou engajamento por post.

### @jonathan_kamargo — creator
**Limitação:** ⚠️ **Handle não resolvido.** Múltiplas buscas não retornaram nenhuma referência à conta específica; só contas semelhantes mas distintas apareceram (@camargojay, @kamargo___, etc.). Não é possível confirmar existência/atividade — recomenda-se verificar/corrigir em `config/profiles.json`.

### @marianatorre.s — marketing
**Limitação:** conta/pessoa real confirmada (existe também no TikTok com handle idêntico), mas nenhuma legenda, tema, contagem de seguidores ou info de conteúdo encontrada — resultados retornaram principalmente outras "Mariana Torres" não relacionadas.

### @marketerhub.ai — marketing
**Tom:** prático, educativo, comunitário.
**Formato:** misto · **Engajamento:** baixo.
**Temas:** páginas temáticas de IA que viralizam, comunidade de marketers usando IA (ligado ao site marketerhub.ai, comunidade paga).
**Limitação:** nenhuma legenda real, contagem de seguidores ou CTA de post encontrada, apenas descrição institucional.

### @marcelaluzzio — marketing
**Hook:** título de reel real (truncado) — "REELS EM...".
**Tom:** estratégico, educativo, tecnológico.
**Formato:** reels · **Engajamento:** alto (Marcela Lúzio, 226K seguidores, MBA em IA para negócios digitais pela USP).
**Temas:** infoprodutos criados/vendidos com IA, marketing de conteúdo.
**Limitação:** título de reel truncado; sem legendas completas, CTAs ou estrutura de vídeo.

### @gestordeaudiencia — marketing
**Limitação:** ⚠️ **Handle não resolvido / dado potencialmente contaminado.** Nenhuma confirmação independente de que é uma conta real e ativa; as únicas menções vêm de um documento do Scribd sobre "Remotion com Claude Code" citando o handle como exemplo dentro de uma galeria de prompts — não é evidência de conteúdo real do perfil. Recomenda-se verificar manualmente.

### @sebintel — ia
**Formato:** reels · **Engajamento:** baixo.
**Limitação:** nome "Seb Intel" confirmado em 3 plataformas (IG, Facebook, TikTok) com o mesmo handle e uma página de reels indexada, mas nenhuma legenda, bio completa, contagem de seguidores ou confirmação de que o conteúdo é sobre IA (apesar da categoria) foi encontrada.

### @avora.ai — agencia
**Hook:** "Siga @avora.ai para conteúdos diários sobre IA na prática!".
**Tom:** prático, aplicado, direto.
**Formato:** misto · **Engajamento:** baixo.
**Limitação:** ambiguidade de marca no espaço — existe também @avora_br_ (mesmo nome de marca) e empresas não relacionadas ("getavora.ai" SaaS de odontologia, "Aivora AI"); sem contagem de seguidores/posts confirmada.

### @ogabrieeldias — creator
**Limitação:** ⚠️ **mismatch de categoria** — título indexado do perfil é "Gabriel Dias | SaaS Founder", alinhando-se melhor com a categoria "founder" do que "creator". Handle existe e é ativo, mas sem seguidores, bio completa, legendas ou exemplos de conteúdo encontrados.

### @rodrigobindes — founder
**Hook:** título real de reel — "Dono de agência, quer espantar os seus clientes? Faça isto" (paradoxo/contraste, freq. média).
**Tom:** direto, provocador, assertivo, orientado a resultados.
**Formato:** reels · **Engajamento:** alto (278K seguidores, 1.835 posts; cofundador da Ultralize com Erico Rocha, Leandro Ladeira e Guilherme Cardoso).
**Temas:** gestão de agências de marketing digital, aquisição/retenção de clientes, erros comuns de donos de agência.
**Limitação:** estrutura/CTA são inferências limitadas a um único exemplo de título de reel encontrado.

### @franklim.gui — creator
**Hook:** título real (via YouTube do mesmo criador) — "por que eu decidi sair do brasil pra viver de lowticket?".
**Tom:** informal, descontraído, direto, pessoal.
**Formato:** misto · **Engajamento:** médio (~51K seguidores, 180 posts).
**Temas:** IA aplicada a negócios (Claude Code), tráfego direto/low-ticket, storytelling pessoal.
**Limitação:** exemplo de hook vem do YouTube do mesmo criador, não confirmado como legenda idêntica no IG. ⚠️ Existe perfil homônimo diferente (@guifranklim, ~1,9K seguidores, Marketing/Direito Penal) — não confundir.

### @gabrielsamp.ai — ia
**Limitação:** ⚠️ **Perfil do Instagram não encontrado.** Existe conta de TikTok com o mesmo handle exato, sugerindo que a marca/pessoa existe, mas o Instagram correspondente não foi localizado (pode ser muito pequeno/não indexado/inativo/inexistente).

### @maestrosdaia — ia
**CTA:** "Junte-se à Comunidade Maestros da IA".
**Tom:** institucional, aspiracional, comunitário.
**Formato:** reels · **Engajamento:** médio (dados inferidos da conta-irmã no TikTok, 71,4K seguidores lá — tratar contagem com cautela).
**Temas:** agentes de IA autônomos, bots de WhatsApp, automação de produção de conteúdo.
**Limitação:** perfil do IG existe e é indexado, mas nenhuma legenda/hook real recuperável; métricas vêm do TikTok da mesma marca.

### @brandsdecoded__ — marketing
**Hook:** legenda real — "Esse carrossel foi feito no Claude." (freq. média).
**Estrutura:** demonstração de processo "behind the scenes" creditando a ferramenta de IA usada, reforçando o produto pago.
**Tom:** técnico, estratégico, confiante, orientado a dados.
**Formato:** carrossel · **Engajamento:** alto (Leonardo Varrichio, fontes divergem entre ~250K e 306K seguidores; produto "Content Machine 3.0" via Hotmart, calibrado com 1.700 posts analisados em 25+ nichos).
**Temas:** criação de carrosséis com IA/Claude, estratégia de conteúdo, cultura e branding.
**Limitação:** texto completo do post não acessível; número exato de seguidores diverge entre fontes.

### @anatex — creator
**Hook:** trecho de hook real (cortado no snippet) — "Você tem anos ..." (classificação de modelo é inferência de baixa confiança).
**Tom:** institucional, corporativo, propositivo, direto — "Coloque a IA para trabalhar no seu negócio: ganhe tempo, reduza custos e crie novas oportunidades de receita nessa nova era".
**Formato:** reels · **Engajamento:** alto (708K seguidores, 1.424 posts — "Ana Tex - Inteligência Artificial para Negócios").
**Temas:** IA aplicada a negócios, produtividade, redução de custos com automação.
**Limitação:** hook truncado no snippet de busca. ⚠️ Existem contas parecidas mas diferentes (@anatex_, @anatex_bysultan, @anatex.shop) — não confundir.

### @larissagomes.ia — ia
**Hook:** "Peça o chatGPT para analisar o feed do seu instagram" (freq. média).
**Estrutura:** tutorial/instrucional — hook imperativo → prompt pronto passo a passo → CTA de seguir/salvar.
**CTA:** "Salva pra lembrar"; variação "siga @larissagomes.ia".
**Tom:** acolhedor, didático, acessível, pessoal — "💻 Te ensino a criar um negócio enxuto e que vende: você + IA ⚡️".
**Tamanho médio educativo:** ~250 palavras.
**Formato:** reels · **Engajamento:** baixo (15K seguidores, 262 posts — menor volume confirmado do lote).
**Temas:** prompts de ChatGPT para negócios, crescimento no IG com IA, negócio enxuto com IA.
**Limitação:** legenda completa indexada a partir do TikTok espelhado da mesma criadora, não confirmada linha-a-linha como idêntica no IG.

### @thiagozaao — creator
**Limitação:** ⚠️ **Handle não encontrado** em nenhuma variação de busca testada. Forte indício de handle incorreto/digitado errado, conta privada não indexada, ou conta inexistente/desativada. Recomenda-se corrigir/remover em `config/profiles.json`.

### @neuwebstudio — agencia
**Estrutura:** vídeos demonstrando efeitos parallax/animações em Figma/Webflow, hashtags técnicas de design, promoção recorrente de produto pago de animações Figma.
**Tom:** cinematográfico, técnico, promocional, visual — "Cinematic Web Design".
**Formato:** reels · **Engajamento:** médio (52K seguidores IG, 168 posts; 172K no TikTok cruzado).
**Temas:** animação em Figma, web design parallax, efeitos cinematográficos.
**Limitação:** nenhuma legenda/hook completo de reel indexado, apenas bio e hashtags gerais.

### @laschuk — founder
**Limitação:** ⚠️ **mismatch de categoria** — posicionamento real é "email marketing"/ActiveCampaign (não um "founder" declarado de empresa própria). Membro do board internacional LATAM da ActiveCampaign, ~R$1.094.956,05 vendidos via email (prova social real).
**Tom:** técnico, direto, autoridade, comercial.
**Formato:** misto · **Engajamento:** médio (36K seguidores, 200 posts).
**Temas:** email marketing, ActiveCampaign, tráfego próprio.
**Limitação adicional:** existem várias outras contas "Laschuk" não relacionadas (sobrenome comum) — risco de confusão.

### @maestroptompts — ia
**Limitação:** ⚠️ **Handle não resolvido.** Só apareceram contas "Maestro" completamente não relacionadas (serviço de pagamento, rapper, PMS de hotel). Provável conta inexistente, privada, ou grafia diferente da real (possível erro de digitação no nome — "ptompts" vs. "prompts"?).

### @faladantasmkt — marketing
**Hook:** linha de bio — "14 years selling online → Sell your service, courses and mentorship every day attracting gold clients".
**Estrutura:** mentoria em marketing digital/vendas com prova social (14 anos de mercado, +10 mil clientes, marcas como Unilever, Tim, Gol, L'Oréal, Sephora, Coca-Cola).
**CTA:** chamada para mentoria/curso via link na bio ("start here").
**Tom:** autoridade, comercial, direto, aspiracional — "Living & Selling +10k clients | start here↓".
**Formato:** misto · **Engajamento:** alto (Jessica Dantas, ~99–108K seguidores).
**Limitação:** nenhum hook ou CTA de reel específico confirmado além da bio.

### @lindsay.ia — ia
**Limitação:** ⚠️ **Handle não resolvido.** Buscas repetidas só trouxeram contas "Lindsay" não relacionadas (fotógrafas, políticas dos EUA, atriz). Provável conta inexistente/não indexada ou grafia diferente.

### @andrevictor.m — marketing
**Hook:** "Fiz meu Primeiro Milhão aos 18 anos desse jeito" (paradoxo/contraste, freq. média).
**Estrutura:** flex/prova de resultado (Ferrari Portofino R$3M à vista, 50 países até os 22) combinado com conteúdo educativo de dropshipping.
**Tom:** aspiracional, ostentação, direto, jovem, comercial.
**Formato:** reels · **Engajamento:** alto (244K seguidores, 286 posts; presença também em TikTok/YouTube).
**Temas:** dropshipping, marketing digital, empreendedorismo, ostentação de resultados.
**Limitação:** captions completas de reels não indexadas; dados vêm de títulos de podcast/YouTube agregados.

### @drisiano — creator
**Limitação:** ⚠️ **Handle não resolvido.** Apenas handles parecidos e não relacionados apareceram (@drinomino, @driso__, @drisansone, @drisanasharma). Provável conta inexistente, privada não indexada, ou grafia diferente.

### @brun0gpt — ia
**Estrutura:** conteúdo educativo sobre uso de IA para marketing/vendas (prompts, automação); estrutura específica dos reels não confirmada.
**Tom:** técnico, comercial — "Bruno Francisco | IA e Marketing".
**Formato:** misto · **Engajamento:** alto (157K seguidores, 1.334 posts).
**Temas:** marketing com IA, vendas com IA, automação.
**Limitação:** nenhuma legenda, hook ou CTA real de reel específico encontrado, apenas descrição agregada do perfil.

### @maxcarrau.ia — ia
**Limitação:** ⚠️ **Handle não resolvido.** Resultado mais próximo tematicamente (@iawithmax, conta francesa de produtividade com IA) é pessoa/conta diferente. Existe canal do YouTube "Max carrau | IA", mas sem link confirmado a uma conta de Instagram ativa com esse handle exato.

### @noevarner — creator
**Limitação:** ⚠️ **Handle ambíguo.** O handle exato @noevarner tem um post indexado ("That time I won at the Arnold's") mas nenhuma métrica/bio encontrada para essa conta específica. Existem contas semelhantes mas **distintas**: @noevarner.ai (91.740 seguidores, foco em "AI systems for content, ads, and growth") e @therealnoevarner (7.123 seguidores, criadores esportivos/treinadores). Sem acesso direto ao IG, não é possível confirmar com segurança qual conta é a monitorada — **recomenda-se verificação manual e correção do handle em `config/profiles.json`**.

### @yikchanltd — creator
**Hook:** formato recomendado pelo próprio Sifu Yik Chan em seu Substack — "[Número] [Período de tempo] e ainda [problema comum]" (maioria errando, freq. baixa).
**Estrutura:** mentoria em eCommerce e IA, prova de autoridade (menções em Yahoo Finance/Forbes), promoção de grupo pago de renda passiva.
**CTA:** DM de palavra-chave para grupo/oferta (ex.: DM "Ai" para grupo de renda passiva de $10k/mês).
**Tom:** autoridade, comercial, direto, aspiracional — "8 Figure eCom Expert & A.I. Coach".
**Formato:** reels · **Engajamento:** alto (79K seguidores, 1.296 posts).
**Limitação:** ⚠️ **possível duplicidade com @yikC** (perfil #2 desta lista) — não foi possível confirmar essa relação via busca; recomenda-se checagem manual para evitar contar a mesma pessoa duas vezes no monitor.

---

## Perfis Sugeridos pelo Sistema

Não aplicável nesta execução — `config/profiles.json` já continha 61 perfis ativos, então o Módulo 2 rodou direto em **Modo Análise** (Passo 2), sem passar pelo Modo Descoberta.

---

## Perfis com Problema de Resolução — ação recomendada em `config/profiles.json`

| Handle | Problema | Ação sugerida |
|--------|----------|----------------|
| @yikC | Não resolve; possível duplicata de @yikchanltd | Verificar manualmente no app; remover ou consolidar com @yikchanltd |
| @eujoaotorresz | Não resolve à pessoa esperada | Verificar/corrigir handle |
| @rafa.grandi | Resolve, mas é analista jurídico (pessoa errada) | Corrigir handle ou remover |
| @nathanhodgson | Handle real provavelmente é `nathanhodgson.ai` | Corrigir handle |
| @ai | Não identificável/verificável | Remover — genérico demais para monitorar |
| @jonathan_kamargo | Não resolve | Verificar/corrigir handle |
| @gestordeaudiencia | Não confirmado; dado de origem duvidosa (Scribd) | Verificar manualmente |
| @rodrigotadewald | É cientista de dados (Asimov), não perfil de marketing | Revisar categoria ou substituir |
| @ogabrieeldias | É "SaaS Founder", categoria "creator" não bate | Mudar categoria para founder |
| @gabrielsamp.ai | Instagram não encontrado (só TikTok existe) | Verificar/remover do IG, manter só se monitorar TikTok |
| @thiagozaao | Não encontrado em nenhuma variação | Verificar/corrigir handle |
| @laschuk | É especialista em email marketing, não "founder" declarado | Revisar categoria |
| @maestroptompts | Não resolve (possível erro de digitação: "prompts"?) | Corrigir handle |
| @lindsay.ia | Não resolve | Verificar/corrigir handle |
| @drisiano | Não resolve | Verificar/corrigir handle |
| @maxcarrau.ia | Não resolve | Verificar/corrigir handle |
| @noevarner | Ambíguo entre 3 contas distintas (@noevarner, @noevarner.ai, @therealnoevarner) | Verificar manualmente qual é a intenção e corrigir handle |
| @yikchanltd | Possível duplicata de @yikC | Verificar manualmente para evitar contagem dupla |

**13 perfis não resolveram para nenhuma conta real/ativa/identificável**, 5 resolveram mas para a pessoa/categoria errada, e 2 pares são possíveis duplicatas — no total, **~30% dos 61 perfis ativos têm algum problema de configuração** que vale revisar antes da próxima execução do monitor.

---

## Limitações de Dados (resumo geral)

- **WebFetch em instagram.com bloqueado pelo proxy de rede em 100% das tentativas** (61/61 perfis) — nenhum dado veio de scraping direto da página; tudo é WebSearch (snippets/caches de terceiros).
- Isso significa que, para a maioria dos perfis, **não foi possível confirmar legendas completas, CTAs literais, estrutura exata de conteúdo ou taxas de engajamento reais** — apenas bio, posicionamento geral e (quando disponível) contagem de seguidores de fontes agregadoras (Social Blade, Hafi.pro) ou cross-posts em TikTok/YouTube do mesmo criador.
- Perfis com **maior qualidade de dados** (hook, estrutura e CTA reais e específicos): @oneyaraujo, @brandsdecoded__, @larissagomes.ia, @leandroladeiran, @rodrigobindes, @andrevictor.m.
- Perfis com **dados praticamente nulos** além da confirmação de existência: @amandadinizmkt, @marianatorre.s, @sebintel, @allesinisgalli, @lonamkt, @nelmoricalde, @geracaotechs, @avora.ai.
- Nenhum dado de engajamento específico por post foi inventado — os campos `engajamento_estimado` refletem apenas sinal indireto (contagem de seguidores relatada por terceiros), nunca uma métrica medida diretamente.
