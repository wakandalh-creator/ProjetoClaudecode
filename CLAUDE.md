# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## Memória Ativa (Hot Cache)

### Quem sou
Lucas — criador do ProjetoClaudecode. Trabalha com Claude Code para automação, monitoramento de tendências e conteúdo Instagram.

### Termos frequentes
| Termo | Significado |
|-------|-------------|
| **monitor** | Sistema de Monitoramento de Tendências + Instagram em `monitor/` |
| **relatório** | Saída do monitor em `reports/YYYY-MM-DD/` |
| **vault** | Vault Obsidian integrado ao monitor |
| **swarm** | Skill de processamento paralelo com sub-agentes |
| **claude mem** | Plugin claude-mem — reinstalado e validado em 2026-07-13 (v13.11.0). Causa raiz do crash (conflito de PATH entre shims npm do Bun e o binário real) corrigida; worker rodando saudável na porta 37778, backup de memórias restaurado. Segunda causa raiz de crash do worker encontrada e corrigida em 2026-07-14 (ver abaixo) |
| **pw** | Plugin playwright-pro (MCPs pw-testrail e pw-browserstack desativados) |
| **gpt maker** | MCP gptmaker (conectado) |
| **auto-sync** | Hook que commita/push automático a cada Write/Edit |
| **graphify** | Skill de knowledge graph (escopo: monitor/config/reports/CLAUDE.md). Atualização diária automática: nuvem (8h BRT, commita grafo + posta no Notion) → local (8h30 BRT, sincroniza vault Obsidian) |
| **hermes agent** | Agente autônomo standalone da Nous Research (`nousresearch/hermes-agent`) — não é skill do Claude Code. Instalado em `%LOCALAPPDATA%\hermes\hermes-agent`, comando `hermes` no PATH do usuário. v0.18.2, validado em 2026-07-16 |

### Setup rápido
- Windows + Node v24.15.0 + Claude Code **2.1.209**
- MCPs ativos: Cloudflare, gptmaker, sequential-thinking, context7 | Google Drive: pendente autenticar
- Backup claude-mem: `OneDrive\Documentos\claude-mem-backup.db`

### Correções aplicadas (2026-07-08)
- `~/.claude/settings.json` → PATH com `nvm/v24.15.0` adicionado na seção `env` (resolve `npx` para playwright, chrome-devtools, firecrawl)
- `.mcp.json` → sequential-thinking pinado no commit `527ba64d` (startup 26s → ~3s, sem rebuild)
- Health check preventivo: `.claude/scripts/mcp-health-check.ps1` — rodar quando suspeitar de problemas de MCP
- **Validado 2026-07-08 15:56** — health check 100% verde, todos os MCPs OK, zero crashes

### Correções aplicadas (2026-07-09)
- Cache do npx corrompido (`_npx\3edc2c0fb421219a`, pacote `twelvelabs-mcp`) causava erro de parse (`dist/index.js` truncado em 90 bytes) — apagado; próximo uso do MCP TwelveLabs rebaixa o pacote limpo.
- Terminal do VSCode preso em modo mouse-tracking (xterm SGR) após o crash do MCP acima, despejando sequências `[<btn;x;yM` na tela — resolvido fechando/reabrindo a aba do terminal.
- `~/.claude/settings.json` → PATH sem `C:\Users\lucas\.local\bin` fazia o MCP **sequential-thinking** falhar com `'uvx' não é reconhecido`. Adicionado ao `env.PATH`. Efeito só após reiniciar o VSCode/sessão.

### Correções aplicadas (2026-07-12)
- Crash do processo Claude Code (`exited with code 3221226505` / `0xC0000409`) causado por: (1) `pwsh` (PowerShell 7) ausente — parser da extensão caía no fallback `powershell.exe` 5.1 via `-EncodedCommand`, que travava/timeout e crashava; (2) erros `EUNKNOWN: unknown error, read` ao ler arquivos de skills — placeholders do OneDrive não baixados localmente.
- Corrigido: `pwsh` instalado via `winget install --id Microsoft.PowerShell -e`. Pasta do projeto fixada no OneDrive com `attrib +P -U /S /D` ("sempre manter neste dispositivo").
- Requer reiniciar o VSCode ("Reload Window") após instalar `pwsh` para a extensão pegar o PATH novo.

