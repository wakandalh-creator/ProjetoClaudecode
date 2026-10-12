# Web OS — Orquestrador

> Sistema de criação, lançamento, medição e evolução de sites e landing pages da Neovertix (e, no futuro, de clientes). Depende do `config/business.json` e de `branding/neovertix/` como fonte de posicionamento, e do squad `Social mídia IA/` pra 3 agentes compartilhados (tese, radar, mede). Gate não-negociável: `_sop/aprovacao-publicacao.md` — nada vai ao ar sem `aprovado: true` marcado pelo Lucas.

## Mapa do sistema

| Camada | Onde | O que faz |
|---|---|---|
| Posicionamento | `_context/`, `tese` (ext.) | Brief de negócio/ICP/oferta por projeto |
| Produção | `modules/` | Instruções passo a passo de cada etapa |
| Squad | `.claude/agents/` | Molda, Constrói, Eixo, Guia, Convence, Busca, Blinda, Evolui, Multiplica (novos) + Tese, Radar, Mede (estendidos) |
| Memória | `_context/`, `bancos/` | Identidade do sistema, ICP web, tokens/componentes/concorrência acumulados |
| Saída | `producao/sites/{slug}/` | Projeto individual: estratégia, design, build, QA, deploy |
| Gate | `_sop/` | Checklist QA Final + aprovação humana de publicação |

## Módulos

| # | Módulo | Agente | Skills previstas (verificadas, 2026-10-12) | Status |
|---|---|---|---|---|
| 20 | Business Discovery & Estratégia Web | Tese (ext) | `problem-framing-canvas`, `jobs-to-be-done`, `positioning-workshop` | ✅ ativo |
| 21 | Design System & Inventário de Componentes | Molda | `design-system`, `frontend-design`, `emil-design-eng` | ✅ ativo |
| 22 | Development & Build + QA Técnico/Acessibilidade | Constrói | `accessibility`, `web-quality-audit`, `impeccable-design-polish`, `qa`, **`image`** (favicon/OG/social preview — acrescentada 2026-10-12, gap real no build do teste) | ✅ ativo |
| 23 | Performance & Launch | Constrói | `land-and-deploy`, `web-quality-audit`, `core-web-vitals`, `vercel-deployment` (condicional) | ✅ ativo |
| 24 | QA Final & Gate de Publicação | Eixo | `production-audit`, `browser-qa`, **`redesign-existing-projects`** (opcional, checklist complementar — flagra favicon/og:image faltando) | ✅ ativo |
| 25 | Arquitetura de Informação & Jornada | Guia | `site-architecture`, `customer-journey-map` | Sprint 2 — a definir |
| 26 | Copy & CRO Framework | Convence | `copywriting`, `cro`, `popups`, `copy-editing` (família real e interligada — `landing-page-copy` não existe, `copywriting` já cobre landing page) | Sprint 2 — a definir |
| 27 | Content Engine (multicanal) | Multiplica | `content-engine` | Sprint 2 — a definir |
| 28 | Pesquisa de Mercado & Competitive Intelligence Web | Radar (ext) | `competitor-profiling`, `competitors` (`competitive-teardown` não existe) | Sprint 3 — a definir |
| 29 | Search Intent & Keyword Research | Busca | `seo-audit` (preferir à família `seo` solta — mais rica e interligada) | Sprint 3 — a definir |
| 30 | Entity Map & Schema | Busca | `schema` (não `schema-markup`) | Sprint 3 — a definir |
| 31 | SEO, SEO Local, GBP Engine, Review Intelligence | Busca | `seo-audit` (cobre parcial) · **`local-seo` é gap real, sem skill instalada — escrever do zero** | Sprint 3 — a definir |
| 32 | AEO, GEO & LLMS.txt | Busca | `ai-seo` (preferir à `aeo` solta — essa está empacotada fora do padrão, pode não carregar), `programmatic-seo` (opcional, só se fizer página-por-cidade em escala) | Sprint 3 — a definir |
| 33 | Analytics Engine: GA4+GTM+Tracking Plan (inclui Behavior Analytics — scroll depth, rage/dead click, abandono por seção) | Mede (ext) | `analytics` (não `analytics-tracking`), `data-and-funnel-analytics` | Sprint 4 — a definir |
| 34 | UTM System & Atribuição | Mede (ext) | `data-and-funnel-analytics` | Sprint 4 — a definir |
| 35 | CRM Integration & BI Dashboard | Mede (ext) | `data-and-funnel-analytics` | Sprint 4 — a definir |
| 36 | Monitoramento Contínuo Web | Mede (ext) | `web-quality-audit` (não `performance-profiler`, que não existe) | Sprint 4 — a definir |
| 37 | Security & Trust Checklist | Blinda | `security-review` (não `security-guidance` — esse é plugin só de hooks, não skill invocável) | Sprint 5 — a definir |
| 38 | LGPD & Privacidade | Blinda | **Gap real, sem skill técnica instalada** — `direito-br` é orientação jurídica, não implementação (cookie banner, política, mapeamento de dados) — escrever do zero | Sprint 5 — a definir |
| 39 | Growth & Experimentation Engine | Evolui | `ab-testing` (cobre sozinha `cro-optimization` e `experiment-designer`, que não existem como nomes separados) | Sprint 5 — a definir |
| 40 | Digital Asset Score™ & AI Readiness Score™ | Evolui | (heurística interna, sem skill 1:1) | Sprint 5 — a definir |
| 41 | Escala & Plano de Crescimento | Eixo + Evolui | `growth-funnel` | Sprint 5 — a definir |
| 42 | Niche System | Eixo | — | Sprint 6 — a definir |
| 43 | Template Engine | Eixo + Constrói | **Gap real** (`saas-scaffolder`, `spec-to-repo` não existem) — escrever do zero | Sprint 6 — a definir |

