# Graph Report - .  (2026-06-18)

## Corpus Check
- 24 files · ~17,211 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 63 nodes · 124 edges · 8 communities
- Extraction: 90% EXTRACTED · 10% INFERRED · 1% AMBIGUOUS · INFERRED: 12 edges (avg confidence: 0.92)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Instagram Monitoring Pipeline|Instagram Monitoring Pipeline]]
- [[_COMMUNITY_ObsidianNotion Export & Insights|Obsidian/Notion Export & Insights]]
- [[_COMMUNITY_Trend Monitoring & Positioning|Trend Monitoring & Positioning]]
- [[_COMMUNITY_Agent Security Risk Content|Agent Security Risk Content]]
- [[_COMMUNITY_Low-Friction Content Formats|Low-Friction Content Formats]]
- [[_COMMUNITY_Monitor-as-Social-Proof Content|Monitor-as-Social-Proof Content]]
- [[_COMMUNITY_Benchmark to Content Models|Benchmark to Content Models]]
- [[_COMMUNITY_Scale Desire POV Content|Scale Desire POV Content]]

## God Nodes (most connected - your core abstractions)
1. `monitor/run.md — Orquestrador Principal` - 12 edges
2. `Módulo 5 — Modelos de Conteúdo` - 10 edges
3. `Relatório 02-perfis-instagram.md (2026-06-17)` - 10 edges
4. `Módulo 6 — Aplicação ao Negócio` - 9 edges
5. `Relatório 01-tendencias.md (2026-06-17)` - 9 edges
6. `Relatório 06-aplicacao-negocio.md (2026-06-17)` - 9 edges
7. `RESUMO.md (2026-06-17)` - 9 edges
8. `Relatório 03-benchmark.md (2026-06-17)` - 8 edges
9. `Relatório 05-modelos-conteudo.md (2026-06-17)` - 8 edges
10. `Módulo 7 — Exportação para Obsidian` - 7 edges

## Surprising Connections (you probably didn't know these)
- `monitor/run.md — Orquestrador Principal` --references--> `config/sources.json`  [EXTRACTED]
  monitor/run.md → config/sources.json
- `Módulo 7 — Exportação para Obsidian` --references--> `config/obsidian.json`  [EXTRACTED]
  monitor/modules/07-obsidian-export.md → config/obsidian.json
- `Relatório 01-tendencias.md (2026-06-17)` --shares_data_with--> `config/sources.json`  [INFERRED]
  reports/2026-06-17/01-tendencias.md → config/sources.json
- `Relatório 02-perfis-instagram.md (2026-06-17)` --shares_data_with--> `config/profiles.json`  [INFERRED]
  reports/2026-06-17/02-perfis-instagram.md → config/profiles.json
- `Relatório 02-perfis-instagram.md (2026-06-17)` --references--> `Perfil Instagram @charliehills`  [EXTRACTED]
  reports/2026-06-17/02-perfis-instagram.md → config/profiles.json

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Pipeline Sequencial dos Módulos 1-8 do Monitor** — 01_trends_modulo1, 02_instagram_modulo2, 03_benchmark_modulo3, 04_top10_analysis_modulo4, 05_content_models_modulo5, 06_business_apply_modulo6, 07_obsidian_export_modulo7, 08_notion_export_modulo8 [EXTRACTED 0.95]
- **Frameworks Reutilizáveis Identificados no Módulo 4** — framework_nomeacao_fenomeno, framework_nome_sistema_resultado, framework_cta_baixo_atrito, framework_contraste_crenca, framework_pergunta_retorica_escala, framework_poder_ate_que, framework_minimo_viavel [EXTRACTED 0.90]
- **Top 5 Ideias de Conteúdo Prontas para Produção (2026-06-17)** — ideia_verdade_sobre_automacao, ideia_sistema_monitora_50_perfis, ideia_prompt_para_criar_agentes, ideia_conteudo_pronto_dormindo, ideia_risco_agentes_ia [EXTRACTED 0.95]

## Communities (8 total, 0 thin omitted)

### Community 0 - "Instagram Monitoring Pipeline"
Cohesion: 0.24
Nodes (15): Módulo 2 — Monitoramento de Perfis Instagram, Módulo 3 — Benchmark de Conteúdo, Módulo 4 — Análise Profunda dos Top 10 Conteúdos, Módulo 6 — Aplicação ao Negócio, Relatório 02-perfis-instagram.md (2026-06-17), config/business.json, config/profiles.json, config/README.md (+7 more)

### Community 1 - "Obsidian/Notion Export & Insights"
Cohesion: 0.25
Nodes (11): Módulo 7 — Exportação para Obsidian, Módulo 8 — Exportação para Notion, Relatório 06-aplicacao-negocio.md (2026-06-17), RESUMO.md (2026-06-17), config/obsidian.json, Framework: Contraste/Negação de Crença Popular, Ideia de Conteúdo: A verdade sobre automação, Modelo de Conteúdo: opiniao_forte (+3 more)

