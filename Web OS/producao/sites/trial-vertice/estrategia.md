# Estratégia Web — trial-vertice (slug provisório)

> **Status: projeto real, destinado a ir ao ar.** Substitui e descarta `Web OS/producao/sites/teste-piloto-vertice/` por decisão do Lucas ("o criado não ficou bom, pode desconsiderar") — **nada daquele projeto é reaproveitado**, nem copy, nem specs, nem design.
> Agente: Tese-ext · Módulo: `Web OS/modules/20-business-discovery-estrategia.md` · Data: 2026-10-12 (revisado 3x no mesmo dia — ver §8) · atualizado em 2026-11-02 (planos pós-trial, decisão 13 reverte a 12; duração do trial 5 → 7 dias, decisão 15)
>
> **Escopo — ler antes de qualquer decisão a jusante.** Este é um produto **novo e independente** da Neovertix (decisão do Lucas, 2026-10-12, 3ª rodada): *"nosso nome da empresa é o mesmo, mas nesse momento são produtos diferentes."* A linha **Vértice** (Piloto / Operação / Full, em `config/business.json`) é a linha de implementação sob medida; o **Web OS** é a linha de criação automática de sites e landing pages — e é a ferramenta que está construindo **esta** página. Este produto (agente de IA + CRM + redes sociais, via Bolten) é uma **terceira linha**: não substitui nenhuma oferta, não se funde, não herda a Garantia Vértice. Agregar à linha Vértice no futuro é decisão do Lucas, não deste brief.
>
> Fontes: entrevista com o Lucas (2026-10-12) · `branding/neovertix/01-estrategia.md` e `02-oferta.md` (marca, voz, léxico, âncoras de custo — a **empresa** é a mesma) · `Web OS/_context/identidade-web-os.md` (princípios e veracidade do sistema) · `config/business.json` (contexto de preço/padrão comercial). **`Web OS/_context/icp-web.md` NÃO é fonte obrigatória aqui** — aquele arquivo mapeia oferta→página **da linha Vértice** (ver §3).
>
> ⚠️ **O slug `trial-vertice` é provisório.** Nome e slug definitivos são pendência nº 2. Decidir **antes** do módulo 22 (build/deploy) — renomear depois arrasta `memory.md`, `specs/`, URLs e tracking. **E atenção:** o nome **não precisa carregar "vértice"**, porque este produto não pertence à linha Vértice — o `-vertice` no slug atual é resíduo do provisório, não decisão de marca.

---

## 1. Objetivo de negócio

**Venda direta no sentido de ativação direta do trial.** A página não gera lead pra reunião, não agenda demo, não pede contato comercial.

**CTA primário único:** começar o teste grátis (conectar o canal). Repetido ao longo da página, sem CTA secundário competindo.

Consequência direta: a conversão da página **termina na ativação técnica**, não num formulário. Isso é diferente de tudo que o Web OS já briefou — o gargalo não é o clique, é a conexão do canal (ver §4 e métrica em §7).

Por que não é demo agendada (modelo que a linha Vértice usa): aqui a prova não é o Lucas mostrando o agente com dados do prospect — é **o próprio agente atendendo os leads reais do prospect**. É o pilar 3 da marca — "você não paga pra descobrir se funciona" (`01-estrategia.md` §5) — levado ao limite: não paga nada e não fala com vendedor.

---

## 2. Oferta específica

**Produto novo e independente da Neovertix.** Não é oferta de entrada da linha Vértice, não substitui a Piloto Vértice, não entra em `config/business.json` por ora. Registrar (ou não) no `business.json` é decisão futura do Lucas — faz sentido se/quando ele decidir agregar este produto à linha Vértice. **Até então, a fonte de verdade desta oferta é este arquivo.** Fonte dos dados: entrevista com o Lucas em 2026-10-12.

| Campo | Valor (fonte: entrevista Lucas 2026-10-12) |
|---|---|
| Formato | Teste grátis self-service: **sem reunião, sem agendamento, sem compromisso** |
| Duração | **7 dias** (fechado — revisto de 5 para 7 em 2026-11-02, decisão 15) |
| Natureza do ambiente | **Módulo/instância própria**, criada para aquele cliente — não sandbox genérico com dados fictícios |
| Ativação | O cliente **conecta o canal real dele**: nº de WhatsApp e/ou Instagram e/ou CRM. **Quem configura é o próprio cliente** (self-service de verdade), com o **agente de IA da Neovertix dando suporte durante a configuração** + material de ativação (documentação/tutorial) que o Lucas vai construir |
| O que roda no trial | O agente de IA atende os **leads reais** do cliente durante o período |
| Fim do trial | **Simplesmente acaba.** Sem cobrança automática, sem renovação, sem letra miúda. O cliente vê o resultado e decide depois |
| Se não comprar | A instância é **simplesmente descartada** — sem acesso residual, sem dado guardado além do período de teste |
| Infraestrutura | Plataforma **Bolten** (parceria nova) — CRM white-label com agente de IA treinável, WhatsApp via QR Code ou Cloud API oficial, Meta/Instagram via Conversions API |

### Enquadramento de venda (decisão explícita do Lucas)

> "Em vez de vender como CRM, vender como agente de IA — o CRM vai de brinde."

Regra para toda a página e para todos os módulos a jusante: **o herói da oferta é o agente de IA.** O CRM é consequência, nunca a manchete. Coerente com `02-oferta.md` §1 (value stack): o agente é o mecanismo central, o CRM existe para "atendimento rápido virar dado que se usa depois".

⚠️ **Correção de léxico (Tese):** "de brinde" é linguagem de venda de impulso e contraria o atributo de voz "sóbrio, não gritado" (`01-estrategia.md` §6). Na copy, usar **"o CRM vem incluído"** / **"vem junto"**. "Brinde" fica no vocabulário interno de posicionamento, não na página.

### Planos pós-trial (fonte: Lucas, direta — atualizado em 2026-11-01, substitui a estrutura de 2026-10-12)

| Plano | Entrada (setup único) | Recorrência | Escopo |
|---|---|---|---|
| **Plano Essencial** | **R$ 2.500** | **R$ 500/mês** | Agente de IA + CRM incluído (sem redes sociais) |
| **Plano Escala** | **R$ 3.200** | **R$ 700/mês** | Tudo do Plano Essencial + Gestão de Redes Sociais (Instagram) |

A entrada continua sendo cobrança à parte, única (decisão 13, §8: valores e nomes do briefing do Lucas; a decisão 12 foi revertida, sem teto de atendimentos).

**Escopo confirmado (Lucas, 2026-11-02):** "Gestão de Redes Sociais (Instagram)" no Plano Escala é **serviço de gestão** (conteúdo/postagem), não apenas o agente respondendo DM do Instagram — ambiguidade levantada pela Tese, resolvida direto com o Lucas antes de liberar pro Convence (módulo 26).

