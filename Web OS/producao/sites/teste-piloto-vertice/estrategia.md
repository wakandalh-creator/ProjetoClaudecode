# Estratégia Web — teste-piloto-vertice

> **Status: PROJETO DE TESTE do pipeline Web OS.** Não vai ao ar. Serve pra validar o módulo 20 ponta a ponta.
> Agente: Tese-ext · Módulo: `Web OS/modules/20-business-discovery-estrategia.md` · Data: 2026-10-08
> Fontes: `config/business.json` (offers[0]) · `branding/neovertix/01-estrategia.md` · `branding/neovertix/02-oferta.md` · `Web OS/_context/icp-web.md` · `Web OS/_context/identidade-web-os.md`

---

## 1. Objetivo de negócio

**Geração de lead qualificado para demo** — não venda direta, não institucional.

A página existe pra converter tráfego frio/morno (Instagram, indicação, busca) em **demo ao vivo agendada com dados do prospect**. O fechamento acontece na demo, com o Lucas, não na página.

Por que não venda direta no checkout: a prova central da marca é a demo com dados reais do prospect antes de qualquer pagamento (`02-oferta.md`, value stack, item 1). Vender no botão contradiz o mecanismo de reversão de risco da própria oferta.

**CTA primário:** agendar demo (1 único CTA repetido, sem CTA secundário competindo).

---

## 2. Oferta específica

**Piloto Vértice** — `config/business.json`, `offers[0]`, tipo `entrada`.

| Campo | Valor (fonte: business.json / 02-oferta.md) |
|---|---|
| Preço | R$ 1.900 setup único · Programa Fundador: R$ 900 |
| Prazo | 2–4 semanas |
| Escopo | 1 canal (WhatsApp **ou** Instagram) · atendimento IA **ou** SDR IA · CRM simples |
| Garantia | Garantia Vértice: métrica combinada por escrito; se não melhorar ≥30% frente à linha de base, devolução total |
| Entregável final | Relatório da métrica combinada |

**Programa Fundador (3–5 vagas):** R$ 900 em troca de autorização de caso de uso com nome/logo + depoimento em vídeo. Na página, tratar como vaga limitada e temporária — **não** como desconto permanente (`02-oferta.md` §3).

---

## 3. ICP

**Primário (quem a página precisa convencer):** dono de PME brasileira, 5–50 funcionários, em serviços, e-commerce, clínica, imobiliária ou educação. Recebe lead por WhatsApp, Instagram ou formulário e demora horas pra responder. Já considerou contratar mais gente — caro e lento de treinar. **Decisor único** (`icp-web.md`, tabela oferta→página).

**Secundário (tolerado, não endereçado):** criador/infoprodutor com DM de lançamento parada. A página não fala com ele diretamente — se ele converter, converte por tabela. Não criar seção pra ele nesta página.

**Fora do ICP desta página:** agência white-label (vai pra página de Vértice Full/consultiva) e empresa sem volume de lead (não tem o que automatizar).

**Objeções que a página é obrigada a responder** (`icp-web.md` + `02-oferta.md` §5):
1. "IA soa robótica" → a demo usa a voz do seu negócio; você ouve antes de ligar em cliente real.
2. "Agência nova, sem case" → você vê rodando com seus dados antes de assinar. Somos novos — e é por isso que o risco inicial é nosso.
3. "Quanto tempo até funcionar" → prazo fechado de 2–4 semanas, métrica definida no início e medida no fim.
4. "Se quebrar, quem conserta" → quem escreve o código atende o chamado. Mais o walkthrough técnico, pra você não depender de caixa-preta.

---

## 4. Problema comercial central

> Skill aplicada: `problem-framing-canvas` (MITRE, 3 fases) — modo single-shot sobre contexto já existente, sem pesquisa nova.

**Look Inward (nosso lado).** Sintoma: a Neovertix não tem página de conversão pro Piloto. Hoje o pedido de demo depende de conversa 1:1 no Instagram ou indicação — ou seja, da agenda do Lucas. Por que não foi resolvido: founder solo, prioridade estava no mecanismo e na marca. Viés a derrubar: supor que quem chega já entende o que é "operações com IA" — não entende; o prospect chega com uma dor operacional ("ninguém responde meu WhatsApp"), não com uma categoria na cabeça.

