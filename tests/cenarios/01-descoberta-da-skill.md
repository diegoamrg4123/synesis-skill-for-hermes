# Cenário 01, descoberta da skill

## Objetivo

Verificar que uma cópia temporária da skill é descoberta pelo Hermes como `synesis`, na categoria `research`, com origem local e estado habilitado.

## Arquivo ou corpus sintético

Não usa corpus. Usa a cópia temporária criada pelo executor a partir dos arquivos da skill.

## Briefing

Instale somente a cópia temporária no perfil temporário e liste as skills disponíveis.

## Comportamento esperado

A listagem mostra uma linha com `synesis`, `research`, `local` e `enabled`.

## Evidência exigida

Saída bruta de `hermes skills list` no perfil temporário.

## Comando de validação

```text
python scripts/run_maintenance_tests.py
```

## Critério de aprovação

O executor termina com `MAINTENANCE_TESTS_OK` e informa a etapa de descoberta como aprovada.

## Estado deste cenário

Esta é uma especificação executada pelo executor determinístico. Não afirma teste comportamental de modelo.