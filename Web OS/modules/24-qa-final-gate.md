# Módulo 24 — QA Final & Gate de Publicação (agente: Eixo)

## Objetivo

Rodar o checklist QA Final cruzando todos os domínios já cobertos pelo Web OS nesta versão, arbitrar qualquer conflito entre camadas, e preparar o projeto pra aprovação humana — sem nunca marcar essa aprovação sozinho.

## Entrada

`producao/sites/{slug}/` com os módulos 20-23 completos (estratégia, design aprovado, build+QA técnico, deploy+auditoria).

## Contexto obrigatório

1. `Web OS/_sop/checklist-qa-final.md` — template do checklist.
2. `Web OS/_sop/aprovacao-publicacao.md` — mecanismo do gate.
3. Todos os artefatos do projeto até aqui: `estrategia.md`, `specs/design.md`, `qa/acessibilidade.md`, `qa/auditoria-lighthouse.md`.

## Instrução

### Passo 1 — Preencher o checklist

Copiar `_sop/checklist-qa-final.md` pra `producao/sites/{slug}/qa/checklist-final.md` e preencher cada linha com base no que de fato foi verificado nos módulos 20-23. Domínio cujo módulo dono ainda não existe (SEO, Local, AI, Tracking, Security, Copy/CRO neste momento) fica marcado "N/A — Sprint N" — nunca aprovado por omissão.

Invocar `production-audit` pra gerar um veredito formal e read-only (score 0-100, blockers nomeados, baseado só em evidência local do projeto — sem mandar dado pra serviço externo).

### Passo 1b — Verificação visual leve

Invocar `browser-qa` pra uma passada visual/de interação read-only. Diferente do `qa` do módulo 22 (que edita código ativamente) — aqui o build já deveria estar fechado, então é só confirmação.

### Passo 2 — Resolver conflito entre camadas

Se houver tensão entre recomendações de módulos diferentes, aplicar nesta ordem:
- Performance × Design → performance vence.
- SEO × UX → nunca keyword-stuff.
- CRO × Confiança → nunca remover informação obrigatória só pra forçar conversão.
- Marketing × Verdade → nunca publicar promessa não comprovada.
- Escala × Qualidade → nunca escalar um processo ainda não validado.

### Passo 3 — Atualizar status

Mover `status` em `projeto.md` livremente até `pronto-para-publicar`. **Nunca** marcar `aprovado: true` — esse campo é exclusivo do Lucas, sem exceção.

### Passo 4 — Apresentar ao Lucas

Mostrar o checklist preenchido + a recomendação (publicar / ajustar X antes) ao Lucas. Só depois disso o projeto pode receber `aprovado: true`.

## Saída

`qa/checklist-final.md` + `projeto.md` com `status: pronto-para-publicar` e `aprovado: false`.

## Regras

- `ship-gate` não é citado neste módulo — não existe como skill instalada neste ambiente (verificado na fase de planejamento).
- `qa` (edição ativa de código) pertence ao módulo 22, não a este — módulo 24 é intencionalmente read-only.
- Invocar `verification-before-completion` antes de declarar qualquer etapa deste módulo "pronta" — regra herdada de todo o squad, não só deste módulo (ver `Web OS/run.md`, Regras herdadas).
