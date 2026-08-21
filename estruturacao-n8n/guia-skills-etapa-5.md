# Guia de Skills — Etapa 5 (Construção do Site)

Referência de consulta pra Claude Code durante a Etapa 5 do pipeline Estruturação (construção manual do site, no VS Code, com a skill `landing` como base técnica — HTML único autocontido, GSAP + CSS, sem build step). Não é uma skill nova, é um documento — ver justificativa no plano principal (`depois-vemos-isso-com-scalable-dolphin.md`, Fase 1.8): o projeto tem `skills-lock.json` rastreando hash de cada skill instalada, então uma skill orquestradora referenciando ~15 outras por nome quebraria silenciosamente a cada re-sync.

**Como usar:** ao construir um site (dry-run ou cliente real), percorrer os blocos abaixo na ordem, usando só as skills que preenchem um gap real da `landing` — ela já resolve sozinha boa parte do trabalho (ver seção "O que a `landing` já cobre" abaixo). Nunca duplicar o que ela já faz.

## O que a skill `landing` já cobre nativamente

- Intake de posicionamento (4 perguntas: produto/pitch, audiência, override de marca, tom)
- Copy estrutural rasa (headline, subtext, bullets, CTA — com fallback que infere se o input for pobre)
- Sistema de marca completo (paleta default navy+teal ou override, validação de contraste WCAG, escala tipográfica)
- Estrutura fixa de 3 seções: Hero → Features → Closing CTA
- Os 5 padrões de animação GSAP (timeline de entrada, parallax de mouse, ScrollTrigger.batch, floats CSS, bounce do scroll indicator)
- Responsividade básica (2 breakpoints: 900px, 580px)
- Validador técnico-estrutural próprio (`html_validator.py`)

## Bloco 0 — Intake & arquitetura de seções

- `landing` nativo cobre posicionamento/paleta/tom.
- `site-architecture` — mapeia as seções reais do cliente (ex: Home/Serviços/Galeria/Agendamento/Contato) em cima da estrutura fixa de 3 seções da `landing`. Resolve a pendência de estrutura de seções (ver nota do piloto).

## Bloco 0.5 — Benchmark dos 3 melhores concorrentes da região (OBRIGATÓRIO — decisão do Fundador, 2026-08-05)

Antes de escrever qualquer seção, analisar os **3 melhores concorrentes do mesmo nicho na mesma cidade/região** (os mais bem avaliados no Google que tenham site — achados via busca; se o nicho local não tiver 3 com site, completar com referências do nicho em cidades maiores):

- **O que eles têm de bom** → lista concreta de padrões a igualar ou superar (seções que convertem, agendamento online, cardápio/serviços com preço, prova social em destaque, fotos reais).
- **O que dá pra melhorar** → vira o diferencial do nosso site (velocidade, mobile quebrado, sem CTA claro, sem WhatsApp visível, SEO fraco, sem schema) — e alimenta a copy ("por que este site é melhor que o do concorrente").
- Registrar o resultado em 5-10 linhas no arquivo do cliente (`clientes/<slug>/benchmark.md`) — entra como insumo do `site-architecture` (Bloco 0) e da copy (Bloco 1).
- Skills de apoio: `competitive-teardown` (análise de um site concorrente) e `web-quality-audit` (nota rápida do site deles). Não gastar mais de ~20 min nisso — é insumo, não relatório.

## Bloco 0.6 — Análise do Instagram do lead (OBRIGATÓRIO — decisão do Fundador, 2026-08-08)

Pra negócio local, o Instagram é a porta do negócio: é de lá que saem público, serviços e identidade visual da prévia. **Nenhuma prévia se constrói sem esta análise** (fallback só se o lead não tiver perfil). Método (validado 2026-08-09, sem precisar de login): (1) WebFetch no perfil → bio, seguidores, destaques, contato; (2) Playwright local + screenshot (`scratchpad/ig-shot.mjs`) → análise visual do grid (identidade, estilo, temas). Chrome logado do Lucas via extensão = só aprofundamento opcional (comentários, stories, engajamento por post). Volume baixo: 1 perfil por vez, espaçado — uso assistido. ~10-15 min por lead. Extrair:

