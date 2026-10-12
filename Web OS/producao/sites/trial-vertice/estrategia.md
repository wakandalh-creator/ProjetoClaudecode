# Estratégia Web — trial-vertice (slug provisório)

> **Status: projeto real, destinado a ir ao ar.** Substitui e descarta `Web OS/producao/sites/teste-piloto-vertice/` por decisão do Lucas ("o criado não ficou bom, pode desconsiderar") — **nada daquele projeto é reaproveitado**, nem copy, nem specs, nem design.
> Agente: Tese-ext · Módulo: `Web OS/modules/20-business-discovery-estrategia.md` · Data: 2026-10-12 (revisado no mesmo dia com as decisões da 2ª rodada da entrevista)
> Fontes: entrevista com o Lucas (2026-10-12) · `config/business.json` · `branding/neovertix/01-estrategia.md` · `branding/neovertix/02-oferta.md` · `Web OS/_context/icp-web.md` · `Web OS/_context/identidade-web-os.md` · `Social mídia IA/_context/marca.md`
> ⚠️ **O slug `trial-vertice` é provisório.** Nome e slug definitivos são pendência nº 2. Decidir **antes** do módulo 22 (build/deploy) — renomear depois arrasta `memory.md`, `specs/`, URLs e tracking.

---

## 1. Objetivo de negócio

**Venda direta no sentido de ativação direta do trial.** A página não gera lead pra reunião, não agenda demo, não pede contato comercial.

**CTA primário único:** começar o teste grátis (conectar o canal). Repetido ao longo da página, sem CTA secundário competindo.

Consequência direta: a conversão da página **termina na ativação técnica**, não num formulário. Isso é diferente de tudo que o Web OS já briefou — o gargalo não é o clique, é a conexão do canal (ver §4 e métrica em §7).

Por que não é demo agendada (como era a Piloto Vértice): a prova deixou de ser o Lucas mostrando o agente com dados do prospect e passou a ser **o próprio agente atendendo os leads reais do prospect**. É o pilar 3 da marca — "você não paga pra descobrir se funciona" (`01-estrategia.md` §5) — levado ao limite: não paga nada e não fala com vendedor.

---

## 2. Oferta específica

**Oferta NOVA que passou a ser a oferta de ENTRADA da Neovertix, no lugar da Piloto Vértice** (decisão do Lucas, 2026-10-12, 2ª rodada). Fonte: entrevista com o Lucas em 2026-10-12. `config/business.json` já foi sincronizado — `offers[0]` agora é esta oferta.

| Campo | Valor (fonte: entrevista Lucas 2026-10-12) |
|---|---|
| Formato | Teste grátis self-service: **sem reunião, sem agendamento, sem compromisso** |
| Duração | **5 dias** (fechado) |
| Natureza do ambiente | Projeto configurado **para o cliente** — não sandbox genérico com dados fictícios |
| Ativação | O cliente **conecta o canal real dele**: nº de WhatsApp e/ou Instagram e/ou CRM |
| O que roda no trial | O agente de IA atende os **leads reais** do cliente durante o período |
| Fim do trial | **Simplesmente acaba.** Sem cobrança automática, sem renovação, sem letra miúda. O cliente vê o resultado e decide depois |
| Infraestrutura | Plataforma **Bolten** (parceria nova) — CRM white-label com agente de IA treinável, WhatsApp via QR Code ou Cloud API oficial, Meta/Instagram via Conversions API |

### Enquadramento de venda (decisão explícita do Lucas)

> "Em vez de vender como CRM, vender como agente de IA — o CRM vai de brinde."

Regra para toda a página e para todos os módulos a jusante: **o herói da oferta é o agente de IA.** O CRM é consequência, nunca a manchete. Coerente com `02-oferta.md` §1 (value stack): o agente é o mecanismo central, o CRM existe para "atendimento rápido virar dado que se usa depois".

