# Prompt para cron diário

Você executa manutenção experimental diária da skill Synesis para Hermes no repositório informado pelo agendador.

Limites obrigatórios:

- Trabalhe somente na branch `hermes/skill-improvement`.
- Nunca altere, envie, faça merge, rebase, tag ou release em `main`.
- Não altere remoto, permissões, credenciais ou configuração global do Git ou Hermes.
- Não use dados reais, pessoais, privados ou de pesquisa.
- Não modifique a skill agnóstica, o Guia didático Synesis, os portões T, O e A, a autoridade metodológica, a versão do frontmatter, licença ou créditos.
- Não aceite relato de agente como prova. Inspecione arquivos e saída bruta.

Rotação semanal:

- Segunda-feira, cenário 01
- Terça-feira, cenário 02
- Quarta-feira, cenário 03
- Quinta-feira, cenário 04
- Sexta-feira, cenário 05
- Sábado e domingo, cenário 01

A rotação não depende da memória da sessão anterior. Nos fins de semana, o cenário 01 repete a verificação determinística de instalação e descoberta.

Procedimento:

1. Entre no clone, execute `git status --short --branch` e pare se houver alteração inesperada.
2. Execute `git fetch origin`. Confirme `origin/main` e confirme a branch atual `hermes/skill-improvement`.
3. Se a branch remota de manutenção divergir da local, pare e registre bloqueio para revisão humana. Não reescreva histórico.
4. Escolha o cenário de `tests/cenarios/` definido pela rotação semanal.
5. Execute primeiro `python3 scripts/run_maintenance_tests.py` e leia toda a saída útil.
6. Execute o cenário escolhido nesta sessão do Hermes com a skill `synesis` carregada. Use o briefing documentado e guarde a resposta bruta como evidência.
7. Use somente fixture em `tests/fixtures/`. Não faça pesquisa qualitativa real, não use corpus real e não trate a resposta do modelo como prova sem inspeção.
8. Inspecione arquivos relevantes e registre hipótese, cenário e evidência reproduzível.
9. Implemente somente correção de baixo risco permitida por `docs/PROTOCOLO_DE_MANUTENCAO.md`.
10. Após cada mudança, execute `python3 scripts/run_maintenance_tests.py`, `python3 scripts/validate_skill.py` e `git diff --check`.
11. Atualize `CHANGELOG_MANUTENCAO.md` somente quando houver mudança real comprovada.
12. Antes de commit, confira `git status --short` e confirme que só há arquivos do escopo.
13. Faça commit e push somente na branch `hermes/skill-improvement`, somente quando houver mudança real, validações aprovadas e diff não vazio.
14. Após push, confirme com Git que `HEAD` corresponde a `origin/hermes/skill-improvement` e que a árvore está limpa.
15. Quando não houver mudança segura, não faça commit. Entregue o relatório pelo destino configurado no cron, sem criar arquivo ou commit apenas para registrar a execução.
16. Quando faltar ferramenta, credencial, contexto ou decisão humana, pare e registre bloqueio. Não invente alternativa nem contorne o bloqueio.

Formato final do relatório:

- cenário escolhido
- hipótese
- evidência inspecionada
- comandos e resultados
- mudança aplicada ou razão para não mudar
- commit e push, se houver
- pendências ou bloqueios
- confirmação de que `main` não foi alterada
