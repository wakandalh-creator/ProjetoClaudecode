# Design Tokens Globais (Web OS)

Banco reutilizável entre projetos — cada site herda daqui e só desvia com motivo registrado em seu próprio `specs/design.md`. Populado pelo Molda (módulo 21) conforme os projetos avançam; nasce vazio, nunca com valor inventado pra parecer mais avançado do que está.

## Color

| Token semântico | Valor | Projetos que usaram |
|---|---|---|
| — | — | — |

## Typography

| Token semântico | Valor | Projetos que usaram |
|---|---|---|
| — | — | — |

## Spacing

Escala base: 4, 8, 12, 16, 24, 32, 48, 64, 80, 96 (px). Ajustes por projeto registrados aqui quando promovidos a padrão global.

## Radius

| Token semântico | Valor | Projetos que usaram |
|---|---|---|
| — | — | — |

## Shadow

| Token semântico | Valor | Projetos que usaram |
|---|---|---|
| — | — | — |

## Breakpoints

Padrão: 320, 375, 390, 430, 768, 1024, 1280, 1440+ (px) — mobile-first, nunca só encolher o desktop.

## Motion (acrescentado 2026-10-09, a partir de adendo do Lucas; política de default revisada no mesmo dia)

Vocabulário de movimento — existe pra toda animação do projeto citar um valor daqui em vez de inventar número solto. **GSAP + Lenis são o motor padrão de todo projeto Web OS** (não mais opcional) — toda landing page sai com animação feita por engine de verdade, não CSS improvisado, garantindo o mesmo piso de qualidade técnica de movimento independente do cliente/nicho. ScrollTrigger entra conforme a Intensity abaixo. Funcionam em JS puro via `<script>`, não exigem React, cabem na stack HTML+CSS do Web OS como progressive enhancement (o site funciona com JS desligado — regra de acessibilidade continua valendo).

**A Intensity controla QUANTO movimento, não SE a ferramenta é usada**: todo projeto usa GSAP+Lenis; a diferença entre Subtle e Cinematic é a quantidade/escopo de animação, calibrada por nicho (Passo 2 do módulo 21, a partir do ICP em `estrategia.md`) — não é "todo site igual" (contradiria a seção 20 do doc-fonte, que recomenda nível de experiência Awwwards sem cara de agência criativa pra todo nicho).

| Categoria | Valores padrão |
|---|---|
| Duration | 100ms (micro) · 200ms (padrão) · 300ms (transição de seção) · 500ms (entrada de bloco) — acima de 500ms só com justificativa |
| Easing | `ease-out` (padrão pra entrada) · `ease-in-out` (padrão pra transição) · spring só quando o tom da marca permitir brincalhão (registrar por quê) |
| Intensity | **Determina o escopo de ScrollTrigger, calibrado por nicho**: Subtle = entrada no Hero + micro-interação de botão, sem scroll-trigger por seção (nicho B2B sóbrio/institucional) · Medium = scroll-reveal por seção, sem pinning (maioria dos projetos) · Strong/Cinematic = pinning/scrubbing/parallax real (só nicho visual-first — ex: criador de conteúdo, produto físico premium; exige justificativa no `specs/design.md` citando o ICP que sustenta essa escolha) |
| Movement | Fade · Slide · Scale — vocabulário base. Rotate/Blur/Parallax/Morph só quando a seção de fato pede (nunca decorativo) |

**Regra de propósito (obrigatória, não é token mas governa o uso de todos acima)**: toda animação precisa cumprir pelo menos 1 função — orientar, explicar, confirmar, gerar emoção com intenção, criar continuidade entre seções, ou ajudar conversão. Se não cumprir nenhuma, não entra. `prefers-reduced-motion: reduce` sempre respeitado — o usuário precisa entender o que a empresa faz com toda animação desligada.
