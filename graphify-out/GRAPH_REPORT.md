# Graph Report - .  (2026-06-25)

## Corpus Check
- 33 files · ~30,814 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 119 nodes · 240 edges · 13 communities
- Extraction: 94% EXTRACTED · 5% INFERRED · 1% AMBIGUOUS · INFERRED: 12 edges (avg confidence: 0.9)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `08aad2f6`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- [[_COMMUNITY_Tendências e Exportação de Dados|Tendências e Exportação de Dados]]
- [[_COMMUNITY_Configuração e Infraestrutura do Monitor|Configuração e Infraestrutura do Monitor]]
- [[_COMMUNITY_Benchmark e Frameworks de Oferta|Benchmark e Frameworks de Oferta]]
- [[_COMMUNITY_Monitoramento Instagram e Templates|Monitoramento Instagram e Templates]]
- [[_COMMUNITY_Perfis Instagram Monitorados|Perfis Instagram Monitorados]]
- [[_COMMUNITY_Modelos e Frameworks de Conteúdo|Modelos e Frameworks de Conteúdo]]
- [[_COMMUNITY_Ideias de Conteúdo e Perfis|Ideias de Conteúdo e Perfis]]
- [[_COMMUNITY_Storytelling e POV|Storytelling e POV]]
- [[_COMMUNITY_Análise Top 10 e Frameworks|Análise Top 10 e Frameworks]]
- [[_COMMUNITY_Prova Social e Case Real|Prova Social e Case Real]]
- [[_COMMUNITY_Automação e Desejo de Escala|Automação e Desejo de Escala]]
- [[_COMMUNITY_Tutorial Rápido e Auditoria|Tutorial Rápido e Auditoria]]
- [[_COMMUNITY_Erro Comum Faturamento vs Automação|Erro Comum: Faturamento vs Automação]]

## God Nodes (most connected - your core abstractions)
1. `Análise de Perfis Instagram — 2026-06-24` - 23 edges
2. `Resumo Semanal — 2026-06-24` - 19 edges
3. `Benchmark de Conteúdo — 2026-06-24` - 18 edges
4. `Análise Profunda do Top 10 — 2026-06-24` - 17 edges
5. `Insights e Aplicação ao Negócio — 2026-06-24` - 17 edges
6. `Modelos de Conteúdo — 2026-06-24` - 12 edges
7. `Tendências — 2026-06-24` - 11 edges
8. `Módulo 5 — Modelos de Conteúdo` - 10 edges
9. `Exportação Notion — 2026-06-24` - 10 edges
10. `monitor/run.md — Orquestrador Principal` - 9 edges

## Surprising Connections (you probably didn't know these)
- `Relatório 01-tendencias.md (2026-06-17)` --implements--> `Template — report-trends.md`  [INFERRED]
  reports/2026-06-17/01-tendencias.md → monitor/templates/report-trends.md
- `Relatório 02-perfis-instagram.md (2026-06-17)` --implements--> `Template — report-instagram.md`  [INFERRED]
  reports/2026-06-17/02-perfis-instagram.md → monitor/templates/report-instagram.md
- `Framework: Nome de Sistema/Método + Resultado Numérico + Prazo` --implements--> `Modelo de Conteúdo: case_real`  [INFERRED]
  reports/2026-06-17/04-top10-analise.md → monitor/modules/05-content-models.md
- `Framework: Contraste/Negação de Crença Popular` --implements--> `Modelo de Conteúdo: opiniao_forte`  [INFERRED]
  reports/2026-06-17/04-top10-analise.md → monitor/modules/05-content-models.md
- `Relatório 06-aplicacao-negocio.md (2026-06-17)` --implements--> `Template — report-insights.md`  [INFERRED]
  reports/2026-06-17/06-aplicacao-negocio.md → monitor/templates/report-insights.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Pipeline Sequencial dos Módulos 1-8 do Monitor** — 01_trends_modulo1, 02_instagram_modulo2, 03_benchmark_modulo3, 04_top10_analysis_modulo4, 05_content_models_modulo5, 06_business_apply_modulo6, 07_obsidian_export_modulo7, 08_notion_export_modulo8 [EXTRACTED 0.95]
