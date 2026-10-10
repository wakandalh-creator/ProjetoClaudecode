# Módulo 21 — Design System & Inventário de Componentes (agente: Molda)

> Conversão direta do guia prático de design system validado na conversa que originou o Web OS (baseado na análise do vídeo `/watch` sobre construir sites com Claude Code).

## Objetivo

Converter 1-3 referências visuais + os tokens globais do banco em `specs/design.md` do projeto — a fonte única de verdade de design — e decidir o inventário de componentes antes de qualquer linha de código.

## Entrada

`Web OS/producao/sites/{slug}/estrategia.md` (módulo 20) já escrito e aprovado.

## Contexto obrigatório (ler antes de propor design)

1. `estrategia.md` do projeto (módulo 20).
2. `Web OS/bancos/design-tokens-globais.md` — base de tokens reutilizável.
3. `Web OS/bancos/componentes-aprovados.md` — o que já funcionou em projetos anteriores.
4. `Web OS/_templates/projeto-specs-design.md` — template de saída.

## Instrução

### Passo 1 — Referências

Curar com o Lucas 1-3 sites de referência (Dribbble, Awwwards, Pinterest — nunca mais de 3, senão mistura estilo). Salvar screenshot full-page + link em `producao/sites/{slug}/references/`.

### Passo 2 — Tokens do projeto

Definir cor primária/secundária/destaque, escala tipográfica, espaçamento (herda 4/8px do global), radius, shadow, breakpoints (320/375/390/430/768/1024/1280/1440+) e **motion** (duration/easing/intensity/movement — herda de `Web OS/bancos/design-tokens-globais.md` seção Motion). Herdar do banco global por padrão; todo desvio precisa de motivo registrado em `specs/design.md`.

Regra de motion, não negociável: toda animação precisa cumprir pelo menos 1 função (orientar, explicar, confirmar, gerar emoção com intenção, criar continuidade, ajudar conversão) — sem função, não entra. `prefers-reduced-motion` sempre respeitado.

Invocar a skill `design-system` (modo "Gerar") pra extrair tokens a partir das referências e gerar o rascunho de `DESIGN.md`/`design-tokens.json` que alimenta o `specs/design.md` final.

### Passo 2b — Performance budget

Antes de desenhar qualquer seção, declarar o orçamento de performance do projeto em `specs/design.md`: LCP < 2,5s, INP < 200ms, CLS < 0,1 (mesmos limiares que o módulo 23 vai auditar), mais um limite consciente de peso de imagem/animação por seção. Cada efeito visual proposto nos passos seguintes precisa caber nesse orçamento — se não cabe, corta ou simplifica antes de chegar no módulo 22, não depois.

### Passo 3c — Trust Architecture

Pra cada seção que pede prova/confiança, listar de onde ela vem *antes* de prometer algo: clareza do processo, metodologia, demonstração do mecanismo, número real (nunca estimado), garantia, política visível — nunca só "depoimento" como única fonte de confiança. Mostrar evidência antes da promessa, não depois.

### Passo 3 — Inventário de componentes e direção visual

Por seção da página (Hero/Problema/Solução/Benefícios/Como funciona/Diferenciais/Prova/Oferta/Objeções/FAQ/CTA final — adaptar ao projeto), decidir: reaproveitar de `componentes-aprovados.md` ou construir custom.

Invocar `frontend-design` (plugin `claude-plugins-official` — há uma segunda cópia no plugin `open-design`, usar a oficial pra evitar ambiguidade) pra escolhas deliberadas de tipografia/cor/layout que não leiam como template genérico. Invocar `emil-design-eng` especificamente pras decisões de movimento/interação (easing, duração, spring, performance de animação).

Nunca empilhar mais de 1 skill de "direção estética anti-genérica" na mesma decisão — `frontend-design`, `design-taste-frontend`, `impeccable-design-polish`, `gpt-taste` e `high-end-visual-design` competem entre si com frameworks diferentes pro mesmo julgamento. `frontend-design` é a escolhida pra esta etapa; `impeccable-design-polish` fica reservada pro módulo 22 (polimento pós-build).

Sem dependência de marketplace de componentes externo como requisito deste squad — o inventário vem do banco próprio ou é construído sob medida.

### Passo 4 — Pipeline de imagem

- **Produto físico real**: fotos em múltiplos ângulos salvas numa pasta de produto → `images.md` com 1 prompt por imagem necessária (ângulo, luz, cenário, proporção, seção) + um prompt-base compartilhado entre todas pra manter consistência.
- **Sem produto físico**: moodboard com 5-8 imagens de referência de *estilo* (não do produto) → gerar uma imagem "âncora" primeiro, aprovar, reusá-la como referência nas demais — evita derivar de uma imagem pra outra.

Invocar `imagegen-frontend-web` (opcional) pra padronizar os prompts de moodboard antes do código.

### Passo 5 — Aprovação

`specs/design.md` precisa de aprovação explícita do Lucas antes do módulo 22 (build) começar. Sem essa aprovação, o Constrói não inicia.

## Saída

`producao/sites/{slug}/specs/design.md` + `references/` + `images.md` (se aplicável).

## Regras

- Nunca escrever código nesta etapa.
- Nunca contradizer uma decisão já registrada em `specs/design.md` sem avisar o Lucas antes.
- Componente novo bem-sucedido é candidato a `Web OS/bancos/componentes-aprovados.md`, mas só promove com confirmação explícita do Lucas.
