# Módulo 22 — Development & Build + QA Técnico/Acessibilidade (agente: Constrói)

## Objetivo

Construir o site a partir do `specs/design.md` aprovado, em HTML+CSS (stack padrão do Web OS), com QA técnico e de acessibilidade completos antes do handoff pro módulo 23 (launch).

## Entrada

`producao/sites/{slug}/specs/design.md` com `- [ ] Aprovado pelo Lucas` marcado.

## Contexto obrigatório (ler antes de construir)

1. `specs/design.md` do projeto (módulo 21) — fonte única de verdade de design.
2. `references/` e `images.md` do projeto.
3. `Web OS/bancos/componentes-aprovados.md` — componentes reutilizáveis já validados.

## Instrução

### Passo 1 — Plano de build

Plano de build completo antes de construir, derivado diretamente do `specs/design.md` aprovado. Nunca codar antes da aprovação existir.

### Passo 2 — Build

HTML semântico, componentes modulares, mobile-first. Testar em 320/375/390/430/768/1024/1280/1440px+ — nunca só encolher o layout desktop.

### Passo 3 — QA ativo

Invocar a skill `qa` — roda em 3 níveis (Rápido/Padrão/Exaustivo), testa, corrige bug encontrado no próprio código, commita cada correção atomicamente, reverifica. Combinar com QA visual direto com o Lucas (click-to-select no preview + anotação do problema).

### Passo 4 — Checklist de acessibilidade (obrigatório)

Contraste mínimo AA, alt text em toda imagem, navegação por teclado funcional, foco visível, labels em todo campo de formulário, semântica HTML correta, área clicável mínima adequada, mensagens de erro claras.

Invocar `accessibility` como referência de implementação WCAG 2.2.

### Passo 4b — Auditoria técnica + polimento + piso de craft

Invocar `web-quality-audit` (auditoria Lighthouse-style: performance, acessibilidade, SEO, boas práticas, com níveis de severidade). Em seguida, invocar `impeccable-design-polish` como passada final de polimento pré-handoff (modos Audit/Critique/Polish).

Checklist do piso de craft (módulo 21, Passo 2a-bis — não-negociável, independente de nicho/Intensity): zero tell de "IA genérica" · micro-interação (hover/focus/active) em todo elemento interativo, nenhum no default do navegador · GSAP+Lenis como motor de animação, nenhuma transição em CSS improvisado · hierarquia tipográfica deliberada · os 8 breakpoints testados de verdade, não só no preview · dentro do performance budget. Falhar qualquer item aqui bloqueia o handoff pro módulo 23 tanto quanto falhar a11y.

Não rodar `impeccable-design-polish` junto com `make-interfaces-feel-better` — cobrem o mesmo tipo de ajuste, é trabalho duplicado.

### Passo 5 — SEO técnico baseline

Title, meta description e H1 únicos por página; `sitemap.xml` e `robots.txt` básicos. Cobertura completa de SEO fica pro módulo 31 (Sprint 3) — aqui é só o piso técnico.

## Saída

`producao/sites/{slug}/build/` + `qa/acessibilidade.md`.

## Regras

- Nunca aprovar/avançar sem os 3 checklists preenchidos (QA ativo, a11y, auditoria técnica).
- Componente bem-sucedido é candidato a `Web OS/bancos/componentes-aprovados.md` — confirmar com o Lucas antes de promover.
- `frontend-patterns` fica de fora desta etapa — é específica de React/Next.js, stack errada pra um build HTML+CSS.
- Motion opcional (verificado, 2026-10-09): se o `specs/design.md` pedir animação disparada por scroll além do que CSS puro resolve, a skill `gsap-scrolltrigger` é real e de propósito geral (não confundir com a skill `gsap` sozinha, que é específica da ferramenta HyperFrames e não se aplica aqui). GSAP/ScrollTrigger/Lenis funcionam em JS puro via `<script>`, sem exigir React — cabem na stack HTML+CSS como progressive enhancement. Não é default; só entra se o `specs/design.md` justificar com a regra de propósito do motion token.