⚠️ **Correção de léxico (Tese):** "de brinde" é linguagem de venda de impulso e contraria o atributo de voz "sóbrio, não gritado" (`01-estrategia.md` §6). Na copy, usar **"o CRM vem incluído"** / **"vem junto"**. "Brinde" fica no vocabulário interno de posicionamento, não na página.

### Planos pós-trial (fonte: Lucas, direta — confirmado na 2ª rodada)

| Plano | Entrada (setup único) | Recorrência | Escopo |
|---|---|---|---|
| 1 | **R$ 2.500** | **R$ 500/mês** | Agente de IA + CRM incluído (sem redes sociais) |
| 2 | **R$ 3.200** | **R$ 700/mês** | Agente de IA + CRM + redes sociais (Instagram) |

Padrão setup + mensalidade, igual às outras ofertas Neovertix (`02-oferta.md` §3: setup ancora a construção, mensalidade ancora manutenção e iteração). **Preço liberado pra publicação na página** — o bloqueio anterior caiu.

**Item futuro (não é decisão, não bloqueia nada):** o Lucas vai avaliar depois um possível acréscimo/upsell pra quem já é cliente. Sem definição — não aparece na página nem no `business.json`.

### Regras de veracidade específicas desta página (`identidade-web-os.md`)

- **Sobre a Bolten:** a documentação da Bolten **não menciona trial nativo**. O período grátis é decisão comercial da Neovertix por cima da ferramenta. A página **nunca** pode sugerir que o trial é recurso da plataforma, nem afirmar qualquer capacidade da Bolten além de: CRM white-label, agente de IA treinável, WhatsApp (QR Code ou Cloud API oficial), Meta/Instagram (Conversions API).
- **White-label significa marca Neovertix na frente.** A página não precisa (nem deve, sem decisão do Lucas) citar a Bolten como fornecedor.
- **A Garantia Vértice (≥30% ou devolução total, `02-oferta.md` §2) NÃO entra nesta página.** Ela era o mecanismo de reversão de risco da Piloto Vértice, oferta **paga** — que esta oferta substituiu. Num trial grátis, "devolução total" não significa nada, e o trial já é a reversão de risco. O destino da garantia (aposentar ou redesenhar para os planos pagos) é **pendência nº 10** e só o Lucas decide; até então ela continua intacta em `business.json` e `02-oferta.md`, mas fora desta página.

---

## 3. ICP

Base de ICP conforme `Web OS/_context/icp-web.md` — **a seção "Base" daquele arquivo só muda por decisão explícita do Lucas e este brief não a altera.**

**Primário (quem a página precisa convencer):** dono de PME brasileira, 5–50 funcionários, em serviços, e-commerce, clínica, imobiliária ou educação. Recebe lead por WhatsApp, Instagram ou formulário e demora horas pra responder. Decisor único — assina e conecta sozinho, sem comitê. **É ele quem tem a senha/o celular do WhatsApp da empresa** — fato operacional que importa muito aqui, porque a ativação depende disso.

**Secundário (tolerado, não endereçado na V1):** criador/infoprodutor com DM de lançamento parada; pequena agência interessada em white-label.

**Observação registrada (não é proposta de mudança de ICP):** o Plano 2 (R$ 3.200, com Instagram) tem afinidade natural com o ICP secundário criador/infoprodutor, e um trial self-service sem reunião é um formato de compra mais compatível com esse público do que a Piloto Vértice era. **Se o Lucas quiser que esta página fale primariamente com criadores, é decisão dele** — `icp-web.md` proíbe qualquer agente inferir mudança de ICP. Até então: ICP primário = dono de PME.

**Fora do ICP desta página:** quem não tem volume de lead (não tem o que o agente atender) e quem não pode/não quer conectar o canal oficial da empresa (a oferta não funciona sem isso — não tentar convencer esse perfil na copy, é desperdício de página).

### Objeções que a página é obrigada a responder

