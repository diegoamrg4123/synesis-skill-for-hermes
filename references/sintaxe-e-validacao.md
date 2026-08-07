# Sintaxe e validação do Synesis

## Escopo desta referência

As regras históricas abaixo foram consolidadas para o compilador 0.6.0. As mudanças de sintaxe e ajuda foram revistas contra o código oficial e a execução do Synesis 0.11.0 em 2026-08-07. Confirme a versão instalada quando houver diferença.

A prova final é a execução real de `compile --stats`.

## Regras gerais

- palavras da linguagem não diferenciam maiúsculas e minúsculas
- comentários começam com `#`
- indentação faz parte da sintaxe
- não misture tabs e espaços
- grave UTF-8 sem BOM
- mantenha cada valor de campo em uma linha
- use `snake_case` sem acento para conceitos que aparecerão em chains

## Projeto `.synp`

```text
PROJECT pesquisa_exemplo

TEMPLATE "template.synt"
INCLUDE BIBLIOGRAPHY "referencias.bib"
INCLUDE ANNOTATIONS "anotacoes/entrevistas.syn"
INCLUDE ONTOLOGY "ontologia/conceitos.syno"
INCLUDE DATASET "dados/*.toml"

METADATA
    version: 1.0
    author: Nome
    created: 2026-07-10
END METADATA

DESCRIPTION
Descrição do projeto e da unidade de análise.
END DESCRIPTION

END PROJECT
```

Os caminhos são relativos à pasta do `.synp`. As linhas de DESCRIPTION ficam sem indentação. As linhas de METADATA ficam indentadas.

## Template `.synt`

O cabeçalho `TEMPLATE nome` é opcional na versão 0.6.0. Não use `version:` ou `author:` soltos no template. Registre metadados como comentários. Não use `END TEMPLATE`.

```text
TEMPLATE pesquisa_exemplo
# versão 1.0

SOURCE FIELDS
    OPTIONAL access_date
END SOURCE FIELDS

ITEM FIELDS
    REQUIRED quote
    REQUIRED memo
    OPTIONAL code
    OPTIONAL chain
END ITEM FIELDS

ONTOLOGY FIELDS
    REQUIRED description
    OPTIONAL topic
END ONTOLOGY FIELDS

FIELD quote TYPE QUOTATION
    SCOPE ITEM
    DESCRIPTION Excerto literal da fonte
END FIELD

FIELD memo TYPE MEMO
    SCOPE ITEM
    DESCRIPTION Interpretação aprovada pelo pesquisador
    GUIDELINES
        Ancorar a interpretação no trecho citado.
    END GUIDELINES
END FIELD

FIELD code TYPE CODE
    SCOPE ITEM
    DESCRIPTION Conceitos aplicados ao item
END FIELD

FIELD chain TYPE CHAIN
    SCOPE ITEM
    ARITY >= 2
    DESCRIPTION Relação entre conceitos
    RELATIONS
        FAVORECE: X aumenta ou facilita Y
        INIBE: X reduz ou impede Y
    END RELATIONS
END FIELD

FIELD description TYPE TEXT
    SCOPE ONTOLOGY
END FIELD

FIELD topic TYPE TOPIC
    SCOPE ONTOLOGY
END FIELD

FIELD access_date TYPE DATE
    SCOPE SOURCE
END FIELD
```

Cada campo listado num bloco de escopo precisa de um bloco FIELD. O `SCOPE` precisa corresponder ao bloco em que o campo foi listado. Essa consistência é verificada por `compile`, não por `validate-template`.

Na versão 0.11.0, consulte a matriz executável antes de escrever ou corrigir um campo.

```bash
synesis help-field
synesis help-field CHAIN
```

O primeiro comando lista os dez tipos. O segundo informa propriedades obrigatórias, opcionais e proibidas para `CHAIN`, com os códigos de erro correspondentes.

## Tipos de campo

| Tipo | Uso comum | Configuração adicional |
|---|---|---|
| QUOTATION | Evidência literal | Nenhuma |
| MEMO | Interpretação | GUIDELINES opcional |
| CODE | Conceito da ontologia | Nenhuma |
| CHAIN | Relação entre conceitos | ARITY obrigatória, RELATIONS opcional |
| TEXT | Texto livre | Nenhuma |
| DATE | Data | Convenção recomendada AAAA-MM-DD |
| SCALE | Número em intervalo | FORMAT obrigatório |
| ENUMERATED | Lista fechada sem ordem | VALUES obrigatório |
| ORDERED | Lista ordenada | VALUES com índices |
| TOPIC | Grupo de ontologia | Valor sem espaço |

