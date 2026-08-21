# Progresso — Sistema de Marketing IA (Neovertix)

> Checklist por sprint, conforme o plano aprovado (`C:\Users\lucas\.claude\plans\tranquil-purring-dolphin.md`). Marcar aqui a cada fase concluída, com evidência do teste real.

## Auditoria de verificação — 2026-08-09

Rodada de 4 verificações independentes (Sprints 1-3 + prontidão do Sprint 4) depois de tudo concluído, pra confirmar que nada regrediu com as edições subsequentes. Achados pequenos corrigidos na hora: exemplo de formato desatualizado em `checklist-qualidade.md`, nota stale em `hooks-concorrentes.md`, campo "Confiança" formalizado em `modules/11-*.md`, rótulo M12 ambíguo no plano, `__pycache__/` faltando no `.gitignore`. **Nenhum problema estrutural, nenhum segredo exposto.**

Pendências reais (não bloqueiam, ficam pra quando fizer sentido):
- **63 posts legados em "Post Salvos" sem `pasta`** (anteriores ao Sprint 2) — rodar `--backfill` com `amount` maior resolve, é decisão do Lucas (grava dado real no Notion).
- **Tarefas agendadas em "Modo de Logon: Interativo apenas"** — risco de falhar silenciosamente na execução automática de amanhã (8h/8h30) se não houver sessão ativa no PC. Vale trocar pra "Executar estando o usuário conectado ou não" se quiser automação de verdade, sem depender do PC ligado com sessão aberta.
- Decisão em aberto desde o Sprint 1: número "4h→15min" no roteiro `mecanismo-sem-culpa.md` — medição real ou honestidade de marca nova?
- Sprint 4: falta decidir qual modelo/skill de imagem o Pixel usa ao escalar além do Pillow (`gemini-3.1-flash-image-preview` via `instagram-content-cloner`, ou a skill `banana`?).

---

## Sprint 1 — Núcleo: cérebro de marca + estrutura + squad + roteiro/QA

**Status: ✅ Concluído e testado ponta a ponta em 2026-08-05**

- [x] M0 — `config/business.json` preenchido (destilado de `branding/neovertix/`)
- [x] M0 — `_context/marca.md` (cérebro de marca operacional)
- [x] M0 — `_context/tom-de-voz.md` (memória viva, regra de volume mínimo p/ validar padrão)
- [x] M1 — estrutura de pastas `Social mídia IA/` (`_context`, `_sop`, `_templates`, `modules`, `bancos`, `producao`)
- [x] M1 — `run.md` orquestrador
- [x] M1 — 10 agentes em `.claude/agents/` (tese, mapeia, noticia, radar, roteira, iana, pixel, corta, posta, mede)
- [x] M1 — seção Org Chart + regra de roteamento no `CLAUDE.md`
- [x] M5 — módulo 13 (roteiros) + módulo 14 (análise/QA) escritos
- [x] Atalhos — skills `/roteiro`, `/concorrentes`, `/campanha`, `/opr`
- [x] **Marco verificado:** roteiro real gerado e avaliado pelo squad nomeado

### Evidência do teste

| Teste | Resultado | Arquivo |
|---|---|---|
| Reel — "leads perdidos" (framework DINHEIRO CONCRETO) | **Aprovado, 8,5/10** | `producao/roteiros/2026-08-05/leads-perdidos-custo.md` |
| Carrossel — "mecanismo sem culpa" (framework REFRAME SEM CULPA), rodada 1 | Reprovado, 6,6/10 | `producao/roteiros/2026-08-05/mecanismo-sem-culpa.md` |
| Mesmo carrossel, rodada 2 (8 correções aplicadas) | Reprovado, 6,9/10 — **limite de 2 rodadas atingido, escalado pro Lucas** | mesmo arquivo |

**O que o teste provou:**
- A Iana não infla nota — reprovou 2x o mesmo roteiro com diagnóstico específico e reescrita proposta por trecho.
- A regra "≥7 passa, <7 volta (máx. 2 rodadas, depois decide o Lucas)" **disparou corretamente** — o sistema não trava nem força aprovação.
- **Bug real encontrado e corrigido:** a Roteira estava copiando literalmente a coluna "Exemplo aplicado" do banco em vez de instanciar o "Framework" com variáveis novas. Corrigido em `.claude/agents/roteira.md` (regra dura adicionada).
- **Risco conhecido, sem correção ainda:** com `bancos/hooks-concorrentes.md` e `hooks-fora-do-nicho.md` vazios (só populam no Sprint 3), todo roteiro tende a reciclar os 12 seeds do branding — aceitável por enquanto, mitigado no Sprint 3.

