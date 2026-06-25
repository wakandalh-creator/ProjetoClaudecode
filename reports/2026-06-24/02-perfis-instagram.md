# Análise de Perfis Instagram — 2026-06-24

**Nota de metodologia:** a skill `instagram-content-cloner` referenciada no `monitor/modules/02-instagram.md` não está instalada nesta sessão (não existe em `.claude/skills/`). A Fase 1 (extração de hook/estrutura/CTA/tom) foi aproximada manualmente via WebSearch — o Instagram bloqueia WebFetch direto (HTTP 403 confirmado em todas as tentativas). A varredura por Swarm também foi substituída por 3 agentes paralelos (concorrência 3, ~5-6 perfis por agente, equivalente a `batchSize: 5`), cada um com a mesma instrução anti-alucinação.

**Nota de escopo:** `config/profiles.json` tem 61 perfis ativos. Seguindo o precedente da semana passada (15 de 56 analisados), foi analisada uma amostra de **16 perfis** cobrindo as 7 categorias, priorizando handles ainda não analisados em `reports/2026-06-17/`. Dois perfis foram mantidos como ponto de comparação semanal (@nick_saraev, @charliehills — os únicos com dados ricos confirmados na semana anterior) e três foram re-tentados por terem ficado sem dados na semana passada (@ninja.automacoes, @avora.ai, @vendedorglobal).

## Visão Geral dos Perfis

| Perfil | Categoria | Seguidores (aprox.) | Formato Dominante | Engajamento | Hook Padrão |
|--------|-----------|---------------------|--------------------|-------------|-------------|
| @nick_saraev | automacao | ~427K–521K (fontes divergem) | reels | alto (recorrência) | comando+CTA ("Comment QWEN...") / fenômeno nomeado ("SMMA to AI Agencies") |
| @ninja.automacoes | automacao | desconhecido | reels | médio (inferido) | maioria_errando ("Chega de automação Nutella...") |
| @brun0gpt | ia | 157K | misto | médio | abertura padronizada "Aqui 👇" + maioria_errando |
| @larissagomes.ia | ia | 15K | reels | médio | tutorial/prompt + CTA follow+save confirmado em legenda completa |
| @sebintel | ia | desconhecido | reels (inferido) | baixo (dado mínimo) | CTA palavra-chave ("Comment 'Cut'...") |
| @gabrielsamp.ai | ia | — | — | — | sem dados — perfil não localizado com confiança |
| @ana.gsoares | marketing | 146K | misto | desconhecido | outro + CTA palavra-chave "IMERSÃO" (inferido por menção cruzada) |
| @marketerhub.ai | marketing | desconhecido | desconhecido | desconhecido | sem dados — apenas bio institucional |
| @brandsdecoded | marketing | ~301K (handle real: @brandsdecoded__) | misto | desconhecido | sem hook confirmado; divergência de handle |
| @charliehills | creator | 74K | reels | desconhecido | fenômeno_nomeado (confirmado 2ª semana) + CTA link na bio |
| @franklim.gui | creator | 46K | reels | desconhecido | maioria_errando/paradoxo ("faturamento ≠ lucro", recorrente em 7+ reels) |
| @neuwebstudio | agencia | ~52K (não verificado) | misto | desconhecido | sem dados — perfil é agência internacional de web design, fora do nicho esperado |
| @avora.ai | agencia | desconhecido | desconhecido | desconhecido | CTA palavra-chave "SKILLS" confirmado |
| @rodrigobindes | founder | 278K | reels | alto | CTA palavra-chave "TREINAMENTO" confirmado |
| @allesinisgalli | founder | 8.155 | reels | desconhecido | transformacao_silenciosa ("LIBERDADE ATRAVÉS DO...") |
| @vendedorglobal | negocio-digital | 83K | reels | desconhecido | sem hook completo confirmado (2ª semana sem dado de hook) |

---

## Análise Detalhada por Perfil

### @nick_saraev
**Categoria:** automacao
**Bio:** Founder @ Maker School, LeftClick.ai — educador e construtor de agências de automação/IA. Oferta: "Get Your First Client in 90d or Full Refund".

#### Padrões de Hook
- Comando + CTA combinado: "Comment 'QWEN' to get this New Opensource..."
- Fenômeno nomeado: "SMMA to AI Agencies - The New Gold Rush!" (mesmo hook já identificado na semana passada — tema recorrente confirmado)
- Transformação silenciosa: "This piece of information changed my..." (frase cortada na busca)

