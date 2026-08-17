# Changelog de manutenção

Este arquivo registra somente mudanças reais e comprovadas na branch `hermes/skill-improvement`.

Não adicione entrada quando uma execução diária não encontrar alteração comprovada. Nesse caso, produza apenas relatório de execução sem commit.

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