**Gaps fora do índice, sem skill e sem módulo dedicado**: i18n/bilíngue (PT+EN) e formulário de lead sem backend pesado (tipo Formspree) — nenhuma skill cobre isso; fica como instrução manual direto no Constrói (módulo 22) quando o projeto precisar.

## Fluxo padrão de um projeto

```
Pedido do Lucas (novo site/landing page)
  └── Tese-ext (mód. 20) → estrategia.md
        └── Molda (mód. 21) → specs/design.md + inventário de componentes [aprovação do Lucas]
              └── Constrói (mód. 22) → build/ + QA técnico/a11y
                    └── Constrói (mód. 23) → deploy + auditoria de performance
                          └── Eixo (mód. 24) → checklist QA Final [status: pronto-para-publicar, aprovado: false]
                                └── Lucas aprova (_sop/aprovacao-publicacao.md) → aprovado: true
                                      └── deploy em produção → status: publicado
```

## Regras herdadas

- Português brasileiro em toda saída final-facing.
- Nunca inventar dado de mercado, número de conversão, preço ou depoimento — dado faltante vira pendência registrada, não estimativa.
- `verification-before-completion`: nenhum agente declara uma etapa "pronta"/"corrigida"/"passando" sem rodar a verificação de novo e confirmar o resultado.
- Regras de conflito entre camadas (doc-fonte NEOVERTIX WEB OS §56), arbitradas pelo Eixo: Performance×Design → performance vence · SEO×UX → nunca keyword-stuff · CRO×Confiança → nunca remover info obrigatória pra forçar conversão · Marketing×Verdade → nunca publicar promessa não comprovada · Escala×Qualidade → nunca escalar processo não validado.
- `tese`, `radar` e `mede` atendem dois squads (Social mídia IA + Web OS) — especifique o contexto (Instagram vs. Web) se não estiver óbvio no pedido.
- Gate inegociável: nada vai ao ar sem `aprovado: true` marcado pelo Lucas (ver `_sop/aprovacao-publicacao.md`).

## Execução parcial

Pra rodar só um módulo: "Execute apenas o Módulo N do Web OS — leia Web OS/modules/NN-nome.md".