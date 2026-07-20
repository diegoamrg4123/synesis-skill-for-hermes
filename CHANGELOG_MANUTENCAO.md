# Changelog de manutenção

Este arquivo registra somente mudanças reais e comprovadas na branch `hermes/skill-improvement`.

Não adicione entrada quando uma execução diária não encontrar alteração comprovada. Nesse caso, produza apenas relatório de execução sem commit.

## 2026-07-20

Cenário: revisão integral da infraestrutura e execução dos cenários 01 a 05
Hipótese: a seleção sem estado podia repetir o mesmo cenário e o validador não inspecionava o próprio `.gitattributes`
Evidência: testes de regressão falharam antes das correções, os cinco cenários foram executados e nenhum arquivo Synesis foi gravado antes dos portões
Arquivos alterados: validador, executor, workflow, protocolo, prompt do cron, README, changelog e testes de regressão
Validações executadas: `python -m unittest discover -s tests -p test_maintenance.py -v`, `python scripts/validate_skill.py`, `python scripts/run_maintenance_tests.py`, `python -m py_compile scripts/validate_skill.py scripts/run_maintenance_tests.py tests/test_maintenance.py` e `git diff --check`
Resultado: rotação semanal definida, relatório sem mudança destinado à entrega do cron, correção de CRLF coberta por regressão e CI ampliado
Pendências humanas: nenhuma

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
