# Design Spec — trial-vertice (slug provisório)

> Fonte única da verdade do design deste projeto. Gerado pelo Molda (módulo 21) a partir de `estrategia.md`, `references/notas-referencia.md`, `Web OS/bancos/design-tokens-globais.md` e `Web OS/bancos/componentes-aprovados.md`. **Precisa de aprovação explícita do Lucas antes do módulo 22 (build) começar** — ver seção Aprovação no fim, com a decisão específica que pede confirmação dele.
>
> **Revisão (atualização pós-protótipo):** depois da entrega original abaixo, Lucas e a sessão de protótipo iteraram diretamente num Artifact visual — decisão de cor/tipografia precisava ser vista, não só lida. O resultado final diverge bastante da proposta original nas seções **Color, Typography, Motion, Trust Architecture e Inventário de Componentes**, reescritas abaixo pra refletir a realidade. **Protótipo vivo (referência mais atual que qualquer descrição em texto): `https://claude.ai/code/artifact/e0537736-3314-4af9-837c-4e6bf1fab12e`.**
>
> Nota de método: a proposta original partiu do banco `design-tokens-globais.md` **vazio**. Na iteração com o Lucas, descobrimos que a Neovertix já tem um design system oficial e aprovado em `branding/neovertix/tokens.json` (formalizado a partir do logo final aprovado) — esse arquivo é a fonte de verdade de **cor** a partir desta revisão, não o banco global vazio.

## Referências analisadas

Ver `references/notas-referencia.md` pra contexto original (Awwwards/land-book/minimal.gallery, características gerais, sem screenshot individual). **Superado na prática pelo protótipo vivo** (link acima) e por uma referência de produto usada na iteração de cor: EasyPanel (fundo claro, texto quase-preto, botão verde sólido em pill) — usada como ponto de partida pras variações claras testadas, não copiada 1:1 (ver correção de contraste em Color).

## Contexto que molda as decisões abaixo

- **ICP não é tech/startup**: comércio local e PME (clínicas, concessionárias, imobiliárias, advocacia) — decisor único, não comitê, não é público que valoriza estética "SaaS do Vale do Silício". Isso pesa contra qualquer intensidade de motion alta e contra qualquer visual que pareça "ferramenta de dev". (Pendência 11b do brief de estratégia sobre validação do ICP continua aberta — não é deste módulo.)
- **Não existe Garantia Vértice aqui.** O mecanismo de confiança próprio é: instância própria por cliente + descarte automático se não comprar. Na versão final isso não é mais um bloco visual separado — virou um dos 4 passos do "Como Funciona" (ver Trust Architecture).
- **Lucas aparece como pessoa** (Cara Comum), mesmo sem vender por reunião.
- **Nenhuma alegação de segurança/LGPD/criptografia** — regra de veracidade mantida; ver nota sobre o ícone de cadeado/escudo em Trust Architecture.

---

## Tokens do projeto

### Color

**Mudança total em relação à entrega original.** A proposta de accent terracota (`#C1552E`) foi **rejeitada** — Lucas pediu "as cores da nossa logo". Fonte de verdade agora é `branding/neovertix/tokens.json` (sistema oficial, formalizado a partir do logo final aprovado), não o banco global vazio.

**Direção testada e descartada:** a paleta navy escura oficial do tokens.json (`bg.canvas #0A0E1A` + `accent.default #43A047`) foi montada num protótipo e **descartada por decisão do Lucas**. Registro aqui pra ninguém redescobrir/testar de novo sem saber que já foi avaliada — não é mais opção ativa.

**Estado atual — 2 variações claras testadas, nenhuma escolhida como definitiva** (pendência real, ver Aprovação). Lucas pediu pra testar direções claras usando como ponto de partida a referência EasyPanel (fundo claro, texto quase-preto, botão verde sólido em pill).

| Token | Cinza claro + verde | Branco + verde | Uso |
|---|---|---|---|
| `color.bg` | `#F6F6F4` | `#FFFFFF` | Fundo raiz da página |
| `color.panel` | `#FFFFFF` | `#FFFFFF` (separação só por borda/sombra — mesmo valor do bg nesta variação) | Cards, nav, inputs |
| `color.panel-raised` | `#EDEDEA` | `#F4F4F2` | Hover de card, superfície elevada |
| `color.ink` | `#121212` | `#121212` | Texto principal |
| `color.ink-soft` | `#5B5B58` | `#5B5B58` | Texto secundário |
| `color.ink-mute` | `#8A8A86` | `#8A8A86` | Texto terciário/placeholder |
| `color.border` | `#E5E5E1` | `#E5E5E1` | Divisores, contorno de card |
| `color.accent` | `#43A047` | `#43A047` | CTA, botão primário, único destaque saturado da página — verde oficial da seta do logo (`tokens.json → color.accent.default`) |
| `color.accent-hover` | `#2E7D32` | `#2E7D32` | Hover do botão — tom mais escuro, pensado pra fundo claro. **Desvio documentado do tokens.json**: o `accent.hover` oficial (`#66BB6A`, mais claro) foi pensado pra fundo escuro — não usar aqui. |
| `color.accent-text` | `#121A2E` (escuro) | `#121A2E` (escuro) | Texto sobre o botão verde — **nunca branco** |

