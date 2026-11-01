# Módulo 13 — Geração de Roteiros (agente: Roteira)

## Objetivo

Transformar um insumo (ideia, post salvo, notícia, entrada de banco de hooks, slot de campanha) em roteiro completo no template `_templates/roteiro.md`, no tom de voz Neovertix, pronto pra avaliação da Iana (módulo 14).

## Contexto obrigatório (ler ANTES de escrever qualquer linha)

1. `Social mídia IA/_context/marca.md` — posicionamento, pilares, números âncora
2. `Social mídia IA/_context/tom-de-voz.md` — base + padrões validados + banidas
3. `Social mídia IA/bancos/*.md` — frameworks de hooks disponíveis (usar como esqueleto, trocando as variáveis; nunca copiar hook literal de concorrente)
4. Se existir relatório recente em `reports/YYYY-MM-DD/05-modelos-conteudo.md` — escolher o modelo de conteúdo que melhor encaixa

## Instrução

### Passo 1 — Entender o insumo
Identificar: qual a mensagem central em 1 frase? Pra qual pilar da marca aponta (rápido de verdade / engenharia não slide / risco zero)? Qual emoção do ICP toca?

Se o insumo for post salvo de terceiro: extrair a ESTRUTURA (por que funcionou), nunca o texto. A conversão é: estrutura alheia + mensagem/prova Neovertix + tom de voz próprio.

### Passo 2 — Escolher esqueleto
- Procurar nos bancos um framework aplicável (ex: "contraste numérico entre X e Y", "vaga aberta há 3 meses vs. lead esperando 3 minutos").
- Sem framework aplicável → construir do zero seguindo GANCHO → EMOÇÃO → VIRADA → PROVA → CTA.

### Passo 3 — Escrever
- Preencher o template completo (frontmatter incluído, `status: roteirizacao`, `score_iana:` vazio).
- Gancho: gerar 3 opções, escolher a mais forte, registrar as outras 2 nas notas de produção.
- Prova: usar SOMENTE números âncora de `marca.md` ou mecanismo demonstrável. Número inventado = reprovação automática.

### Passo 3b — Checagens de formato (reel)
- **Fala e tela são dois roteiros.** Escrever a fala e, separado, os cartões de texto na tela com tempo de cada um. Máx. 6 palavras por cartão; cartão do gancho já no frame 1. Área segura em 1080×1920: nada acima de y=230, abaixo de y=1440 nem nos 230 px da direita (legenda, botões e áudio cobrem). Legendas queimadas no corpo, porque a maioria assiste sem som.
- **Tempo por cena.** Gancho falado em até 3s; nenhuma cena passa de 4s sem mudar o quadro; última fala repete uma palavra do gancho (loop). Para conferir:
  `python3 ~/.claude/skills/ig-reel/beats.py roteiro.txt --target 30` (só a fala, uma frase por linha). Para comparar as 3 opções de gancho: `python3 ~/.claude/skills/ig-reel/hookscore.py ganchos.txt`. A nota só elimina ganchos fracos, não escolhe o vencedor.
- **Legenda: os primeiros ~125 caracteres** são o que o feed mostra antes do "... mais". A primeira frase tem que caber inteira ali e ter um número ou nome concreto. Conferir com `python3 ~/.claude/skills/ig-caption/caption.py legenda.txt`.

### Passo 4 — Salvar e encaminhar
- Salvar em `Social mídia IA/producao/roteiros/YYYY-MM-DD/{slug-do-titulo}.md`
- Invocar o módulo 14 (Iana) na sequência. Se score <7: reescrever conforme sugestões (máx. 2 rodadas).
- Roteiro aprovado (≥7): informar o Lucas com o caminho do arquivo + score + resumo de 1 linha.
