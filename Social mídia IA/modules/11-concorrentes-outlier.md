# Módulo 11 — Concorrentes + Outlier (agente: Radar)

## Objetivo

Analisar os perfis monitorados em `config/profiles.json`, detectar outliers de performance (≥3x a média das últimas ~30 postagens do PRÓPRIO perfil — nunca views absolutas), extrair o FRAMEWORK de cada outlier (nunca o texto literal) e popular `bancos/hooks-concorrentes.md` (e `hooks-fora-do-nicho.md`, quando aplicável).

## Entrada

- `config/profiles.json` — 61 perfis monitorados, categorias atuais: `creator`, `founder`, `marketing`, `ia`, `negocio-digital`, `automacao`, `agencia`. A categoria `fora-do-nicho` ainda NÃO existe no arquivo — ver Passo 4.
- Relatórios mais recentes em `reports/YYYY-MM-DD/`: `02-perfis-instagram.md`, `03-benchmark.md`, `04-top10-analise.md` (gerados pelo monitor, módulos 02-04). Não refazer scraping — esses relatórios são a fonte de dados de performance.

## Contexto obrigatório

1. `Social mídia IA/_context/marca.md` — pilares, ICP, números âncora
2. `Social mídia IA/_context/tom-de-voz.md` — base + banidas (toda adaptação passa por aqui)
3. `Social mídia IA/bancos/hooks-concorrentes.md` e `hooks-fora-do-nicho.md` — formato de entrada e o que já foi extraído (não duplicar)

## Instrução

### Passo 1 — Checar frescor

- Localizar a pasta `reports/YYYY-MM-DD/` mais recente que contenha `02-perfis-instagram.md`, `03-benchmark.md` e `04-top10-analise.md`.
- Se nenhum relatório existir: avisar o Lucas ("nenhum relatório de perfis/benchmark encontrado — rode `monitor/run.md` (módulos 02-04) antes de rodar o módulo 11") e parar.
- Se o relatório mais recente tiver mais de 7 dias: avisar ("relatório de perfis/benchmark tem N dias, outliers podem estar desatualizados — sugiro rodar `monitor/run.md` antes") e só prosseguir com confirmação do Lucas.

### Passo 2 — Calcular outlier score

- Para cada perfil ativo (`active: true`) em `profiles.json`, usar os dados de `02-perfis-instagram.md` / `03-benchmark.md` / `04-top10-analise.md` pra montar a média de views das últimas ~30 postagens DO PRÓPRIO perfil.
- Um post é outlier se `views_do_post ≥ 3x média_do_próprio_perfil`. Performance é sempre relativa ao perfil — nunca comparar views absolutas entre perfis diferentes (perfil grande e pequeno não são comparáveis).
- Se os relatórios não tiverem dado suficiente pra calcular a média (perfil novo, histórico curto): pular o perfil e registrar na saída ("perfil @X sem histórico suficiente — pulado").

### Passo 3 — Extrair framework

- Para cada outlier confirmado: identificar a ESTRUTURA do gancho (não o texto), por que funcionou, e a emoção disparada.
- Nunca copiar texto literal do concorrente — a entrada no banco é sempre a estrutura reutilizável com variáveis, no mesmo padrão de `hooks-proprios.md`.
- Validar a adaptação Neovertix contra `tom-de-voz.md` (banidas, léxico) antes de registrar.

### Passo 4 — Fora do nicho (bloqueio conhecido)

- A categoria `fora-do-nicho` não existe em `config/profiles.json` hoje.
- Se não houver perfis com essa categoria: **pular essa parte do módulo com aviso explícito** ao Lucas ("sem perfis fora-do-nicho cadastrados — indique 5-10 perfis fora do nicho de IA/automação pra eu minerar ângulos que ninguém no nicho usa") em vez de falhar ou improvisar com perfis do nicho.
- Quando existirem perfis fora-do-nicho: mesmo método dos Passos 2-3, mas a entrada em `hooks-fora-do-nicho.md` inclui por que o padrão TRANSFERE pro nicho da Neovertix.

### Passo 5 — Popular os bancos

- Adicionar cada framework extraído em `Social mídia IA/bancos/hooks-concorrentes.md`, formato: **Framework** · **Fonte** (@handle, link, performance vs. média) · **Adaptação Neovertix** · **Emoção** · **Confiança** (nível de evidência por trás da entrada — de "outlier numérico confirmado ≥3x" até "hipótese, sinal fraco/n baixo"; nunca apresentar uma entrada sem deixar claro o quão sólida é a evidência).
- Não duplicar frameworks já presentes (mesma estrutura essencial) — se já existir, atualizar fonte/performance/confiança em vez de criar entrada nova.

### Passo 6 — Reportar

Informar o Lucas: quantos perfis analisados, quantos outliers encontrados, quantos frameworks novos entraram no banco, e o status do bloqueio fora-do-nicho (se aplicável).

## Regras

- Outlier é sempre relativo ao próprio perfil — nunca ranking de views absolutas entre perfis.
- Nunca copiar texto literal — só estrutura/framework.
- Nunca inventar performance ou dado que não está nos relatórios do monitor.
- Fora-do-nicho pendente = aviso e pular, nunca falha silenciosa nem invenção de perfil.