- **Identidade visual** → paleta e estilo da prévia: cores predominantes, estilo de foto (clean/rústico/premium), logo, energia da marca.
- **Serviços reais** → seções e copy: o que aparece nos posts/destaques (serviços, preços quando publicados, diferenciais que o próprio negócio enfatiza).
- **Público** → tom de voz da copy: quem comenta, como a marca responde, formalidade das legendas, faixa etária aparente.
- **Prova social viva** → antes/depois, resultados, clientes marcando — candidatos a destaque na prévia (conteúdo DELE, mostrado de volta pra ele).
- **O que já performa** → posts com mais engajamento revelam o que o público valoriza = hierarquia das seções.
- **Infos práticas** → horários, endereço, formas de agendamento (bio/destaques) — vão direto pro site e pro schema LocalBusiness.

Registrar em 5-10 linhas no `clientes/<slug>/instagram.md`, junto com o benchmark. Consentimento formal de imagem continua obrigatório antes da PUBLICAÇÃO (checklist Fase 6) — na prévia, usar o conteúdo público do próprio negócio é demonstração, não publicação.

## Bloco 1 — Copy profunda

- `copywriting`, `marketing-psychology` — aprofundam o que `landing` só faz de forma rasa.
- `landing-page-copy` — blocos que `landing` não pede nativamente (problema, mecanismo).
- `brand-guidelines` / `brandkit` — só se o cliente já tiver marca definida ou quiser fugir do default.

## Bloco 2 — CRO avançado

- `page-cro` / `cro` — prova social, urgência, pricing, FAQ (maior gap real da `landing`, que não tem nenhum desses blocos).
- `form-cro` — a seção de Agendamento é um formulário; otimizar fricção.
- Reaproveitar `quebra-objecoes-estruturacao.md` (já pronto) como base de FAQ — não regerar objeções do zero.

## Bloco 2.5 — Referências de excelência do nicho (OBRIGATÓRIO — decisão do Fundador, 2026-08-09)

O Bloco 0.5 (concorrentes locais) define o **piso** — eles têm site fraco, é por isso que são leads. Este bloco define o **teto**: buscar 2-3 exemplos de excelência real no MESMO NICHO, **sem limite de região** (agências/estúdios premiados, Awwwards, sites de referência do setor em qualquer país) — o que "muito bom" parece de verdade, não só "melhor que o vizinho".

- Se o Fundador já indicou 2-3 links de referência (qualquer nicho) pra calibrar gosto geral, aplicar esse padrão de qualidade (tipografia, espaçamento, hierarquia visual, fotografia) em cima do conteúdo específico do nicho.
- Registrar 3-5 bullets do que copiar de padrão (não de conteúdo): densidade de texto, tratamento de fotografia, uso de espaço em branco, hierarquia de CTA.
- ~10 min — é calibração de olho, não pesquisa extensa.

## Bloco 3 — Design/visual

Escolher **UMA**, nunca empilhar mais de uma:
- `design-taste-frontend`
- `minimalist-ui`
- `high-end-visual-design`
- `industrial-brutalist-ui`

**Passe de polimento obrigatório (decisão do Fundador, 2026-08-09)** — depois de aplicar a skill de design escolhida, rodar `make-interfaces-feel-better`: ritmo de espaçamento, escala tipográfica, refinamento de sombra/borda, timing de microinteração, área de toque, quebra de texto, estados de interação. É o que separa "bom" de "premium" — nunca pular.

**Curadoria de fotos (não despejo)**: do material do Bloco 0.6 (Instagram), escolher as 5-8 MELHORES fotos (composição, luz, foco) — nunca usar tudo que existe. Foto fraca derruba o teto de qualidade do site inteiro, não importa o quão bom o código seja. Cortar/tratar se precisar (`image-enhancer`).

