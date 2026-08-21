---
name: video-to-learning
description: Assiste um vídeo de qualquer fonte (YouTube, Instagram, TikTok, X, Vimeo, Twitch, podcast ou arquivo local — qualquer origem suportada pelo plugin `watch`) e destila o conteúdo operacional — frameworks, processos, checklists, regras de decisão — personalizado para o negócio (config/business.json). Ao contrário da /book-to-skill, NÃO gera um SKILL.md novo: só salva o aprendizado (nota Obsidian/Notion). Trigger: "transforma esse vídeo em aprendizado", "extrai o aprendizado desse podcast/reels", "processa os vídeos pendentes".
---

# video-to-learning — transforma vídeos em aprendizado aplicável

## O que isso faz (e o que NÃO faz)

Assiste um vídeo — aula, palestra, podcast, reels, tutorial — e extrai o
que é **transferível e acionável**: frameworks nomeados, processos com
passos, checklists, regras de decisão. Personaliza para o negócio (mesmo
padrão de `config/business.json` usado no resto do projeto) e salva o
resultado como **nota de aprendizado**.

**Não gera uma skill nova.** É o mesmo pipeline de destilação da
`/book-to-skill` (ACQUIRE → EXTRACT → DISTILL → FACT-CHECK → BUSINESS
SYNTHESIS → EXPORT), só que a etapa SYNTHESIZE produz uma nota Obsidian,
não um `SKILL.md` reutilizável pelo Claude Code. Se o pedido for "quero
poder invocar isso depois como ferramenta", use `/book-to-skill` (ela lê
livros, mas o mesmo raciocínio de "vídeo → skill" pode ser adaptado à
mão). Se for "só quero guardar o que aprendi e aplicar no negócio", use
esta.

## Dependência: plugin `watch` (claude-video)

Esta skill não reimplementa download/transcrição de vídeo — reaproveita
o motor já instalado do plugin `watch` (`yt-dlp` + `ffmpeg` +
Whisper Groq/OpenAI, chave em `~/.config/watch/.env`). Se `/watch` nunca
rodou neste ambiente, rode `python3 <caminho-do-plugin>/scripts/setup.py`
uma vez antes (ele instala `ffmpeg`/`yt-dlp` e escreve o `.env`).

Diferença do fluxo de `/watch`: `/watch` sempre extrai frames (pensado
pra Claude "ver" o vídeo e responder perguntas visuais). Esta skill só
precisa do **texto** pra destilar aprendizado, então usa
`scripts/transcript_only.py` (bundled nesta skill), que importa
`download.py`/`transcribe.py`/`whisper.py` do plugin `watch` diretamente
e pula a extração de frames — mais rápido, sem custo de tokens de
imagem, e funciona em fontes só-áudio (podcast em `.mp3`) onde a
extração de frame do `/watch` quebraria por falta de stream de vídeo.

Se o conteúdo depender de algo visual (slide, código na tela, gráfico) e
a transcrição sozinha não for suficiente, é válido rodar `/watch` também
e ler os frames relevantes como complemento — mas isso não é o padrão.

## Pipeline

### 1. ACQUIRE — obter a transcrição

```bash
python3 "${CLAUDE_SKILL_DIR}/scripts/transcript_only.py" "<source>"
```

`<source>` é a URL (YouTube, Instagram, TikTok, X, Vimeo, Twitch, RSS de
podcast — qualquer coisa que `yt-dlp` suporte) ou um caminho de arquivo
local (vídeo ou áudio). O script imprime um JSON com `title`, `uploader`,
`duration_seconds`, `source_hash`, `chapters` (se o YouTube expuser
capítulos), `transcript_source` (`captions` ou `whisper (groq|openai)`)
e `transcript` (texto com timestamps `[MM:SS]`).

**Dedup:** checar `video-learnings-lock.json` (raiz do repo) por
`source_hash` em `videos.*.sourceVideo.sourceHash`. Se já existe com
`status: "completed"`, parar e informar a nota existente — perguntar
antes de reprocessar. Nunca duplicar silenciosamente.

