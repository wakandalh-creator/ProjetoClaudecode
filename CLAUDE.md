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