Mais:
- `image-to-code` / `imagegen-frontend-web` — se houver referência visual do cliente (comum no Caminho B, que já tem site/identidade a preservar).
- MCP `21st` — componentes premium prontos (galeria, depoimentos, pricing). **Free tier limitado a 2 buscas/dia** — reservar pra Galeria/Serviços. Builder ($8/mês) se precisar de mais.
- MCP `shadcn` — componentes de registry; como `landing` não usa framework, adaptar JSX pra HTML/CSS/JS vanilla na hora de aplicar.
- **Fora de escopo (decisão 2026-08-09)**: mundos 3D/scroll cinematográfico (Three.js, `build-threejs-scroll-worlds`, `scroll-world-storytelling`) — carga pesada é o oposto de premium pra público mobile-first de negócio local; a meta de performance do Bloco 8 (90+ Lighthouse) e a meta de conversão andam junto com velocidade, não com espetáculo técnico.

## Bloco 4 — Animação (auditoria, não implementação)

- `animation-vocabulary`, `find-animation-opportunities`, `review-animations`, `improve-animations` — auditam o GSAP que `landing` já gera, não reimplementam.
- `emil-design-eng` — referência de filosofia (easing, transform-origin, feel) por trás do critério que `review-animations` usa.
- **Fora de escopo**: skills de animação genéricas (gsap-scrolltrigger, motion-*, three*, lottie etc.) — reimplementariam o que `landing` já faz. `apple-design` (motion de gesto/spring) também fica de fora — não se aplica a uma landing estática sem gestos/sheets.
- **Bug real encontrado no dry-run (`dry-run-etapa5/oficina-do-ze.html`)**: o padrão de entrada da hero (`gsap.set([".btn-primary", ...])`) usa seletor sem escopo — se a seção de Closing CTA reusa a mesma classe `.btn-primary` (como o Bloco 3 do próprio guia recomenda), o `gsap.set()` inicial esconde os dois botões, mas a timeline de revelação só anima o `.hero .btn-primary` de volta pra opacidade 1, deixando o botão da seção final permanentemente invisível. Testado com Playwright (screenshot em mobile/tablet/desktop) e só apareceu no render real, não na leitura do código. **Correção**: escopar tanto o `gsap.set()` inicial quanto o `.to()` de revelação com `.hero` (`.hero .eyebrow`, `.hero .btn-primary` etc.) — nunca selecionar `.btn-primary` sem escopo quando a página tem mais de um botão com essa classe. Checar isso em toda página gerada, não só nesta. **Corrigido na fonte (2026-08-08)**: skill `landing` v1.1.0 (patch local) já gera os seletores escopados, e o `html_validator.py` agora FALHA quando um `gsap.set()` esconde elementos que nunca revela pelo mesmo seletor (regra `gsap-selector-scope`, testada contra repro sintético do bug). O check visual do Bloco 8 permanece como cinto de segurança.

## Bloco 5 — Responsividade & acessibilidade

- `a11y-audit` — checklist WCAG real (`landing` só valida contraste de paleta, não cobre alt-text, foco, landmarks, `prefers-reduced-motion`).
- MCP `chrome-devtools` — `resize_page`/`emulate` além dos 2 breakpoints fixos da `landing`; teste em dispositivos reais.

## Bloco 6 — SEO + AEO/GEO

- `seo-audit`, `local-seo` (cobre também Google Meu Negócio — GBP, NAP, citações locais), `schema-markup` (LocalBusiness/Service) — sempre, pro nicho local.
- `ai-seo`, `aeo` — llms.txt, estrutura de conteúdo citável, sinais E-E-A-T. O Portfólio v3.0 promete "SEO + AEO + GEO" em todos os planos — não excluir.
- **Fora de escopo**: `programmatic-seo`, `entity-seo`, `parasite-seo` — jogadas de escala/portfólio, não de 1 site institucional.

## Bloco 6.5 — Segurança básica

Superfície de ataque é pequena (HTML estático, sem backend), mas checar:
- Nenhum segredo/API key no JS client-side
- Formulário de Agendamento com honeypot/validação anti-spam básica
- SSL forçado (responsabilidade do host — Vercel/Hostinger já fazem por padrão, só confirmar)
- Headers de segurança mínimos (CSP/X-Frame-Options) via `vercel.json` ou `.htaccess`, conforme o host
- **SRI (Subresource Integrity) nos scripts CDN da skill `landing`** (`gsap.min.js`/`ScrollTrigger.min.js`) — gap real encontrado no dry-run (`dry-run-etapa5/oficina-do-ze.html`): o template da skill não incluía `integrity`/`crossorigin` por padrão. **Corrigido na fonte (2026-08-08)**: skill `landing` v1.1.0 (patch local) traz os hashes sha384 fixados pra GSAP 3.12.2, calculados a partir dos arquivos reais baixados do cdnjs, e o `html_validator.py` FALHA em script CDN sem SRI (regra `cdn-sri`). Se subir a versão do GSAP, recalcular os hashes do arquivo baixado (`openssl dgst -sha384 -binary | openssl base64 -A`) — nunca inventar/copiar de terceiro.

