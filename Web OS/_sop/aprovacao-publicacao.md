# SOP — Gate de Aprovação de Publicação (Web OS)

**NADA vai ao ar sem aprovação explícita do Lucas.** Sem exceção, nem em fluxo agendado/autônomo.

## Mecanismo

Cada projeto tem `Web OS/producao/sites/{slug}/projeto.md` com este frontmatter:

```yaml
---
projeto: {slug}
status: discovery | design | build | qa | pronto-para-publicar | publicado
aprovado: false   # só o Lucas muda pra true — nenhum agente marca, sugere marcar, ou assume
url_publicada:
data_aprovacao:
---
```

- `status` é o estágio de produção — qualquer agente do Web OS move livremente.
- `aprovado` é **ORTOGONAL** a `status`, booleano, e só o Lucas marca — editando o arquivo diretamente, ou respondendo "aprovado, pode publicar" pro Eixo escrever em seu nome.
- O Eixo prepara o projeto até `status: pronto-para-publicar` com `aprovado: false` — não existe um valor de `status` separado pra "pronto pra aprovação"; é a combinação dos dois campos que sinaliza isso.
- Deploy em domínio público real (módulo 23) só roda com `aprovado: true`. Preview/staging interno roda livre, sem esse gate.
- Pós-publicação: `status: publicado`, `data_aprovacao` e `url_publicada` preenchidos pelo Eixo.

## Auditoria pré-aprovação

Antes de apresentar o projeto ao Lucas pra aprovação, o Eixo confirma:
- `_sop/checklist-qa-final.md` preenchido, sem domínio coberto marcado como pendente.
- `qa/acessibilidade.md` e `qa/auditoria-lighthouse.md` existem e foram rodados pelo menos 1x.
- `specs/design.md` foi aprovado pelo Lucas (módulo 21) e o build final não diverge dele sem justificativa registrada.
- Nenhuma promessa/número/depoimento no site sem fonte verificável.

## Regra de rotina

Esta regra é duplicada de propósito em `.claude/agents/eixo.md` — o agente que a executa também a declara explicitamente, mesmo padrão do `posta.md` na Social mídia IA.
