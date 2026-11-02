# Análise de Perfis Instagram — 2026-11-02

## Nota Metodológica Importante

Esta execução do Módulo 2 rodou em MODO ANÁLISE sobre os 61 perfis ativos de `config/profiles.json`, processados em 13 lotes de até 5 perfis via sub-agentes paralelos (WebSearch + WebFetch), seguindo as regras de segurança do swarm do projeto (batch 5, concorrência 3, anti-alucinação).

**Limitação sistêmica encontrada:** nesta sessão/sandbox, `WebFetch` para `instagram.com` (e para a maioria dos agregadores de terceiros — creatordb.app, imginn.com, hypeauditor.com etc.) falhou com erro de rede (`ENOTFOUND`) em 100% das tentativas — inclusive em domínio neutro de teste, confirmando bloqueio de rede da sessão, não bloqueio específico do Instagram. Toda a coleta foi feita exclusivamente via `WebSearch`. Para a grande maioria dos 61 handles (a maior parte contas pequenas/nicho em português), a busca não indexa posts, captions ou métricas — portanto **61 de 61 perfis** tiveram o campo `limitacao_dados` preenchido, e apenas **2 perfis** (@charliehills e @fabianocarvalhojr) retornaram algum indício real de padrão de conteúdo (via menções de terceiros, não captions literais de Instagram).

**Recomendação para o Lucas:** considerar conectar um MCP/skill de scraping de Instagram autorizado (ex. API oficial, serviço de terceiros com acesso de rede liberado) para que o Módulo 2 tenha dados reais em execuções futuras — nesta sandbox, WebSearch isoladamente não é suficiente para a maioria dos perfis monitorados.

---

## Visão Geral dos Perfis

| Perfil | Categoria | Formato Dominante | Engajamento | Hook Padrão / Status |
|--------|-----------|------------------|-------------|------------------------|
| @charliehills | creator | misto | baixo | paradoxo_contraste |
| @yikC | creator | misto | baixo | dados insuficientes |
| @eujoaotorresz | creator | misto | baixo | dados insuficientes |
| @fabianocarvalhojr | founder | misto | baixo | outro |
| @rafa.grandi | marketing | misto | baixo | dados insuficientes |
| @brusantanna.ai | ia | misto | baixo | dados insuficientes |
| @vendedorglobal | negocio-digital | misto | baixo | dados insuficientes |
| @oluizmain | creator | misto | baixo | dados insuficientes |
| @nick_saraev | automacao | misto | baixo | dados insuficientes |
| @nathanhodgson | ia | misto | baixo | dados insuficientes |
| @ai | ia | misto | baixo | dados insuficientes |
| @ana.gsoares | marketing | misto | baixo | dados insuficientes |
| @chase.h.ai | ia | misto | baixo | dados insuficientes |
| @leosoares.ia | ia | misto | baixo | dados insuficientes |
| @gabriel.adamuchi | creator | misto | baixo | dados insuficientes |
| @viverdeia.ai | ia | misto | baixo | dados insuficientes |
| @ninja.automacoes | automacao | misto | baixo | dados insuficientes |
| @nikolassasso | creator | misto | baixo | dados insuficientes |
| @eduardocavalcanti | founder | misto | baixo | dados insuficientes |
| @jonylan | creator | misto | baixo | dados insuficientes |
| @allesinisgalli | founder | misto | baixo | dados insuficientes |
| @lonamkt | marketing | misto | baixo | dados insuficientes |
| @gabrielbarbosa.oficial | creator | misto | baixo | dados insuficientes |
| @opensession.co | agencia | misto | baixo | dados insuficientes |
| @leandroladeiran | marketing | misto | baixo | dados insuficientes |
| @christiantriad | creator | misto | baixo | dados insuficientes |
| @oneyaraujo | creator | reels | alto | dados insuficientes |
| @geracaotechs | ia | misto | baixo | dados insuficientes |
| @amandadinizmkt | marketing | misto | baixo | dados insuficientes |
| @human___academy | ia | misto | baixo | dados insuficientes |
| @geiss11 | creator | misto | baixo | dados insuficientes |
| @nelmoricalde | creator | misto | baixo | dados insuficientes |
| @rodrigotadewald | marketing | misto | baixo | dados insuficientes |
| @sujeitoprogramador | ia | misto | baixo | dados insuficientes |
| @jonathan_kamargo | creator | misto | baixo | dados insuficientes |
| @marianatorre.s | marketing | misto | baixo | dados insuficientes |
| @marketerhub.ai | marketing | misto | baixo | dados insuficientes |
| @marcelaluzzio | marketing | misto | baixo | dados insuficientes |
| @gestordeaudiencia | marketing | misto | baixo | dados insuficientes |
| @sebintel | ia | misto | baixo | dados insuficientes |
| @avora.ai | agencia | misto | baixo | dados insuficientes |
| @ogabrieeldias | creator | misto | baixo | dados insuficientes |
| @rodrigobindes | founder | misto | baixo | dados insuficientes |
| @franklim.gui | creator | misto | baixo | dados insuficientes |
| @gabrielsamp.ai | ia | misto | baixo | dados insuficientes |
| @maestrosdaia | ia | misto | baixo | dados insuficientes |
| @brandsdecoded__ | marketing | misto | baixo | dados insuficientes |
| @anatex | creator | misto | baixo | dados insuficientes |
| @larissagomes.ia | ia | misto | baixo | dados insuficientes |
| @thiagozaao | creator | misto | baixo | dados insuficientes |
| @neuwebstudio | agencia | misto | baixo | dados insuficientes |
| @laschuk | founder | misto | baixo | dados insuficientes |
| @maestroptompts | ia | misto | baixo | dados insuficientes |
| @faladantasmkt | marketing | misto | baixo | dados insuficientes |
| @lindsay.ia | ia | misto | baixo | dados insuficientes |
| @andrevictor.m | marketing | misto | baixo | dados insuficientes |
| @drisiano | creator | misto | baixo | dados insuficientes |
| @brun0gpt | ia | misto | baixo | dados insuficientes |
| @maxcarrau.ia | ia | misto | baixo | dados insuficientes |
| @noevarner | creator | misto | baixo | dados insuficientes |
| @yikchanltd | creator | misto | baixo | dados insuficientes |

---

## Análise Detalhada por Perfil

### @charliehills

**Categoria:** creator

#### Padrões de Hook identificados
- Modelo: paradoxo_contraste (frequência: alta) — ex: "Linha de abertura curta seguida de uma segunda linha que contradiz/inverte a expectativa criada pela primeira (formato descrito por análise de terceiros do seu conteúdo: 'hook, setup, pivot, steps, insight, CTA')"
- Modelo: outro (frequência: media) — ex: "Hook citando uma ferramenta/nome específico nas primeiras linhas + um número na segunda linha + palavra entre parênteses como '(actually)' — táticas que ele mesmo descreve usar para aumentar alcance"