#### CTA dominante
- Palavra-chave nos comentários (ex.: "Comment QWEN to get this...")

#### Tom de voz
- Adjetivos: direto, didático, orientado a resultado, confiante
- Exemplo: "Don't default to hiring in your business" (frase truncada)

#### Métricas
- 351 posts confirmados; seguidores divergem entre fontes (427K–521K) — sem confirmação única.

**limitacao_dados:** apenas títulos truncados de reels recuperados via busca, sem corpo completo das legendas nem métricas reais de engajamento.

---

### @ninja.automacoes
**Categoria:** automacao
**Bio:** Matheus Pessoa — automação e IA aplicada a negócios (Ninja Academy/Ninja Cursos, inclui curso de Claude Code).

#### Padrões de Hook
- Maioria errando: "Chega de 'automação Nutella' que só..."
- Paradoxo/contraste: "Você está preso em um jogo onde só ganha se estiver..."
- Fenômeno nomeado: "O Ninja Rank não é só mais uma ferramenta de..."

#### CTA dominante
- Não confirmado diretamente — padrão de nicho sugere CTA por comentário, mas sem exemplo real capturado.

#### Tom de voz
- Adjetivos: provocador, didático, direto.

**limitacao_dados:** re-tentado após não ter dados na semana 06-17 — desta vez obteve-se bio e hooks truncados, mas ainda sem seguidores/posts/CTA confirmados. Há possível confusão com handle parecido (@ninja_automacoes) em alguns resultados.

---

### @brun0gpt
**Categoria:** ia
**Bio:** Bruno Francisco | IA e Marketing — conteúdo sobre marketing e vendas com IA em português.

#### Padrões de Hook
- Abertura padronizada "Aqui 👇" seguida de diferentes ganchos (maioria_errando, transformação silenciosa, paradoxo) — padrão estrutural consistente em pelo menos 4 posts.
- Tutorial direto: "Primeiro, peça ao ChatGPT para analisar suas métricas..."

#### CTA dominante
- Inferido como DM implícita/link na bio (via "Aqui 👇"), não confirmado por texto completo.

#### Tom de voz
- Adjetivos: didático, direto, consultivo, orientado a tutorial.

#### Métricas
- 157K seguidores, 1.334 posts confirmados.

**limitacao_dados:** hooks são apenas início de legenda (cortados pela indexação); sem dados de engajamento.

---

### @larissagomes.ia
**Categoria:** ia
**Bio:** Marketing e IA — "criar, crescer e vender todos os dias com IA".

#### Padrões de Hook
- Tutorial estruturado: "Peça o ChatGPT para analisar o feed do seu Instagram 🧠" — **legenda completa recuperada via republicação no TikTok**, caso raro de confirmação total nesta rodada.

#### CTA dominante
- Follow explícito + salvar post: "siga @larissagomes.ia para receber mais conteúdos como esse" + "📩 Salva pra lembrar de analisar o seu perfil!" — confirmado em texto completo.

#### Tom de voz
- Adjetivos: didático, estruturado, acessível, engajador.

#### Métricas
- 15K seguidores, ~262 posts (fonte única, não cruzada).

**limitacao_dados:** apenas 1 dos 4 hooks identificados teve legenda completa; demais são títulos truncados. Sem dados de engajamento.

---

### @sebintel
**Categoria:** ia

**limitacao_dados:** dado mínimo — apenas 1 reel encontrado com hook parcial ("Comment 'Cut' and I'll send you the full guide..."). Bio, seguidores, posts, tom e temas não confirmados. Risco de mistura com perfis homônimos não relacionados.

---

### @gabrielsamp.ai
**Categoria:** ia

**limitacao_dados:** nenhum resultado relevante encontrado no Instagram. Apenas uma conta de TikTok com o mesmo handle foi confirmada, sem ligação comprovada com um perfil de Instagram. Possível perfil inexistente, muito pequeno/pouco indexado, ou renomeado.

---

### @ana.gsoares
**Categoria:** marketing
**Bio:** Ana G. Soares — Agile Coach, fundadora da Universidade Ágil (UNIAGIL), criadora do método LACP e da imersão "Claude Project"; hospeda o podcast "Vivendo do Digital".

#### Padrões de Hook
- Outro: "Se você acordou hoje com a sensação de que o tempo..." (frase truncada).

