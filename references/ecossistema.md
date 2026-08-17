# Ecossistema e execução

## Compilador verificado

A referência empírica detalhada antiga desta skill é o Synesis 0.6.0. Ela é uma linha de base histórica, não uma recomendação de instalação.

Em 2026-08-07, a versão 0.11.0 foi instalada com `uv tool install synesis==0.11.0`. Foram verificados `--version`, ajuda geral, `compile --help`, `help-field`, `export-snippets` e uma compilação multiprojeto. Também passaram 69 testes oficiais das áreas de dataset, descrição de campos, snippets e linkagem.

A versão 0.10.0 introduziu datasets TOML e mudou a licença do compilador. A versão 0.11.0 acrescentou a referência executável de campos, snippets derivados, o erro `SYNESIS_E086` e a exibição da topologia multiprojeto.

A versão 0.7.0 corrigiu leitura fora da pasta do projeto, leitura sem limite de tamanho e injeção de fórmulas em CSV. Se a versão instalada for anterior, pare antes de processar projeto não confiável e proponha a atualização ao pesquisador.

```bash
python -m pip install synesis
synesis --version
synesis --help
synesis compile --help
synesis help-field CHAIN
synesis export-snippets --help
```

No Windows, o executável pode ficar numa pasta `Scripts` fora do PATH. Use o caminho informado pelo instalador ou ajuste o PATH. O pacote 0.6.0 não oferece `python -m synesis` como substituto garantido.

## Licença do compilador

As versões até 0.9.0 foram publicadas sob MIT. A partir da 0.10.0, o código-fonte declara `AGPL-3.0-only AND LicenseRef-Synesis-data-output-exception`.

A Synesis Data-Output Exception informa que entradas do usuário e saídas geradas, como JSON, CSV, Excel, Alpaca JSONL e artefatos de grafo, não recebem a obrigação de copyleft apenas por terem sido processadas pelo Synesis. A AGPL continua aplicável ao compilador e aos componentes cobertos quando modificados, distribuídos ou oferecidos como serviço.

A saída de `synesis --version` do pacote 0.11.0 publicado no PyPI ainda mostra uma mensagem de transição que menciona MIT e AGPL pendente. O `pyproject.toml`, `LICENSE`, `LICENSE.exception` e `NOTICE` da tag oficial v.0.11.0 registram a licença nova. Não use a linha resumida da CLI como única fonte para decisão jurídica.

A licença MIT desta skill é independente da licença do compilador Synesis.

## Inicialização

```bash
synesis init
```

Na versão 0.6.0, `init` não usa `--name` e cria uma estrutura plana. O projeto gerado serve para provar que o ambiente funciona. Ele não deve ser tratado como template metodológico aprovado.

O arquivo de anotações gerado pode conter valor multilinha que perde conteúdo na exportação. Reescreva os campos após o portão T.

## Validação

```bash
synesis check arquivo.syn
synesis validate-template template.synt
synesis compile projeto.synp --stats
```

Os dois primeiros comandos verificam sintaxe. O terceiro realiza a validação semântica completa.

## Referência executável e snippets

Na versão 0.11.0, consulte os tipos de campo e a matriz da versão instalada.

```bash
synesis help-field
synesis help-field TEXT
synesis help-field CHAIN
```

O comando mostra propriedades obrigatórias, opcionais e proibidas. Ele confirmou que `VALUES` só se aplica a `ORDERED` e `ENUMERATED`. Nos outros oito tipos, a propriedade produz `SYNESIS_E086`.

Para gerar snippets de editor:

```bash
synesis export-snippets -o snippets/synesis.code-snippets
```

Na execução verificada, foram gerados dez snippets. O snippet de `CHAIN` continha `ARITY` e não continha `VALUES`. O arquivo gerado deve ser regenerado pelo compilador, não mantido por edição manual.

## Exportação

```bash
synesis compile projeto.synp --json resultados/projeto.json
synesis compile projeto.synp --csv resultados/csv
synesis compile projeto.synp --xls resultados/projeto.xlsx
synesis compile projeto.synp --alpaca resultados/projeto.jsonl
```

A CLI 0.6.0 não oferece `--output` nem comando `export`.

A exportação pode não imprimir confirmação dos arquivos. Verifique o disco.

## Ligação multiprojeto

Dois ou mais caminhos `.synp` no mesmo comando ativam o link step.

```bash
synesis compile lattes.synp abstracts.synp
synesis compile lattes.synp abstracts.synp --stats
```

`IDENTIFIES` declara o campo que identifica uma entidade. `REFERS TO` declara uma referência à mesma entidade. Os dois modificadores se aplicam a campos com `SCOPE SOURCE`.

Na versão 0.11.0, a saída padrão mostra duas seções mesmo sem `--stats`.

- `Ligacao entre projetos` descreve a estrutura declarada nos templates
- `Resolucao das ligacoes` descreve quantas referências foram resolvidas nos dados

Uma linha com `aguardando coleta` indica projeto de origem sem `SOURCE`. Uma linha com `0 resolvidas` indica que o projeto tem dados, mas nenhum valor casou. Referências órfãs e rótulos sem aresta precisam aparecer como pendências, mesmo que o sumário informe que os projetos foram linkados.

