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
| vault | Vault Obsidian integrado ao monitor (`Cerebro Claude`) |
| swarm | Skill de processamento paralelo com sub-agentes |
| auto-sync | Hook que commita e push automático a cada Write/Edit no Claude Code |
| graphify | Skill que transforma código/docs em knowledge graph (PyPI `graphifyy`) — escopo: `monitor/`+`config/`+`reports/`+`CLAUDE.md`, output em `graphify-out/` |
| rotina em nuvem / /schedule | Agente cloud isolado (CCR) da Anthropic — roda em ambiente próprio, sem acesso ao PC local, mas alcança MCPs conectados (ex: Notion) |
| Monitor — Grafo de Código | Database Notion criada para receber o resumo diário do graphify (God Nodes, Surprising Connections, pergunta sugerida) |
| codex-plugin-cc | Plugin oficial OpenAI pra usar Codex dentro do Claude Code (`/codex:review`, `/codex:adversarial-review`) — instalado, grátis com conta ChatGPT Free |
| open-design / `od` | App de design agêntico (`nexu-io/open-design`) — instalado em versão portátil isolada em `C:\open-design-sandbox\app\`, sem instalador no sistema |
| Remotion / create-video | Framework de vídeo programático em React — testado em `Documentos\teste-remotion\meu-teste\`, template TikTok (legendas via Whisper.cpp local) |
| Whisper.cpp | Transcrição de áudio local usada pelo template Remotion-TikTok — na máquina do Lucas, só os modelos `tiny`/`base`/`small` cabem na RAM disponível |

## Comandos frequentes

| Atalho | Comando completo |
|--------|-----------------|
| rodar monitor | `Execute o monitor — leia monitor/run.md` |
| ver relatório | `Abra o relatório mais recente em reports/` |
| exportar obsidian | `Execute apenas o Módulo 7 — leia monitor/modules/07-obsidian-export.md` |
| atualizar grafo manualmente | `/graphify monitor config reports CLAUDE.md --update --obsidian` |
| ver grafo no navegador | Abrir `graphify-out/graph.html` |
