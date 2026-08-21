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

## Referências externas — modelos de contrato

Salvos em 2026-08-05 para verificar depois, ao formalizar o contrato do pacote Otimização Multi-Mecanismo (SEO+AEO+GEO+CRO — ver artefato SOP gerado na sessão):

- Contrato de prestação de serviços (genérico): https://diegocastroadvogado.com.br/contrato-de-prestacao-de-servicos/
- Modelo de contrato de prestação de serviços de SEO: https://diegocastroadvogado.com.br/modelo-de-contrato-de-prestacao-de-servicos-de-seo/

Servem de base para os contratos próprios. Revisar quando a estruturação da empresa estiver concluída.

## Vault "Estruturação" — regra de escrita (2026-08-05)

**Sempre escrever em `G:\Meu Drive\Estruturação\`, nunca mais em `C:\Users\lucas\OneDrive\Documentos\Obsidian Vault\Estruturação\`.** O Drive é o vault mestre oficial (decisão de 13/07, reafirmada em 05/08 depois de reconectar o Google Drive Desktop). O caminho do OneDrive é backup histórico — tinha virado o vault de fato só porque o Drive Desktop ficou desligado por quase um mês; isso foi corrigido.

Detalhe: os dois locais ainda estão parcialmente divergentes (só o arquivo do Piloto Salões/Barbearias foi reconciliado em 05/08). Se for editar algo que só existe na cópia do OneDrive, avisar o Lucas antes de decidir onde gravar.

## Comandos frequentes

| Atalho | Comando completo |
|--------|-----------------|
| rodar monitor | `Execute o monitor — leia monitor/run.md` |
| ver relatório | `Abra o relatório mais recente em reports/` |
| exportar obsidian | `Execute apenas o Módulo 7 — leia monitor/modules/07-obsidian-export.md` |
| atualizar grafo manualmente | `/graphify monitor config reports CLAUDE.md --update --obsidian` |
| ver grafo no navegador | Abrir `graphify-out/graph.html` |
