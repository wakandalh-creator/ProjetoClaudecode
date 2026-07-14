---
name: book-to-skill
description: Lê um livro (EPUB, PDF, MOBI/AZW3, DOCX ou TXT) e destila seu conteúdo operacional — frameworks, processos, checklists, regras de decisão — num SKILL.md reutilizável pelo Claude Code. Gera versão empresa (adaptada a config/business.json, vai para .claude/skills/ e .agents/skills/) e/ou versão pessoal (desenvolvimento pessoal, vai para os skills globais do usuário). Trigger: "transforma esse livro em skill", "processa os livros pendentes", "livro pra skill".
---

# book-to-skill — transforma livros em conhecimento operacional

## O que isso faz (e o que NÃO faz)

Lê um livro e extrai o que é **transferível e acionável** — frameworks
nomeados, processos com passos, checklists, regras de decisão — e produz
um `SKILL.md` de verdade, invocável pelo Claude Code depois.

**Não é** a `skills/book-mirror` (skill global, `~/.claude/skills/book-mirror/`):
book-mirror personaliza a narrativa completa do livro pra vida do
leitor (coluna-espelho, depende do CLI `gbrain`). `book-to-skill` mata a
narrativa e preserva só o método — o produto final é uma skill operável,
não uma leitura personalizada. Se o pedido for "quero ver como esse
livro se aplica à minha vida", use `book-mirror`. Se for "quero poder
usar o que esse livro ensina depois, como uma ferramenta", use esta.

> Uso interno — conteúdo derivado de obra protegida por direitos
> autorais, não redistribuir fora da organização.

## Intake — onde soltar o livro

Pasta dedicada no Google Drive: `livros-inbox`. Nunca solte o arquivo
bruto do livro dentro do repositório `ProjetoClaudecode` — o hook
`auto-sync` (`.claude/auto-sync.ps1`, disparado por `PostToolUse` em
`Write|Edit`) commita e dá push em tudo que for escrito no repo, e
arquivos de livro costumam ser protegidos por direitos autorais.

Pré-requisito: conector `claude.ai Google Drive` autorizado (ver
`CLAUDE.md` — hoje listado como pendente). Sem isso, peça ao usuário pra
autorizar via configurações de conector do claude.ai antes de continuar.

Acionamento:
- Com nome explícito: "transforma 'Traction.epub' (no Drive) em skill,
  destino empresa" → localizar via `search_files` dentro de `livros-inbox`.
- Sem nome: "processa os livros pendentes" → listar `livros-inbox` via
  `list_recent_files`/`search_files`, baixar cada um com
  `download_file_content` para um diretório temporário local (fora do
  repo), processar os que ainda não estão em `generated-skills-lock.json`
  com `status: completed`.

O download vive só em `$WORK` (temp dir) durante o processamento e é
apagado ao final — o arquivo original permanece no Drive, sem necessidade
de mover ou apagar nada lá.

## Pipeline

### 1. ACQUIRE

Detectar formato pela extensão. Calcular hash:

```bash
sha256sum "$BOOK_FILE"
```

Checar `generated-skills-lock.json` (raiz do repo) por esse hash em
`skills.*.sourceBook.fileHash`. Se já existe com `status: "completed"`,
parar e informar o `skillSlug`/`destination` existentes — perguntar antes
de reprocessar. Nunca duplicar silenciosamente.

### 2. EXTRACT — texto por capítulo, qualquer formato

```bash
SLUG="titulo-do-livro"                          # kebab-case, provisório
WORK="$(mktemp -d)/$SLUG"
mkdir -p "$WORK/chapters"
```

| Formato | Método |
|---|---|
| EPUB | `unzip -o book.epub -d "$WORK/unpacked"`, listar XHTML/HTML ordenados, extrair texto com BeautifulSoup — mesmo padrão de `skills/book-mirror/SKILL.md` (seção "2. Text extraction / EPUB"), um `.txt` por arquivo de capítulo |
| PDF | `pdftotext -layout book.pdf "$WORK/full.txt"`, dividir por regex de cabeçalho (`Chapter N`, `CHAPTER N`, título em caixa alta) — mesmo padrão de `book-mirror` (seção "PDF") |
| MOBI/AZW3 | `ebook-convert book.mobi "$WORK/book.epub"` (Calibre). Checar `command -v ebook-convert` antes; se ausente, avisar claramente ("Calibre não instalado — instale antes de processar MOBI/AZW3") e parar, não tentar contornar. Depois cai no caminho EPUB |
| DOCX | `pandoc --to=plain --wrap=none book.docx -o "$WORK/full.txt"`, dividir com a mesma heurística de cabeçalho do PDF (DOCX não tem arquivo por capítulo como EPUB) |
| TXT | passthrough direto, dividir por padrão de cabeçalho (`^Chapter \d+`, `^CHAPTER [IVXLCDM]+`, linha curta em caixa alta isolada) |

