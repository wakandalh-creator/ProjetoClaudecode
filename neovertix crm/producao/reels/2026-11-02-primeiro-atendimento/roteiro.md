---
projeto: neovertix crm
formato: reel
tema: primeiro atendimento automático no WhatsApp (abordagem 2 de 3)
cta: Experimente gratuitamente por 5 dias (link na bio)
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
E pode testar de graça por 5 dias.
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
| 0:25 | 5 DIAS GRÁTIS |
| 0:28 | SEM CARTÃO. SEM COMPROMISSO. |

Área segura em 1080×1920: nada acima de y=230, abaixo de y=1440 nem nos 230 px da direita. Legendas queimadas na fala inteira.

## Direção de edição

| Tempo | Imagem |
|---|---|
| 0:00–0:06 | Celular na mesa, tela acende com notificação de WhatsApp; relógio marcando 23h. Movimento no primeiro frame. |
| 0:06–0:18 | **Captura de tela real** do agente respondendo e fazendo as perguntas de qualificação (trocar o quadro a cada frase). |
| 0:18–0:25 | **Captura de tela real** do CRM: contato novo com histórico e etapa do funil. |
| 0:25–0:30 | Tela do cadastro do teste mostrando que não pede cartão (**captura necessária**). |
| 0:30–0:34 | Tela final com "5 dias grátis" e indicação do link na bio. |

## Pendências antes de gravar

- **Capturas necessárias:** agente respondendo no WhatsApp e CRM com histórico. Usar contato fictício identificado como exemplo. Sem essas telas, os beats 3 a 7 não se sustentam.
- **Confirmar no produto:** o agente faz perguntas configuráveis (qualificação) e salva a conversa no CRM (o briefing diz "conforme as funcionalidades disponíveis").
- **Confirmado pelo Lucas (2026-11-02):** teste sem cartão de crédito. **A confirmar:** "sem compromisso" (nada é cobrado ao fim dos 5 dias se a pessoa não contratar?) e "responde na hora".
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

## Histórico

- v1 (2026-11-02): primeiro atendimento às 23h.
- v2 (2026-11-02): pedido do Lucas — enfatizar atendimento 24h, qualificação do lead e teste grátis sem cartão, para aumentar a percepção de valor.