#### Estrutura típica do conteúdo
```
Hook curto (1-3 linhas, geralmente de contraste/expectativa invertida) -> setup -> virada (pivot) -> passos práticos -> insight -> CTA. Estrutura descrita por análises de terceiros (viralbrain.ai, magicpost.in) sobre o conteúdo dele; ele afirma aplicar a mesma fórmula 'em qualquer plataforma' (LinkedIn, Instagram, X).
```

#### CTA dominante
- Padrão: oferta de recurso/material gratuito

#### Tom de voz
- Adjetivos: direto, didático
- Exemplo de frase característica: ""Stop asking AI to write LinkedIn posts. Do this instead: 1. Mine your voice before you write..." (post atribuído a @charliehills via nota no Substack, não confirmado como post de Instagram)"

#### Métricas estimadas
- Tamanho médio de post educativo: dados insuficientes
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Temas identificados
- IA aplicada a conteúdo e marketing
- estratégia de hooks e viralização
- produtividade e automação com agentes de IA
- construção de audiência com conteúdo gerado por IA

---

### @yikC

**Categoria:** creator

#### Padrões de Hook identificados
- Dados insuficientes — nenhum post real localizado via busca.

#### Estrutura típica do conteúdo
```
dados insuficientes
```

#### CTA dominante
- Padrão: dados insuficientes

#### Tom de voz
- Adjetivos: -

#### Métricas estimadas
- Tamanho médio de post educativo: dados insuficientes
- Formato mais usado: misto
- Engajamento estimado: baixo

---

### @eujoaotorresz

**Categoria:** creator

#### Padrões de Hook identificados
- Dados insuficientes — nenhum post real localizado via busca.

#### Estrutura típica do conteúdo
```
dados insuficientes
```

#### CTA dominante
- Padrão: dados insuficientes

#### Tom de voz
- Adjetivos: -

#### Métricas estimadas
- Tamanho médio de post educativo: dados insuficientes
- Formato mais usado: misto
- Engajamento estimado: baixo

---

### @fabianocarvalhojr

**Categoria:** founder

#### Padrões de Hook identificados
- Modelo: outro (frequência: baixa) — ex: "Post/imagem sobre rodar '7 departamentos de uma empresa dentro do Claude' (citando áreas como desenvolvimento, design, marketing, financeiro e jurídico) — paráfrase de legenda encontrada via busca, não transcrição literal"

#### Estrutura típica do conteúdo
```
Conteúdo demonstrativo/educativo sobre uso de agentes de IA em processos de empresa (ex: departamentos operando dentro de ferramentas de IA como Claude), com oferta de aula gratuita como chamada para ação no perfil. Baseado em poucos indícios encontrados via busca, não em revisão direta do feed.
```

#### CTA dominante
- Padrão: oferta de aula gratuita (link na bio)

#### Tom de voz
- Adjetivos: -

#### Métricas estimadas
- Tamanho médio de post educativo: dados insuficientes
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Temas identificados
- agentes de IA para negócios
- automação de processos empresariais com IA
- aula gratuita sobre IA aplicada a empresas (lasy.ai)

---

### @rafa.grandi

**Categoria:** marketing

#### Padrões de Hook identificados
- Dados insuficientes — nenhum post real localizado via busca.

#### Estrutura típica do conteúdo
```
dados insuficientes
```

#### CTA dominante
- Padrão: dados insuficientes

#### Tom de voz
- Adjetivos: -

#### Métricas estimadas
- Tamanho médio de post educativo: dados insuficientes
- Formato mais usado: misto
- Engajamento estimado: baixo

---

### @brusantanna.ai

**Categoria:** ia

#### Padrões de Hook identificados
- Dados insuficientes — nenhum post real localizado via busca.

#### Estrutura típica do conteúdo
```
dados insuficientes
```

#### CTA dominante
- Padrão: dados insuficientes

#### Tom de voz
- Adjetivos: -

#### Métricas estimadas
- Tamanho médio de post educativo: dados insuficientes
- Formato mais usado: misto
- Engajamento estimado: baixo

---

### @vendedorglobal

**Categoria:** negocio-digital

#### Padrões de Hook identificados
- Dados insuficientes — nenhum post real localizado via busca.

#### Estrutura típica do conteúdo
```
dados insuficientes
```

#### CTA dominante
- Padrão: dados insuficientes

#### Tom de voz
- Adjetivos: -

#### Métricas estimadas
- Tamanho médio de post educativo: dados insuficientes
- Formato mais usado: misto
- Engajamento estimado: baixo

---

### @oluizmain

**Categoria:** creator

#### Padrões de Hook identificados
- Dados insuficientes — nenhum post real localizado via busca.

#### Estrutura típica do conteúdo
```
dados insuficientes
```

#### CTA dominante
- Padrão: dados insuficientes

#### Tom de voz
- Adjetivos: -

#### Métricas estimadas
- Tamanho médio de post educativo: dados insuficientes
- Formato mais usado: misto
- Engajamento estimado: baixo

---

### @nick_saraev

**Categoria:** automacao

#### Padrões de Hook identificados
- Dados insuficientes — nenhum post real localizado via busca.

#### Estrutura típica do conteúdo
```
dados insuficientes
```

#### CTA dominante
- Padrão: dados insuficientes

#### Tom de voz
- Adjetivos: -

#### Métricas estimadas
- Tamanho médio de post educativo: dados insuficientes
- Formato mais usado: misto
- Engajamento estimado: baixo

---

### @nathanhodgson

**Categoria:** ia

#### Padrões de Hook identificados
- Dados insuficientes — nenhum post real localizado via busca.

#### Estrutura típica do conteúdo
```
dados insuficientes
```

#### CTA dominante
- Padrão: dados insuficientes

#### Tom de voz
- Adjetivos: -

#### Métricas estimadas
- Tamanho médio de post educativo: dados insuficientes
- Formato mais usado: misto
- Engajamento estimado: baixo

---

### @ai

**Categoria:** ia

#### Padrões de Hook identificados
- Dados insuficientes — nenhum post real localizado via busca.

#### Estrutura típica do conteúdo
```
dados insuficientes
```

#### CTA dominante
- Padrão: dados insuficientes

#### Tom de voz
- Adjetivos: -

#### Métricas estimadas
- Tamanho médio de post educativo: dados insuficientes
- Formato mais usado: misto
- Engajamento estimado: baixo

---

### @ana.gsoares

**Categoria:** marketing

#### Padrões de Hook identificados
- Dados insuficientes — nenhum post real localizado via busca.

#### Estrutura típica do conteúdo
```
dados insuficientes
```

#### CTA dominante
- Padrão: dados insuficientes

#### Tom de voz
- Adjetivos: -

#### Métricas estimadas
- Tamanho médio de post educativo: dados insuficientes
- Formato mais usado: misto
- Engajamento estimado: baixo

---

### @chase.h.ai

**Categoria:** ia

#### Padrões de Hook identificados
- Dados insuficientes — nenhum post real localizado via busca.

#### Estrutura típica do conteúdo
```
dados insuficientes
```

#### CTA dominante
- Padrão: dados insuficientes