**Look Outward (lado do prospect).** Quem sente: o dono, pessoalmente — é ele quem vê a mensagem não respondida às 22h. Quando: picos de lead (campanha, indicação, pós-conteúdo) e fora do horário comercial. Consequência: lead esfria e compra de quem respondeu primeiro. Quem **não** tem o problema: quem já tem equipe de plantão (e paga por isso) ou quem não gera lead. Quem se beneficia do problema continuar: o concorrente do prospect que respondeu primeiro. Quem foi deixado de fora: o dono que já tentou chatbot de árvore de decisão e saiu queimado — ele é o mais cético e o mais qualificado.

**Reframe — o problema comercial central da página:**

> Dono de PME com volume de lead perde venda por demora de resposta, mas não compra automação de IA porque não consegue distinguir quem entrega de quem promete — e todo fornecedor do nicho soa igual. O custo de errar a escolha (dinheiro + tempo de implantação + cliente ouvindo um robô ruim) parece maior que o custo de continuar perdendo lead.

**How Might We:** como fazer a página provar o mecanismo *antes* do primeiro pagamento — e deixar explícito que o risco inicial é da Neovertix — pra que o próximo passo custe quase nada em risco percebido?

**Consequência direta pra arquitetura da página:** a página não vende IA. Ela vende **a demo** como o passo barato. Prova > promessa (`identidade-web-os.md`, princípios de decisão).

---

## 5. Por que contratariam isso (JTBD)

> Skill aplicada: `jobs-to-be-done` (Christensen + Value Proposition Canvas), destilado do avatar de `02-oferta.md` §1 — sem persona nem citação inventada.

**Job funcional:** responder todo lead que entra, em segundos, qualificar, e ter isso registrado num lugar só — sem contratar mais ninguém.

**Job social:** parecer uma empresa organizada e responsiva pro cliente dele. Não parecer "aquele negócio pequeno que nunca responde".

**Job emocional:** parar de carregar o WhatsApp da empresa como ansiedade pessoal. Dormir sem a sensação de que tem dinheiro parado em mensagem não lida.

**Dores (ordenadas por intensidade):**
1. Lead esfriando enquanto ninguém responde — perda de receita direta.
2. Contratar é caro e lento: a âncora de custo da própria oferta é SDR CLT júnior a ~R$ 2.200 de salário + ~80% de encargos = ~R$ 3.800–4.200/mês, só em horário comercial, com turnover (`02-oferta.md` §3). *Usar como cálculo que o prospect faz na demo — não como slogan de comparação.*
3. Medo de o cliente ouvir um robô ruim e piorar a percepção da marca dele.
4. Já viu fornecedor prometer e não entregar.

**Ganhos que fariam ele trocar o status quo:**
- Ver funcionando com os dados do negócio dele antes de pagar.
- Prazo fechado (2–4 semanas), não consultoria de trimestre.
- Garantia com métrica definida em conjunto — risco de entrada baixo.
- Poder auditar o que roda (walkthrough técnico), em vez de depender de caixa-preta.

**O que ele "contrata" hoje no lugar:** ele mesmo e a equipe respondendo no intervalo, chatbot de árvore de decisão, ou nada.

---

## 6. Diferencial e posicionamento da página

> Skill aplicada: `positioning-workshop` → saída no formato Geoffrey Moore. Deriva do posicionamento-mãe (`01-estrategia.md` §2) especializado pro Piloto numa landing page.

**Para** donos de PME brasileira (5–50 funcionários) com volume de lead no WhatsApp/Instagram
**que precisam** parar de perder venda por demora de resposta sem contratar mais gente,
**o Piloto Vértice**
**é um** piloto de operações com IA de 2–4 semanas em 1 canal
**que** coloca o atendimento (ou o SDR) respondendo em segundos, qualificando e registrando o lead no CRM — com métrica combinada e garantia de 30% ou devolução total.

**Diferenciação:**
**Diferente de** agências de marketing com IA e consultorias de IA genéricas, que vendem no slide e cobram antes de mostrar,
**o Piloto Vértice**
**entrega** o sistema rodando com os dados do prospect na demo, antes de contrato — construído e suportado pela mesma pessoa que escreve o código.

