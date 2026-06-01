# Módulo 5 — Modelos de Conteúdo

## Objetivo

Identificar e catalogar os 10 modelos de conteúdo que mais geram resultado entre todos os perfis monitorados. Construir um repertório reutilizável com frequência, performance, contexto ideal e exemplos de hook para cada modelo.

## Dependência

Requer os relatórios:
- `reports/YYYY-MM-DD/02-perfis-instagram.md` (padrões por perfil)
- `reports/YYYY-MM-DD/03-benchmark.md` (top conteúdos e padrões transversais)
- `reports/YYYY-MM-DD/04-top10-analise.md` (frameworks identificados)

## Modelos a detectar

Os modelos abaixo são os candidatos principais. O sistema deve detectar os que aparecem nos dados, não inventar:

| ID | Nome | Descrição |
|----|------|-----------|
| `tutorial_rapido` | Tutorial Rápido | "Como fazer X em N passos" |
| `erro_comum` | Erro Comum | "O erro que todo mundo comete ao fazer X" |
| `pov` | POV | Ponto de vista pessoal sobre tendência ou decisão |
| `storytelling` | Storytelling | Narrativa pessoal com arco emocional |
| `antes_depois` | Antes/Depois | Transformação ou comparação temporal |
| `bastidores` | Bastidores | Processo, rotina ou bastidores reais |
| `lista_checklist` | Lista/Checklist | "X coisas que você precisa saber/fazer" |
| `case_real` | Case Real | Resultado de um projeto ou cliente real |
| `opiniao_forte` | Opinião Forte | Posicionamento polarizador sobre tema do nicho |
| `trend_adaptada` | Trend Adaptada | Formato/trend viral adaptado ao nicho |

## Instrução para o agente

### Passo 1 — Mapear modelos encontrados nos dados

Leia os três relatórios de dependência.

Para cada conteúdo analisado, classifique-o em um dos modelos acima (ou crie um novo se o padrão não se encaixar).

### Passo 2 — Agregar métricas por modelo via Swarm

**Tasks:** um objeto por modelo detectado.

```javascript
instruction: "Analise o modelo de conteúdo '{nome_modelo}' com base nos dados coletados dos perfis monitorados. Quantos conteúdos foram classificados neste modelo? Qual a taxa de performance? Em quais perfis aparece? Qual o contexto ideal de uso? Qual a facilidade de produção? Gere um exemplo de hook para este modelo adaptado ao nicho de IA e automação."

context: "Dados dos perfis monitorados: {resumo_dos_dados}. Negócio de Lucas: {business_positioning}."

responseSchema: {
  type: "object",
  additionalProperties: false,
  properties: {
    nome_modelo: { type: "string" },
    descricao: { type: "string" },
    frequencia_absoluta: { type: "number", description: "Quantos conteúdos deste modelo foram encontrados." },
    taxa_performance: { type: "string", enum: ["alta", "media", "baixa"] },
    perfis_que_usam: { type: "array", items: { type: "string" } },
    contexto_ideal: { type: "string", description: "Quando usar este modelo: objetivo, momento da jornada, etc." },
    facilidade_producao: { type: "string", enum: ["facil", "media", "dificil"] },
    potencial_negocio_lucas: { type: "string", enum: ["alto", "medio", "baixo"] },
    justificativa_potencial: { type: "string" },
    exemplo_hook_adaptado: { type: "string", description: "Hook de exemplo para o nicho de IA e automação." },
    exemplo_estrutura: { type: "string", description: "Estrutura típica do modelo em passos." }
  },
  required: ["nome_modelo", "frequencia_absoluta", "taxa_performance", "contexto_ideal", "facilidade_producao", "potencial_negocio_lucas", "exemplo_hook_adaptado"]
}

concurrency: 3
batchSize: 5
```

**Retry:**
```javascript
filter: { column: "taxa_performance", exists: false }
```

### Passo 3 — Rankear e selecionar Top 10

Com `rows()`, recupere todos os modelos.

Ordene por:
1. `taxa_performance` (alta primeiro)
2. `frequencia_absoluta` (maior primeiro)
3. `potencial_negocio_lucas` (alto primeiro)

Selecione os Top 10 (ou todos se houver menos de 10).

### Passo 4 — Gerar relatório

Escreva `reports/YYYY-MM-DD/05-modelos-conteudo.md` com:

**Seção 1 — Ranking dos 10 Modelos**

Para cada modelo:

```markdown
### #N — {nome_modelo}

**Descrição:** {descricao}
**Frequência nos dados:** {frequencia_absoluta} conteúdos
**Taxa de performance:** Alta/Média/Baixa
**Perfis que mais usam:** @handle1, @handle2
**Contexto ideal:** {contexto_ideal}
**Facilidade de produção:** Fácil/Média/Difícil
**Potencial para o negócio:** Alto/Médio/Baixo — {justificativa}

**Hook de exemplo:**
> "{exemplo_hook_adaptado}"

**Estrutura:**
{exemplo_estrutura}
```

**Seção 2 — Matriz de Decisão**

Tabela cruzando facilidade de produção × potencial de resultado:

|  | Alta Performance | Média Performance | Baixa Performance |
|--|-----------------|-------------------|-------------------|
| **Fácil** | Fazer agora | Testar | Deprioritizar |
| **Médio** | Planejar | Avaliar | Ignorar |
| **Difícil** | Investir quando escalar | Reservar | Descartar |

**Seção 3 — Recomendação de Sequência**

"Para começar, priorize: modelo A → modelo B → modelo C"
Justificativa baseada em facilidade + potencial.