Com `--stats`, a versão 0.11.0 mostra tabela por membro com linha `TOTAL`, bloco separado para ontologia e contagens agregadas. A coluna `Codes` deixou de ser impressa porque repetia a contagem da ontologia.

## Formatos

### JSON

Use como saída canônica para inspeção programática. Ele inclui índices, frequências, fontes, itens, ontologias e triples.

### CSV

Um projeto com chains pode produzir:

- `sources.csv`
- `items.csv`
- `ontologies.csv`
- `chains.csv`

Sem chains, a última tabela não é criada. A ausência não indica erro.

A coluna de chain em `items.csv` pode conter representação interna pouco legível. Para análise, use `chains.csv` ou os triples do JSON.

Campos com vários códigos usam um separador próprio na célula. Inspecione a saída antes de preparar filtros.

### XLSX

As abas seguem as tabelas disponíveis. Projeto sem chain pode ter apenas três abas.

### Alpaca JSONL

Não presuma uma linha por ITEM. O exportador cria pares de categorias diferentes e pode fundir exemplos com a mesma instrução e saída mesmo quando as citações diferem.

Se o pesquisador precisar de um exemplo por item, gere o conjunto a partir do JSON ou de `items.csv` e valide as contagens.

## API Python

Na versão 0.6.0, `synesis.load()` recebe conteúdo, não caminhos.

```python
import synesis

result = synesis.load(
    project_content=project_text,
    template_content=template_text,
    annotation_contents={"anotacoes.syn": annotations_text},
    ontology_contents={"ontologia.syno": ontology_text},
    bibliography_content=bib_text,
    dataset_index=dataset_index,
)

if result.success:
    frames = result.to_dataframes()
    data = result.to_json_dict()
else:
    diagnostics = result.get_diagnostics()
```

`to_dataframes()` pode omitir tabelas vazias. Confira se `chains` existe no retorno antes de acessá-lo.

Não existe tabela `codes` nesse retorno. Os nomes comuns são sources, items, ontologies e, quando houver dados, chains.

Na versão 0.10.0 ou posterior, `dataset_index` fornece registros já carregados sem exigir leitura de arquivo pela API. O JSON v3.0 mantém uma seção `dataset` separada de `bibliography`.

## `synesis-coder`

Esta seção depende de confirmação local. Antes de prometer comandos, instale e leia `synesis-coder --help`.

O uso envolve provedor de IA, custo e envio de corpus. Peça autorização do pesquisador antes de instalar, configurar ou executar.

Fluxo de controle:

1. aprovar template e guidelines
2. aprovar ontologia ou estratégia de propostas
3. aprovar dois ou três itens piloto
4. executar lote pequeno
5. compilar
6. revisar com subagente separado
7. apresentar amostra ao pesquisador
8. ampliar após aprovação

Nunca digite ou exponha credenciais no chat. Use configuração segura local.

## `synesis-graph`

O pipeline oficial de representações em grafo está em https://github.com/synesis-lang/synesis-graph. Em 2026-08-17 foi publicada a versão 0.7.0. A ferramenta é opcional e externa ao compilador: precisa de instalação do pacote, de um backend e, nos casos de banco, de servidor e configuração. Confirme a ajuda da versão instalada antes de prometer comandos.

Três backends acompanham a versão 0.7.0, todos sob o mesmo contrato `BackendAdapter`.

| Backend | Protocolo | Dependência Python | Infraestrutura |
|---|---|---|---|
| Neo4j | BOLT, porta 7687 | driver `neo4j` (extra) | servidor de banco |
| ArcadeDB | HTTP/JSON, porta 2480 | nenhuma, só stdlib | servidor de banco |
| HTML | sem protocolo | nenhuma | nenhuma |

A interface comum se baseia em subcomandos por backend. A forma geral é:

```bash
pip install "synesis-graph[neo4j]"
synesis-graph neo4j --project caminho/projeto.synp
synesis-graph arcadedb --project caminho/projeto.synp
synesis-graph html --project caminho/projeto.synp --output grafo.html
```

A configuração de credenciais e opções vive num `config.toml` na raiz do projeto usado, com seções `[neo4j]` e `[arcadedb]`. O backend HTML não exige credenciais.

A versão 0.7.0 acrescentou busca semântica por embeddings vetoriais no backend ArcadeDB. Ela exige o extra opcional `embeddings`.

```bash
pip install "synesis-graph[embeddings]"
synesis-graph arcadedb --project caminho/projeto.synp --vector-embeddings ontologia_descricao,tema
```

O nome dos campos passados em `--vector-embeddings` é validado contra o template do projeto. O modelo de embeddings é uma decisão por projeto, configurada em `[arcadedb.embeddings]` do `config.toml`, e a escolha depende do idioma do corpus. Os vetores são cacheados num arquivo lateral que deve ficar fora do Git. O backend Neo4j não suporta vetores nesta versão.

Os dois backends de banco geram o mesmo grafo estrutural a partir do mesmo projeto. As métricas avançadas (PageRank, betweenness e community) vêm de motores diferentes, com Neo4j exigindo o plugin Graph Data Science e ArcadeDB usando algoritmos nativos, e os scores dos dois não são diretamente comparáveis entre si.