- **Frameworks Reutilizáveis Identificados no Módulo 4** — framework_nomeacao_fenomeno, framework_nome_sistema_resultado, framework_cta_baixo_atrito, framework_contraste_crenca, framework_pergunta_retorica_escala, framework_poder_ate_que, framework_minimo_viavel [EXTRACTED 0.90]
- **Top 5 Ideias de Conteúdo Prontas para Produção (2026-06-17)** — ideia_verdade_sobre_automacao, ideia_sistema_monitora_50_perfis, ideia_prompt_para_criar_agentes, ideia_conteudo_pronto_dormindo, ideia_risco_agentes_ia [EXTRACTED 0.95]

## Communities (13 total, 0 thin omitted)

### Community 0 - "Tendências e Exportação de Dados"
Cohesion: 0.13
Nodes (23): Módulo 1 — Monitoramento de Tendências, Módulo 7 — Exportação para Obsidian, Módulo 8 — Exportação para Notion, Relatório 01-tendencias.md (2026-06-17), Relatório 06-aplicacao-negocio.md (2026-06-17), RESUMO.md (2026-06-17), Framework: Contraste/Negação de Crença Popular, Framework: 'Poder... até que...' (Alerta de Risco Oculto) (+15 more)

### Community 1 - "Configuração e Infraestrutura do Monitor"
Cohesion: 0.16
Nodes (23): Case Flora — US$ 42M com cobrança por uso, .claude/skills/swarm/SKILL.md, config/business.json, config/obsidian.json, config/sources.json, Lacuna de mercado: segurança de agentes/MCP em português, monitor/ (sistema de monitoramento de Lucas), monitor/modules/06-business-apply.md (+15 more)

### Community 2 - "Benchmark e Frameworks de Oferta"
Cohesion: 0.26
Nodes (13): Framework: Aforismo de contraste A vs. B, Framework: CTA por palavra-chave → entrega via DM, Framework: Falsa dicotomia + reframe, Framework: Lista numerada did you know + lead magnet, Framework: Tese forte + urgência de mercado, Ideia: A Nova Corrida do Ouro das Agências, Modelo de conteúdo: oferta_gratuita_dm, @avora.ai (+5 more)

### Community 3 - "Monitoramento Instagram e Templates"
Cohesion: 0.31
Nodes (10): Módulo 2 — Monitoramento de Perfis Instagram, Módulo 3 — Benchmark de Conteúdo, Módulo 6 — Aplicação ao Negócio, Relatório 02-perfis-instagram.md (2026-06-17), config/README.md, Skill instagram-content-cloner, Modo Análise (perfis ativos), Modo Descoberta (perfis vazios) (+2 more)

### Community 4 - "Perfis Instagram Monitorados"
Cohesion: 0.22
Nodes (9): config/profiles.json, monitor/modules/02-instagram.md, @gabrielsamp.ai, @marketerhub.ai, @neuwebstudio, @sebintel, @vendedorglobal, reports/2026-06-17/ (relatório da semana anterior) (+1 more)

### Community 5 - "Modelos e Frameworks de Conteúdo"
Cohesion: 0.38
Nodes (7): Módulo 5 — Modelos de Conteúdo, Relatório 05-modelos-conteudo.md (2026-06-17), Framework: CTA de Baixo Atrito (Comentar Palavra-chave → DM), Framework: Mínimo Viável (Redução de Complexidade), Modelo de Conteúdo: case_real, Modelo de Conteúdo: lista_checklist, Modelo de Conteúdo: tutorial_rapido

### Community 6 - "Ideias de Conteúdo e Perfis"
Cohesion: 0.38
Nodes (7): Ideia: 7 Recursos Escondidos do Claude Code, Ideia: A Pergunta Errada Sobre Ferramentas de IA, Modelo de conteúdo: lista_checklist, Modelo de conteúdo: opiniao_forte, @brandsdecoded__ (handle corrigido), @charliehills, @ninja_automacoes (handle corrigido)

### Community 7 - "Storytelling e POV"
Cohesion: 0.33
Nodes (6): Modelo de conteúdo: pov, Modelo de conteúdo: storytelling, monitor/modules/05-content-models.md, @allesinisgalli, @ana.gsoares, Modelos de Conteúdo — 2026-06-24

### Community 8 - "Análise Top 10 e Frameworks"
Cohesion: 0.50
Nodes (5): Módulo 4 — Análise Profunda dos Top 10 Conteúdos, Relatório 03-benchmark.md (2026-06-17), Relatório 04-top10-analise.md (2026-06-17), Framework: Nomeação de Fenômeno + Transição De X Para Y, Conteúdo: 'SMMA to AI Agencies - The New Gold Rush!'