Mesmo padrão setup + mensalidade que a Neovertix já pratica na linha Vértice (`02-oferta.md` §3: setup ancora a construção, mensalidade ancora manutenção e iteração) — coerência de empresa, não pertencimento à linha. **Preço liberado pra publicação na página.**

**Item futuro (não é decisão, não bloqueia nada):** o Lucas vai avaliar depois um possível acréscimo/upsell pra quem já é cliente. Sem definição — não aparece na página.

### Funcionalidades reais da plataforma (fonte: screenshots do dashboard Bolten, Lucas, 2026-11-03)

**Isto é inventário de funcionalidade REAL e verificado** — os 5 módulos abaixo são o que a plataforma Bolten de fato entrega, transcritos dos 5 screenshots do dashboard que o Lucas enviou em 2026-11-03. Diferente de alegação de marketing, é fato operacional (mesma natureza da linha "Infraestrutura" na tabela do §2, não uma decisão numerada do Lucas). **Pode ser usado na copy sem violar a regra de veracidade do `tom-de-voz.md`** — desde que respeitadas as "Regras de veracidade específicas desta página" logo abaixo (white-label: marca Neovertix na frente; nunca atribuir trial à plataforma).

Abas do dashboard (cabeçalho comum aos 5): **CRM de Vendas · Agente de Atendimento IA · Conversões · Redes Sociais · Central de Atendimento.**

| Módulo | Descrição (transcrita) | Funcionalidades reais (checklist transcrito) |
|---|---|---|
| **CRM de Vendas** | "Gerencie leads, acompanhe negociações e maximize suas conversões." | Gestão de Leads e Contatos · Funil Kanban Personalizável · Integração com WhatsApp · Conversão Meta Ads · Tarefas e Responsáveis · Relatórios · Preenchimento automático com IA · Webhooks e API |
| **Agente de Atendimento IA** | "Comunicação multicanal eficiente feito com Agente de IA para respostas rápidas e personalizadas." | Conectado direto ao WhatsApp · Base de conhecimento personalizada · Escalonamento humano · Possibilidade para intervenção humana · Transcrição e entendimento de áudios · Responsáveis e fila de atendimento |
| **Conversões** | "Rastreie seus leads e automatize seu funil de vendas." | Rastreio de origem dos leads · Atualização em tempo real · Integração com o CRM · Conversão com o Meta ADS · Relatórios · Análise em recortes de tempos · Atualize o CRM automaticamente |
| **Redes Sociais** | "Economize horas de trabalho com fluxos de aprovação ágeis e relatórios automáticos." | Agendamento de Posts e Stories · Fluxos de aprovação com cliente · Relatórios completos do perfil · Analytics de publicações · Multicontas em um único acesso |
| **Central de Atendimento** | "Organize o atendimento ao cliente com gestão de tickets, Whatsapp e Agente de IA." | Gerencie tickets · Tarefas e Responsáveis · Integração com WhatsApp · Agente de atendimento IA · Escalonamento humano · Histórico de interação |

**Resolve a lacuna da aba "Redes Sociais" do protótipo.** No protótipo HTML anterior, a aba "Redes Sociais" foi **removida** porque continha alegação falsa (que o agente responde DM do Instagram — o Lucas confirmou que não é verdade). Agora há conteúdo real e honesto para essa aba: **agendamento de posts e stories, fluxo de aprovação com o cliente, relatórios completos e analytics do perfil, multicontas em um único acesso.** A aba pode voltar na copy **com esse escopo** — o de uma ferramenta de gestão/publicação de conteúdo. **Não é automação de DM.** Isso casa com o "Escopo confirmado (Lucas, 2026-11-02)" acima, que já definiu "Gestão de Redes Sociais (Instagram)" como serviço de gestão (conteúdo/postagem), não o agente respondendo DM.

**"Central de Atendimento" é módulo novo — não aparecia no brief nem no protótipo.** Registrado aqui como **funcionalidade real existente** da plataforma (gestão de tickets + WhatsApp + agente de IA, com escalonamento humano e histórico). **PONTO EM ABERTO (não decidido):** a qual plano este módulo pertence (Essencial? Escala? ambos?) e se é diferencial do Escala **não está definido** — os screenshots mostram que a funcionalidade existe, não a qual pacote comercial ela é atribuída. Não assumir. Pendência pro Lucas esclarecer antes de a copy vincular "Central de Atendimento" a um plano específico.

**Limites do uso desta tabela na copy:** (1) continua valendo "white-label = marca Neovertix na frente" — a página não cita Bolten como fornecedor; (2) descrever funcionalidade ≠ prometer resultado/número — nada aqui gera métrica medida (ver §7, números proibidos); (3) nenhum destes itens muda preço, nome de plano, duração do trial ou ICP já fechados no §8; (4) qualquer alegação de segurança/LGPD derivada destes módulos ainda passa pelo Blinda (módulos 37–38).

### Regras de veracidade específicas desta página (`identidade-web-os.md`)

- **Sobre a Bolten:** a documentação da Bolten **não menciona trial nativo**. O período grátis é decisão comercial da Neovertix por cima da ferramenta. A página **nunca** pode sugerir que o trial é recurso da plataforma, nem afirmar qualquer capacidade da Bolten além de: CRM white-label, agente de IA treinável, WhatsApp (QR Code ou Cloud API oficial), Meta/Instagram (Conversions API).
- **White-label significa marca Neovertix na frente.** A página não precisa (nem deve, sem decisão do Lucas) citar a Bolten como fornecedor.
- **Um mecanismo de prova por página — a Garantia Vértice não entra aqui.** A garantia de ≥30% ou devolução total (`02-oferta.md` §2) é o mecanismo de reversão de risco **da linha Vértice**, que é paga. Este produto nunca a teve e não a herda: num trial grátis, "devolução total" não significa nada, e o próprio trial já é a reversão de risco. Os dois mecanismos **coexistem na empresa** sem problema (produtos distintos podem ser anunciados em paralelo), mas **nunca na mesma página** — juntos, confundem. Nada em `02-oferta.md` muda por causa deste brief.

---

## 3. ICP

**ICP próprio deste produto, definido pelo Lucas** (2026-10-12). `Web OS/_context/icp-web.md` mapeia oferta→página **da linha Vértice** e **não** é fonte aqui — este produto tem ICP próprio e nada do que segue vai pra `icp-web.md`.

⚠️ **Definido ≠ validado.** O alvo abaixo é decisão do dono do negócio, não resultado de campanha: **nenhuma conversão real testou esse recorte ainda**. Tratar como alvo de trabalho, não como ICP comprovado (pendência nº 11b — validação em campanha).

**Primário — comércio local e pequenas empresas em geral**, "tudo que tiver essa possibilidade de venda" (palavras do Lucas). Verticais citadas explicitamente:

| Vertical | Por que entra |
|---|---|
| Clínicas | Volume de agendamento por WhatsApp, lead perecível |
| Concessionárias | Lead de alto ticket, resposta rápida decide a visita |
| Imobiliárias | Lead chega por anúncio a qualquer hora |
| Advocacia | Primeiro contato por WhatsApp, triagem de caso |
| Comércio local (amplo) | Qualquer negócio com venda por mensagem |