#### Tom de voz
- Adjetivos: -

#### Métricas estimadas
- Tamanho médio de post educativo: dados insuficientes
- Formato mais usado: misto
- Engajamento estimado: baixo

---

### @leosoares.ia

**Categoria:** ia

#### Padrões de Hook identificados
- Dados insuficientes — nenhum post real localizado via busca.

#### Estrutura típica do conteúdo
```
dados insuficientes
```

#### CTA dominante
- Padrão: dados insuficientes

#### Tom de voz
- Adjetivos: -

#### Métricas estimadas
- Tamanho médio de post educativo: dados insuficientes
- Formato mais usado: misto
- Engajamento estimado: baixo

---

### @gabriel.adamuchi

**Categoria:** creator

#### Padrões de Hook identificados
- Dados insuficientes — nenhum post real localizado via busca.

#### Estrutura típica do conteúdo
```
dados insuficientes
```

#### CTA dominante
- Padrão: dados insuficientes

#### Tom de voz
- Adjetivos: -

#### Métricas estimadas
- Tamanho médio de post educativo: dados insuficientes
- Formato mais usado: misto
- Engajamento estimado: baixo

---

### @viverdeia.ai

**Categoria:** ia

#### Padrões de Hook identificados
- Dados insuficientes — nenhum post real localizado via busca.

#### Estrutura típica do conteúdo
```
dados insuficientes
```

#### CTA dominante
- Padrão: dados insuficientes

#### Tom de voz
- Adjetivos: -

#### Métricas estimadas
- Tamanho médio de post educativo: dados insuficientes
- Formato mais usado: misto
- Engajamento estimado: baixo

---

### @ninja.automacoes

**Categoria:** automacao

#### Padrões de Hook identificados
- Dados insuficientes — nenhum post real localizado via busca.

#### Estrutura típica do conteúdo
```
dados insuficientes
```

#### CTA dominante
- Padrão: dados insuficientes

#### Tom de voz
- Adjetivos: -

#### Métricas estimadas
- Tamanho médio de post educativo: dados insuficientes
- Formato mais usado: misto
- Engajamento estimado: baixo

---

### @nikolassasso

**Categoria:** creator

#### Padrões de Hook identificados
- Dados insuficientes — nenhum post real localizado via busca.

#### Estrutura típica do conteúdo
```
dados insuficientes
```

#### CTA dominante
- Padrão: dados insuficientes

#### Tom de voz
- Adjetivos: -

#### Métricas estimadas
- Tamanho médio de post educativo: dados insuficientes
- Formato mais usado: misto
- Engajamento estimado: baixo

---

### @eduardocavalcanti

**Categoria:** founder

#### Padrões de Hook identificados
- Dados insuficientes — nenhum post real localizado via busca.

#### Estrutura típica do conteúdo
```
dados insuficientes
```

#### CTA dominante
- Padrão: dados insuficientes

#### Tom de voz
- Adjetivos: -

#### Métricas estimadas
- Tamanho médio de post educativo: dados insuficientes
- Formato mais usado: misto
- Engajamento estimado: baixo

---

### @jonylan

**Categoria:** creator

#### Padrões de Hook identificados
- Dados insuficientes — nenhum post real localizado via busca.

#### Estrutura típica do conteúdo
```
dados insuficientes
```

#### CTA dominante
- Padrão: dados insuficientes

#### Tom de voz
- Adjetivos: -

#### Métricas estimadas
- Tamanho médio de post educativo: dados insuficientes
- Formato mais usado: misto
- Engajamento estimado: baixo

---

### @allesinisgalli

**Categoria:** founder

#### Padrões de Hook identificados
- Dados insuficientes — nenhum post real localizado via busca.

#### Estrutura típica do conteúdo
```
dados insuficientes
```

#### CTA dominante
- Padrão: dados insuficientes

#### Tom de voz
- Adjetivos: -

#### Métricas estimadas
- Tamanho médio de post educativo: dados insuficientes
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Temas identificados
- inteligência artificial aplicada a marketing/negócios (comunidade citada: 'IA Club')

---

### @lonamkt

**Categoria:** marketing

#### Padrões de Hook identificados
- Dados insuficientes — nenhum post real localizado via busca.

#### Estrutura típica do conteúdo
```
dados insuficientes
```

#### CTA dominante
- Padrão: dados insuficientes

#### Tom de voz
- Adjetivos: -

#### Métricas estimadas
- Tamanho médio de post educativo: dados insuficientes
- Formato mais usado: misto
- Engajamento estimado: baixo

---

### @gabrielbarbosa.oficial

**Categoria:** creator

#### Padrões de Hook identificados
- Dados insuficientes — nenhum post real localizado via busca.

#### Estrutura típica do conteúdo
```
dados insuficientes
```

#### CTA dominante
- Padrão: dados insuficientes

#### Tom de voz
- Adjetivos: -

#### Métricas estimadas
- Tamanho médio de post educativo: dados insuficientes
- Formato mais usado: misto
- Engajamento estimado: baixo

---

### @opensession.co

**Categoria:** agencia

#### Padrões de Hook identificados
- Dados insuficientes — nenhum post real localizado via busca.

#### Estrutura típica do conteúdo
```
dados insuficientes
```

#### CTA dominante
- Padrão: dados insuficientes

#### Tom de voz
- Adjetivos: -

#### Métricas estimadas
- Tamanho médio de post educativo: dados insuficientes
- Formato mais usado: misto
- Engajamento estimado: baixo

---

### @leandroladeiran

**Categoria:** marketing

#### Padrões de Hook identificados
- Dados insuficientes — nenhum post real localizado via busca.

#### Estrutura típica do conteúdo
```
dados insuficientes
```

#### CTA dominante
- Padrão: dados insuficientes

#### Tom de voz
- Adjetivos: motivacional, humorístico, educativo

#### Métricas estimadas
- Tamanho médio de post educativo: dados insuficientes
- Formato mais usado: misto
- Engajamento estimado: baixo

#### Temas identificados
- marketing digital e negócios online
- empreendedorismo / 'ganhar dinheiro online'

---

### @christiantriad

**Categoria:** creator

#### Padrões de Hook identificados
- Dados insuficientes — nenhum post real localizado via busca.

#### Estrutura típica do conteúdo
```
dados insuficientes
```

#### CTA dominante
- Padrão: dados insuficientes

#### Tom de voz
- Adjetivos: -

#### Métricas estimadas
- Tamanho médio de post educativo: dados insuficientes
- Formato mais usado: misto
- Engajamento estimado: baixo

---

### @oneyaraujo

**Categoria:** creator

#### Padrões de Hook identificados
- Dados insuficientes — nenhum post real localizado via busca.

#### Estrutura típica do conteúdo
```
dados insuficientes
```

#### CTA dominante
- Padrão: dados insuficientes

#### Tom de voz
- Adjetivos: -

#### Métricas estimadas
- Tamanho médio de post educativo: dados insuficientes
- Formato mais usado: reels
- Engajamento estimado: alto

