# Resumo Semanal — 2026-06-25

## Tendências em Destaque (Módulo 1)
- Claude Code lançou Plan mode, Auto mode e Routines (agentes cloud agendados por cron/webhook/evento), além de agentes aninhados e marketplace de ferramentas — exatamente o tipo de execução que este monitor já usa.
- Claude Agent SDK e o comando `claude -p` deixaram de contar no limite de uso do plano desde 15/jun/2026 — abre espaço para escalar automações sem gastar cota.
- Gartner projeta US$ 206,5 bi em software de agentes de IA em 2026 (+139% vs. 2025); Instagram passou a penalizar conteúdo "obviamente gerado por IA" e reciclado nos Reels.

## Perfis Analisados (Módulo 2)
- 16 perfis monitorados (de 58 cadastrados em `config/profiles.json`).
- Formato dominante: Reels (confirmado em praticamente todos os perfis com dado disponível).
- Hook mais comum: demonstração de ferramenta de IA + CTA de palavra-chave em comentário para entrega por DM.
- **Atenção:** handle `@nathanhodgson` em `config/profiles.json` não corresponde a nenhum perfil de IA — o perfil correto é `@nathanhodgson.ai`. 6 perfis (`@nikolassfaria`, `@jonylan`, `@laschuk`, `@anatex`, `@marianatorre.s`, `@eujoaotorresz`) tiveram dados insuficientes ou perfil não localizado — ver limitações no relatório completo.

## Top Conteúdo da Semana (Módulo 3)
- **@chase.h.ai** — "ferramenta de geração de leads para AI agents" — maior base de seguidores do trio com conteúdo mais forte (201K), funil de mentoria paga validado, prova de resultado de negócio implícita.
- **@leosoares.ia** — "Comenta 'IA7'" — mecanismo de engajamento mecânico comprovado com citação exata via URL do reel.
- **@geracaotechs** — criação de jogos com IA via Replit — combina ferramenta gratuita, apelo "sem programar" e CTA de engajamento.

## Insights Estratégicos (Módulos 4+5)
- O framework mais replicável e direto para Lucas hoje é **"mostrar uma ferramenta real → demonstrar resultado → CTA de palavra-chave em comentário"** — aparece em 5 dos 8 perfis com conteúdo confirmado e tem alta performance no Top 10.
- O modelo de conteúdo mais frequente e com maior potencial para o negócio é `demonstracao_ferramenta` (10 ocorrências nos dados), seguido de `lista_checklist` (3) e `trend_adaptada` (3) — todos classificados como fácil/média produção e alto potencial.
- `storytelling` performa alto nos dados gerais, mas tem replicabilidade e potencial baixos para Lucas agora — guardar para quando houver audiência/autoridade construída.

## Ações para Esta Semana (Módulo 6)
1. Produzir: "O Agente Que Vira Vigia do Instagram" (Reel — demonstração da ferramenta deste próprio monitor)
2. Produzir: "7 Skills do Claude Code Que Você Não Usa" (Reel — lista/checklist com CTA "Comenta SKILLS")
3. Testar: hook de reação à novidade do Claude Code (Routines/Plan mode) — formato `reacao_lancamento`, vantagem estrutural única de Lucas via este monitor

## Posts Prontos para Publicar
- [Ver relatório completo](06-aplicacao-negocio.md) — 5 posts com texto completo, hook, estrutura e CTA prontos para gravar.

## Bloqueios Estruturais do Ambiente
- **Módulo 7 (Obsidian):** bloqueado — ambiente Linux remoto sem acesso ao filesystem Windows onde o vault está localizado.
- **Módulo 8 (Notion):** bloqueado — nenhum MCP server do Notion conectado nesta sessão.
- Ver detalhes em `07-obsidian-export.md` e `08-notion-export.md`.
