---
name: roteiro
description: Gera um roteiro de conteúdo Neovertix no tom de voz da marca e o submete à avaliação de qualidade da Iana (score 0-10, corte 7). Use quando o Lucas pedir /roteiro, "escreve um roteiro", "transforma isso em roteiro" ou passar uma ideia/post/notícia pra virar conteúdo.
argument-hint: "<ideia, tema, link ou fonte do roteiro>"
user-invocable: true
---

# /roteiro — Roteira escreve, Iana avalia

Fluxo encadeado dos módulos 13 + 14 do sistema de marketing (`Social mídia IA/`).

## Passos

1. **Entenda o insumo** do argumento do usuário (ideia solta, tema, post salvo, notícia, slot de campanha). Se não houver argumento, pergunte o que ele quer transformar em roteiro.
2. **Lance o agente `roteira`** (Agent tool) com o insumo + instrução de seguir `Social mídia IA/modules/13-roteiros.md`. O agente lê contexto de marca, escolhe framework nos bancos, escreve no template e salva em `Social mídia IA/producao/roteiros/YYYY-MM-DD/{slug}.md`.
3. **Lance o agente `iana`** (Agent tool) com o caminho do roteiro salvo + instrução de seguir `Social mídia IA/modules/14-analise-roteiro.md`. Ela devolve a avaliação completa (tabela + score) e atualiza o frontmatter.
4. **Se score <7:** repasse as sugestões da Iana ao `roteira` para reescrita (máximo 2 rodadas no total). Na 2ª reprovação, apresente ao Lucas as versões + diagnóstico e pare.
5. **Apresente ao Lucas:** caminho do arquivo, score final, o gancho escolhido e a mensagem central — e a avaliação resumida da Iana.

## Regras

- Nunca pule a Iana — roteiro sem score não segue na esteira.
- Roteiros são salvos SEMPRE em `Social mídia IA/producao/roteiros/` (a pasta é criada na primeira escrita).
- Português brasileiro.