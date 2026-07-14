# Setup Técnico — Lucas

## Máquina
- Windows (OneDrive sync ativo)
- Node.js v24.15.0
- Bun instalado (mas com problema de compatibilidade com claude-mem)
- **RAM: 7,7GB totais, frequentemente <1GB livre.** Limita modelos de IA local — sempre usar variantes `tiny`/`base`/`small` (nunca `medium`/`large`, ex: Whisper.cpp) e fechar apps pesados antes de rodar algo que precise de memória

## Claude Code
- Versão: 2.1.204
- Modelo: Sonnet 4.6
- Projeto: `C:\Users\lucas\OneDrive\Documentos\ProjetoClaudecode`
- GitHub: https://github.com/wakandalh-creator/ProjetoClaudecode
- Auto-sync ativo via `.claude/auto-sync.ps1`

## MCPs conectados (julho 2026)
| MCP | Status |
|-----|--------|
| Cloudflare Developer Platform | Conectado |
| gptmaker | Conectado |
| Google Drive | Precisa autenticar |
| sequential-thinking | Conectado — commit pinado `527ba64d` (evita rebuild no startup) |
| context7 | Conectado (HTTP) |
| pw-testrail | Desativado |
| pw-browserstack | Desativado |
| playwright | Falha graciosamente (npx via nvm — PATH corrigido em settings.json) |
| chrome-devtools | Falha graciosamente (npx via nvm — PATH corrigido em settings.json) |
| firecrawl-mcp | Falha graciosamente (npx, FIRECRAWL_API_KEY não configurada) |

## Correções aplicadas (2026-07-08)
| Arquivo | O que foi feito |
|---------|----------------|
| `~/.claude/settings.json` | Adicionado PATH com `nvm/v24.15.0` na seção `env` — resolve MCPs que usam `npx` |
| `.mcp.json` | sequential-thinking pinado no commit `527ba64d` — startup de 26s → ~3s |

## Crash investigado (2026-07-08)
- Sintoma: exit code 3221226505 (0xC0000005 = access violation) na extensão VSCode
- Causa MCPs: `npx` não encontrado no PATH do VSCode → 3 MCPs falhavam no startup
- Crash esporádico: sem registro no Event Viewer de `node.exe` → causa raiz ainda não confirmada
- Suspeita principal restante: driver GPU (LiveKernelEvent 141) instável na máquina
- Script de monitoramento: `.claude/scripts/mcp-health-check.ps1`

## Plugins instalados
| Plugin | Status |
|--------|--------|
| claude-mem (thedotmack) | Desinstalado — quebrado no Windows/Node v24 |
| playwright-pro | Instalado — MCPs desativados |
| graphify (`graphifyy` via uv tool) | Instalado, escopo de projeto. Skill em `.claude/skills/graphify/` |
| codex@openai-codex | Instalado (escopo user) — `/codex:review`, `/codex:adversarial-review`, `/codex:rescue` |
| open-design@open-design | Instalado (escopo user) — app real em `C:\open-design-sandbox\app\` (versão portátil, não pelo plugin/instalador) |

## Projetos de teste (fora do repo principal)
| Pasta | O que é |
|-------|---------|
| `C:\open-design-sandbox\app\` | Open Design versão portátil — `Open Design.exe`, sem instalação no sistema |
| `Documentos\teste-remotion\meu-teste\` | Scaffold Remotion template TikTok (legendas), testado e funcionando, modelo Whisper `base`/`pt` |

## Automação graphify (configurada em 2026-06-18)
| Peça | Onde | Frequência |
|------|------|-----------|
| Rotina em nuvem `graphify-daily-update` | `trig_017yfMuS3SAxeLEPwsqWGwxX` (claude.ai/code/routines) | Diária, 11h00 UTC (8h BRT) |
| Tarefa Windows `Graphify-ProjetoClaudecode-ObsidianSync` | `.claude/scripts/graphify-obsidian-sync.ps1` | Diária, 8h30 BRT |
| Database Notion | "Monitor — Grafo de Código" (data source `d78c3c4c-8972-4161-b0c3-31a5b952d977`) | Atualizada pela rotina em nuvem |
| Log local | `.claude/scripts/graphify-obsidian-sync.log` | Checar ocasionalmente |

## Backup claude-mem
- Localização: `C:\Users\lucas\OneDrive\Documentos\claude-mem-backup.db`
- Restaurar quando sair versão compatível com Windows

## Arquivos importantes
- `CLAUDE.md` — instruções do projeto + memória ativa
- `memory/` — memória persistente (este sistema)
- `.claude/settings.local.json` — config local do Claude Code (no git)
- `monitor/run.md` — ponto de entrada do sistema de monitoramento