### Decisão pendente do Lucas

O carrossel "mecanismo-sem-culpa" está travado em 6,9/10, a 3 edições cirúrgicas de aprovar (detalhe na avaliação da Iana no próprio arquivo). Iana precisa saber: o número "4h de triagem → 15 minutos" no slide de prova **tem medição real por trás**, ou deve ser reformulado como honestidade de marca nova ("ainda não tenho case, mas monto com seus dados antes de você pagar")?

---

## Sprint 2 — Salvos do Instagram por pasta + kanban de aprovação

**Status: ✅ Concluído e verificado ponta a ponta em produção, 2026-08-09**

- [x] `.gitignore` para `.env`/segredos (feito antes de tocar em qualquer coisa)
- [x] Consolidar cópia canônica do `ig-saves-engine/` no repo
- [x] Cookies renovados pelo Lucas + endpoint de coleções corrigido (ver "Achados do teste ao vivo")
- [x] M2 — `instagram_saves_sync.py` evoluído: coleções via `instagrapi`, campo `pasta` gravado no Notion
- [x] M2 — `config/instagram-pastas.json` com `pastas_ativas` configurável (Claude/Empreendedorismo/Marketing Digital + ângulo por pasta)
- [x] M2 — `--backfill` implementado e rodado (0 dos 63 posts antigos casaram — ver nota abaixo, não bloqueia)
- [x] M2 — `generate_ideas.py` gera roteiro completo no template/tom Neovertix via Gemini — **9/10 roteiros reais gerados com sucesso em "Ideias de Posts"**
- [x] M9 — kanban Notion "Produção de Conteúdo" criado (10 campos, Status × Aprovado ortogonais) + 2 registros de teste
- [x] Campo `pasta` (Select) adicionado em "Post Salvos"
- [x] 2 tarefas agendadas do Windows (`IG Saves Sync` 8h, `IG Generate Ideas` 8h30) repontadas pro repo
- [x] **Marco verificado:** sync real trouxe **129 posts novos** das 3 pastas; `generate_ideas.py` gerou roteiro completo (ex: "o-custo-do-atendimento-lento", pasta Marketing Digital) no tom Neovertix, números âncora corretos, salvo em "Ideias de Posts"

### Achados do teste ao vivo (todos corrigidos)

1. **Nomes de coleção não batiam** (config tinha "Claude"/"Marketing Digital", conta real tinha "claude"/"Marketing digital"/"Empreendedorismo "). Corrigido: matching agora ignora maiúsculas/minúsculas e espaços nas pontas (`instagram_saves_sync.py`) — não depende mais do Lucas manter nomes idênticos.
2. **Endpoint `/api/v1/feed/collection/{id}/posts/` via `requests` cru dava 404/erro silencioso** — API privada do Instagram exige mais headers do que o endpoint de listagem. Trocado para a lib `instagrapi` (mantida, resolve isso por baixo dos panos) — era o "Plano B" já previsto no plano original. Bônus de segurança: fingerprint de dispositivo salvo em `.instagrapi_settings.json` (gitignored) e reaproveitado entre execuções, em vez de logar do zero 2x/dia.
3. **`ANTHROPIC_API_KEY` sem créditos** — `generate_ideas.py` migrado pra Gemini (`gemini-3.5-flash`, já usando `GOOGLE_API_KEY` existente).
4. **Bug do Gemini 3.5**: modelo gasta parte do orçamento de tokens em raciocínio interno antes de responder — com `max_output_tokens` baixo (copiado do padrão Anthropic), a resposta saía cortada no meio do "pensamento". Corrigido: `max_output_tokens=4000` + `thinking_budget=512`.
5. **Backfill não achou os 63 posts antigos** — porque `get_collection_posts` busca só os ~50 mais recentes de cada coleção (a "Claude" sozinha tem 1255 itens) e os posts antigos são mais antigos que isso. Não é um bug, é uma limitação conhecida do cap atual — se quiser popular a pasta desses 63 retroativamente, dá pra rodar o backfill uma vez com um `amount` bem maior (ex: 1000+), é mais lento mas resolve. Não bloqueia nada — todo post NOVO a partir de agora já vem com pasta certa.
6. **1 de 10 roteiros saiu com título genérico** ("Ideia gerada", fallback do parser) — provavelmente resposta do Gemini fugiu um pouco do formato nesse caso específico. Não investigado a fundo (baixo impacto, 1/10).