Perfil comum: **decisor único** — assina e conecta sozinho, sem comitê. **É ele quem tem a senha/o celular do WhatsApp da empresa** — fato operacional que importa muito aqui, porque a ativação depende disso.

**Recorte mais amplo que o da linha Vértice** (`01-estrategia.md` §3: serviços, e-commerce, clínicas, imobiliárias, educação): este produto inclui explicitamente **concessionárias e advocacia**, e lidera com "comércio local" em vez de "PME 5–50 funcionários". Mais uma razão para não forçar os dois ICPs no mesmo arquivo.

**Hipótese criador/infoprodutor — descartada pelo Lucas.** Eu havia levantado que o Plano Escala (com Instagram) teria afinidade com criador/infoprodutor; o alvo definido é PME/comércio local. **Não construir a página para criador.**

**Fora do ICP desta página:** quem não tem volume de lead (não tem o que o agente atender) e quem não pode/não quer conectar o canal oficial da empresa (a oferta não funciona sem isso — não tentar convencer esse perfil na copy, é desperdício de página).

**Canal de aquisição (nota de distribuição, não é ICP — insumo pro Multiplica/módulo 27):** começa pelas **postagens do Instagram do Lucas**, com possível migração pro **TikTok** depois. Consequência prática pra esta página: o tráfego da V1 é **morno e founder-led** (gente que já viu o Lucas falar), não frio de busca — a página pode contar com algum reconhecimento prévio, mas não pode depender dele.

### Objeções que a página é obrigada a responder

Herdadas do público já mapeado pela Neovertix (`01-estrategia.md` §3 + `02-oferta.md` §5) — válidas aqui porque a dor de origem é a mesma:
1. **"IA soa robótica"** → no trial não é demo: é o seu lead real conversando. Você lê as conversas que o agente resolveu.
2. **"Agência nova, sem case"** → o trial é a prova. Você não paga pra descobrir — nem com cartão, nem com reunião.
3. **"Quanto tempo até funcionar"** → prazo fechado de 7 dias.
4. **"Se quebrar, quem conserta"** → quem escreve o código é quem responde (Cara Comum, `01-estrategia.md` §4).

**Novas, criadas pelo próprio mecanismo desta oferta** (derivadas do fato "ativação exige conectar WhatsApp/Instagram/CRM", não inventadas):

5. **"Vou conectar o WhatsApp da minha empresa numa empresa que eu não conheço?"** — esta é, na leitura da Tese, **a objeção nº 1 desta página**, acima de preço. **Resposta factual (decidida pelo Lucas, 2026-10-12):** cada cliente recebe uma **instância própria**, criada só pra ele, com acesso durante os 7 dias. **Se não der continuidade, a instância é descartada** — sem acesso residual, sem dado guardado além do período de teste. Nada é compartilhado com outro cliente, porque o ambiente não é compartilhado.
   **Como escrever isso na página:** afirmar exatamente o que está acima, sem esticar. **Não** prometer "seus dados são 100% seguros", conformidade LGPD, criptografia, certificação ou retenção em prazo específico — nada disso foi declarado. Alegação de segurança além deste parágrafo precisa passar pelo Blinda (módulos 37–38).
6. **"Acaba e vocês me cobram?"** → não. Acaba e pronto: sem cobrança automática, sem renovação. Usar a formulação da fonte da marca: **"sem letra miúda"** (`02-oferta.md` §2), não "sem pegadinha".
7. **"Quanto trabalho eu tenho pra ligar isso?"** → **quem configura é o próprio cliente** — self-service de verdade, o Lucas não faz por ele. Mas o cliente **não fica sozinho**: o **agente de IA da Neovertix dá suporte durante a configuração** (pode ser acionado pra qualquer dúvida), e vai existir material de ativação (documentação/tutorial) construído pra essa fase não travar. A página tem que ser honesta sobre a etapa técnica existir — fingir fricção zero queima a confiança na primeira tela de QR Code e contraria o atributo "honesto sobre onde estamos" (`01-estrategia.md` §6).
   **Ângulo de copy que a Tese recomenda:** o próprio suporte à configuração é prova do produto — *o agente que vai atender seu cliente é o mesmo que te ajuda a ligar ele*. Mágico + Cara Comum numa frase, sem promessa nova. **Não** prometer tempo ("pronto em X minutos"): não existe número medido (pendência nº 7, parte residual).

---

## 4. Problema comercial central

> Skill aplicada: `problem-framing-canvas` (3 fases) — single-shot sobre contexto existente, **sem pesquisa de mercado nova** (isso é do Radar, módulo 28).

**Look Inward (nosso lado).** A Neovertix hoje só tem porta de entrada que passa pela agenda do Lucas: demo ao vivo, conversa 1:1, indicação. Isso trava a aquisição no gargalo de um founder solo. A oferta nova resolve isso estruturalmente — o trial vende sozinho enquanto o Lucas constrói. Risco de viés a derrubar: supor que tirar o Lucas da venda é só ganho. Tirar o Lucas da venda **também tira o arquétipo Cara Comum e a profundidade técnica demonstrada ao vivo**, que são dois dos três espaços vagos que a marca ocupa contra a concorrência (`01-estrategia.md` §8). Se a página virar um SaaS self-service anônimo, a Neovertix perde o diferencial do próprio posicionamento Moore ("o fundador escrevendo o código — não um departamento comercial entre você e a solução"). **Consequência obrigatória: o Lucas tem que estar visível na página como pessoa e como autor do sistema, mesmo sem aparecer na venda.**

**Look Outward (lado do prospect).** Quem sente a dor: o dono, pessoalmente, vendo mensagem não respondida às 22h. Quando aparece: pico de lead e fora do horário comercial. Consequência: o lead compra de quem respondeu primeiro. Quem não tem o problema: quem já paga equipe de plantão, ou quem não gera lead. Quem é o mais cético e o mais qualificado ao mesmo tempo: o dono que já tentou chatbot de árvore de decisão e saiu queimado.

**O que é diferente aqui.** Num produto pago e assistido (como a linha Vértice), o custo de errar a escolha é **dinheiro + tempo de implantação**. Num trial grátis, sem cartão e sem reunião, esse custo foi a zero. **Mas o custo percebido não foi a zero — ele mudou de natureza.**

**Reframe — problema comercial central desta página:**

> O risco financeiro da decisão foi eliminado, mas sobraram dois custos que a página tem que derrubar: **o risco de confiança** (entregar o canal de vendas vivo da empresa — WhatsApp/Instagram — pra uma marca nova, sem case) e **o esforço de ativação** (conectar, configurar, ver funcionando). Hoje, pro dono de PME, esses dois custos juntos ainda parecem maiores que o custo silencioso de continuar perdendo lead por demora.

**How Might We:** como fazer a conexão do canal parecer **pequena, reversível e segura** — ao ponto de o dono preferir conectar hoje a continuar perdendo lead — sem mentir sobre a fricção técnica que existe?