### Correções aplicadas (2026-07-13)
- **Causa raiz do crash do claude-mem no Windows identificada**: existiam duas instalações do Bun brigando pelo PATH — shims órfãos em `C:\Users\lucas\AppData\Roaming\npm\bun` / `bun.cmd` / `bun.ps1` (não pertenciam a nenhum pacote npm — `npm list -g` não os listava) e o binário real em `C:\Users\lucas\.bun\bin\bun.exe`. O `Get-Command bun` resolvia para o shim `bun.ps1`, que vem antes de `.bun\bin` no PATH.
- Isso reproduz os padrões descritos nos issues #1595/#1452 do repo `thedotmack/claude-mem`: no Windows, `spawn()` sem `shell:true` não executa `.cmd`/`.ps1` diretamente, então o worker cai num fallback que acaba invocando `node.exe` em vez do Bun real — e o `node.exe` não tem `bun:sqlite`, causando o crash do `worker-service.cjs`.
- **Corrigido**: removidos os shims órfãos (`Remove-Item "$env:APPDATA\npm\bun"`, `bun.cmd`, `bun.ps1`). `where.exe bun` agora resolve só para `C:\Users\lucas\.bun\bin\bun.exe`.
- Verificado nos releases do claude-mem (13.6.2 até 13.11.0, a mais recente) — nenhuma correção nova para esse cenário específico chegou a ser lançada; a solução veio de limpar o PATH local, não de atualizar o plugin.
- **Reinstalação em andamento (2026-07-13, tarde)**: `claude plugins install claude-mem@thedotmack` rodado com sucesso (`Successfully installed plugin: claude-mem@thedotmack, scope: user`) — via terminal **pwsh 7.6.3** dentro do VS Code (não Windows PowerShell 5.1, que continua sendo o perfil padrão do terminal — ainda não trocamos o padrão, só rodamos `pwsh` manualmente na sessão). Próximo passo: restaurar backup (`copy C:\Users\lucas\OneDrive\Documentos\claude-mem-backup.db C:\Users\lucas\.claude-mem\claude-mem.db`) e validar que o worker sobe sem o erro `bun:sqlite`.
- **Perfil padrão do terminal corrigido (2026-07-13)**: a paleta de comandos em português não reconheceu "Terminal: Select Default Profile" (nem variantes em PT) — contornado editando `settings.json` diretamente (`code $env:APPDATA\Code\User\settings.json`), adicionando `"terminal.integrated.defaultProfile.windows": "PowerShell"` e o perfil apontando pra `C:\Program Files\PowerShell\7\pwsh.exe`. Validado: nova aba de terminal já nasce em pwsh 7.6.3 (`Major: 7`), sem precisar digitar `pwsh` manualmente.
- **Reinstalação concluída e validada (2026-07-13, tarde)** — claude-mem 13.11.0 rodando 100% saudável:
  - Backup restaurado com sucesso (`claude-mem.db` do dia 17/06 copiado por cima do db novo; o db novo foi preservado em `claude-mem.db.new-install-backup` por precaução).
  - `where.exe bun` resolve só para `.bun\bin\bun.exe` — sem shims órfãos.
  - Log do dia (`claude-mem-2026-07-13.log`) mostra uma falha isolada de spawn logo no boot (13:11, provavelmente durante a transição do Reload Window), seguida de recuperação automática: `Connected to chroma-mcp successfully`, `Smart backfill complete`, `Worker available` — sem novos erros depois de 13:12:56.
  - `npm run worker:status` → worker rodando (PID 29348, porta **37778** — não a porta padrão 37777), versão 13.11.0.
  - `npx claude-mem doctor` inicialmente acusou "Marketplace runtime: node_modules missing" → corrigido com `npx claude-mem repair` → doctor voltou "All required checks passed." (o X residual em "Worker daemon" é falso positivo do doctor batendo na porta padrão 37777 em vez da 37778 real — não é um problema).
  - `curl -UseBasicParsing http://127.0.0.1:37778/health` → `200 OK`, `{"status":"ok","activeSessions":0}`.
  - **Causa raiz confirmada resolvida**: o worker não emitiu mais `Cannot find module 'bun:sqlite'` em nenhum momento após a limpeza do PATH.

