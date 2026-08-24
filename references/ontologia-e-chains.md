# Ontologia e chains

## Autoridade

A ontologia e as chains contêm interpretação. O Hermes propõe, compara e verifica. O pesquisador aprova definições, fronteiras e relações.

## Estratégia da ontologia

Pergunte antes de criar conceitos.

| Estratégia | Procedimento |
|---|---|
| Dedutiva | Parte do referencial teórico aprovado |
| Indutiva | Começa mínima e recebe propostas durante a leitura |
| Mista | Mantém núcleo teórico e expansão controlada |

Em qualquer estratégia, conceitos novos passam pelo portão O.

## Anatomia de um conceito

Um conceito precisa de:

- nome estável
- descrição operacional
- grupo coerente
- critério de inclusão
- critério de exclusão
- exemplos ou casos limítrofes quando houver ambiguidade

Exemplo para revisão:

| nome | descrição | grupo | inclusão | exclusão |
|---|---|---|---|---|
| `pressao_tempo` | Uso de prazo curto para reduzir a verificação | `condicoes` | prazo, urgência ou ameaça de perda imediata | menção geral a rapidez sem efeito sobre verificação |

Os critérios podem ficar no log metodológico ou nas guidelines quando não forem campos do `.syno`.

## Nomes

Use a convenção aprovada pelo pesquisador. Para compatibilidade com chains, prefira:

- `snake_case`
- sem espaços
- sem acentos
- sem hífen
- um nome canônico por fenômeno

Registre sinônimos na descrição em vez de criar duplicatas por grafia.

## Descrições

Uma descrição precisa permitir decidir entre conceitos vizinhos. Compare perguntas como:

- O trecho descreve o conceito ou apenas menciona seu contexto?
- Qual evidência mínima permite aplicar o código?
- Que caso parecido deve ficar fora?
- Dois codificadores aplicariam a mesma fronteira?

O compilador 0.6.0 não avisa sobre descrições idênticas. O Hermes deve procurar sobreposição e levar a decisão ao pesquisador.

## Grupos

Escolha uma lógica de agrupamento e mantenha-a.

Possibilidades:

- dimensão analítica
- fase de processo
- ator ou posição social
- barreira, condição, mecanismo e desfecho
- nível individual, organizacional e institucional

Não misture lógicas sem registrar a razão.

## Granularidade

Sinais para revisão:

- código usado em um único item
- código aplicado a grande parte do corpus
- dois códigos que aparecem sempre juntos
- conceito definido por um exemplo específico
- conceitos que diferem apenas por ator, local ou tecnologia sem necessidade analítica

Esses sinais geram perguntas, não fusões automáticas.

## Hierarquia conceitual explícita

O Synesis 0.12.0 suporta uma hierarquia taxonômica dentro da ontologia. A capacidade já existia pelo menos na 0.11.0, portanto não é uma adição da release 0.12.0. Ela é distinta de uma chain anotada em um `ITEM`: não representa uma afirmação atribuída a uma fonte, mas uma decisão conceitual aprovada no portão O.

Para usá-la, declare um campo opcional `parent` do tipo `CHAIN` no escopo `ONTOLOGY` do template. A forma canônica no `.syno` é uma chain simples, de filho para pai:

```text
FIELD parent TYPE CHAIN
    SCOPE ONTOLOGY
    ARITY >= 2
END FIELD

ONTOLOGY FIELDS
    OPTIONAL parent
END ONTOLOGY FIELDS
```

```text
ONTOLOGY mamifero
    description: Animal que amamenta filhotes.
    parent: mamifero -> animal
END ONTOLOGY
```

Não escreva `mamifero -> IS_A -> animal`. O linker trata cada par consecutivo como filho e pai, portanto essa escrita inseriria `IS_A` como nó intermediário. O parser também reconhece `parents`, `is_a` e `isa`, mas use `parent` como convenção documental do projeto.

