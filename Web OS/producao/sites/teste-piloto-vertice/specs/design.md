# Design Spec — Piloto Vértice (teste-piloto-vertice)

> Fonte única da verdade do design deste projeto. Gerado pelo Molda (módulo 21) ANTES de qualquer código.
> **Status: PROJETO DE TESTE do pipeline Web OS.** Não vai ao ar — valida o módulo 21 ponta a ponta.
> Precisa de aprovação explícita do Lucas antes do módulo 22 (build) começar. Ver checklist no final.
> Entrada: `estrategia.md` (módulo 20, Tese-ext) · `Web OS/bancos/design-tokens-globais.md` (hoje vazio) · `Web OS/bancos/componentes-aprovados.md` (hoje vazio) · `branding/neovertix/tokens.json` + `tokens.css` + `brandbook.md`.

---

## Referências analisadas

**Nenhuma referência externa curada pelo Lucas nesta rodada** (sem Dribbble/Awwwards/Pinterest) — desvio deliberado do Passo 1 do módulo 21, autorizado explicitamente para este teste porque o projeto é da própria Neovertix, não de um cliente novo sem identidade.

Referência primária usada no lugar: a identidade de marca já aprovada pelo Lucas —

- `branding/neovertix/tokens.json` + `tokens.css` — tokens formalizados a partir do logo final aprovado.
- `branding/neovertix/brandbook.md` — voz, arquétipos, paleta, tipografia, aplicação.
- `branding/neovertix/logo/final/logo-neovertix.png` — asset de logo aprovado (não recriar).

Pendência registrada (não bloqueia esta spec): se um dia o Lucas quiser curar referências de layout/estética de página externas pra inspirar a composição por seção, isso entra como adendo — os tokens de marca já são base suficiente pra fechar esta spec.

## Tokens do projeto

Herança: `Web OS/bancos/design-tokens-globais.md` está vazio em todas as categorias de cor/tipografia/radius/shadow (só Spacing e Breakpoints têm default genérico populado). Por isso, **a origem destes tokens é `branding/neovertix/tokens.json`/`tokens.css` diretamente — não o banco global do Web OS.** Motivo do desvio: este não é um cliente novo sem identidade — é a própria Neovertix, com marca e logo já aprovados pelo Lucas; herdar do próprio brandbook é mais correto do que herdar de um banco genérico vazio.