### Instalações (2026-07-08)
- **skillspector v2.3.11** (NVIDIA) — scanner de segurança para skills. Instalado via `uv tool`. Uso: `skillspector scan ~/.claude/skills/<skill>/`. Adicionar `ANTHROPIC_API_KEY` ao `.env` para análise semântica. Binário em `~/.local/bin/skillspector`.
- **claude-obsidian v1.9.2** (AgriciDaniel) — plugin Claude Code com 15 skills para Obsidian. Instalado via `claude plugin install`. Skills disponíveis: `/wiki`, `/autoresearch`, `/canvas`, `/save`, `/think`, `wiki-ingest`, `wiki-lint`, `wiki-retrieve`, `wiki-mode`. Complementa o Módulo 7 do monitor.
- **Avaliação de 11 repos de skills** realizada com `git ls-remote` + `git clone --depth 1`. Descartados: harness/harness, revfactory/harness, apache/camel (não são skills), 2FastLabs/agent-squad (redundante), 1jehuang/jcode (autor desconhecido), opensesh/KARIMO, 2FastLabs/agent-squad. Aprovados para uso futuro: apache/camel-mcp (quando precisar de conectores robustos).

### Instalações (2026-07-12)
- **mattpocock/skills** — 15 skills de engenharia via `npx skills@latest add mattpocock/skills`. Destaques: `tdd`, `diagnosing-bugs`, `request-refactor-plan`, `obsidian-vault`, `grilling`.
- **obra/superpowers** — 14 skills de metodologia agentic via `npx skills@latest add obra/superpowers`. Destaques: `brainstorming`, `test-driven-development`, `systematic-debugging`, `writing-plans`, `using-git-worktrees`.
- **garrytan/gstack** — 55 skills (equipe virtual de engenharia: `/ship`, `/review`, `/qa`, `/plan-ceo-review`, `/browse`). Instalado via `git clone` em `~/.claude/skills/gstack` + `./setup`. Exigiu instalar o runtime **bun** (ausente no sistema, `~/.bun/bin/bun`) e rodar `bun install` (faltava dependência `color-name`) antes do setup funcionar. Skills grandes (até ~28k tokens cada) — remover as não usadas se pesar no contexto.
- **claude-office-skills/skills** — avaliado (150+ skills genéricas, template raso, descartado instalar tudo). Copiadas seletivamente 3 skills para `~/.claude/skills/` com prefixo `office-`: `office-n8n-workflow`, `office-notion-automation`, `office-social-publisher`. Atenção: as duas últimas referenciam MCPs genéricos inexistentes (`notion-mcp`, `social-media-mcp`) — usar os MCPs reais conectados (gptmaker, Notion) no lugar.
- **kepano/obsidian-skills** — descartado. Redundante com `claude-obsidian` já instalado (mesmos nomes: `defuddle`, `obsidian-bases`, `obsidian-markdown`).

### Termos adicionados
| Termo | Significado |
|-------|-------------|
| **skillspector** | Scanner NVIDIA para auditar skills antes de instalar. Roda: `skillspector scan <path>` |
| **claude-obsidian** | Plugin de knowledge base Obsidian + Claude Code. Entry point: `/wiki` |
| **gstack** | 55 skills de "equipe virtual de engenharia" (`~/.claude/skills/gstack`). Requer runtime `bun`. Entry points: `/ship`, `/review`, `/qa` |
| **superpowers** | Metodologia agentic da obra/superpowers — TDD, brainstorming, worktrees, subagentes |
| **office-* skills** | 3 skills selecionadas do claude-office-skills (`office-n8n-workflow`, `office-notion-automation`, `office-social-publisher`) — playbooks, não automação plug-and-play |

