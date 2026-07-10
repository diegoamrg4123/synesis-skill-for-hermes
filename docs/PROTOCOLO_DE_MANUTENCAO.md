# Protocolo de manutenção experimental

## Finalidade

A manutenção diária verifica se a skill Synesis para Hermes mantém seus limites, instruções e arquivos de suporte. Cada execução usa cenários pequenos, sintéticos, reproduzíveis e auditáveis. O objetivo é encontrar falhas operacionais ou de redação e preparar correções com risco baixo na branch `hermes/skill-improvement`.

## Limite entre teste e pesquisa

O teste da skill não é pesquisa qualitativa real. Não usa pessoas, entrevistas, material privado, dados pessoais nem corpus de pesquisa. Um fixture sintético serve somente para exercitar instruções da skill. Nenhum resultado de cenário mede qualidade interpretativa, valida uma ontologia ou autoriza decisão metodológica.

## Ciclo diário

1. Formular uma hipótese limitada sobre um cenário.
2. Selecionar o cenário e o fixture sintético indicado.
3. Executar primeiro a infraestrutura determinística disponível.
4. Quando houver execução comportamental futura, conservar a saída bruta e os arquivos usados.
5. Comparar a evidência com o comportamento esperado do cenário.
6. Aplicar somente uma correção de baixo risco que seja ligada à evidência.
7. Rodar regressão com o executor e o validador.
8. Registrar relatório, ou changelog quando houver mudança real.

## Matriz de categorias

| Categoria | Alvo | Resultado esperado | Destino inicial |
|---|---|---|---|
| Descoberta | metadados e instalação temporária | a skill aparece como `synesis`, `research`, local e habilitada | correção automática de baixo risco |
| Arquivos | protocolo, cenários e fixtures | caminhos presentes e consistentes | correção automática de baixo risco |
| Redação operacional | instruções sem ambiguidade mecânica | texto preserva limites aprovados | correção automática de baixo risco |
| Portão T | template e unidade de análise | pergunta ou pendência antes de gravar | relatório para Diego |
| Portão O | ontologia e definições operacionais | pergunta ou pendência antes de gravar | relatório para Diego |
| Portão A | piloto e lote de anotação | revisão humana antes do lote | relatório para Diego |
| Autoridade metodológica | decisões do pesquisador | não há escolha silenciosa | relatório para Diego |

## Evidência para aceitar uma correção

Uma correção precisa conter, no mínimo:

- hipótese associada a um cenário identificado
- saída bruta ou inspeção de arquivo que mostre a falha
- diff pequeno que trate a falha observada
- resultado aprovado de `python scripts/validate_skill.py`
- resultado aprovado de `python scripts/run_maintenance_tests.py`
- resultado aprovado de `git diff --check`

Relato de agente não basta como evidência. A pessoa responsável deve conseguir ler a saída e os arquivos usados para reproduzir a conclusão.

## Correções automáticas de baixo risco

Podem ser aplicadas na branch de manutenção quando houver evidência:

- ajuste de caminho, nome de arquivo ou referência interna
- inclusão de fixture sintético pequeno
- correção de documentação operacional sem mudar autoridade
- melhoria de verificação determinística
- correção de erro mecânico de script com teste de regressão

## Casos que exigem relatório para Diego

Não alterar de modo autônomo:

- autoridade metodológica do pesquisador
- portões T, O ou A
- perguntas de decisão metodológica
- versão do frontmatter de `SKILL.md`
- licença, créditos, remotos ou credenciais
- escopo de uso de corpus real
- qualquer resultado que dependa de julgamento qualitativo

Nesses casos, registrar hipótese, cenário, saída bruta, impacto e decisão humana necessária. Não fazer commit apenas para registrar ausência de mudança.

## Regras de Git

- Nunca enviar alteração para `main`.
- Trabalhar somente em `hermes/skill-improvement`.
- Não criar commit quando a execução não mostrar mudança comprovada.
- Não criar commit vazio.
- Não reescrever o histórico remoto da branch de manutenção.

## Formato do changelog de manutenção

Uma entrada de mudança real deve conter:

```text
## AAAA-MM-DD

Cenário: <identificador>
Hipótese: <afirmação verificável>
Evidência: <saída bruta ou arquivos inspecionados>
Arquivos alterados: <lista>
Validações: <comandos e resultado>
Resultado: <correção aplicada ou rejeitada>
Pendências humanas: <nenhuma ou descrição>
```
