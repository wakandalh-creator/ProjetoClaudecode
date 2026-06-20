# Graph Report - /home/user/ProjetoClaudecode  (2026-06-20)

## Corpus Check
- 24 files · ~17,211 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 54 nodes · 98 edges · 7 communities
- Extraction: 89% EXTRACTED · 10% INFERRED · 1% AMBIGUOUS · INFERRED: 10 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `6d001ff4`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- [[_COMMUNITY_Monitoramento de Tendências e Exportação|Monitoramento de Tendências e Exportação]]
- [[_COMMUNITY_Monitoramento Instagram e Benchmark|Monitoramento Instagram e Benchmark]]
- [[_COMMUNITY_Modelos e Frameworks de Conteúdo|Modelos e Frameworks de Conteúdo]]
- [[_COMMUNITY_Aplicação ao Negócio e Cases|Aplicação ao Negócio e Cases]]
- [[_COMMUNITY_Análise Top10 e Frameworks|Análise Top10 e Frameworks]]
- [[_COMMUNITY_Framework de Opinião Forte  Contraste|Framework de Opinião Forte / Contraste]]
- [[_COMMUNITY_Framework de Risco Oculto|Framework de Risco Oculto]]

## God Nodes (most connected - your core abstractions)
1. `Módulo 5 — Modelos de Conteúdo` - 10 edges
2. `monitor/run.md — Orquestrador Principal` - 9 edges
3. `Relatório 06-aplicacao-negocio.md (2026-06-17)` - 9 edges
4. `Módulo 6 — Aplicação ao Negócio` - 8 edges
5. `Relatório 01-tendencias.md (2026-06-17)` - 8 edges
6. `Relatório 03-benchmark.md (2026-06-17)` - 8 edges
7. `Relatório 05-modelos-conteudo.md (2026-06-17)` - 8 edges
8. `RESUMO.md (2026-06-17)` - 7 edges
9. `Módulo 7 — Exportação para Obsidian` - 6 edges
10. `Módulo 2 — Monitoramento de Perfis Instagram` - 5 edges

## Surprising Connections (you probably didn't know these)
- `Relatório 01-tendencias.md (2026-06-17)` --implements--> `Template — report-trends.md`  [INFERRED]
  reports/2026-06-17/01-tendencias.md → monitor/templates/report-trends.md
- `Relatório 02-perfis-instagram.md (2026-06-17)` --implements--> `Template — report-instagram.md`  [INFERRED]
  reports/2026-06-17/02-perfis-instagram.md → monitor/templates/report-instagram.md
- `Framework: Contraste/Negação de Crença Popular` --implements--> `Modelo de Conteúdo: opiniao_forte`  [INFERRED]
  reports/2026-06-17/04-top10-analise.md → monitor/modules/05-content-models.md
- `Relatório 06-aplicacao-negocio.md (2026-06-17)` --implements--> `Template — report-insights.md`  [INFERRED]
  reports/2026-06-17/06-aplicacao-negocio.md → monitor/templates/report-insights.md
- `Módulo 3 — Benchmark de Conteúdo` --references--> `Relatório 02-perfis-instagram.md (2026-06-17)`  [EXTRACTED]
  monitor/modules/03-benchmark.md → reports/2026-06-17/02-perfis-instagram.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Pipeline Sequencial dos Módulos 1-8 do Monitor** — 01_trends_modulo1, 02_instagram_modulo2, 03_benchmark_modulo3, 04_top10_analysis_modulo4, 05_content_models_modulo5, 06_business_apply_modulo6, 07_obsidian_export_modulo7, 08_notion_export_modulo8 [EXTRACTED 0.95]
- **Frameworks Reutilizáveis Identificados no Módulo 4** — framework_nomeacao_fenomeno, framework_nome_sistema_resultado, framework_cta_baixo_atrito, framework_contraste_crenca, framework_pergunta_retorica_escala, framework_poder_ate_que, framework_minimo_viavel [EXTRACTED 0.90]
- **Top 5 Ideias de Conteúdo Prontas para Produção (2026-06-17)** — ideia_verdade_sobre_automacao, ideia_sistema_monitora_50_perfis, ideia_prompt_para_criar_agentes, ideia_conteudo_pronto_dormindo, ideia_risco_agentes_ia [EXTRACTED 0.95]

## Communities (7 total, 0 thin omitted)

### Community 0 - "Monitoramento de Tendências e Exportação"
Cohesion: 0.21
Nodes (13): Módulo 1 — Monitoramento de Tendências, Módulo 7 — Exportação para Obsidian, Módulo 8 — Exportação para Notion, Relatório 01-tendencias.md (2026-06-17), RESUMO.md (2026-06-17), Insight: AI Agency via Orquestração Agêntica é Tendência Forte, Insight: Segurança de Agentes/MCP Privados em PT é Lacuna de Mercado, Skill daydream (+5 more)