**Consequências diretas pra arquitetura da página** (entregar pro Guia/módulo 25 e pro Convence/módulo 26):
- A página **não vende IA**. Vende um teste de 7 dias que acaba sozinho.
- **Prova > promessa** (`identidade-web-os.md`): o ativo de prova mais forte disponível é o **log de conversas reais** que o agente resolveu durante o trial — mostrar o formato do que o cliente vai ver, não um dashboard bonito.
- **Reversibilidade é bloco de página, não rodapé.** Agora com conteúdo factual (§3, objeção 5): instância própria, acaba em 7 dias, descartada se não comprar. Mesmo peso visual do CTA.
- A fricção de ativação é um **funil dentro da página** (3 passos nomeados), não um botão mágico — e o suporte do agente de IA durante a configuração entra como parte do passo, não como rodapé de FAQ.

---

## 5. Por que contratariam isso (JTBD)

> Skill aplicada: `jobs-to-be-done` (Christensen + Value Proposition Canvas), destilado do avatar de `02-oferta.md` §1. Sem persona, citação ou demografia inventada.

**Job funcional:** responder todo lead que entra, em segundos, qualificar e registrar num lugar só — sem contratar mais ninguém.

**Job social:** parecer uma empresa organizada e responsiva pro cliente dele. Não parecer "aquele negócio pequeno que nunca responde".

**Job emocional:** parar de carregar o WhatsApp da empresa como ansiedade pessoal.

**Job específico deste produto (o que o trial contrata e um serviço assistido não contrata):** *"deixar de apostar."* O dono não quer avaliar um fornecedor — ele quer **ver com os olhos dele, nos leads dele, antes de assumir qualquer compromisso**, e sem gastar uma hora numa reunião de vendas pra isso. O trial não compete com outra IA; compete com **procrastinar a decisão**.

**Dores, ordenadas:**
1. Lead esfriando enquanto ninguém responde — perda de receita direta.
2. Contratar é caro e lento — âncora da própria oferta: SDR CLT júnior ~R$ 2.200 de salário + ~80% de encargos = **~R$ 3.800–4.200/mês**, só em horário comercial, com turnover (`02-oferta.md` §3). *Usar como cálculo que o prospect faz sozinho, nunca como slogan de comparação — e jamais na forma banida "vale por N humanos".*
3. Medo de o cliente dele ouvir um robô ruim e piorar a percepção da marca dele.
4. Já viu fornecedor prometer e não entregar.
5. **Nova, específica do trial:** medo de dar acesso ao canal de vendas da empresa.

**Ganhos que fazem ele trocar o status quo:**
- Ver o agente atendendo **leads reais dele**, não um sandbox de demonstração.
- Zero compromisso: acaba sozinho, sem cobrança, sem precisar cancelar nada.
- Nenhuma reunião pra marcar, nenhum vendedor pra despachar.
- O CRM vem junto, sem ser a coisa que ele precisa aprender a usar pra ter valor.

**O que ele "contrata" hoje no lugar:** ele mesmo e a equipe respondendo no intervalo do almoço, chatbot de árvore de decisão, ou nada.

---

## 6. Diferencial e posicionamento da página

> Skill aplicada: `positioning-workshop` → formato Geoffrey Moore, derivado do posicionamento-mãe (`01-estrategia.md` §2) e especializado pra esta página.

**Para** donos de comércio local e pequenas empresas brasileiras com volume de lead no WhatsApp e no Instagram
**que precisam** parar de perder venda por demora de resposta sem contratar mais gente,
**[nome pendente — ver pendência nº 2]**
**é um** teste grátis de 7 dias em que o agente de IA da Neovertix é configurado no canal real do negócio
**que** atende, qualifica e registra os leads de verdade durante o período — e no fim **simplesmente acaba**, sem cobrança e sem compromisso: o dono vê as conversas que o agente resolveu e decide depois.

**Diferenciação:**
**Diferente de** agências de marketing com IA e consultorias de IA genéricas, que vendem no slide e cobram antes de mostrar,
**esta oferta**
**entrega** o mecanismo rodando nos leads reais do cliente **antes de qualquer pagamento e sem uma única reunião** — configurado e suportado pela mesma pessoa que escreve o código.

✅ **Contra-ângulo validado pelo Radar (módulo 28, pendência nº 5 — resolvida em 2026-11-03):** a hipótese original ("painel vazio pro cliente configurar sozinho") **não se confirmou como estava formulada** — nenhum concorrente analisado se anuncia como "você se vira sozinho". O dado real é diferente e mais forte:

- **3 dos 5 concorrentes BR de "agente de IA" analisados (Bluelephant, Intelecta, MelhorAgência.ai) nem oferecem trial self-service** — todos exigem reunião/diagnóstico com vendas antes de qualquer acesso ao produto. É o oposto do "painel vazio": é **nenhum painel até passar por um vendedor**.
- Os outros 2 com trial self-service (Toolzz, Essent.IA) **anunciam onboarding guiado/assistido** (checklist passo a passo com apoio do time, na Toolzz; wizard conversacional de 15 min pra treinar o agente, na Essent.IA) — nenhum dos dois se apresenta como "configure sozinho".
- Dos dois CRMs com trial próprio: a **RD Station** tem onboarding estruturado documentado (planejamento de primeiros passos, comunidade, treinamentos) — refuta a hipótese. Já a **Kommo** tem reclamações reais e específicas no Reclame Aqui sobre dificuldade de configuração e suporte "só por link" durante o setup — **sustenta parcialmente** a hipótese, mas só pra Kommo, não generalizável à categoria.

**Autorizado pra copy, citando a fonte (tabela abaixo):** liderar o contra-ângulo com **"nenhuma reunião antes do acesso"**, não com "painel vazio" — esse é o diferencial mais forte e verificado: a maioria da concorrência direta de "agente de IA" no Brasil pede uma call de vendas antes de o cliente ver o produto rodando; aqui o cliente entra e testa sozinho, sem conversar com ninguém, nos próprios leads.

**NÃO autorizado:** generalizar "concorrente entrega painel vazio" como manchete — o dado real mostra o contrário pra Toolzz, Essent.IA e RD Station (todos anunciam onboarding assistido). A fricção de configuração da Kommo só pode ser usada se citada nominalmente (não como "a concorrência" genérica).

**Visual (gradiente azul-roxo + ícone de robô) confirmado só em parte:** confirmado na **Toolzz**; não confirmado (ou diferente) em RD Station, Kommo, Bluelephant, MelhorAgência.ai e Intelecta. A direção visual da Neovertix (zero gradiente, zero robô, `01-estrategia.md` §8) continua diferenciada, mas não por oposição a "todo mundo usa isso" — só parte do grupo usa.

#### Resumo da pesquisa de concorrência (Radar, 2026-11-03)