| Categoria | Valor | Desvio do global? Por quê? |
|---|---|---|
| Color — estrutura (fundo) | `bg-canvas` `#0A0E1A` (navy quase-preto, nunca preto puro) · `surface-base` `#121A2E` · `surface-raised` `#1A2440` · `surface-overlay` `#232F52` | Banco global vazio nessa categoria. Herdado de `branding/neovertix/tokens.json`. Confirma `estrategia.md` §6: "off-black/off-white, nunca preto puro". |
| Color — texto | `text-primary` `#F5F7FA` (17,9:1 AAA) · `text-secondary` `#AAB4C2` (9,2:1 AAA) · `text-muted` `#7A8699` (5,2:1 AA — evitar em `surface-overlay`, cai p/ 3,6:1) | Idem acima. |
| Color — destaque (accent) | `#43A047` (verde contido da seta do logo) · hover `#66BB6A` · texto sobre accent `#121A2E` (nunca branco — branco dá só 3,3:1, reprova AA) | Idem acima. **Regra herdada de `estrategia.md` §6: UMA cor de destaque por tela** — accent reservado pro CTA e pra 1 número de prova (ver Garantia Vértice abaixo), nunca espalhado como decoração. |
| Typography | Display: **Chakra Petch** 600/700 (h1–h4) · Texto: **Manrope** 400–700 (body/UI) · Mono: **JetBrains Mono** 400/500 (anotação técnica, eyebrow) — escala completa em `tokens.json > type-scale` (h1 3.5rem/1.05 → overline 0.72rem/uppercase) | Banco global vazio nessa categoria. Herdado de `branding/neovertix/tokens.json`. |
| Spacing | Escala 4/8px: `space-1` 0.25rem (4px) → `space-9` 6rem (96px) | **Sem desvio** — idêntica à escala global (4, 8, 12, 16, 24, 32, 48, 64, 80, 96px). |
| Radius | `sm` 6px (botão/input) · `md` 10px (card) · `lg` 14px (superfícies maiores) · `full` 999px (pill/badge) | Banco global vazio nessa categoria. Herdado de `tokens.json`. Diferenciado por hierarquia — nunca um raio único em tudo (ver AI-slop check abaixo). |
| Shadow | `inset-highlight` (realce sutil) · `elevated` (modal/popover) · `glow-accent` (estado ativo) · `focus-ring` (foco de teclado) | Banco global vazio nessa categoria. Herdado de `tokens.json`. UI escura evita sombra pesada tipo `rgba(0,0,0,.1)` genérica — usa glow/inset, conforme nota do próprio `tokens.json`. |
| Breakpoints | 320/375/390/430/768/1024/1280/1440+ | **Sem desvio** — idêntico ao padrão global. |
| Motion *(revisado 2026-10-09, exceção pontual — ver nota abaixo)* | Duration: 160-250ms discretas (padrão global) + scroll-scrub síncrono ao scroll onde houver parallax · Easing: `ease-out` em toda entrada, `ease-in-out` em transição, sem spring (ver Movimento e interação abaixo) · **Intensity: Strong** em 2 pontos específicos (parallax) + **Medium** (scroll-reveal) nas demais 8 seções · Movement: Fade + Slide em todas as seções, Parallax restrito a 2 camadas (ver abaixo) | **Desvio do default calibrado por nicho.** O default pro ICP desta página (PME B2B sóbria, decisor único) seria Subtle, conforme a própria tabela do banco global. Desvio pedido pelo Lucas (2026-10-09): esta página específica não é só uma conversão pra PME — é a **vitrine da própria Neovertix**, vista por um prospect avaliando "essa agência constrói coisa impressionante?". A audiência que julga o *craft* da página não é o mesmo ICP sóbrio que julga o *tom* da copy — por isso o léxico/voz continuam sóbrios (nenhuma mudança na seção Tom), só a intensidade de movimento sobe. **Registrado como exceção pontual deste projeto — não muda a calibração geral do banco `design-tokens-globais.md` (Subtle continua o default de qualquer projeto futuro com ICP B2B sóbrio padrão).** |

**Pendência pro Lucas (não decido isso sozinho):** estes tokens são a identidade travada da Neovertix, não um padrão genérico de cliente — não promovi nada para `Web OS/bancos/design-tokens-globais.md` nesta rodada porque cor/tipografia aqui são *marca específica*, não padrão reutilizável entre clientes futuros (só a escala de espaçamento e os breakpoints já batem 1:1 com o global, sem ação necessária). Se o Lucas quiser que o espaçamento/radius/shadow desta marca vire o default do Web OS mesmo assim, isso é uma decisão explícita dele, não inferida aqui.

## Performance budget (acrescentado 2026-10-09; revisado no mesmo dia após subir Intensity pra Strong)

Declarado antes do módulo 22 começar — todo efeito visual proposto nesta spec precisa caber aqui, senão corta antes de chegar no build. Limiares não mudam com a Intensity (são os mesmos que o módulo 23 audita depois); o que muda é como o orçamento é gasto:

- **LCP < 2,5s** — página continua 100% tipográfica (zero imagem hero a orçar). Risco novo com Strong: o H1 do Hero não pode depender de JS pra aparecer — elemento do LCP precisa estar visível via CSS puro desde o primeiro paint; a entrada animada (opacity/translateY) só pode partir de um estado que já reserva o espaço e nunca pode ficar invisível além de ~150ms se o GSAP atrasar (fallback: conteúdo visível por padrão, JS só adiciona o estado inicial oculto depois de confirmar que carregou — nunca o inverso). GSAP core + ScrollTrigger + Lenis (~45-70KB combinados, gzip) carregam com `defer`, nunca bloqueando o parse do HTML/CSS.
- **INP < 200ms** — todo listener de scroll usa o ticker do GSAP/Lenis (passivo, `transform`/`opacity` só — nunca propriedade de layout), pra não travar a thread principal durante um toque/clique no meio de um scroll.
- **CLS < 0,1** — todo elemento com scroll-reveal reserva o espaço de layout desde o carregamento (oculto via `opacity`, nunca via `display:none`/`height:0`); nenhuma reflow quando a animação dispara.
- **Orçamento de animação por seção** (Passo 2a-bis exige consciência por seção, não orçamento único genérico):