**Sem transcrição disponível** (sem legenda e sem chave Whisper): o
script avisa no stderr. Perguntar ao usuário se quer configurar a chave
(`~/.config/watch/.env`, mesma usada pelo `/watch`) ou seguir só com
título/descrição do vídeo (aprendizado ficará raso — avisar isso).

### 2. EXTRACT — segmentar a transcrição

Se `chapters` veio preenchido (vídeos longos do YouTube costumam ter),
use os capítulos como unidade de segmentação — equivalente aos
capítulos de um livro. Sem capítulos, segmente por mudança de assunto
no texto (a cada ~5-10 min de fala ou virada de tópico perceptível).

Salvar `$WORK/segments/NN.txt` (um por segmento) + `INDEX.md` (título do
segmento, timestamp de início, contagem de palavras) — mesmo padrão de
`book-to-skill/chapters/INDEX.md`.

### 3. DISTILL — a mesma divergência-chave da /book-to-skill

Por segmento, produzir blocos estruturados — sem resumo em prosa:

```markdown
## Framework: <nome dado no vídeo, ou descritivo se não for nomeado>
1. Passo 1
2. Passo 2
...

## Regra: <nome>
Se <condição>, então <ação>.

## Checklist: <nome>
- [ ] Critério 1
- [ ] Critério 2
```

**Manter:** frameworks nomeados com passos, regras de decisão,
checklists, terminologia que o vídeo define, processos repetíveis.

**Matar:** história pessoal, hype, call-to-action de venda, tangente —
**a menos que** seja o único veículo carregando uma técnica; nesse caso,
extrair a técnica e descartar o invólucro.

Se um segmento não contém nada operacional (introdução, agradecimentos,
publicidade), o bloco fica vazio — esperado, não é erro.

### 4. FACT-CHECK

Cada framework/regra/checklist precisa ser rastreável a um trecho real
da transcrição — citar o timestamp `[MM:SS]` correspondente. Remover o
que não bater com algo realmente dito no vídeo. Mesmo princípio do
fact-check de `book-to-skill`: **melhor perder textura do que atribuir
ao criador do vídeo algo que ele não disse.**

### 5. BUSINESS SYNTHESIS

Ler `config/business.json` (posicionamento, `possible_niches`,
`target_audience`, `content_goal`, `tone`, `offers`, `avoid_topics`).
Para cada aprendizado sobrevivente, aplicar o mesmo padrão de
`monitor/modules/06-business-apply.md` (Bloco E: Insight → Adaptação →
Próxima ação):

```markdown
> Adaptação: <como esse aprendizado se aplica à realidade específica do negócio>
> Próxima ação: <ação concreta e testável>
```

Se `business.json` tiver campos vazios (`offers: []`, `avoid_topics: []`
hoje é o caso), não inventar conteúdo pra preencher — pular a adaptação
desse campo especificamente, seguir com o resto.

### 6. CLASSIFY — destino da nota

Confirmar destino: `empresa`, `pessoal` ou `both`. Se não veio explícito
no pedido do usuário, perguntar. `empresa` roda a etapa 5 (síntese de
negócio); `pessoal` pula a etapa 5 e enquadra o aprendizado como
desenvolvimento pessoal em vez de aplicação de negócio. `both` gera duas
seções na mesma nota (não duas notas separadas — ao contrário de
`book-to-skill`, aqui não há dois artefatos de skill pra manter em
sincronia).

### 7. SYNTHESIZE — montar a nota de aprendizado

**Isto substitui a etapa "gerar SKILL.md" de `book-to-skill`.** Nenhum
arquivo entra em `.claude/skills/` ou `.agents/skills/` aqui.

```markdown
---
date: YYYY-MM-DD
type: aprendizado-video
titulo: "<titulo>"
fonte_tipo: "<youtube|instagram|tiktok|x|vimeo|twitch|podcast|arquivo-local>"
fonte_url: "<url ou caminho>"
autor_canal: "<uploader>"
duracao: "<MM:SS>"
tags: [aprendizado, video, <topico-slug>]
---

# {Título}

> Fonte: {fonte_tipo} — {autor_canal}, {duração}. Transcrito em {data}.
> {fonte_url}

## O que aprendi

{blocos de Framework/Regra/Checklist sobreviventes do fact-check, cada um com o timestamp de rastreio}

## Aplicação no negócio

{Insight → Adaptação → Próxima ação, por aprendizado — só se destino inclui empresa}

## Frases-chave

{opcional: 1-3 citações literais marcantes, com timestamp — só se agregar algo que os blocos acima não capturam}
```