### Community 1 - "Monitoramento Instagram e Benchmark"
Cohesion: 0.31
Nodes (10): Módulo 2 — Monitoramento de Perfis Instagram, Módulo 3 — Benchmark de Conteúdo, Módulo 6 — Aplicação ao Negócio, Relatório 02-perfis-instagram.md (2026-06-17), config/README.md, Skill instagram-content-cloner, Modo Análise (perfis ativos), Modo Descoberta (perfis vazios) (+2 more)

### Community 2 - "Modelos e Frameworks de Conteúdo"
Cohesion: 0.27
Nodes (10): Módulo 5 — Modelos de Conteúdo, Relatório 05-modelos-conteudo.md (2026-06-17), Framework: CTA de Baixo Atrito (Comentar Palavra-chave → DM), Framework: Mínimo Viável (Redução de Complexidade), Framework: Pergunta Retórica Ligada a Desejo de Escala, Ideia de Conteúdo: Conteúdo pronto enquanto você dorme, Modelo de Conteúdo: lista_checklist, Modelo de Conteúdo: pov (+2 more)

### Community 3 - "Aplicação ao Negócio e Cases"
Cohesion: 0.32
Nodes (8): Relatório 06-aplicacao-negocio.md (2026-06-17), Framework: Nome de Sistema/Método + Resultado Numérico + Prazo, Ideia de Conteúdo: O prompt que eu uso pra criar agentes, Ideia de Conteúdo: O sistema que monitora 50 perfis de IA por mim, Insight: Sistema monitor/ como Prova Social (case_real), Modelo de Conteúdo: case_real, Template — report-insights.md, Conteúdo: 'The N8N Instagram Parasite System'

### Community 4 - "Análise Top10 e Frameworks"
Cohesion: 0.50
Nodes (5): Módulo 4 — Análise Profunda dos Top 10 Conteúdos, Relatório 03-benchmark.md (2026-06-17), Relatório 04-top10-analise.md (2026-06-17), Framework: Nomeação de Fenômeno + Transição De X Para Y, Conteúdo: 'SMMA to AI Agencies - The New Gold Rush!'

### Community 5 - "Framework de Opinião Forte / Contraste"
Cohesion: 0.67
Nodes (4): Framework: Contraste/Negação de Crença Popular, Ideia de Conteúdo: A verdade sobre automação, Modelo de Conteúdo: opiniao_forte, Conteúdo: 'A verdade é que a IA não vai vender por você...'

### Community 6 - "Framework de Risco Oculto"
Cohesion: 0.67
Nodes (4): Framework: 'Poder... até que...' (Alerta de Risco Oculto), Ideia de Conteúdo: O risco que ninguém fala sobre agentes de IA, Modelo de Conteúdo: erro_comum, Conteúdo: 'Tus agentes de IA son poderosos… hasta que se filtran'

## Ambiguous Edges - Review These
- `Framework: Mínimo Viável (Redução de Complexidade)` → `Framework: CTA de Baixo Atrito (Comentar Palavra-chave → DM)`  [AMBIGUOUS]
  reports/2026-06-17/04-top10-analise.md · relation: semantically_similar_to

## Knowledge Gaps
- **4 isolated node(s):** `Skill Swarm (processamento paralelo)`, `Skill daydream`, `Tendência: Fim do Pricing por Assento (SaaS) até 2028`, `Insight: Sistema monitor/ como Prova Social (case_real)`
  These have ≤1 connection - possible missing edges or undocumented components.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `Framework: Mínimo Viável (Redução de Complexidade)` and `Framework: CTA de Baixo Atrito (Comentar Palavra-chave → DM)`?**
  _Edge tagged AMBIGUOUS (relation: semantically_similar_to) - confidence is low._
- **Why does `Relatório 06-aplicacao-negocio.md (2026-06-17)` connect `Aplicação ao Negócio e Cases` to `Modelos e Frameworks de Conteúdo`, `Framework de Opinião Forte / Contraste`, `Framework de Risco Oculto`?**
  _High betweenness centrality (0.024) - this node is a cross-community bridge._
- **Why does `monitor/run.md — Orquestrador Principal` connect `Monitoramento Instagram e Benchmark` to `Monitoramento de Tendências e Exportação`, `Modelos e Frameworks de Conteúdo`, `Análise Top10 e Frameworks`?**
  _High betweenness centrality (0.018) - this node is a cross-community bridge._
- **Why does `Relatório 03-benchmark.md (2026-06-17)` connect `Análise Top10 e Frameworks` to `Modelos e Frameworks de Conteúdo`, `Aplicação ao Negócio e Cases`, `Framework de Opinião Forte / Contraste`, `Framework de Risco Oculto`?**
  _High betweenness centrality (0.017) - this node is a cross-community bridge._
- **What connects `Skill Swarm (processamento paralelo)`, `Skill daydream`, `Tendência: Fim do Pricing por Assento (SaaS) até 2028` to the rest of the system?**
  _5 weakly-connected nodes found - possible documentation gaps or missing edges._