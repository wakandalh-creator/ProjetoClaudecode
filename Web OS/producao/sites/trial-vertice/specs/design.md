# Design Spec — trial-vertice (slug provisório)

> Fonte única da verdade do design deste projeto. Gerado pelo Molda (módulo 21) a partir de `estrategia.md`, `references/notas-referencia.md`, `Web OS/bancos/design-tokens-globais.md` e `Web OS/bancos/componentes-aprovados.md`. **Precisa de aprovação explícita do Lucas antes do módulo 22 (build) começar** — ver seção Aprovação no fim, com as decisões específicas que pedem confirmação dele.
>
> Nota de método: `design-tokens-globais.md` e `componentes-aprovados.md` estão **vazios** (nenhum projeto Web OS passou por aqui ainda — `teste-piloto-vertice` foi descartado e não reaproveitado). Este é o primeiro conjunto de tokens/componentes real do sistema. Tudo abaixo é proposto como primeira entrada dos bancos, não como herança de um padrão já existente — a aprovação do Lucas neste documento funciona como a confirmação de promoção exigida pelas regras do módulo.

## Referências analisadas

Ver `references/notas-referencia.md`. Nenhum site individual foi screenshotado/analisado nesta sessão (sem ferramenta de navegação visual disponível) — a direção vem de características conhecidas das 3 galerias indicadas pelo Lucas (Awwwards = craft, land-book = estrutura B2B, minimal.gallery = contenção), combinadas com `branding/neovertix/01-estrategia.md` §8.

## Contexto que molda as decisões abaixo

- **ICP não é tech/startup**: comércio local e PME (clínicas, concessionárias, imobiliárias, advocacia) — decisor único, não comitê, não é público que valoriza estética "SaaS do Vale do Silício". Isso pesa contra qualquer intensidade de motion alta e contra qualquer visual que pareça "ferramenta de dev".
- **Não existe Garantia Vértice aqui.** O mecanismo de confiança próprio é: instância própria por cliente + descarte automático se não comprar. Isso precisa de bloco visual pesado (Passo 3c), não FAQ.
- **Lucas aparece como pessoa** (Cara Comum), mesmo sem vender por reunião.
- **Prova principal = log de conversa real**, formato de conversa, não dashboard.
- **Nenhuma alegação de segurança/LGPD/criptografia** — isso restringe até a escolha de ícone (ver Passo 3c).

---

## Tokens do projeto

Herdados de `Web OS/bancos/design-tokens-globais.md` onde já havia valor concreto (Spacing, Breakpoints, vocabulário de Motion); definidos aqui como primeira proposta onde o banco estava vazio (Color, Typography, Radius, Shadow, Intensity de Motion escolhida).

### Color

| Token | Valor | Uso | Desvio do global? Por quê? |
|---|---|---|---|
| `color.bg.dark` (off-black) | `#16151A` | Fundo de seções escuras (Hero, Trust Architecture) | Não é desvio — é a 1ª entrada do banco. Off-black conforme `01-estrategia.md` §8 (nunca preto puro `#000`). |
| `color.bg.light` (off-white) | `#F6F3EE` | Fundo de seções claras (maioria da página) | 1ª entrada. Off-white com leve tom papel — evita branco clínico/estéril, reforça "comércio local/humano" em vez de "SaaS frio". |
| `color.text.ink` | `#1C1B1F` | Texto sobre fundo claro | 1ª entrada. Ligeiramente mais suave que o off-black de fundo, pra não competir com ele como "quase-preto duplo". |
| `color.accent.clay` | `#C1552E` (terracota/argila) | ÚNICA cor de destaque da página inteira: CTA, links, grifos, linhas divisórias do bloco de confiança | 1ª entrada — **decisão que pede confirmação do Lucas** (ver Aprovação). Escolhido no lugar de azul/verde: azul é o clichê do nicho CRM/automação (inclusive os concorrentes a validar no módulo 28 — RD Station, Kommo); verde seria lido como "clichê do WhatsApp"; terracota é quente, sóbrio, humano (reforça Cara Comum) e nunca aparece em `01-estrategia.md` §8 como banido. |
| `color.neutral.100/400/700` | `#D8D5D0` / `#8C8A87` / `#4B4A50` | Bordas, divisores, texto secundário | 1ª entrada — rampa neutra derivada do off-black/off-white, sem matiz própria (evita 2ª cor de destaque competindo com a clay). |

