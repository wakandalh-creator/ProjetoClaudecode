# Análise de Perfis Instagram — 2026-10-19

## ⚠️ Limitação estrutural identificada nesta execução

Execução automatizada via rotina agendada "Monitor Instagram - Módulo 2 semanal", seguindo a instrução de ir direto ao **Passo 2 (Modo Análise)** e usar **WebSearch + WebFetch** para coletar dados dos **61 perfis ativos** em `config/profiles.json`. O trabalho foi distribuído em 5 lotes sequenciais de ~12 perfis cada (via Agent/WebSearch), cobrindo os 61 perfis ativos, com no mínimo 2-3 buscas por handle, sem inventar dados.

**Confirmado novamente nesta execução:** `www.instagram.com` continua **bloqueado a nível de rede** pelo proxy de egress deste ambiente (`getaddrinfo ENOTFOUND www.instagram.com` em todas as tentativas diretas de WebFetch). Tentativas de WebFetch em agregadores de terceiros (creatordb.app) também falharam por DNS. **Todos os dados abaixo vêm exclusivamente de snippets do Google indexados via WebSearch** — nunca de leitura direta da página de origem.

**Resultado:** dos 61 perfis ativos, **nenhum** teve um post real (legenda, hook, CTA, exemplo de tom de voz) localizado — os campos `hook_modelos`, `estrutura_tipica`, `cta_padrao`, `tom_adjetivos` e `top_posts_temas` ficam em `limitacao_dados` para os 61/61 perfis. **11 perfis (18%)** tiveram algum dado agregado recuperado (bio, seguidores, nicho/posicionamento) — 5 via snippet do Google indexando a própria página do Instagram (mais confiável, mas ainda não confirmado em tempo real) e 6 via agregadores de terceiros (creatordb.app, não confirmados). Os demais **50 perfis (82%)**, não retornaram nenhum dado específico e verificável; buscas retornaram apenas conteúdo genérico ou perfis homônimos claramente distintos, descartados para evitar dado inventado.

**Recomendação para o Lucas (mantida de execuções anteriores):** os campos de extração profunda deste módulo (hook_modelos, cta_padrao, tom_exemplo_frase, top_posts_temas) dependem de acesso real aos posts do Instagram. Com o bloqueio de rede atual, isso só é viável por: (a) liberar `instagram.com` no proxy de egress deste ambiente, (b) usar a skill `instagram-content-cloner` a partir de uma sessão/ambiente com acesso ao Instagram, ou (c) importar dados manualmente (export/scraping feito fora deste ambiente). Sem isso, este módulo continuará retornando majoritariamente `limitacao_dados` nas próximas execuções agendadas.

---

## Visão Geral dos Perfis (com algum dado recuperável — não confirmado em tempo real)

| Perfil | Categoria | Formato Dominante | Engajamento | Fonte / Confiabilidade |
|--------|-----------|-------------------|-------------|------------------------|
| @christiantriad | creator | indefinido | indefinido (seguidores conflitantes entre snippets: ~571K vs ~304K) | Snippet Google de instagram.com (cache da própria bio) |
| @oneyaraujo | creator | reels (inferência pelo produto de curso) | indefinido (seguidores conflitantes: ~1,3M vs ~2M) | Snippet Google de instagram.com + reportei.com |
| @human___academy | ia | indefinido | indefinido (~260K seguidores, snippet com ~680 dias, pode estar desatualizado) | Snippet Google de instagram.com |
| @geiss11 | creator | indefinido | indefinido (~45K seguidores) | Snippet Google de instagram.com |
| @sujeitoprogramador | ia | indefinido | indefinido (~165K seguidores, ~3.000 posts) | Snippet Google de instagram.com |
| @nick_saraev | automacao | indefinido (Reels sugerido, não confirmado) | indefinido (~693K seguidores, terceiro) | creatordb.app (agregador, snippet apenas) |
| @chase.h.ai | ia | indefinido (Reels/Stories sugerido) | indefinido (~236K seguidores) | creatordb.app (agregador, snippet apenas) |
| @nikolassasso | creator | indefinido | médio — 2,8% ER (~181K seguidores) | creatordb.app (agregador, snippet apenas) |
| @leandroladeiran | marketing | indefinido | alto — 3,1% ER (~2,31M seguidores, +39K/30d) | creatordb.app (agregador, snippet apenas) |
| @sebintel | ia | indefinido (Reels/Stories sugerido) | médio — 4,5% ER (~340K seguidores) | creatordb.app (agregador, snippet apenas) |
| @anatex | creator | indefinido | indefinido (~717K seguidores, sem ER confiável) | creatordb.app (agregador, snippet apenas) |

Os **50 perfis restantes** não retornaram nenhum dado específico verificável (ver seção "Limitações de Dados" abaixo) — todos marcados com `formato_dominante: indefinido`, `engajamento_estimado: indefinido` por ausência de dado real.

