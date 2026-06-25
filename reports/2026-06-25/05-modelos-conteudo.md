# Modelos de Conteúdo — 2026-06-25

## Nota de metodologia

Como nos Módulos 4, esta análise depende apenas de dados já coletados e verificados nos Módulos 2 (`02-perfis-instagram.md`) e 3 (`03-benchmark.md`), cruzados com `config/business.json` — não há busca de fatos externos nova, então foi feita diretamente nesta sessão em vez de via sub-agentes paralelos (mesmo princípio aplicado no Módulo 4). Cada conteúdo confirmado (hook citado literalmente, não inferência fraca) foi classificado em um dos 10 modelos candidatos do briefing; quando um padrão recorrente não se encaixava em nenhum dos 10, um novo modelo foi criado — isso aconteceu duas vezes (`demonstracao_ferramenta` e `reacao_lancamento`), ambos já documentados como frameworks no Módulo 4. Conteúdos marcados como `limitacao_dados` no Módulo 2 (sem hook exato confirmado) não foram classificados, para não inflar artificialmente a frequência de nenhum modelo.

## Seção 1 — Ranking dos 10 Modelos

### #1 — demonstracao_ferramenta

**Descrição:** Mostra uma ferramenta de IA (própria ou de terceiros) em uso, do prompt/input ao resultado, geralmente terminando em CTA de baixo atrito.
**Frequência nos dados:** 10 conteúdos (@chase.h.ai 1, @leosoares.ia 1, @geracaotechs 5, @gabriel.adamuchi 2, @nathanhodgson.ai 1)
**Taxa de performance:** Alta — 4 dos 5 itens deste modelo no Top 10 do Módulo 3 (#1, #3, #7, #8, #10)
**Perfis que mais usam:** @geracaotechs, @chase.h.ai, @leosoares.ia, @gabriel.adamuchi, @nathanhodgson.ai
**Contexto ideal:** Quando há uma ferramenta/agente real para mostrar (monitor de tendências, instagram-content-cloner, qualquer automação construída com Claude Code) e o objetivo é gerar prova de capacidade + leads de baixo atrito.
**Facilidade de produção:** Fácil
**Potencial para o negócio:** Alto — Lucas já tem múltiplas ferramentas reais (este próprio monitor, instagram-content-cloner) prontas para demonstrar sem precisar inventar nada.

**Hook de exemplo:**
> "Eu pedi pro Claude Code construir um agente que monitora 16 perfis de IA no Instagram e me manda o relatório todo dia. Olha o que ele encontrou hoje 👇"

**Estrutura:**
1. Mostrar a ferramenta/agente rodando (tela ou resultado)
2. Explicar o que ela resolve em uma frase
3. CTA de palavra-chave em comentário ou DM para acesso/replicação

---

### #2 — lista_checklist

**Descrição:** Entrega de uma lista numerada/nomeada de itens de valor (ferramentas, prompts, recursos) via CTA de comentário.
**Frequência nos dados:** 3 conteúdos (@charliehills "8 personalidades ocultas do ChatGPT", @leosoares.ia "IA7", @laschuk "5 modelos de email")
**Taxa de performance:** Alta — item mais forte (@leosoares.ia "IA7") confirmado como Top 10 #2 (Alto)
**Perfis que mais usam:** @leosoares.ia, @charliehills, @laschuk
**Contexto ideal:** Quando Lucas tem um recurso compilável (lista de skills, prompts, ferramentas) entregável rapidamente por DM — ideal para construir lista de leads no início da jornada de autoridade.
**Facilidade de produção:** Fácil
**Potencial para o negócio:** Alto — mecanismo comprovadamente eficaz e barato de produzir; alinhado ao objetivo de "aquisição de clientes" de `config/business.json`.

**Hook de exemplo:**
> "O Claude Code tem 7 skills nativas que praticamente ninguém usa. Comenta 'SKILLS' que eu mando a lista completa."

**Estrutura:**
1. Prometer um número específico de itens de valor
2. Mostrar 1-2 exemplos rápidos na tela
3. CTA "Comenta [PALAVRA] que mando o resto por DM"

---

### #3 — trend_adaptada

**Descrição:** Conteúdo que monta sobre uma tendência cultural ou tecnológica em alta (ex.: "todo mundo só fala de Claude", prompts sazonais) e adapta ao nicho.
**Frequência nos dados:** 3 conteúdos (@gabriel.adamuchi guia Claude + prompt de Natal, @geracaotechs "bonequinho"/action figure)
**Taxa de performance:** Alta — item confirmado no Top 10 #7 (Médio-Alto, @gabriel.adamuchi)
**Perfis que mais usam:** @gabriel.adamuchi, @geracaotechs
**Contexto ideal:** Quando um tema (ferramenta, meme, formato visual) está em alta no momento e pode ser conectado à proposta de Lucas sem forçar.
**Facilidade de produção:** Média — exige monitorar constantemente o que está em alta.
**Potencial para o negócio:** Alto — Lucas já tem o monitor de tendências (Módulo 1) rodando todo dia, o que reduz drasticamente a dificuldade real desse modelo especificamente para ele.

**Hook de exemplo:**
> "Esse fim de semana todo mundo tá testando o Nano Banana 2. Eu testei integrado com Claude Code — olha o que rolou."

**Estrutura:**
1. Identificar a trend do momento (via monitor)
2. Conectar a um uso prático de IA/automação
3. CTA de comentário ou link na bio

---

### #4 — storytelling

**Descrição:** Narrativa pessoal com abertura contraintuitiva/filosófica, desenvolvimento de argumento e fechamento reflexivo.
**Frequência nos dados:** 2 conteúdos (@leandroladeiran)
**Taxa de performance:** Alta — confirmado no Top 10 #5 (Alto), sustentado por ~2M seguidores e GPTs de terceiros replicando o método do autor
**Perfis que mais usam:** @leandroladeiran
**Contexto ideal:** Funciona melhor com audiência e prova social já estabelecidas — gera identificação genuína, mas depende de confiança prévia do público no autor.
**Facilidade de produção:** Difícil — exige tom de voz e persona consolidados, que Lucas ainda está construindo (posicionamento "em definição" em `business.json`).
**Potencial para o negócio:** Baixo (por ora) — conforme já identificado no Módulo 4, esse formato deve ser guardado para uma fase futura, quando Lucas já tiver audiência e autoridade construídas.

**Hook de exemplo (guardado para fase futura):**
> "Passei meses tentando 'achar meu nicho' em IA. Só descobri quando parei de procurar um nicho e comecei a documentar o que eu já fazia todo dia."

**Estrutura:**
1. Abertura contraintuitiva/filosófica
2. Argumento pessoal desenvolvido
3. Fechamento com reflexão/lição

---

### #5 — reacao_lancamento

**Descrição:** Reação rápida (24-48h) a um lançamento de ferramenta de IA relevante, capitalizando o timing/FOMO do momento (newsjacking).
**Frequência nos dados:** 1 conteúdo (@charliehills, lançamento Nano Banana 2)
**Taxa de performance:** Alta — confirmado no Top 10 #6 (Médio-Alto)
**Perfis que mais usam:** @charliehills
**Contexto ideal:** Toda vez que uma ferramenta de IA relevante ao nicho lança algo novo — quanto mais rápida a reação, maior o ganho de distribuição orgânica.
**Facilidade de produção:** Média — exige monitoramento ativo de lançamentos.
**Potencial para o negócio:** Alto — vantagem direta e replicável via o próprio monitor de tendências do Módulo 1, que já rastreia esses lançamentos automaticamente.

**Hook de exemplo:**
> "Saiu uma ferramenta nova de IA hoje e meu sistema de monitoramento já me avisou antes da maioria. Olha o que ela faz."

**Estrutura:**
1. Monitorar lançamentos relevantes ao nicho
2. Publicar reação + demonstração nas primeiras 24-48h
3. Implicar a mudança de cenário para o público

---

### #6 — tutorial_rapido

**Descrição:** "Como fazer X" em poucos passos, demonstrando uma técnica ou prompt específico.
**Frequência nos dados:** 1 conteúdo (@leandroladeiran, "Como ficar bom de copy")
**Taxa de performance:** Alta — sinal indireto forte (~2M seguidores, método replicado por GPTs de terceiros)
**Perfis que mais usam:** @leandroladeiran
**Contexto ideal:** Quando Lucas quer construir autoridade prática mostrando exatamente como fazer algo replicável (prompt, configuração, skill).
**Facilidade de produção:** Fácil — Lucas já documenta prompts e skills que usa no dia a dia.
**Potencial para o negócio:** Alto — alinhado ao tom "direto, prático, orientado a resultados, sem jargão técnico desnecessário" do posicionamento de Lucas.

**Hook de exemplo:**
> "Como configurar seu primeiro agente de IA com Claude Code em 3 passos (sem programar)."

**Estrutura:**
1. Prometer um resultado específico em N passos
2. Demonstrar cada passo rapidamente
3. CTA para o prompt/skill completo

---

### #7 — case_real

**Descrição:** Apresentação de um resultado de negócio real (próprio ou de cliente) como prova social.
**Frequência nos dados:** 1 conteúdo (@oneyaraujo, "Código Viral", "+63.000 alunos")
**Taxa de performance:** Alta — confirmado no Top 10 #4 (Alto)
**Perfis que mais usam:** @oneyaraujo
**Contexto ideal:** Quando há um resultado quantificável para mostrar — funciona melhor com prova social já acumulada.
**Facilidade de produção:** Média — Lucas ainda não tem casos de clientes pagantes documentados, mas pode usar o próprio sistema (este monitor) como case inicial.
**Potencial para o negócio:** Médio — alto valor de conversão, mas limitado hoje pela falta de cases externos; deve crescer conforme Lucas adquire os primeiros clientes/projetos (objetivo "aquisição de clientes" de `business.json`).

**Hook de exemplo:**
> "Esse sistema de monitoramento que eu construí com Claude Code já gerou relatórios completos de mercado todos os dias sem eu precisar abrir o Instagram uma vez. Resultado real, não teoria."

**Estrutura:**
1. Apresentar o resultado numérico/tangível
2. Explicar brevemente como foi alcançado
3. CTA para replicar ou contratar

---

### #8 — erro_comum

**Descrição:** Revela um erro ou crença equivocada comum no nicho, geralmente sobre um tema técnico ou de algoritmo.
**Frequência nos dados:** 4 conteúdos (@oneyaraujo 2, @laschuk 1, @amandadinizmkt 1)
**Taxa de performance:** Média — nenhum item deste modelo foi confirmado diretamente no Top 10; sinal indireto via porte de conta de @oneyaraujo (~2M seguidores)
**Perfis que mais usam:** @oneyaraujo, @laschuk, @amandadinizmkt
**Contexto ideal:** Quando existe uma crença equivocada específica e comum no público-alvo de Lucas (ex.: "preciso saber programar para ter um agente de IA").
**Facilidade de produção:** Média — exige identificar um mito específico e validado, não genérico.
**Potencial para o negócio:** Médio — útil para construir autoridade ao corrigir uma crença, mas exige mais cuidado de pesquisa para não soar genérico.

**Hook de exemplo:**
> "Todo mundo acha que precisa saber programar pra ter um agente de IA trabalhando por você. Não precisa — e eu vou te mostrar o porquê."

**Estrutura:**
1. Apresentar a crença comum equivocada
2. Explicar por que está errada com um exemplo prático
3. Mostrar o caminho correto + CTA

---

### #9 — opiniao_forte

**Descrição:** Posicionamento direto e polarizador sobre um tema do nicho (ex.: comparação entre tecnologias/abordagens).
**Frequência nos dados:** 1 conteúdo (@oneyaraujo)
**Taxa de performance:** Média — sem confirmação direta no Top 10
**Perfis que mais usam:** @oneyaraujo
**Contexto ideal:** Quando Lucas já tiver um ponto de vista consolidado para defender — pode ajudar a "descobrir posicionamento" (objetivo de `business.json`), mas com risco se a opinião não for genuína/consistente.
**Facilidade de produção:** Média — exige confiança para se posicionar publicamente.
**Potencial para o negócio:** Médio — pode acelerar a definição de posicionamento, mas é arriscado sem uma persona já consolidada.

**Hook de exemplo:**
> "Claude Code não é só 'mais um' assistente de código. É a diferença entre automatizar uma tarefa e automatizar um negócio. E quase ninguém tá usando assim."

**Estrutura:**
1. Afirmação direta e polarizadora
2. Argumento de sustentação
3. Convite à discussão nos comentários

---

### #10 — bastidores

**Descrição:** Mostra o processo real de construção/rotina por trás de um projeto ou ferramenta.
**Frequência nos dados:** 1 conteúdo (@amandadinizmkt, "nona edição da minha imersão")
**Taxa de performance:** Baixa — nenhum sinal de performance confirmável nos dados coletados (perfil sem seguidores/posts confirmados)
**Perfis que mais usam:** @amandadinizmkt
**Contexto ideal:** Quando Lucas quer gerar autenticidade mostrando o processo de construção do próprio sistema/monitor, sem precisar de produção elaborada.
**Facilidade de produção:** Fácil — é só registrar o processo real já em andamento.
**Potencial para o negócio:** Alto — apesar da performance baixa nos dados coletados (que reflete falta de dados sobre o único perfil observado, não um sinal negativo confirmado), esse modelo tem potencial alto especificamente para Lucas: ele já está construindo algo real (este monitor) que pode ser documentado organicamente como subproduto do trabalho, ajudando a "descobrir posicionamento" via prova de processo em vez de teoria.

**Hook de exemplo:**
> "Bastidores de como eu construí o sistema que gera meus relatórios de tendências automaticamente — do primeiro prompt até funcionar de ponta a ponta."

**Estrutura:**
1. Mostrar o ponto de partida/problema
2. Registrar o processo de construção (decisões, tentativas, prints)
3. Mostrar o resultado final funcionando

## Seção 2 — Matriz de Decisão

|  | Alta Performance | Média Performance | Baixa Performance |
|--|-----------------|-------------------|-------------------|
| **Fácil** | Fazer agora — `demonstracao_ferramenta`, `lista_checklist`, `tutorial_rapido` | — | Deprioritizar* — `bastidores` |
| **Médio** | Planejar — `trend_adaptada`, `reacao_lancamento`, `case_real` | Avaliar — `erro_comum`, `opiniao_forte` | — |
| **Difícil** | Investir quando escalar — `storytelling` | — | — |

\* **Exceção a registrar:** `bastidores` está na célula "Deprioritizar" apenas porque os dados coletados não permitem confirmar sua performance (não porque tenha sinal negativo). Dado seu custo de produção quase zero (Lucas só precisa registrar o que já está fazendo), vale testá-lo de forma oportunista mesmo fora da prioridade formal.

## Seção 3 — Recomendação de Sequência

**Para começar, priorize:** `demonstracao_ferramenta` → `lista_checklist` → `tutorial_rapido`

**Justificativa:** os três modelos caem na célula "Fácil + Alta Performance" da matriz — Lucas já possui as ferramentas reais (este monitor, instagram-content-cloner, skills do Claude Code) e os prompts/processos para produzir esse conteúdo imediatamente, sem depender de autoridade ainda não construída ou de timing externo. Juntos, cobrem o objetivo central de `config/business.json` ("descobrir posicionamento + construir autoridade + aquisição de clientes") com o menor atrito possível: `demonstracao_ferramenta` mostra capacidade real, `lista_checklist` converte essa capacidade em leads, e `tutorial_rapido` consolida autoridade prática.

**Em seguida:** `trend_adaptada` e `reacao_lancamento` — ambos de dificuldade média, mas com potencial alto especificamente para Lucas por já ter o monitor de tendências (Módulo 1) como vantagem estrutural sobre outros criadores que precisariam pesquisar manualmente. `case_real` entra no mesmo momento, evoluindo de "mostrar o próprio sistema" para "mostrar resultados de clientes" assim que os primeiros forem conquistados.

**Por último:** `erro_comum` e `opiniao_forte` (exigem mais cuidado de pesquisa/posicionamento antes de produzir em escala) e `storytelling` (guardado para uma fase futura, quando Lucas já tiver audiência e prova social suficientes para sustentar o tom de vulnerabilidade reflexiva — conforme já recomendado no Módulo 4). `bastidores` pode ser produzido de forma oportunista em paralelo, dado seu custo quase nulo.