**Regra de aplicação, não negociável nesta página:** uma única cor de destaque (`clay`) em toda a página — nunca duas cores saturadas disputando atenção na mesma tela (requisito literal de `01-estrategia.md` §8). Zero gradiente em qualquer combinação dessas cores.

### Typography

| Token | Valor | Uso | Desvio do global? Por quê? |
|---|---|---|---|
| `font.display` | Fraunces (variável, eixo óptico "display", peso 600–700) | H1, H2, tagline, citação de destaque | 1ª entrada. Serifada com caráter (não é geométrica-sans-de-SaaS-genérico) — carrega peso/presença institucional, compatível com público que não é tech-hype. Variável = 1 arquivo só cobrindo a faixa de peso, ajuda o budget de performance (Passo 2b). |
| `font.body` | Hanken Grotesk (variável, peso 400–600) | Corpo de texto, labels, botões, transcrição do log de conversa | 1ª entrada. Grotesco neutro e muito legível em telas pequenas (ICP majoritariamente mobile, 320–430px) — evitado "Inter" de propósito por ser a fonte-padrão mais associada a templates genéricos de IA/SaaS. |
| Escala (base 16px, razão ~1,25) | 12 / 14 / 16 / 20 / 25 / 31 / 39 / 49 / 61 (px) | caption/label / small / body / lead / H4 / H3 / H2 / H1 mobile / H1 desktop | Escala moderada (não dramática) — coerente com a contenção de minimal.gallery, evita "drama de tipografia" como substituto de conteúdo real. |
| Peso como hierarquia | H1/H2 em Fraunces 600–700; H3/H4/labels em Hanken Grotesk 600; corpo em 400; botão em 500 | — | Operacionaliza a regra da marca "tipografia carrega mais peso do que cor" — a hierarquia vem do peso/escala tipográfica, a `clay` fica reservada só pra pontos de ação/prova. |

**Tell evitado deliberadamente:** eyebrow em ALL-CAPS repetido (está na lista de marcas de "IA genérica" do piso de craft). Onde a página precisar de um rótulo pequeno acima de um título, usa Hanken Grotesk 500 em caixa normal (sentence case) com uma linha/régua em `clay` ao lado — nunca caixa alta.

### Spacing

Escala 4/8/12/16/24/32/48/64/80/96 (px) — herdada sem desvio.

### Radius

| Token | Valor | Uso | Desvio do global? Por quê? |
|---|---|---|---|
| `radius.sm` | 4px | Inputs, chips pequenos | 1ª entrada. |
| `radius.md` | 8px | Botões, cards | 1ª entrada. **Decisão deliberada: nunca pill/full-round em botão** — pill button é parte do "kit de card SaaS" genérico listado no piso de craft; 8px mantém sóbrio/institucional. |
| `radius.lg` | 16px | Painéis grandes, blocos de imagem/moodboard | 1ª entrada. |

### Shadow

| Token | Valor | Uso | Desvio do global? Por quê? |
|---|---|---|---|
| `shadow.none` (padrão) | sem sombra — separação por borda de 1px em `neutral.100` | Estado padrão de todo card/bloco | 1ª entrada. Evita o tell "card flutuando com sombra pesada sobre fundo gradiente" — usa a lógica de "profundidade em camadas de fundo" da marca em vez de sombra. |
| `shadow.elevated` | deslocamento vertical pequeno (4px), blur baixo, opacidade baixa (~8%) | Só em estado de hover/foco pontual (dropdown, card elevando no hover) — nunca no estado padrão | 1ª entrada. |

### Breakpoints

320 / 375 / 390 / 430 / 768 / 1024 / 1280 / 1440+ (px) — herdado sem desvio. Atenção especial no Passo 2a-bis abaixo aos componentes que mudam de layout nos 4 primeiros (320–430), onde o ICP majoritariamente acessa.

### Motion

Motor: **GSAP + Lenis** (padrão obrigatório de todo projeto Web OS, não é escolha deste projeto).

