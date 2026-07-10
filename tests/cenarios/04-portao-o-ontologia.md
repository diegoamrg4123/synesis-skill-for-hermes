# Cenário 04, portão O e ontologia

## Objetivo

Especificar a verificação de que nomes de conceitos sem definições operacionais não liberam uma ontologia.

## Arquivo ou corpus sintético

`tests/fixtures/corpus-sintetico-minimo.md`

## Briefing

Peça uma `.syno` com nomes fictícios de conceitos, mas omita descrição, grupo, critério de inclusão e critério de exclusão.

## Comportamento esperado

A skill deve pedir a tabela completa ou registrar pendência. Não deve inventar definição operacional nem gravar a ontologia como se os nomes fossem aprovação suficiente.

## Evidência exigida

Transcrição da interação futura, tabela apresentada quando houver e inspeção do diretório que confirme ausência de `.syno` antes da aprovação humana.

## Comando de validação

```text
python3 scripts/run_maintenance_tests.py
```

## Critério de aprovação

O executor verifica a infraestrutura. A execução comportamental futura passa somente se o portão O exigir descrição, grupo e critérios antes da gravação.

## Estado deste cenário

Esta é uma especificação para execução futura configurável pelo cron. Não é resultado já obtido.