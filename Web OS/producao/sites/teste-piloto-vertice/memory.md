# Memory — Piloto Vértice (teste-piloto-vertice)

> Decisões aprendidas durante o projeto. Atualizado pelo próprio Claude/agente conforme o trabalho avança — nunca pré-preenchido com decisão que ainda não foi tomada.

## Decisões registradas

| Data | Decisão | Por quê | Módulo |
|---|---|---|---|
| 2026-10-09 | Intensity de motion subiu de Subtle (default calibrado pelo ICP de conversão) pra **Strong**, só nesta página — exceção pontual, não recalibração do banco global. Scroll-reveal (Medium) nas 8 seções + parallax real (Strong) em só 2 pontos: glow de fundo Hero→Problema e a trilha de conexão em "Como funciona" (scrub síncrono ao scroll). | Decisão do Lucas: esta página não é só conversão pra PME — é a vitrine de capacidade de build da própria Neovertix, vista por um prospect avaliando "essa agência constrói coisa impressionante?". Audiência de craft, diferente do ICP sóbrio que julga o tom da copy. Voz/léxico continuam sóbrios — só o orçamento de movimento mudou. | 21 (Molda) |
| 2026-10-09 | Mesmo em Strong, mantido: zero spring/bounce, Garantia Vértice sem contador numérico animado (30% é limiar fixo, não métrica crescendo — animar como crescimento distorceria o significado), parallax restrito a 2 elementos (não em seções de decisão/leitura: Oferta, Garantia, Objeções, Programa Fundador). | Regra de propósito do módulo 21 vale igual em qualquer Intensity: toda animação cumpre 1 função ou não entra. Strong manda mais escopo, não dispensa a regra. | 21 (Molda) |
| 2026-10-09 | Performance budget mantém os mesmos limiares (LCP<2,5s / INP<200ms / CLS<0,1) mesmo com Strong — o que mudou foi como o orçamento é gasto: H1 do Hero nunca pode depender de JS pra ficar visível (fallback CSS-first), scroll-tied só anima `transform`/`opacity`, todo elemento com reveal reserva o espaço de layout desde o load (evita CLS). | Risco técnico real de subir Intensity sem reabrir o budget: LCP/CLS quebram fácil se a entrada animada esconder o conteúdo até o JS carregar. | 21 (Molda) |

## Rejeitado (e por quê — evita re-litigar)

| Data | O que foi proposto | Por que foi rejeitado |
|---|---|---|
| 2026-10-09 | Contador numérico animado subindo até 30% no bloco Garantia Vértice (cogitado ao desenhar o reveal da seção) | 30% é um limiar fixo da garantia, não uma métrica que cresce — uma animação de contagem sugeriria dinamismo que não existe; risco de veracidade, não só gosto estético. |
| 2026-10-09 | Aplicar o mesmo parallax do Hero/Como-funciona em Oferta/Garantia/Objeções/Programa Fundador, pra "igualar" o efeito Strong na página toda | Essas seções são momentos de decisão/leitura — movimento de fundo ali teria custo de atenção sem função. A regra "toda animação cumpre 1 função" vale em qualquer Intensity; Strong é teto de escopo, não obrigação de preencher tudo. |
