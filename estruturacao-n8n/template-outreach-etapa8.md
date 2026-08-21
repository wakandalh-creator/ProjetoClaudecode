# Template de Outreach — Etapa 8 (WhatsApp, 5 linhas)

## v2 — Prévia-first (Hormozi, 2026-08-08) — TEMPLATE VIGENTE na fase manual

Com a decisão de construir a prévia ANTES do contato, o elemento mais forte do Hormozi destrava: **risk reversal total** — não vendemos promessa, mostramos produto pronto. A fórmula muda de "posso te mostrar?" (pede permissão = adiciona um passo) pra **hybrid hook**: CALLOUT + PROVA ESPECÍFICA + MECANISMO ("já fizemos") + RISCO ZERO + TAKEAWAY.

```
1. Gancho (callout + prova específica): "{Nome}, {nota} com {N} avaliações e {dor observável} — isso está custando cliente novo."
2. Mecanismo + risk reversal: "Em vez de te vender uma ideia, a gente já montou o site de vocês. Pronto, é só abrir:"
3. {LINK DA PRÉVIA}
4. Contraste: "Compara com o que aparece hoje quando alguém pesquisa '{nome}' no Google."
5. CTA esforço-zero + takeaway: "Se gostar, fica no ar em até 5 dias úteis. Se não fizer sentido, ignora e seguimos 🙂"
```

Por que cada peça (princípios do hook generator):
- **Callout nominal** = "isso é exatamente pra mim" instantâneo; número real (nota/avaliações) mata o cheiro de spam.
- **"Já montamos"** = mechanism hook + time-delay zero (não "em poucos dias" — JÁ).
- **Link direto** = elimina o passo de pedir permissão; o produto é o argumento.
- **Contraste antes/depois** = valor visível sem explicação.
- **Takeaway** ("ignora e seguimos") = remove pressão, aumenta resposta — e é honesto.

Follow-ups v2 (urgência REAL, nunca inventada):
- +2h: "Abre no celular, leva 30 segundos — foi feito sob medida pro {nome}, não é modelo pronto."
- +24h: "Curiosidade sincera: o que achou do site? Se tiver qualquer coisa que mudaria, me fala que eu ajusto antes de te mostrar de novo."
- Última (1 dia após as 48h): "Vou tirar a prévia do {nome} do ar na sexta pra dar lugar a outro projeto. Se quiser dar uma última olhada: {link}. Qualquer dia, se fizer sentido, é só chamar. Sucesso!" ← o takeaway aqui é verdadeiro: a prévia é reciclada mesmo.

A v1 abaixo permanece como referência (fase automatizada / leads sem prévia pronta).

---

Gerado com `hormozi-hooks` (variações de gancho) + `hormozi-pitch` (versão curta). Niche-agnostic — todos os campos entre `{chaves}` vêm do briefing da Etapa 3 (`03-briefing-claude-api.json`), nunca hardcoded pra salão/JF.

## 1. Mensagem-base (Hormozi — Core Message)

- **Audiência:** donos de negócio local (qualquer nicho, qualquer cidade/estado) com reputação real (avaliações, clientes recorrentes) mas presença digital fraca ou inexistente.
- **Resultado:** presença digital que traz clientes novos de forma previsível, sem depender só de indicação.
- **Dor:** `{briefing.padrao_de_dor}` — varia por prospect, extraído das avaliações reais dele (não suposição genérica).
- **Velocidade:** staging pronto em poucos dias.
- **Facilidade:** zero trabalho técnico da parte do dono — só aprovar ou pedir ajuste.
- **Objeção-chave:** "já tenho Instagram/site", "não tenho orçamento agora", "não confio em vendedor genérico".

## 2. Variações de gancho (testar, meta de resposta >8%)

| Tipo | Gancho |
|---|---|
| **Outcome** | "Conseguimos aumentar a chegada de clientes novos pra negócios como o {nome} sem depender só de indicação." |
| **Time-based** | "Em poucos dias conseguimos deixar pronta uma versão de teste da presença digital do {nome} — sem compromisso." |
| **Effort-reduction** | "Preparamos algo pro {nome} sem precisar que você mexa em nada — só decidir se aprova ou não." |
| **Callout** | "Se você é responsável pelo {nome} e sente que o negócio merece aparecer melhor online do que aparece hoje, isso é pra você." |
| **Pain** (recomendado como padrão) | "Reparamos que clientes do {nome} mencionam {padrao_de_dor_resumido} nas avaliações — isso tem solução, e queríamos te mostrar." |

**Recomendação:** usar o **Pain Hook** como padrão — é o único gancho ancorado num dado real e específico do prospect (vem direto do briefing da Etapa 3), o que aumenta a percepção de "isso não é spam genérico". Os outros 4 ficam como variantes pra teste A/B assim que o volume de outreach justificar (a meta de >8% de resposta já definida no piloto é o critério de corte).

## 3. Template completo (Gancho→Dor→Ponte→Prova→CTA)

```
1. Gancho: [uma das variações acima — padrão: Pain Hook]
2. Dor: Isso costuma custar clientes que decidem antes mesmo de entrar em contato — só pela primeira impressão.
3. Ponte: Por isso preparamos algo específico pro seu negócio, não um modelo genérico.
4. Prova: Baseado no que já funcionou pra negócios parecidos — nota {nota_google} nas suas próprias avaliações é real, e o padrão que aparece nelas a gente já sabe resolver.
5. CTA: Posso te mostrar o que preparamos? Sem compromisso.
```

## 4. Versão curta (hormozi-pitch, short version)

Pra reaproveitar como abertura mais compacta (ex.: fallback de e-mail do Caminho B, ou variação de teste):

```
Analisamos o {nome} e identificamos um padrão específico nas suas avaliações que pode estar custando clientes — preparamos uma solução sob medida pra isso, sem compromisso pra ver.
```

## Onde isso entra no pipeline

Substitui o texto genérico do node **"Montar mensagem 1 (primeiro contato)"** em `06-outreach-whatsapp.json`, agora parametrizado com `$json.briefing.padrao_de_dor`, `$json.nicho` e `$json.nota_google` (todos já existentes desde a Etapa 3, ver `schema-briefing-etapa3.md`). As mensagens 2/3/4 (follow-ups 2h/24h/48h) continuam como estavam — são reengajamento, não o gancho principal, e já são propositalmente mais soft.