#### Temas identificados
- estratégias para viralizar no Instagram
- crescimento de seguidores
- monetização de audiência
- curso 'Código Viral'
- análise/reação a campanhas e estratégias de outros criadores (ex: Black Friday de gurus digitais)

---

### @geracaotechs

**Categoria:** ia

#### Padrões de Hook identificados
- Dados insuficientes — nenhum post real localizado via busca.

#### Estrutura típica do conteúdo
```
dados insuficientes
```

#### CTA dominante
- Padrão: dados insuficientes

#### Tom de voz
- Adjetivos: -

#### Métricas estimadas
- Tamanho médio de post educativo: dados insuficientes
- Formato mais usado: misto
- Engajamento estimado: baixo

---

### @amandadinizmkt

**Categoria:** marketing

#### Padrões de Hook identificados
- Dados insuficientes — nenhum post real localizado via busca.

#### Estrutura típica do conteúdo
```
dados insuficientes
```

#### CTA dominante
- Padrão: dados insuficientes

#### Tom de voz
- Adjetivos: -

#### Métricas estimadas
- Tamanho médio de post educativo: dados insuficientes
- Formato mais usado: misto
- Engajamento estimado: baixo

---

### @human___academy

**Categoria:** ia

#### Padrões de Hook identificados
- Dados insuficientes — nenhum post real localizado via busca.

#### Estrutura típica do conteúdo
```
dados insuficientes
```

#### CTA dominante
- Padrão: dados insuficientes

#### Tom de voz
- Adjetivos: -

#### Métricas estimadas
- Tamanho médio de post educativo: dados insuficientes
- Formato mais usado: misto
- Engajamento estimado: baixo

---

### @geiss11

**Categoria:** creator

#### Padrões de Hook identificados
- Dados insuficientes — nenhum post real localizado via busca.

#### Estrutura típica do conteúdo
```
dados insuficientes
```

#### CTA dominante
- Padrão: dados insuficientes

#### Tom de voz
- Adjetivos: -

#### Métricas estimadas
- Tamanho médio de post educativo: dados insuficientes
- Formato mais usado: misto
- Engajamento estimado: baixo

---

### @nelmoricalde

**Categoria:** creator

#### Padrões de Hook identificados
- Dados insuficientes — nenhum post real localizado via busca.

#### Estrutura típica do conteúdo
```
dados insuficientes
```

#### CTA dominante
- Padrão: dados insuficientes

#### Tom de voz
- Adjetivos: -

#### Métricas estimadas
- Tamanho médio de post educativo: dados insuficientes
- Formato mais usado: misto
- Engajamento estimado: baixo

---

### @rodrigotadewald

**Categoria:** marketing

#### Padrões de Hook identificados
- Dados insuficientes — nenhum post real localizado via busca.

#### Estrutura típica do conteúdo
```
dados insuficientes
```

#### CTA dominante
- Padrão: dados insuficientes

#### Tom de voz
- Adjetivos: -

#### Métricas estimadas
- Tamanho médio de post educativo: dados insuficientes
- Formato mais usado: misto
- Engajamento estimado: baixo

---

### @sujeitoprogramador

**Categoria:** ia

#### Padrões de Hook identificados
- Dados insuficientes — nenhum post real localizado via busca.

#### Estrutura típica do conteúdo
```
dados insuficientes
```

#### CTA dominante
- Padrão: dados insuficientes

#### Tom de voz
- Adjetivos: -

#### Métricas estimadas
- Tamanho médio de post educativo: dados insuficientes
- Formato mais usado: misto
- Engajamento estimado: baixo

---

### @jonathan_kamargo

**Categoria:** creator

#### Padrões de Hook identificados
- Dados insuficientes — nenhum post real localizado via busca.

#### Estrutura típica do conteúdo
```
dados insuficientes
```

#### CTA dominante
- Padrão: dados insuficientes

#### Tom de voz
- Adjetivos: -

#### Métricas estimadas
- Tamanho médio de post educativo: dados insuficientes
- Formato mais usado: misto
- Engajamento estimado: baixo

---

### @marianatorre.s

**Categoria:** marketing

#### Padrões de Hook identificados
- Dados insuficientes — nenhum post real localizado via busca.

#### Estrutura típica do conteúdo
```
dados insuficientes
```

#### CTA dominante
- Padrão: dados insuficientes

#### Tom de voz
- Adjetivos: -

#### Métricas estimadas
- Tamanho médio de post educativo: dados insuficientes
- Formato mais usado: misto
- Engajamento estimado: baixo

---

### @marketerhub.ai

**Categoria:** marketing

#### Padrões de Hook identificados
- Dados insuficientes — nenhum post real localizado via busca.

#### Estrutura típica do conteúdo
```
dados insuficientes
```

#### CTA dominante
- Padrão: dados insuficientes

#### Tom de voz
- Adjetivos: -

#### Métricas estimadas
- Tamanho médio de post educativo: dados insuficientes
- Formato mais usado: misto
- Engajamento estimado: baixo

---

### @marcelaluzzio

**Categoria:** marketing

#### Padrões de Hook identificados
- Dados insuficientes — nenhum post real localizado via busca.

#### Estrutura típica do conteúdo
```
dados insuficientes
```

#### CTA dominante
- Padrão: dados insuficientes

#### Tom de voz
- Adjetivos: -

#### Métricas estimadas
- Tamanho médio de post educativo: dados insuficientes
- Formato mais usado: misto
- Engajamento estimado: baixo

---

### @gestordeaudiencia

**Categoria:** marketing

#### Padrões de Hook identificados
- Dados insuficientes — nenhum post real localizado via busca.

#### Estrutura típica do conteúdo
```
dados insuficientes
```

#### CTA dominante
- Padrão: dados insuficientes

#### Tom de voz
- Adjetivos: -

#### Métricas estimadas
- Tamanho médio de post educativo: dados insuficientes
- Formato mais usado: misto
- Engajamento estimado: baixo

---

### @sebintel

**Categoria:** ia

#### Padrões de Hook identificados
- Dados insuficientes — nenhum post real localizado via busca.

#### Estrutura típica do conteúdo
```
dados insuficientes
```

#### CTA dominante
- Padrão: dados insuficientes

#### Tom de voz
- Adjetivos: -

#### Métricas estimadas
- Tamanho médio de post educativo: dados insuficientes
- Formato mais usado: misto
- Engajamento estimado: baixo

---

### @avora.ai

**Categoria:** agencia

#### Padrões de Hook identificados
- Dados insuficientes — nenhum post real localizado via busca.

#### Estrutura típica do conteúdo
```
dados insuficientes
```

#### CTA dominante
- Padrão: dados insuficientes

#### Tom de voz
- Adjetivos: -

#### Métricas estimadas
- Tamanho médio de post educativo: dados insuficientes
- Formato mais usado: misto
- Engajamento estimado: baixo

---

### @ogabrieeldias

**Categoria:** creator

#### Padrões de Hook identificados
- Dados insuficientes — nenhum post real localizado via busca.