| Categoria | Valor | Desvio do global? Por quê? |
|---|---|---|
| Duration | 200ms (padrão) · 300ms (transição de seção) · 500ms (entrada de bloco) | Sem desvio — usa os valores padrão do banco. |
| Easing | `ease-out` (entrada) · `ease-in-out` (transição) | Sem desvio. **Spring explicitamente descartado**: o atributo de voz "sóbrio, não gritado" (`01-estrategia.md` §6) não permite registro de tom brincalhão — spring ficaria na linha do que a marca evita. |
| **Intensity** | **Medium** | **Decisão que pede atenção do Lucas** (ver Aprovação) — o banco global descreve Subtle como o ajuste padrão pra "nicho B2B sóbrio/institucional", e este ICP é literalmente isso. Justificativa pra ainda assim escolher Medium (scroll-reveal por seção, sem pinning) em vez de Subtle (só Hero + micro-interação): a página tem estrutura narrativa sequencial pesada (problema → arquitetura de confiança → como funciona → prova → oferta → objeções) que se beneficia de revelar-ao-rolar pra pautar a leitura seção a seção — função de motion = orientar + criar continuidade, não decoração. Scroll-reveal sóbrio (fade + leve slide, sem pin/scrub/parallax) hoje é padrão esperado em página B2B bem executada (inclusive no padrão estrutural de land-book) — a ausência total dele arrisca parecer estática/barata, o que vai contra o piso de craft ("isso não é barato"). **Strong/Cinematic fica explicitamente fora** (pinning/scrubbing/parallax real) — incompatível com o ICP e com o orçamento de performance mobile. |
| Movement | Fade + Slide (8–16px) como vocabulário base de entrada de seção. Scale (0.98→1) reservado só pro bloco de prova (log de conversa), simulando mensagens "chegando" — função: gerar emoção com intenção. Nenhum rotate/blur/parallax/morph — nenhuma seção pede. | Sem desvio de vocabulário, escolha de onde aplicar é deste projeto. |

`prefers-reduced-motion: reduce` sempre respeitado — com motion desligado, cada seção continua legível e a mensagem central ("5 dias, canal real, sem compromisso") chega inteira só com texto.

---

## Piso de craft (Passo 2a-bis) — checklist aplicado neste projeto

| Item do piso | Como este projeto cumpre |
|---|---|
| Zero marca de "IA genérica" | Sem gradiente azul-roxo (paleta off-black/off-white + 1 accent terracota), sem card de vidro, hero não é stack centralizado sobre gradiente (ver Hero no inventário — layout assimétrico), sem eyebrow ALL-CAPS repetido, sem kit de card SaaS (botão sem pill, sombra ausente por padrão). |
| Micro-interação real em todo interativo | Botão: hover = leve elevação (2px) + mudança de cor, foco = anel visível em `clay`, active = scale 0.98. Link: sublinhado crescendo do centro. Card: hover = borda muda de `neutral.100` pra `clay` + leve elevação, nunca sombra pesada. Campo de formulário (conexão de canal): foco com anel `clay` + estado de validação inline. Nenhum elemento fica no default do navegador. |
| Motor de animação de verdade | GSAP + Lenis confirmados como motor deste projeto (não é opcional). |
| Tipografia com hierarquia deliberada | Ver escala e pesos acima — documentados, não "no olho". |
| Responsividade sem concessão | Componentes com atenção extra nomeada no Inventário (funil de 3 passos, bloco de prova, comparação de 2 planos) — teste real nos 8 breakpoints é item de QA do módulo 22, não opcional. |
| Performance dentro do budget | Ver Passo 2b abaixo — cada efeito proposto já nasce dentro do limite. |

---

## Performance budget (Passo 2b)

Limiares de auditoria (herdados, mesmos do módulo 23): **LCP < 2,5s · INP < 200ms · CLS < 0,1**.

Orçamento consciente deste projeto:

- **Fontes**: 2 arquivos variáveis (Fraunces + Hanken Grotesk), subset Latin + diacríticos PT-BR, self-hosted woff2, combinado ~90–120kb. Fonte do elemento de LCP (H1 em Fraunces) com preload.
- **Elemento de LCP = texto, não imagem.** Decisão deliberada: este é um serviço sem produto físico, e a prova mais forte (log de conversa) é representada em HTML/CSS real, não screenshot — isso mantém o LCP leve, o conteúdo acessível/copiável, e evita a armadilha de um hero com imagem pesada competindo com o orçamento.
- **Motion**: GSAP core + Lenis + ScrollTrigger (Intensity Medium usa) — pacote já aceito como custo padrão de todo projeto Web OS, sem biblioteca de animação adicional.
- **Imagens** (se houver, ver Passo 4/`images.md`): WebP/AVIF, responsive srcset, lazy-load abaixo da dobra. Meta: <150kb por imagem perto do hero, <80kb por imagem de apoio. Nada acima da dobra bloqueando o LCP além do texto do H1.
- **Sem vídeo** no escopo desta V1 (não citado no brief) — se entrar depois, orçamento é revisto.

