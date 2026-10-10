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
| Motion *(acrescentado 2026-10-09)* | Duration: 160-250ms (padrão global) · Easing: `ease-out` em toda entrada, sem spring (ver Movimento e interação abaixo) · Intensity: Subtle em toda a página — nada de Strong/Cinematic, conflitaria com o tom sóbrio · Movement: Fade + Slide curto, sem Rotate/Blur/Parallax | **Sem desvio** — valores já batem com o padrão global (`bancos/design-tokens-globais.md`). |

**Pendência pro Lucas (não decido isso sozinho):** estes tokens são a identidade travada da Neovertix, não um padrão genérico de cliente — não promovi nada para `Web OS/bancos/design-tokens-globais.md` nesta rodada porque cor/tipografia aqui são *marca específica*, não padrão reutilizável entre clientes futuros (só a escala de espaçamento e os breakpoints já batem 1:1 com o global, sem ação necessária). Se o Lucas quiser que o espaçamento/radius/shadow desta marca vire o default do Web OS mesmo assim, isso é uma decisão explícita dele, não inferida aqui.

## Performance budget (acrescentado 2026-10-09, a partir de adendo do Lucas)

Declarado antes do módulo 22 começar — todo efeito visual proposto nesta spec precisa caber aqui, senão corta antes de chegar no build:

- LCP < 2,5s · INP < 200ms · CLS < 0,1 (mesmo limiar que o módulo 23 vai auditar depois).
- Página 100% tipográfica (ver Pipeline de imagem abaixo) — sem peso de imagem hero a orçar nesta rodada.
- Animação: só a entrada orquestrada do Hero (ver Movimento e interação) + micro-interação de botão. Nada de scroll-triggered nesta v1 — se entrar depois, é incremento sobre este orçamento, não substituição dele.

## Trust Architecture (acrescentado 2026-10-09)

Evidência antes de promessa, por seção — nenhuma delas depende de depoimento (que não existe ainda):

| Seção | De onde vem a confiança |
|---|---|
| Como funciona | Mecanismo exposto passo a passo (lê → consulta CRM → responde) — clareza do processo, não afirmação genérica |
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

**Motor: GSAP + Lenis** (padrão de todo projeto Web OS, revisado em 2026-10-09 — não é mais CSS puro improvisado, mesmo em Intensity Subtle). Intensity desta página: **Subtle** — ICP é PME B2B sóbrio, decisor único (`icp-web.md`), sem justificativa pra Medium/Strong (que exigiriam nicho mais visual). Subtle aqui significa escopo contido de ScrollTrigger (sem reveal por seção, sem pinning/parallax), não motor improvisado — o piso de craft (módulo 21, Passo 2a-bis) continua valendo igual a qualquer outro projeto: toda micro-interação é real, não default do navegador.

Decisões de easing/duração/spring aplicadas — não empilhadas com outra skill de "taste" na mesma decisão:

- **Um único momento orquestrado de entrada, no Hero**: eyebrow aparece (opacity 160ms ease-out) → linhas do H1 entram com stagger curto (translateY(8px)→0 + opacity, ~40ms entre linhas, ease-out, ≤250ms cada) → CTA aparece por último. Nenhuma outra seção tem animação de scroll-reveal por padrão — evita o "fade-and-slide-up em cada seção" que o próprio `frontend-design` marca como tell de IA.
- **Botões** (CTA primário/secundário): `transform: scale(0.97)` em `:active`, `transition: transform 160ms ease-out` — feedback de pressão imediato. Hover já definido em `tokens.css` (`background-color .15s ease`), mantido sem alteração.
- **Foco de teclado**: usar `--nv-focus-ring` (já tokenizado) em todo elemento interativo — nunca remover outline sem substituto visível.
- **Card de Oferta**: sem hover de elevação — o card em si não é clicável (o CTA dentro dele é); animar algo que não responde a uma ação do usuário não tem propósito, conforme o framework de decisão do emil ("should this animate at all?").
- **Objeções**: estático, sem transição — reforça o tom "sóbrio, não gritado".
- **Sem spring/bounce em nenhum elemento** — decisão deliberada: springs/bounce comunicam playfulness, que conflita com o tom sóbrio e o arquétipo Cara Comum da marca. Reservado pra nunca usar nesta página, a menos que o Lucas peça explicitamente.
- **`prefers-reduced-motion: reduce`** respeitado em toda a página — mantém opacity, remove transform-based motion (regra de acessibilidade do emil-design-eng, não negociável mesmo em teste de pipeline).

## Pipeline de imagem

**Pendência — não resolvida nesta rodada**, por instrução explícita deste teste (não há produto físico nem é o foco deste teste de pipeline).

- Produto físico real? **Não.**
- Moodboard de estilo aprovado? **Não** — nenhuma sessão de moodboard rodada ainda.
- Direção provisória proposta (não é decisão final de imagem, é só a hipótese de trabalho pro módulo 22 não ficar travado): página 100% tipográfica + tokens de UI (diagrama dos 3 passos do mecanismo em texto/mono, sem foto nem ilustração de estoque) — coerente com o pilar "engenharia, não slide" (mostrar o mecanismo em texto/diagrama, não em imagem genérica de IA/robô, que é banida). Se o Lucas quiser imagem real em algum momento (ex: foto do Lucas, screenshot real do CRM/fluxo rodando), isso volta como moodboard com imagem-âncora antes de qualquer prompt, conforme o módulo pede.
- `images.md` não foi criado nesta rodada — não há prompt nenhum a registrar ainda.

## Checklist de aprovação

- [ ] Aprovado pelo Lucas em: {data}

**Sem essa marcação, o módulo 22 (Constrói) não inicia.**
