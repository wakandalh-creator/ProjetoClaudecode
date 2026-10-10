# QA de Acessibilidade — Piloto Vértice (teste-piloto-vertice)

> Módulo 22, Passo 4. Referência de implementação: WCAG 2.2 Level AA (skill `accessibility`).
> Ambiente desta sessão não tem ferramenta de navegador/screen-reader real — a verificação
> abaixo é estática (código-fonte, cálculo de contraste, validação de estrutura via Node),
> não um teste manual com NVDA/VoiceOver/Lighthouse real. Marcado onde isso importa.

## Checklist do módulo 22 (Passo 4)

| Item | Status | Nota |
|---|---|---|
| Contraste mínimo AA | ✅ Passa (calculado) | Ver tabela de contraste abaixo — todos os pares texto/fundo usados na página calculados via fórmula WCAG 2.1 (luminância relativa sRGB), não só herdados do token sem checar o uso real. |
| Alt text em toda imagem | ✅ N/A | Página 100% tipográfica (decisão do módulo 21 — "Pipeline de imagem"). Zero `<img>` no build (`grep` confirma: 0 ocorrências). Nada a fazer aqui ainda. |
| Navegação por teclado funcional | ✅ Passa (estático) | Skip link funcional (`href="#main"`, focável, visível só no foco). 3 instâncias do CTA (`<a class="nv-btn">`) são links reais, focáveis por padrão, sem `tabindex` negativo nem `div` fingindo de botão. Nenhum elemento interativo depende de mouse/hover só. |
| Foco visível | ✅ Passa (estático) | `:focus-visible` global em `a`/`button` com `box-shadow: var(--nv-focus-ring)` (token da marca, glow verde 3px) — nunca `outline: none` sem substituto. Aplicado a: skip link, 3 CTAs. |
| Labels em todo campo de formulário | ✅ N/A | Zero `<input>`/`<form>` nesta página (CTA é link de âncora pra seção de contato, não formulário). Nada a fazer aqui ainda — entra quando o canal de agendamento (pendência #5) tiver um formulário real. |
| Semântica HTML correta | ✅ Passa, com 1 bug corrigido nesta sessão | Ver "Bugs encontrados e corrigidos" abaixo — `<div>` solta dentro de `<ol>` era HTML inválido, corrigido. Hierarquia de heading verificada: 1 `<h1>`, 7 `<h2>` (1 por seção), `<h3>` só onde há subitem real (3 passos do mecanismo + 4 objeções) — sem salto de nível. |
| Área clicável mínima adequada | ✅ Passa | `.nv-btn` tem `min-height: 44px` (acima do mínimo WCAG 2.2 SC 2.5.8 de 24×24px CSS). Skip link tem padding suficiente pra não ficar abaixo de 24px mesmo sendo texto longo. |
| Mensagens de erro claras | ✅ N/A | Sem formulário, sem validação, nada a validar ainda. |

## Tabela de contraste (calculado nesta sessão, fórmula WCAG 2.1)

| Par | Contraste | Uso real na página | Exigência | Resultado |
|---|---|---|---|---|
| `text-primary` `#F5F7FA` / `bg-canvas` `#0A0E1A` | 17,94:1 | H1, H2, H3, corpo de texto padrão | AA normal ≥4,5:1 | ✅ AAA |
| `text-secondary` `#AAB4C2` / `bg-canvas` | 9,18:1 | Subheadline do Hero, `.body-lg` em todas as seções | AA normal ≥4,5:1 | ✅ AAA |
| `text-muted` `#7A8699` / `bg-canvas` | 5,22:1 | Microcopy de baixo risco, preço "de setup único", linha de contato do rodapé | AA normal ≥4,5:1 | ✅ AA |
| `accent` `#43A047` / `bg-canvas` | 5,83:1 | Eyebrow (mono), número "30%" da Garantia | AA normal ≥4,5:1 (eyebrow é texto pequeno) | ✅ AA |
| `accent-contrast` `#121A2E` / `accent` `#43A047` | 5,24:1 | Texto do botão CTA sobre fundo verde | AA normal ≥4,5:1 | ✅ AA |
| `border-strong` `#5A6780` / `bg-canvas` | 3,38:1 | Borda do bloco Garantia Vértice (não é texto — UI/non-text) | AA non-text SC 1.4.11 ≥3:1 | ✅ AA |

Nenhum uso de `border-subtle` (#18213A) ou `text-muted` sobre `surface-overlay` nesta página — as duas combinações de baixo contraste do token (documentadas como "reservar pra texto grande" no `tokens.json`) simplesmente não aparecem em nenhum componente construído. Não precisou de exceção.

## Bugs encontrados e corrigidos nesta sessão (QA ativo — não só relatório)

1. **HTML inválido: `<div class="mecanismo__trail">` direto dentro de `<ol>`.** `<ol>` só aceita `<li>` (e elementos de script) como filho direto — navegadores fazem recuperação de erro imprevisível nesse caso, o que quebraria o posicionamento absoluto da trilha de parallax. **Corrigido**: a trilha e a `<ol>` agora são irmãs dentro de um `<div class="mecanismo__wrap">` (que carrega o `position: relative`). Validado depois: parser de tags balanceado (script Node ad-hoc) não encontrou mais nenhum erro de aninhamento em `index.html`.
2. **Inconsistência de componente: CTA final não reusava a classe `.hero__cta`.** A spec pede que o CTA final "reuse o mesmo componente do Hero" — no HTML, o `<div>` que envolve botão+microcopy da seção final estava sem a classe, então o layout lado-a-lado (botão + microcopy) que entra a partir de 430px no Hero não se replicaria lá; ficaria sempre em coluna. **Corrigido**: classe `hero__cta` adicionada ao wrapper do CTA final.
3. **Desalinhamento da trilha de parallax ("Como funciona")**: o breakpoint ≥768px mudava `padding-left` tanto do `<ol>` quanto de cada `<li>`, deslocando a coluna dos números (01/02/03) pra longe do `left` fixo da trilha (`.mecanismo__trail`) — a linha de conexão ficaria visualmente desalinhada dos números que ela deveria conectar. **Corrigido**: removido o `padding-left` extra do breakpoint; a posição x dos números fica constante em todo breakpoint, e a trilha permanece alinhada. Isto não é um item do checklist de a11y em si, mas é exatamente o tipo de regressão visual que o QA ativo (skill `qa`) existe pra pegar antes do handoff — registrado aqui porque foi encontrado durante a mesma passada de verificação.
4. **Risco de conteúdo preso em `opacity:0` permanente** (achado ao aplicar o checklist do `impeccable-design-polish`: "reveal animations... don't gate content visibility on a class-triggered transition" — impressão/export em PDF ou qualquer renderização headless que não dispare scroll nunca cruzaria o `ScrollTrigger`, deixando a seção em branco). **Corrigido**: `@media print` força `opacity:1`/`transform:none` em todo `[data-reveal]`/`[data-hero-reveal]`. Decidi não adicionar um `setTimeout` global de "forçar visível depois de Nms" — isso brigaria com o próprio scroll-reveal pra quem lê a página em ritmo normal (seção ficaria "pop" visível antes do usuário rolar até ela), e o caso real que importa (impressão/headless) já fica coberto pelo `@media print`.

## Limitação desta rodada (registrada, não resolvida)

Esta verificação não incluiu teste manual com leitor de tela real (NVDA/VoiceOver/JAWS), nem teste de zoom a 400%, nem Lighthouse real rodado num navegador — o ambiente deste subagente não tem ferramenta de browser disponível. O que foi feito é 100% verificação estática: leitura de código, cálculo de contraste via fórmula WCAG, e um validador de balanceamento de tags/ids escrito ad-hoc em Node. Antes do handoff real pro módulo 23, recomendo rodar ao menos um passe com o Lucas usando um leitor de tela real e o Lighthouse do Chrome DevTools — essa parte do checklist ("QA visual direto com o Lucas") continua pendente, como já é esperado pelo próprio módulo 22 (Passo 3).