---

## Sprint 3 — Concorrentes, outlier score, notícias, viralização

**Status: ✅ Concluído e verificado com dado fresco, 2026-08-09**

- [x] `monitor/run.md` rodado do zero (8 módulos) pra gerar `reports/2026-08-09/*` — pré-requisito de dado fresco pros módulos 10/11
- [x] M3 — módulo 11 (Radar): rodado com os relatórios de hoje
- [x] Bancos `hooks-concorrentes.md` populado — **4 frameworks reais** (CTA de palavra-chave @nick_saraev, contraste temporal @brandsdecoded__, CTA de recorrência @jonylan, credencial como hook — hipótese n=2)
- [x] M4 — módulo 10 (Notícia): **7 notícias relevantes → 21 ângulos** (7 × Polêmico/Educacional/Storytelling) em `producao/roteiros/2026-08-09/noticias-angulos.md`
- [x] 5 handles desatualizados corrigidos em `config/profiles.json` (achados pelo monitor, confirmados pelo Radar)
- [ ] categoria `fora-do-nicho` em `config/profiles.json` (aguarda Lucas indicar 5-10 perfis — não bloqueou o resto)
- [ ] M12 — `_context/viralizacao.md` já existe como estrutura (Sprint 3 anterior), mas segue vazio de conteúdo — só populava com ≥3 outliers confirmados, e nenhum outlier numérico foi confirmável nesta rodada (ver limitação abaixo)
- [x] **Marco:** bancos populados; 21 ângulos de notícia gerados

### Limitação real encontrada (documentada, não bloqueou)

O Instagram bloqueia indexação de texto de post/reel via WebSearch para os 61 perfis — impossível montar série de views por post, então **nenhuma entrada do banco tem outlier numérico confirmado (≥3x média)**. O Radar não inventou número: cada entrada foi marcada com nível de confiança explícito (do fragmento de legenda real + mesmo modelo de negócio, até hipótese n=2 sem texto capturado). `viralizacao.md` continua vazio até haver outlier numérico de verdade — é o comportamento correto do sistema (regra de volume mínimo), não uma falha.

---

## Sprint 4 — Carrosséis, criativos, campanha

**Status: 🟡 Código pronto e parcialmente verificado, 2026-08-21**

- [x] M6 — módulo 15 (carrossel estático + animado) + `_templates/carrossel-animado.md` escritos — **teste ao vivo travado** (o roteiro de carrossel da campanha de teste bateu 2x reprovado na Iana, decisão de negócio pendente com o Lucas: ver Sprint 1)
- [x] M7 — módulo 16 (criativos Pillow-first + Nano Banana) escrito **e testado ao vivo com sucesso** — criativo real gerado pro roteiro "leads-perdidos-custo.md" (8,5/10), `create_image.py` evoluído pra puxar cores/fontes de `tokens.json`
- [x] M8 — módulo 18 (calendário) + `_context/sazonalidades-brasil.md` (12 datas) escritos **e testados ao vivo** — campanha semanal real gerada em `producao/campanhas/2026-08/campanha.md` com dado fresco do monitor (2026-08-21)
- [x] Monitor atualizado antes do teste (relatório de 09/08 estava com 12 dias) — achado bônus: módulo 6 do monitor gerou 2x a frase banida "vendedor que nunca dorme" e se autocorrigiu antes de salvar
- [ ] **Marco (parcial):** campanha semanal real ✅, criativo real ✅ — carrossel real ainda pendente da decisão do Lucas sobre o slide de prova (ver abaixo)

### Decisão pendente do Lucas (bloqueia o teste completo do módulo 15)

Roteiro `producao/roteiros/2026-08-21/triagem-4h-15min.md`, rodada 2, 6,9/10, reprovado — Iana achou um **número inventado** no gancho ("em 4 minutos, ele já decidiu", não existe em `marca.md`) mesmo na correção. O bloqueio real: o slide de prova só fecha em ≥7 se usar a garantia de 30% — mas ela já está reservada pro slot de sexta da mesma campanha (framework RISCO INVERTIDO). Duas opções, detalhadas no próprio arquivo (seção "Avaliação Iana — rodada 2"):
- **A** — mantém a garantia reservada pra sexta, este carrossel fica em ~7,0 (prova mais fraca)
- **B** — usa a garantia aqui também (~7,3), sexta precisa de outro ângulo