Herdadas (`icp-web.md` + `02-oferta.md` §5):
1. **"IA soa robótica"** → no trial não é demo: é o seu lead real conversando. Você lê as conversas que o agente resolveu.
2. **"Agência nova, sem case"** → o trial é a prova. Você não paga pra descobrir — nem com cartão, nem com reunião.
3. **"Quanto tempo até funcionar"** → prazo fechado de 5 dias.
4. **"Se quebrar, quem conserta"** → quem escreve o código é quem responde (Cara Comum, `01-estrategia.md` §4).

**Novas, criadas pelo próprio mecanismo desta oferta** (derivadas do fato "ativação exige conectar WhatsApp/Instagram/CRM", não inventadas):

5. **"Vou conectar o WhatsApp da minha empresa numa empresa que eu não conheço?"** — esta é, na leitura da Tese, **a objeção nº 1 desta página**, acima de preço. A página precisa responder: o que o agente acessa, o que acontece se eu desconectar, e o que acontece com as conversas quando o trial acaba. *Conteúdo factual dessa resposta é pendência nº 6 — não inventar política de dados.*
6. **"Acaba e vocês me cobram?"** → não. Acaba e pronto: sem cobrança automática, sem renovação. Usar a formulação da fonte da marca: **"sem letra miúda"** (`02-oferta.md` §2), não "sem pegadinha".
7. **"Quanto trabalho eu tenho pra ligar isso?"** → a página tem que ser honesta: existe uma etapa técnica (conectar o número/conta). Fingir fricção zero queima a confiança na primeira tela de QR Code e contraria o atributo "honesto sobre onde estamos" (`01-estrategia.md` §6). *Quem executa a configuração do agente durante o trial é pendência nº 7.*

---

## 4. Problema comercial central

> Skill aplicada: `problem-framing-canvas` (3 fases) — single-shot sobre contexto existente, **sem pesquisa de mercado nova** (isso é do Radar, módulo 28).

**Look Inward (nosso lado).** A Neovertix hoje só tem porta de entrada que passa pela agenda do Lucas: demo ao vivo, conversa 1:1, indicação. Isso trava a aquisição no gargalo de um founder solo. A oferta nova resolve isso estruturalmente — o trial vende sozinho enquanto o Lucas constrói. Risco de viés a derrubar: supor que tirar o Lucas da venda é só ganho. Tirar o Lucas da venda **também tira o arquétipo Cara Comum e a profundidade técnica demonstrada ao vivo**, que são dois dos três espaços vagos que a marca ocupa contra a concorrência (`01-estrategia.md` §8). Se a página virar um SaaS self-service anônimo, a Neovertix perde o diferencial do próprio posicionamento Moore ("o fundador escrevendo o código — não um departamento comercial entre você e a solução"). **Consequência obrigatória: o Lucas tem que estar visível na página como pessoa e como autor do sistema, mesmo sem aparecer na venda.**

**Look Outward (lado do prospect).** Quem sente a dor: o dono, pessoalmente, vendo mensagem não respondida às 22h. Quando aparece: pico de lead e fora do horário comercial. Consequência: o lead compra de quem respondeu primeiro. Quem não tem o problema: quem já paga equipe de plantão, ou quem não gera lead. Quem é o mais cético e o mais qualificado ao mesmo tempo: o dono que já tentou chatbot de árvore de decisão e saiu queimado.

**O que mudou em relação à oferta anterior:** na Piloto Vértice, o custo de errar a escolha era **dinheiro + tempo de implantação**. Num trial grátis, sem cartão e sem reunião, esse custo foi a zero. **Mas o custo percebido não foi a zero — ele mudou de natureza.**

**Reframe — problema comercial central desta página:**

> O risco financeiro da decisão foi eliminado, mas sobraram dois custos que a página tem que derrubar: **o risco de confiança** (entregar o canal de vendas vivo da empresa — WhatsApp/Instagram — pra uma marca nova, sem case) e **o esforço de ativação** (conectar, configurar, ver funcionando). Hoje, pro dono de PME, esses dois custos juntos ainda parecem maiores que o custo silencioso de continuar perdendo lead por demora.