Quality check por capítulo (mesmo padrão do book-mirror): >1500 palavras
típico, sem HTML residual, parágrafos preservados com `\n\n`. Salvar
`$WORK/chapters/INDEX.md` (número, título, contagem de palavras).

### 3. DISTILL — a divergência chave

Por capítulo, ler `chapters/NN.txt` e produzir `distilled/NN.md` contendo
**só** blocos estruturados — sem resumo em prosa:

```markdown
## Framework: <nome dado pelo livro, ou descritivo se o livro não nomeia>
1. Passo 1
2. Passo 2
...

## Regra: <nome>
Se <condição>, então <ação>.

## Checklist: <nome>
- [ ] Critério 1
- [ ] Critério 2
```

**Manter:** frameworks nomeados com passos, regras de decisão, checklists,
terminologia/glossário que o livro define, processos repetíveis.

**Matar:** anedota, estudo de caso, biografia do autor, apelo emocional —
**a menos que** a anedota seja o único veículo carregando uma técnica;
nesse caso, extrair a técnica e descartar o invólucro narrativo.

Se um capítulo não contém nada operacional (ex.: introdução, agradecimentos),
o `distilled/NN.md` fica vazio — isso é esperado, não um erro.

### 4. FACT-CHECK (antes de sintetizar)

Para cada framework/regra/checklist em `distilled/`, confirmar que é
rastreável ao texto correspondente em `chapters/NN.txt` — nome, passos e
afirmações-chave precisam bater com algo que o capítulo realmente diz,
não uma generalização ou inferência do modelo. Remover o que não passar.
Mesmo princípio do fact-check do book-mirror, mas aplicado ao conteúdo do
livro em vez de a fatos sobre o leitor: **melhor perder textura do que
atribuir ao autor algo que ele não disse.**

### 5. BUSINESS SYNTHESIS (só se destino inclui `empresa`)

Ler `config/business.json` (posicionamento, `possible_niches`,
`target_audience`, `content_goal`, `tone`, `offers`, `avoid_topics`).
Para cada framework sobrevivente, aplicar o mesmo padrão de
`monitor/modules/06-business-apply.md` (Bloco E: Insight → Adaptação →
Próxima ação), substituindo os insights de conteúdo social pelos
frameworks do livro. Anexar ao bloco:

```markdown
> Adaptação: <como esse framework se aplica à realidade específica do negócio>
> Próxima ação: <ação concreta e testável>
```

Se `business.json` tiver campos vazios (`offers: []`, `avoid_topics: []`
hoje é o caso), não inventar conteúdo pra preencher — pular a adaptação
desse campo especificamente, seguir com o resto.

### 6. CLASSIFY

Confirmar destino: `empresa`, `pessoal` ou `both`. Se não veio explícito
no pedido do usuário, perguntar. Se `both`, os passos 5 e 7 rodam duas
vezes com inputs diferentes — a versão empresa carrega a síntese de
negócio, a versão pessoal não é a mesma coisa copiada, é destilado puro
com enquadramento de desenvolvimento pessoal.

### 7. SYNTHESIZE — montar o SKILL.md final

Mesclar os blocos de todos os capítulos num arquivo coerente:
deduplicar frameworks repetidos entre capítulos, ordenar do conceitual
pro aplicado (não na ordem dos capítulos). Frontmatter simples, mesma
convenção desta própria skill (`name` + `description`, sem os campos
gbrain-específicos do book-mirror). Template do corpo:

```markdown
---
name: <slug>
description: <1-2 frases, o que a skill resolve e quando usar>
---

# <Nome>

> Uso interno — derivado de obra protegida, não redistribuir.

## What this does
...

## When to use this
...

## Source
<Título> — <Autor>, <ano>. Extraído em <data>.

## <Nome do Framework 1>
[passos / checklist / tabela de decisão, como no livro]
[se destino empresa: bloco Adaptação → Próxima ação]

## Anti-patterns
[se o livro nomear modos de falha]

## Output checklist
...

## Rastreio de uso
Ao aplicar esta skill em trabalho real, atualize `useCount`, `lastUsed`
e (se o framework foi de fato executado) `impacto` da entrada
`<slug>` em `generated-skills-lock.json`.
```

