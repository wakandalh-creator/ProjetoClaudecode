# Template — CLAUDE.md do projeto (instanciar em `producao/sites/{slug}/CLAUDE.md` se o projeto usar Claude Code Desktop diretamente)

```markdown
# {Nome do projeto} — CLAUDE.md

> Portão de entrada. Lido toda sessão. Aponta pros outros 2 arquivos do cérebro do projeto.

## Arquivos

- `specs/design.md` — fonte única da verdade do design (paleta, tipografia, tom, estrutura). Gerado analisando `references/` ANTES de escrever qualquer coisa.
- `memory.md` — decisões aprendidas, atualizado pelo próprio Claude conforme o projeto evolui.

## Regra inegociável

Se o pedido contradiz qualquer decisão já registrada em `specs/design.md` ou `memory.md`, PARE e avise antes de agir. Nunca sobrescrever uma decisão sem confirmar.

## Contexto do projeto

- Marca/produto: {preencher}
- Oferta (`config/business.json`): {preencher}
- Stack: HTML + CSS (padrão Web OS — ver `Web OS/run.md` antes de desviar)
- Referências: ver `references/`
```

Preenchido pelo Molda no módulo 21, junto com `specs/design.md`.
