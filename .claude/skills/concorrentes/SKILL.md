---
name: concorrentes
description: Análise de concorrentes da Neovertix com outlier score (≥3x a média de views) e extração de frameworks de ganchos pros bancos de hooks. Use quando o Lucas pedir /concorrentes, "analisa os concorrentes", "o que está performando no nicho" ou "atualiza os bancos de hooks".
argument-hint: "[perfil específico ou vazio para rodada completa]"
user-invocable: true
---

# /concorrentes — Radar analisa e popula os bancos

Atalho pro módulo 11 do sistema de marketing (`Social mídia IA/modules/11-concorrentes-outlier.md`).

## Passos

1. Verifique se o módulo 11 já existe em `Social mídia IA/modules/`. **Se ainda não existir (Sprint 3 pendente):** avise o Lucas que o módulo completo entra no Sprint 3 e ofereça a alternativa parcial — rodar o agente `radar` diretamente sobre os relatórios mais recentes de `reports/YYYY-MM-DD/` (02-perfis, 03-benchmark, 04-top10) que já existirem.
2. **Lance o agente `radar`** (Agent tool) com o escopo (perfil específico do argumento, ou rodada completa) e a instrução de seguir o módulo 11 / regras base do próprio agente.
3. O Radar identifica outliers (≥3x a média das últimas ~30 postagens do próprio perfil), extrai FRAMEWORKS (nunca texto literal) e popula `Social mídia IA/bancos/hooks-concorrentes.md` e `hooks-fora-do-nicho.md` com adaptação Neovertix.
4. **Apresente ao Lucas:** quantos outliers encontrados, os 3 frameworks mais fortes com a adaptação proposta, e o que entrou nos bancos.

## Regras

- Performance relativa sempre (vs. média do próprio perfil), nunca views absolutas.
- Se `config/profiles.json` ainda não tiver perfis com categoria `fora-do-nicho`, lembre o Lucas de indicar 5-10 perfis de outros nichos.
- Português brasileiro.