| Seção | Animação orçada |
|---|---|
| Hero | Entrada orquestrada (eyebrow→H1 stagger→CTA) + parallax camada 1 (glow de fundo, baixo custo: 1 elemento, só `transform`) |
| Problema | Scroll-reveal simples (fade+slide curto) |
| Como funciona | Scroll-reveal + parallax camada 2 (trilho entre os 3 passos, scrub síncrono — maior custo da página, mitigado por ser só `transform` em 1 elemento) |
| Oferta | Scroll-reveal simples |
| Garantia Vértice | Scroll-reveal simples — **sem** contador numérico animado (ver nota em Movimento e interação) |
| Objeções | Scroll-reveal com stagger entre os 4 itens |
| Programa Fundador | Scroll-reveal simples |
| CTA final | Scroll-reveal simples |

Nenhuma seção ganha mais de 1 efeito simultâneo. Os 2 parallax (Hero e Como funciona) são o teto da página — não adicionar um terceiro sem revisar este orçamento de novo.

## Trust Architecture (acrescentado 2026-10-09)

Evidência antes de promessa, por seção — nenhuma delas depende de depoimento (que não existe ainda):

| Seção | De onde vem a confiança |
|---|---|
| Como funciona | Mecanismo exposto passo a passo (lê → consulta CRM → responde) — clareza do processo, não afirmação genérica. *(2026-10-09: o parallax/scrub desta seção — ver Movimento e interação — reforça essa evidência, não substitui; a animação segue a sequência real, não decora em cima dela.)* |
| Garantia Vértice | Risco invertido: métrica combinada + devolução de 30% — garantia é a prova, não o depoimento |
| Objeções | Resposta direta às 4 objeções reais do ICP, não genérica |
| Programa Fundador | Vaga limitada enquadrada como real/temporária (3-5), nunca contador falso |
| Rodapé (implícito, cobrir no módulo 22) | Contato real do Lucas, não "equipe" — reforça arquétipo Cara Comum |

## Tom e estrutura

**Tom** (herdado de `brandbook.md` §3 + `estrategia.md` §6):
- Direto, técnico sem jargão, honesto sobre onde a Neovertix está ("somos novos — e é por isso que o risco é nosso"), sóbrio — nunca gritado, orientado a número real (nunca inventado).
- Arquétipos: **Mágico** (antes/depois do fluxo manual→automático, sempre demonstrado via mecanismo, nunca só afirmado) + **Cara Comum** (o Lucas aparece como pessoa e autor do código — zero "nossa equipe", zero linguagem corporativa).
- Léxico obrigatório: vértice · construímos · roda sozinho · responde em [tempo] · mecanismo · fluxo · testado — não prometido · entrega.
- Léxico banido (bloqueio duro): revolucionar · turbinar · o futuro chegou · funcionário digital que não dorme · disruptivo · sinergia · potencializar · ecossistema · game changer · "vale por N humanos".
- Regra visual herdada: **nada de ícone de robô**, zero gradiente azul-roxo, tipografia carregando mais peso que cor.

**Estrutura de seções** — adaptada da lista completa de 11 (Hero/Problema/Solução/Benefícios/Como funciona/Diferenciais/Prova/Oferta/Objeções/FAQ/CTA final) para uma landing page de conversão de **1 oferta única** (Piloto Vértice), conforme `estrategia.md` §1 ("CTA primário único, sem CTA secundário competindo") e `icp-web.md` ("página de conversão rápida, baixo compromisso"):

