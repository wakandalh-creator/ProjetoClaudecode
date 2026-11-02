---
projeto: neovertix crm
formato: reel
tema: primeiro atendimento automático no WhatsApp (abordagem 2 de 3)
cta: Experimente gratuitamente por 7 dias (link na bio)
status: rascunho — não publicar sem aprovação do Lucas
duracao_estimada: 33.5s a 165 ppm (cronometrar a leitura real)
---

# Reel — "23h. Cliente novo no WhatsApp."

## Ganchos (hookscore.py)

| Nota | Fórmula | Fala | Tela |
|---|---|---|---|
| **100 STRONG** | #18 Cold Open Demo (cena) | "23h. Cliente novo no WhatsApp, e você já dormiu." | 23H. CLIENTE NOVO. |
| 94 STRONG | #18 variação | "Mensagem no seu WhatsApp às 23h. Ninguém responde até amanhã." | 23H. NINGUÉM RESPONDE. |
| 51 OK | #20 Permission | "Você não precisa contratar mais um atendente pra responder o primeiro contato." | SEM CONTRATAR ATENDENTE |
| 36 WEAK | #10 If This, Then Watch | "Se o seu cliente espera horas pela primeira resposta, esse atendimento resolve." | — |

Escolhido o primeiro, encurtado para caber em 2,5s: a cena é concreta (horário + canal), fala direto com o dono e não depende de número sem fonte.

## Fala (v2: 24h, qualificação e teste sem cartão)

```
23h. Cliente novo no WhatsApp. Você dormindo.
Até amanhã, ele pode fechar com quem responder primeiro.
Com um agente de IA no seu WhatsApp,
o atendimento funciona 24 horas por dia.
Ele responde na hora e qualifica o lead:
pergunta o que a pessoa precisa, do jeito que você definiu.
Tudo fica salvo no CRM, com o histórico.
De manhã, você vê quem está mais perto de comprar.
E pode testar de graça por 7 dias.
Sem cartão de crédito. Sem compromisso.
O próximo cliente das 23h não espera. Link na bio.
```

## Texto na tela (máx. 6 palavras, dentro da área segura)

| Tempo | Cartão |
|---|---|
| 0:00 | 23H. CLIENTE NOVO. |
| 0:06 | ATENDIMENTO 24 HORAS |
| 0:11 | QUALIFICA O LEAD |
| 0:18 | TUDO SALVO NO CRM |
| 0:21 | QUEM ESTÁ PERTO DE COMPRAR |
| 0:25 | 7 DIAS GRÁTIS |
| 0:28 | SEM CARTÃO. SEM COMPROMISSO. |

Área segura em 1080×1920: nada acima de y=230, abaixo de y=1440 nem nos 230 px da direita. Legendas queimadas na fala inteira.

## Direção de edição

| Tempo | Imagem |
|---|---|
| 0:00–0:06 | Celular na mesa, tela acende com notificação de WhatsApp; relógio marcando 23h. Movimento no primeiro frame. |
| 0:06–0:18 | **Captura de tela real** do agente respondendo e fazendo as perguntas de qualificação (trocar o quadro a cada frase). |
| 0:18–0:25 | **Captura de tela real** do CRM: contato novo com histórico e etapa do funil. |
| 0:25–0:30 | Tela do cadastro do teste mostrando que não pede cartão (**captura necessária**). |
| 0:30–0:34 | Tela final com "7 dias grátis" e indicação do link na bio. |

## Pendências antes de gravar

- **Capturas necessárias:** agente respondendo no WhatsApp e CRM com histórico. Usar contato fictício identificado como exemplo. Sem essas telas, os beats 3 a 7 não se sustentam.
- **Confirmar no produto:** o agente faz perguntas configuráveis (qualificação) e salva a conversa no CRM (o briefing diz "conforme as funcionalidades disponíveis").
- **Confirmado pelo Lucas (2026-11-02):** teste sem cartão de crédito. **A confirmar:** "sem compromisso" (nada é cobrado ao fim dos 7 dias se a pessoa não contratar?) e "responde na hora".
- **Captura necessária:** tela de cadastro do teste sem campo de cartão.
- **Link do teste gratuito** na bio: {{URL a confirmar}}.
- **Ritmo real:** cronometrar a leitura e rodar `beats.py --wpm <número>`.

## Verificações

- `beats.py`: 33,5s, nenhuma cena acima de 4s, gancho em 2,5s, loop fechado ("23h", "cliente"). O aviso "beats 5-7 sem nada concreto" é em parte falso positivo: o script não reconhece "CRM" nem "lead" como concretos. As capturas de tela desses trechos é que dão a prova.
- `ig-human`: 0 clichês, 0 travessões, 0 caracteres invisíveis. A "nota de humano" (40) não vale para este texto: um roteiro quebrado em falas curtas tem frases de tamanho parecido por definição, e o detector não reconhece "WhatsApp" e "CRM". O guia recomenda não usar essas notas para classificar texto em português.

