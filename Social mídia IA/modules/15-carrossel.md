# Módulo 15 — Carrosséis (agente: Pixel)

## Objetivo

Converter um roteiro aprovado (`score_iana ≥7`, `formato: carrossel`) em lâminas de carrossel prontas pra preview — capa = gancho, 1 ideia por lâmina, última = CTA. Dois modos: **estático** (Pillow-first) e **animado** (segue `_templates/carrossel-animado.md`).

## Entrada

- Roteiro em `Social mídia IA/producao/roteiros/YYYY-MM-DD/{slug}.md`, com `score_iana ≥7` e `formato: carrossel` no frontmatter. Se não tiver as duas condições: avisar o Lucas e parar (não produzir carrossel de roteiro reprovado ou de outro formato).

## Contexto obrigatório

1. `branding/neovertix/tokens.json` — cores e tipografia (`color.bg.canvas #0A0E1A`, `color.text.primary #F5F7FA`, `color.accent.default #43A047`, `font.display` = Chakra Petch, `font.text` = Manrope)
2. `Social mídia IA/_context/marca.md` e `tom-de-voz.md` — léxico, banidas, números âncora
3. `Social mídia IA/_templates/carrossel-animado.md` — obrigatório só no modo animado

## Instrução

### Passo 1 — Escolher o modo

- **Estático** é o default.
- **Animado** só quando o Lucas pedir explicitamente ou as `Notas de gravação/produção` do roteiro indicarem `formato: carrossel animado`.

### Passo 2 — Quebrar o roteiro em lâminas

- **Capa** = o gancho (`[GANCHO]` do roteiro), tipografia grande, é o que precisa parar o scroll.
- **Lâminas do meio** = 1 ideia por lâmina, quebrando `[EMOÇÃO]` → `[VIRADA]` → `[PROVA]` em unidades curtas e autônomas (cada lâmina precisa fazer sentido sozinha — quem só vê essa lâmina no feed ainda entende o ponto). Texto curto: preferir 1 frase ou 1 dado por lâmina, nunca parágrafo.
- **Última lâmina** = CTA (`[CTA]` do roteiro), sóbrio, conforme `tom-de-voz.md`.
- Registrar a quebra em `roteiro-laminas.md` (texto exato de cada lâmina) antes de gerar imagem — é o documento de trabalho e o que o Lucas revisa primeiro se pedir ajuste de texto sem mexer no visual.

### Passo 3a — Modo estático (Pillow-first)

- Gerar cada lâmina via script Python com Pillow, evoluindo a base de `ig-saves-engine/create_image.py` (mesma lógica de composição/word-wrap, paleta trocada pelos tokens reais — ver correção já aplicada nesse arquivo).
- Custo zero, sem chamada de IA de imagem — é o caminho padrão pra carrossel puramente tipográfico.

### Passo 3b — Modo animado

- Seguir `_templates/carrossel-animado.md` de ponta a ponta: Nano Banana gera a composição base (Passo 1 do template) → Pillow sobrepõe o texto fixo (Passo 2) → prompt KlingAI pronto é entregue ao Lucas pra ele colar manualmente na interface (Passo 3 — **sem API, etapa manual**, sinalizar isso claramente no preview).

### Passo 4 — Trava de fidelidade visual

Adaptação do conceito de `Criador UGC/_context/tecnica-fotos-produto.md` (lá é fidelidade de produto físico; aqui é fidelidade de **identidade visual**): mesma paleta e tipografia sempre — dentro de um carrossel (todas as lâminas) E entre carrosséis diferentes (nunca variar cor de fundo, cor de destaque ou fonte de um carrossel pro outro). O que varia é só o conteúdo (texto, elemento temático no modo animado). Bloco fixo de referência a aplicar sempre que a peça envolver geração por IA:

```
Identity lock: match the Neovertix visual identity exactly — navy-black
background (#0A0E1A), off-white text (#F5F7FA), single accent green
(#43A047), display type in a geometric condensed sans, body type in a
neutral humanist sans. Do not invent a logo, do not add any robot icon,
do not use purple or gradient effects, do not introduce a second accent
color.
```

### Passo 5 — Salvar e apresentar

- Salvar lâminas + `roteiro-laminas.md` em `Social mídia IA/producao/carrosseis/YYYY-MM-DD/{slug-do-roteiro}/`.
- Apresentar ao Lucas como **preview** (nunca como entrega final): todas as lâminas em sequência + qual modo foi usado +, se animado, lembrete explícito de que o passo KlingAI ainda depende dele.

### Passo 6 — Loop de edição

Ajustes pedidos pelo Lucas são aplicados e reapresentados até aprovação. Carrossel só é considerado pronto pra Posta (módulo de publicação) com OK explícito — nunca por omissão/silêncio.

## Regras

- Nunca gerar carrossel de roteiro com `score_iana <7` ou `formato` diferente de `carrossel`.
- Capa sem gancho forte = capa fraca — se o gancho do roteiro não funcionar isolado (fora do contexto do vídeo/texto), sinalizar ao Lucas antes de prosseguir.
- Nunca inventar número/dado — só os de `marca.md` ou o que já está no roteiro aprovado.
- Identidade visual é fixa (tokens da marca); o que muda é sempre só o conteúdo.
- Nunca dar carrossel por aprovado sem OK explícito do Lucas.