1. **Hero** — headline + subheadline + CTA único (agendar demo) + microcópia de baixo risco.
2. **Problema** — a dor específica (lead esfriando, dono vendo mensagem não respondida à noite). Substitui "Problema" da lista completa; Diferenciais/Benefícios ficam **fundidos aqui e no Hero** (não ganham seção própria — página curta, 1 oferta, decisor único, não precisa repetir o mesmo argumento 3 vezes).
3. **Como funciona** (= "Solução" + "Como funciona" da lista completa fundidos) — mecanismo em 3 passos reais: lê a mensagem → consulta o CRM → responde.
4. **Oferta** — Piloto Vértice: escopo (1 canal, atendimento IA *ou* SDR IA, CRM simples), preço (R$ 1.900 / R$ 900 Fundador), prazo (2–4 semanas).
5. **Garantia Vértice** — bloco próprio, métrica combinada + devolução de 30%. Funciona como a seção "Prova" desta página — ver nota abaixo.
6. **Objeções** — as 4 objeções obrigatórias de `estrategia.md` §3, resposta direta cada. Substitui "FAQ" genérico — são objeções nomeadas, não perguntas soltas.
7. **Programa Fundador** — vaga limitada (3–5), enquadrada como oportunidade temporária real, nunca como desconto permanente.
8. **CTA final** — repetição do único CTA (agendar demo) + microcópia.

**Seção "Prova" explicitamente omitida como bloco de depoimento/case:** `estrategia.md` §8 pendência 2 registra "zero prova social própria (sem case, sem depoimento)" — regra de veracidade do Web OS proíbe inventar depoimento/cliente/resultado. A prova desta página vem do **mecanismo demonstrado** (seção 3) e da **Garantia Vértice** (seção 5, risco invertido), não de depoimento. Quando o Programa Fundador fechar vagas com caso de uso real, uma seção de Prova entra como v2 — não antes.

**Copy final não é desta etapa:** headline/subheadline exatos dependem da pendência #4 em aberto (`estrategia.md` §8 — tagline comercial "em iteração" vs. "Escala sem contratar" oficial). Esta spec define estrutura, tom e tokens — não resolve a tagline. Build (módulo 22) não deve travar nisso: usar placeholder `[headline — aguarda decisão Lucas/Tese]` até resolver.

## Inventário de componentes

`Web OS/bancos/componentes-aprovados.md` está vazio — este é o primeiro projeto do Web OS, não há nada pra reaproveitar de lá ainda. Toda linha abaixo é construção custom. Dois primitivos já vêm prontos do **brandkit da Neovertix** (`tokens.css`), não do banco Web OS: `.nv-btn` (botão) e `.nv-card` (card) — uso como base, não do zero.

| Seção | Reaproveitar de `componentes-aprovados.md`? | Construir custom |
|---|---|---|
| Hero | Banco vazio, nada a reaproveitar. | Eyebrow mono (uso único na página, não repetido por seção — ver nota AI-slop) + H1 display + body-lg subheadline + CTA primário (base `.nv-btn--primary`) + microcópia de baixo risco abaixo do botão. |
| Problema | Banco vazio. | Bloco de texto único (headline curta + body), sem ícone, sem ilustração — não há pipeline de imagem pronto nesta rodada (ver abaixo). |
| Como funciona | Banco vazio. | Lista numerada de 3 passos, dígitos em mono — numeração **justificada** porque o conteúdo é de fato sequencial (o mecanismo real, não decoração). |
| Oferta (Piloto Vértice) | Banco vazio. | Card (base `.nv-card`) com escopo + preço + prazo em destaque. |
| Garantia Vértice | Banco vazio. | Bloco com borda `border-strong` (não accent — accent já está no CTA) + o número "30%" em accent como único dado em destaque da seção (orientado a número, não decoração). |
| Objeções | Banco vazio. | 4 blocos pergunta→resposta estáticos, sem accordion — volume baixo (4 itens) não justifica interação de abrir/fechar (YAGNI). |
| Programa Fundador | Banco vazio. | Faixa com vagas (3–5) enquadradas como reais e temporárias — sem contador regressivo falso (não há deadline real pra mostrar). |
| CTA final | Banco vazio. | Repetição do CTA primário + microcópia — mesmo componente do Hero, não um novo. |

Se esta página for construída e funcionar, os 8 componentes acima são candidatos a `Web OS/bancos/componentes-aprovados.md` — **promoção só acontece com confirmação explícita do Lucas** (regra do módulo), não nesta etapa.

