---
name: synesis
version: 1.0.0
description: Use no Synesis com controle humano e automação pelo Hermes.
author: Diego Amorim Goulart e Hermes Agent
license: MIT
platforms: [windows, linux, macos]
metadata:
  hermes:
    tags: [synesis, pesquisa-qualitativa, ontologia, codificacao, metodologia]
    category: research
---

# Synesis para Hermes Agent

## Visão geral

Synesis é uma linguagem declarativa e um compilador para organizar, validar e exportar pesquisa qualitativa. O projeto reúne cinco tipos de arquivo.

| Extensão | Função |
|---|---|
| `.synp` | Ponto de entrada do projeto |
| `.synt` | Contrato metodológico com campos, tipos e relações |
| `.syn` | Fontes, itens e anotações |
| `.syno` | Ontologia de conceitos |
| `.bib` | Referências BibTeX |

O Hermes auxilia o pesquisador, executa a mecânica e mantém uma trilha verificável. O Hermes não escolhe sozinho a unidade de análise, os campos do template, a ontologia, as relações, as definições operacionais nem o grau de automação.

## Quando usar

Carregue esta skill quando o usuário:

- mencionar Synesis ou arquivos `.synp`, `.synt`, `.syn`, `.syno` e `.bib`
- quiser iniciar, revisar, validar, compilar ou exportar um projeto Synesis
- estiver codificando material qualitativo ou construindo uma ontologia
- pedir automação de anotações, revisão por agentes ou uso do `synesis-coder`
- precisar interpretar diagnósticos do compilador

Não trate esta skill como autorização para decidir o método. Pedidos vagos de automação ainda exigem os portões descritos abaixo.

## Regra de autoridade

A autoridade segue esta ordem.

1. O pesquisador decide o método e pode rever qualquer decisão.
2. Os arquivos aprovados do projeto registram o estado metodológico vigente.
3. A execução real do compilador mostra o comportamento da versão instalada.
4. A documentação e esta skill orientam quando não há prova local.

Em conflito entre documentação e compilador, relate a divergência. Não altere o método apenas para silenciar um diagnóstico.

## Divisão de trabalho

### O Hermes executa sem perguntar

- localizar e ler os arquivos do projeto
- conferir instalação, versão e ajuda da CLI
- criar pastas já aprovadas
- escrever sintaxe que materialize decisões aprovadas
- corrigir formatação, indentação, caminhos e erros mecânicos
- compilar, exportar, inspecionar saídas e contar artefatos
- apresentar diferenças, estatísticas e amostras
- manter uma lista de pendências metodológicas

### O Hermes pergunta antes de agir

- definir ou mudar a unidade de análise
- criar ou alterar campos, tipos, obrigatoriedade e bundles do template
- criar ou mudar relações e aridade de chains
- criar, dividir, fundir, renomear ou redefinir conceitos
- escolher critérios de inclusão e exclusão
- decidir se uma interpretação cabe no corpus
- escolher o nível de automação
- ampliar o escopo de uma tarefa já aprovada

Use `clarify` para decisões com até quatro opções. Faça uma ou duas perguntas por vez. Cada opção deve explicar a consequência em linguagem comum. Use pergunta aberta quando o pesquisador precisar formular um critério próprio.

Se `clarify` não estiver disponível, faça a pergunta no chat e aguarde. Nunca transforme ausência da ferramenta em autorização para escolher.

## Três portões de aprovação

### Portão T para o template

Antes de gravar ou alterar qualquer `.synt`:

1. conduza a entrevista de `references/decisoes-metodologicas.md`
2. monte um rascunho integral
3. apresente o texto completo por seções
4. peça confirmação dos campos, tipos, obrigatoriedade, bundles, relações, aridade, guidelines e unidade de análise
5. grave somente após a aprovação explícita

Aprovação de um resumo não aprova o arquivo.

### Portão O para a ontologia

Antes de gravar ou reestruturar qualquer `.syno`, apresente uma tabela com uma linha por conceito e estas colunas.

- nome
- descrição
- grupo
- critério de inclusão
- critério de exclusão

O pesquisador pode aprovar, editar ou rejeitar cada lote. Aprovar apenas nomes ou grupos não aprova definições operacionais.

### Portão A para anotação em lote

Antes de codificar um corpus inteiro:

1. produza dois ou três itens piloto
2. apresente citação, memo, códigos, chains e demais campos
3. peça revisão do pesquisador
4. ajuste o procedimento conforme a resposta
5. só então processe o lote aprovado

Uma revisão depois do corpus inteiro não substitui o piloto.

## Níveis de automação

Pergunte no começo do projeto e quando houver mudança de fase.

