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

### Passo 4 — Salvar e encaminhar
- Salvar em `Social mídia IA/producao/roteiros/YYYY-MM-DD/{slug-do-titulo}.md`
- Invocar o módulo 14 (Iana) na sequência. Se score <7: reescrever conforme sugestões (máx. 2 rodadas).
- Roteiro aprovado (≥7): informar o Lucas com o caminho do arquivo + score + resumo de 1 linha.