### Correções aplicadas (2026-07-14)
- **Checkup geral do ambiente rodado** (`.claude/scripts/mcp-health-check.ps1`) — 100% verde: npx/nvm, uvx, cache sequential-thinking, PATH do nvm, extensão VSCode (`2.1.209`), zero crashes nas últimas 24h.
- **Segunda causa raiz de crash do worker do claude-mem identificada (diferente da de 2026-07-13)**: `~/.claude/settings.json` tinha `"PATH": "...;${PATH}"` — o `${PATH}` é sintaxe bash/POSIX e **não é expandido** pelo Claude Code no Windows, então virava um PATH **literal**, substituindo (não completando) o PATH real do sistema. Resultado: `C:\Windows\System32`, `WindowsPowerShell\v1.0` etc. ficavam fora do PATH de todo processo spawnado pelo Claude Code — confirmado testando `powershell.exe` e `ipconfig.exe`, ambos "not recognized". Isso quebrava o spawn do worker do claude-mem, que no Windows depende de chamar `powershell -NoProfile -EncodedCommand ...` para lançar o daemon via `Start-Process`.
- **Corrigido**: `~/.claude/settings.json` → `env.PATH` reescrito substituindo `${PATH}` pelo conteúdo real do PATH de Machine + User (System32, WindowsPowerShell, Git, Docker, WinGet packages etc.), mantendo os prefixos de prioridade (`nvm\v24.15.0`, `npm`, `.local\bin`, `.bun\bin`) na frente. Backup salvo em `~/.claude/settings.json.bak-checkup`. **Efeito só após "Reload Window" no VSCode.**
- `npx claude-mem repair` + start manual do worker resolveram o sintoma imediato; `npx claude-mem doctor` voltou limpo (o X residual em "Worker daemon" continua sendo o falso positivo já conhecido, batendo na porta 37777 em vez da 37778 real).
- **Achado à parte — cuidado com o auto-sync em edições fora do projeto**: editar um arquivo fora do repo (`~/.claude/settings.json`, global) ainda disparou o hook de auto-sync do projeto (`git add -A` + commit + push), porque o hook roda relativo ao cwd da sessão. Isso varreu e commitou automaticamente 169 arquivos de uma reorganização de skills que estava pendente (sem revisão prévia), e por engano incluiu `node_modules/` (8523 arquivos) num dos commits — corrigido logo em seguida por um commit `f93003d "Untrack node_modules and .playwright-mcp..."` que **não foi feito por esta sessão**, indicando outra sessão/processo do Claude Code ativo no mesmo repositório ao mesmo tempo. Estado final: repo limpo e sincronizado com `origin/master`, sem segredos vazados (falsos positivos eram só código de bibliotecas com "token" no nome do arquivo).
- **Lição**: `git add -A` no `auto-sync.ps1` é "tudo ou nada" — qualquer Write/Edit em qualquer arquivo, mesmo fora do projeto, pode empurrar mudanças não relacionadas e não revisadas para o GitHub. Se isso for um problema, considerar trocar por `git add -A -- ':!node_modules' ':!.playwright-mcp'` ou revisar o hook para não rodar em sessões cujo Write/Edit alvo está fora do diretório do projeto.
- **Submódulo `llm-council`** (`karpathy/llm-council.git`) tem scaffold de testes Playwright (`.github/workflows/`, `frontend/e2e/`, `playwright.config.js`, `bun.lock`) local, não commitado dentro do submódulo — decisão do Lucas: manter como está. Submódulo em si está 100% atualizado com o upstream (commit `92e1fcc`, sem divergência).