| Nível | Papel do Hermes | Papel do pesquisador |
|---|---|---|
| Guiado | Explica, valida e corrige a mecânica | Escreve e decide cada bloco |
| Colaborativo | Redige rascunhos e executa após cada portão | Revisa decisões e artefatos antes da gravação |
| Automatizado com revisão | Processa lotes aprovados e produz auditoria | Aprova método, piloto, amostras e mudanças |

O nível automatizado não suspende os portões T, O e A.

## Fluxo de trabalho

### Fase 0, diagnóstico

1. Procure projetos existentes com `search_files` antes de propor arquivos.
2. Leia `.synp`, `.synt`, `.syno`, `.syn` e `.bib` relevantes com `read_file`.
3. Identifique a pergunta de pesquisa, abordagem, fontes, unidade de análise, estágio do trabalho e destino das exportações.
4. Pergunte o nível de automação.
5. Registre decisões e lacunas em um arquivo do projeto, nunca apenas na memória global do Hermes.

Conclusão da fase, o estado atual está descrito e nenhuma lacuna metodológica foi preenchida em silêncio.

### Fase 1, ambiente

1. Consulte `references/sintaxe-e-validacao.md` e `references/ecossistema.md`.
2. Confirme a versão instalada com execução real.
3. Confira `synesis --help` e `synesis compile --help` se a versão diferir da referência desta skill.
4. Se não houver projeto, use `synesis init` apenas para verificar o ambiente. Não use o conteúdo gerado como modelo sem revisão.

Conclusão da fase, a versão e os comandos disponíveis foram confirmados por saída real.

### Fase 2, projeto e template

1. Conduza a entrevista metodológica.
2. Passe pelo portão T.
3. Grave `.synt` e `.synp` em UTF-8 sem BOM.
4. Execute a compilação semântica completa.
5. Apresente diagnósticos e impacto de qualquer correção.

Conclusão da fase, o template integral foi aprovado e o projeto compila sem erros.

### Fase 3, ontologia

1. Pergunte se a estratégia é dedutiva, indutiva ou mista.
2. Proponha conceitos em lotes pequenos.
3. Compare nomes e descrições para detectar sobreposição que o compilador não detecta.
4. Passe pelo portão O.
5. Grave, compile e mostre as mudanças.

Conclusão da fase, todos os conceitos gravados têm definição aprovada e fronteiras de uso compreensíveis.

### Fase 4, bibliografia e corpus

1. Use tipos BibTeX padrão.
2. Use `@misc` para entrevistas quando não houver tipo padrão adequado.
3. Confira se cada `SOURCE @bibref` existe no `.bib`.
4. Não altere citações para fazê-las caber numa interpretação.

Conclusão da fase, os vínculos bibliográficos compilam e a evidência original foi preservada.

### Fase 5, anotação

1. Defina o lote e a unidade de análise já aprovada.
2. Passe pelo portão A.
3. Codifique somente o lote autorizado.
4. Não crie conceito ou relação nova em silêncio. Mantenha propostas separadas até o portão correto.
5. Recompile a cada lote e apresente amostras e distribuição de códigos.

Conclusão da fase, todos os itens pertencem ao lote aprovado e as exceções estão registradas.

### Fase 6, validação e exportação

1. Execute `synesis compile projeto.synp --stats`.
2. Corrija primeiro template, depois projeto, bibliografia, ontologia e anotações.
3. Exporte apenas após compilação limpa, salvo pedido explícito para diagnóstico com `--force`.
4. Verifique no disco cada arquivo esperado.
5. Compare contagens de fontes, itens, ontologias e chains com o que foi aprovado.

Conclusão da fase, a saída do comando, o código de retorno e os artefatos no disco foram conferidos.

## Uso das ferramentas do Hermes

### `todo`

Use em trabalhos com várias fases. Um único item fica em andamento. Marque cada portão como tarefa própria quando houver risco de avançar cedo demais.

### `clarify`

Use para decisões do pesquisador. Não coloque as opções dentro do texto da pergunta quando a ferramenta aceitar escolhas separadas.

### `read_file` e `search_files`

Leia antes de editar. Procure definições e usos de campos e conceitos no projeto inteiro antes de renomear ou remover algo.

### `terminal`

Use para versão, ajuda, compilação, exportação, testes e Git. Não invente saída. No Windows, respeite o shell efetivamente fornecido pela instalação.

### `execute_code`

Use para inspeções mecânicas de muitos artefatos, contagens e tabelas. Não use um script para tomar decisão interpretativa.

### `delegate_task`

Use apenas depois que o método necessário para o subtrabalho estiver fechado. Subagentes não podem perguntar ao pesquisador e não conhecem a conversa do agente principal. Siga `references/fluxos-hermes.md`.

### Memória e histórico

Não grave decisões de um projeto Synesis na memória global como fonte única. Registre-as em comentários, documentação do projeto ou log de decisões. Use `session_search` como contexto secundário, nunca como prova do estado atual dos arquivos.