**How Might We:** como fazer a conexão do canal parecer **pequena, reversível e segura** — ao ponto de o dono preferir conectar hoje a continuar perdendo lead — sem mentir sobre a fricção técnica que existe?

**Consequências diretas pra arquitetura da página** (entregar pro Guia/módulo 25 e pro Convence/módulo 26):
- A página **não vende IA**. Vende um teste de 5 dias que acaba sozinho.
- **Prova > promessa** (`identidade-web-os.md`): o ativo de prova mais forte disponível é o **log de conversas reais** que o agente resolveu durante o trial — mostrar o formato do que o cliente vai ver, não um dashboard bonito.
- **Reversibilidade é bloco de página, não rodapé.** "Desconecta quando quiser / acaba e pronto" tem o mesmo peso visual do CTA.
- A fricção de ativação é um **funil dentro da página** (3 passos nomeados), não um botão mágico.

---

## 5. Por que contratariam isso (JTBD)

> Skill aplicada: `jobs-to-be-done` (Christensen + Value Proposition Canvas), destilado do avatar de `02-oferta.md` §1. Sem persona, citação ou demografia inventada.

**Job funcional:** responder todo lead que entra, em segundos, qualificar e registrar num lugar só — sem contratar mais ninguém.

**Job social:** parecer uma empresa organizada e responsiva pro cliente dele. Não parecer "aquele negócio pequeno que nunca responde".

**Job emocional:** parar de carregar o WhatsApp da empresa como ansiedade pessoal.

**Job específico desta oferta (o que o trial contrata que a Piloto não contratava):** *"deixar de apostar."* O dono não quer avaliar um fornecedor — ele quer **ver com os olhos dele, nos leads dele, antes de assumir qualquer compromisso**, e sem gastar uma hora numa reunião de vendas pra isso. O trial não compete com outra IA; compete com **procrastinar a decisão**.

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

**Para** donos de PME brasileira (5–50 funcionários) com volume de lead no WhatsApp e no Instagram
**que precisam** parar de perder venda por demora de resposta sem contratar mais gente,
**[nome pendente — ver pendência nº 2]**
**é um** teste grátis de 5 dias em que o agente de IA da Neovertix é configurado no canal real do negócio
**que** atende, qualifica e registra os leads de verdade durante o período — e no fim **simplesmente acaba**, sem cobrança e sem compromisso: o dono vê as conversas que o agente resolveu e decide depois.

**Diferenciação:**
**Diferente de** agências de marketing com IA e consultorias de IA genéricas, que vendem no slide e cobram antes de mostrar,
**esta oferta**
**entrega** o mecanismo rodando nos leads reais do cliente **antes de qualquer pagamento e sem uma única reunião** — configurado e suportado pela mesma pessoa que escreve o código.

⚠️ **Contra-ângulo ainda NÃO autorizado pra copy:** a hipótese de que as ferramentas de IA concorrentes entregam "um painel vazio pro cliente configurar sozinho" (o que faria do nosso "a gente configura pra você" o diferencial mais afiado) é **hipótese da Tese, sem dado**. `01-estrategia.md` §8 só documenta que a concorrência BR compete em "custa menos que humano", com visual gradiente azul-roxo e ícone de robô. **Validar com o Radar (módulo 28) antes de virar headline comparativa** — pendência nº 5.

**Os 3 pilares traduzidos pra hierarquia desta página** (`01-estrategia.md` §5):

| Pilar | O que esta página mostra |
|---|---|
| Rápido de verdade | Prazo fechado de 5 dias, com os 3 passos de ativação nomeados e visíveis |
| Engenharia, não slide | O agente atende **lead real**, não demo — e você lê as conversas. "Testado — não prometido" é literalmente a oferta aqui |
| Você não paga pra descobrir se funciona | Levado ao extremo: não paga, não agenda, não fala com vendedor, e no fim não precisa cancelar nada |