### Direção visual deliberada (`frontend-design`, plugin oficial `claude-plugins-official`)

Decisões tomadas pra não ler como template genérico, verificadas contra a lista de "tells" de design gerado por IA:

- **Hero alinhado à esquerda, não centralizado** — evita o default "texto centralizado sobre gradiente" apontado como tell comum; também escaneia melhor numa página de conversão com decisor único.
- **Sem palavra isolada destacada em cor/itálico/bold dentro do H1** — outro tell comum listado; o peso visual vem da hierarquia tipográfica (Chakra Petch bold vs. Manrope), não de pintar uma palavra.
- **Eyebrow mono usado uma única vez na página inteira (Hero)**, não repetido como label ALL-CAPS acima de cada seção — mesmo os tokens definirem um estilo `overline` reutilizável, usar em todo título é o tell "tracked-out ALL-CAPS eyebrow acima de cada heading". Reservado pro eyebrow técnico que já tem função própria na marca (`brandbook.md`: "reforça o pilar engenharia, não slide").
- **Numeração em "Como funciona" é a única numeração da página** — não decoro outras seções com 01/02/03 porque Oferta/Objeções/Garantia não são sequência.
- **Radius diferenciado por hierarquia** (sm botão/input, md card, lg superfície maior) — evita o "SaaS-card kit" (um raio só em tudo).
- **Sombra como glow/inset sobre navy, nunca `rgba(0,0,0,.1)` genérica** — já vem assim do próprio `tokens.json`, mantido.
- **Sem gradiente azul-roxo e sem ícone de robô** — regra herdada diretamente de `estrategia.md` §6, confirmada aqui.
- **Sem seta "→" decorativa anexada ao texto do CTA** — botão diz exatamente a ação ("Agendar demo"), voz ativa, sem ornamento.

### Movimento e interação (`emil-design-eng`)

**Revisão 2026-10-09 — Intensity subiu de Subtle pra Strong, exceção pontual deste projeto.** Decisão do Lucas, não inferida por mim: o default calibrado pelo ICP de conversão (`icp-web.md` — PME B2B sóbria, decisor único) continuaria Subtle, e é isso que vale pra qualquer projeto futuro com esse mesmo perfil. Esta página específica, porém, acumula um segundo papel que o ICP de conversão não cobre: ela é a **vitrine de capacidade de build da própria Neovertix**, olhada por quem está avaliando se a agência "constrói coisa impressionante" antes de confiar o próprio projeto a ela — uma audiência de craft, não de tom. Por isso: **a voz/léxico/estrutura de copy não mudam em nada** (seção Tom e estrutura intacta, sóbria) — só o orçamento de movimento sobe, e só nos dois pontos abaixo onde isso tem função, não decoração.

**Motor: GSAP + Lenis** (padrão de todo projeto Web OS desde 2026-10-09 — não é CSS improvisado em nenhuma Intensity). Com Strong, Lenis assume o scroll smoothing da página inteira (não só o Hero) e ScrollTrigger passa a orquestrar reveal por seção + os 2 parallax abaixo.

**Onde entra scroll-reveal (Medium, todas as 8 seções) — com variação por seção, não o mesmo tratamento repetido:**

| Seção | Reveal | Função |
|---|---|---|
| Hero | Não é scroll-reveal (já visível no load) — ver entrada orquestrada abaixo | Primeira impressão não pode depender de scroll |
| Problema | Fade + slide curto (translateY 8px→0, 300ms ease-out) | Dar 1 pausa de leitura antes do mecanismo |
| Como funciona | Reveal por passo, sincronizado com o scrub do parallax (ver abaixo) — não é um fade genérico | Literalmente demonstra a sequência do mecanismo — função explicativa, não decorativa |
| Oferta | Fade + slide curto | Pontuar o momento de preço/escopo |
| Garantia Vértice | Fade + slide curto — **sem contador numérico subindo até 30%**: a garantia é um limiar fixo, não uma métrica que "cresce"; animar como se fosse crescendo distorceria o que o número significa (risco de veracidade, não só estética) | Reforça o risco invertido sem fingir dinamismo que não existe |
| Objeções | Stagger entre os 4 itens (~60ms entre cada, fade+slide) | Pacing de leitura — evita parede de texto |
| Programa Fundador | Fade + slide curto | Pausa visual antes do CTA final |
| CTA final | Fade + slide curto, reusa o componente do Hero | Fecha o espelhamento com a abertura |