### Automação durável

Não use cron para atravessar um portão humano. Uma tarefa agendada pode validar ou gerar relatório de um projeto já aprovado, mas não pode criar template, ontologia ou novos critérios sem revisão presente.

## Multiagentes no Hermes

O agente principal mantém o diálogo e a autoridade metodológica. Subagentes executam trabalho delimitado.

Padrão seguro:

1. o agente principal lê o projeto e obtém as aprovações
2. um codificador recebe arquivos, unidade de análise, definições e lote explícitos
3. outro subagente revisa o resultado contra os mesmos critérios
4. o agente principal verifica arquivos e saídas brutas
5. divergências voltam ao pesquisador quando exigem julgamento

Não peça a um subagente para escolher conceitos, completar lacunas do briefing ou aprovar o trabalho de outro agente. A revisão por agente encontra inconsistências, mas não substitui a revisão do pesquisador.

## Linha de base histórica do Synesis 0.6.0

As regras abaixo foram testadas detalhadamente no Synesis 0.6.0. Em 2026-07-20, a versão atual era 0.9.0 e passou num teste básico com `--version`, `compile --help`, `init` e `compile --stats`.

Não recomende a instalação da versão 0.6.0. Use pelo menos 0.7.0, que corrigiu leitura fora da pasta do projeto, leitura sem limite de tamanho e injeção de fórmulas em CSV. Se a versão instalada diferir da linha de base, confirme as regras abaixo por execução antes de aplicá-las ao corpus.

- `check` e `validate-template` verificam sintaxe, não a semântica completa
- a validação completa é `synesis compile projeto.synp --stats`
- não existe flag `--output` nem comando `export`
- as exportações usam `--json`, `--csv`, `--xls` e `--alpaca`
- valores multilinha podem ser truncados sem aviso, mantenha cada valor em uma linha
- chain sem seta pode ser descartada sem aviso
- projeto sem chains não gera tabela de chains
- tipos BibTeX não padrão podem ser descartados
- o compilador rejeita BOM UTF-8
- `--strict` pode retornar falha mantendo o rótulo visual de aviso
- avisos de código ausente podem aparecer duplicados
- o Alpaca JSONL não representa um item por linha e pode fundir exemplos diferentes

Consulte `references/sintaxe-e-validacao.md` antes de escrever arquivos e confirme a versão instalada.

## Decisões não cobertas

Quando um pedido em lote deixar uma lacuna:

1. não invente aprovação
2. pare antes da ação irreversível ou metodológica
3. produza o artefato de revisão em arquivo separado quando isso ajudar
4. liste a lacuna, o impacto e as opções
5. aguarde o pesquisador

Um caminho conservador pode preservar arquivos e gerar diagnóstico. Ele não pode introduzir método novo.

## Armadilhas

1. Confundir autonomia com autoridade. O Hermes pode executar muito sem receber poder para decidir o método.
2. Delegar cedo. Um subagente sem contexto pode preencher lacunas como se fossem detalhes técnicos.
3. Aprovar por resumo. Template e ontologia precisam dos artefatos integrais dos portões.
4. Tratar compilação limpa como validação interpretativa. O compilador verifica consistência formal, não qualidade conceitual.
5. Guardar decisões só na conversa ou memória. O projeto precisa carregar sua própria trilha.
6. Confiar no relato do subagente. Leia arquivos, saídas e contagens.
7. Misturar codificação e revisão no mesmo agente. Separe papéis quando o lote justificar o custo.
8. Alterar a unidade de análise para acomodar dados difíceis. Volte ao pesquisador.

## Referências desta skill

| Arquivo | Carregar quando |
|---|---|
| `references/decisoes-metodologicas.md` | Antes de criar ou alterar template, ontologia ou nível de automação |
| `references/sintaxe-e-validacao.md` | Antes de escrever arquivos ou corrigir compilação |
| `references/ontologia-e-chains.md` | Ao trabalhar com conceitos, definições e relações |
| `references/fluxos-hermes.md` | Ao delegar codificação, revisão ou processamento em lote |
| `references/ecossistema.md` | Ao instalar, exportar ou integrar ferramentas externas |

## Verificação final

- [ ] O nível de automação foi acordado
- [ ] Toda decisão metodológica tem aprovação ou pendência visível
- [ ] Os portões aplicáveis foram respeitados
- [ ] Nenhum subagente decidiu método
- [ ] A unidade de análise permaneceu estável ou foi renegociada
- [ ] O projeto passou por `compile --stats`
- [ ] O código de retorno e os artefatos foram verificados
- [ ] As decisões ficaram registradas no projeto
- [ ] O pesquisador recebeu amostras, estatísticas e limitações
