---
projeto: neovertix crm
formato: reel
tema: primeiro atendimento automático no WhatsApp (abordagem 2 de 3)
cta: Experimente gratuitamente por 5 dias (link na bio)
status: rascunho — não publicar sem aprovação do Lucas
duracao_estimada: 30.6s a 165 ppm (cronometrar a leitura real)
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

## Fala

```
23h. Cliente novo no WhatsApp. Você dormindo.
Até amanhã, ele pode fechar com quem responder primeiro.
Com um agente de IA no seu WhatsApp,
o atendimento começa às 23h mesmo.
Ele responde e faz as perguntas que você definiu.
Anota o que o cliente precisa.
E salva tudo no CRM, com o histórico.
De manhã, você vê quem chegou e o que quer.
Quem decide o próximo passo é você.
Teste 5 dias grátis. Link na bio.
O próximo cliente das 23h não espera.
```

## Texto na tela (máx. 6 palavras, dentro da área segura)

| Tempo | Cartão |
|---|---|
| 0:00 | 23H. CLIENTE NOVO. |
| 0:05 | AGENTE DE IA NO WHATSAPP |
| 0:10 | RESPONDE E FAZ AS PERGUNTAS |
| 0:16 | TUDO SALVO NO CRM |
| 0:19 | DE MANHÃ: QUEM CHEGOU |
| 0:22 | VOCÊ DECIDE |
| 0:25 | TESTE 5 DIAS GRÁTIS |

Área segura em 1080×1920: nada acima de y=230, abaixo de y=1440 nem nos 230 px da direita. Legendas queimadas na fala inteira.

## Direção de edição

| Tempo | Imagem |
|---|---|
| 0:00–0:05 | Celular na mesa, tela acende com notificação de WhatsApp; relógio marcando 23h. Movimento no primeiro frame. |
| 0:05–0:16 | **Captura de tela real** do agente respondendo e fazendo as perguntas (trocar o quadro a cada frase). |
| 0:16–0:22 | **Captura de tela real** do CRM: contato novo com histórico da conversa. |
| 0:22–0:25 | Lucas (ou mão no celular) abrindo o CRM de manhã. |
| 0:25–0:30 | Tela final com "Teste 5 dias grátis" e indicação do link na bio. |

## Pendências antes de gravar

- **Capturas necessárias:** agente respondendo no WhatsApp e CRM com histórico. Usar contato fictício identificado como exemplo. Sem essas telas, os beats 3 a 7 não se sustentam.
- **Confirmar no produto:** o agente faz perguntas configuráveis e salva a conversa no CRM (o briefing diz "conforme as funcionalidades disponíveis").
- **Link do teste gratuito** na bio: {{URL a confirmar}}.
- **Ritmo real:** cronometrar a leitura e rodar `beats.py --wpm <número>`.

## Verificações

- `beats.py`: 30,6s, nenhuma cena acima de 4s, gancho em 2,5s, loop fechado ("23h", "cliente"). O aviso "beats 2-4 sem nada concreto" é falso positivo: o script não reconhece "WhatsApp" nem "23h" como concretos.
- `ig-human`: 0 clichês, 0 travessões, 0 caracteres invisíveis. A "nota de humano" (40) não vale para este texto: um roteiro quebrado em falas curtas tem frases de tamanho parecido por definição, e o detector não reconhece "WhatsApp" e "CRM". O guia recomenda não usar essas notas para classificar texto em português.

## Série (as 3 abordagens do briefing)

1. Educativo: "Sua empresa recebe contatos todos os dias, mas quantos deles realmente recebem acompanhamento?"
2. **Transformação (este reel):** primeiro atendimento automático no WhatsApp.
3. Posicionamento: "Não basta atrair clientes. É preciso ter uma estrutura preparada para atender, organizar e converter oportunidades."
