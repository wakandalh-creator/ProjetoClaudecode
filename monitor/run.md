# Monitor — Orquestrador Principal

Você é o orquestrador do sistema de monitoramento de tendências e Instagram do Lucas.

## Antes de começar

Leia estes três arquivos de configuração:
- `config/business.json` — posicionamento, nicho, público e tom do negócio
- `config/sources.json` — fontes, tópicos e queries de busca
- `config/profiles.json` — perfis do Instagram a monitorar

Registre mentalmente:
- A data de hoje no formato `YYYY-MM-DD`
- Se `profiles` está vazio (modo descoberta) ou tem perfis ativos (modo análise)

## Criar pasta do relatório

Crie a pasta `reports/YYYY-MM-DD/` com a data de hoje.
Se já existir, use a existente.

## Executar módulos em sequência

Execute os módulos abaixo **um por vez**, na ordem indicada.
**Salve o relatório de cada módulo antes de avançar para o próximo.**
Confirme que o arquivo foi criado antes de prosseguir.

---

### Módulo 1 — Tendências

Leia `monitor/modules/01-trends.md` e execute todas as instruções.

Entregável: `reports/YYYY-MM-DD/01-tendencias.md` ✓

---

### Módulo 2 — Instagram

Leia `monitor/modules/02-instagram.md` e execute todas as instruções.

**Se a lista de perfis estiver vazia:**
- Execute o Modo Descoberta
- Apresente as sugestões ao usuário
- Aguarde confirmação antes de prosseguir para o Módulo 3

**Se houver perfis ativos:**
- Execute a análise completa com a Fase 1 do `instagram-content-cloner`

Entregável: `reports/YYYY-MM-DD/02-perfis-instagram.md` ✓

---

### Módulo 3 — Benchmark

Leia `monitor/modules/03-benchmark.md` e execute todas as instruções.

Depende do Módulo 2 — só inicie após confirmar que `02-perfis-instagram.md` existe.

Entregável: `reports/YYYY-MM-DD/03-benchmark.md` ✓

---

### Módulo 4 — Análise Top 10

Leia `monitor/modules/04-top10-analysis.md` e execute todas as instruções.

Depende do Módulo 3 — só inicie após confirmar que `03-benchmark.md` existe.

Entregável: `reports/YYYY-MM-DD/04-top10-analise.md` ✓

---

### Módulo 5 — Modelos de Conteúdo

Leia `monitor/modules/05-content-models.md` e execute todas as instruções.

Depende dos Módulos 2, 3 e 4.

Entregável: `reports/YYYY-MM-DD/05-modelos-conteudo.md` ✓

---

### Módulo 6 — Aplicação ao Negócio

Leia `monitor/modules/06-business-apply.md` e execute todas as instruções.

Depende de todos os módulos anteriores.

Este módulo usa a **Fase 2 do `instagram-content-cloner`** para gerar os textos completos dos posts.

Se o usuário solicitar imagens, execute também as Fases 3 e 4.

Entregáveis:
- `reports/YYYY-MM-DD/06-aplicacao-negocio.md` ✓
- `reports/YYYY-MM-DD/RESUMO.md` ✓

---

### Módulo 7 — Exportação para Obsidian

Leia `monitor/modules/07-obsidian-export.md` e execute todas as instruções.

Depende do Módulo 1 (obrigatório) e do Módulo 6 (opcional, enriquece a exportação).

Este módulo converte os relatórios em **notas atômicas** no vault Obsidian, alimentando
o banco de conhecimento que a skill `daydream` usará no futuro.

Leia `config/obsidian.json` antes de iniciar — se `enabled` for `false`, pule este módulo.

Entregáveis (no vault Obsidian):
- `Monitor/Tendencias/YYYYMMDD-*.md` (N notas de tendências) ✓
- `Monitor/Ideias/YYYYMMDD-*.md` (5 notas de ideias de conteúdo) ✓
- `Monitor/Insights/YYYYMMDD-*.md` (N notas de insights) ✓
- `Monitor/Perfis/@handle.md` (atualizado ou criado) ✓
- `Monitor/Daily/YYYY-MM-DD-monitor.md` (índice do dia) ✓

---

## Ao finalizar

Confirme ao usuário:

```
✅ Monitoramento concluído — {DATA}

Relatórios gerados em reports/{DATA}/:
• 01-tendencias.md
• 02-perfis-instagram.md
• 03-benchmark.md
• 04-top10-analise.md
• 05-modelos-conteudo.md
• 06-aplicacao-negocio.md
• RESUMO.md

📓 Obsidian atualizado:
• {N} tendências, {N} ideias, {N} insights exportados
• Índice: Monitor/Daily/{DATA}-monitor.md

Próxima ação recomendada: leia o RESUMO.md para os highlights
ou 06-aplicacao-negocio.md para os posts prontos para produção.

Quer que eu gere as imagens para os posts via Gemini? (precisa de GOOGLE_API_KEY)
```

---

## Regras gerais para todos os módulos

- Nunca invente dados — se não encontrar, documente a limitação
- Salve cada relatório antes de avançar
- Siga as regras do Swarm: `concurrency: 3`, `batchSize: 5`, retry obrigatório, `additionalProperties: false`
- Inclua sempre `context` anti-alucinação em cada run do Swarm
- Use `rows()` para validar resultados antes de gerar o relatório
- Se uma fonte estiver inacessível, registre e continue — não interrompa o fluxo

## Execução parcial

Para rodar apenas um módulo específico, diga:
```
Execute apenas o Módulo 1 — leia monitor/modules/01-trends.md
Execute apenas o Instagram — leia monitor/modules/02-instagram.md
```
