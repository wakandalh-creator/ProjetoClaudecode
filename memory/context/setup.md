# Setup Técnico — Lucas

## Máquina
- Windows (OneDrive sync ativo)
- Node.js v24.15.0
- Bun instalado (mas com problema de compatibilidade com claude-mem)

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

## Backup claude-mem
- Localização: `C:\Users\lucas\OneDrive\Documentos\claude-mem-backup.db`
- Restaurar quando sair versão compatível com Windows

## Arquivos importantes
- `CLAUDE.md` — instruções do projeto + memória ativa
- `memory/` — memória persistente (este sistema)
- `.claude/settings.local.json` — config local do Claude Code (no git)
- `monitor/run.md` — ponto de entrada do sistema de monitoramento
