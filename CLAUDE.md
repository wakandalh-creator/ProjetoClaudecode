# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## GitHub Repository

**URL:** https://github.com/wakandalh-creator/ProjetoClaudecode

### Auto-sync

Every file created or edited via Claude Code is automatically committed and pushed to GitHub via a `PostToolUse` hook configured in `.claude/settings.local.json`.

The hook runs `.claude/auto-sync.ps1` after every `Write` or `Edit` tool call. The script:
1. Checks for uncommitted changes (`git status --porcelain`)
2. Stages all changes (`git add -A`)
3. Commits with a timestamp message (`Auto-sync: YYYY-MM-DD HH:mm:ss`)
4. Pushes to `origin HEAD`

### Manual sync

To push manually from a terminal:

```powershell
git add -A
git commit -m "sua mensagem"
git push
```

## Configuration

Claude Code settings and the auto-sync script are in `.claude/`. The file `.claude/settings.local.json` is excluded from git (via `.gitignore`) since it may contain local-only permissions.

## Swarm Skill — Regras Obrigatórias de Segurança

Sempre que usar a skill `swarm`, aplicar TODAS as regras abaixo sem exceção:

### 1. `responseSchema` sempre estrito
- Usar `enum` para campos com valores fixos (sentimento, categoria, status)
- Usar `type: "string"` com descrição clara para campos livres
- Nunca omitir `required` — listar todos os campos obrigatórios
- Nunca usar `additionalProperties: true`

```javascript
responseSchema: {
  type: "object",
  additionalProperties: false,
  properties: {
    categoria: { type: "string", enum: ["A", "B", "C"] },
    resumo: { type: "string", description: "Máximo 2 frases." },
  },
  required: ["categoria", "resumo"],
}
```

### 2. Concorrência máxima: 3
```javascript
concurrency: 3  // nunca aumentar sem aprovação explícita do usuário
```

### 3. `subagentType` apenas quando estritamente necessário
- Omitir para: classificação, extração, resumo, análise de texto
- Usar apenas quando: o sub-agente precisa ler arquivos ou executar múltiplos passos

### 4. Sempre incluir `context` para ancorar o modelo
```javascript
context: "Responda apenas com base nos dados fornecidos. Não invente informações."
```

### 5. Sempre implementar retry após o `run` inicial
```javascript
await run(table.id, {
  ...opcoesOriginais,
  filter: { column: "campoObrigatorio", exists: false },
});
```

### 6. Nunca logar conteúdo bruto — apenas contagens e amostras curtas
### 7. Nunca escrever em `.swarm/` diretamente — sempre usar `create()`
### 8. `batchSize` padrão: 5 (nunca acima de 10 sem aprovação)
### 9. Validar resultado com `rows()` antes de considerar a tarefa concluída

---

## Sistema de Monitoramento de Tendências + Instagram

O projeto possui uma rotina completa de inteligência de mercado em `monitor/`.

### Comandos rápidos

| O que fazer | Comando para o Claude |
|-------------|----------------------|
| Rodar o monitor completo | `Execute o monitor — leia monitor/run.md` |
| Só tendências | `Execute apenas o Módulo 1 — leia monitor/modules/01-trends.md` |
| Só Instagram | `Execute apenas o Instagram — leia monitor/modules/02-instagram.md` |
| Benchmark de conteúdo | `Execute apenas o Módulo 3 — leia monitor/modules/03-benchmark.md` |
| Só exportar para Obsidian | `Execute apenas o Módulo 7 — leia monitor/modules/07-obsidian-export.md` |
| Ver último relatório | `Abra o relatório mais recente em reports/` |
| Adicionar perfil Instagram | `Adicione @handle em config/profiles.json na categoria X` |
| Atualizar posicionamento | `Atualize config/business.json com meu foco atual` |
| Mudar caminho do vault | `Atualize vault_path em config/obsidian.json` |
| Gerar imagens dos posts | `Gere as imagens para os posts do relatório de hoje usando instagram-content-cloner` |
| Agendar rotina semanal | `/schedule Toda segunda-feira às 8h: execute o monitor — leia monitor/run.md` |
| Descobrir conexões no vault | `/daydream` (instalar: `npx skills add git@github.com:glebis/claude-skills.git@daydream -g -y`) |

### Estrutura de arquivos

```
config/
  business.json      ← posicionamento, nicho, tom, ofertas
  sources.json       ← fontes de tendências e search queries
  profiles.json      ← perfis Instagram monitorados (edite aqui)
  obsidian.json      ← caminho do vault e configuração de exportação
  README.md          ← instruções de uso

monitor/
  run.md             ← orquestrador principal (ponto de entrada)
  modules/           ← instruções de cada módulo (01 a 07)
  templates/         ← templates dos relatórios

reports/
  YYYY-MM-DD/        ← relatórios gerados por data
    RESUMO.md        ← highlights consolidados (leia primeiro)
    06-aplicacao-negocio.md ← posts prontos para produção

[vault Obsidian]/Monitor/
  Daily/             ← índice diário (MOC) de cada execução
  Tendencias/        ← uma nota por tendência identificada
  Ideias/            ← uma nota por ideia de conteúdo gerada
  Insights/          ← uma nota por insight estratégico
  Perfis/            ← uma nota por perfil Instagram (histórico acumulado)
```

### Skills integradas

O sistema usa:
- `instagram-content-cloner` — Módulo 2 (Fase 1) e Módulo 6 (Fases 2-4)
- `daydream` — roda manualmente com `/daydream` após acumular ~50 notas no vault

Para geração de imagens, é necessário `GOOGLE_API_KEY` (gratuita em https://aistudio.google.com/apikey).

### Fluxo Obsidian + Daydream

```
Monitor semanal (run.md)
  └── Módulo 7 exporta notas atômicas para o vault
        └── Após ~4 semanas: /daydream descobre conexões entre notas
              └── Insights não-óbvios → novos ângulos de conteúdo
```