#### CTA dominante
- Inferido (não confirmado em legenda direta): comentar "IMERSÃO" para acesso ao "Lote Zero" de um produto — inferido de menções cruzadas no Threads sobre o lançamento "Claude Project".

#### Tom de voz
- Adjetivos: motivacional, didático, aspiracional, direto.

#### Métricas
- 146K seguidores, 2.840 posts confirmados.

**limitacao_dados:** CTA não confirmado em legenda direta, apenas inferido; sem dados de engajamento; hook capturado apenas truncado.

---

### @marketerhub.ai
**Categoria:** marketing
**Bio:** "Empowering Digital Marketers" — comunidade privada de marketing com IA (cursos, prompts, templates).

**limitacao_dados:** perfil com menos dados confirmados entre os 16 analisados — sem seguidores, posts, hooks, CTA ou tom de voz confirmados. Apenas a descrição institucional do site/bio foi recuperada.

---

### @brandsdecoded
**Categoria:** marketing
**Bio:** BrandsDecoded® | AI Content Agency, administrada por Leonardo Varricchio — promove a ferramenta "Content Machine 3.0" para criação automatizada de carrosséis.

#### Tom de voz
- Adjetivos: confiante, tecnológico, promocional, aspiracional.
- Exemplo (truncado): "A ferramenta mais poderosa que já criei está disponível"

#### Métricas
- ~301K seguidores, 1.734 posts (fonte aponta handle real como @brandsdecoded__, com dois underscores).

**limitacao_dados:** divergência de handle não resolvida (config tem `@brandsdecoded` sem underscores — recomenda-se verificar e corrigir em `config/profiles.json`, similar ao caso @rafa.grandi/@humam__academy já reportado na semana anterior). CTA é inferência de nicho, não confirmado em legenda real.

---

### @charliehills
**Categoria:** creator
**Bio:** "I help you (actually) use AI" — guias gratuitos de Claude na bio, newsletter no Substack sobre Claude, Nano Banana (Gemini) e workflows de IA para conteúdo.

#### Padrões de Hook (confirmados com texto completo)
- Fenômeno nomeado: "Did you know that ChatGPT has 8 hidden personalities that you can choose from?"
- Fenômeno nomeado: "We're so cooked. Nano Banana 2 dropped today. Look at this..."

#### CTA dominante
- Link na bio para recurso gratuito (ex.: "Click here for FREE: stan.store/charliehills1/p/chatgpt-personalities-guide") — tipo "link na bio", diferente do CTA de palavra-chave em comentário dominante em outros perfis do nicho.

#### Tom de voz
- Adjetivos: direto, prático, bem-humorado, didático, informal.

#### Métricas
- 74K seguidores, 202 posts — mesmos números da semana passada (perfil estável).

**limitacao_dados:** segunda semana consecutiva com dados ricos confirmados — bom candidato a perfil de referência fixo para benchmark contínuo.

---

### @franklim.gui
**Categoria:** creator
**Bio:** Guilherme Franklim — cursos de IA (foco em Claude Code) e tráfego pago "low-ticket"; produtos: "Dev de Oferta Roadmap", "GG Checkout", "GG Spy".

#### Padrões de Hook (tema recorrente confirmado em 7+ reels)
- Maioria errando: "Confundir faturamento com lucro é um erro."
- Paradoxo/contraste: "Faturamento é o que entra. Lucro é o que sobra. Simples assim."

#### Tom de voz
- Adjetivos: direto, didático, objetivo, confrontador (no sentido de corrigir crenças erradas).

#### Métricas
- 46K seguidores, 159 posts.

**limitacao_dados:** CTA não confirmado em legenda (apenas inferido do link na bio); sem dados de engajamento.

---

### @neuwebstudio
**Categoria:** agencia

**limitacao_dados:** divergência relevante de nicho — o perfil encontrado é uma agência internacional de web design (fundadores não-brasileiros, foco em Webflow/animações Figma), não um perfil brasileiro de IA/automação/negócios digitais como esperado pela categoria "agencia" do monitoramento. Recomenda-se revisar se este é o handle correto em `config/profiles.json`.

---

### @avora.ai
**Categoria:** agencia
**Bio:** "Siga @avora.ai para conteúdos diários sobre IA na prática!"

#### Padrões de Hook
- "👉 Comente 'Skills' para receber o acesso!"