Trate arquivos com senha como secretos e mantenha-os fora do Git. Antes de sincronizar um grafo, explique ao pesquisador se o modo substitui ou combina dados existentes no servidor, porque a repetição de uma exportação pode alterar informações já gravadas.

A licença do pipeline mudou de MIT para AGPL-3.0-only com a Synesis Data-Output Exception a partir da versão que passou a cobrir os backends ArcadeDB e HTML. As versões publicadas antes permanecem sob MIT. Os grafos e o HTML gerados a partir das entradas do usuário não recebem obrigação de copyleft apenas por terem sido produzidos pela ferramenta, mas a ferramenta em si, se modificada, distribuída ou oferecida como serviço de rede, segue as obrigações da AGPL. Consulte `LICENSE` e `LICENSE.exception` da versão usada antes de decisão jurídica.

## LSP e editor

A extensão oficial Synesis para VS Code, versão 0.9.0 no repositório consultado, requer VS Code 1.60 ou posterior. Ela cobre `.syn`, `.synt`, `.synp`, `.syno` e `.synr`. O arquivo `.synr` pertence ao pipeline ACT e recebe suporte de editor, mas não deve ser tratado como um dos cinco arquivos do projeto sem confirmar a versão e o fluxo em uso.

Antes de instalar a extensão ou o LSP, peça autorização. A instalação altera o ambiente local. Depois, confira no VS Code se a pasta aberta contém um `.synp`, se `synesis-lsp` está disponível e se o canal de saída `Synesis LSP` não relata falha de inicialização.

```bash
python -m pip install synesis synesis-lsp
synesis-lsp --help
```

Se o executável não estiver no PATH, configure `synesisExplorer.lsp.pythonPath` com o caminho completo de `synesis-lsp`. Essa configuração, assim como `synesisExplorer.lsp.args` e `synesisExplorer.coder.path`, tem escopo de máquina. Ela não deve vir de `.vscode/settings.json` de um projeto externo.

Recursos confirmados da extensão:

- diagnósticos inline, autocomplete, hover, hints de autor e ano, destaque semântico e navegação entre arquivos pelo LSP
- painéis de referências, códigos, relações, tópicos da ontologia, anotações da ontologia e campos do template
- grafo de relações do projeto, do arquivo ativo ou do ITEM sob o cursor
- visualização do abstract da referência ativa
- ir à definição de um código com `F12`
- renomear código ou referência com `F2`
- enviar seleção de um `.syn` ao `synesis-coder` com `Ctrl+Shift+I`, somente após autorização para uso de IA e envio de corpus

Os painéis de relações e de anotações aparecem ao editar `.syn`. O painel de tópicos aparece ao editar `.syno`. Uma ausência de painel pode refletir o tipo de arquivo ativo, não uma falha.

O LSP e os painéis ajudam a localizar inconsistências, mas não substituem `synesis compile projeto.synp --stats`. Rode a compilação após mudança que afete o projeto inteiro, antes de exportar e antes de concluir uma correção.

O comando de renomear não atravessa os portões metodológicos. Renomear um conceito exige o portão O e confirmação das definições afetadas. Renomear uma referência é mecânico, mas exige inspeção dos vínculos atualizados e compilação completa. Não aceite uma alteração em lote apenas porque o editor a aplicou sem erro.

## Zotero

A organização Synesis mantém o projeto `zotero-synesis-export`. Confirme versão e compatibilidade antes de orientar a instalação. Preserve o identificador BibTeX usado pelos `SOURCE` e `ITEM`.

## Git

Arquivos Synesis são texto e funcionam bem com Git. Sugira versionamento depois de confirmar o escopo.

Um `.gitignore` de projeto pode excluir:

```text
.env
neo4j_config.toml
resultados/
__pycache__/
```

Não faça commit, push ou criação de remoto sem pedido do usuário.

## Hermes e instalação de ferramentas

Instalar pacote, alterar PATH, configurar provedor ou habilitar ferramenta muda o ambiente. Confirme escopo e impacto antes de agir.

Depois da instalação:

1. confira versão
2. confira ajuda
3. execute um projeto mínimo
4. registre a saída real
5. só então use no corpus

## Fontes

- documentação do Synesis em https://synesis-lang.github.io/synesis-docs/pt/
- compilador em https://github.com/synesis-lang/synesis
- releases do compilador em https://github.com/synesis-lang/synesis/releases
- extensão Synesis para VS Code em https://github.com/synesis-lang/synesis-vscode
- organização em https://github.com/synesis-lang
- documentação do Hermes em https://hermes-agent.nousresearch.com/docs

## Critérios de conclusão

- [ ] Versão confirmada por comando
- [ ] Ajuda da CLI consultada quando necessário
- [ ] Instalações e custos autorizados
- [ ] Segredos fora de arquivos versionados
- [ ] `compile --stats` executado
- [ ] Exportações verificadas no disco
- [ ] Contagens e formatos explicados ao pesquisador
- [ ] Afirmações não testadas identificadas como tal
