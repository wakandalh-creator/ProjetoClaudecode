# Técnica — Fotos de produto em lote (trava de fidelidade)

> Extraída de um guia externo (Claude + Flow), adaptada pra rodar via API direto (Nano Banana / `gemini-3.1-flash-image-preview`, mesma chave já validada em `ig-saves-engine/.env`) em vez de Claude for Chrome + Flow web — mais confiável, sem depender de automação de navegador.

## O que resolve

A partir de 1 foto de produto em fundo neutro, gera um lote de variações de criativo (anúncio/post) mantendo o produto **idêntico** entre todas — mesma forma, cor, acabamento, proporções.

## Peças da técnica

**1. Trava de fidelidade** — bloco fixo em inglês, colado no fim de todo prompt de imagem, travando o que não pode mudar:
```
Fidelity lock: render the product exactly as shown in the reference image —
preserve shape, color, finish, surface texture, proportions and label
placement. Do not invent logos, patterns or brand elements not present
in the photo.
```

**2. Geração em lote por categoria** — não gera 1 imagem por vez, gera N organizadas por categoria de conteúdo. Adaptar as 5 categorias do guia original (promoção, benefícios, prova social, lifestyle, sazonal) pro nicho real deste criador quando o `genese` definir o posicionamento — pode não fazer sentido pra todo nicho.

**3. Regras de prompt** (aplicar sempre, independente do nicho):
- Parágrafo único por prompt, 2-4 frases: proporção (1:1, 4:5, 9:16), fundo/paleta, posição do produto, iluminação, headline exata entre aspas, CTA exato entre aspas, estilo visual
- Headline ≤4 palavras, CTA ≤3 palavras (modelo erra texto longo)
- Nunca repetir fundo, headline ou paleta entre variações do mesmo lote

**4. Rollout disciplinado** — não testar as 20 variações de uma vez: rodar 5-6 primeiro (categorias de maior intenção de compra), ver o que performa, só then expandir. Mesmo princípio de `batchSize` pequeno já usado no resto do sistema.

## Diferença do guia original

- Chamar `client.models.generate_content(model='gemini-3.1-flash-image-preview', ...)` direto via `google-genai`, não Claude for Chrome + flow.google.com
- Mesma trava de fidelidade funciona igual — é texto de prompt, não depende da ferramenta