## Série (as 3 abordagens do briefing)

1. Educativo: "Sua empresa recebe contatos todos os dias, mas quantos deles realmente recebem acompanhamento?"
2. **Transformação (este reel):** primeiro atendimento automático no WhatsApp.
3. Posicionamento: "Não basta atrair clientes. É preciso ter uma estrutura preparada para atender, organizar e converter oportunidades."

## v3 — texto do Lucas, ajustado (43,6s)

Original do Lucas em `lucas-v3.txt` (200 palavras, ~73s). Versão ajustada em `ajustado-v3.txt`:

```
Fim do expediente.
Cliente novo no seu WhatsApp, e ninguém responde.
Você está descansando. E ele pode estar conversando com outras empresas.
Muitas vezes, a venda não se perde pelo preço.
Se perde porque alguém respondeu primeiro.
Com o Agente de IA da Neovertix,
seu atendimento funciona 24 horas por dia.
Ele responde, conversa com o interessado
e qualifica o contato com as perguntas que você definiu.
Tudo fica no CRM, com o histórico da conversa.
Quando você começa o dia, não precisa procurar conversa perdida.
Você já sabe quais oportunidades precisam de atenção.
Teste grátis por 7 dias. Sem cartão de crédito. Sem compromisso.
Link na bio.
Não perca mais nenhuma oportunidade
no seu WhatsApp por falta de atendimento.
```

| Tempo | Cartão |
|---|---|
| 0:00 | FIM DO EXPEDIENTE. |
| 0:04 | ALGUÉM RESPONDEU PRIMEIRO |
| 0:13 | ATENDIMENTO 24 HORAS |
| 0:18 | QUALIFICA O CONTATO |
| 0:24 | TUDO NO CRM |
| 0:31 | OPORTUNIDADES QUE PRECISAM DE ATENÇÃO |
| 0:34 | 7 DIAS GRÁTIS. SEM CARTÃO. |

- **Gancho:** "Fim do expediente. Cliente novo no seu WhatsApp, e ninguém responde." nota 80 (o original "Acabou o seu expediente. Um potencial cliente chama sua empresa no WhatsApp." fez 44: longo e sem tensão).
- **Cortes:** "E não para por aí" (ponte sem conteúdo); "Mais organização para atender. Mais clareza para vender." (abstratos, regra do tom de voz); "Não perca clientes porque sua empresa não conseguiu responder a tempo" (repetia a ideia); "transforme já o seu negócio" (genérico, banido); "Cadastre-se" + "Acesse o link" viraram uma chamada só.
- **"Não perca mais nenhuma oportunidade… por falta de atendimento" mantida no fim** (decisão do Lucas, 2026-11-02): o agente existe para nenhum contato ficar sem resposta; o "por falta de atendimento" deixa claro que a promessa é sobre responder, não sobre vender.
- **"Responde imediatamente" virou "responde"** até confirmar no produto.
- **Duração do teste: 7 dias** (decisão do Lucas, 2026-11-02; antes o briefing dizia 5).

## Legenda (v3, /ig-caption)

Tipo A: o vídeo já carrega o gancho; a legenda faz a chamada e traz os termos de busca.

```
Teste o Agente de IA da Neovertix por 7 dias grátis, sem cartão de crédito. Link na bio.

Fim do expediente não precisa ser fim do atendimento. Com um agente de IA, o seu atendimento no WhatsApp continua fora do horário comercial, e cada contato recebe resposta.

Ele conversa com o interessado e qualifica o lead com as perguntas que você define.

As informações ficam no CRM, com o histórico da conversa e as oportunidades organizadas.

De manhã, você já sabe quem precisa de atenção. Quem decide o próximo passo é você.

#atendimentowhatsapp #agentedeia #crm #pequenasempresas
```

- Linter (`caption.py`): **READY**. 1ª linha com 88 caracteres, inteira antes do "... mais"; 1 chamada; 4 hashtags; 0 emoji.
- Termos de busca: "agente de IA" (1ª linha), "atendimento no WhatsApp" (2º parágrafo), "CRM" (4º parágrafo).
- Humanizador: nada para limpar.
- Link do teste vai na bio, não na legenda: {{URL a confirmar}}.

## Histórico

- v1 (2026-11-02): primeiro atendimento às 23h.
- v2 (2026-11-02): pedido do Lucas — enfatizar atendimento 24h, qualificação do lead e teste grátis sem cartão, para aumentar a percepção de valor.
