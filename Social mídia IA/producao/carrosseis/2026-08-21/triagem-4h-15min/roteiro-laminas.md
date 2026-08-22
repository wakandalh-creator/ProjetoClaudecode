---
roteiro_origem: Social mídia IA/producao/roteiros/2026-08-21/triagem-4h-15min.md
score_iana: 7.5
formato: carrossel estático (8 lâminas)
modo: Pillow-first
---

# Quebra em lâminas — triagem 4h → 15min

Texto de cada lâmina é literal do roteiro aprovado (rodada 3, `score_iana` 7,5).
Nenhuma palavra foi alterada — só a diagramação (quebras de linha, o que vira
eyebrow/label vs. corpo, o que ganha cor de destaque). Os "Refinos opcionais"
da Iana (pré-produção) NÃO foram aplicados aqui — mudam texto, decisão é do
Lucas/Roteira, fora do escopo do Pixel.

## Lâmina 1 — CAPA / GANCHO
> Sua equipe leva 4 horas pra responder um lead. O concorrente respondeu em segundos.

Design: tipografia grande, sem imagem de fundo (nota de produção). "4 HORAS" e
"EM SEGUNDOS" em verde de destaque (accent.default) — os dois relógios do
contraste duplo.

## Lâmina 2 — EMOÇÃO
> Ele não espera a fila andar — testa quem responder primeiro. 10 leads perdidos por demora custam R$3.000 a R$15.000 por mês.

Design: corpo em off-white; faixa "CUSTO" (mono) + números R$3.000-R$15.000 em
destaque (accent), maior que o resto — é o dado que dói.

## Lâmina 3 — VIRADA (antes, 1/2)
> Antes: a mensagem chega e fica parada até alguém sair de outra ligação.

Design: eyebrow "ANTES" (mono, cinza — sem cor de destaque, reforça "estado
parado"). Ícone geométrico de relógio parado (ponteiros na mesma posição).

## Lâmina 4 — VIRADA (antes, 2/2)
> Antes: quando alguém finalmente abre o CRM, já se passaram 4 horas — e o lead quente esfriou junto com o resto da fila.

Design: eyebrow "ANTES" (mono, cinza). Ícone geométrico de fila (pontos em
linha, sem cor de destaque).

## Lâmina 5 — VIRADA (depois, 1/2)
> Depois: o agente lê a mensagem no segundo em que ela chega e consulta o CRM sozinho — histórico, se já é cliente, o que já foi combinado.

Design: eyebrow "DEPOIS · 1" em verde de destaque. Círculo numerado "1" +
seta — início do fluxo contínuo (contraste visual com a fila parada de antes).

## Lâmina 6 — VIRADA (depois, 2/2)
> Depois: responde com esse histórico na mão e sobe pro topo da fila quem já pediu orçamento. 4 horas de triagem viram 15 minutos.

Design: eyebrow "DEPOIS · 2" em verde de destaque. Círculo numerado "2" +
seta. Payoff "4 HORAS VIRAM 15 MINUTOS." em destaque no fim do card.

## Lâmina 7 — PROVA
> Isso é o Piloto Vértice: 2 a 4 semanas rodando com os dados da sua operação, com a métrica de tempo de resposta combinada antes de começar — semanas, não trimestre.

Design: eyebrow "PILOTO VÉRTICE" (mono, verde). "2 a 4 semanas" em destaque
dentro do corpo.

## Lâmina 8 — CTA
> Comenta TRIAGEM aqui embaixo — te chamo no direct e monto esse fluxo com os números da sua operação, ao vivo.

Design: balão de comentário (forma geométrica simples, borda verde) com a
palavra "TRIAGEM" em destaque dentro; corpo abaixo com o resto da frase.

---

## Trava de fidelidade visual aplicada

- Fundo `#0A0E1A` (off-black/navy) em todas as 8 lâminas, texto `#F5F7FA`
  (off-white), única cor de destaque `#43A047` (accent.default) — nunca uma
  segunda cor de acento, nunca gradiente roxo, nenhum ícone de robô.
- Tipografia: display = Chakra Petch (substituto vendorizado `BigShoulders-Bold`,
  Chakra Petch não instalada no ambiente — mesma decisão já registrada em
  `producao/criativos/2026-08-21/leads-perdidos-custo/gerar_criativo.py`),
  corpo = Manrope (substituto `WorkSans-Regular`), mono = `JetBrainsMono-Bold`
  para eyebrows/labels/contador de página.
- Contraste "antes/depois" é 100% visual (cor + ícone), não duplica em copy —
  os rótulos "Antes:"/"Depois:" do roteiro viram eyebrow de design, mantendo
  a frase completa como corpo (texto não foi cortado, só redistribuído).
