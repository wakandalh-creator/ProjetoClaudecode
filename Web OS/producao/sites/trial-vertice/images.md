# Pipeline de imagem — trial-vertice

> Módulo 21, Passo 4. Produto: serviço (agente de IA + CRM via Bolten) — **sem produto físico**, logo o caminho é moodboard, não fotos de produto.

## Decisão de partida

Esta página foi desenhada em `specs/design.md` como **text/componente-led**, não imagem-led: a prova central (log de conversa real) é HTML/CSS, não screenshot, e o Hero usa texto como elemento de LCP. Resultado prático: a dependência de imagem gerada é **mínima**, quase zero no escopo da V1. Isso é bom pro orçamento de performance (Passo 2b) e evita o risco de imagem genérica de IA competir com a autenticidade que a marca exige (Cara Comum, "testado — não prometido").

Sem ferramenta de navegação/screenshot visual disponível nesta sessão (mesma limitação registrada em `references/notas-referencia.md`) — por isso este arquivo não lista um moodboard de 5-8 imagens "vistas" em algum lugar. O que segue é a direção de prompt a aplicar **se e quando** o Lucas decidir que algum bloco precisa de imagem de apoio, mais um item que não é pipeline de imagem gerada (foto real do Lucas).

## O que NÃO entra como imagem gerada

- **Foto do Lucas (seção "Quem constrói").** Precisa ser foto real dele, nunca gerada por IA — contraria o arquétipo Cara Comum e a regra de veracidade se for substituída por imagem sintética ou banco de imagens genérico de "founder". **Pendência prática**: o Lucas precisa fornecer/agendar essa foto antes do módulo 22. Não é tarefa deste pipeline.
- **Log de conversa (seção Prova).** É HTML/CSS com conteúdo real, nunca imagem/screenshot — ver Trust Architecture em `specs/design.md`. Transcrição ainda não entregue a este módulo (pendência de conteúdo, não de imagem).

## Se houver imagem de apoio (opcional, decisão aberta)

Caso o Lucas queira textura/imagem de apoio em algum bloco (ex.: fundo com leve textura na seção Hero ou na Arquitetura de Confiança, reforçando a "profundidade em camadas de fundo" de `01-estrategia.md` §8), o caminho é moodboard de **estilo**, não de produto:

1. Aprovar com o Lucas 5-8 referências de *estilo visual* (textura, não objeto) antes de gerar qualquer coisa.
2. Gerar uma imagem **âncora** primeiro, aprovar, só depois reusar essa âncora como referência nas demais — nunca derivar imagem de imagem sem uma âncora aprovada.
3. Prompt-base compartilhado (se aplicável): paleta restrita a off-black `#16151A` / off-white `#F6F3EE` / accent clay `#C1552E`, abstrata/geométrica, nunca figurativa de robô, nunca gradiente azul-roxo, nunca ícone de cadeado/escudo.
4. `imagegen-frontend-web` é opcional pra padronizar os prompts — não é obrigatório, dado o volume baixo previsto.

**Até o Lucas pedir isso, o default deste projeto é zero imagem gerada além do que está listado como "não entra" acima.**
