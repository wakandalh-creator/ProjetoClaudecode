# Criador UGC — segunda marca de conteúdo

> Espaço reservado. **Não é a Neovertix** — é um criador/avatar próprio, com nicho e posicionamento ainda a definir, pra diversificar renda, alcançar outros públicos e testar formatos que não cabem no tom sóbrio B2B da Neovertix.

## Status: 📋 Registrado, aguardando kickoff

## Como isso nasce

Quando o Lucas quiser começar de verdade, ele chama o agente **`genese`** (`.claude/agents/genese.md`). Ele conduz a entrevista de posicionamento (nicho, público, tom de voz, pilares, monetização, se envolve produto físico) e a partir das respostas:

1. Preenche `_context/marca.md` e `_context/tom-de-voz.md` deste espaço (mesmo padrão da Neovertix)
2. Monta o resto da estrutura (`_sop/`, `_templates/`, `modules/`, `bancos/`, `producao/`) — só depois de saber o nicho, pra não criar módulo genérico demais
3. Decide junto com o Lucas se o squad reaproveita os agentes da Neovertix (Roteira, Iana, Pixel, Corta) apontando pra esse `_context/` novo, ou se esse criador merece squad próprio — é uma decisão de arquitetura real, não trivial, fica documentada na hora

## Pré-requisitos antes de produzir de verdade

- [ ] Sessão de posicionamento com o `genese` (nicho, tom, direção)
- [ ] Higgsfield e HeyGen (HyperFrames) reconectados em claude.ai → Settings → Connectors (avatar não funciona sem isso)
- [ ] Se envolver produto físico: técnica de "trava de fidelidade" + mega-prompt (ver `_context/tecnica-fotos-produto.md`) pronta pra gerar fotos de produto via Nano Banana

## Duas frentes de uso do avatar (já decidido)

1. **Conteúdo Neovertix** — avatar entrega roteiros da Neovertix quando o Lucas não quiser aparecer (fica no `Social mídia IA/`, módulo 14 — não duplica aqui)
2. **Este criador UGC** — persona própria, nicho próprio, formato mais solto — é o que este espaço aqui organiza

**Regra dura, sem exceção**: nunca simular depoimento de cliente fake. Avatar com persona própria e conteúdo declaradamente gerado por IA, sim — cliente inventado fingindo ser real, não. Contradiz o próprio pilar da Neovertix ("prova nomeável, zero fumaça") e é risco regulatório real (propaganda enganosa).
