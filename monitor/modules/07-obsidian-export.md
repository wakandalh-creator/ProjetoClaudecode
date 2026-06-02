# Módulo 7 — Exportação para Obsidian

Transforma os relatórios do dia em **notas atômicas** no vault Obsidian, prontas para
conexão pela skill `daydream` no futuro.

## Dependências

Requer que existam na pasta `reports/YYYY-MM-DD/`:
- `01-tendencias.md`
- `06-aplicacao-negocio.md`
- `RESUMO.md`

## Passo 0 — Carregar configuração

Leia `config/obsidian.json` e registre:
- `VAULT_PATH` — caminho do vault
- `FOLDERS` — mapeamento de subpastas
- `TAGS` — tags base por tipo de nota
- `MIN_RELEVANCE` — nível mínimo para exportar tendências ("alto" | "medio" | "baixo")

Se `enabled` for `false`, encerre o módulo e informe o usuário.

## Passo 1 — Criar estrutura de pastas

```powershell
New-Item -ItemType Directory -Force -Path "$VAULT_PATH/Monitor/Tendencias"
New-Item -ItemType Directory -Force -Path "$VAULT_PATH/Monitor/Ideias"
New-Item -ItemType Directory -Force -Path "$VAULT_PATH/Monitor/Insights"
New-Item -ItemType Directory -Force -Path "$VAULT_PATH/Monitor/Perfis"
New-Item -ItemType Directory -Force -Path "$VAULT_PATH/Monitor/Daily"
```

## Passo 2 — Extrair dados dos relatórios

### 2a. Tendências (de `01-tendencias.md`)
Para cada tendência com relevância >= `MIN_RELEVANCE`, extraia:
- `titulo` — nome curto da tendência
- `descricao` — 2-3 frases explicando a tendência
- `topico` — categoria (ex: IA Generativa, Agentes, Marketing)
- `relevancia` — alto | medio | baixo
- `fontes` — lista das fontes onde apareceu
- `oportunidade` — se houver oportunidade identificada no relatório

### 2b. Ideias de conteúdo (de `06-aplicacao-negocio.md`)
Para cada uma das 5 ideias do Bloco C, extraia:
- `titulo` — título da ideia
- `formato` — tipo de post (ex: carrossel, reels, single)
- `hook` — primeira linha do post
- `estrutura` — os 6 passos
- `cta` — chamada para ação
- `modelo_base` — perfil de referência
- `texto_completo` — texto gerado na Fase 2 (se disponível)

### 2c. Insights estratégicos (de `06-aplicacao-negocio.md` Bloco D + E)
Para cada insight ou oportunidade de nicho identificada, extraia:
- `titulo` — nome curto do insight
- `descricao` — o que foi identificado
- `acao` — próxima ação recomendada (do Bloco E)

### 2d. Perfis Instagram (de `02-perfis-instagram.md`, se existir)
Para cada perfil analisado, extraia:
- `handle` — @perfil
- `nicho` — categoria do perfil
- `destaques` — 2-3 pontos principais da análise

## Passo 3 — Gerar notas de tendências

Para cada tendência extraída, crie o arquivo:
**Caminho:** `{VAULT_PATH}/Monitor/Tendencias/{YYYYMMDD}-{slug}.md`

Gere o `slug`: lowercase, espaços → hífens, sem caracteres especiais, máx 50 chars.

**Template:**
```markdown
---
date: YYYY-MM-DD
type: tendencia
topico: "{topico}"
relevancia: "{relevancia}"
tags: [monitor, ia, tendencia, {topico-slug}]
fonte_relatorio: "[[Monitor/Daily/{YYYY-MM-DD}-monitor|Monitor {YYYY-MM-DD}]]"
---

# {titulo}

{descricao}

## Por que importa

{oportunidade — se não houver, escreva 1 frase sobre o impacto para criadores de conteúdo com IA}

## Fontes

{lista de fontes como bullets}

## Conexões possíveis

- Relacionado a: (deixe em branco — o daydream vai preencher)
```

## Passo 4 — Gerar notas de ideias de conteúdo

Para cada ideia, crie:
**Caminho:** `{VAULT_PATH}/Monitor/Ideias/{YYYYMMDD}-{slug}.md`