**Onde entra parallax real (Strong) — só 2 camadas, nada mais:**

1. **Hero → Problema**: glow de fundo (radial, cor accent-dim, já tokenizado) atrás do H1 se move a ~0,4x da velocidade do scroll enquanto o usuário desce do Hero pro Problema. Função: **criar continuidade entre seções** (uma das funções explicitamente permitidas pela regra de propósito do módulo 21) — a página não "corta" de uma seção pra outra, ela tem profundidade espacial.
2. **Como funciona**: a trilha/linha que conecta os 3 passos numerados se move em velocidade diferente do texto dos passos (scrub: true, atado à posição do scroll, não a uma duração fixa). Função: **explicar** — o movimento da trilha reforça visualmente que é uma sequência acontecendo, não 3 cards soltos.

Nenhum outro elemento ganha parallax — Oferta/Garantia/Objeções/Programa Fundador são momentos de decisão/leitura, e movimento de fundo ali teria custo de atenção sem função (mesmo em Strong, a regra "toda animação cumpre 1 função" continua valendo — Strong manda escopo, não dispensa).

**Decisões que não mudam com Strong** (não empilhadas com outra skill de "taste" na mesma decisão):

- **Sem spring/bounce em nenhum elemento, mesmo em Strong.** Importante não confundir: Strong aqui significa mais coreografia de scroll (parallax/scrub), não playfulness. Spring/bounce comunicaria um tom brincalhão que contradiz o arquétipo Cara Comum e a voz sóbria — isso não mudou, só o escopo de scroll mudou.
- **Botões** (CTA primário/secundário): `transform: scale(0.97)` em `:active`, `transition: transform 160ms ease-out`. Hover já definido em `tokens.css` (`background-color .15s ease`), mantido sem alteração.
- **Foco de teclado**: `--nv-focus-ring` (já tokenizado) em todo elemento interativo — nunca remover outline sem substituto visível.
- **Card de Oferta**: ainda sem hover de elevação — o card não é clicável (o CTA dentro dele é); isso não muda com Strong, continua sem função.
- **`prefers-reduced-motion: reduce`**: com Strong isso importa mais, não menos — reveal vira opacity-only (sem translateY), e os 2 parallax desligam completamente (ficam estáticos na posição final), nunca só "mais lento". O usuário entende 100% do conteúdo com todo movimento desligado — regra de acessibilidade do emil-design-eng, não negociável independente de Intensity.
- **Progressive enhancement**: com motor GSAP/Lenis real e mais pontos de animação, a exigência de "funciona com JS desligado" (banco de Motion Tokens) fica mais importante de testar no módulo 22, não menos — todo conteúdo revelado por scroll-reveal precisa estar presente e legível no HTML/CSS base, só a entrada que depende de JS.

## Pipeline de imagem

**Pendência — não resolvida nesta rodada**, por instrução explícita deste teste (não há produto físico nem é o foco deste teste de pipeline).

- Produto físico real? **Não.**
- Moodboard de estilo aprovado? **Não** — nenhuma sessão de moodboard rodada ainda.
- Direção provisória proposta (não é decisão final de imagem, é só a hipótese de trabalho pro módulo 22 não ficar travado): página 100% tipográfica + tokens de UI (diagrama dos 3 passos do mecanismo em texto/mono, sem foto nem ilustração de estoque) — coerente com o pilar "engenharia, não slide" (mostrar o mecanismo em texto/diagrama, não em imagem genérica de IA/robô, que é banida). Se o Lucas quiser imagem real em algum momento (ex: foto do Lucas, screenshot real do CRM/fluxo rodando), isso volta como moodboard com imagem-âncora antes de qualquer prompt, conforme o módulo pede.
- `images.md` não foi criado nesta rodada — não há prompt nenhum a registrar ainda.

## Checklist de aprovação

- [ ] Aprovado pelo Lucas em: {data}

**Sem essa marcação, o módulo 22 (Constrói) não inicia.**
