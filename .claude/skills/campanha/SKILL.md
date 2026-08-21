---
name: campanha
description: Monta o calendário de campanha da Neovertix (mensal, 15 dias ou semanal) com funil de temas, formatos por dia e sazonalidades brasileiras. Use quando o Lucas pedir /campanha, "planeja o mês", "campanha da semana" ou "calendário de conteúdo".
argument-hint: "<mês | 15d | semana> [tema opcional]"
user-invocable: true
---

# /campanha — Mapeia planeja o período

Atalho pro módulo 18 do sistema de marketing (`Social mídia IA/modules/18-campanha.md`).

## Passos

1. Verifique se o módulo 18 já existe em `Social mídia IA/modules/`. **Se ainda não existir (Sprint 4 pendente):** avise o Lucas e ofereça a versão base — o agente `mapeia` planeja seguindo as regras do próprio agente (pilares equilibrados, funil topo→meio→fundo, encomendas pro roteira).
2. **Lance o agente `mapeia`** (Agent tool) com o período do argumento (mês/15d/semana) + tema opcional.
3. Saída esperada: `Social mídia IA/producao/campanhas/YYYY-MM/campanha.md` — tema central, calendário com formato por dia, mensagem central de cada slot, pilar da marca, e a lista de encomendas de roteiro.
4. **Apresente ao Lucas:** resumo do calendário + pergunte se quer já disparar os primeiros roteiros via `/roteiro`.

## Regras

- Nunca 2 posts de fundo de funil seguidos; os 3 pilares da marca aparecem no período.
- Sazonalidade só com conexão real com o ICP (dono de PME BR).
- Português brasileiro.