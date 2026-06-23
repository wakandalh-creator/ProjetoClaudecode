# Graph Report - .  (2026-06-23)

## Corpus Check
- 25 files · ~18,291 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 94 nodes · 138 edges · 10 communities (8 shown, 2 thin omitted)
- Extraction: 90% EXTRACTED · 9% INFERRED · 1% AMBIGUOUS · INFERRED: 12 edges (avg confidence: 0.9)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `ab66865a`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- [[_COMMUNITY_Configuração e Infraestrutura do Monitor|Configuração e Infraestrutura do Monitor]]
- [[_COMMUNITY_Modelos e Frameworks de Conteúdo|Modelos e Frameworks de Conteúdo]]
- [[_COMMUNITY_Tendências e Exportação de Dados|Tendências e Exportação de Dados]]
- [[_COMMUNITY_Monitoramento Instagram e Templates|Monitoramento Instagram e Templates]]
- [[_COMMUNITY_Análise Top 10 e Frameworks|Análise Top 10 e Frameworks]]
- [[_COMMUNITY_Regras de Segurança do Swarm|Regras de Segurança do Swarm]]
- [[_COMMUNITY_Auto-Sync e Identidade do Projeto|Auto-Sync e Identidade do Projeto]]
- [[_COMMUNITY_Framework de Risco Oculto|Framework de Risco Oculto]]
- [[_COMMUNITY_Plugins Desativados do Projeto|Plugins Desativados do Projeto]]
- [[_COMMUNITY_MCP GPT Maker|MCP GPT Maker]]

## God Nodes (most connected - your core abstractions)
1. `Módulo 5 — Modelos de Conteúdo` - 10 edges
2. `monitor/run.md — Orquestrador Principal` - 9 edges
3. `Relatório 06-aplicacao-negocio.md (2026-06-17)` - 9 edges
4. `monitor` - 9 edges
5. `Módulo 6 — Aplicação ao Negócio` - 8 edges
6. `Relatório 01-tendencias.md (2026-06-17)` - 8 edges
7. `Relatório 03-benchmark.md (2026-06-17)` - 8 edges
8. `Relatório 05-modelos-conteudo.md (2026-06-17)` - 8 edges
9. `RESUMO.md (2026-06-17)` - 7 edges
10. `Swarm Skill — Regras Obrigatórias de Segurança` - 7 edges

## Surprising Connections (you probably didn't know these)
- `Relatório 06-aplicacao-negocio.md (2026-06-17)` --implements--> `Template — report-insights.md`  [INFERRED]
  reports/2026-06-17/06-aplicacao-negocio.md → monitor/templates/report-insights.md
- `Relatório 01-tendencias.md (2026-06-17)` --implements--> `Template — report-trends.md`  [INFERRED]
  reports/2026-06-17/01-tendencias.md → monitor/templates/report-trends.md
- `Relatório 02-perfis-instagram.md (2026-06-17)` --implements--> `Template — report-instagram.md`  [INFERRED]
  reports/2026-06-17/02-perfis-instagram.md → monitor/templates/report-instagram.md
- `Framework: Contraste/Negação de Crença Popular` --implements--> `Modelo de Conteúdo: opiniao_forte`  [INFERRED]
  reports/2026-06-17/04-top10-analise.md → monitor/modules/05-content-models.md
- `Módulo 3 — Benchmark de Conteúdo` --references--> `Relatório 02-perfis-instagram.md (2026-06-17)`  [EXTRACTED]
  monitor/modules/03-benchmark.md → reports/2026-06-17/02-perfis-instagram.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Pipeline Sequencial dos Módulos 1-8 do Monitor** — 01_trends_modulo1, 02_instagram_modulo2, 03_benchmark_modulo3, 04_top10_analysis_modulo4, 05_content_models_modulo5, 06_business_apply_modulo6, 07_obsidian_export_modulo7, 08_notion_export_modulo8 [EXTRACTED 0.95]
- **Frameworks Reutilizáveis Identificados no Módulo 4** — framework_nomeacao_fenomeno, framework_nome_sistema_resultado, framework_cta_baixo_atrito, framework_contraste_crenca, framework_pergunta_retorica_escala, framework_poder_ate_que, framework_minimo_viavel [EXTRACTED 0.90]
- **Top 5 Ideias de Conteúdo Prontas para Produção (2026-06-17)** — ideia_verdade_sobre_automacao, ideia_sistema_monitora_50_perfis, ideia_prompt_para_criar_agentes, ideia_conteudo_pronto_dormindo, ideia_risco_agentes_ia [EXTRACTED 0.95]

## Communities (10 total, 2 thin omitted)

### Community 0 - "Configuração e Infraestrutura do Monitor"
Cohesion: 0.10
Nodes (22): config/business.json, config/obsidian.json, config/profiles.json, config/sources.json, daydream (skill), memory/glossary.md, GOOGLE_API_KEY, graphify-out/GRAPH_REPORT.md (+14 more)

### Community 1 - "Modelos e Frameworks de Conteúdo"
Cohesion: 0.18
Nodes (17): Módulo 5 — Modelos de Conteúdo, Relatório 05-modelos-conteudo.md (2026-06-17), Relatório 06-aplicacao-negocio.md (2026-06-17), Framework: Contraste/Negação de Crença Popular, Framework: CTA de Baixo Atrito (Comentar Palavra-chave → DM), Framework: Mínimo Viável (Redução de Complexidade), Framework: Nome de Sistema/Método + Resultado Numérico + Prazo, Ideia de Conteúdo: O prompt que eu uso pra criar agentes (+9 more)

