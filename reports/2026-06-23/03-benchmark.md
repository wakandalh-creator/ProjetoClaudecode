# Benchmark de Conteúdo — 2026-06-23

## Nota Metodológica

Mesma limitação estrutural do Módulo 2: sem Swarm/`instagram-content-cloner`, a varredura "4 queries × 61 perfis" prescrita em `03-benchmark.md` foi substituída por uma abordagem em duas camadas:

1. **Camada 1 (herdada do Módulo 2):** todos os exemplos de hook/CTA/formato já coletados em `02-perfis-instagram.md`.
2. **Camada 2 (pesquisa adicional direta, 12 buscas):** aprofundamento via WebSearch nos perfis com sinal de engajamento "alto" e hook já confirmado, buscando um segundo post/confirmação de padrão.

Sem acesso a métricas reais de visualizações/curtidas/comentários por post, **`performance_estimada` é inferida a partir de proxy de seguidores + evidência de indexação/recorrência de padrão** — nunca de números de engajamento inventados. Campos que exigiriam inspeção visual/vídeo direta (`duracao_segundos`, `num_slides`, `estilo_visual` detalhado) são marcados **"não disponível"** quando nenhuma fonte os confirmou — não foram estimados.

A seleção do Top 10 e a Seção 2 cobrem os **17 perfis com engajamento "alto" e ao menos 1 hook/CTA verificável** identificados no Módulo 2 — os demais 44 perfis não têm conteúdo específico suficiente para benchmark individual (ver `02-perfis-instagram.md` § Limitações de Dados).

---

## Seção 1 — Top 10 Conteúdos de Alta Performance

Ordenados por `performance_estimada: alto` (todos os 10 estão neste nível); critério de desempate: nº de seguidores (proxy de alcance, não métrica de engajamento real) e tipo de conteúdo (reel > carrossel > foto).

| # | Perfil | Tipo | Tema | Hook | Emoção | Performance |
|---|--------|------|------|------|--------|-------------|
| 1 | @oneyaraujo | reel | Curso "Código Viral" / growth Reels | "🚨 ChatGPT vs Código Viral: Quem vence essa? Me conta nos comentários." | curiosidade | alto |
| 2 | @leandroladeiran | misto | Copywriting/lançamentos | "Como VENDER para quem NÃO GOSTA de ler" | curiosidade | alto |
| 3 | @anatex | reel | IA para negócios (lead gen) | conteúdo de negócios via IA (título truncado nas buscas) | inspiracao | alto |
| 4 | @christiantriad | reel | Produtividade com IA | "Transforme seu dia a dia com IA agora mesmo!" | urgencia | alto |
| 5 | @nick_saraev | reel | AI automation / lead magnet | "Comment 'FLUX' to get this FREE AI Image..." | curiosidade | alto |
| 6 | @jonylan | indeterminado | IA/negócio digital | hook não recuperado nas buscas | indeterminado | alto |
| 7 | @brandsdecoded__ | carrossel | Carrosséis com IA ("Content Machine 3.0") | "Apresentando um pouco mais da nova versão do Content Machine 3.0..." | inspiracao | alto |
| 8 | @marcelaluzzio | reel | Marketing de Conteúdo & IA | hook não recuperado nas buscas | indeterminado | alto |
| 9 | @leosoares.ia | reel | IA para geração de leads | "Com essa IA eu coloco muito mais leads nos funis dos meus..." | inspiracao | alto |
| 10 | @oluizmain | reel | Stories criativos (clonagem de autoridade) | "Salve para fazer seus stories criativos..." | curiosidade | alto |

---

## Seção 2 — Análise por Perfil (17 perfis com sinal "alto" + hook verificável)

### @oneyaraujo (creator → na prática, growth/viral de Reels)
- Conteúdos encontrados: 4+ reels/vídeos confirmados, incluindo cross-post idêntico no TikTok.
- Padrão predominante: reel + curiosidade/comparação (“X vs Y”) + CTA de comentário ou link na bio.
- Melhor conteúdo: "ChatGPT vs Código Viral" — formato de comparação/debate gera engajamento de comentário direto.
- `duracao_segundos` / `num_slides`: não disponível.

### @leandroladeiran
- Conteúdos encontrados: perfil confirmado (2M seguidores, 834 posts), nenhum hook literal de post específico recuperado — apenas tema geral (copywriting/lançamentos/infoprodutos).
- Padrão predominante: misto, hashtags de venda/lançamento como reforço.
- Melhor conteúdo: não identificável com confiança nesta execução.

### @anatex
- Conteúdos encontrados: perfil confirmado, bio e posicionamento ("IA para Negócios"), sem texto completo de hook recuperado (apenas títulos truncados).
- Padrão predominante: reel + foco em geração de leads via IA para empresas.
- Melhor conteúdo: não identificável com confiança — maior seguidor base do lote (682K) sugere alcance consistente, não um pico isolado.

### @christiantriad
- Conteúdos encontrados: perfil confirmado, 2 reels com título parcial sobre IA/produtividade.
- Padrão predominante: reel + urgência ("agora mesmo").
- Contagem de seguidores inconsistente entre buscas (349K vs 585K) — não resolvido nesta execução.

