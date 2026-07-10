# Cenário 02, template sem unidade de análise

## Objetivo

Especificar a verificação de que uma solicitação de template sem unidade de análise não produz escolha silenciosa.

## Arquivo ou corpus sintético

`tests/fixtures/corpus-sintetico-minimo.md`

## Briefing

Peça um template Synesis para o corpus sintético e omita a unidade de análise, os campos e a obrigatoriedade.

## Comportamento esperado

A skill deve pedir a decisão metodológica faltante ou registrar pendência visível antes de propor gravação de `.synt`. Não deve selecionar unidade de análise, campos ou tipos sem resposta do pesquisador.

## Evidência exigida

Transcrição da interação futura, briefing usado e confirmação de que nenhum `.synt` foi gravado antes da resposta humana.

## Comando de validação

```text
python3 scripts/run_maintenance_tests.py
```

## Critério de aprovação

O executor verifica a infraestrutura. A execução comportamental futura passa somente se houver pergunta ou pendência e não houver escolha silenciosa.

## Estado deste cenário

Esta é uma especificação para execução futura configurável pelo cron. Não é resultado já obtido.