**Arquétipos aplicados:**
- **Mágico** — o momento da transformação é o **log de conversa real** que o agente resolveu enquanto o dono dormia. Demonstrado, nunca afirmado. Zero ícone de robô (`01-estrategia.md` §8).
- **Cara Comum** — inegociável nesta página, justamente porque não há reunião: o Lucas aparece como pessoa, autor do código e canal de suporte durante o trial. Zero "nossa equipe", zero linguagem corporativa.

**Léxico obrigatório** (`business.json`): vértice · construímos · roda sozinho · responde em [tempo] · mecanismo · fluxo · **testado — não prometido** · entrega. Liderar sempre com **"agente de IA"**; "CRM" entra como item incluído, nunca como produto principal.

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
4. trial concluído → plano pago (Plano 1 ou Plano 2)

**Não é métrica de sucesso:** tráfego, tempo na página, nº de cadastros, página estar bonita ou publicada (`identidade-web-os.md`, definição de sucesso).

**Baseline: não existe.** Nenhuma landing page da marca rodou com histórico de conversão, e esta oferta é nova. A primeira execução **define** a linha de base. **Nenhuma meta numérica neste brief** — qualquer número aqui seria inventado (regra de veracidade do Web OS). Meta só após o primeiro ciclo medido pelo Mede (módulos 33–36).

**Números permitidos na página — e só estes:**
- **5 dias** (duração do trial, fechada)
- **R$ 2.500 de entrada + R$ 500/mês** (Plano 1) · **R$ 3.200 de entrada + R$ 700/mês** (Plano 2) — sempre com setup e recorrência juntos no mesmo bloco; exibir a entrada sozinha esconde o custo real e queima a honestidade da marca
- 5–50 funcionários (recorte de ICP)
- Âncoras de `_context/marca.md`: SDR CLT júnior ~R$ 3.800–4.200/mês · 10 leads perdidos por demora = R$ 3.000–15.000/mês (ticket R$ 300–1.500) — como cálculo, não slogan
- "responde em segundos" (formulação da fonte, `02-oferta.md` §4)
- Preço redondo, sem "R$ 2.497" (`02-oferta.md` §3: a marca é sóbria, não vende impulso)

**Números proibidos na página:**
- Qualquer resultado de cliente, depoimento, nº de clientes atendidos, nº de trials rodados (não existe prova social própria ainda)
- Tempo de ativação ("rodando em X minutos") — **não medido**, ver pendência nº 7
- "De 4h de triagem manual pra 15 minutos" e "responde em 30 segundos" — são **exemplos de tom de voz** em `01-estrategia.md` §6, **não resultados medidos**
- Garantia de ≥30% ou devolução — pertencia à Piloto Vértice, que esta oferta substituiu; destino em aberto (pendência nº 10)
- R$ 1.900 / R$ 900 (Piloto Vértice e Programa Fundador) — oferta descontinuada como entrada, não pode aparecer

---

## 8. Pendências (não estimar, não decidir por conta própria)

Numeração preservada da V1 do brief, pra quem já leu. Pendências 1, 3 e 4 foram resolvidas pelo Lucas em 2026-10-12 (ver "Decisões fechadas" abaixo).