### Instalações (2026-07-16)
- **Hermes Agent** (`nousresearch/hermes-agent`) — analisado a pedido do Lucas: **não é uma skill do Claude Code** (sem `SKILL.md`), é um framework de agente autônomo standalone com runtime próprio (gateway multi-plataforma Telegram/Discord/Slack/WhatsApp/Signal, cron scheduler, subagentes, suporte a 300+ modelos). Instalado via instalador oficial (`iex (irm https://hermes-agent.nousresearch.com/install.ps1)`) em `C:\Users\lucas\AppData\Local\hermes\hermes-agent`.
- Já havia uma instalação anterior de 2026-07-13 não documentada na memória, **15.839 commits desatualizada** — o instalador fez fast-forward até `dc7a20cb0`. PATH do usuário atualizado permanentemente (`hermes-agent\venv\Scripts`, `hermes\bin`, `hermes\node`). Validado: `hermes --version` → **v0.18.2**.
- Instalador retornou exit code 1 na primeira tentativa: falha ao reaplicar o `git stash` automático que guarda mudanças locais antes do update (conflito em `website/i18n/zh-Hans/.../model-catalog.md`). Investigado antes de mexer: as 401 diffs eram só do site de documentação (Docusaurus) do próprio Hermes — nada em `agent/`, `tools/`, `providers/`, `gateway/` ou no `venv`. Resolvido com `git stash drop` (2x) + `git reset --hard HEAD` dentro do clone do Hermes, sem impacto na funcionalidade do CLI (confirmado antes e depois com `hermes --version`).

→ Glossário completo: `memory/glossary.md`
→ Setup detalhado: `memory/context/setup.md`

### Preferências
- Antes de encerrar qualquer sessão, lembrar: **"Quer que eu atualize a memória com o que fizemos hoje?"**
- **Higgsfield desconectado (2026-07-14)** — conector claude.ai removido para reduzir tempo de boot de subprocessos (causava timeouts de 60s ao abrir abas/subagentes novos, junto com o plugin `remotion-superpowers` desabilitado no mesmo dia). Se o Lucas pedir algo que precise do Higgsfield (geração de vídeo/imagem/áudio via Higgsfield), lembrar: precisa reconectar em claude.ai → Settings → Connectors → Higgsfield antes de usar.
- **Acompanhar uso de tokens:** monitorar o consumo da sessão e avisar proativamente o Lucas quando houver uso elevado (ex: muitas subagentes em paralelo, leitura de arquivos grandes, operações repetidas/pesadas, sessão muito longa). Obs: não há acesso a uma API de telemetria de tokens em tempo real — o acompanhamento é por estimativa/heurística com base nas ações tomadas na sessão, não um contador exato.

---


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

## graphify

This project has a knowledge graph at graphify-out/ with god nodes, community structure, and cross-file relationships.

Rules:
- For codebase questions, first run `graphify query "<question>"` when graphify-out/graph.json exists. Use `graphify path "<A>" "<B>"` for relationships and `graphify explain "<concept>"` for focused concepts. These return a scoped subgraph, usually much smaller than GRAPH_REPORT.md or raw grep output.
- If graphify-out/wiki/index.md exists, use it for broad navigation instead of raw source browsing.
- Read graphify-out/GRAPH_REPORT.md only for broad architecture review or when query/path/explain do not surface enough context.
- After modifying code, run `graphify update .` to keep the graph current (AST-only, no API cost).

## n8n

MCP `n8n-mcp` conectado (instância local `http://localhost:5678`, credenciais em `~/.claude/.env`). Plugin de skills `n8n-mcp-skills` instalado (14 skills especializadas: expressões, validação, nodes, código JS/Python, error handling, sub-workflows, agentes, multi-instância, self-hosting).

Regras:
- Sempre validar o workflow antes de deployar (usar as ferramentas de validação do n8n-mcp).
- Deploy direto via `n8n_create_workflow` — sem copiar/colar JSON manualmente.
- Fluxo de trabalho recomendado: Planning → Research → Build → Deploy & Test, limpando contexto entre fases em workflows complexos.

<!-- SPECKIT START -->
For additional context about technologies to be used, project structure,
shell commands, and other important information, read the current plan
<!-- SPECKIT END -->
