# Template — specs/design.md do projeto (instanciar em `producao/sites/{slug}/specs/design.md`)

```markdown
# Design Spec — {Nome do projeto}

> Fonte única da verdade do design deste projeto. Gerado pelo Molda (módulo 21) analisando `references/` + `Web OS/bancos/design-tokens-globais.md` ANTES de qualquer código. Precisa de aprovação explícita do Lucas antes do módulo 22 (build) começar.

## Referências analisadas

- {link/screenshot 1}
- {link/screenshot 2 — opcional}
- {link/screenshot 3 — opcional, máx. 3 no total}

## Tokens do projeto

Herdados de `Web OS/bancos/design-tokens-globais.md`; desvio abaixo exige motivo.

| Categoria | Valor | Desvio do global? Por quê? |
|---|---|---|
| Color — primary | {preencher} | — |
| Color — secondary | {preencher} | — |
| Typography | {preencher} | — |
| Spacing | 4/8px scale (padrão) | — |
| Radius | {preencher} | — |
| Shadow | {preencher} | — |
| Breakpoints | 320/375/390/430/768/1024/1280/1440+ (padrão) | — |

## Tom e estrutura

- Tom: {preencher, derivado de `Web OS/_context/icp-web.md` + `estrategia.md`}
- Estrutura de seções: {Hero / Problema / Solução / Benefícios / Como funciona / Diferenciais / Prova / Oferta / Objeções / FAQ / CTA final — adaptar}

## Inventário de componentes

| Seção | Reaproveitar de `componentes-aprovados.md`? | Ou construir custom? |
|---|---|---|
| Hero | {preencher} | {preencher} |

## Pipeline de imagem

- Produto físico real? {sim/não}
- Se sim: fotos em `my-products/` ou pasta equivalente, prompt base compartilhado em `images.md`.
- Se não: moodboard em `moodboard/`, imagem-âncora aprovada primeiro.

## Aprovação

- [ ] Aprovado pelo Lucas em: {data}
```
