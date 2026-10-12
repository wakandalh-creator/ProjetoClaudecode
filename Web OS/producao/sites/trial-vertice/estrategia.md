# Estratégia Web — trial-vertice (slug provisório)

> **Status: projeto real, destinado a ir ao ar.** Substitui e descarta `Web OS/producao/sites/teste-piloto-vertice/` por decisão do Lucas ("o criado não ficou bom, pode desconsiderar") — **nada daquele projeto é reaproveitado**, nem copy, nem specs, nem design.
> Agente: Tese-ext · Módulo: `Web OS/modules/20-business-discovery-estrategia.md` · Data: 2026-10-12 (revisado 3x no mesmo dia — ver §8)
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
| Duração | **5 dias** (fechado) |
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

### Planos pós-trial (fonte: Lucas, direta — confirmado na 2ª rodada)

| Plano | Entrada (setup único) | Recorrência | Escopo |
|---|---|---|---|
| 1 | **R$ 2.500** | **R$ 500/mês** | Agente de IA + CRM incluído (sem redes sociais) |
| 2 | **R$ 3.200** | **R$ 700/mês** | Agente de IA + CRM + redes sociais (Instagram) |

Mesmo padrão setup + mensalidade que a Neovertix já pratica na linha Vértice (`02-oferta.md` §3: setup ancora a construção, mensalidade ancora manutenção e iteração) — coerência de empresa, não pertencimento à linha. **Preço liberado pra publicação na página.**

**Item futuro (não é decisão, não bloqueia nada):** o Lucas vai avaliar depois um possível acréscimo/upsell pra quem já é cliente. Sem definição — não aparece na página.

### Regras de veracidade específicas desta página (`identidade-web-os.md`)

- **Sobre a Bolten:** a documentação da Bolten **não menciona trial nativo**. O período grátis é decisão comercial da Neovertix por cima da ferramenta. A página **nunca** pode sugerir que o trial é recurso da plataforma, nem afirmar qualquer capacidade da Bolten além de: CRM white-label, agente de IA treinável, WhatsApp (QR Code ou Cloud API oficial), Meta/Instagram (Conversions API).
- **White-label significa marca Neovertix na frente.** A página não precisa (nem deve, sem decisão do Lucas) citar a Bolten como fornecedor.
- **Um mecanismo de prova por página — a Garantia Vértice não entra aqui.** A garantia de ≥30% ou devolução total (`02-oferta.md` §2) é o mecanismo de reversão de risco **da linha Vértice**, que é paga. Este produto nunca a teve e não a herda: num trial grátis, "devolução total" não significa nada, e o próprio trial já é a reversão de risco. Os dois mecanismos **coexistem na empresa** sem problema (produtos distintos podem ser anunciados em paralelo), mas **nunca na mesma página** — juntos, confundem. Nada em `02-oferta.md` muda por causa deste brief.

---

## 3. ICP

**ICP próprio deste produto, definido pelo Lucas** (2026-10-12). `Web OS/_context/icp-web.md` mapeia oferta→página **da linha Vértice** e **não** é fonte aqui — este produto tem ICP próprio e nada do que segue vai pra `icp-web.md`.

⚠️ **Definido ≠ validado.** O alvo abaixo é decisão do dono do negócio, não resultado de campanha: **nenhuma conversão real testou esse recorte ainda**. Tratar como alvo de trabalho, não como ICP comprovado (pendência nº 11, reduzida à validação em campanha).

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

**Hipótese criador/infoprodutor — descartada pelo Lucas.** Eu havia levantado que o Plano 2 (com Instagram) teria afinidade com criador/infoprodutor; o alvo definido é PME/comércio local. **Não construir a página para criador.**

**Fora do ICP desta página:** quem não tem volume de lead (não tem o que o agente atender) e quem não pode/não quer conectar o canal oficial da empresa (a oferta não funciona sem isso — não tentar convencer esse perfil na copy, é desperdício de página).

**Canal de aquisição (nota de distribuição, não é ICP — insumo pro Multiplica/módulo 27):** começa pelas **postagens do Instagram do Lucas**, com possível migração pro **TikTok** depois. Consequência prática pra esta página: o tráfego da V1 é **morno e founder-led** (gente que já viu o Lucas falar), não frio de busca — a página pode contar com algum reconhecimento prévio, mas não pode depender dele.