Skill de apoio: `security-review`, pra revisar o HTML/JS gerado antes do deploy. É um checklist curto, não uma etapa pesada.

## Bloco 7 — Deploy

- `redesign-existing-projects` — só no Caminho B, pra auditar o site atual antes de reconstruir em cima.
- **Fora de escopo**: `vercel-react-best-practices` — é sobre performance React/Next.js; `landing` gera HTML puro sem framework, não se aplica.

## Bloco 8 — QA final (GATE OBRIGATÓRIO — nenhuma prévia vai pro cliente sem passar aqui)

Decisão do Fundador (2026-08-05): os Blocos 0.5, 5, 6 e 8 são **gates**, não consulta opcional. Antes de enviar qualquer staging ao cliente, três camadas — rodar nesta ordem (a automática é grátis, roda primeiro e corta retrabalho das outras duas):

**① Automático — `html_validator.py` (regex, sem custo, roda a cada geração)**

- [ ] `python .agents/skills/landing/scripts/html_validator.py --file <path>` retorna `PASS` (0 FAIL) — se der FAIL, regenerar a seção apontada antes de seguir pras camadas ② e ③
- Cobre sozinho: 3 seções presentes, CDNs + SRI, `gsap.set()` antes de qualquer `.to()` (FOUC), **escopo do bug de botão invisível** (`.hero .btn-primary` etc. — antes exigia render real pra achar, agora é FAIL de build), breakpoints 900px/580px, `lang`, meta description, OG, `prefers-reduced-motion`, semântica de CTA

**② Semi-automático — ferramenta roda, humano julga o resultado**

- [ ] Responsividade em 3 tamanhos reais (mobile/tablet/desktop — Playwright ou chrome-devtools `resize_page`) — pega quebras visuais que regex não vê
- [ ] `lighthouse_audit` (MCP `chrome-devtools`): performance/a11y/SEO/best practices — meta 90+ em performance e SEO
- [ ] `full-page-screenshot` — o mesmo screenshot já exigido pelo Checkpoint 2 (conecta com `05-checkpoint-2-staging.json`)

**③ Manual — julgamento humano puro, sem ferramenta**

- [ ] Critérios de fundação SEO/AEO/GEO do Bloco 6 aplicados de fato ao conteúdo (schema LocalBusiness com dados reais, sitemap, headers) — o validador só confirma que os campos existem, não que o conteúdo é bom
- [ ] Benchmark do Bloco 0.5 respondido: "o que este site tem que os 3 concorrentes não têm?" — se a resposta for vaga, voltar pra copy

## Bloco 9 — Analytics

- `analytics-tracking` — injetado antes do deploy, pra alimentar `10-monitoramento-pos-entrega.json`.
- **Fora de escopo**: `ab-testing` — só faz sentido com portfólio/tráfego acumulado, não pra 1 site novo.

---

## Skills não instaladas (não citar como se existissem)

Confirmadas ausentes em qualquer camada (`.agents/skills`, `.claude/skills` do projeto, `~/.claude/skills` global): `web-interface-guidelines` (usar `web-design-guidelines` no lugar), `landing-report`, `conversion-path-builder`, `brand-voice`, `headline-matrix`, `schwartz-awareness-mapper` (as duas últimas cobertas por `copywriting` + `marketing-psychology` + `hormozi-hooks`).

## Nota sobre as 3 camadas de skills

O projeto resolve skills em 3 lugares: `.agents/skills/` (projeto), `.claude/skills/` (projeto, mais completo) e `~/.claude/skills/` (usuário, global). Uma skill "ausente" em `.agents/skills` pode existir nas outras duas — na prática, todas as skills citadas neste guia são referenciáveis pelo nome normalmente.