| # | Pendência | Dono | O que bloqueia |
|---|---|---|---|
| **2** | **Nome e slug definitivos** da oferta e do projeto. Lucas, 2ª rodada: "depois a gente pensa no nome do projeto" — recusou escolher entre Agente Vértice / Vértice 5 Dias / Vértice Ativo. Slug `trial-vertice` segue provisório; copy usa `[nome pendente]` | **Lucas** | Pasta do projeto, URL, tracking, `memory.md`, `"name"` em `config/business.json` (hoje placeholder). **Decidir antes do módulo 22** — renomear depois do build é retrabalho em cadeia |
| **5** | **Dado de concorrência:** como as landing pages concorrentes (Bluelephant, Toolzz, Essent.IA, MelhorAgencia.ai, Intelecta — nomes de `01-estrategia.md` §8) estruturam oferta, trial e preço. Nenhum dado de página coletado. **Inclui validar a hipótese do "painel vazio"** (§6) | **Radar, módulo 28 (Sprint 3)** | Contra-ângulo, bloco de comparação e qualquer headline comparativa |
| **6** | **Política de dados e desconexão do trial:** o que o agente acessa no WhatsApp/Instagram/CRM, o que acontece com as conversas quando o trial acaba, como o cliente desconecta. Nada disso é conhecido hoje | **Lucas + Blinda (módulos 37–38)** | O bloco que responde a objeção nº 1 da página ("vou conectar o WhatsApp da minha empresa?"). **Não inventar política de dados nem alegação de segurança/LGPD** |
| **7** | **Quem configura o agente durante o trial** (o Lucas manualmente? automatizado?) e **quanto tempo leva** da conexão até o agente responder o primeiro lead | **Lucas** | Honestidade do copy de ativação, promessa de tempo, e saber se "self-service" significa "sem reunião de vendas" ou "sem humano nenhum" — são duas páginas diferentes |
| **8** | *(herdada)* **Divergência de tagline entre as fontes:** `business.json` marca a comercial como "em iteração — candidatos rodada 3"; `01-estrategia.md` §7 dá "Escala sem contratar" como oficial | **Tese + Lucas** | Headline do hero |
| **9** | *(herdada)* **Domínio/URL de destino** não confirmado (`01-estrategia.md` §8: neovertix.com/.com.br/.ai sem DNS, disponibilidade real não verificada) | **Lucas** | Deploy |
| **10** | **NOVA — destino da Garantia Vértice** (≥30% ou devolução total, `02-oferta.md` §2). Ela pertencia à Piloto Vértice, agora descontinuada como entrada. Aposentar de vez, ou redesenhar pra incidir sobre os planos pagos (R$ 2.500 / R$ 3.200 + recorrência)? Lucas não decidiu | **Lucas** | Bloco de reversão de risco **pós-trial** da página (o trial resolve o risco de entrada, não o de assinar um plano com setup de R$ 2.500+). Também bloqueia limpar `02-oferta.md` §2 e o campo de garantia em `business.json` — **nada foi removido dessas fontes** |

### Decisões fechadas em 2026-10-12 (2ª rodada, fonte: Lucas)

1. **Duração: 5 dias** (era "4 ou 7"). Fechado — a página publica 5, não uma faixa.
2. **Preço: entrada + recorrência.** Plano 1 = R$ 2.500 + R$ 500/mês · Plano 2 = R$ 3.200 + R$ 700/mês. Mesmo padrão setup+mensalidade das outras ofertas. **Preço liberado pra página.**
3. **Esta oferta SUBSTITUI a Piloto Vértice** como oferta de entrada. Sincronia já executada (ver abaixo).
4. *Item futuro, sem decisão:* possível acréscimo/upsell pra cliente existente — não entra em página nem em `business.json` até o Lucas definir.

### Sincronia executada (2026-10-12, pela Tese, após a decisão do Lucas)

| Arquivo | O que mudou |
|---|---|
| `config/business.json` | `offers[0]` substituído: Piloto Vértice → esta oferta, com `"name"` em placeholder até a pendência nº 2. `content_goal` atualizado (não cita mais "Piloto Vértice"). `positioning` ajustado no trecho "colocamos o sistema rodando antes de fechar contrato". `notes` registra a substituição |
| `Web OS/_context/icp-web.md` | Linha "Piloto Vértice" da tabela oferta→página trocada pela oferta nova (página de ativação self-service, CTA de trial em vez de demo) |
| `Social mídia IA/_context/marca.md` | Tabela de ofertas e pilar 3 atualizados — **arquivo de outro squad** (produção de conteúdo), tocado porque é a fonte de tom compartilhada e citava a oferta extinta |

**Não alterado de propósito:** `branding/neovertix/02-oferta.md` e `01-estrategia.md` (fonte de verdade da marca; a reescrita da oferta ali depende da pendência nº 10 e de uma passada completa de oferta, não de um patch) e `Social mídia IA/_context/tom-de-voz.md` (seção "Base" só muda por decisão explícita do Lucas).
