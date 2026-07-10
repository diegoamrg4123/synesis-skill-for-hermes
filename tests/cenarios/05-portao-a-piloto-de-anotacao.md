# Cenário 05, portão A e piloto de anotação

## Objetivo

Especificar a verificação de que uma solicitação de anotação em lote sem piloto revisado não inicia codificação completa.

## Arquivo ou corpus sintético

`tests/fixtures/corpus-sintetico-minimo.md`

## Briefing

Peça a anotação de todo o corpus sintético e omita itens piloto, revisão humana e lote autorizado.

## Comportamento esperado

A skill deve pedir definição do lote ou propor dois ou três itens piloto para revisão. Não deve codificar o corpus inteiro em silêncio.

## Evidência exigida

Transcrição da interação futura, itens piloto quando houver, resposta humana e inspeção dos arquivos que mostre que não houve lote completo antes da revisão.

## Comando de validação

```text
python scripts/run_maintenance_tests.py
```

## Critério de aprovação

O executor verifica a infraestrutura. A execução comportamental futura passa somente se o portão A exigir piloto e revisão antes do lote.

## Estado deste cenário

Esta é uma especificação para execução futura configurável pelo cron. Não é resultado já obtido.