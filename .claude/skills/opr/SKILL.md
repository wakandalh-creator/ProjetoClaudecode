---
name: opr
description: Gera o OPR (relatório de performance semanal) da Neovertix — resultados por post, padrões do que performou e recomendações; realimenta a memória de tom de voz e os bancos de hooks. Use quando o Lucas pedir /opr, "relatório de performance", "como foram os posts" ou "fecha a semana".
argument-hint: "[período opcional, padrão: últimos 7 dias]"
user-invocable: true
---

# /opr — Mede fecha o ciclo

Atalho pro módulo 19 do sistema de marketing (`Social mídia IA/modules/19-relatorio-performance.md`).

## Passos

1. Verifique se o módulo 19 já existe em `Social mídia IA/modules/`. **Se ainda não existir (Sprint 5 pendente):** avise o Lucas e ofereça a versão base — o agente `mede` roda com as regras do próprio agente.
2. **Antes de lançar o agente:** confirme com o Lucas se os posts do período já têm resultado marcado (flopou/comum/bom/viralizou) no kanban. Sem marcação, o OPR sai incompleto — liste os posts pendentes de marcação.
3. **Lance o agente `mede`** (Agent tool) com o período.
4. Saída esperada: `Social mídia IA/producao/campanhas/opr/YYYY-MM-DD.md` — publicados, resultado por post, outliers próprios (≥3x média), padrões observados, 3 recomendações pra próxima semana.
5. O Mede também atualiza: "Hipóteses em teste"/"Padrões validados" em `_context/tom-de-voz.md` (respeitando o mínimo de 10 posts marcados) e a seção "Validados" de `bancos/hooks-proprios.md`.
6. **Apresente ao Lucas:** o OPR resumido + o que mudou na memória da marca.

## Regras

- Métricas próprias vêm da marcação manual no kanban até o Metricool entrar — nunca de API frágil.
- Português brasileiro.