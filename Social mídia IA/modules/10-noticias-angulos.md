# Módulo 10 — Notícias com Ângulos (agente: Notícia)

## Objetivo

Transformar as tendências/notícias do dia (relatório do monitor) em 3 ângulos de conteúdo prontos pra virar roteiro — sem refazer scraping, sem inventar dado.

## Entrada

Relatório mais recente em `reports/YYYY-MM-DD/01-tendencias.md` (gerado pelo monitor, módulo 01). Nenhuma outra fonte de notícias — o módulo não faz scraping próprio.

## Contexto obrigatório (ler antes de gerar os ângulos)

1. `Social mídia IA/_context/marca.md` — pilares de mensagem, ICP, números âncora
2. `Social mídia IA/_context/tom-de-voz.md` — base + léxico + banidas

## Instrução

### Passo 1 — Checar frescor

- Localizar a pasta mais recente em `reports/YYYY-MM-DD/` que contenha `01-tendencias.md`.
- Se não existir nenhum relatório: avisar o Lucas ("nenhum relatório de tendências encontrado — rode `monitor/run.md` ou ao menos o módulo 1 antes") e parar.
- Se o relatório mais recente tiver mais de 7 dias: avisar ("relatório de tendências tem N dias, pode estar desatualizado — sugiro rodar `monitor/run.md` antes de gerar ângulos") e só prosseguir com confirmação do Lucas.

### Passo 2 — Filtrar relevância

- Ler todas as notícias/tendências do relatório.
- Manter só as que respondem SIM a: "isso muda algo na operação/atendimento/vendas de um dono de PME BR (5-50 func.) ou de um criador/infoprodutor?" (ICP de `marca.md`).
- Descartar o resto — não forçar ângulo em notícia irrelevante pro ICP.

### Passo 3 — Gerar 3 ângulos por notícia relevante

Para cada notícia que passou o filtro, gerar:

- **Polêmico** — confronta uma crença do nicho (sem sensacionalismo; sóbrio como a marca)
- **Educacional** — ensina com autoridade o que a notícia significa na prática pro ICP
- **Storytelling** — conecta a notícia com a dor/desejo do ICP via história

Cada ângulo traz: gancho sugerido (1 linha) + mensagem central (1 frase) + pilar da marca que serve (rápido de verdade / engenharia não slide / risco zero).

### Passo 4 — Validar tom

Checar cada gancho contra a lista de banidas de `tom-de-voz.md`. Qualquer termo banido = reescrever antes de salvar.

### Passo 5 — Salvar e reportar

- Salvar em `Social mídia IA/producao/roteiros/YYYY-MM-DD/noticias-angulos.md` (data de hoje, não a do relatório-fonte). Uma seção por notícia relevante, 3 ângulos cada.
- Informar o Lucas: quantas notícias relevantes encontradas, caminho do arquivo. Ângulos escolhidos por ele viram roteiro completo via módulo 13 (Roteira).

## Regras

- Nunca inventar notícia ou dado — só o que está no relatório do monitor.
- Nunca pular a checagem de frescor.
- Ângulo Polêmico nunca vira sensacionalismo — a marca é sóbria mesmo confrontando uma crença.
- Se zero notícias passarem o filtro de relevância: informar o Lucas e não gerar arquivo vazio.