### Community 2 - "Tendências e Exportação de Dados"
Cohesion: 0.21
Nodes (13): Módulo 1 — Monitoramento de Tendências, Módulo 7 — Exportação para Obsidian, Módulo 8 — Exportação para Notion, Relatório 01-tendencias.md (2026-06-17), RESUMO.md (2026-06-17), Insight: AI Agency via Orquestração Agêntica é Tendência Forte, Insight: Segurança de Agentes/MCP Privados em PT é Lacuna de Mercado, Skill daydream (+5 more)

### Community 3 - "Monitoramento Instagram e Templates"
Cohesion: 0.27
Nodes (11): Módulo 2 — Monitoramento de Perfis Instagram, Módulo 3 — Benchmark de Conteúdo, Módulo 6 — Aplicação ao Negócio, Relatório 02-perfis-instagram.md (2026-06-17), config/README.md, Skill instagram-content-cloner, Modo Análise (perfis ativos), Modo Descoberta (perfis vazios) (+3 more)

### Community 4 - "Análise Top 10 e Frameworks"
Cohesion: 0.28
Nodes (9): Módulo 4 — Análise Profunda dos Top 10 Conteúdos, Relatório 03-benchmark.md (2026-06-17), Relatório 04-top10-analise.md (2026-06-17), Framework: Nomeação de Fenômeno + Transição De X Para Y, Framework: Pergunta Retórica Ligada a Desejo de Escala, Ideia de Conteúdo: Conteúdo pronto enquanto você dorme, Modelo de Conteúdo: pov, Conteúdo: 'Quer fazer seu agente de IA vender enquanto você dorme?' (+1 more)

### Community 5 - "Regras de Segurança do Swarm"
Cohesion: 0.25
Nodes (8): batchSize padrão 5, concurrency: 3, context (ancoragem do modelo), responseSchema (estrito), retry após run inicial, subagentType (uso restrito), swarm, Swarm Skill — Regras Obrigatórias de Segurança

### Community 6 - "Auto-Sync e Identidade do Projeto"
Cohesion: 0.33
Nodes (6): auto-sync, .claude/auto-sync.ps1, GitHub Repository (wakandalh-creator/ProjetoClaudecode), Lucas, ProjetoClaudecode, .claude/settings.local.json

### Community 7 - "Framework de Risco Oculto"
Cohesion: 0.67
Nodes (4): Framework: 'Poder... até que...' (Alerta de Risco Oculto), Ideia de Conteúdo: O risco que ninguém fala sobre agentes de IA, Modelo de Conteúdo: erro_comum, Conteúdo: 'Tus agentes de IA son poderosos… hasta que se filtran'

## Ambiguous Edges - Review These
- `Framework: Mínimo Viável (Redução de Complexidade)` → `Framework: CTA de Baixo Atrito (Comentar Palavra-chave → DM)`  [AMBIGUOUS]
  reports/2026-06-17/04-top10-analise.md · relation: semantically_similar_to
- `pw (playwright-pro plugin)` → `claude mem`  [AMBIGUOUS]
  CLAUDE.md · relation: conceptually_related_to

## Knowledge Gaps
- **23 isolated node(s):** `Skill Swarm (processamento paralelo)`, `Skill daydream`, `Tendência: Fim do Pricing por Assento (SaaS) até 2028`, `Insight: Sistema monitor/ como Prova Social (case_real)`, `swarm` (+18 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **2 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `Framework: Mínimo Viável (Redução de Complexidade)` and `Framework: CTA de Baixo Atrito (Comentar Palavra-chave → DM)`?**
  _Edge tagged AMBIGUOUS (relation: semantically_similar_to) - confidence is low._
- **What is the exact relationship between `pw (playwright-pro plugin)` and `claude mem`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **Why does `Relatório 06-aplicacao-negocio.md (2026-06-17)` connect `Modelos e Frameworks de Conteúdo` to `Monitoramento Instagram e Templates`, `Análise Top 10 e Frameworks`, `Framework de Risco Oculto`?**
  _High betweenness centrality (0.008) - this node is a cross-community bridge._
- **Why does `monitor/run.md — Orquestrador Principal` connect `Monitoramento Instagram e Templates` to `Modelos e Frameworks de Conteúdo`, `Tendências e Exportação de Dados`, `Análise Top 10 e Frameworks`?**
  _High betweenness centrality (0.006) - this node is a cross-community bridge._
- **Why does `Relatório 03-benchmark.md (2026-06-17)` connect `Análise Top 10 e Frameworks` to `Modelos e Frameworks de Conteúdo`, `Framework de Risco Oculto`?**
  _High betweenness centrality (0.006) - this node is a cross-community bridge._
- **What connects `Skill Swarm (processamento paralelo)`, `Skill daydream`, `Tendência: Fim do Pricing por Assento (SaaS) até 2028` to the rest of the system?**
  _27 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Configuração e Infraestrutura do Monitor` be split into smaller, more focused modules?**
  _Cohesion score 0.10276679841897234 - nodes in this community are weakly interconnected._