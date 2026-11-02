# neovertix crm

Projeto à parte: **Agente de IA para WhatsApp + CRM incluso + Instagram/redes sociais**.
Usa o nome Neovertix, mas **não é** a marca principal do squad em `Social mídia IA/`
(Piloto, Operação e Vértice Full). Não misturar os contextos.

## Estrutura

| Caminho | O que é |
|---|---|
| `_context/briefing.md` | Briefing "MEU NEGÓCIO / MINHA VOZ / PROVAS / REGRAS" do Lucas (2026-11-01) |
| `_context/marca.md` | Cérebro de marca do projeto (planos Essencial e Escala, teste de 7 dias) |
| `_context/tom-de-voz.md` | Tom de voz (Base v2 + expressões do briefing ajustadas) |
| `_context/business.json` | Versão estruturada da marca deste projeto |
| `_context/tom-de-voz-v2-proposta.md` | Proposta da Tese que originou o tom de voz (histórico) |
| `_context/voice.md` | Cópia de `~/.claude/instagram/voice.md`, lido pelas skills `ig-*` |
| `conversas/` | Transcrições das conversas que montaram este projeto |
| `producao/` | Conteúdos produzidos (roteiros, legendas, carrosséis) |

## Skills de Instagram

As 13 skills `ig-*` estão em `~/.claude/skills/`, adaptadas para português, e leem
`~/.claude/instagram/voice.md`. Se o tom de voz mudar aqui, atualize os dois `voice.md`.

## Regras

- Não inventar clientes, depoimentos, resultados ou urgência.
- Nada é publicado, agendado ou enviado sem autorização do Lucas.
- Informação ausente fica marcada como `{{a confirmar}}`.
