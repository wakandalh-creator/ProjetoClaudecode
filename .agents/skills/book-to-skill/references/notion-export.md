# Export Notion — Frameworks de Livros

Reaproveita o padrão de campo-tabela + dedup-antes-de-criar de
`monitor/modules/08-notion-export.md`, aplicado a uma nova database:
"Frameworks de Livros".

## Pré-requisito (setup manual, não automatizado por esta skill)

A database `NOTION_DB_FRAMEWORKS` **ainda não existe**. Antes do export
funcionar, o usuário precisa:

1. Criar a database "Frameworks de Livros" no Notion, com os campos
   abaixo.
2. Adicionar o ID dela onde os outros três IDs já vivem hoje —
   hardcoded em `monitor/modules/08-notion-export.md` (linhas 16-19).

Se `NOTION_DB_FRAMEWORKS` não estiver configurado quando esta skill
tentar exportar, pular a etapa com uma mensagem clara ("Notion export
pulado — NOTION_DB_FRAMEWORKS não configurado") e seguir o resto do
pipeline normalmente. Não é um erro fatal.

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
