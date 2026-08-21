# Guardião do Cutover — protocolo de troca de DNS sem prejudicar o cliente

Runbook operacional executado pelo agente (Claude Code) em **todo** go-live de cliente.
Na fase manual, o agente roda cada gate na mão. Na fase n8n, este documento é a spec
para endurecer o workflow `09-deploy-hostinger` (hoje ele só checa MX e para — não tem
snapshot, verificação pós-cutover nem rollback).

**Princípio único: nenhum registro DNS do cliente muda sem snapshot antes, verificação
depois e caminho de volta documentado.**

Nota 2026-08-05: na fase manual o destino do apontamento é a **Vercel** (não a Hostinger)
— o protocolo é agnóstico de host e não muda; onde este doc diz "Hostinger", leia
"destino do deploy da fase vigente". A Hostinger volta a ser o destino quando a operação
migrar (5+ sites / decisão de caixa).

---

## Regras invioláveis (o guardião NUNCA)

1. **Nunca** transfere a titularidade do domínio para fora do CNPJ/CPF do cliente.
2. **Nunca** troca nameservers (NS) de um domínio que tem MX ativo — a não ser que a
   zona inteira (MX, SPF, DKIM, DMARC, tudo) já esteja replicada 1:1 no destino e
   validada.
3. **Nunca** deleta registro DNS. Registro que "sobrou" fica; só se altera o que aponta
   para o site (A/AAAA/CNAME de `@` e `www`).
4. **Nunca** cancela a hospedagem/serviço antigo no dia do cutover. Mínimo 30 dias no ar
   em paralelo.
5. **Nunca** faz cutover sem o site novo já testado e no ar no destino (staging validado).
6. Qualquer anomalia em qualquer gate → **PARA**, avisa o fundador (Telegram/WhatsApp) e
   não segue sozinho.

---

## Gate 0 — Na prospecção (antes até da venda) — Caminho B

Para todo lead que já tem site/domínio, registrar na planilha de leads a coluna
`dominio_status`:

- **Titular**: quem é o dono no WHOIS/registro.br? (cliente / agência / não identificado)
- **DNS host**: onde a zona está hospedada (registro.br, Cloudflare, locaweb, GoDaddy…)
- **MX**: tem e-mail no domínio? De qual provedor (Google Workspace, Titan, Zoho…)?
- **Risco**: `baixo` (cliente é titular, sem MX) / `médio` (cliente titular, MX ativo) /
  `alto` (domínio no nome de terceiro — negociar recuperação antes de prometer prazo)

Comando de referência (DoH, sem depender de ferramenta local):
`curl "https://dns.google/resolve?name=<dominio>&type=MX"` (idem para `A`, `NS`, `TXT`).

---

## Gate 1 — Pré-cutover: snapshot completo (obrigatório)

Rodar **antes de tocar em qualquer painel**. Salvar em
`estruturacao-n8n/clientes/<slug>/dns-snapshot-<AAAA-MM-DD>.json`:

Registros a capturar (via DoH ou `nslookup -type=<tipo>`):
- `A` e `AAAA` de `@` e `www`
- `CNAME` de `www`
- `MX` (todos, com prioridade)
- `TXT` de `@` (SPF), `_dmarc.<dominio>` (DMARC)
- DKIM: `default._domainkey`, `google._domainkey`, `titan1._domainkey`,
  `zoho._domainkey` (testar os seletores comuns do provedor identificado no MX)
- `NS` e `SOA`
- TTLs de cada registro

Além do JSON: anotar registrar, painel de DNS, quem tem o acesso, e — se houver acesso
ao painel — screenshot da zona completa.

**Checklist de saída do Gate 1:**
- [ ] Snapshot salvo e legível (reabrir o arquivo e conferir)
- [ ] Provedor de e-mail identificado (ou confirmado "sem e-mail no domínio")
- [ ] Site novo no ar e validado no destino (URL temporária Hostinger / preview) —
      HTTP 200, HTTPS ok, mobile ok
- [ ] Se o painel permitir: TTL dos registros a alterar reduzido para 300s
      (espera-se o TTL antigo expirar antes do cutover — rollback fica rápido)
- [ ] Cliente avisado do dia/horário e do que pode acontecer (janela de propagação)

---

## Gate 2 — Cutover cirúrgico

- Mudança feita **no painel de DNS atual do cliente** (registro.br, Cloudflare etc.),
  não movendo a zona.
- Alterar **somente**: `A`/`AAAA` de `@` e `www` (ou `CNAME` de `www`) → IP/host da
  Hostinger.
- MX, TXT, DKIM, DMARC, NS: **intocados**.
- Migração de nameservers para a Hostinger só em dois casos: (a) domínio sem MX; ou
  (b) zona replicada 1:1 na Hostinger e conferida registro a registro contra o snapshot
  **antes** da troca de NS. Com a zona na Hostinger, usar a API de DNS (validate +
  snapshots nativos da Hostinger) — o rollback vira uma chamada de restore.
- Registrar no arquivo do cliente: o que foi alterado, valor antigo → valor novo,
  horário.

---

## Gate 3 — Verificação pós-cutover (até 24h, com marcos)

**Imediato (0–30 min, repetir a cada ~10 min até propagar):**
- [ ] `@` e `www` resolvem para o novo destino (DoH `type=A`)
- [ ] Site abre com HTTP 200 no apex e no www; redirect entre eles funciona
- [ ] HTTPS válido (certificado emitido na Hostinger — não deixar o cliente ver aviso
      de certificado)
- [ ] **MX idêntico ao snapshot** (diff literal contra o JSON do Gate 1)
- [ ] SPF/DKIM/DMARC idênticos ao snapshot

**Com o cliente (mesmo dia):**
- [ ] Cliente envia um e-mail de teste do endereço profissional e recebe um de volta
- [ ] Cliente abre o site no celular dele (rede móvel, não wifi — pega DNS de operadora)

**24h depois:**
- [ ] Repetir o diff completo do snapshot (nada além de A/AAAA/CNAME mudou)
- [ ] Workflow `10-monitoramento-pos-entrega` ativo para o domínio (uptime 15/15min)

---

## Gate 4 — Rollback (critérios objetivos, sem julgamento no calor do momento)

Voltar os registros para os valores do snapshot **imediatamente** se:
- Site fora do ar > 30 min após propagação esperada; ou
- **Qualquer** falha de e-mail relatada ou detectada (envio ou recebimento); ou
- Certificado HTTPS não emitido em 24h.

Rollback = reaplicar os valores antigos do JSON do Gate 1 no mesmo painel (por isso o
TTL de 300s no Gate 1 — a volta propaga em minutos). Zona na Hostinger: restore do
snapshot nativo via API. Depois do rollback: diagnóstico com calma, cliente avisado com
transparência, novo cutover só com a causa corrigida.

---

## Deltas para o workflow `09-deploy-hostinger` (fase n8n)

O que este runbook adiciona por cima do que o `09` já faz:

1. Antes do IF de MX: node que captura o snapshot completo (todos os tipos acima via
   DoH) e persiste (arquivo/planilha), não só MX.
2. Depois do FTP: bloco de verificação pós-cutover (HTTP 200 apex+www, HTTPS, diff de
   MX/TXT contra o snapshot) com retry — falhou → Telegram com o diff, não seguir.
3. Node de rollback semiautomático: mensagem no Telegram com os valores antigos prontos
   para colar (ou chamada de restore, se a zona estiver na Hostinger).
4. O disparo do `10` só acontece após o bloco 2 passar (hoje dispara direto após o FTP).
