# Export Notion — Aprendizados de Vídeo

Mesmo padrão de `book-to-skill/references/notion-export.md`: dedup por
identificador antes de criar, aplicado a uma database irmã.

## Database

```
NOTION_DB_LEARNINGS = <preencher após criar a database no Notion>
```

Ainda não existe — ao contrário de `NOTION_DB_FRAMEWORKS`, nenhuma
database "Aprendizados de Vídeo" foi criada no workspace até agora. Se
o usuário pedir export pro Notion e essa variável não estiver definida
aqui, **parar e avisar** ("database ainda não criada — quer que eu
crie uma agora, ou prefere só o Obsidian por enquanto?"). Não inventar
um ID.

## Campos (mesma estrutura de `NOTION_DB_FRAMEWORKS`, adaptada)

| Campo | Tipo | Conteúdo |
|---|---|---|
| `titulo` | title | Título do aprendizado/nota |
| `fonte` | text | Tipo + canal/criador (ex.: "YouTube — Canal X") |
| `url_origem` | url | Link do vídeo/podcast, ou caminho se arquivo local |
| `destino` | select | `empresa` / `pessoal` / `both` |
| `slug` | text | Slug da nota (bate com `video-learnings-lock.json`) |
| `data_geracao` | date | YYYY-MM-DD |
| `link_nota` | url/text | Caminho da nota no vault Obsidian |
| `status` | select | `ativo` / `arquivado` |
| `proxima_acao` | text | Ação concreta gerada na síntese de negócio |
| `impacto_registrado` | text | Preenchido quando a ação é executada de fato. Vazio até lá. |

## Regra de dedup

Antes de criar um novo registro, buscar por `slug` existente na
database. Se já existe, **atualizar** (especialmente `status` e
`impacto_registrado`) em vez de criar duplicado.
