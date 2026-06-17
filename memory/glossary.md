# Glossário — Decoder Ring Completo

Atalhos, siglas e linguagem interna do Lucas.

## Plugins e ferramentas

| Termo | Significado | Contexto |
|-------|-------------|---------|
| claude mem / claude men | Plugin `claude-mem` (thedotmack) | Memória persistente entre sessões — instalado mas quebrado no Windows/Node v24 |
| pw | Plugin `playwright-pro` | Testes Playwright; MCPs pw-testrail e pw-browserstack desativados |
| gpr maker / gpt maker | `gptmaker` MCP | Conectado e funcionando |
| MCP | Model Context Protocol | Protocolo de integração de ferramentas no Claude Code |
| worker | `worker-service.cjs` do claude-mem | Processo em segundo plano que requer `bun:sqlite` |

## Projetos e sistemas

| Termo | Significado |
|-------|-------------|
| monitor | Sistema de Monitoramento de Tendências + Instagram em `monitor/` |
| relatório | Saída do monitor em `reports/YYYY-MM-DD/` |
| vault | Vault Obsidian integrado ao monitor |
| swarm | Skill de processamento paralelo com sub-agentes |
| auto-sync | Hook que commita e push automático a cada Write/Edit no Claude Code |

## Comandos frequentes

| Atalho | Comando completo |
|--------|-----------------|
| rodar monitor | `Execute o monitor — leia monitor/run.md` |
| ver relatório | `Abra o relatório mais recente em reports/` |
| exportar obsidian | `Execute apenas o Módulo 7 — leia monitor/modules/07-obsidian-export.md` |