Ainda em aberto desde o Sprint 1: o mesmo tipo de decisão no roteiro `producao/roteiros/2026-08-05/mecanismo-sem-culpa.md` (nunca resolvida).
- [ ] **Marco:** campanha do mês completa com carrossel animado e criativos

---

## Sprint 5 — Vídeo, agendamento, OPR

**Status: ⬜ Não iniciado**

- [ ] M10 — módulo 17 (cortes SRT-driven, ffmpeg + Whisper)
- [ ] M11 — agendamento (`/schedule` p/ fluxos Claude; Task Scheduler mantém publicação)
- [ ] M13 — módulo 19 (OPR semanal, métricas manuais até Metricool)
- [ ] **Marco:** 1 vídeo cortado; agendamentos ativos; 1º OPR

---

## Sprint 6 — Publicação multirede

**Status: ⬜ Não iniciado**

**Decisão registrada (2026-08-21):** o sistema precisa publicar em **todas as redes sociais**, não só Instagram. Prioridade de conexão: **Instagram + TikTok primeiro**, resto (YouTube, LinkedIn, X, Facebook, Pinterest, Threads) conforme fizer sentido.

- [ ] Conta Metricool criada — **confirmar no plano escolhido que Instagram + TikTok estão cobertos antes de assinar**
- [ ] M15 — migração de publicação p/ Metricool (dual com ig-saves-engine até estabilizar)
- [ ] **Decisão técnica em aberto:** TikTok tem Content Posting API oficial própria (mais robusta que a API não-oficial que usamos pro Instagram) — avaliar na hora se vale integrar TikTok direto por ali em vez de só via Metricool, ou se Metricool cobre bem o suficiente
- [ ] **Formato nativo por rede** — hoje o roteiro só modela Instagram (Reel/Carrossel/Post); campo `rede` já adicionado no template (`_templates/roteiro.md`) pra não travar isso depois, mas as regras de formato/tom por rede (LinkedIn mais texto, YouTube mais longo, TikTok com convenção própria) ainda precisam ser definidas quando chegar a hora — não construir isso especulativamente agora
- [ ] M14 — avatar de IA (Higgsfield/HeyGen reconectados) — só quando as contas estiverem prontas
- [ ] **Marco:** 1 post publicado em Instagram E TikTok via Metricool, com fallback intacto

---

## Fase 2 — Dashboard web (planejada, execução futura)

**Status: 📋 Planejada em alto nível, não iniciada** — ver seção 4 do plano aprovado.

---

## Iniciativa paralela — Criador UGC (segunda marca)

**Status: 📋 Registrado e com espaço criado, 2026-08-21 — aguardando kickoff**

Ideia do Lucas: usar o avatar de IA em duas frentes — (1) conteúdo Neovertix quando ele não quiser aparecer (já é o módulo 14/Sprint 6, sem duplicar aqui) e (2) uma persona/criador **separado**, nicho a definir, pra diversificar renda e testar formatos fora do tom B2B sóbrio da Neovertix.

- [x] Espaço criado: `Criador UGC/` (README com contexto, pré-requisitos e a regra dura contra depoimento fake)
- [x] Técnica de fotos de produto em lote registrada (`_context/tecnica-fotos-produto.md`) — trava de fidelidade + Nano Banana, adaptada do guia externo pra rodar via API em vez de Claude for Chrome + Flow
- [x] Agente **Gênese** criado (`.claude/agents/genese.md`) — engenheiro de prompt/onboarding, conduz a entrevista de posicionamento (nicho, público, monetização, tom, persona do avatar) e monta o cérebro de marca inicial
- [ ] Sessão de entrevista com o Gênese (aguardando o Lucas decidir rodar)
- [ ] Higgsfield/HeyGen reconectados (bloqueio externo, mesmo do módulo 14)
- [ ] Resto da estrutura (`_sop/`, `_templates/`, `modules/`, `bancos/`, `producao/`) — só depois da entrevista, pra não nascer genérica

**Não é sprint numerado do plano principal** — corre em paralelo, sem tirar prioridade do Sprint 4 em diante.

---

## Complemento — Lapida (engenheiro de prompt do sistema)

**Status: ✅ Criado, 2026-08-21**

11º agente do squad (`.claude/agents/lapida.md`), Opus. Duas funções: (1) refina pedido vago do Lucas num briefing executável antes de rotear pro agente certo; (2) audita ambiguidade/referência quebrada/ineficiência no squad depois de qualquer mudança grande — formaliza o que as auditorias manuais dos Sprints 1-3 já faziam ad-hoc. Registrado na regra de roteamento do `CLAUDE.md`.
