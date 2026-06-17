# Modelos de Conteúdo — 2026-06-17

**Nota de escopo:** modelos detectados a partir dos conteúdos classificados nos Módulos 2-4 (amostra de 15 perfis, com hooks confirmados apenas em @nick_saraev e @charliehills). Apenas 6 dos 10 modelos candidatos da lista oficial foram detectados nos dados reais coletados — `storytelling`, `antes_depois`, `bastidores` e `trend_adaptada` não apareceram na amostra e não foram inventados aqui (a pesquisa de tendências do Módulo 1 indica que `trend_adaptada` é um formato forte no mercado em geral — POV, micro-story loop, transformation reveal — mas sem instância confirmada nos perfis monitorados).

## Seção 1 — Ranking dos Modelos Detectados

### #1 — opiniao_forte

**Descrição:** Posicionamento polarizador sobre um tema do nicho — nomeia uma tendência de mercado ou contraria uma crença popular.
**Frequência nos dados:** 2 conteúdos
**Taxa de performance:** Alta
**Perfis que mais usam:** @nick_saraev, @charliehills
**Contexto ideal:** construir autoridade rápido e gerar comentários/discussão; ideal para a fase de "descobrir posicionamento" em que o Lucas está.
**Facilidade de produção:** Fácil
**Potencial para o negócio:** Alto — alinhado diretamente ao `content_goal` "construir autoridade" e ao tom "direto, prático" de `config/business.json`

**Hook de exemplo:**
> "Claude Code não vai automatizar seu negócio sozinho. Quem automatiza é quem sabe pedir certo."

**Estrutura:**
1. Citar a crença popular → 2. Negar/contrastar diretamente → 3. Revelar a verdade prática

---

### #2 — case_real

**Descrição:** Resultado de um projeto ou processo real, com nome próprio e métrica concreta.
**Frequência nos dados:** 1 conteúdo
**Taxa de performance:** Alta
**Perfis que mais usam:** @nick_saraev
**Contexto ideal:** prova social; bom para a fase de aquisição de clientes, quando já existe um resultado real para mostrar.
**Facilidade de produção:** Média — exige ter (ou documentar) um resultado real antes de gravar
**Potencial para o negócio:** Alto — Lucas já tem um case real pronto: o próprio sistema de monitoramento (`monitor/`) rodando no Claude Code

**Hook de exemplo:**
> "O sistema que monitora 50+ perfis de IA e me entrega o relatório de conteúdo pronto toda semana, sem eu abrir uma aba."

**Estrutura:**
1. Nomear o sistema/processo → 2. Mostrar o resultado numérico → 3. Convidar a audiência a replicar

---

### #3 — pov

**Descrição:** Ponto de vista pessoal sobre uma possibilidade ou tendência, geralmente em forma de pergunta retórica.
**Frequência nos dados:** 1 conteúdo
**Taxa de performance:** Alta
**Perfis que mais usam:** @charliehills
**Contexto ideal:** ativar um desejo (ex: escalar sem esforço) antes de apresentar a solução.
**Facilidade de produção:** Fácil
**Potencial para o negócio:** Alto — encaixa bem no público de "empreendedores que querem escalar com IA" (`target_audience`)

**Hook de exemplo:**
> "Quer que seu conteúdo do Instagram já venha pronto toda segunda de manhã, sem você abrir uma aba?"

**Estrutura:**
1. Pergunta retórica ligada a um desejo → 2. Resposta com o mecanismo (automação/agente) → 3. CTA

---

### #4 — lista_checklist

**Descrição:** Lista de recursos, passos ou itens essenciais — inclui variações de CTA tipo "comenta X" para receber a lista.
**Frequência nos dados:** 3 conteúdos
**Taxa de performance:** Média (1 alto + 2 médio)
**Perfis que mais usam:** @nick_saraev, @charliehills
**Contexto ideal:** geração de lead/captura de contato; bom para construir lista de interessados.
**Facilidade de produção:** Fácil
**Potencial para o negócio:** Alto — fácil de implementar e gera lead direto

**Hook de exemplo:**
> "Comenta 'AGENTE' que eu te mando o prompt exato que uso pra criar agentes no Claude Code."

**Estrutura:**
1. Prometer recurso de valor → 2. Pedir comentário de palavra-chave específica → 3. Entregar via DM automatizada

---

### #5 — erro_comum

**Descrição:** Aponta um erro ou risco comum que a audiência comete ou desconhece.
**Frequência nos dados:** 2 conteúdos
**Taxa de performance:** Média
**Perfis que mais usam:** @charliehills
**Contexto ideal:** gerar urgência/atenção quando há um caso técnico real para sustentar (ex: segurança de agentes/MCP).
**Facilidade de produção:** Média — exige profundidade técnica para não soar vazio
**Potencial para o negócio:** Médio — fortalece autoridade técnica, mas só funciona com conhecimento real por trás

**Hook de exemplo:**
> "Seu agente de Claude Code tá conectado ao CRM do seu cliente? Então ele pode vazar tudo se você não fizer isso."

**Estrutura:**
1. Afirmar o poder da ferramenta → 2. "até que" revela o risco oculto → 3. Solução/mitigação

---

### #6 — tutorial_rapido

**Descrição:** Promessa de dominar uma habilidade ou processo através de um método nomeado.
**Frequência nos dados:** 1 conteúdo
**Taxa de performance:** Média
**Perfis que mais usam:** @nick_saraev
**Contexto ideal:** funciona melhor quando já existe alguma autoridade construída/prova social prévia.
**Facilidade de produção:** Média
**Potencial para o negócio:** Médio — Lucas ainda está construindo autoridade; funciona melhor com foco no método do que no nome próprio

**Hook de exemplo:**
> "O método que uso pra criar um agente de monitoramento em menos de 1 hora com Claude Code."

**Estrutura:**
1. Prometer domínio de uma habilidade → 2. Mostrar o método em passos → 3. CTA

---

## Seção 2 — Matriz de Decisão

|  | Alta Performance | Média Performance | Baixa Performance |
|--|-----------------|-------------------|-------------------|
| **Fácil** | opiniao_forte, pov — Fazer agora | lista_checklist — Testar | — |
| **Médio** | case_real — Planejar | erro_comum, tutorial_rapido — Avaliar | — |
| **Difícil** | — | — | — |

*Nenhum modelo de dificuldade "Difícil" foi detectado nos dados desta amostra.*

## Seção 3 — Recomendação de Sequência

**Para começar, priorize: opiniao_forte → pov → lista_checklist → case_real → erro_comum / tutorial_rapido**

Justificativa: os três primeiros são fáceis de produzir e têm alta (ou média-alta) performance, servindo para validar posicionamento rápido sem exigir produção elaborada ou case prévio. `case_real` vem em seguida porque exige só organizar uma prova social que o Lucas já tem (o próprio monitor). `erro_comum` e `tutorial_rapido` ficam para depois, pois dependem de mais profundidade técnica ou autoridade já construída para não soarem vazios.