**Os 3 pilares, traduzidos pra hierarquia da página** (`01-estrategia.md` §5):
| Pilar | O que a página mostra |
|---|---|
| Rápido de verdade | Prazo fechado de 2–4 semanas, escopo de 1 canal visível e delimitado |
| Engenharia, não slide | Explicação em passos do mecanismo ("lê a mensagem, consulta o CRM, responde") + promessa do walkthrough técnico |
| Você não paga pra descobrir se funciona | Garantia Vértice em bloco próprio, com a métrica em destaque |

**Arquétipos aplicados à página:** Mágico (o "antes/depois" do fluxo manual vs. automático, demonstrado — nunca afirmado) + Cara Comum (o Lucas aparece como pessoa e autor do código; zero linguagem corporativa, zero "nossa equipe").

**Léxico obrigatório:** vértice · construímos · roda sozinho · responde em [tempo] · mecanismo · fluxo · testado — não prometido · entrega.

**Banidas (bloqueio duro na copy):** revolucionar · turbinar · o futuro chegou · funcionário digital que não dorme · disruptivo · sinergia · potencializar · ecossistema · game changer · "vale por N humanos".

**Direção visual herdada** (`01-estrategia.md` §8, pro módulo de UI): off-black/off-white (nunca preto puro), UMA cor de destaque por tela, zero gradiente azul-roxo, tipografia carregando mais peso que cor, **nada de ícone de robô**.

---

## 7. Métrica de sucesso

**Métrica primária:** nº de **demos qualificadas agendadas** por semana vindas da página (qualificada = ICP primário com volume de lead declarado).

**Secundárias:** taxa visitante → agendamento · taxa agendado → compareceu · nº de pilotos vendidos (incluindo vagas do Programa Fundador).

**Não é métrica de sucesso:** tráfego, tempo na página, página estar bonita ou publicada (`identidade-web-os.md`, definição de sucesso).

**Baseline:** não existe. Primeira landing page da marca, sem histórico de conversão. A primeira execução **define** a linha de base — não há meta numérica nesta versão do brief, porque qualquer número aqui seria inventado (regra de veracidade do Web OS). Meta só depois do primeiro ciclo medido pelo módulo de measurement.

**Números permitidos na página** (únicos com fonte): R$ 1.900 / R$ 900 · 2–4 semanas · 1 canal · 30% de melhora ou devolução · 3–5 vagas do Programa Fundador · 5–50 funcionários.

**Números proibidos na página:** qualquer resultado de cliente, depoimento, nº de clientes atendidos, "de 4h pra 15 minutos" e "responde em 30 segundos" — estes dois últimos são **exemplos de tom de voz** em `01-estrategia.md` §6, não resultados medidos. Pra descrever o mecanismo, usar a formulação da fonte: "responde em segundos" (`02-oferta.md` §4).

---

## 8. Pendências (não estimar — resolver com quem é dono)

| # | Pendência | Dono | Bloqueia |
|---|---|---|---|
| 1 | Estrutura, oferta e preço praticados pelos concorrentes nas landing pages deles (Bluelephant, Toolzz, Essent.IA, MelhorAgencia.ai, Intelecta — nomes de `01-estrategia.md` §8; nenhum dado de página coletado) | **Radar, módulo 28 (Sprint 3)** | Decisão de contra-ângulo e de bloco de comparação |
| 2 | Zero prova social própria (sem case, sem depoimento) — a página precisa converter sem isso. Resolve quando o Programa Fundador fechar as 3–5 vagas | Lucas | Bloco de prova social |
| 3 | Domínio/URL de destino não confirmado (`01-estrategia.md` §8: neovertix.com/.com.br/.ai sem DNS, disponibilidade real não verificada) | Lucas | Deploy |
| 4 | Tagline comercial em iteração (rodada 3, `business.json`) — "Escala sem contratar" é a oficial em `01-estrategia.md` §7. Divergência entre as duas fontes | Tese + Lucas | Headline/hero |
| 5 | Canal de agendamento da demo (Calendly, WhatsApp, formulário?) e o que é capturado no lead | Lucas | CTA e tracking |

**Nota de sincronia (fora do escopo desta página, pra registro):** `config/business.json` lista a tagline comercial como "em iteração — candidatos rodada 3", enquanto `branding/neovertix/01-estrategia.md` §7 dá "Escala sem contratar" como oficial. Precisa decisão do Lucas pra alinhar as duas fontes.
