# Export Notion — Frameworks de Livros

Reaproveita o padrão de campo-tabela + dedup-antes-de-criar de
`monitor/modules/08-notion-export.md`, aplicado a uma nova database:
"Frameworks de Livros".

## Database

```
NOTION_DB_FRAMEWORKS = 4337aca285aa48da881351b9829287e8
```

Criada em 2026-07-14 ("Monitor — Frameworks de Livros"), como database
independente na raiz do workspace — mesmo padrão das outras 4 databases
do Monitor (nenhuma tem página-pai). Se por algum motivo o ID mudar ou a
database for movida, atualizar aqui.

## Campos

| Campo | Tipo | Conteúdo |
|---|---|---|
| `titulo` | title | Nome do framework/skill gerada |
| `livro_origem` | text | Título do livro + autor |
| `destino` | select | `empresa` / `pessoal` / `both` |
| `slug` | text | Slug da skill (bate com `generated-skills-lock.json`) |
| `data_geracao` | date | YYYY-MM-DD |
| `link_skill` | url/text | Caminho ou URL do `SKILL.md` |
| `status` | select | `ativo` / `rascunho` / `arquivado` |
| `proxima_acao` | text | Ação concreta gerada na síntese de negócio (ex.: "testar SEO programático como 2º canal") |
| `impacto_registrado` | text | Preenchido quando a ação é executada de fato — o que mudou no negócio por causa desse livro. Vazio até lá. |
| `uso_contagem` | number | Espelha `useCount` do lock file |

## Regra de dedup

Antes de criar um novo registro, buscar por `slug` existente na
database. Se já existe, **atualizar** o registro (especialmente
`status`, `impacto_registrado`, `uso_contagem`) em vez de criar
duplicado — mesma regra do Módulo 8 ("never duplicate — check existing
before creating").

## Por que esse painel importa

`impacto_registrado` vazio vs. preenchido é o filtro que responde "esse
livro valeu a extração?" sem precisar abrir o `generated-skills-lock.json`
— a liderança consegue ver isso direto no Notion, sem tocar em código.
