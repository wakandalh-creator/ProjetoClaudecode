# SOP — Gate de Aprovação (regra inegociável)

**NADA é publicado sem aprovação explícita do Lucas.** Sem exceção, nem em fluxo agendado/autônomo.

## Como funciona

O card no Notion (database "Produção de Conteúdo") tem **dois campos independentes** — não confundir:

- **Status** — estágio de produção: `Roteirização → Gravação → Edição → Agendado → Postado`. Agentes movem isso livremente.
- **Aprovado** — checkbox, ortogonal ao Status. **Só o Lucas marca.** Nenhum agente marca, sugere marcar, ou assume que está marcado.

1. Todo conteúdo pronto (roteiro aprovado pela Iana + criativo/preview) vira card com Status refletindo o estágio real de produção.
2. Agentes preparam o card até Status = `Agendado` com `Aprovado` ainda desmarcado — esse é o estado "pronto pra aprovação" (não existe um valor de Status separado pra isso; é a combinação Status=Agendado + Aprovado=false).
3. A publicação (hoje: `ig-saves-engine/post_to_instagram.py`; futuro: Metricool) só age sobre cards com **`Aprovado = true`** — mesmo padrão já validado no ig-saves-engine (lá o campo equivalente é `status: aprovado` na database "Ideias de Posts", que é um sistema diferente e não precisa ser unificado com este).
4. Após publicar, o publicador muda Status pra `Postado` e o Mede registra o resultado (Sem resultado/Flopou/Comum/Bom/Viralizou) no OPR seguinte.

## Auditoria pré-aprovação (o Posta anexa ao card)

- Preview do criativo final (imagem/vídeo) + copy completa como será publicada
- Verificação de limites da plataforma (caracteres de legenda, formato, proporção)
- Zero palavras banidas (checagem contra `_context/tom-de-voz.md`)
- CTA funcional (link/palavra-chave configurados de verdade)