| Concorrente | Trial? | Self-service ou exige reunião? | Preço | Ângulo de venda | Visual |
|---|---|---|---|---|---|
| **RD Station** | Sim (Free permanente + planos pagos) | Self-service, sem cartão — mas com onboarding guiado ativo (treinamentos, comunidade, planejamento de 1º passos) | Só mensalidade por usuário (Free · Basic ~R$60-66 · Pro ~R$108-119 · Advanced sob consulta). Sem setup | Lidera com "CRM", mas forte presença de IA (Copiloto IA, priorização inteligente) | Azul/gradiente, ícones de chat — roxo não confirmado |
| **Kommo** | Sim, 14 dias | Self-service, sem cartão — onboarding é checklist auto-guiado; reclamações reais no Reclame Aqui de dificuldade de configuração e suporte "só por link" | Só mensalidade por usuário (US$20-45 ou BRL via parceiro, contrato mín. 6 meses no BR). Sem setup | Lidera com "CRM com IA" | Gradiente vibrante com efeito brilho; azul-roxo não confirmado especificamente |
| **Bluelephant** | Não tem | Exige "falar com especialista" antes de qualquer acesso — 100% consultivo | Sob consulta, sem preço público | Lidera com "agentes de IA"/consultoria sob medida | Azul claro, sóbrio, sem ícone de robô |
| **Toolzz** | Sim, 15 dias | Self-service via checkout — mas com onboarding guiado ("missões", checklist passo a passo, time ajuda a alinhar base de conhecimento) | Só mensalidade por agente (Mini R$399 · Starter R$990 · Enterprise a partir de R$3.900/mês). Sem setup mencionado | Lidera com "Agentes de IA" | **Gradiente azul-roxo + ícone de robô — confirma a observação do brief original (`01-estrategia.md` §8), só pra este concorrente** |
| **Essent.IA** | Trial sem cartão citado em busca (fonte única, não confirmado em 1ª mão — site é SPA, não renderizou texto completo via fetch) | Onboarding citado como wizard conversacional guiado ("O GUIA", 15 min) — não é painel vazio | Planos "Starter"/"Flex" por volume de respostas da IA; valor exato **não encontrado** | Lidera com "Sistema Operacional de IA" (agente + CRM AI-first + Revenue Intelligence) | **Não verificado** — site não renderizou visual via fetch |
| **MelhorAgência.ai** | Não tem trial self-service | "Consultoria grátis" via WhatsApp + garantia de reembolso de 7 dias pós-compra (não é trial pré-pagamento) | Sob consulta; comparam a "10% do salário de um humano" | Lidera com **"funcionários AI"** — termo que a própria Neovertix bane na copy (§6, banidas) | Emojis de robô/chave/foguete; gradiente azul-roxo **não confirmado** |
| **Intelecta** | Não tem | Exige "Reunião de Diagnóstico" (30-40 min) antes de qualquer proposta — 100% consultivo | Não divulgado; projetos de 15-45 dias + contratos de 12+ meses | Lidera com consultoria + CRM próprio ("G360") | Azul/ciano, ícones genéricos (SVGs não carregaram no fetch) |

*Nota de método: dado coletado via busca web e fetch de páginas públicas em 2026-11-03. Onde a página não renderizou (SPA/JS) ou a fonte foi única e genérica, está marcado "não verificado" — não extrapolar na copy.*

#### Matriz de features por concorrente (Radar, 2026-11-03 — rodada 2: "o que cada produto de fato inclui")

Pesquisa diferente da rodada 1 (acima): não é sobre como vendem, é sobre **o que cada produto de fato entrega**, comparado aos 5 módulos reais que o trial-vertice já tem hoje numa única plataforma e um único preço (fonte: tabela "Funcionalidades reais da plataforma" em §2) — agente de IA/WhatsApp, CRM com funil, rastreio/atribuição de conversão (Meta Ads), central de atendimento com tickets, gestão/agendamento de redes sociais.

| Concorrente | (a) Agente de IA / WhatsApp | (b) CRM com funil | (c) Rastreio/atribuição Meta Ads | (d) Central de atendimento (tickets) | (e) Gestão/agendamento de redes sociais | Nota |
|---|---|---|---|---|---|---|
| **RD Station** | Sim — RD Atendimento: "Configure chatbots com agentes de IA para responder dúvidas frequentes, qualificar leads" | Sim — RD Vendas: "Funil de Vendas... em um ou vários Funis de Vendas personalizados" | Sim — rastreamento de origem (parâmetro rdst_srcid), integração Meta Lead Ads e Relatório de Atribuição de Conversão (este último só combinando RD CRM Pro + RD Marketing Advanced) | Sim — RD Atendimento: "Gestão de Tickets: transforme conversas em demandas organizadas, com prazo e responsável" | Sim — RD Marketing: "Agendamento de Posts" no Instagram/Facebook/LinkedIn, com licença oficial da Meta | **Os 5 existem, mas em 3 produtos/planos separados (RD Marketing, RD Vendas/CRM, RD Atendimento) que se integram nativamente — não é uma plataforma, um preço** |
| **Kommo** | Sim — IA responde 24/7, qualifica e agenda reuniões | Sim — funil Kanban é o recurso histórico central da marca (ex-amoCRM) | Sim — Conversions API (CAPI) da Meta: eventos de Lead e de Purchase sincronizados automaticamente | Não verificado nativo — "gestão de tickets" aparece citada via integração com Zendesk (ferramenta terceira); não encontrada central de tickets própria documentada | **Não** — Instagram entra só como canal de resposta a mensagens/comentários; nenhuma menção a agendar publicações | |
| **Bluelephant** | Sim — "agente de IA no WhatsApp" (produto Morphia) | Não verificado — menciona "CRM" e "orçamento", sem detalhe de funil Kanban próprio | Não verificado — nenhuma menção a Meta Ads | Não verificado — "atendimento" e "escalonamento humano" citados, sem sistema de tickets detalhado | **Não** — nenhuma menção a agendamento/gestão de posts | 100% consultivo (decisão 16) — site raso em detalhe de produto |
| **Toolzz** | Sim — agente treinado pra WhatsApp Business, Instagram Direct, Messenger, site | **Não** — "conecta com seu CRM existente (Salesforce, HubSpot)" via API aberta; não tem CRM próprio | Não verificado — nenhuma menção | Parcial — menciona roteamento pra humano, sem central de tickets formal documentada | **Não** — Instagram é canal de atendimento (responde comentário/DM), não ferramenta de publicação | |
| **Essent.IA** | Não verificado | Não verificado | Não verificado | Não verificado | Não verificado | Site é SPA, não renderiza texto via fetch — mesmo problema da rodada 1. Busca de terceiros menciona um "Agente de Conteúdo" (3º de 3 agentes da suíte) que "cria conteúdo 24/7", mas isso não é necessariamente agendamento/aprovação/analytics de posts — não confirmado em 1ª mão |
| **MelhorAgência.ai** | Sim — "SDR no WhatsApp", "Vendedor AI no WhatsApp" | **Não** — nenhuma menção a CRM/funil | **Não** — nenhuma menção | Não verificado — "suporte 24/7" genérico, sem sistema de tickets detalhado | **Não** — nenhuma menção | |
| **Intelecta** | Sim — agente de IA integrado ao WhatsApp Business API (confirmado em conteúdo institucional do próprio domínio, não na home) | Sim — CRM próprio G360: "centraliza a gestão de leads, automatiza follow-ups, organiza o funil de vendas" | Não verificado — nenhuma menção a Meta Ads na home | Parcial/não verificado na página oficial — "classificação automática de mensagens e direcionamento de tickets por intenção" aparece em busca, não confirmado direto na home | **Não** — "análise de sentimento em tempo real" sobre redes sociais é monitoramento de reputação, não agendamento/gestão de publicação | |