### 8. REGISTER

Escrever/atualizar `generated-skills-lock.json` (raiz do repo):

```json
{
  "version": 1,
  "skills": {
    "<slug>": {
      "sourceBook": {"title": "...", "author": "...", "fileHash": "sha256:...", "originalPath": "livros-inbox/..."},
      "generatedDate": "YYYY-MM-DD",
      "destination": "empresa",
      "skillPath": {
        "empresa": [".claude/skills/<slug>/SKILL.md", ".agents/skills/<slug>/SKILL.md"]
      },
      "status": "completed",
      "lastUsed": null,
      "useCount": 0,
      "proximasAcoes": ["<ação concreta gerada na etapa 5>"],
      "impacto": []
    }
  }
}
```

Antes de finalizar o slug, checar colisão contra: as próprias chaves de
`generated-skills-lock.json`, as chaves de `skills-lock.json` (raiz do
repo), e uma listagem viva de `.claude/skills/`, `.agents/skills/` e
`C:\Users\lucas\.claude\skills\`. Se colidir, usar sufixo `-book` ou
numérico e avisar o usuário do ajuste.

### 9. EXPORT

- **Arquivos da skill** — escrever em `.claude/skills/<slug>/SKILL.md`
  **e** `.agents/skills/<slug>/SKILL.md` (destino empresa) e/ou em
  `C:\Users\lucas\.claude\skills\<slug>-pessoal\SKILL.md` (destino
  pessoal).
- **Obsidian** — seguir o padrão de criação de nota de
  `monitor/modules/07-obsidian-export.md` (frontmatter YAML +
  `New-Item -ItemType Directory -Force`), usando
  `folders.book_frameworks` de `config/obsidian.json`. Se
  `config/obsidian.json.enabled` for `false`, pular com aviso.
- **Notion** — seguir `references/notion-export.md` desta skill. Se
  `NOTION_DB_FRAMEWORKS` não estiver configurado, pular com mensagem
  clara (não é erro — database ainda não foi criada pelo usuário).
- **Graphify** — rodar `graphify update .` **só se** o diretório da nova
  skill já estiver dentro do `.graphify_root` rastreado (checar
  `graphify-out/.graphify_root` ou prefixo no manifest). Caso contrário,
  imprimir uma linha avisando que é preciso um `/graphify` multi-path
  novo incluindo o diretório da skill — não rodar rebuild completo do
  repo silenciosamente.

### 10. VALIDATE

Checklist final antes de reportar sucesso:

- [ ] Hash do livro registrado em `generated-skills-lock.json`.
- [ ] Sem colisão de slug (verificado, não assumido).
- [ ] `SKILL.md` tem seção `Source` com título/autor/data.
- [ ] Pelo menos um framework com passos concretos numerados (não só prosa).
- [ ] Se destino empresa: pelo menos uma adaptação referencia um campo
      real de `business.json` (não genérico).
- [ ] Arquivos existem nos dois diretórios (`.claude/skills/` e
      `.agents/skills/`) para destino empresa.
- [ ] Nota Obsidian criada (se `enabled: true`).
- [ ] Graphify atualizado ou aviso de escopo impresso.

## Anti-patterns

- ❌ Preservar narrativa/anedota sem extrair a técnica que ela carrega.
- ❌ Frameworks genéricos sem passos concretos ("seja mais estratégico").
- ❌ Escrever em `.claude/skills/` sem também escrever em `.agents/skills/`.
- ❌ Reprocessar um livro já no lock file sem perguntar antes.
- ❌ Fabricar síntese de negócio quando campos de `business.json` estão vazios.
- ❌ Soltar o arquivo bruto do livro dentro do repositório Git.
- ❌ Manter um framework no SKILL.md final que não passou no fact-check.

## Poda/auditoria (sob demanda, não automática)

Quando pedido ("audita as skills de livros"): listar entradas de
`generated-skills-lock.json` com `status: completed`, `generatedDate` há
mais de ~90 dias, `useCount: 0` e `impacto: []` — candidatas a revisão
ou arquivamento (mover o `SKILL.md` pra fora das pastas de skills,
marcar `status: archived` no lock file, preservando o histórico).
Reaproveitar `skill-security-auditor` já instalado em vez de construir
um scanner novo.

## Related skills

- `skills/book-mirror` (global) — personaliza o livro inteiro pra vida
  do leitor; use quando o objetivo é reflexão pessoal, não uma
  ferramenta reutilizável.
- `graphify` — cruza o conhecimento das skills geradas com o resto da
  base da empresa.