### 8. REGISTER

Escrever/atualizar `video-learnings-lock.json` (raiz do repo):

```json
{
  "version": 1,
  "videos": {
    "<slug>": {
      "sourceVideo": {
        "title": "...",
        "uploader": "...",
        "sourceHash": "sha256:...",
        "originalSource": "<url ou caminho>",
        "durationSeconds": 0
      },
      "generatedDate": "YYYY-MM-DD",
      "destination": "empresa",
      "notePath": "<VAULT_PATH>/Monitor/Aprendizados/<slug>.md",
      "status": "completed",
      "proximasAcoes": ["<ação concreta gerada na etapa 5>"],
      "impacto": []
    }
  }
}
```

`<slug>`: kebab-case do título, checar colisão contra as chaves já
existentes no próprio arquivo antes de gravar.

### 9. EXPORT

- **Obsidian** — seguir o padrão de `monitor/modules/07-obsidian-export.md`
  (frontmatter YAML + `New-Item -ItemType Directory -Force`), usando
  `folders.video_learnings` de `config/obsidian.json`
  (`Monitor/Aprendizados`). Se `config/obsidian.json.enabled` for
  `false`, pular com aviso.
- **Notion** — seguir `references/notion-export.md` desta skill. Se
  `NOTION_DB_LEARNINGS` não estiver configurado, pular com mensagem
  clara (não é erro — database ainda não foi criada pelo usuário).
- **Graphify** — mesma regra condicional de `book-to-skill`: rodar
  `graphify update .` só se `Monitor/Aprendizados` já estiver dentro do
  `.graphify_root` rastreado; caso contrário, avisar que é preciso um
  `/graphify` multi-path novo.
- **Limpeza** — apagar `$WORK` (diretório de download/transcrição) ao
  final, a menos que o usuário peça pra manter o vídeo baixado.

### 10. VALIDATE

Checklist final antes de reportar sucesso:

- [ ] `source_hash` registrado em `video-learnings-lock.json`.
- [ ] Nota tem seção "Fonte" com tipo/canal/data.
- [ ] Pelo menos um aprendizado (framework/regra/checklist) com passos
      concretos, não só prosa.
- [ ] Se destino empresa: pelo menos uma adaptação referencia um campo
      real de `business.json` (não genérico).
- [ ] Nota Obsidian criada (se `enabled: true`).
- [ ] Graphify atualizado ou aviso de escopo impresso.
- [ ] **Nenhum `SKILL.md` foi gerado** — se em algum momento parecer que
      o pedido é criar uma skill nova reutilizável, isso é escopo da
      `/book-to-skill`, não desta.

## Anti-patterns

- ❌ Preservar história/tangente sem extrair a técnica que ela carrega.
- ❌ Aprendizado genérico sem passos concretos ("seja mais consistente").
- ❌ Gerar um `SKILL.md` ou escrever em `.claude/skills/`/`.agents/skills/`
  — não é a função desta skill.
- ❌ Rodar `/watch` (com extração de frame completa) quando só o texto
  já resolve — desperdiça tokens de imagem.
- ❌ Tentar extrair frames de fonte só-áudio (podcast `.mp3` sem stream
  de vídeo) — `transcript_only.py` já evita isso pulando `frames.py`.
- ❌ Reprocessar um vídeo já com `status: completed` no lock file sem
  perguntar antes.
- ❌ Fabricar síntese de negócio quando campos de `business.json` estão
  vazios.
- ❌ Manter um aprendizado na nota final que não passou no fact-check.

## Related skills

- `/book-to-skill` — mesmo pipeline de destilação, mas para livros e
  gera uma skill nova reutilizável em vez de uma nota.
- `watch` (plugin `claude-video`) — motor de download+transcrição
  reaproveitado por esta skill via `scripts/transcript_only.py`.
- `graphify` — cruza o conhecimento das notas de aprendizado com o
  resto da base da empresa.
