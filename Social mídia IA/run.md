# Sistema de Marketing IA — Orquestrador

> Camada de **produção e distribuição** de conteúdo da Neovertix. A camada de inteligência é o `monitor/` (módulos 01-08) — este sistema consome os relatórios de `reports/YYYY-MM-DD/`. Gate inegociável: `_sop/aprovacao.md` — nada publica sem OK do Lucas.

## Mapa do sistema

| Camada | Onde | O que faz |
|---|---|---|
| Inteligência | `monitor/` (01-08) | tendências, perfis, benchmark, top10, modelos, aplicação, exports |
| Produção | `Social mídia IA/modules/` (10-19) | notícias→ângulos, concorrentes→hooks, salvos→roteiros, roteiros, QA, carrosséis, criativos, vídeo, campanha, OPR |
| Braço Python | `ig-saves-engine/` | sync de salvos do IG (por pasta) + publicação com gate `aprovado` — hoje só Instagram; **meta é multirede (prioridade Instagram+TikTok) via Metricool no Sprint 6** |
| Squad | `.claude/agents/` | 11 agentes nomeados (org chart no CLAUDE.md) |
| Memória | `_context/` + vault Obsidian | marca, tom de voz vivo, viralização, sazonalidades |

## Módulos (status de implementação)

| # | Módulo | Agente | Status |
|---|---|---|---|
| 10 | Notícias com ângulos (polêmico/educacional/storytelling) | Notícia | ✅ ativo |
| 11 | Concorrentes + outlier ≥3x + bancos de hooks | Radar | ✅ ativo |
| 12 | Salvos do IG → roteiros no tom de voz | Roteira | Sprint 2 |
| 13 | Geração de roteiros | Roteira | ✅ ativo |
| 14 | Análise de roteiro (score 0-10, corte ≥7) | Iana | ✅ ativo |
| 15 | Carrosséis (estático + animado) | Pixel | ✅ ativo |
| 16 | Criativos de imagem (Pillow-first) | Pixel | ✅ ativo |
| 17 | Vídeo: cortes SRT-driven | Corta | Sprint 5 |
| 18 | Calendário de campanha + sazonalidades | Mapeia | ✅ ativo |
| 19 | OPR / relatório de performance | Mede | Sprint 5 |

## Fluxo padrão de um conteúdo

```
insumo (salvos | notícia | banco | campanha | ideia)
  → Roteira escreve (mód. 13, template _templates/roteiro.md)
  → Iana avalia (mód. 14): ≥7 passa | <7 volta (máx. 2 rodadas)
  → [formato carrossel/foto] Pixel produz criativo (15/16)
  → [formato reel] gravação → Corta edita (17)
  → Posta prepara card no Notion com preview + auditoria (_sop/aprovacao.md)
  → LUCAS aprova (único gate humano obrigatório)
  → publicação (ig-saves-engine | Metricool) → status publicado
  → Mede registra resultado → realimenta tom-de-voz.md e bancos (19)
```

## Regras herdadas

- Skill Swarm: sempre com as regras obrigatórias do CLAUDE.md (concurrency 3, batchSize 5, retry, schema estrito).
- Todo entregável em português brasileiro.
- Cada módulo confere se seu insumo existe antes de rodar (ex: mód. 13 sem bancos populados → usa seeds de hooks-proprios.md).
- Saídas datadas em `producao/{tipo}/YYYY-MM-DD/`.

## Comandos rápidos (skills locais)

| Comando | Faz |
|---|---|
| `/roteiro {ideia ou fonte}` | Módulo 13 + 14 encadeados (Roteira escreve, Iana avalia) |
| `/concorrentes` | Módulo 11 (Radar — requer Sprint 3) |
| `/campanha {mês \| 15d \| semana}` | Módulo 18 (Mapeia — requer Sprint 4) |
| `/opr` | Módulo 19 (Mede — requer Sprint 5) |