**Correção de acessibilidade sobre a própria referência copiada:** a referência EasyPanel usa texto escuro sobre botão verde — testamos contraste e confirmamos que não é só estética, é necessário: branco sobre `#43A047` dá 3.3:1 (reprova WCAG AA pra texto normal); escuro (`#121A2E`) sobre o mesmo verde dá 5.2:1 (aprova). Isso coincide com o que o próprio `tokens.json` já havia calculado pra fundo escuro (`color.accent.contrast`) — aqui confirma que vale igual pra fundo claro.

**Regra de aplicação, ainda vale:** uma única cor de destaque saturada (`accent` verde) em toda a página — nunca duas cores saturadas competindo na mesma tela.

### Typography

**Mudança total.** O par Fraunces + Hanken Grotesk (proposta original) foi abandonado. Chakra Petch — fonte oficial de display do `tokens.json` — também foi testada e **não ficou** como escolha final. A versão final usa **Manrope como única família**, display e body.

| Token | Valor | Uso |
|---|---|---|
| `font.display` / `font.body` | Manrope (variável) | Toda a página — não há mais par serifado/grotesco, é tudo sans-serif Manrope |
| Peso em títulos de destaque (H1/H2/H3) | 800 | Hierarquia vem do peso dentro da mesma família, não de uma segunda fonte |
| Peso no corpo | 400–600 | Texto corrido, labels, botão |

Escala numérica de tamanho (12/14/16/20/25/31/39/49/61 px) da entrega original **mantida sem revisão nesta sessão** — ninguém testou/definiu uma escala nova no protótipo, só a família/peso mudaram.

**Tell evitado, ainda vale (ajustado o nome do token de cor):** eyebrow em ALL-CAPS repetido continua banido. Onde a página precisar de um rótulo pequeno acima de um título: Manrope 500–600 em caixa normal (sentence case) com uma linha/régua em `accent` (verde) ao lado — nunca caixa alta.

### Spacing

Escala 4/8/12/16/24/32/48/64/80/96 (px) — herdada sem desvio, sem mudança reportada no protótipo.

### Radius

| Token | Valor | Uso | Nota |
|---|---|---|---|
| `radius.sm` | 4px | Inputs, chips pequenos | Sem mudança reportada. |
| `radius.card` | **14px** | Cards, painéis (ambas as variações claras) | **Decidido no protótipo** — coincide com `radius.lg` do `tokens.json` oficial (14px). |
| `radius.button` | **pill (full-round)** | Botão primário | **Mudança em relação à entrega original**, que proibia pill explicitamente ("sem pill, 8px institucional"). A referência EasyPanel usa botão pill e o protótipo final adotou — registrado aqui como decisão nova, substitui a regra antiga. |

### Shadow

| Token | Valor | Uso | Nota |
|---|---|---|---|
| `shadow.card` | `0 2px 10px rgba(0,0,0,.05)` — bem suave | Estado padrão de card/painel (ambas as variações claras) | **Mudança em relação à entrega original**, que previa "sem sombra por padrão, só borda". No protótipo final há sombra suave por padrão, nunca pesada — sem sombra pesada em nenhum estado. |

### Breakpoints

320 / 375 / 390 / 430 / 768 / 1024 / 1280 / 1440+ (px) — herdado sem desvio, sem mudança reportada.

### Motion

Motor: **GSAP + Lenis** (padrão obrigatório de todo projeto Web OS, não é escolha deste projeto).

**A pergunta genérica "Intensity: Medium vs. Subtle" da entrega original foi substituída na prática.** O protótipo final não usa scroll-reveal genérico por seção — usa animações pontuais e funcionais, uma por módulo/seção, cada uma com propósito claro (confirmar que é real ou explicar o mecanismo), não decoração:

| Onde | Animação | Função |
|---|---|---|
| Aba "Agente de IA" (Módulos com abas) | Bolhas de conversa de WhatsApp aparecendo em sequência | Confirmar que é real, não mockup estático |
| Aba "Redes Sociais" (Módulos com abas) | Bolhas de conversa de Instagram aparecendo em sequência | Mesma função, outro canal |
| Aba "CRM de Vendas" (Módulos com abas) | Barras de "sinal" (urgência/orçamento) preenchendo quando o card aparece | Explicar o mecanismo de qualificação do lead |
| Aba "Conversões" (Módulos com abas) | Linha conectando "anúncio → lead" | Explicar o mecanismo de atribuição |

