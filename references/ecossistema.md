# Ecossistema e execução

## Compilador verificado

A referência empírica desta skill é o Synesis 0.6.0. Confirme a instalação real.

```bash
python -m pip install synesis
synesis --version
synesis --help
synesis compile --help
```

No Windows, o executável pode ficar numa pasta `Scripts` fora do PATH. Use o caminho informado pelo instalador ou ajuste o PATH. O pacote 0.6.0 não oferece `python -m synesis` como substituto garantido.

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

## Exportação

```bash
synesis compile projeto.synp --json resultados/projeto.json
synesis compile projeto.synp --csv resultados/csv
synesis compile projeto.synp --xls resultados/projeto.xlsx
synesis compile projeto.synp --alpaca resultados/projeto.jsonl
```

A CLI 0.6.0 não oferece `--output` nem comando `export`.

A exportação pode não imprimir confirmação dos arquivos. Verifique o disco.

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
)

if result.success:
    frames = result.to_dataframes()
    data = result.to_json_dict()
else:
    diagnostics = result.get_diagnostics()
```

`to_dataframes()` pode omitir tabelas vazias. Confira se `chains` existe no retorno antes de acessá-lo.

Não existe tabela `codes` nesse retorno. Os nomes comuns são sources, items, ontologies e, quando houver dados, chains.

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

## `synesis2graph`

A integração com Neo4j ou Memgraph precisa de instalação, servidor e configuração. Confirme a ajuda da versão instalada.

Trate arquivos com senha como secretos e mantenha-os fora do Git. Antes de sincronizar um grafo, explique se o modo substitui ou combina dados existentes.

## LSP e editor

A documentação menciona `synesis-lsp` e a extensão Synesis Explorer. A disponibilidade e os atalhos precisam ser conferidos no ambiente do pesquisador.

O LSP ajuda na escrita, mas não substitui `compile --stats`.

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
