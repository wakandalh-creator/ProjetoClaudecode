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

| # | Módulo | Agente | Status |
|---|---|---|---|
| 20 | Business Discovery & Estratégia Web | Tese (ext) | ✅ ativo |
| 21 | Design System & Inventário de Componentes | Molda | ✅ ativo |
| 22 | Development & Build + QA Técnico/Acessibilidade | Constrói | ✅ ativo |
| 23 | Performance & Launch | Constrói | ✅ ativo |
| 24 | QA Final & Gate de Publicação | Eixo | ✅ ativo |
| 25 | Arquitetura de Informação & Jornada | Guia | Sprint 2 — a definir |
| 26 | Copy & CRO Framework | Convence | Sprint 2 — a definir |
| 27 | Content Engine (multicanal) | Multiplica | Sprint 2 — a definir |
| 28 | Pesquisa de Mercado & Competitive Intelligence Web | Radar (ext) | Sprint 3 — a definir |
| 29 | Search Intent & Keyword Research | Busca | Sprint 3 — a definir |
| 30 | Entity Map & Schema | Busca | Sprint 3 — a definir |
| 31 | SEO, SEO Local, GBP Engine, Review Intelligence | Busca | Sprint 3 — a definir |
| 32 | AEO, GEO & LLMS.txt | Busca | Sprint 3 — a definir |
| 33 | Analytics Engine: GA4+GTM+Tracking Plan (inclui Behavior Analytics — scroll depth, rage/dead click, abandono por seção, acrescentado 2026-10-09) | Mede (ext) | Sprint 4 — a definir |
| 34 | UTM System & Atribuição | Mede (ext) | Sprint 4 — a definir |
| 35 | CRM Integration & BI Dashboard | Mede (ext) | Sprint 4 — a definir |
| 36 | Monitoramento Contínuo Web | Mede (ext) | Sprint 4 — a definir |
| 37 | Security & Trust Checklist | Blinda | Sprint 5 — a definir |
| 38 | LGPD & Privacidade | Blinda | Sprint 5 — a definir |
| 39 | Growth & Experimentation Engine | Evolui | Sprint 5 — a definir |
| 40 | Digital Asset Score™ & AI Readiness Score™ | Evolui | Sprint 5 — a definir |
| 41 | Escala & Plano de Crescimento | Eixo + Evolui | Sprint 5 — a definir |
| 42 | Niche System | Eixo | Sprint 6 — a definir |
| 43 | Template Engine | Eixo + Constrói | Sprint 6 — a definir |

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