Fora dessas quatro, sem scroll-reveal genérico documentado no protótipo. `prefers-reduced-motion: reduce` continua respeitado — sem motion, cada painel segue legível só com o checklist em texto.

---

## Piso de craft (Passo 2a-bis) — checklist aplicado neste projeto

Mantido como estava na entrega original, com uma correção factual (os tokens de cor/radius/shadow mudaram, ver acima):

| Item do piso | Como este projeto cumpre |
|---|---|
| Zero marca de "IA genérica" | Sem gradiente, sem card de vidro, hero não é stack centralizado sobre gradiente — paleta clara cinza/branco + 1 accent verde (cores oficiais do logo via `tokens.json`), sem eyebrow ALL-CAPS repetido. **Nota de revisão:** a regra original "botão sem pill, sombra ausente por padrão" foi superada pela decisão do protótipo (botão pill, sombra suave por padrão — ver Radius/Shadow); os demais itens desta linha continuam valendo. |
| Micro-interação real em todo interativo | Sem mudança reportada no protótipo — mantida a intenção original (hover/foco/active visíveis em todo elemento interativo); detalhe fino é tarefa do módulo 22. |
| Motor de animação de verdade | GSAP + Lenis confirmados como motor deste projeto (não é opcional). |
| Tipografia com hierarquia deliberada | Ver Typography acima — hierarquia por peso dentro de Manrope, documentada. |
| Responsividade sem concessão | Teste real nos 8 breakpoints é item de QA do módulo 22, não opcional. |
| Performance dentro do budget | Ver Performance budget abaixo. |

---

## Performance budget (Passo 2b)

Limiares de auditoria (herdados, mesmos do módulo 23): **LCP < 2,5s · INP < 200ms · CLS < 0,1**.

Orçamento consciente deste projeto, **atualizado pra refletir Manrope como única fonte**:

- **Fontes**: 1 arquivo variável (Manrope), subset Latin + diacríticos PT-BR, self-hosted woff2 — menor custo que o par original de 2 famílias. Preload no peso usado pelo H1 (800).
- **Elemento de LCP**: a entrega original previa texto puro (H1) como LCP, sem imagem no Hero. **Atenção pro módulo 22/23**: o Hero final tem "2 cards lado a lado, cada um com uma 'tela' de produto emoldurada tipo navegador" — se isso for implementado como imagem/screenshot (em vez de HTML/CSS real), checar se não passa a competir com o H1 pelo LCP antes de publicar.
- **Motion**: GSAP core + Lenis + ScrollTrigger — mesmo pacote de custo padrão de todo projeto Web OS, sem biblioteca adicional. As 4 animações funcionais por aba (ver Motion) são pontuais, não scroll-reveal de página inteira — custo menor que a proposta original de Medium intensity.
- **Imagens** (telas de produto emolduradas, screenshots dos módulos — ver `images.md`): WebP/AVIF, responsive srcset, lazy-load abaixo da dobra. Meta: <150kb por imagem perto do hero, <80kb por imagem de apoio.
- **Sem vídeo** no escopo desta V1.

---

## Trust Architecture (Passo 3c)

**Mudança estrutural**: o bloco separado "Arquitetura de Confiança" da entrega original não existe mais como seção isolada — a resposta à objeção nº1 (conectar WhatsApp é seguro/simples) virou um dos 4 passos do "Como Funciona". Essa pendência pode ser fechada como **resolvida por integração**: não há mais necessidade de ícone de cadeado/escudo (a seção virou texto nos passos numerados), então a extensão da regra "zero ícone de robô" pra zero ícone de segurança não-declarada deixa de ser uma decisão isolada — simplesmente não há mais bloco onde esse ícone poderia aparecer.

Mapeamento atualizado promessa → evidência, pela estrutura final de página:

