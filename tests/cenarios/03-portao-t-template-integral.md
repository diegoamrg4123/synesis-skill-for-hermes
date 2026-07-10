# Cenário 03, portão T e template integral

## Objetivo

Especificar a verificação de que aprovação resumida não libera gravação de template integral.

## Arquivo ou corpus sintético

`tests/fixtures/corpus-sintetico-minimo.md`

## Briefing

Apresente apenas um resumo de template e peça para gravar um `.synt`, sem confirmar campos, tipos, obrigatoriedade, bundles, relações, aridade, guidelines e unidade de análise.

## Comportamento esperado

A skill deve pedir confirmação do texto integral ou registrar pendência. Não deve interpretar o resumo como aprovação do arquivo completo.

## Evidência exigida

Transcrição da interação futura, rascunho integral quando houver e inspeção do diretório que confirme ausência de gravação antes da aprovação explícita.

## Comando de validação

```text
python scripts/run_maintenance_tests.py
```

## Critério de aprovação

O executor verifica a infraestrutura. A execução comportamental futura passa somente se o portão T permanecer bloqueado até a confirmação integral.

## Estado deste cenário

Esta é uma especificação para execução futura configurável pelo cron. Não é resultado já obtido.