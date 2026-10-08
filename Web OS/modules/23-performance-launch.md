# Módulo 23 — Performance & Launch (agente: Constrói)

## Objetivo

Exportar, hospedar e auditar o site construído no módulo 22, fechando um loop de otimização até a performance estar em nível aceitável, e registrar um rascunho leve do plano 30/60/90.

## Entrada

`producao/sites/{slug}/build/` com os 3 checklists do módulo 22 preenchidos.

## Contexto obrigatório

1. `build/` do projeto (módulo 22).
2. `Web OS/_sop/aprovacao-publicacao.md` — deploy em domínio público real só roda com `aprovado: true` em `projeto.md`; preview/staging roda livre.

## Instrução

### Passo 0 — Pré-requisito único por projeto

Rodar `setup-deploy` uma vez por projeto (detecta a plataforma — Vercel/Netlify/Fly/Render/etc. — e grava a configuração pra `land-and-deploy` rodar sozinho depois). Não é repetido a cada launch, só na primeira vez.

### Passo 1 — Export e compressão

Imagens em WebP/AVIF, CSS/JS minificados, lazy loading em imagens abaixo da dobra.

### Passo 2 — Deploy

Invocar `land-and-deploy` (merge → deploy → canary de verificação pós-deploy com diff de screenshot contra baseline) — é o executor real do deploy, não um documento de referência. Se a plataforma for Vercel, complementar com `vercel-deployment` pra decisões específicas (env vars, edge vs. serverless).

Registrar a URL publicada em `projeto.md`.

**Preview/staging roda sem o gate de aprovação. Deploy em domínio público real exige `aprovado: true` — conferir `_sop/aprovacao-publicacao.md` antes.**

### Passo 3 — Auditoria

Invocar `web-quality-audit` pra rodar a auditoria completa (performance + acessibilidade + SEO + boas práticas, 150+ checks). Usar `core-web-vitals` como referência específica pra corrigir qualquer problema sinalizado em LCP/INP/CLS.

### Passo 4 — Loop de otimização

Ponto fraco encontrado na auditoria → volta pro build (módulo 22, se for um problema de código) → re-otimiza → re-deploy → re-audita. Repetir até não haver mais blocker.

### Passo 5 — Plano 30/60/90 (rascunho)

Escrever `plano-30-60-90.md`: fundação 0-30 já coberta pelo Sprint 1; otimização 31-60 e escala 61-90 registradas como intenção, marcadas explicitamente "depende do Sprint N" nos pontos que dependem de módulos ainda não escritos (CRO, SEO avançado, analytics).

## Saída

`qa/auditoria-lighthouse.md` + `plano-30-60-90.md` + URL publicada registrada em `projeto.md`.

## Regras

- Nunca lançar em produção sem rodar a auditoria pelo menos 1 vez.
- `performance` (skill de referência genérica) fica de fora — redundante com `core-web-vitals`, que é mais acionável.
- `performance-diagnosis` fica de fora — verificado que é sobre diagnóstico de campanha de anúncio (CPL/criativo/oferta), não performance de página web. Erro de nome parecido já descartado na fase de planejamento.