### Community 9 - "Prova Social e Case Real"
Cohesion: 0.40
Nodes (5): Framework: Nome de Sistema/Método + Resultado Numérico + Prazo, Ideia de Conteúdo: O prompt que eu uso pra criar agentes, Ideia de Conteúdo: O sistema que monitora 50 perfis de IA por mim, Insight: Sistema monitor/ como Prova Social (case_real), Conteúdo: 'The N8N Instagram Parasite System'

### Community 10 - "Automação e Desejo de Escala"
Cohesion: 0.67
Nodes (4): Framework: Pergunta Retórica Ligada a Desejo de Escala, Ideia de Conteúdo: Conteúdo pronto enquanto você dorme, Modelo de Conteúdo: pov, Conteúdo: 'Quer fazer seu agente de IA vender enquanto você dorme?'

### Community 11 - "Tutorial Rápido e Auditoria"
Cohesion: 0.67
Nodes (4): Ideia: O Prompt Que Audita Sua Oferta, Modelo de conteúdo: tutorial_rapido, @brun0gpt, @larissagomes.ia

### Community 12 - "Erro Comum: Faturamento vs Automação"
Cohesion: 1.00
Nodes (3): Ideia: Faturamento vs. Automação — O Erro Que Todo Empreendedor Comete, Modelo de conteúdo: erro_comum, @franklim.gui

## Ambiguous Edges - Review These
- `Framework: Mínimo Viável (Redução de Complexidade)` → `Framework: CTA de Baixo Atrito (Comentar Palavra-chave → DM)`  [AMBIGUOUS]
  reports/2026-06-17/04-top10-analise.md · relation: semantically_similar_to
- `Case Flora — US$ 42M com cobrança por uso` → `Lacuna de mercado: segurança de agentes/MCP em português`  [AMBIGUOUS]
  reports/2026-06-24/06-aplicacao-negocio.md · relation: conceptually_related_to

## Knowledge Gaps
- **23 isolated node(s):** `Skill Swarm (processamento paralelo)`, `Skill daydream`, `Tendência: Fim do Pricing por Assento (SaaS) até 2028`, `Insight: Sistema monitor/ como Prova Social (case_real)`, `Modelo oferta_gratuita_dm` (+18 more)
  These have ≤1 connection - possible missing edges or undocumented components.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `Framework: Mínimo Viável (Redução de Complexidade)` and `Framework: CTA de Baixo Atrito (Comentar Palavra-chave → DM)`?**
  _Edge tagged AMBIGUOUS (relation: semantically_similar_to) - confidence is low._
- **What is the exact relationship between `Case Flora — US$ 42M com cobrança por uso` and `Lacuna de mercado: segurança de agentes/MCP em português`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **Why does `Análise de Perfis Instagram — 2026-06-24` connect `Perfis Instagram Monitorados` to `Configuração e Infraestrutura do Monitor`, `Benchmark e Frameworks de Oferta`, `Ideias de Conteúdo e Perfis`, `Storytelling e POV`, `Tutorial Rápido e Auditoria`, `Erro Comum: Faturamento vs Automação`?**
  _High betweenness centrality (0.005) - this node is a cross-community bridge._
- **Why does `Relatório 06-aplicacao-negocio.md (2026-06-17)` connect `Tendências e Exportação de Dados` to `Prova Social e Case Real`, `Automação e Desejo de Escala`?**
  _High betweenness centrality (0.005) - this node is a cross-community bridge._
- **Why does `Benchmark de Conteúdo — 2026-06-24` connect `Benchmark e Frameworks de Oferta` to `Configuração e Infraestrutura do Monitor`, `Perfis Instagram Monitorados`, `Ideias de Conteúdo e Perfis`, `Storytelling e POV`, `Tutorial Rápido e Auditoria`, `Erro Comum: Faturamento vs Automação`?**
  _High betweenness centrality (0.004) - this node is a cross-community bridge._
- **What connects `Skill Swarm (processamento paralelo)`, `Skill daydream`, `Tendência: Fim do Pricing por Assento (SaaS) até 2028` to the rest of the system?**
  _24 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Tendências e Exportação de Dados` be split into smaller, more focused modules?**
  _Cohesion score 0.12648221343873517 - nodes in this community are weakly interconnected._