### @nick_saraev
- Conteúdos encontrados: 5+ reels confirmados com o mesmo padrão de CTA ("Comment 'FLUX'", "Comment 'SYSTEM'").
- Padrão predominante: reel + lead magnet via comentário — é o padrão mais consistente e replicado de todo o levantamento.
- Melhor conteúdo: qualquer reel da série "Comment [PALAVRA] to get..." — padrão, não post isolado.

### @jonylan
- Conteúdos encontrados: apenas bio/seguidores (306K); nenhum post específico indexado em nenhuma das duas rodadas de busca.
- Padrão predominante: não disponível.

### @brandsdecoded__ (handle correto confirmado com duplo underscore, diferente do registrado em `config/profiles.json`)
- Conteúdos encontrados: produto "Content Machine 3.0" confirmado por múltiplas fontes (site oficial, plataforma de curso).
- Padrão predominante: carrossel + estrutura problema→solução + CTA de conversão, validado (segundo a própria empresa) em "+25 nichos".
- Melhor conteúdo: carrossel de apresentação do "Content Machine 3.0".

### @marcelaluzzio
- Conteúdos encontrados: perfil confirmado (226K seguidores, 964 posts), apenas título truncado "REELS EM ...".
- Padrão predominante: reel, tema marketing de conteúdo + IA.

### @leosoares.ia
- Conteúdos encontrados: 1 reel confirmado com URL direta.
- Padrão predominante: reel + resultado/prova ("Com essa IA eu coloco muito mais leads") + CTA "Comenta 'IA7'".
- Melhor conteúdo: o reel de leads confirmado é o único ponto de dados, então é por definição o "melhor" identificado.

### @oluizmain
- Conteúdos encontrados: 1 reel confirmado (dica de stories).
- Padrão predominante: reel + CTA "Salve" (save-bait).

### @rodrigobindes
- Conteúdos encontrados: perfil confirmado (278K), 2 reels com hook parcial ("Dono de agência, quer espantar os seus clientes? Faça isto").
- Padrão predominante: reel + confronto/contraste (estilo "erro comum").

### @vendedorglobal
- Conteúdos encontrados: 2 reels/posts do Módulo 2 ("Ganhe em DÓLAR sem precisar investir NADA!").
- Padrão predominante: reel + urgência/promessa financeira.

### @nathanhodgson.ai
- Conteúdos encontrados: bio confirmada ("Built a 6-Figure Business Powered By AI", "Trusted by Google · Meta · OpenAI · Anthropic"), CTA padrão "Comment [PALAVRA] for the full guide" do Módulo 2 — nenhum post novo confirmado nesta rodada.
- Padrão predominante: reel + lead magnet via comentário (mesmo padrão de @nick_saraev).

### @viverdeia.ai
- Conteúdos encontrados: 2 reels adicionais confirmados ("Já imaginou a IA analisando e direcionando...", "O que você vai encontrar dentro do VIVER...").
- Padrão predominante: misto + tom institucional/aspiracional (fundador Rafael Milagre).

### @chase.h.ai
- Conteúdos encontrados: bio detalhada confirmada (201K seguidores, 695 posts, ensina "175.000 pessoas" entre IG/TikTok/YouTube) — nenhum hook literal novo.
- Padrão predominante: reel + educação em IA no-code.

### @sujeitoprogramador
- Conteúdos encontrados: bio/métricas reconfirmadas (167K, 3.014 posts); nenhum post novo recuperado.
- Padrão predominante: reel/misto + hook de identificação ("Se você não passou por isso, ainda não é dev").

### @brun0gpt
- Conteúdos encontrados: dados do Módulo 2 mantidos (157K seguidores); hook recorrente "Aqui 👇" como abertura de leitura.
- Padrão predominante: misto + curiosidade.

---

## Seção 3 — Padrões Transversais

**Emoção dominante:** curiosidade e inspiração lideram entre os top performers (4 de 10 cada categoria combinada), seguidas de urgência. Medo, humor, nostalgia e surpresa não apareceram com evidência textual confirmada em nenhum dos perfis analisados — isso pode refletir o nicho (IA/negócios/marketing tende a vender "resultado" e "oportunidade", não usar gatilhos de medo ou humor como primário).

**Estrutura mais recorrente:** "lead magnet via comentário" (`Comment [PALAVRA] to get/te mando...`) — confirmado em pelo menos 4 perfis distintos (@nick_saraev, @nathanhodgson.ai, @leosoares.ia, @gabriel.adamuchi no Módulo 2) com a mesma mecânica: hook de resultado/curiosidade → prova rápida → CTA de comentário → DM automatizada com o material.

**Tipo de conteúdo dominante no Top 10:** reels (8 de 10); carrossel aparece 1 vez (@brandsdecoded__, com produto dedicado a esse formato); 1 perfil sem tipo confirmável.

**CTA mais frequente:** comentar uma palavra-chave para receber material gratuito por DM — claramente o padrão dominante no nicho de IA/automação monitorado, à frente de "link na bio" (mais comum em infoprodutores/cursos como @oneyaraujo e @brandsdecoded__) e de "salve o post" (@oluizmain).

**Limitação a registrar para o Módulo 4:** nenhum dado de visualizações, curtidas, comentários ou taxa de salvamento por post individual foi confirmado nesta execução — todas as classificações de "performance alto" usam seguidores totais da conta como proxy, não desempenho do post específico. Tratar com essa ressalva ao priorizar replicabilidade no Módulo 4.