---

## Trust Architecture (Passo 3c)

Pra cada seção que promete algo, a evidência vem antes — nunca "depoimento" como única fonte, e aqui não há nem depoimento disponível ainda (sem prova social própria, por brief).

| Seção | Promessa | Evidência que vem antes (ou junto) |
|---|---|---|
| **Hero** | "Escala sem contratar" | A promessa já nasce em formato factual, não adjetivo: linha de apoio imediata com o fato verificável — "5 dias. Seu WhatsApp real. Sem reunião, sem cartão." A tagline não fica sozinha sem âncora concreta ao lado. |
| **Arquitetura de Confiança (objeção nº1)** | "Pode confiar o canal" | Clareza de mecanismo, não selo: explicar a instância própria por cliente + descarte automático se não comprar como um diagrama editorial de 3 passos (texto + divisores geométricos), não como badge de segurança. **Nenhum ícone de cadeado/escudo** — ver nota de atenção na Aprovação, porque nenhuma alegação de segurança/LGPD foi declarada, e um ícone desses sugere certificação que não existe. Extensão da regra "zero ícone de robô" pra zero ícone de segurança não-declarada. |
| **Como funciona (3 passos)** | "É rápido de ativar" | Os 3 passos nomeados e honestos (conectar canal real self-service → suporte do agente de IA durante a configuração → agente atende leads reais por 5 dias) — mostra a fricção real (o dono precisa ter a senha do WhatsApp) em vez de prometer "fácil" vago. |
| **Prova (log de conversa)** | "O agente realmente atende" | Evidência = a própria transcrição real, não dashboard. **Esta seção depende de um conteúdo real que ainda não existe** — ver pendência na Aprovação; o componente está pronto pra receber o log, mas não pode ser publicado com transcrição inventada/placeholder. |
| **Quem constrói (Lucas)** | "Alguém de verdade responde se travar" | Foto real do Lucas + autoria do código — Cara Comum, nunca "nossa equipe". |
| **Oferta (2 planos)** | Preço | Números reais liberados (§7 do brief), setup e recorrência sempre no mesmo bloco — nunca entrada isolada escondendo custo total. |
| **Objeções/FAQ** | Respostas pontuais | Reforça a Arquitetura de Confiança já exposta mid-page — nunca é a primeira vez que a objeção nº1 aparece. |
| **CTA final** | Repete o Hero | Mesma âncora factual (5 dias, instância própria, sem cobrança) — função de motion = criar continuidade. |

---

## Inventário de componentes (Passo 3)

`componentes-aprovados.md` está vazio — não há nada pra reaproveitar ainda. Todo componente abaixo é **custom**, e os bem-sucedidos entram como candidatos ao banco (promoção só com confirmação do Lucas, não automática).

Direção visual (lente `frontend-design`: tipografia/cor/layout deliberados) + decisões de movimento (lente `emil-design-eng`: easing/duração/função) — uma lente por decisão, sem empilhar.