Nenhum dos 61 perfis teve hook, CTA, tom de voz ou tema de post real extraído — campo obrigatório `limitacao_dados` aplicado a 100% da amostra nesses campos.

---

## Análise Detalhada — Perfis com Dados Parciais

### @christiantriad
**Categoria:** creator | **Tags:** ia, negocio-digital
- **Bio/posicionamento:** conta confirmada (handle existe), de Christian Barbosa, posicionado em bio como foco em "IA, Tech & SaaS"; é o criador do método de gestão de tempo "A Tríade do Tempo" (urgente/importante/circunstancial), conhecido como "Senhor do Tempo" no mercado de produtividade BR. Fonte: snippet Google de instagram.com/christiantriad; contexto do método via blog.grancursosonline.com.br e getabstract.com.
- **Hook/estrutura/CTA/tom/top_posts_temas:** `limitacao_dados` — nenhuma frase de abertura, estrutura ou CTA real encontrada.
- **Formato dominante:** indefinido.
- **Engajamento estimado:** indefinido — seguidores conflitantes entre snippets (~571K vs ~304K, possível cache antigo).

### @oneyaraujo
**Categoria:** creator | **Tags:** negocio-digital, marketing
- **Bio/posicionamento:** conta confirmada (Oney Araújo). Bio via snippet: "Revelando Segredos de como Viralizar, Ganhar Seguidores e Vender Online", +62.000 alunos. Produto "Código Viral®" descrito por fonte terceira (reportei.com) com "19 padrões de viralização" e foco em formatos de Reels de alta tração.
- **Hook/estrutura/CTA/tom/top_posts_temas:** tema geral real (viralização/crescimento/monetização via Reels), mas nenhuma frase exata de post, CTA ou tom — `limitacao_dados` para esses campos específicos.
- **Formato dominante:** reels (inferência razoável pelo produto, não confirmação direta do feed).
- **Engajamento estimado:** indefinido — seguidores conflitantes entre fontes (~1,3M vs ~2M).

### @human___academy
**Categoria:** ia | **Tags:** ia, educacao, automacao
- **Bio/posicionamento:** handle confirmado via snippet de instagram.com: escola de IA para criativos, promovendo workshop "AI Videolab"; ~260K seguidores, 496 seguindo, 450 posts (snippet com ~680 dias, pode estar desatualizado). Contexto compatível (não 100% confirmado como mesma entidade): produtora BR "Human" mantém braço educacional "Human Academy", curso "AI Video Creator", CEO citado Nando Blum.
- **Hook/estrutura/CTA/tom/top_posts_temas:** `limitacao_dados`.
- **Formato dominante:** indefinido.
- **Engajamento estimado:** indefinido.

### @geiss11
**Categoria:** creator | **Tags:** negocio-digital
- **Bio/posicionamento:** handle confirmado via snippet, pertencente a Henrique Geiss. Bio: venda de produtos digitais ("sells digital products worldwide"). ~45K seguidores, 601 seguindo, 83 posts.
- **Hook/estrutura/CTA/tom/top_posts_temas:** `limitacao_dados`.
- **Formato dominante:** indefinido.
- **Engajamento estimado:** indefinido.

### @sujeitoprogramador
**Categoria:** ia | **Tags:** tech, ia, programacao
- **Bio/posicionamento:** handle confirmado via snippet, pertencente a Matheus Fraga. Bio: 12+ anos como programador, +45.000 alunos, cursos de programação + IA focados em colocação profissional. ~165K seguidores, ~3.000 posts.
- **Hook/estrutura/CTA/tom/top_posts_temas:** tema geral real (cursos de programação + IA), mas nenhum hook/estrutura/CTA real — `limitacao_dados`.
- **Formato dominante:** indefinido.
- **Engajamento estimado:** indefinido.

### @nick_saraev
**Categoria:** automacao | **Tags:** ia, automacao, agencia
- **Bio/posicionamento (dado de agregador terceiro, NÃO confirmado):** creatordb.app descreve Nick Saraev como criador canadense de educação em automação com IA (Make.com, n8n, Agentic Workflows, Claude Code), fundador da consultoria "LeftClick" e do programa "Maker School". ~693K seguidores no Instagram, ~531K no YouTube (dados conflitantes com outra fonte que citava >100K).
- **Hook/estrutura/CTA/tom/top_posts_temas:** `limitacao_dados`.
- **Formato dominante:** indefinido (Reels sugerido por terceiro, não confirmado).
- **Engajamento estimado:** indefinido.

