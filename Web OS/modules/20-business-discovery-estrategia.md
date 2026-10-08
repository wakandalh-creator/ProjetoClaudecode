# Módulo 20 — Business Discovery & Estratégia Web (agente: Tese-ext)

## Objetivo

Adaptar o posicionamento Neovertix (ou de um cliente futuro) a 1 projeto específico de site/landing page, devolvendo o brief que todo o resto do squad Web OS usa como fonte — sem esse brief, nenhum outro módulo começa.

## Entrada

Pedido do Lucas identificando o projeto (nome, slug, se é Neovertix ou cliente) + qual oferta de `config/business.json` a página representa.

## Contexto obrigatório (ler antes de escrever)

1. `config/business.json` — ofertas, posicionamento, tom, léxico/banidas.
2. `branding/neovertix/01-estrategia.md` e `02-oferta.md` — fonte completa (se o projeto for Neovertix).
3. `Web OS/_context/icp-web.md` — qual ICP essa oferta atende numa landing page (fallback: `Social mídia IA/_context/marca.md` se `icp-web.md` ainda não tiver o caso específico).
4. `Web OS/_context/identidade-web-os.md` — princípios e regra de veracidade do sistema.

## Instrução

### Passo 1 — Confirmar objetivo e oferta

Pergunte ao Lucas (se não estiver claro no pedido): qual é o objetivo de negócio da página (lead, venda direta, autoridade/institucional) e qual oferta exata de `config/business.json` ela representa. Não assuma.

### Passo 2 — Reaproveitar dado existente

Nunca rodar pesquisa de mercado nova aqui — isso é trabalho do Radar (módulo 28, Sprint 3). Se faltar dado de concorrente ou de mercado pra fundamentar uma decisão, registre como pendência explícita em `estrategia.md`, não estime.

### Passo 3 — Escrever o brief

Escreva `Web OS/producao/sites/{slug}/estrategia.md` com: objetivo de negócio, oferta específica, ICP (primário/secundário conforme a oferta), problema comercial central, diferencial, métrica de sucesso.

Invocar, nesta ordem:
1. `problem-framing-canvas` — isolar o problema comercial central antes de propor qualquer solução.
2. `jobs-to-be-done` — entender por que o cliente contrataria essa solução especificamente (job funcional/social/emocional).
3. `positioning-workshop` — estruturar o brief final de posicionamento pra essa página.

## Saída

`Web OS/producao/sites/{slug}/estrategia.md`.

## Regras

- Nunca inventar dado de mercado, número de conversão, preço ou depoimento.
- Número âncora só o que já existe em `config/business.json` ou `_context/marca.md` — nunca um número novo sem fonte.
- Se o projeto for de cliente novo (não Neovertix) e faltar `_context/icp-web.md` equivalente, registrar pendência e pedir a informação ao Lucas antes de prosseguir.
