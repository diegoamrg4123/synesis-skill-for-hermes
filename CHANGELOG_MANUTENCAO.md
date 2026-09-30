# Changelog de manutenção

Este arquivo registra mudanças reais e comprovadas. A manutenção automática ocorre somente na branch `hermes/skill-improvement`. Atualizações solicitadas por Diego são identificadas como revisão humana, sem autorizar publicação automática.

Não adicione entrada quando uma execução diária não encontrar alteração comprovada. Nesse caso, produza apenas relatório de execução sem commit.

## 2026-09-30

Cenário: revisão humana das rotas de codificação com Hermes e Synesis Coder
Hipótese: a skill descrevia principalmente execução externa do Coder e não orientava a codificação direta ou a preparação de prompts com execução pelo Hermes
Evidência: inspeção do código oficial do Coder 0.12.0, dependência Synesis 0.13.1, modos com `--prompt-only`, limites do dump, cliente de inferência e documentação atual do Hermes. O novo teste falhou por ausência da referência antes da atualização
Arquivos alterados: SKILL, README, referências de ecossistema e fluxos, nova referência de codificação, testes de regressão e changelog
Validações executadas: 11 testes de manutenção, `python3 scripts/validate_skill.py`, `python3 scripts/run_maintenance_tests.py` com descoberta em perfil temporário e `git diff --check`
Resultado: skill 1.4.0 documenta rota básica e híbrida, preserva a rota nativa e deixa integrações avançadas sem configuração. A revisão separada, proveniência, normalização e incorporação mantêm os portões humanos
Pendências humanas: autorizar ambiente compatível e piloto de inferência antes de tratar a integração híbrida como validada ponta a ponta. Nenhum pacote, serviço ou agendamento foi instalado ou alterado nesta revisão

## 2026-08-24

Cenário: confirmação da hierarquia ontológica e do limite de exportação semântica
Hipótese: a habilidade podia confundir chains de evidência em `ITEM` com a relação taxonômica `parent` no `ONTOLOGY`, ou atribuir à 0.12.0 exportadores OWL/RDF inexistentes
Evidência: inspeção do código oficial nas tags 0.11.0 e 0.12.0, projeto mínimo compilado no Synesis 0.12.0 com `parent: mamifero -> animal`, JSON contendo `parent_chains` e `indices.hierarchy`, e ajuda da CLI sem `--owl`, `--rdf` ou `--ttl`
Arquivos alterados: SKILL, README, referência de ontologia e chains, testes de regressão e changelog
Validações executadas: projeto mínimo compilado com JSON, testes de manutenção, validador da skill, executor de manutenção e `git diff --check`
Resultado: skill 1.3.0 registra a hierarquia estrutural já presente ao menos na 0.11.0, preserva o portão O e delimita as exportações nativas a JSON, CSV, XLS e Alpaca JSONL
Pendências humanas: decidir, em projeto futuro, se uma conversão para OWL/RDF é necessária e qual vocabulário semântico a orientará

Cenário: atualização da skill para o Synesis 0.12.0
Hipótese: a skill não registrava a forma canônica de `ORDERED`, `SYNESIS_E087`, `SYNESIS_E088`, agrupamento de diagnósticos e rótulos auxiliares no JSON
Evidência: release oficial v0.12.0, execução isolada de projetos mínimos para `SYNESIS_E087` e `SYNESIS_E088`, inspeção do JSON e 96 testes upstream focados aprovados
Arquivos alterados: SKILL, README, referências de sintaxe, ecossistema e decisões metodológicas, testes de regressão e changelog
Validações executadas: checagens específicas do Synesis 0.12.0, testes de regressão locais, validador da skill, executor de manutenção, compilação Python e `git diff --check`
Resultado: skill 1.2.0 documenta a migração por projeto, exige compilação semântica para os novos diagnósticos e separa a release verificada do executável principal ainda na 0.11.0
Pendências humanas: atualizar o executável principal para 0.12.0 é decisão separada