### @chase.h.ai
**Categoria:** ia | **Tags:** ia, automacao
- **Bio/posicionamento (agregador terceiro, NÃO confirmado):** creatordb.app descreve criador/consultor de IA nos EUA, foco em educação de IA no-code; ~236K seguidores no Instagram, Reels/Stories citados como formatos usados.
- **Hook/estrutura/CTA/tom/top_posts_temas:** `limitacao_dados`.
- **Formato dominante:** indefinido.
- **Engajamento estimado:** indefinido.

### @nikolassasso
**Categoria:** creator | **Tags:** ia, negocio-digital
- **Bio/posicionamento (agregador terceiro, NÃO confirmado):** creatordb.app descreve educador BR de marketing digital/estratégia de negócio online desde 2017, com método de "venda automatizada" sem aparecer em vídeo (faceless). Possível sinal de inatividade: "último upload 7 meses atrás" segundo a mesma fonte.
- **Hook/estrutura/CTA/tom/top_posts_temas:** `limitacao_dados`.
- **Formato dominante:** indefinido.
- **Engajamento estimado:** médio — ~181.472 seguidores, 2,8% engagement (creatordb.app, não confirmado).

### @leandroladeiran
**Categoria:** marketing | **Tags:** marketing, growth, negocio-digital
- **Bio/posicionamento (agregador terceiro, NÃO confirmado):** creatordb.app descreve empreendedor digital BR na interseção entre educação de marketing digital e storytelling bem-humorado; YouTube como plataforma primária, TikTok secundário (~880K).
- **Hook/estrutura/CTA/tom/top_posts_temas:** `limitacao_dados` — apenas descrição agregada de estilo, nenhuma frase real.
- **Formato dominante:** indefinido (agregador cita ~11 posts/semana, sem especificar tipo).
- **Engajamento estimado:** alto — ~2.310.828 seguidores, 3,1% ER (vs. mediana de categoria 1,5%), +39K seguidores/30 dias (creatordb.app, não confirmado).

### @sebintel
**Categoria:** ia | **Tags:** ia, tech
- **Bio/posicionamento (agregador terceiro, NÃO confirmado):** creatordb.app descreve canal de educação em ferramentas de IA operado por "Sebastien Jefferies", foco em ensino prático de ferramentas de IA; parceria citada com Replit.
- **Hook/estrutura/CTA/tom/top_posts_temas:** `limitacao_dados`.
- **Formato dominante:** indefinido (Reels/Stories sugerido, não confirmado).
- **Engajamento estimado:** médio — ~340.751 seguidores, 4,5% ER, 11,4 posts/semana (creatordb.app, não confirmado).

### @anatex
**Categoria:** creator | **Tags:** negocio-digital
- **Bio/posicionamento (agregador terceiro, NÃO confirmado):** creatordb.app descreve educador(a) BR de IA para profissionais de negócios; ~717K seguidores, ~74% da audiência no Instagram (plataforma principal); tema de exemplo citado: tutoriais de geração de imagem com IA (estilo "Disney Pixar").
- **Hook/estrutura/CTA/tom/top_posts_temas:** tema geral citado (tutoriais de IA), mas sem legenda/hook/CTA real — `limitacao_dados`.
- **Formato dominante:** indefinido.
- **Engajamento estimado:** indefinido — agregador não forneceu taxa de engajamento confiável.

---

## Limitações de Dados — Perfis sem nenhum dado recuperado (50)

Todos os campos do schema (hook_modelos, estrutura_tipica, cta_padrao, tom_adjetivos, formato_dominante, engajamento_estimado, top_posts_temas) estão em `limitacao_dados` para os perfis abaixo. WebSearch não retornou nenhuma informação específica e confiável sobre o handle exato — apenas conteúdo genérico, ou perfis homônimos claramente diferentes (descartados para evitar dado inventado):

@charliehills, @yikC, @eujoaotorresz, @fabianocarvalhojr, @rafa.grandi, @brusantanna.ai, @vendedorglobal, @oluizmain, @nathanhodgson, @ai, @ana.gsoares, @leosoares.ia, @gabriel.adamuchi, @viverdeia.ai, @ninja.automacoes, @eduardocavalcanti, @jonylan, @allesinisgalli, @lonamkt, @gabrielbarbosa.oficial, @opensession.co, @geracaotechs, @amandadinizmkt, @nelmoricalde, @rodrigotadewald, @jonathan_kamargo, @marianatorre.s, @marketerhub.ai, @marcelaluzzio, @gestordeaudiencia, @avora.ai, @ogabrieeldias, @rodrigobindes, @franklim.gui, @gabrielsamp.ai, @maestrosdaia, @brandsdecoded__, @larissagomes.ia, @thiagozaao, @neuwebstudio, @laschuk, @maestroptompts, @faladantasmkt, @lindsay.ia, @andrevictor.m, @drisiano, @brun0gpt, @maxcarrau.ia, @noevarner, @yikchanltd