Na versão 0.11.0, `VALUES` só se aplica a `ORDERED` e `ENUMERATED`. Usá-lo em `QUOTATION`, `MEMO`, `CODE`, `CHAIN`, `TEXT`, `DATE`, `SCALE` ou `TOPIC` produz `SYNESIS_E086`.

## Valores fechados

```text
FIELD confianca TYPE ENUMERATED
    SCOPE ITEM
    VALUES
        baixa: evidência insuficiente no trecho isolado
        media: evidência parcial
        alta: evidência direta
    END VALUES
END FIELD

FIELD intensidade TYPE ORDERED
    SCOPE ITEM
    VALUES
        [1] fraca: menção lateral
        [2] forte: tema central
    END VALUES
END FIELD
```

Cada valor precisa de descrição. Um valor sem descrição pode causar erro de sintaxe apresentado pelo `compile` como template não encontrado. Use `validate-template` para localizar o parse quebrado.

## Datasets TOML

O Synesis 0.10.0 adicionou datasets estruturados como origem de valores e contexto. O `.synp` inclui os arquivos.

```text
INCLUDE DATASET "dados/*.toml"
```

O bloco de campos declara a origem de cada valor.

```text
SOURCE FIELDS
    REQUIRED researcher_id ON DATASET "informacoes_pessoais.id_lattes"
    OPTIONAL bolsa ON DATASET "informacoes_pessoais.bolsa_produtividade"
END SOURCE FIELDS
```

O caminho fica dentro da string. Um filtro pode usar a forma `projetos[ano_conclusao=Atual]`.

`CONTEXT FROM DATASET` pertence ao bloco `FIELD`, não ao bloco `SOURCE FIELDS` ou `ITEM FIELDS`.

```text
FIELD chain TYPE CHAIN
    SCOPE ITEM
    ARITY >= 2
    CONTEXT FROM DATASET "linhas_de_pesquisa", "projetos[ano_conclusao=Atual]"
    GUIDELINES
        Use o contexto somente conforme os critérios aprovados.
    END GUIDELINES
END FIELD
```

`ON DATASET` indica origem de valor. `CONTEXT FROM DATASET` fornece insumo para processar um campo. A forma antiga de `CONTEXT` dentro do bloco de campos não tem compatibilidade retroativa na 0.10.0.

Um campo obrigatório sem valor no dataset produz `SYNESIS_E085`. Um campo opcional ausente não deve produzir esse erro na 0.10.0 ou posterior. O JSON v3.0 mantém a seção `dataset` separada de `bibliography`.

## Required e bundle

```text
ITEM FIELDS
    REQUIRED quote, memo, code
END ITEM FIELDS
```

A linha acima declara três campos obrigatórios independentes.

```text
ITEM FIELDS
    REQUIRED quote
    REQUIRED BUNDLE memo, chain
END ITEM FIELDS
```

O bundle exige que memo e chain apareçam juntos e com a mesma quantidade. Use bundle apenas após decisão do pesquisador.

## Anotações `.syn`

```text
SOURCE @silva2026
    access_date: 2026-07-10
END SOURCE

ITEM @silva2026
    quote: A instituição criou uma regra para revisar todo conteúdo automatizado.
    memo: A regra introduz revisão humana antes da publicação.
    code: revisao_humana, governanca
    chain: regra_institucional -> FAVORECE -> revisao_humana
END ITEM
```

Cada ITEM precisa de SOURCE correspondente no mesmo arquivo. O `@bibref` precisa existir no `.bib`.

Múltiplos códigos usam vírgula. Valores de campo ficam numa linha, mesmo quando longos.

## Ontologia `.syno`

```text
ONTOLOGY revisao_humana
    description: Conferência realizada por uma pessoa antes do uso ou publicação do resultado.
    topic: governanca
END ONTOLOGY
```

O nome precisa ser utilizável nas chains. O compilador aceita algumas formas inconvenientes, mas espaço dentro de chain causa erro. Mantenha a convenção aprovada pelo projeto.

Descrições idênticas em conceitos diferentes podem passar sem aviso. Compare-as antes do portão O.

## Chains

Chain qualificada:

```text
chain: pressao_tempo -> INIBE -> verificacao
```

Chain estendida:

```text
chain: capacitacao -> FAVORECE -> confianca -> FAVORECE -> adocao
```

A sequência alterna conceito, relação e conceito. Todos os conceitos precisam existir na ontologia e todas as relações precisam estar no template.

