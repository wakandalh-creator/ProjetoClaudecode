# Módulo 18 — Calendário de Campanha (agente: Mapeia)

## Objetivo

Montar o calendário de uma campanha (mensal, 15 dias ou semanal) a partir de um tema central: distribuir formato por dia (reel/carrossel/post), balancear os 3 pilares de marca e organizar o funil topo (atenção/dor) → meio (mecanismo/prova) → fundo (oferta/CTA). Cada dia do calendário vira uma encomenda pronta pro módulo 13 (Roteira).

## Entrada

- Período pedido pelo Lucas (mês, 15 dias ou semana — com data de início quando relevante)
- Relatório mais recente do monitor: `reports/YYYY-MM-DD/05-modelos-conteudo.md` e `06-aplicacao-negocio.md`
- `Social mídia IA/bancos/hooks-proprios.md` e `hooks-concorrentes.md`
- `Social mídia IA/_context/sazonalidades-brasil.md` — só entra em jogo se o período cair perto de uma data listada lá

## Contexto obrigatório (ler antes de montar o calendário)

1. `Social mídia IA/_context/marca.md` — pilares de mensagem, ICP, números âncora, ofertas
2. `Social mídia IA/_context/tom-de-voz.md` — base + léxico + banidas
3. `Social mídia IA/_context/sazonalidades-brasil.md` — datas com conexão real com o ICP

## Instrução

### Passo 1 — Checar frescor do relatório do monitor

- Localizar a pasta mais recente em `reports/YYYY-MM-DD/` que contenha `05-modelos-conteudo.md` e `06-aplicacao-negocio.md`.
- Se nenhum relatório existir: avisar o Lucas ("nenhum relatório de modelos de conteúdo/aplicação ao negócio encontrado — rode `monitor/run.md` antes de montar a campanha") e parar.
- Se o relatório mais recente tiver mais de 7 dias: avisar ("relatório de modelos de conteúdo tem N dias, o tema central pode estar baseado em algo desatualizado — sugiro rodar `monitor/run.md` antes") e só prosseguir com confirmação do Lucas.

### Passo 2 — Definir o tema central do período

- A partir de `06-aplicacao-negocio.md` + pilares de `marca.md`, escolher 1 tema central que amarra o período inteiro (ex: "seu atendimento aguenta o pico?", "sistema, não malabarismo manual").
- Consultar `sazonalidades-brasil.md`: se o período cair perto (antes ou durante) de uma data listada, avaliar se dá pra amarrar o tema central a ela. Só amarrar se a conexão for natural — nunca forçar sazonalidade só porque a data existe no calendário.

### Passo 3 — Montar a grade de dias

Pra cada dia do período, definir:
- **Formato:** reel / carrossel / post
- **Etapa de funil:** topo (atenção/dor) / meio (mecanismo/prova) / fundo (oferta/CTA)
- **Pilar de marca:** rápido de verdade / engenharia, não slide / você não paga pra descobrir se funciona

Regras de distribuição:
- Nunca 2 dias de fundo de funil seguidos.
- Balancear os 3 pilares ao longo do período — nenhum pilar deve dominar mais da metade dos slots, salvo pedido explícito do Lucas.
- Funil deve progredir de forma coerente ao longo do período (mais topo no início, fundo concentrado perto de datas-chave ou do fim), não distribuído aleatoriamente.

### Passo 4 — Gerar a encomenda de cada slot

Cada slot do calendário vira uma encomenda completa pro módulo 13 (Roteira), com:
- **Mensagem central** (1 frase)
- **Pilar** da marca
- **Formato** (reel/carrossel/post)
- **Rede:** instagram (TikTok só entra quando Sprint 6/Metricool estiver pronto — ver `Social mídia IA/PROGRESSO.md`)
- **Etapa de funil**
- **Referência de banco:** nome do Framework de `hooks-proprios.md` ou `hooks-concorrentes.md` — nunca o texto de "Exemplo aplicado"/"Adaptação Neovertix" pronto. A Roteira instancia as variáveis na hora de escrever.

### Passo 5 — Salvar e reportar

- Salvar em `Social mídia IA/producao/campanhas/YYYY-MM/campanha.md` (a pasta `producao/campanhas/` ainda não existe — criar ao gerar a primeira campanha).
- Informar o Lucas: período coberto, tema central, quantos slots, distribuição de pilares e de funil, e relatório-fonte usado (com data).
- Mencionar que existe espelho opcional no Notion (calendário) como possibilidade futura — não implementado ainda, só documentado.

## Saída

`Social mídia IA/producao/campanhas/YYYY-MM/campanha.md`, com:
- Cabeçalho: período, tema central, relatório-fonte (com data), sazonalidade usada (se houver)
- Uma linha/bloco por dia do calendário: data, formato, etapa de funil, pilar, mensagem central, referência de banco
- Cada slot pronto pra ser passado individualmente ao módulo 13 quando o Lucas decidir produzir

## Regras

- Nunca 2 posts de fundo de funil seguidos.
- Balancear os 3 pilares da marca ao longo do período.
- Sazonalidade só entra com conexão real (critério de `sazonalidades-brasil.md`) — nunca forçar data comemorativa sem relação com a dor/operação do ICP.
- Nunca pular a checagem de frescor do relatório do monitor.
- Referência de banco = nome do framework, nunca o texto pronto de exemplo/adaptação — quem instancia variável é a Roteira, não o Mapeia.
- TikTok não entra como rede até o Sprint 6/Metricool estar pronto.
- Se o relatório mais recente não tiver insumo suficiente pra sugerir tema central: avisar o Lucas e pedir direção manual em vez de inventar tema.
