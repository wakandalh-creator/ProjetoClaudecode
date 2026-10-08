# Checklist QA Final (Web OS)

Preenchido pelo Eixo (módulo 24) antes de declarar um projeto `pronto-para-publicar`. Modelado na seção 53 do documento-fonte NEOVERTIX WEB OS. Regra: nunca marcar um domínio "N/A — Sprint N" depois que o módulo dono dele já existir — nesse ponto ele vira cobrível de verdade.

| Domínio | Item | Módulo que cobre | Status neste projeto |
|---|---|---|---|
| Business | Objetivo, público, oferta, diferenciais | 20 | — |
| UX/UI | Design system, componentes, responsividade | 21 | — |
| UX/UI | Mobile + desktop, acessibilidade | 22 | — |
| Performance | LCP/INP/CLS, auditoria rodada | 23 | — |
| SEO | Titles, meta, H1/H2/H3, URLs, sitemap, robots, canonical, schema, links internos | 29-32 | N/A — Sprint 3 |
| Local | GBP, NAP, categorias, serviços, reviews, fotos, páginas locais | 31 | N/A — Sprint 3 |
| AI | AEO, GEO, entity map, schema, FAQ, llms.txt | 30, 32 | N/A — Sprint 3 |
| Tracking | GA4, GTM, Search Console, eventos, conversões, UTM, CRM | 33-35 | N/A — Sprint 4 |
| Security | Secrets, auth, authz, database, storage, upload, rate limit, CORS, headers, LGPD | 37-38 | N/A — Sprint 5 |
| Copy/CRO | Framework de copy, CTAs, objeções, oferta | 26 | N/A — Sprint 2 |

## Como preencher "Status neste projeto"

- `✅ ok` — item verificado e conforme.
- `⚠️ pendência: <descrição>` — item relevante mas com dado faltante ou ajuste necessário.
- `N/A — Sprint N` — módulo dono ainda não existe nesta versão do Web OS (não é falha do projeto, é limite do sistema).

Nenhuma combinação de `✅ ok` em todas as linhas disponíveis substitui a aprovação humana em `_sop/aprovacao-publicacao.md`.