Após `synesis compile projeto.synp --json resultado.json`, confira dois níveis da saída:

- `ontology.<conceito>.parent_chains` preserva a declaração.
- `indices.hierarchy` materializa o mapeamento direto `filho -> pai`.

O índice derivado comporta um único pai imediato por conceito. Não modele múltipla herança como se estivesse preservada no índice sem uma decisão explícita e inspeção do JSON gerado.

Essa estrutura dá forma computável à taxonomia, mas não substitui as definições, os critérios de inclusão e exclusão, nem o portão O.

## Evolução segura

### Adicionar

Apresente definição e critérios, passe pelo portão O, grave e compile.

### Renomear

1. compile a linha de base
2. procure o nome em códigos e chains
3. explique o impacto
4. obtenha aprovação
5. altere todas as ocorrências
6. recompile
7. compare as contagens

### Dividir

Crie propostas para os conceitos novos. Revise com o pesquisador cada ocorrência do conceito anterior. Não distribua automaticamente os itens quando houver interpretação.

### Fundir

Mostre diferenças de definição, ocorrências e efeito sobre frequências. O pesquisador escolhe o conceito resultante e a nova descrição.

### Remover

Procure todos os usos. Um conceito usado não pode desaparecer sem decidir o destino das ocorrências.

## Portão O

Antes de gravar, apresente a tabela completa do lote. A aprovação precisa ocorrer depois da apresentação.

Se o pesquisador aprovar apenas nomes ou grupos, mantenha as definições como pendentes.

## Chains

Chains representam relações entre conceitos. Elas não substituem a ontologia.

Padrões para discussão:

```text
barreira -> INIBE -> resultado
facilitador -> FAVORECE -> resultado
causa -> FAVORECE -> mediador -> FAVORECE -> resultado
```

Use chains separadas para caminhos independentes.

```text
fator_a -> FAVORECE -> resultado
fator_b -> INIBE -> resultado
```

Uma chain estendida indica sequência. Chains separadas indicam caminhos distintos.

## Escolha da relação

Pergunte quando houver mais de uma leitura possível.

- A direção é de A para B ou de B para A?
- A fonte afirma causalidade ou apenas associação?
- O termo representa condição, mecanismo ou resultado?
- Há mediador sustentado pela citação?
- A relação escolhida tem definição aprovada?

O compilador verifica o nome da relação, não se a leitura é adequada.

## Quando não usar chain

- descrição sem relação dirigida
- associação incerta sem definição aceita
- classificação taxonômica no `ITEM`: se a taxonomia for aprovada, registre-a como `parent` no `ONTOLOGY`, não como evidência atribuída à fonte
- relação inferida além do trecho
- tentativa de ligar códigos apenas porque aparecem juntos

Use código e memo quando a chain não estiver sustentada.

## Revisão de um lote

A cada lote aprovado:

1. compile o projeto
2. confira frequência e distribuição dos códigos
3. confira relações usadas
4. liste conceitos propostos e não aprovados
5. amostre itens comuns e casos limítrofes
6. leve mudanças ao pesquisador
7. atualize a ontologia apenas após o portão O

## Uso de IA

Uma IA pode sugerir definições, grupos e relações. Trate a saída como rascunho.

Falhas a procurar:

- generalização excessiva
- conceitos duplicados por grafia
- definição circular
- relação causal inferida sem evidência
- mistura de níveis analíticos
- mudança da unidade de análise

Um revisor subagente pode encontrar inconsistências. O pesquisador resolve as decisões interpretativas.

## Critérios de conclusão

- [ ] Estratégia da ontologia aprovada
- [ ] Cada conceito tem definição e fronteira de uso
- [ ] O portão O foi registrado
- [ ] Relações têm definições aprovadas
- [ ] Nenhuma chain excede a evidência da citação
- [ ] Mudanças foram aplicadas em todos os usos
- [ ] O projeto foi recompilado