#### Estrutura típica do conteúdo
```
dados insuficientes
```

#### CTA dominante
- Padrão: dados insuficientes

#### Tom de voz
- Adjetivos: -

#### Métricas estimadas
- Tamanho médio de post educativo: dados insuficientes
- Formato mais usado: misto
- Engajamento estimado: baixo

---

### @rodrigobindes

**Categoria:** founder

#### Padrões de Hook identificados
- Dados insuficientes — nenhum post real localizado via busca.

#### Estrutura típica do conteúdo
```
dados insuficientes
```

#### CTA dominante
- Padrão: dados insuficientes

#### Tom de voz
- Adjetivos: -

#### Métricas estimadas
- Tamanho médio de post educativo: dados insuficientes
- Formato mais usado: misto
- Engajamento estimado: baixo

---

### @franklim.gui

**Categoria:** creator

#### Padrões de Hook identificados
- Dados insuficientes — nenhum post real localizado via busca.

#### Estrutura típica do conteúdo
```
dados insuficientes
```

#### CTA dominante
- Padrão: dados insuficientes

#### Tom de voz
- Adjetivos: -

#### Métricas estimadas
- Tamanho médio de post educativo: dados insuficientes
- Formato mais usado: misto
- Engajamento estimado: baixo

---

### @gabrielsamp.ai

**Categoria:** ia

#### Padrões de Hook identificados
- Dados insuficientes — nenhum post real localizado via busca.

#### Estrutura típica do conteúdo
```
dados insuficientes
```

#### CTA dominante
- Padrão: dados insuficientes

#### Tom de voz
- Adjetivos: -

#### Métricas estimadas
- Tamanho médio de post educativo: dados insuficientes
- Formato mais usado: misto
- Engajamento estimado: baixo

---

### @maestrosdaia

**Categoria:** ia

#### Padrões de Hook identificados
- Dados insuficientes — nenhum post real localizado via busca.

#### Estrutura típica do conteúdo
```
dados insuficientes
```

#### CTA dominante
- Padrão: dados insuficientes

#### Tom de voz
- Adjetivos: -

#### Métricas estimadas
- Tamanho médio de post educativo: dados insuficientes
- Formato mais usado: misto
- Engajamento estimado: baixo

---

### @brandsdecoded__

**Categoria:** marketing

#### Padrões de Hook identificados
- Dados insuficientes — nenhum post real localizado via busca.

#### Estrutura típica do conteúdo
```
dados insuficientes
```

#### CTA dominante
- Padrão: dados insuficientes

#### Tom de voz
- Adjetivos: -

#### Métricas estimadas
- Tamanho médio de post educativo: dados insuficientes
- Formato mais usado: misto
- Engajamento estimado: baixo

---

### @anatex

**Categoria:** creator

#### Padrões de Hook identificados
- Dados insuficientes — nenhum post real localizado via busca.

#### Estrutura típica do conteúdo
```
dados insuficientes
```

#### CTA dominante
- Padrão: dados insuficientes

#### Tom de voz
- Adjetivos: -

#### Métricas estimadas
- Tamanho médio de post educativo: dados insuficientes
- Formato mais usado: misto
- Engajamento estimado: baixo

---

### @larissagomes.ia

**Categoria:** ia

#### Padrões de Hook identificados
- Dados insuficientes — nenhum post real localizado via busca.

#### Estrutura típica do conteúdo
```
dados insuficientes
```

#### CTA dominante
- Padrão: dados insuficientes

#### Tom de voz
- Adjetivos: -

#### Métricas estimadas
- Tamanho médio de post educativo: dados insuficientes
- Formato mais usado: misto
- Engajamento estimado: baixo

---

### @thiagozaao

**Categoria:** creator

#### Padrões de Hook identificados
- Dados insuficientes — nenhum post real localizado via busca.

#### Estrutura típica do conteúdo
```
dados insuficientes
```

#### CTA dominante
- Padrão: dados insuficientes

#### Tom de voz
- Adjetivos: -

#### Métricas estimadas
- Tamanho médio de post educativo: dados insuficientes
- Formato mais usado: misto
- Engajamento estimado: baixo

---

### @neuwebstudio

**Categoria:** agencia

#### Padrões de Hook identificados
- Dados insuficientes — nenhum post real localizado via busca.

#### Estrutura típica do conteúdo
```
dados insuficientes
```

#### CTA dominante
- Padrão: dados insuficientes

#### Tom de voz
- Adjetivos: -

#### Métricas estimadas
- Tamanho médio de post educativo: dados insuficientes
- Formato mais usado: misto
- Engajamento estimado: baixo

---

### @laschuk

**Categoria:** founder

#### Padrões de Hook identificados
- Dados insuficientes — nenhum post real localizado via busca.

#### Estrutura típica do conteúdo
```
dados insuficientes
```

#### CTA dominante
- Padrão: dados insuficientes

#### Tom de voz
- Adjetivos: -

#### Métricas estimadas
- Tamanho médio de post educativo: dados insuficientes
- Formato mais usado: misto
- Engajamento estimado: baixo

---

### @maestroptompts

**Categoria:** ia

#### Padrões de Hook identificados
- Dados insuficientes — nenhum post real localizado via busca.

#### Estrutura típica do conteúdo
```
dados insuficientes
```

#### CTA dominante
- Padrão: dados insuficientes

#### Tom de voz
- Adjetivos: -

#### Métricas estimadas
- Tamanho médio de post educativo: dados insuficientes
- Formato mais usado: misto
- Engajamento estimado: baixo

---

### @faladantasmkt

**Categoria:** marketing

#### Padrões de Hook identificados
- Dados insuficientes — nenhum post real localizado via busca.

#### Estrutura típica do conteúdo
```
dados insuficientes
```

#### CTA dominante
- Padrão: dados insuficientes

#### Tom de voz
- Adjetivos: -

#### Métricas estimadas
- Tamanho médio de post educativo: dados insuficientes
- Formato mais usado: misto
- Engajamento estimado: baixo

---

### @lindsay.ia

**Categoria:** ia

#### Padrões de Hook identificados
- Dados insuficientes — nenhum post real localizado via busca.

#### Estrutura típica do conteúdo
```
dados insuficientes
```

#### CTA dominante
- Padrão: dados insuficientes

#### Tom de voz
- Adjetivos: -

#### Métricas estimadas
- Tamanho médio de post educativo: dados insuficientes
- Formato mais usado: misto
- Engajamento estimado: baixo

---

### @andrevictor.m

**Categoria:** marketing

#### Padrões de Hook identificados
- Dados insuficientes — nenhum post real localizado via busca.

#### Estrutura típica do conteúdo
```
dados insuficientes
```

#### CTA dominante
- Padrão: dados insuficientes

#### Tom de voz
- Adjetivos: -

#### Métricas estimadas
- Tamanho médio de post educativo: dados insuficientes
- Formato mais usado: misto
- Engajamento estimado: baixo

---

### @drisiano

**Categoria:** creator