*Nota de método (rodada 2): mesma regra da rodada 1 — dado só registrado quando a página pública (ou, no caso da Intelecta, conteúdo institucional do próprio domínio) confirma; "não verificado" onde o fetch não renderizou (SPA) ou a busca não achou menção. Nenhum dado inventado.*

#### Concorrente mais parecido com a combinação completa — busca por achado novo (Radar, 2026-11-03)

Busca adicional, fora dos 7 concorrentes já mapeados, por qualquer CRM/plataforma brasileira que junte os 5 módulos numa plataforma só. **Nenhum encontrado com os 5 de 5** — mas um candidato novo chega a 4 de 5, mais perto do que qualquer um dos 7 originais:

| Candidato novo | (a) | (b) | (c) | (d) | (e) | Preço / posicionamento |
|---|---|---|---|---|---|---|
| **ClienX CRM** (clienx.com.br) | Sim | Sim — funil Kanban | Sim — "Traqueamento e Envio de Conversões (Meta e Google Ads)" | Parcial — distribuição Round-Robin entre atendentes, sem tickets/SLA formal documentado | **Não** — nenhuma menção a agendamento/aprovação/analytics de posts | R$ 89,90/mês (plano único integrado; canal extra de WhatsApp é add-on); trial de 7 dias sem cartão |
| Criativivo (criativivo.com.br) | Parcial/ambíguo — "IA que responde por você" no módulo FlowChat, mas o produto é primariamente ferramenta de gestão de tráfego pago pra agências/gestores de tráfego, não atendimento ao cliente de PME | Sim — CRM Kanban (dentro do FlowChat) | Sim — alimenta o pixel do Meta Ads com eventos de conversão reais | Não verificado — sem central de tickets formal documentada | Sim — agendamento de posts estáticos, carrosséis e Reels | Preço variável (consultar #pricing); **público-alvo é agência/gestor de tráfego, ICP diferente do nosso (dono de PME)** |
| Captar Leads (captarleads.com.br) | Sim | Sim — funil Kanban customizável | **Não** | Sim — "Tickets, SLA, fila controlada e satisfação medida" | **Não** | Plano único ("pare de juntar 5 ferramentas") |
| SM Click (smclick.com.br) | Sim | Sim — Kanban | Não verificado | Sim (parcial) — relatórios de atendimento, departamentos ilimitados | Parcial — Instagram conectado como canal, sem agendamento | |

**Achado principal:** nem os 7 concorrentes da rodada 1, nem os 4 candidatos novos desta busca, entregam os 5 módulos (agente de IA + CRM + rastreio de Meta Ads + central de atendimento com tickets + gestão/agendamento de redes sociais) numa única plataforma com um único preço. O item **(e) gestão/agendamento de redes sociais é o mais raro de todos** — só apareceu de forma clara na RD Station (em produto/plano separado do CRM, não junto) e na Criativivo (ferramenta de agência de tráfego pago, ICP diferente do nosso). Nenhum concorrente de "agente de IA + CRM" voltado a dono de PME/comércio local (o nosso ICP, §3) tem essa peça.

**Mais perto, mas não é equivalente:** ClienX CRM — não mapeado nas rodadas anteriores — chega a 4 dos 5 módulos num preço único e barato (R$ 89,90/mês, sem entrada/setup), mas falta a gestão de redes sociais e o item (d) é fraco (round-robin, não um sistema de tickets/SLA como o nosso). Vale registrar como concorrente a monitorar daqui pra frente, mesmo tendo aparecido só nesta rodada.

**Liberado pra copy, com a formulação certa:** "stack completo numa plataforma só" **pode** ser usado — mas a afirmação sustentada pelos dados é sobre **unificação em uma plataforma e um preço**, não sobre "ser o único a ter o módulo X" isoladamente (a RD Station tem os 5 módulos, só que espalhados em 3 produtos/planos pagos separadamente; Kommo, Captar Leads e outros têm 3-4 dos 5 cada). A frase que os dados sustentam: os concorrentes que têm peças parecidas às nossas, ou vendem cada peça num produto/preço separado (RD Station), ou não têm a peça de redes sociais (todo o resto, exceto a Criativivo — que tem ICP de agência, não de PME).

**Não autorizado:** "somos os únicos com agente de IA" ou "somos os únicos com CRM" — isso é falso, a categoria toda tem isso individualmente. A única afirmação que os dados sustentam sem forçar é sobre a **combinação inteira numa coisa só, com um preço só** — não sobre cada módulo isolado.

**Os 3 pilares traduzidos pra hierarquia desta página** (`01-estrategia.md` §5):

| Pilar | O que esta página mostra |
|---|---|
| Rápido de verdade | Prazo fechado de 7 dias, com os 3 passos de ativação nomeados e visíveis |
| Engenharia, não slide | O agente atende **lead real**, não demo — e você lê as conversas. "Testado — não prometido" é literalmente a oferta aqui |
| Você não paga pra descobrir se funciona | Levado ao extremo: não paga, não agenda, não fala com vendedor, e no fim não precisa cancelar nada |

**Arquétipos aplicados:**
- **Mágico** — o momento da transformação é o **log de conversa real** que o agente resolveu enquanto o dono dormia. Demonstrado, nunca afirmado. Zero ícone de robô (`01-estrategia.md` §8).
- **Cara Comum** — inegociável nesta página, justamente porque não há reunião: o Lucas aparece como pessoa, autor do código e canal de suporte durante o trial. Zero "nossa equipe", zero linguagem corporativa.

**Léxico da marca — continua valendo, é a mesma empresa** (`business.json` / `01-estrategia.md` §6): construímos · roda sozinho · responde em [tempo] · mecanismo · fluxo · **testado — não prometido** · entrega. Liderar sempre com **"agente de IA"**; "CRM" entra como item incluído, nunca como produto principal.

**Tagline oficial deste produto: "Escala sem contratar"** (decisão do Lucas, 2026-10-12 — resolve a divergência a favor de `01-estrategia.md` §7, contra o "em iteração" de `business.json`). Benefício em 3 palavras, serve de headline ou de linha de apoio do hero. A assinatura institucional **"A gente constrói, não promete."** continua disponível como fechamento.

**Ressalva sobre "vértice":** a palavra segue no léxico da **empresa**, mas este produto **não pertence à linha Vértice** — usar "vértice" no nome ou na copy desta página sugeriria um parentesco de produto que não existe. Recomendação da Tese: reservar "vértice" para a linha Vértice e nomear este produto por aquilo que ele faz. Decisão do nome é do Lucas (pendência nº 2).

**Banidas — bloqueio duro na copy** (`business.json`): revolucionar · turbinar · o futuro chegou · funcionário digital que não dorme · disruptivo · sinergia · potencializar · ecossistema · game changer · "vale por N humanos".

**Banidas adicionais específicas desta página (decisão da Tese, dentro do atributo de voz "sóbrio, não gritado"):** "de brinde" · "sem pegadinha" (usar "sem letra miúda", formulação da fonte) · "grátis" em caps ou repetido como grito · emoji de foguete · "100% automático" (o agente é configurado por gente) · qualquer construção que sugira fricção zero na ativação.

**Direção visual herdada** (`01-estrategia.md` §8 — entregar pro Molda/módulo 21): off-black/off-white, nunca preto puro · UMA cor de destaque por tela · zero gradiente azul-roxo · tipografia carrega mais peso que cor · **nada de ícone de robô**.

---

## 7. Métrica de sucesso

**Métrica primária: nº de trials ATIVADOS por semana.**
Definição de ativado, inegociável: **canal conectado e o agente respondendo pelo menos 1 lead real.** Cadastro sem conexão **não conta** — a página pode encher de cadastro e entregar zero valor, porque esta oferta só existe depois que o canal está conectado.

**Secundárias (medir o funil onde ele realmente quebra):**
1. visitante → início da ativação (clique no CTA)
2. **início → conexão concluída** (a taxa que mede a fricção técnica — provavelmente a mais importante do projeto)
3. trial ativado → trial com uso real (leads atendidos > 0 ao longo do período)
4. trial concluído → plano pago (Plano Essencial ou Plano Escala)

**Não é métrica de sucesso:** tráfego, tempo na página, nº de cadastros, página estar bonita ou publicada (`identidade-web-os.md`, definição de sucesso).

**Baseline: não existe.** Nenhuma landing page da marca rodou com histórico de conversão, e esta oferta é nova. A primeira execução **define** a linha de base. **Nenhuma meta numérica neste brief** — qualquer número aqui seria inventado (regra de veracidade do Web OS). Meta só após o primeiro ciclo medido pelo Mede (módulos 33–36).

**Números permitidos na página — e só estes:**
- **7 dias** (duração do trial, fechada — decisão 15)
- **R$ 2.500 de entrada + R$ 500/mês** (Plano Essencial) · **R$ 3.200 de entrada + R$ 700/mês** (Plano Escala) — sempre com setup e recorrência juntos no mesmo bloco; exibir a entrada sozinha esconde o custo real e queima a honestidade da marca
- **7 dias** e os nomes dos verticais do ICP (clínica, concessionária, imobiliária, advocacia, comércio local) — ditos pelo Lucas. **"5–50 funcionários" sai:** esse recorte é da linha Vértice, não deste produto, cujo alvo é "comércio local e pequenas empresas em geral" sem faixa de headcount declarada
- Âncoras de `_context/marca.md`: SDR CLT júnior ~R$ 3.800–4.200/mês · 10 leads perdidos por demora = R$ 3.000–15.000/mês (ticket R$ 300–1.500) — como cálculo, não slogan
- "responde em segundos" (formulação da fonte, `02-oferta.md` §4)
- Preço redondo, sem "R$ 2.497" (`02-oferta.md` §3: a marca é sóbria, não vende impulso)

**Números proibidos na página:**
- Qualquer resultado de cliente, depoimento, nº de clientes atendidos, nº de trials rodados (não existe prova social própria ainda)
- Tempo de ativação ("rodando em X minutos") — **não medido**, ver pendência nº 7
- "De 4h de triagem manual pra 15 minutos" e "responde em 30 segundos" — são **exemplos de tom de voz** em `01-estrategia.md` §6, **não resultados medidos**
- Garantia de ≥30% ou devolução · R$ 1.900 / R$ 900 · Programa Fundador · "piloto de 2–4 semanas" — tudo isso é **da linha Vértice**, outro produto. Não aparece nesta página, nem como comparação

---

## 8. Pendências (não estimar, não decidir por conta própria)

Numeração preservada das versões anteriores do brief, pra quem já leu. Resolvidas: 1, 3, 4, 5, 6, 8 e a maior parte de 7 e 11. Canceladas: 10 e 12. **Só o que está na tabela abaixo ainda bloqueia trabalho.**

| # | Pendência | Dono | O que bloqueia |
|---|---|---|---|
| **2** | **Nome e slug definitivos** do produto e do projeto. Lucas: "depois a gente pensa no nome do projeto". Slug `trial-vertice` segue provisório; a copy usa `[nome pendente]`. **O nome não precisa usar "vértice"** (não é produto da linha Vértice — ver §6) | **Lucas** | Pasta do projeto, URL, tracking, `memory.md`, hero da página. **Decidir antes do módulo 22** — renomear depois do build é retrabalho em cadeia |
| **7b** | **Tempo de ativação:** quanto leva da conexão até o agente responder o primeiro lead. **Sem número medido** (a parte "quem configura" foi resolvida — ver decisões) | **Lucas / primeira execução real** | Qualquer promessa de tempo na copy ("pronto em X minutos"). Até medir, a página descreve passos, não minutos |
| **9** | *(herdada)* **Domínio/URL de destino** não confirmado (`01-estrategia.md` §8: neovertix.com/.com.br/.ai sem DNS, disponibilidade real não verificada) | **Lucas** | Deploy |
| **11b** | **Validação do ICP em campanha real.** O alvo está definido pelo Lucas (§3), mas **nenhuma conversão testou esse recorte** — nem qual vertical responde melhor (clínica? concessionária? advocacia?) | **Mede, módulos 33–36, após o 1º ciclo** | Priorizar vertical na copy e no tráfego da V2. Não bloqueia a V1 |

### Decisões fechadas em 2026-10-12 (fonte: Lucas)

1. ~~**Duração: 5 dias** (era "4 ou 7"). A página publica 5, não uma faixa.~~ — **substituída pela decisão 15 (2026-11-02): duração passa a 7 dias.** A regra "a página publica um número fechado, não uma faixa" continua valendo.
2. **Preço: entrada + recorrência.** ~~R$ 2.500 + R$ 500/mês · R$ 3.200 + R$ 700/mês~~ — **valores de recorrência substituídos pela decisão 12 (2026-11-01) e restaurados pela decisão 13 (2026-11-02): R$ 500/mês e R$ 700/mês voltam a valer.** O modelo entrada + recorrência continua valendo.
3. **Linha de produto: independente** (corrige a leitura anterior de "substitui a Piloto Vértice"). Mesma empresa — Neovertix —, produtos diferentes: linha Vértice (implementação sob medida), Web OS (criação automática de sites/landing pages) e **este produto** (agente de IA + CRM + redes sociais, via Bolten). **Não substitui, não se funde, não herda a Garantia Vértice.**
4. **Dados e descarte (era pendência nº 6):** instância própria por cliente durante os 7 dias (duração revista pela decisão 15); **se não comprar, a instância é descartada** — sem acesso residual, sem dado além do período. É só isso que a página pode afirmar (ver §3, objeção 5).
5. **Quem configura (era a metade de nº 7):** **o próprio cliente**, self-service de verdade, com **suporte do agente de IA da Neovertix durante a configuração** + material de ativação (documentação/tutorial) a ser construído. O "quanto tempo leva" segue aberto como nº 7b.
6. **Tagline (era pendência nº 8): "Escala sem contratar"** — oficial para este produto, a favor de `01-estrategia.md` §7.
7. **ICP (era pendência nº 11):** comércio local e pequenas empresas em geral — clínicas, concessionárias, imobiliárias, advocacia, comércio local amplo. **Criador/infoprodutor descartado.** Validação em campanha fica como nº 11b.
8. **Canal de aquisição:** Instagram do Lucas, possível TikTok depois (nota de distribuição em §3, insumo pro módulo 27).
9. *Item futuro, sem decisão:* possível acréscimo/upsell pra cliente existente.
10. **Pendência nº 10 CANCELADA** ("destino da Garantia Vértice"): nasceu da leitura errada de substituição. Este produto nunca teve essa garantia — nada pra aposentar. A garantia continua sendo da linha Vértice, intacta.
11. **Modelo de venda reafirmado:** marketing leva o cliente a entrar → testa sem fidelidade → se gostar, compra. Já coberto em §1 e §4, sem mudança.

### Decisões fechadas em 2026-11-01 (fonte: Lucas, confirmado por pergunta de clarificação)

12. ~~REVERTIDA pela decisão 13 (2026-11-02)~~ **Planos renomeados e recorrência reprecificada** (substitui os valores da decisão 2). **Plano Inteligente** = R$ 2.500 de entrada + **R$ 2.700/mês** (era R$ 500) — CRM + agente de IA, **teto de até 500 atendimentos/mês** (limite de uso novo, não existia antes). **Plano Escala** = R$ 3.200 de entrada + **R$ 3.500/mês** (era R$ 700) — tudo do Inteligente + Gestão de Redes Sociais (Instagram). Entrada (setup único) **inalterada e ainda cobrada à parte**. Liberado pra página. O que acontece acima do teto segue aberto como pendência nº 12.
   ~~*Nota da Tese para os módulos 26 (Convence) e 27:*~~ *(obsoleta com a decisão 13 — a recorrência voltou a R$ 500/R$ 700, longe da âncora SDR)* com a nova recorrência, o Plano Escala (R$ 3.500/mês) fica perto da âncora SDR CLT júnior (~R$ 3.800–4.200/mês, `02-oferta.md` §3). A âncora continua verdadeira, mas a margem de comparação ficou estreita — usar como cálculo que o prospect faz, nunca como manchete de economia.

### Decisões fechadas em 2026-11-02 (fonte: Lucas)

13. **Planos voltam aos nomes e valores do briefing** (supera e reverte a decisão 12 em três pontos: nome **Inteligente → Essencial**; mensalidade **R$ 2.700 → R$ 500** e **R$ 3.500 → R$ 700**; **teto de 500 atendimentos/mês removido**). **Plano Essencial** = R$ 2.500 de entrada + **R$ 500/mês** — Agente de IA + CRM. **Plano Escala** = R$ 3.200 de entrada + **R$ 700/mês** — Agente de IA + CRM + redes sociais (Instagram). Entrada inalterada. Fonte: tabela final enviada pelo Lucas em 2026-11-02 (coincide com `neovertix crm/_context/briefing.md`). A tabela é completa sobre o que cada plano inclui e não cita teto — leitura registrada: o mecanismo de limite de uso saiu do modelo.
14. **Pendência nº 12 CANCELADA** ("política acima do teto de 500 atendimentos/mês", aberta em 2026-11-01): nasceu de um teto que não existe mais nesta versão da oferta (decisão 13). Nada pra definir sobre excedente, contagem de atendimento ou teto no trial. Se um limite de uso voltar ao modelo, abre-se pendência nova.
15. **Duração do trial: 5 → 7 dias** (substitui a decisão 1). Fonte: Lucas, direto no chat, 2026-11-02. Atualizado em §2 (tabela), §3 (objeções 3 e 5), §4, §6 (Moore e pilar "Rápido de verdade"), §7 (números permitidos) e decisão 4. Nenhum argumento muda de natureza: "prazo fechado" e "acaba sozinho" seguem válidos com 7; continua sem métrica de sucesso atrelada à duração. `tom-de-voz.md` do projeto já atualizado pelo Lucas.

### Decisões fechadas em 2026-11-03 (fonte: Radar, módulo 28 — pesquisa de concorrência)

16. **Dado de concorrência (pendência nº 5): resolvida.** Radar analisou páginas públicas de RD Station, Kommo, Bluelephant, Toolzz, Essent.IA, MelhorAgência.ai e Intelecta (2026-11-03) — todos os 7 alvos listados foram encontrados e analisados, nenhum precisou ser descartado por inexistência. **Achado principal:** a hipótese do "painel vazio" (§6) **não se confirmou como formulada** — nenhum concorrente se anuncia assim, e os dois únicos concorrentes de "agente de IA" com trial self-service (Toolzz, Essent.IA) anunciam onboarding guiado. O diferencial real e validado é outro: **3 dos 5 concorrentes de agente de IA (Bluelephant, Intelecta, MelhorAgência.ai) nem oferecem trial self-service**, exigindo reunião de vendas/diagnóstico antes de qualquer acesso — esse é o contra-ângulo autorizado em §6, não "painel vazio". Ponto pontual sobre fricção de configuração da Kommo (via reclamações no Reclame Aqui) registrado, mas só utilizável citando a Kommo nominalmente, não generalizado. Tabela completa de achados por concorrente e as regras de uso em copy estão em §6, bloco "Contra-ângulo".

### Nenhuma fonte de marca foi alterada por este brief

Nada em `config/business.json`, `Web OS/_context/icp-web.md`, `Social mídia IA/_context/marca.md`, `branding/neovertix/*` ou `tom-de-voz.md` muda por causa deste produto. Uma sincronia chegou a ser feita na 2ª rodada (quando a leitura era "substitui a Piloto Vértice") e **foi revertida** ao baseline. Se/quando o Lucas decidir agregar este produto à linha Vértice, a Tese faz o registro — não antes.

**O que continua herdado da marca Neovertix** (é a mesma empresa): posicionamento, voz, arquétipos Mágico + Cara Comum, léxico e palavras banidas, âncoras de custo (`02-oferta.md` §3) e a direção visual de `01-estrategia.md` §8.