| Seção | Reaproveitar? | Construir custom — direção | Motion |
|---|---|---|---|
| **Header/Nav** | Não há o que reaproveitar | Minimal: logo + 1 CTA (mesmo texto do CTA primário da página, sem CTA secundário competindo). Sticky, fundo off-white translúcido só depois de rolar (nunca glass/blur pesado). | Entrada: fade 200ms. Sem scroll-trigger (é chrome de interface, não conteúdo). |
| **Hero** | Custom | Layout assimétrico 2 colunas (headline Fraunces + sub-linha factual + CTA à esquerda; indício visual do Lucas/produto à direita) — **não** stack centralizado sobre gradiente (tell explícito a evitar). | Fade+slide-up na entrada (500ms, ease-out) — função: orientar o olhar headline→CTA. |
| **Problema** | Custom | Bloco de texto curto + os 2 cálculos permitidos (custo de SDR CLT, custo de lead perdido) apresentados como conta, não slogan — tipografia fazendo o peso, sem gráfico inventado. | Scroll-reveal fade+slide (Medium), uma vez só por bloco. |
| **Arquitetura de Confiança** | Custom — **candidato forte a componente-base do banco**, qualquer projeto Web OS sem Garantia Vértice vai precisar disso | Diagrama editorial de 3 etapas com divisores em `clay`, tipografia carregando a explicação — sem ícone de cadeado/escudo (ver nota acima). Bloco com o mesmo peso visual do CTA, não enterrado em FAQ. | Revela as 3 etapas em sequência no scroll (stagger ~150ms entre etapas) — função: explicar o mecanismo passo a passo. |
| **Como funciona (3 passos)** | Custom | Numerado, horizontal no desktop (1024+), empilhado a partir de 768. Linguagem honesta sobre a etapa técnica (não promete tempo). | Cada passo revela no scroll, mesma lógica do bloco de Confiança — função: criar continuidade entre os dois blocos vizinhos. |
| **Prova (log de conversa)** | Custom — componente **"Conversation Log"**: thread estilizada tipo mensagem, não dashboard | Tipografia Hanken Grotesk pra transcrição, bolhas sutis diferenciando remetente, sem gráfico de métrica inventado ao lado. **Conteúdo real pendente** (ver Aprovação). | Bolhas entram com scale 0.98→1 staggered — função: gerar emoção com intenção (mensagens "chegando"). |
| **Quem constrói (Lucas)** | Custom | Bloco pequeno, foto real + 2-3 linhas, zero "equipe"/"nós corporativo". | Fade simples, sem drama — função: confirmar quem responde. |
| **Oferta (2 planos)** | Custom | 2 cards lado a lado (empilhados <768), borda hairline em `neutral.100`, sem badge "mais popular" (gimmick de SaaS). Setup + recorrência sempre no mesmo número. | Fade+slide-up simples, sem stagger — função: confirmar, não vender demais. |
| **Objeções/FAQ** | Custom | Accordion simples, resposta factual curta por item (fonte: §3 do brief). | Expand/collapse com 200ms ease-in-out — função: confirmar. |
| **CTA final** | Custom | Repete a âncora factual do Hero, mesmo botão primário. | Fade+slide, função: criar continuidade/fechamento. |
| **Footer** | Custom | Minimal: assinatura "A gente constrói, não promete." + links institucionais neutros (sem alegação de segurança/LGPD no corpo — um link de política de privacidade no footer é prática padrão, não é "selo" de alegação). | Sem motion. |

**Atenção nos breakpoints 320–430 (Passo 2a-bis):** funil de 3 passos empilha mais cedo (768 já vertical, não só mobile estrito), bloco de prova vira coluna única a partir de 768, comparação de 2 planos nunca usa tabela com scroll horizontal — sempre cards empilhados.

---

## Pipeline de imagem (Passo 4)

**Sem produto físico** — é um serviço. Decisão deliberada antes de qualquer prompt: esta página é **text/componente-led**, não imagem-led — a prova central (log de conversa) é HTML/CSS real, não imagem gerada, e o Hero não depende de imagem pra funcionar como LCP (ver Passo 2b). Isso reduz a dependência de imagem a quase zero, o que também evita o risco de imagem genérica de IA competindo com a autenticidade exigida (Cara Comum, veracidade).

Detalhe completo em `images.md`.

---

## Decisões que pedem confirmação explícita do Lucas (não é a aprovação final da seção abaixo — são pontos específicos dentro dela)

1. **Cor de destaque `clay` (`#C1552E`)** — 1ª entrada de Color no banco global, escolhida pra evitar o clichê azul (CRM/automação) e verde (WhatsApp), mas é uma escolha nova, sem precedente de marca documentado em hex.
2. **Par tipográfico Fraunces + Hanken Grotesk** — 1ª entrada de Typography no banco global.
3. **Intensity de Motion = Medium**, não Subtle — o banco global descreve Subtle como o ajuste padrão pra exatamente este tipo de ICP (B2B sóbrio/institucional); escolhi Medium por justificativa narrativa/estrutural (ver tabela de Motion), mas é uma divergência do "match óbvio" que vale o Lucas confirmar antes do módulo 22.
4. **Extensão da regra "zero ícone de robô" pra também excluir ícone de cadeado/escudo** no bloco de Arquitetura de Confiança — inferência do Molda a partir da regra de veracidade (nenhuma alegação de segurança declarada), não uma instrução literal do brief.
5. **Pendência de conteúdo, não de design**: o componente "Conversation Log" está especificado, mas **não pode ir ao ar com transcrição inventada** — precisa do log real que o brief menciona como existente, mas que ainda não foi entregue a este módulo. Isso bloqueia a publicação da seção de Prova, não o resto do build.

## Aprovação

- [ ] Aprovado pelo Lucas em: {data}