## 2026-08-17

Cenário: complemento da mudança de ecossistema após a liberação dos módulos do ecossistema no PyPI
Hipótese: o remoto já registrava o compilador 0.11.0 e o `synesis-graph` 0.7.0, mas a atualização conjunta, o coder 0.8.0 publicado e a extensão 0.11.0 não constavam da referência
Evidência: lançamentos oficiais `synesis 0.11.0`, `synesis-lsp 0.22.0`, `synesis-graph 0.7.0` e `synesis-coder 0.8.0`
Arquivos alterados: referência de ecossistema, changelog e cópia instalada da skill
Validações executadas: `python scripts/validate_skill.py`, `python -m unittest discover -s tests -p test_maintenance.py -v`, `python scripts/run_maintenance_tests.py` e `git diff --check`
Resultado: comando de atualização conjunta documentado, extensão descrita na versão 0.11.0, exigência do `synesis-lsp` 0.22.0 para campos MEMO registrada e coder 0.8.0 descrito como publicado
Pendências humanas: nenhuma

## 2026-07-20

Cenário: revisão integral da infraestrutura e execução dos cenários 01 a 05
Hipótese: a seleção sem estado podia repetir o mesmo cenário e o validador não inspecionava o próprio `.gitattributes`
Evidência: testes de regressão falharam antes das correções, os cinco cenários foram executados e nenhum arquivo Synesis foi gravado antes dos portões
Arquivos alterados: validador, executor, workflow, protocolo, prompt do cron, README, changelog e testes de regressão
Validações executadas: `python -m unittest discover -s tests -p test_maintenance.py -v`, `python scripts/validate_skill.py`, `python scripts/run_maintenance_tests.py`, `python -m py_compile scripts/validate_skill.py scripts/run_maintenance_tests.py tests/test_maintenance.py` e `git diff --check`
Resultado: rotação semanal definida, relatório sem mudança destinado à entrega do cron, correção de CRLF coberta por regressão e CI ampliado
Pendências humanas: nenhuma

Cenário: auditoria antes da publicação pública
Hipótese: a referência histórica 0.6.0 podia ser interpretada como recomendação atual e o nome `synesis2graph` não correspondia ao repositório vigente
Evidência: o Synesis 0.9.0 passou no teste básico, o changelog oficial registrou correções de segurança na 0.7.0 e a organização mantém `synesis-graph`
Arquivos alterados: README, SKILL, referência de ecossistema, workflow, changelog e testes de regressão
Validações executadas: `python -m unittest discover -s tests -p test_maintenance.py -v`, `python scripts/validate_skill.py`, `python scripts/run_maintenance_tests.py`, `python -m py_compile scripts/validate_skill.py scripts/run_maintenance_tests.py tests/test_maintenance.py` e `git diff --check`
Resultado: compatibilidade delimitada, versão mínima segura registrada, integração de grafos atualizada e GitHub Actions com permissão de leitura e actions fixadas por SHA
Pendências humanas: tornar o repositório público após revisar o diff

## 2026-07-10

Cenário: preservação de LF em clones Windows
Hipótese: um clone com `core.autocrlf=true` convertia arquivos para CRLF e causava falha falsa no validador
Evidência: o validador rejeitou arquivos de texto de um clone Windows sem alteração de conteúdo
Arquivos alterados: `.gitattributes` e `README.md`
Validações executadas: `python scripts/validate_skill.py`, `python scripts/run_maintenance_tests.py` e `git diff --check`
Resultado: preservação de LF em clones Windows com `* text=auto eol=lf`
Pendências humanas: nenhuma

## Modelo de entrada

```text
## AAAA-MM-DD

Cenário: <identificador>
Hipótese: <afirmação verificável>
Evidência: <saída bruta ou arquivos inspecionados>
Arquivos alterados: <lista>
Validações executadas: <comandos e resultado>
Resultado: <correção aplicada ou rejeitada>
Pendências humanas: <nenhuma ou descrição>
```
