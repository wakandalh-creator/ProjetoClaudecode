# Como Gerenciar o Sistema de Monitoramento

## Rodar o sistema

No Claude Code, escreva:
```
Execute o monitor — leia monitor/run.md
```

Para módulos individuais:
```
Execute apenas o módulo de tendências — leia monitor/modules/01-trends.md
Execute apenas o Instagram — leia monitor/modules/02-instagram.md
```

---

## Adicionar um perfil do Instagram

Edite `config/profiles.json` e adicione um objeto ao array `profiles`:

```json
{
  "handle": "nomeDoPerfil",
  "url": "https://www.instagram.com/nomeDoPerfil/",
  "category": "founder",
  "tags": ["ia", "automacao"],
  "active": true,
  "notes": "Por que você monitora este perfil"
}
```

**Categorias disponíveis:** `ia`, `marketing`, `automacao`, `creator`, `agencia`, `founder`, `negocio-digital`

## Desativar temporariamente um perfil

Mude `"active": false` no objeto do perfil desejado.

---

## Atualizar o contexto do seu negócio

Edite `config/business.json`. Campos mais importantes:
- `positioning` — seu posicionamento atual
- `offers` — liste seus produtos/serviços
- `avoid_topics` — temas que não quer que o sistema sugira

---

## Adicionar fonte de tendências

Edite `config/sources.json`:
- `topics` — adicione temas para monitorar
- `web_sources` — adicione URLs de sites para vasculhar
- `search_queries` — adicione queries de busca específicas

---

## Ver relatórios

Os relatórios ficam em `reports/YYYY-MM-DD/`:

| Arquivo | Conteúdo |
|---------|----------|
| `01-tendencias.md` | Novidades da semana em IA, marketing, SaaS |
| `02-perfis-instagram.md` | Análise de padrões dos perfis monitorados |
| `03-benchmark.md` | Top conteúdos e métricas de performance |
| `04-top10-analise.md` | Análise profunda dos 10 melhores conteúdos |
| `05-modelos-conteudo.md` | Os 10 modelos de conteúdo mais eficazes |
| `06-aplicacao-negocio.md` | Insights e conteúdos prontos para produção |
| `RESUMO.md` | Highlights consolidados de todos os módulos |

---

## Gerar conteúdo visual (Fases 3 e 4)

O Módulo 6 pode gerar imagens via Gemini API. Para isso você precisa:

1. Uma `GOOGLE_API_KEY` (gratuita em https://aistudio.google.com/apikey)
2. Dizer ao Claude: "Gere imagens para os posts do relatório de hoje"

O script `gerar_posts.js` será criado automaticamente no diretório `reports/YYYY-MM-DD/`.

---

## Agendar a rotina

Para criar uma rotina semanal automática, escreva no Claude Code:
```
/schedule Toda segunda-feira às 8h: execute o sistema de monitoramento — leia monitor/run.md
```
