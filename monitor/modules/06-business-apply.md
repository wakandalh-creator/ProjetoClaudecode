# Módulo 6 — Aplicação ao Negócio

## Objetivo

Síntese estratégica de todos os dados coletados. Transformar análise em ação: formatos para testar, hooks prontos, ideias de conteúdo adaptadas ao posicionamento do Lucas, oportunidades de nicho e, opcionalmente, geração de imagens via Gemini (Fases 2-4 da skill `instagram-content-cloner`).

## Dependência

Requer todos os relatórios do dia:
- `reports/YYYY-MM-DD/01-tendencias.md`
- `reports/YYYY-MM-DD/02-perfis-instagram.md`
- `reports/YYYY-MM-DD/03-benchmark.md`
- `reports/YYYY-MM-DD/04-top10-analise.md`
- `reports/YYYY-MM-DD/05-modelos-conteudo.md`
- `config/business.json`

## Instrução para o agente

### Passo 1 — Carregar contexto completo

Leia `config/business.json` para absorver o posicionamento atual, nicho, público, tom e ofertas do Lucas.

Leia todos os relatórios do dia listados acima. Construa um mapa mental dos principais achados antes de prosseguir.

### Passo 2 — Gerar insights estratégicos

Responda cada bloco abaixo com base **exclusivamente nos dados coletados** — nunca em suposições genéricas.

---

#### Bloco A — Formatos para testar esta semana

Selecione **3 formatos** com maior probabilidade de resultado para Lucas agora.

Critérios de seleção:
- Alta replicabilidade (do Módulo 4)
- Alta performance nos dados (do Módulo 3)
- Fácil ou média produção (do Módulo 5)
- Alinhado com o posicionamento atual (de `business.json`)

Para cada formato:
- Nome e tipo (reel/carrossel/foto)
- Por que agora (justificativa baseada nos dados)
- Modelo de referência (perfil + conteúdo específico)
- Hook sugerido adaptado ao nicho de Lucas

---

#### Bloco B — Hooks adaptados ao posicionamento

Pegue os **5 melhores hooks** identificados nos dados (Módulos 2, 3 e 4).

Para cada um, entregue:
- Hook original (exato, com atribuição ao perfil)
- Hook adaptado para o negócio de Lucas
- Modelo de conteúdo onde encaixa melhor
- Emoção que o hook dispara

---

#### Bloco C — Top 5 ideias de conteúdo prontas para produção

Gere **5 ideias completas e acionáveis**, cada uma pronta para ser produzida hoje.

Para cada ideia:
```
Título: {nome interno}
Formato: reel / carrossel / foto
Hook: "{hook completo, pronto para usar}"
Estrutura:
  1. [abertura — problema ou fenômeno]
  2. [contexto ou dado]
  3. [decodificação ou framework]
  4. [conexão com o leitor]
  5. [insight ou transformação]
  6. [CTA]
CTA: "{chamada para ação exata}"
Modelo base: {nome do modelo de conteúdo}
Referência: @{handle} — {conteúdo que inspirou}
Tempo estimado: {X} minutos para produzir
```

---

#### Bloco D — Oportunidades de nicho

**Lacunas:** Temas com alta demanda nos dados mas pouca oferta nos perfis monitorados.

**Formatos underused:** Formatos que funcionam no mercado mas os criadores do nicho do Lucas pouco exploram.

**Tendências para capitalizar agora:** Do relatório de tendências (Módulo 1), o que pode virar conteúdo imediatamente.

**Oportunidades de autoridade:** Onde Lucas pode ser referência que ainda não existe no nicho.

**Oportunidades de aquisição:** Conteúdos que naturalmente atraem o público-alvo descrito em `business.json`.

**Oportunidades de conversão:** Formatos que levam à ação (DM, link na bio, comentário) mais naturalmente.

---

#### Bloco E — Pergunta estratégica obrigatória

Para cada insight relevante dos módulos anteriores, responder explicitamente:

**"Como posso adaptar isso para meu negócio, meu posicionamento e minha estratégia?"**

Formato:
```
Insight: {o que foi encontrado nos dados}
Adaptação: {como Lucas especificamente aplica}
Próxima ação: {o que fazer nos próximos 3 dias}
```

---

### Passo 3 — Geração de conteúdo textual (Fase 2 — instagram-content-cloner)

Após gerar o Bloco C, use a **Fase 2 da skill `instagram-content-cloner`** para redigir os textos completos das 5 ideias.

Regras obrigatórias:
- **Linha 1 = hook puro** — sem apresentação, sem "Olá", entra direto
- Desenvolvimento segue a estrutura definida no Bloco C
- CTA coerente com o padrão dominante dos perfis analisados
- Tom replicando os adjetivos extraídos de `config/business.json`
- Tamanho respeitando a média identificada no Módulo 2

Para cada post, entregar no formato:
```
POST [N] — {título da ideia}
{texto completo}

---
Hook usado: {modelo}
Estrutura: {resumo do fluxo}
CTA: {tipo}
```

---

### Passo 4 — Geração de imagens (opcional — Fases 3+4)

Se o usuário solicitar imagens, ou se houver `GOOGLE_API_KEY` disponível no ambiente:

1. Pergunte ao usuário: "Quer que eu gere as imagens para os posts acima via Gemini?"
2. Se confirmado, execute as **Fases 3 e 4 da skill `instagram-content-cloner`**:
   - Fase 3: extraia parâmetros visuais de uma imagem de referência fornecida pelo usuário
   - Fase 4: gere as imagens com `gemini-3.1-flash-image-preview`
3. Salve os arquivos em `reports/YYYY-MM-DD/output/`

---

### Passo 5 — Gerar relatórios finais

**Escreva `reports/YYYY-MM-DD/06-aplicacao-negocio.md`** seguindo o template `monitor/templates/report-insights.md`.
Inclua todos os blocos A-E + os textos completos dos posts (Fase 2).

**Escreva `reports/YYYY-MM-DD/RESUMO.md`** — consolidado de todos os módulos em no máximo 2 páginas:

```markdown
# Resumo Semanal — {DATA}

## Tendências em Destaque (Módulo 1)
- {3 bullets das principais novidades}

## Perfis Analisados (Módulo 2)
- {N} perfis monitorados
- Formato dominante: {formato}
- Hook mais comum: {modelo}

## Top Conteúdo da Semana (Módulo 3)
- @{handle} — "{tema}" — {por que se destacou}

## Insights Estratégicos (Módulos 4+5)
- {3 bullets dos principais insights}

## Ações para Esta Semana (Módulo 6)
1. Produzir: {ideia 1}
2. Produzir: {ideia 2}
3. Testar: {formato ou hook novo}

## Posts Prontos para Publicar
- [Ver relatório completo](06-aplicacao-negocio.md)
```