| Seção | Promessa | Evidência que vem antes (ou junto) |
|---|---|---|
| **Hero** | "Escala sem contratar" | 2 cards lado a lado (um por plano), cada um com uma tela de produto emoldurada tipo navegador — produto real visível, não mockup abstrato. **Se as telas incluírem as bolhas de conversa (WhatsApp/Instagram) do Motion**: precisa de conteúdo real, não transcrição inventada — mesma regra de veracidade da entrega original. |
| **Problema** | Custo de não automatizar | Os 2 números de custo (custo de SDR CLT, custo de lead perdido) como conta, não slogan — mantido da entrega original. |
| **Como Funciona (4 passos)** | "É rápido e seguro de ativar" | 4 passos numerados e honestos — um deles responde à objeção nº1 (conectar o canal real) só com texto, sem ícone de segurança/selo. |
| **Módulos com abas** | "O produto realmente faz isso" | Checklist + screenshot emoldurado tipo navegador por módulo (Agente de IA / CRM / Conversões / Redes Sociais), com legenda embaixo — padrão adaptado do site da Bolten (fornecedor white-label), **sem reusar os screenshots reais deles** (mostram a marca errada). |
| **Faixa de logos** | — | Marcada explicitamente como **ilustrativa, sem clientes reais ainda** — não é alegação de prova social. |
| **Diferenciais por vertical** | "Serve pro meu negócio específico" | Abas por segmento (Clínicas/Imobiliárias/Concessionárias/Advocacia/Comércio local) — especificidade em vez de alegação genérica. |
| **FAQ** | Respostas pontuais | Accordion nativo `<details>`, respostas factuais curtas. |
| **Quem Constrói (Lucas)** | "Alguém de verdade responde se travar" | Foto real do Lucas + bio — Cara Comum, nunca "nossa equipe". |
| **CTA final** | Repete o Hero | Mesma âncora factual do Hero. |

---

## Inventário de componentes (Passo 3)

`componentes-aprovados.md` segue vazio — nada pra reaproveitar ainda. Todo componente abaixo é **custom**; os bem-sucedidos entram como candidatos ao banco (promoção só com confirmação do Lucas, não automática).

**Estrutura de página final** (substitui o inventário da entrega original, baseado no brief anterior):

| Seção | Direção | Motion |
|---|---|---|
| **Nav** | Logo + 1 CTA, sem CTA secundário competindo. | Sem scroll-trigger documentado. |
| **Hero** | 2 cards lado a lado, um por plano, cada um com uma "tela" de produto emoldurada tipo navegador. | Ver Motion — se incluir bolhas de conversa, são as animações de WhatsApp/Instagram descritas acima. |
| **Problema** | 2 números de custo apresentados como conta, tipografia fazendo o peso. | Sem mudança reportada. |
| **Como Funciona** | 4 passos numerados — um deles absorve a resposta à objeção nº1, só com texto. | Sem animação específica documentada no protótipo além da revelação dos passos. |
| **Módulos com abas** | 4 abas (Agente de IA / CRM de Vendas / Conversões / Redes Sociais) — cada aba troca um painel com checklist + screenshot emoldurado tipo navegador e legenda embaixo. Padrão adaptado do site da Bolten, **sem reusar os screenshots reais deles**. | Uma animação funcional por aba — ver tabela em Motion. |
| **Faixa de logos** | Marcada explicitamente como ilustrativa, sem clientes reais ainda. | Sem motion documentado. |
| **Diferenciais por vertical** | Abas por segmento: Clínicas / Imobiliárias / Concessionárias / Advocacia / Comércio local. | Sem motion documentado além da troca de aba. |
| **FAQ** | Accordion nativo `<details>` — sem componente custom de accordion. | Comportamento nativo do navegador. |
| **Quem Constrói (Lucas)** | Bloco pequeno, foto real + bio curta, zero "equipe"/"nós corporativo" — mantido da entrega original. | Sem drama. |
| **CTA final** | Repete a âncora factual do Hero, mesmo botão primário. | Sem mudança reportada. |
| **Footer** | Não revisado na sessão de protótipo — mantido da entrega original: minimal, assinatura institucional + links, sem alegação de segurança/LGPD no corpo. | Sem motion. |

**Atenção nos breakpoints 320–430 (Passo 2a-bis):** segue valendo a regra geral de empilhar cedo (768 já vertical) e nunca usar tabela com scroll horizontal pra comparação de planos — sempre cards empilhados. Validar especificamente as abas de "Módulos" e "Diferenciais por vertical" em mobile (padrão de aba costuma precisar virar um padrão alternativo — select/accordion — abaixo de 768; não testado no protótipo, item de atenção pro módulo 22).

---

## Pipeline de imagem (Passo 4)

**Sem produto físico** — é um serviço. Sem mudança reportada no protótipo em relação à decisão original: a página continua text/componente-led onde possível, mas ver nota de atenção em Performance budget sobre as telas de produto emolduradas do Hero e os screenshots emoldurados dos Módulos com abas — esses sim são imagem-led e precisam de pipeline próprio.

Detalhe completo em `images.md`.

---

## Decisão que pede confirmação explícita do Lucas

1. **Qual das 2 variações claras vira a definitiva: cinza claro + verde ou branco + verde.** Lucas testou as duas e disse "deixa assim por enquanto" sem escolher — não foi decidido por ele ainda, e o Molda não decide isso no lugar dele.

## Aprovação

- [ ] Aprovado pelo Lucas em: {data}
