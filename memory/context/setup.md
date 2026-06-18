# Setup Técnico — Lucas

## Máquina
- Windows (OneDrive sync ativo)
- Node.js v24.15.0
- Bun instalado (mas com problema de compatibilidade com claude-mem)
- **RAM: 7,7GB totais, frequentemente <1GB livre.** Limita modelos de IA local — sempre usar variantes `tiny`/`base`/`small` (nunca `medium`/`large`, ex: Whisper.cpp) e fechar apps pesados antes de rodar algo que precise de memória

## Claude Code
- Versão: 2.1.179
- Modelo: Sonnet 4.6
- Projeto: `C:\Users\lucas\OneDrive\Documentos\ProjetoClaudecode`
- GitHub: https://github.com/wakandalh-creator/ProjetoClaudecode
- Auto-sync ativo via `.claude/auto-sync.ps1`

## MCPs conectados (junho 2026)
| MCP | Status |
|-----|--------|
| Cloudflare Developer Platform | Conectado |
| gptmaker | Conectado |
| Google Drive | Precisa autenticar |
| pw-testrail | Desativado (`.mcp.json` limpo) |
| pw-browserstack | Desativado (`.mcp.json` limpo) |

## Plugins instalados
| Plugin | Status |
|--------|--------|
| claude-mem (thedotmack) | Desinstalado — quebrado no Windows/Node v24 |
| playwright-pro | Instalado — MCPs desativados |
| graphify (`graphifyy` via uv tool) | Instalado, escopo de projeto. Skill em `.claude/skills/graphify/` |

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