**Template:**
```markdown
---
date: YYYY-MM-DD
type: ideia-conteudo
formato: "{formato}"
modelo_base: "{modelo_base}"
tags: [monitor, ia, ideia-conteudo, instagram, {formato-slug}]
fonte_relatorio: "[[Monitor/Daily/{YYYY-MM-DD}-monitor|Monitor {YYYY-MM-DD}]]"
---

# {titulo}

**Formato:** {formato}
**Hook:** {hook}

## Estrutura

{estrutura — cada passo em um item de lista}

## CTA

{cta}

## Texto completo

{texto_completo — se disponível; caso contrário, omita esta seção}

## Referência

Baseado em: {modelo_base}
```

## Passo 5 — Gerar notas de insights estratégicos

Para cada insight, crie:
**Caminho:** `{VAULT_PATH}/Monitor/Insights/{YYYYMMDD}-{slug}.md`

**Template:**
```markdown
---
date: YYYY-MM-DD
type: insight
tags: [monitor, ia, insight, estrategia]
fonte_relatorio: "[[Monitor/Daily/{YYYY-MM-DD}-monitor|Monitor {YYYY-MM-DD}]]"
---

# {titulo}

{descricao}

## Próxima ação

{acao}

## Conexões possíveis

- Relacionado a: (deixe em branco — o daydream vai preencher)
```

## Passo 6 — Atualizar notas de perfis Instagram

Para cada perfil, verifique se já existe `{VAULT_PATH}/Monitor/Perfis/{handle}.md`.

**Se não existir**, crie:
```markdown
---
type: perfil-instagram
handle: "{handle}"
nicho: "{nicho}"
primeira_analise: YYYY-MM-DD
ultima_analise: YYYY-MM-DD
tags: [monitor, instagram, perfil, {nicho-slug}]
---

# {handle}

**Nicho:** {nicho}

## Análise — {YYYY-MM-DD}

{destaques}
```

**Se já existir**, adicione uma nova seção `## Análise — {YYYY-MM-DD}` com os destaques do dia, sem apagar o histórico anterior.

## Passo 7 — Gerar nota MOC do dia

Crie o índice diário com links para tudo que foi gerado:
**Caminho:** `{VAULT_PATH}/Monitor/Daily/{YYYY-MM-DD}-monitor.md`

```markdown
---
date: YYYY-MM-DD
type: monitor-daily
tags: [monitor, daily, ia]
tendencias_exportadas: {N}
ideias_exportadas: {N}
insights_exportados: {N}
---

# Monitor {YYYY-MM-DD}

Execução completa do sistema de monitoramento de tendências e Instagram.

## Tendências ({N})

{Para cada tendência, uma linha:}
- [[Monitor/Tendencias/{YYYYMMDD}-{slug}|{titulo}]] — {relevancia}

## Ideias de Conteúdo ({N})

{Para cada ideia, uma linha:}
- [[Monitor/Ideias/{YYYYMMDD}-{slug}|{titulo}]] — {formato}

## Insights ({N})

{Para cada insight, uma linha:}
- [[Monitor/Insights/{YYYYMMDD}-{slug}|{titulo}]]

## Perfis analisados

{Para cada perfil, uma linha:}
- [[Monitor/Perfis/{handle}|{handle}]] — {nicho}

## Relatório completo

Arquivos em `reports/{YYYY-MM-DD}/`:
- 01-tendencias.md, 02-perfis-instagram.md, 03-benchmark.md
- 04-top10-analise.md, 05-modelos-conteudo.md
- 06-aplicacao-negocio.md, RESUMO.md
```

## Passo 8 — Resumo final

Informe ao usuário:

```
📓 Obsidian atualizado — {DATA}

Notas criadas em {VAULT_PATH}/Monitor/:
• {N} tendências  → Monitor/Tendencias/
• {N} ideias      → Monitor/Ideias/
• {N} insights    → Monitor/Insights/
• {N} perfis      → Monitor/Perfis/
• 1 índice diário → Monitor/Daily/{DATA}-monitor.md

Após ~4 execuções semanais você terá notas suficientes
para rodar /daydream e descobrir conexões não-óbvias.
```

## Tratamento de erros

- **Vault path não existe:** Criar as pastas automaticamente via `New-Item -Force`. Se falhar por permissão, avisar o usuário e sugerir que verifique o `vault_path` em `config/obsidian.json`.
- **Relatório incompleto:** Se `06-aplicacao-negocio.md` não existir, exportar apenas tendências do módulo 01.
- **Nota já existe:** Nunca sobrescrever — adicionar sufixo `-v2`, `-v3`, etc. Exceção: perfis Instagram (sempre atualizar via append).