A aridade conta conceitos. Uma chain com dois conceitos tem aridade dois.

Uma linha com apenas `chain: conceito` pode ser descartada sem aviso. Confira a contagem de chains no `--stats`.

## Bibliografia `.bib`

Use tipos padrão.

```text
@article{silva2026,
  author = {Ana Silva},
  title = {Governança de sistemas automatizados},
  year = {2026}
}

@misc{entrevista_maria2026,
  author = {Maria da Silva},
  title = {Entrevista sobre adoção tecnológica},
  year = {2026},
  type = {Entrevista semiestruturada}
}
```

Tipos não padrão como `@interview` podem ser descartados. Use `@misc` e descreva a natureza da fonte.

## Comandos de validação

```bash
synesis --version
synesis check anotacoes.syn
synesis validate-template template.synt
synesis compile projeto.synp --stats
synesis help-field TEXT
synesis export-snippets -o snippets/synesis.code-snippets
```

`check` e `validate-template` verificam sintaxe. Apenas `compile --stats` faz a validação semântica completa do projeto na versão 0.6.0.

Exportação:

```bash
synesis compile projeto.synp --json resultados/projeto.json
synesis compile projeto.synp --csv resultados/csv
synesis compile projeto.synp --xls resultados/projeto.xlsx
synesis compile projeto.synp --alpaca resultados/projeto.jsonl
```

Não existe `--output` na versão 0.6.0 nem na 0.11.0.

`synesis export-snippets` não exporta resultados de pesquisa. Ele gera snippets de blocos `FIELD` para editores. Na 0.11.0, o arquivo contém dez snippets derivados da matriz do validador. Trate o cabeçalho gerado como aviso para não editar o arquivo manualmente.

## Ligação multiprojeto

Dois ou mais projetos ativam o link step.

```bash
synesis compile lattes.synp abstracts.synp
synesis compile lattes.synp abstracts.synp --stats
```

Um campo `IDENTIFIES researcher` declara a chave de uma entidade. Um campo `REFERS TO researcher` declara uma referência à mesma entidade. Ambos precisam ter `SCOPE SOURCE`.

Na versão 0.11.0, a saída padrão inclui `Ligacao entre projetos`, derivada dos templates, e `Resolucao das ligacoes`, derivada dos dados. A estrutura pode aparecer mesmo quando o projeto de origem ainda não tem `SOURCE`.

Interprete os estados separadamente.

- `aguardando coleta` significa que o projeto de origem não tem `SOURCE`
- `0 resolvidas` significa que há dados, mas nenhum valor casou
- `N orfaos` indica valores de `REFERS TO` sem `IDENTIFIES` correspondente

O sumário pode avisar que há rótulos sem nenhuma aresta. Esse aviso impede que a mensagem de projetos linkados seja lida como sucesso completo. Com `--stats`, confira a tabela por membro, a linha `TOTAL`, o bloco de ontologia e as contagens de arestas e órfãos.

## Ordem de correção

1. template
2. projeto
3. bibliografia
4. ontologia
5. anotações

Leia todos os diagnósticos antes de editar. Um erro inicial pode produzir mensagens em cascata.

Correção mecânica pode ser executada. Correção que muda conceito, relação, campo ou unidade volta ao pesquisador.

## Armadilhas silenciosas

| Situação | Resultado observado |
|---|---|
| Valor em várias linhas | Pode ser truncado na primeira linha |
| Chain sem seta | Pode virar nula e desaparecer |
| Data inválida | Pode ser aceita |
| Campo usado fora do escopo | Pode ser aceito |
| Descrições de conceitos iguais | Podem passar sem aviso |
| Projeto sem chains | Não produz tabela de chains |
| Alpaca com saídas iguais | Pode fundir exemplos com citações diferentes |

## Diagnósticos conhecidos

- `Template 'x.synt' nao encontrado` com o arquivo presente costuma indicar falha de parse
- BOM pode causar token inesperado na primeira linha
- aviso de código não definido pode aparecer duas vezes para uma ocorrência
- `--strict` pode retornar código 1 mantendo o rótulo `[WARNING]`
- erro semântico pode apontar para o início do bloco, não para a linha exata do campo

## Critérios de conclusão

- [ ] Arquivos gravados em UTF-8 sem BOM
- [ ] Valores em uma linha
- [ ] `compile --stats` terminou com código 0
- [ ] Não há erro semântico
- [ ] Avisos foram apresentados ao pesquisador
- [ ] Contagens correspondem ao corpus esperado
- [ ] Arquivos exportados foram verificados no disco
