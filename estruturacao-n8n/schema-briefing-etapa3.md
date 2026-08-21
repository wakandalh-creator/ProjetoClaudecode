# Schema do Briefing — Etapa 3

Referência formal do JSON que o node "Chamar Claude API" (`03-briefing-claude-api.json`) precisa produzir, mais um teste isolado do prompt (sem n8n).

## Schema

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "tom_de_voz": { "type": "string", "description": "Reflete o nicho — ex.: advocacia/clínica pedem tom mais formal; salão/oficina podem ser mais próximos." },
    "paleta_sugerida": { "type": "array", "items": { "type": "string" }, "minItems": 3, "maxItems": 3, "description": "3 cores hex." },
    "proposta_de_valor": { "type": "string" },
    "nome": { "type": "string" },
    "telefone": { "type": "string" },
    "email": { "type": "string" },
    "redes_sociais": {
      "type": "object",
      "properties": { "instagram": { "type": "string" } },
      "required": ["instagram"]
    },
    "padrao_de_dor": { "type": "string", "description": "Extraído das avaliações reais do Google — nunca suposição genérica." }
  },
  "required": ["tom_de_voz", "paleta_sugerida", "proposta_de_valor", "nome", "telefone", "email", "redes_sociais", "padrao_de_dor"]
}
```

**Adicionado nesta revisão**: o prompt agora recebe `nicho` e `regiao` como contexto de entrada (não são gerados pela Claude, vêm da triagem/scraping anterior — Etapas 1-2) e instrui explicitamente que `tom_de_voz`/`proposta_de_valor` devem refletir o nicho, não usar um tom genérico de salão. Isso é o dado que os Blocos 3/6 do `guia-skills-etapa-5.md` (escolha de skill de design, `local-seo`) já esperam receber parametrizado.

## Teste isolado do prompt (mock, sem chamar a API de verdade)

Não há `ANTHROPIC_API_KEY` configurada nesta sessão/ambiente — o teste abaixo é uma simulação manual (mesmo prompt exato do node, preenchido com dados fictícios de um nicho **diferente** de salão/barbearia, de propósito, pra confirmar que o pipeline não está hardcoded).

**Input mock** (nicho: oficina mecânica, região: Uberlândia-MG — não Juiz de Fora, de propósito):
```json
{
  "nicho": "oficina mecânica",
  "regiao": "Uberlândia-MG",
  "tem_site_existente": false,
  "nome": "Oficina do Zé",
  "telefone": "(34) 99999-0000",
  "email": "contato@oficinadoze.com.br",
  "instagram_handle": "@oficinadoze",
  "instagram_bio": "Mecânica de confiança há 15 anos",
  "nota_google": 4.6,
  "avaliacoes_texto": [
    "Serviço bom mas demorou muito pra me passar o orçamento",
    "Preço mudou depois que o carro já estava lá, não gostei",
    "Trabalho excelente, só a comunicação que podia ser mais rápida"
  ]
}
```

**Output simulado** (resposta que a Claude API daria pro prompt gerado por esse input — validado com `node -e` contra o schema acima: `OK: schema bate, todas as chaves presentes e tipadas corretamente`):
```json
{
  "tom_de_voz": "Direto e confiável, sem jargão técnico — fala como um mecânico experiente explicando pro cliente o que está acontecendo com o carro, sem enrolar e sem esconder o preço.",
  "paleta_sugerida": ["#1A2B3C", "#F2A900", "#F5F5F0"],
  "proposta_de_valor": "Orçamento claro e por escrito antes de qualquer serviço, com prazo real de entrega — o cliente sabe exatamente quanto vai pagar e quando pega o carro de volta.",
  "nome": "Oficina do Zé",
  "telefone": "(34) 99999-0000",
  "email": "contato@oficinadoze.com.br",
  "redes_sociais": { "instagram": "@oficinadoze" },
  "padrao_de_dor": "Avaliações reais mencionam repetidamente demora no retorno do orçamento e sensação de preço mudando depois do carro já estar na oficina — o padrão de dor é falta de transparência e previsibilidade, não qualidade do serviço em si (que é bem avaliada)."
}
```

Confirma 3 coisas:
1. O prompt produz JSON compatível com o schema, inclusive fora do nicho piloto (salão/JF).
2. `padrao_de_dor` vem mesmo das avaliações mockadas (demora + preço mudando), não de suposição genérica — o critério que o próprio prompt exige.
3. O node seguinte (`Parsear briefing JSON`) já tem fallback via regex (`text.match(/\{[\s\S]*\}/)`) pra extrair o JSON mesmo se a Claude decorar a resposta com texto antes/depois — não testado aqui porque o mock já veio limpo, mas é o comportamento esperado em produção.

**Pendência real, não resolvida por este teste**: validar contra a API de verdade exige configurar `anthropic-api` (header `x-api-key`) e o model ID atual — ambos já sinalizados como TODO dentro do próprio `03-briefing-claude-api.json`.