#### Padrões de Hook identificados
- Dados insuficientes — nenhum post real localizado via busca.

#### Estrutura típica do conteúdo
```
dados insuficientes
```

#### CTA dominante
- Padrão: dados insuficientes

#### Tom de voz
- Adjetivos: -

#### Métricas estimadas
- Tamanho médio de post educativo: dados insuficientes
- Formato mais usado: misto
- Engajamento estimado: baixo

---

### @brun0gpt

**Categoria:** ia

#### Padrões de Hook identificados
- Dados insuficientes — nenhum post real localizado via busca.

#### Estrutura típica do conteúdo
```
dados insuficientes
```

#### CTA dominante
- Padrão: dados insuficientes

#### Tom de voz
- Adjetivos: -

#### Métricas estimadas
- Tamanho médio de post educativo: dados insuficientes
- Formato mais usado: misto
- Engajamento estimado: baixo

---

### @maxcarrau.ia

**Categoria:** ia

#### Padrões de Hook identificados
- Dados insuficientes — nenhum post real localizado via busca.

#### Estrutura típica do conteúdo
```
dados insuficientes
```

#### CTA dominante
- Padrão: dados insuficientes

#### Tom de voz
- Adjetivos: -

#### Métricas estimadas
- Tamanho médio de post educativo: dados insuficientes
- Formato mais usado: misto
- Engajamento estimado: baixo

---

### @noevarner

**Categoria:** creator

#### Padrões de Hook identificados
- Dados insuficientes — nenhum post real localizado via busca.

#### Estrutura típica do conteúdo
```
dados insuficientes
```

#### CTA dominante
- Padrão: dados insuficientes

#### Tom de voz
- Adjetivos: -

#### Métricas estimadas
- Tamanho médio de post educativo: dados insuficientes
- Formato mais usado: misto
- Engajamento estimado: baixo

---

### @yikchanltd

**Categoria:** creator

#### Padrões de Hook identificados
- Dados insuficientes — nenhum post real localizado via busca.

#### Estrutura típica do conteúdo
```
dados insuficientes
```

#### CTA dominante
- Padrão: dados insuficientes

#### Tom de voz
- Adjetivos: -

#### Métricas estimadas
- Tamanho médio de post educativo: dados insuficientes
- Formato mais usado: misto
- Engajamento estimado: baixo

---

## Perfis Sugeridos pelo Sistema

Não aplicável nesta execução — `config/profiles.json` já tinha 61 perfis ativos, modo descoberta não foi utilizado.

---

## Limitações de Dados

Perfis onde não foi possível coletar dados suficientes (campo `limitacao_dados` preenchido) e motivo resumido:

- @charliehills — Acesso direto ao instagram.com/charliehills via WebFetch falhou (DNS/rede bloqueada nesta sessão: 'getaddrinfo ENOTFOUND www.instagram.com'; teste com outro domínio qualquer, example.com, também falhou, confirmando que WebFetch está bloqueado nesta sessão, ...
- @yikC — Nenhum perfil ou conteúdo correspondente ao handle 'yikC' foi encontrado via WebSearch (múltiplas queries, modo standard e extended) — os resultados retornaram apenas contas/pessoas com nomes parecidos (ex: @yk/Yik Keat em Singapura/Taiwan, @yicheng.0227, @...
- @eujoaotorresz — Nenhum perfil ou conteúdo correspondente ao handle 'eujoaotorresz' foi encontrado via WebSearch (múltiplas queries em português e inglês, incluindo variações com 'João Torres', 'IA', 'automação'). Os resultados retornaram apenas pessoas homônimas não relaci...
- @fabianocarvalhojr — Confirmado via WebSearch que o perfil @fabianocarvalhojr existe e pertence a Fabiano Carvalho, fundador da lasy.ai (empresa de agentes de IA para negócios), com bio citando ~130 mil seguidores e oferta de aula gratuita; encontrada menção paráfraseada (não l...
- @rafa.grandi — ALERTA DE POSSÍVEL PERFIL ERRADO: a busca via WebSearch encontrou o perfil real @rafa.grandi, mas ele pertence a 'Rafael Grandi Borges', com apenas ~247 seguidores, 284 seguindo e 36 posts, cuja bio o descreve como analista jurídico do governo do estado do ...
- @brusantanna.ai — WebFetch direto em instagram.com/brusantanna.ai falhou (host bloqueado na rede desta sessão: getaddrinfo ENOTFOUND www.instagram.com). Múltiplas buscas via WebSearch (nome do perfil + 'instagram posts reels 2026', + 'instagram conteúdo', e site:instagram.co...
- @vendedorglobal — WebFetch direto em instagram.com/vendedorglobal falhou (host bloqueado na rede desta sessão: getaddrinfo ENOTFOUND www.instagram.com). Buscas via WebSearch ('vendedorglobal' instagram posts reels 2026; 'vendedorglobal' instagram conteúdo viral; site:instagr...
- @oluizmain — WebFetch direto em instagram.com/oluizmain falhou (host bloqueado na rede desta sessão: getaddrinfo ENOTFOUND www.instagram.com). Buscas via WebSearch ('oluizmain' instagram; oluizmain instagram conteúdo reels; site:instagram.com) não retornaram nenhum resu...
- @nick_saraev — WebFetch direto em instagram.com/nick_saraev falhou (host bloqueado na rede desta sessão: getaddrinfo ENOTFOUND www.instagram.com). Buscas via WebSearch confirmaram apenas que Nick Saraev é um educador de AI automation/AI agency (fontes: favikon.com, creato...
- @nathanhodgson — WebFetch direto em instagram.com/nathanhodgson falhou (host bloqueado na rede desta sessão: getaddrinfo ENOTFOUND www.instagram.com). Buscas via WebSearch não encontraram o handle exato 'nathanhodgson', mas localizaram variantes possivelmente relacionadas c...
- @ai — Handle de uma única letra ('ai'), provavelmente conta genérica/corporativa de alto perfil (possivelmente o próprio handle oficial 'AI' do Instagram/Meta ou similar) e não um criador de nicho IA/automação/marketing. WebSearch com múltiplas queries (nome do h...
- @ana.gsoares — Nenhuma busca (handle isolado, + 'instagram', + 'marketing conteúdo reels', + 'posts reels 2026') retornou qualquer resultado específico sobre esse perfil. Os resultados trouxeram apenas perfis homônimos não relacionados (ex.: @gonsoares, @ana_rapozso, joga...
- @chase.h.ai — Encontrada apenas uma página de terceiro (creatordb.app/creatorstats/chase-h-ai) descrevendo 'Chase H AI' como criador americano de educação sobre IA no-code, com audiência concentrada em YouTube — mas a página não confirma existência, conteúdo ou métricas ...
- @leosoares.ia — Nenhuma busca (handle isolado, + 'instagram', + 'inteligência artificial conteúdo', + 'posts reels 2026') retornou qualquer resultado específico sobre esse perfil. Resultados trouxeram apenas perfis homônimos não relacionados (ex.: @elisoares, @leosiqueirab...
- @gabriel.adamuchi — Encontrada apenas uma loja Gumroad (gabrieladamuchi.gumroad.com) de um 'Gabriel Adamuchi' descrito como investidor/empreendedor/creator vendendo produtos digitais (prompts ChatGPT/Midjourney, guia de vendas) — mas nenhuma fonte confirma que essa é a mesma p...
- @viverdeia.ai — WebFetch direto em www.instagram.com falhou com erro de rede (ENOTFOUND - host fora da allowlist desta sandbox), confirmado novamente neste batch. Múltiplas queries no WebSearch ('viverdeia.ai instagram posts reels 2026', 'viverdeia.ai instagram conteúdo mo...
- @ninja.automacoes — WebFetch em www.instagram.com falhou (ENOTFOUND, host fora da allowlist da sandbox). WebSearch com múltiplas variações ('ninja.automacoes instagram posts reels', 'ninja.automacoes instagram automação', 'ninjadasautomacoes OR "ninja das automações" instagram...
- @nikolassasso — WebFetch em www.instagram.com e em creatordb.app falhou (ENOTFOUND, hosts fora da allowlist da sandbox). WebSearch encontrou apenas uma fonte agregadora de terceiros (creatordb.app/creatorstats/nikolassasso) descrevendo-o como educador de marketing digital ...
- @eduardocavalcanti — WebFetch em www.instagram.com falhou (ENOTFOUND, host fora da allowlist da sandbox). WebSearch com múltiplas variações ('eduardocavalcanti instagram posts reels founder', 'Eduardo Cavalcanti instagram fundador startup', '@eduardocavalcanti instagram') não r...
- @jonylan — WebFetch em www.instagram.com falhou (ENOTFOUND, host fora da allowlist da sandbox). WebSearch com múltiplas variações ('jonylan instagram posts reels', 'Jony Lan instagram', '@jonylan instagram') não retornou nenhum resultado correspondente a este handle. ...
- @allesinisgalli — WebSearch em múltiplas variações ('allesinisgalli' instagram posts reels 2026, instagram conteúdo, Alessandra Sinisgalli IA marketing) não retornou o perfil oficial do Instagram nem páginas de terceiros com múltiplos posts. Único achado com algum sinal real...
- @lonamkt — WebSearch com múltiplas variações ('lonamkt' instagram posts reels, instagram conteúdo marketing, 'Lona' marketing agência instagram @lonamkt, lonamkt instagram viral site:instagram.com) não retornou nenhum resultado que mencione esse handle específico. Tod...
- @gabrielbarbosa.oficial — WebSearch com várias variações ('gabrielbarbosa.oficial' instagram, instagram reels viral, Gabriel Barbosa criador conteúdo marketing digital instagram oficial) não encontrou o perfil correspondente a esse handle de categoria 'creator'. Todos os resultados ...
- @opensession.co — WebSearch com múltiplas variações ('opensession.co' instagram agência, 'Open Session' agência marketing instagram, opensession.co agência viral instagram carrossel, site:linkedin.com) não retornou nenhuma página mencionando esse domínio/agência. Os resultad...
- @leandroladeiran — WebSearch ('leandroladeiran' instagram marketing, Leandro Ladeiran instagram hooks reels CTA) encontrou apenas uma fonte com algum sinal real: a página de um agregador de terceiros não-oficial (creatordb.app), que não pôde ser aberta diretamente via WebFetc...
- @christiantriad — Busca via WebSearch (variações: '"christiantriad" instagram posts reels 2026', 'instagram conteúdo', '"@christiantriad" instagram viral', 'site:instagram.com christiantriad', e o termo isolado '"christiantriad"') não retornou nenhum resultado relacionado ao...
- @oneyaraujo — Não foi possível acessar posts individuais do perfil: WebFetch em instagram.com/oneyaraujo falhou com erro de rede (ENOTFOUND) e as buscas 'site:instagram.com oneyaraujo' não indexaram o perfil. Via WebSearch foi encontrada uma fonte terciária real (artigo ...
- @geracaotechs — Busca via WebSearch (variações: 'instagram posts reels 2026', 'instagram conteúdo', 'site:instagram.com geracaotechs', '"geração techs" instagram IA', e o termo isolado '"geracaotechs"') não retornou nenhum resultado relacionado ao perfil real @geracaotechs...
- @amandadinizmkt — Busca via WebSearch (variações: 'instagram posts reels 2026', 'instagram conteúdo', 'site:instagram.com amandadinizmkt', '"Amanda Diniz" marketing digital instagram', e o termo isolado '"amandadinizmkt"') não retornou nenhum resultado relacionado ao perfil ...
- @human___academy — Busca via WebSearch (variações: '"human___academy" instagram posts reels 2026', 'site:instagram.com human___academy', 'human academy instagram IA conteúdo', 'humanacademy.ai instagram @human___academy') não retornou posts reais do perfil @human___academy do...
- @geiss11 — WebSearch (3 variações de query, incluindo busca direta por 'instagram.com/geiss11') não retornou nenhum resultado referente a este perfil. Todos os resultados retornados foram sobre temas não relacionados: guias genéricos sobre Instagram Reels em 2026 e, n...
- @nelmoricalde — WebSearch (3 variações de query, incluindo busca direta por 'instagram.com/nelmoricalde') não retornou nenhum resultado sobre este perfil. Os resultados foram artigos acadêmicos genéricos sobre marketing de conteúdo no Instagram e perfis homônimos não confi...
- @rodrigotadewald — WebSearch (3 variações de query, incluindo busca pelo nome 'Rodrigo Tadewald marketing digital instagram') não retornou nenhum resultado específico sobre este perfil ou pessoa. Apareceu apenas um perfil homônimo não confirmado (@rodrigotarjapreta) em site d...
- @sujeitoprogramador — WebSearch (3 variações de query, incluindo busca por 'Sujeito Programador instagram @sujeitoprogramador' e termos sobre viralização em programação) não retornou nenhum resultado específico sobre o perfil Instagram @sujeitoprogramador, apesar de ser descrito...
- @jonathan_kamargo — WebSearch (3 variações de query, incluindo busca direta por 'instagram.com/jonathan_kamargo') não retornou nenhum resultado sobre este perfil. Apareceram apenas perfis homônimos com grafia diferente do sobrenome (ex.: @jcamargo_co, Jonathan Camargo robótica...
- @marianatorre.s — WebSearch com múltiplas variações de query ("marianatorre.s" instagram posts reels 2026, instagram conteúdo marketing, marketing digital, nome completo + handle) não retornou nenhum post, bio, hook, CTA ou dado de engajamento do perfil real. Os resultados r...
- @marketerhub.ai — WebSearch com múltiplas variações ("marketerhub.ai" instagram posts reels, instagram conteúdo, newsletter marketing quem é) não retornou nenhum resultado específico sobre esta conta ou domínio — nem posts, nem bio, nem informação sobre quem administra o per...
- @marcelaluzzio — WebSearch com múltiplas variações ("marcelaluzzio" instagram posts reels marketing, instagram viral conteúdo, nome completo + IA conteúdo seguidores) não retornou nenhum post, hook, CTA ou número de engajamento real do perfil. Único resultado relevante foi ...
- @gestordeaudiencia — WebSearch com múltiplas variações ("gestordeaudiencia" instagram reels posts, instagram viral conteúdo marketing, "@gestordeaudiencia" OR "gestor de audiência" instagram perfil) não retornou nenhum resultado relacionado a este perfil específico — nem posts,...
- @sebintel — WebSearch com múltiplas variações ("sebintel" instagram IA reels posts, instagram viral conteúdo IA automação, instagram followers hook video script) não retornou posts reais, hooks, CTAs ou métricas de engajamento verificáveis. O único resultado relevante ...
- @avora.ai — WebSearch (múltiplas variações: "avora.ai" instagram posts reels, conteúdo IA agência, site:instagram.com, agência Instagram Brasil automação) não retornou nenhum post, bio, print ou menção de terceiros sobre o perfil @avora.ai. Os resultados só trazem prod...
- @ogabrieeldias — WebSearch (variações: "ogabrieeldias" instagram posts reels 2026, instagram conteúdo, criador conteúdo, instagram isolado) não retornou nenhum resultado específico sobre esse handle. Todos os resultados foram sobre pessoas homônimas não relacionadas (Gabrie...
- @rodrigobindes — WebSearch localizou apenas contexto biográfico de terceiros (reportei.com): Rodrigo Bindes é descrito como fundador da Supersal e da Mentoria Ultra, mentor de agências e especialista em marketing para restaurantes, sócio investidor da franqueadora Giraffas,...
- @franklim.gui — WebSearch (variações: "franklim.gui" instagram posts reels, instagram creator conteúdo, handle isolado) não retornou nenhum resultado relacionado a esse perfil. Os resultados trouxeram apenas ferramentas genéricas de Instagram (clientes desktop, plugins Fra...
- @gabrielsamp.ai — WebSearch (variações: "gabrielsamp.ai" instagram posts reels, instagram IA criador) não retornou nenhum resultado específico sobre esse perfil ou domínio. Os resultados trouxeram apenas conteúdo genérico sobre recursos de IA do Instagram/Meta (Meta AI Studi...
- @maestrosdaia — WebSearch não retornou nenhum post, reel, bio, print ou menção de terceiros sobre a conta @maestrosdaia em nenhuma das variações de query testadas (handle + 'instagram posts reels 2026', + 'instagram conteúdo IA', 'Mestres de IA' + handle, site:instagram.co...
- @brandsdecoded__ — WebSearch não encontrou a conta @brandsdecoded__ nem qualquer post/reel associado a ela em nenhuma variação de query (handle + 'instagram posts reels branding', 'Brands Decoded' instagram branding creator, site:instagram.com + handle). Os resultados retorna...
- @anatex — WebSearch não retornou nenhum post, reel ou carrossel específico de @anatex com texto de hook, CTA ou tema analisável. A única fonte com alguma informação foi um perfil agregador de terceiros (creatordb.app/creatorstats/anatex, dados de 22/09/2026), que des...
- @larissagomes.ia — WebSearch não encontrou nenhum resultado referente à conta @larissagomes.ia ou a uma pessoa chamada Larissa Gomes associada a conteúdo de IA, em nenhuma das queries testadas (handle isolado, site:instagram.com + handle, 'Larissa Gomes' IA instagram automaçã...
- @thiagozaao — WebSearch não encontrou nenhum resultado referente à conta @thiagozaao ou a uma pessoa chamada 'Thiago Zaão', em nenhuma das queries testadas (handle isolado, site:instagram.com + handle, '"Thiago Zaão" instagram criador conteúdo'). Todos os resultados fora...
- @neuwebstudio — WebSearch com múltiplas variações de query ("neuwebstudio" instagram posts reels 2026; "neuwebstudio" instagram conteúdo agência; neuwebstudio instagram viral agencia site) não retornou nenhum resultado que mencione este perfil ou esta agência especificamen...
- @laschuk — WebSearch com múltiplas variações de query ("laschuk" instagram posts reels 2026; "laschuk" instagram founder conteúdo; laschuk instagram viral fundador startup) não retornou nenhum resultado associado a este handle/pessoa. Os resultados trouxeram apenas pe...
- @maestroptompts — WebSearch com múltiplas variações de query ("maestroptompts" instagram; "Maestro de Prompts" instagram engenharia de prompts) não retornou nenhum resultado para este handle ou para o nome "Maestro de Prompts". Os resultados foram páginas genéricas sobre eng...
- @faladantasmkt — WebSearch com múltiplas variações de query ("faladantasmkt" instagram; fala dantas mkt instagram marketing digital) não retornou nenhum resultado para este handle. Apareceram apenas perfis homônimos não relacionados (@falamb3, @falakhub, @falanimastani) e u...
- @lindsay.ia — WebSearch com múltiplas variações de query ("lindsay.ia" instagram; lindsay.ia inteligência artificial instagram brasil) não retornou nenhum resultado para este handle. Apareceram apenas perfis homônimos não relacionados (outras "Lindsay" nos EUA/UK) e list...
- @andrevictor.m — WebSearch com múltiplas queries ('andrevictor.m instagram', 'andrevictor.m instagram conteúdo marketing digital', 'site:instagram.com andrevictor.m') não retornou nenhum resultado correspondente ao perfil real @andrevictor.m. Todos os resultados foram de pe...
- @drisiano — WebSearch com múltiplas queries ('drisiano instagram', 'drisiano instagram reels creator conteúdo', 'site:instagram.com drisiano') não retornou nenhum resultado correspondente ao perfil real @drisiano. Os resultados foram contas homônimas não relacionadas (...
- @brun0gpt — WebSearch com múltiplas queries ('brun0gpt instagram', 'brun0gpt instagram IA automação reels', 'site:instagram.com brun0gpt') não retornou nenhum resultado correspondente ao perfil real @brun0gpt. Os resultados foram contas homônimas não relacionadas (vári...
- @maxcarrau.ia — WebSearch com múltiplas queries ('maxcarrau.ia instagram', 'maxcarrau.ia instagram IA conteúdo reels', 'site:instagram.com maxcarrau.ia') não retornou nenhum resultado correspondente ao perfil real @maxcarrau.ia. Os resultados foram contas/pessoas homônimas...
- @noevarner — WebSearch com múltiplas queries ('noevarner instagram', 'noevarner instagram reels viral conteúdo', 'site:instagram.com noevarner') não retornou nenhum resultado correspondente ao perfil real @noevarner. O resultado mais próximo foi a conta com grafia difer...
- @yikchanltd — WebFetch direto em instagram.com está bloqueado nesta sandbox (ENOTFOUND), então a análise dependeu exclusivamente de WebSearch. Foram executadas 3 buscas com variações diferentes: "yikchanltd" instagram; "yikchanltd" instagram posts reels; site:instagram.c...
