# Progresso — Web OS (Neovertix)

> Checklist por sprint, conforme o plano aprovado (`C:\Users\lucas\.claude\plans\neovertix-web-os-cached-key.md`). Marcar aqui a cada fase concluída, com evidência do teste real.

## Sprint 1 — Núcleo: squad + brain de projeto + pipeline discovery→design→build→launch→QA

**Status: 🔧 Scaffoldado em 2026-10-08, ainda sem teste ponta a ponta**

- [x] Estrutura de pastas `Web OS/` (`_context`, `_sop`, `_templates`, `modules`, `bancos`, `producao`)
- [x] `run.md` orquestrador com índice completo dos módulos 20-43
- [x] 9 agentes novos em `.claude/agents/` (molda, constroi, eixo, guia, convence, busca, blinda, evolui, multiplica)
- [x] 3 agentes estendidos (tese, radar, mede — seção "Extensão" acrescentada, comportamento original pra Social mídia IA preservado)
- [x] Seção Org Chart + regra de roteamento + linha de gate no `CLAUDE.md` raiz
- [x] `config/business.json` — nota de escopo acrescentada (Vértice Full → Web OS)
- [x] Gate de aprovação `_sop/aprovacao-publicacao.md` (campos ortogonais status/aprovado) + `_sop/checklist-qa-final.md`
- [x] `_context/identidade-web-os.md` + `_context/icp-web.md`
- [x] `bancos/design-tokens-globais.md` + `componentes-aprovados.md` (ativos, vazios) + `landing-pages-concorrentes.md` + `copy-frameworks-validados.md` (pendentes, Sprint 2/3)
- [x] `_templates/` — os 3 arquivos do "cérebro" de projeto (CLAUDE.md/specs-design/memory)
- [x] Módulos 20-24 escritos por completo, com skills verificadas uma a uma (não só citadas por nome)
- [ ] **Teste ponta a ponta** — ainda não rodado nenhum projeto real pelo pipeline completo (20→21→22→23→24)
- [ ] Confirmar que o gate de aprovação recusa deploy em produção sem `aprovado: true`

### Nota sobre as skills

A 1ª versão do plano citou skills só pelo nome, sem verificar conteúdo — o Lucas pegou isso e pediu verificação real. Dois exploradores confirmaram o conteúdo de cada skill citada no Sprint 1; achados: `positioning-statement`, `a11y-audit` e `ship-gate` não existem como skill instalada (substituídas/removidas), `impeccable` é na verdade `impeccable-design-polish`, `performance-diagnosis` é sobre campanha de anúncio (não performance web — removida). Detalhe completo no plano aprovado.

### Decisão pendente do Lucas

Rodar o primeiro projeto de teste pelo pipeline Sprint 1 pra validar o fluxo ponta a ponta antes de considerar o Sprint 1 realmente concluído (não só escrito).

---

## Sprint 2 — Arquitetura de Informação, Copy & CRO, Content Engine

**Status: não iniciado** — módulos 25 (Guia), 26 (Convence), 27 (Multiplica) reservados no índice, sem conteúdo.

## Sprint 3 — Pesquisa de Mercado Web, SEO, SEO Local, AEO, GEO

**Status: não iniciado** — módulos 28 (Radar-ext), 29-32 (Busca) reservados.

## Sprint 4 — Analytics, Tracking, CRM, Atribuição, Monitoramento

**Status: não iniciado** — módulos 33-36 (Mede-ext) reservados.

## Sprint 5 — Security/LGPD, Growth/Experimentação, Scores, Escala

**Status: não iniciado** — módulos 37-41 (Blinda, Evolui, Eixo) reservados.

## Sprint 6 — Niche System, Template Engine

**Status: não iniciado** — módulos 42-43 (Eixo, Constrói) reservados.