#### CTA dominante
- Palavra-chave nos comentários ("SKILLS") confirmado em trecho de legenda real.

#### Tom de voz
- Adjetivos: prático, direto, educativo.

**limitacao_dados:** re-tentado após não ter dados na semana 06-17 — desta vez obteve-se confirmação de existência e 1 CTA real, mas sem seguidores/posts/formato dominante confirmados.

---

### @rodrigobindes
**Categoria:** founder
**Bio:** "Mostro como chegar aos 100k/mês com agência de mkt".

#### Padrões de Hook
- "Comente 'TREINAMENTO' pra receber o link de inscrição do..."

#### CTA dominante
- Palavra-chave nos comentários ("TREINAMENTO") confirmado.

#### Tom de voz
- Adjetivos: direto, mentor, orientado a resultado, didático.

#### Métricas
- 278K seguidores, 1.835 posts — engajamento estimado alto (maior seguidor:post ratio entre os founders analisados).

**limitacao_dados:** apenas 1 legenda completa capturada; formato "reels" inferido pelos links retornados, não por contagem real.

---

### @allesinisgalli
**Categoria:** founder
**Bio:** Allessandra Sinisgalli — especialista em IA aplicada a negócios; mentoria "IA CLUB" / "Gold Proximity".

#### Padrões de Hook
- Transformação silenciosa: "LIBERDADE ATRAVÉS DO..."
- Outro: "VENDAS COM AI & MARKETING | A..."

#### Tom de voz
- Adjetivos: aspiracional, prático, educativo, motivacional.

#### Métricas
- 8.155 seguidores, 3.548 posts — alto volume de posts para audiência pequena.

**limitacao_dados:** CTA dominante não confirmado; hooks apenas truncados.

---

### @vendedorglobal
**Categoria:** negocio-digital
**Bio:** Murilo Bevervanso — e-commerce e IA, comunidade "Troop do MAESTRO".

#### Métricas
- 83K seguidores, 2.280 posts — mesmos números da semana passada (perfil estável).

**limitacao_dados:** segunda semana consecutiva sem hook ou CTA literal confirmado — buscas retornam apenas títulos genéricos sem gancho completo. Tom inferido apenas pela descrição institucional (canal YouTube, site), não por copy real do Instagram.

---

## Perfis Sugeridos pelo Sistema
N/A — `config/profiles.json` já tinha perfis ativos (modo análise), Modo Descoberta não foi executado.

---

## Limitações de Dados

- **6 de 16 perfis** (@sebintel, @gabrielsamp.ai, @marketerhub.ai, @neuwebstudio, @avora.ai, @vendedorglobal) retornaram dados mínimos ou nenhum hook/CTA confirmado — o Instagram não expõe esse nível de detalhe a buscas públicas indexadas, e o WebFetch direto foi bloqueado (403) em 100% das tentativas.
- **@brandsdecoded** — possível divergência de handle: fonte indica @brandsdecoded__ (dois underscores), não @brandsdecoded. Revisar em `config/profiles.json`.
- **@neuwebstudio** — o perfil encontrado é uma agência internacional de web design, não condiz com o nicho esperado (IA/automação/negócios digitais BR). Revisar handle.
- **@gabrielsamp.ai** — não foi possível confirmar a existência do perfil no Instagram (apenas TikTok homônimo, sem vínculo comprovado).
- **Pendências da semana anterior ainda não resolvidas:** @rafa.grandi (handle parece ser perfil pessoal não relacionado) e @humam__academy (possível typo, talvez @human___academy) não foram re-analisados nesta rodada — seguem sinalizados desde `reports/2026-06-17/02-perfis-instagram.md`.
- **Cobertura parcial:** 16 dos 61 perfis ativos foram analisados nesta execução. Os 45 perfis restantes não foram processados — ver nota de escopo no topo do relatório para critério de amostragem.
- Nenhum dado de engajamento (curtidas, comentários, taxa) pôde ser confirmado numericamente para nenhum dos 16 perfis — todas as classificações de "engajamento" são estimativas qualitativas, não métricas reais.
- **Perfis de continuidade:** @nick_saraev e @charliehills mantiveram dados estáveis em relação à semana passada (mesmos números de seguidores/posts para @charliehills; tema recorrente "SMMA to AI Agencies" confirmado novamente para @nick_saraev), sugerindo que são bons candidatos a virar referência fixa de benchmark nas próximas semanas.