### Objeções que a página é obrigada a responder

Herdadas do público já mapeado pela Neovertix (`01-estrategia.md` §3 + `02-oferta.md` §5) — válidas aqui porque a dor de origem é a mesma:
1. **"IA soa robótica"** → no trial não é demo: é o seu lead real conversando. Você lê as conversas que o agente resolveu.
2. **"Agência nova, sem case"** → o trial é a prova. Você não paga pra descobrir — nem com cartão, nem com reunião.
3. **"Quanto tempo até funcionar"** → prazo fechado de 5 dias.
4. **"Se quebrar, quem conserta"** → quem escreve o código é quem responde (Cara Comum, `01-estrategia.md` §4).

**Novas, criadas pelo próprio mecanismo desta oferta** (derivadas do fato "ativação exige conectar WhatsApp/Instagram/CRM", não inventadas):

5. **"Vou conectar o WhatsApp da minha empresa numa empresa que eu não conheço?"** — esta é, na leitura da Tese, **a objeção nº 1 desta página**, acima de preço. **Resposta factual (decidida pelo Lucas, 2026-10-12):** cada cliente recebe uma **instância própria**, criada só pra ele, com acesso durante os 5 dias. **Se não der continuidade, a instância é descartada** — sem acesso residual, sem dado guardado além do período de teste. Nada é compartilhado com outro cliente, porque o ambiente não é compartilhado.
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
- A página **não vende IA**. Vende um teste de 5 dias que acaba sozinho.
- **Prova > promessa** (`identidade-web-os.md`): o ativo de prova mais forte disponível é o **log de conversas reais** que o agente resolveu durante o trial — mostrar o formato do que o cliente vai ver, não um dashboard bonito.
- **Reversibilidade é bloco de página, não rodapé.** Agora com conteúdo factual (§3, objeção 5): instância própria, acaba em 5 dias, descartada se não comprar. Mesmo peso visual do CTA.
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
4. trial concluído → plano pago (Plano 1 ou Plano 2)

**Não é métrica de sucesso:** tráfego, tempo na página, nº de cadastros, página estar bonita ou publicada (`identidade-web-os.md`, definição de sucesso).

**Baseline: não existe.** Nenhuma landing page da marca rodou com histórico de conversão, e esta oferta é nova. A primeira execução **define** a linha de base. **Nenhuma meta numérica neste brief** — qualquer número aqui seria inventado (regra de veracidade do Web OS). Meta só após o primeiro ciclo medido pelo Mede (módulos 33–36).

**Números permitidos na página — e só estes:**
- **5 dias** (duração do trial, fechada)
- **R$ 2.500 de entrada + R$ 500/mês** (Plano 1) · **R$ 3.200 de entrada + R$ 700/mês** (Plano 2) — sempre com setup e recorrência juntos no mesmo bloco; exibir a entrada sozinha esconde o custo real e queima a honestidade da marca
- **5 dias** e os nomes dos verticais do ICP (clínica, concessionária, imobiliária, advocacia, comércio local) — ditos pelo Lucas. **"5–50 funcionários" sai:** esse recorte é da linha Vértice, não deste produto, cujo alvo é "comércio local e pequenas empresas em geral" sem faixa de headcount declarada
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

Numeração preservada das versões anteriores do brief, pra quem já leu. Pendências 1, 3 e 4 foram resolvidas e a nº 10 foi **cancelada** (ver abaixo).