**Casos notáveis descartados por homonímia/ambiguidade** (resultado existia mas apontava claramente para pessoa/entidade diferente, ou achado não confirmável como o mesmo perfil):
- @charliehills — achado só liga a presença no LinkedIn ("Charlie Hills", estrategista britânico), sem confirmação de ser o mesmo @ do Instagram.
- @fabianocarvalhojr — vários "Fabiano/Fabrício/Fabio Carvalho" claramente distintos (atleta, acadêmico, designer).
- @rafa.grandi — perfis "Grandi" encontrados (dançarino em Roma, etc.) são pessoas diferentes.
- @brusantanna.ai — resultado principal é Bruna Santana, irmã do cantor Luan Santana (moda/celebridade), nada a ver com IA.
- @nathanhodgson — Hodgsons encontrados (jornalista britânica, jogador de rugby) são pessoas diferentes.
- @ana.gsoares — "Anas Soares" encontradas (médica, analista de marketing com métricas zeradas) são contas/pessoas diferentes.
- @eduardocavalcanti — resultados retornam o treinador de futebol "Dado Cavalcanti" e o cantor "@eduardocosta", sem relação confirmada.
- @allesinisgalli — único resultado próximo é o poeta italiano falecido Leonardo Sinisgalli, sem relação com o founder de SaaS monitorado.
- @gabrielbarbosa.oficial — resultados dominados pelo jogador de futebol "Gabigol" (Gabriel Barbosa), sem confirmação de que o handle monitorado seja dele.
- @geracaotechs — único resultado próximo (`geracaotech_celulares`) é loja de eletrônicos.
- @amandadinizmkt — contas semelhantes (`amandadinizz`, `amandadiniz13`) são perfis de lifestyle/fé, não de marketing.
- @nelmoricalde — resultado mais próximo é uma imobiliária (`nelio_ricalde`) no México.
- @jonathan_kamargo — resultados mais próximos são uma empresa espanhola (`kamargo___`) e uma menção tangencial, sem relação clara.
- @marianatorre.s — resultados são atriz e tatuadora com nomes parecidos, sem relação com marketing/IA.
- @marketerhub.ai — possível correspondência (`marketer_hub`, 87 seguidores) é pequena demais e com handle diferente (underscore vs. ".ai") para ser tratada como confirmada.
- @ogabrieeldias — resultados são modelos/atrizes (Gabrielle Diana, Gabriela Dias) sem relação com IA/negócio digital.
- @franklim.gui — homônimo parcial (@franklinathos, maquiador), nicho totalmente diferente.
- @gabrielsamp.ai — homônimos de nicho diferente (trading, estética).
- @larissagomes.ia — homônimos de moda/beleza, sem relação com IA/automação.
- @rodrigobindes — achado (artigo sobre um "Rodrigo Bindes", mentor de marketing para restaurantes/agências) não confirmado como o operador do handle monitorado; foco relatado não corresponde às tags (saas, growth).
- @laschuk — homônimos claros (educadora alemã-georgiana, cantora, outra criadora), sem ligação ao handle.
- @maestroptompts — produtos/perfis homônimos sem relação (app "Maestro" de prompts ChatGPT, perfis "Maestro Mayonais"/"Maestro Fresh Wes").
- @lindsay.ia — múltiplas "Lindsay" homônimas sem relação com IA/automação.
- @andrevictor.m — múltiplos "Victor" homônimos sem relação.
- @drisiano — único hit próximo é um rapper argelino homônimo ("Driski"), sem evidência de ligação.
- @brun0gpt — apenas projetos/produtos de terceiros com "gpt" no nome, sem relação com o handle.
- @noevarner — achado (@noyavner, grafia diferente, sem posts há 60+ dias) não confirmado como o mesmo perfil.
- @yikchanltd — homônimos (fotógrafo "Lee Yik Keat", canais/empresas distintas) sem relação.
- @jonylan — achado com grafia diferente (@jonilane_) não confirmado como o mesmo handle.
- @lonamkt — achado com nome parecido ("La Liga MKT" / "laligamkt") não confirmado como o mesmo handle.

**Observação comparativa com a execução de 2026-10-12:** desta vez 11 perfis retornaram algum dado parcial (vs. 6 na semana passada) — incluindo 5 handles confirmados diretamente via cache do Google de suas próprias páginas do Instagram (@christiantriad, @oneyaraujo, @human___academy, @geiss11, @sujeitoprogramador), que não haviam aparecido na execução anterior. @charliehills, @nathanhodgson e @ana.gsoares, que tinham retornado dado parcial em 2026-10-12, não retornaram nada de confiável nesta execução. Isso reflete a natureza instável/não-determinística da indexação por WebSearch, não uma mudança real nos perfis monitorados.

---

## Perfis Sugeridos pelo Sistema
Não aplicável nesta execução — `config/profiles.json` já tinha 61 perfis ativos (Modo Análise, não Modo Descoberta).