### Community 2 - "Trend Monitoring & Positioning"
Cohesion: 0.25
Nodes (9): Módulo 1 — Monitoramento de Tendências, Relatório 01-tendencias.md (2026-06-17), Posicionamento do Negócio (em definição), config/sources.json, Insight: AI Agency via Orquestração Agêntica é Tendência Forte, Skill Swarm (processamento paralelo), Template — report-trends.md, Tendência: Fim do Pricing por Assento (SaaS) até 2028 (+1 more)

### Community 3 - "Agent Security Risk Content"
Cohesion: 0.33
Nodes (7): Framework: 'Poder... até que...' (Alerta de Risco Oculto), Ideia de Conteúdo: O risco que ninguém fala sobre agentes de IA, Insight: Segurança de Agentes/MCP Privados em PT é Lacuna de Mercado, Modelo de Conteúdo: erro_comum, Perfil Instagram @charliehills, Tendência: Claude Managed Agents (sandbox + MCP privado), Conteúdo: 'Tus agentes de IA son poderosos… hasta que se filtran'

### Community 4 - "Low-Friction Content Formats"
Cohesion: 0.33
Nodes (6): Relatório 05-modelos-conteudo.md (2026-06-17), Framework: CTA de Baixo Atrito (Comentar Palavra-chave → DM), Framework: Mínimo Viável (Redução de Complexidade), Ideia de Conteúdo: O prompt que eu uso pra criar agentes, Modelo de Conteúdo: lista_checklist, Modelo de Conteúdo: tutorial_rapido

### Community 5 - "Monitor-as-Social-Proof Content"
Cohesion: 0.40
Nodes (6): Framework: Nome de Sistema/Método + Resultado Numérico + Prazo, Ideia de Conteúdo: O sistema que monitora 50 perfis de IA por mim, Insight: Sistema monitor/ como Prova Social (case_real), Modelo de Conteúdo: case_real, Perfil Instagram @nick_saraev, Conteúdo: 'The N8N Instagram Parasite System'

### Community 6 - "Benchmark to Content Models"
Cohesion: 0.60
Nodes (5): Módulo 5 — Modelos de Conteúdo, Relatório 03-benchmark.md (2026-06-17), Relatório 04-top10-analise.md (2026-06-17), Framework: Nomeação de Fenômeno + Transição De X Para Y, Conteúdo: 'SMMA to AI Agencies - The New Gold Rush!'

### Community 7 - "Scale Desire POV Content"
Cohesion: 0.67
Nodes (4): Framework: Pergunta Retórica Ligada a Desejo de Escala, Ideia de Conteúdo: Conteúdo pronto enquanto você dorme, Modelo de Conteúdo: pov, Conteúdo: 'Quer fazer seu agente de IA vender enquanto você dorme?'

## Ambiguous Edges - Review These
- `Framework: Mínimo Viável (Redução de Complexidade)` → `Framework: CTA de Baixo Atrito (Comentar Palavra-chave → DM)`  [AMBIGUOUS]
  reports/2026-06-17/04-top10-analise.md · relation: semantically_similar_to

## Knowledge Gaps
- **7 isolated node(s):** `config/obsidian.json`, `Skill Swarm (processamento paralelo)`, `Skill daydream`, `Perfil Instagram @rafa.grandi (handle suspeito)`, `Perfil Instagram @humam__academy (possível typo)` (+2 more)
  These have ≤1 connection - possible missing edges or undocumented components.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `Framework: Mínimo Viável (Redução de Complexidade)` and `Framework: CTA de Baixo Atrito (Comentar Palavra-chave → DM)`?**
  _Edge tagged AMBIGUOUS (relation: semantically_similar_to) - confidence is low._
- **Why does `Relatório 06-aplicacao-negocio.md (2026-06-17)` connect `Obsidian/Notion Export & Insights` to `Agent Security Risk Content`, `Low-Friction Content Formats`, `Monitor-as-Social-Proof Content`, `Scale Desire POV Content`?**
  _High betweenness centrality (0.017) - this node is a cross-community bridge._
- **Why does `monitor/run.md — Orquestrador Principal` connect `Instagram Monitoring Pipeline` to `Obsidian/Notion Export & Insights`, `Trend Monitoring & Positioning`, `Benchmark to Content Models`?**
  _High betweenness centrality (0.015) - this node is a cross-community bridge._
- **Why does `Relatório 03-benchmark.md (2026-06-17)` connect `Benchmark to Content Models` to `Obsidian/Notion Export & Insights`, `Agent Security Risk Content`, `Monitor-as-Social-Proof Content`, `Scale Desire POV Content`?**
  _High betweenness centrality (0.013) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `Relatório 02-perfis-instagram.md (2026-06-17)` (e.g. with `config/profiles.json` and `Template — report-instagram.md`) actually correct?**
  _`Relatório 02-perfis-instagram.md (2026-06-17)` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `Relatório 01-tendencias.md (2026-06-17)` (e.g. with `config/sources.json` and `Template — report-trends.md`) actually correct?**
  _`Relatório 01-tendencias.md (2026-06-17)` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `config/obsidian.json`, `Skill Swarm (processamento paralelo)`, `Skill daydream` to the rest of the system?**
  _8 weakly-connected nodes found - possible documentation gaps or missing edges._