| # | Pendência | Dono | O que bloqueia |
|---|---|---|---|
| **2** | **Nome e slug definitivos** do produto e do projeto. Lucas: "depois a gente pensa no nome do projeto" — não escolheu entre os candidatos sugeridos. Slug `trial-vertice` segue provisório; a copy usa `[nome pendente]`. **O nome não precisa usar "vértice"** (não é produto da linha Vértice — ver §6) | **Lucas** | Pasta do projeto, URL, tracking, `memory.md`, hero da página. **Decidir antes do módulo 22** — renomear depois do build é retrabalho em cadeia |
| **5** | **Dado de concorrência:** como as landing pages concorrentes (Bluelephant, Toolzz, Essent.IA, MelhorAgencia.ai, Intelecta — nomes de `01-estrategia.md` §8) estruturam oferta, trial e preço. Nenhum dado de página coletado. **Inclui validar a hipótese do "painel vazio"** (§6) | **Radar, módulo 28 (Sprint 3)** | Contra-ângulo, bloco de comparação e qualquer headline comparativa |
| **6** | **Política de dados e desconexão do trial:** o que o agente acessa no WhatsApp/Instagram/CRM, o que acontece com as conversas quando o trial acaba, como o cliente desconecta. Nada disso é conhecido hoje | **Lucas + Blinda (módulos 37–38)** | O bloco que responde a objeção nº 1 da página ("vou conectar o WhatsApp da minha empresa?"). **Não inventar política de dados nem alegação de segurança/LGPD** |
| **7** | **Quem configura o agente durante o trial** (o Lucas manualmente? automatizado?) e **quanto tempo leva** da conexão até o agente responder o primeiro lead | **Lucas** | Honestidade do copy de ativação, promessa de tempo, e saber se "self-service" significa "sem reunião de vendas" ou "sem humano nenhum" — são duas páginas diferentes |
| **8** | *(herdada)* **Divergência de tagline entre as fontes:** `business.json` marca a comercial como "em iteração — candidatos rodada 3"; `01-estrategia.md` §7 dá "Escala sem contratar" como oficial | **Tese + Lucas** | Headline do hero |
| **9** | *(herdada)* **Domínio/URL de destino** não confirmado (`01-estrategia.md` §8: neovertix.com/.com.br/.ai sem DNS, disponibilidade real não verificada) | **Lucas** | Deploy |
| **11** | **NOVA — ICP não validado para este produto.** O ICP de §3 é **inferido** do público geral da Neovertix; não existe ICP validado para este produto independente, e `icp-web.md` (linha Vértice) não serve como fonte. Um trial self-service com conexão técnica de canal pode atrair perfil diferente do que a venda assistida atrai | **Lucas** | Confirmar a quem a página fala (dono de PME? criador/infoprodutor, dada a afinidade do Plano 2 com Instagram?). Afeta copy, objeções e canal de tráfego. **Se este produto ganhar ICP próprio, ele precisa de `_context` próprio — não encaixar em `icp-web.md`** |

### Decisões fechadas em 2026-10-12 (fonte: Lucas)

1. **Duração: 5 dias** (era "4 ou 7"). Fechado — a página publica 5, não uma faixa.
2. **Preço: entrada + recorrência.** Plano 1 = R$ 2.500 + R$ 500/mês · Plano 2 = R$ 3.200 + R$ 700/mês. **Liberado pra página.**
3. **Linha de produto: independente** (3ª rodada, corrige a leitura anterior de "substitui a Piloto Vértice"). Mesma empresa — Neovertix —, produtos diferentes: linha Vértice (implementação sob medida), Web OS (criação automática de sites/landing pages) e **este produto** (agente de IA + CRM + redes sociais, via Bolten). **Não substitui, não se funde, não herda a Garantia Vértice.** Agregar à linha Vértice no futuro é decisão do Lucas.
4. *Item futuro, sem decisão:* possível acréscimo/upsell pra cliente existente.
5. **Pendência nº 10 CANCELADA** ("destino da Garantia Vértice"): ela nasceu da leitura errada de substituição. Este produto nunca teve essa garantia — não há nada pra aposentar nem redesenhar. A garantia continua sendo da linha Vértice, intacta.

### Nenhuma fonte de marca foi alterada por este brief

Nada em `config/business.json`, `Web OS/_context/icp-web.md`, `Social mídia IA/_context/marca.md`, `branding/neovertix/*` ou `tom-de-voz.md` muda por causa deste produto. Uma sincronia chegou a ser feita na 2ª rodada (quando a leitura era "substitui a Piloto Vértice") e **foi revertida** ao baseline. Se/quando o Lucas decidir agregar este produto à linha Vértice, a Tese faz o registro — não antes.

**O que continua herdado da marca Neovertix** (é a mesma empresa): posicionamento, voz, arquétipos Mágico + Cara Comum, léxico e palavras banidas, âncoras de custo (`02-oferta.md` §3) e a direção visual de `01-estrategia.md` §8.
