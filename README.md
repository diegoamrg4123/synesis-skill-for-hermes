# Synesis para Hermes Agent

Skill para usar o Hermes Agent como assistente de projetos Synesis, com automação da mecânica e controle metodológico mantido pelo pesquisador.

## Propósito

O Synesis transforma decisões de pesquisa qualitativa em arquivos verificáveis. A autonomia do Hermes ajuda na leitura de corpus, escrita da DSL, compilação, exportação e auditoria. Essa autonomia não concede ao agente o papel de escolher categorias, unidade de análise, relações ou critérios de codificação.

A skill organiza essa separação com três portões.

- Portão T para aprovação integral do template
- Portão O para aprovação das definições da ontologia
- Portão A para aprovação de itens piloto antes de anotações em lote

## Diferenças em relação à skill agnóstica

Esta versão deriva da skill criada inicialmente com Claude Code, mas foi reescrita para o funcionamento do Hermes.

Ela inclui:

- uso explícito de `clarify` para decisões do pesquisador
- regras para `todo`, `read_file`, `search_files`, `terminal` e `execute_code`
- coordenação plana de subagentes pelo agente principal
- separação entre codificador, revisor e árbitro humano
- pacotes de contexto para subagentes que começam sem histórico
- limites para cron, memória e automações sem interação
- instalação no diretório de skills e uso por diretório externo
- metadados compatíveis com o formato de skills do Hermes

## Estrutura

```text
SKILL.md
README.md
LICENSE
.gitignore
.github/
    workflows/
        validate.yml
references/
    decisoes-metodologicas.md
    ecossistema.md
    fluxos-hermes.md
    ontologia-e-chains.md
    sintaxe-e-validacao.md
scripts/
    validate_skill.py
```

O `SKILL.md` contém o processo que deve estar disponível sempre. As referências são carregadas somente na fase correspondente.

Durante o desenvolvimento local, um `AGENTS.md` ignorado pelo Git pode registrar
instruções para o agente que mantém a skill. Esse arquivo não faz parte da
distribuição nem da instalação usada pelo pesquisador.

## Instalação local

### Cópia para o perfil padrão

No Git Bash usado pelo Hermes no Windows:

```bash
mkdir -p "$HOME/AppData/Local/hermes/skills/research/synesis"
cp -R SKILL.md README.md LICENSE references "$HOME/AppData/Local/hermes/skills/research/synesis/"
```

O caminho real do perfil pode variar. Confirme com:

```bash
hermes config path
```

A pasta de skills fica dentro do `HERMES_HOME` do perfil. Em instalações que usam `~/.hermes`, o destino usual é:

```text
~/.hermes/skills/research/synesis/
```

Reinicie a sessão ou use `/reload-skills` após instalar. Confira com:

```bash
hermes skills list
```

Depois, carregue a skill com `/synesis` ou mencione um projeto Synesis para ativação por contexto.

Esta adaptação usa o mesmo nome `synesis` da skill agnóstica. Instale somente uma
delas em cada perfil do Hermes. Duas skills com o mesmo nome criam ambiguidade de
descoberta e atualização.

### Diretório externo para desenvolvimento

O Hermes pode ler skills mantidas fora do perfil. Adicione ao `config.yaml` a pasta que contém este repositório.

```yaml
skills:
  external_dirs:
    - C:/caminho/para/a/pasta-pai
```

Use uma pasta pai que contenha a pasta desta skill. Caminhos aceitam `~` e variáveis de ambiente. Reinicie a sessão após alterar a configuração.

Diretórios externos graváveis podem ser alterados pelo `skill_manage`. Se quiser manter o repositório como fonte revisada manualmente, não peça ao Hermes para atualizar essa skill durante o uso normal.

## Instalação a partir do GitHub

Quando este diretório virar um repositório, a forma mais previsível de instalar a skill completa, incluindo referências, será clonar o repositório dentro do diretório de skills.

```bash
git clone URL_DO_REPOSITORIO "$HOME/.hermes/skills/research/synesis"
```

No Windows, substitua o destino pelo `HERMES_HOME` indicado por `hermes config path` quando ele não for `~/.hermes`.

Não use uma URL isolada de `SKILL.md` se a instalação não trouxer também a pasta `references`. O núcleo aponta para esses arquivos durante o trabalho.

## Uso

Exemplos de pedidos:

```text
/synesis quero iniciar um projeto para analisar entrevistas
```

```text
/synesis revise a ontologia, mas não altere nada sem minha aprovação
```

```text
/synesis codifique este lote com um agente e use outro para revisar
```

No terceiro caso, o agente principal deve obter as decisões antes de delegar. Os subagentes trabalham com critérios fechados e não fazem perguntas ao pesquisador.

## Requisitos

Para trabalhar com arquivos e compilar projetos:

- Hermes Agent com ferramentas de arquivo e terminal
- Python 3.10 ou posterior
- pacote `synesis`

Instalação do compilador:

```bash
python -m pip install synesis
synesis --version
```

Ferramentas externas como `synesis-coder`, `synesis2graph` e o LSP são opcionais. As referências indicam quais afirmações foram verificadas na versão 0.6.0 do compilador e quais dependem de confirmação local.

## Teste antes de publicar

Execute a validação local:

```bash
python scripts/validate_skill.py
```

O script confere frontmatter, arquivos obrigatórios, referências, codificação e
as restrições de redação desta pasta. O fluxo em `.github/workflows/validate.yml`
executa a mesma validação em pushes e pull requests depois que o repositório for
publicado no GitHub.

Antes de criar uma versão ou enviar ao GitHub:

1. valide o frontmatter do `SKILL.md`
2. procure caracteres proibidos e arquivos inesperados
3. instale a skill num perfil de teste ou diretório externo
4. abra uma nova sessão do Hermes
5. confira se `/synesis` aparece
6. rode um cenário guiado com decisões faltantes
7. confirme que o Hermes pergunta em vez de preencher as lacunas
8. rode um cenário em lote com codificador e revisor
9. confira os arquivos e a saída real do compilador

A validação completa do comportamento exige uma sessão nova, porque o carregador de skills pode manter cache durante a sessão atual.

## Versionamento

Este diretório está pronto para virar a raiz de um repositório Git. A criação do repositório, o primeiro commit e o remoto devem ser feitos somente quando o proprietário definir nome, descrição e URL.

Versões sugeridas:

- correção de texto ou procedimento sem mudança de comportamento, incremento de patch
- novo fluxo compatível, incremento de versão menor
- mudança nos portões ou na autoridade metodológica, incremento de versão maior

O campo `version` no `SKILL.md` deve acompanhar as versões publicadas.

## Fontes

A base técnica vem de:

- documentação oficial do Synesis em https://synesis-lang.github.io/synesis-docs/pt/
- organização Synesis em https://github.com/synesis-lang
- testes empíricos locais do compilador Synesis 0.6.0
- documentação do Hermes Agent em https://hermes-agent.nousresearch.com/docs

Quando houver conflito entre texto e execução, o comportamento observado deve ser registrado e reproduzido antes de atualizar a skill.

## Créditos

Synesis foi criado por Christian M. De Britto. O projeto oficial está em https://github.com/synesis-lang/synesis e usa licença MIT.

A skill agnóstica que serviu de base foi criada por Diego Amorim Goulart com apoio do Claude Fable 5 via Claude Code. Esta adaptação para Hermes Agent foi dirigida por Diego e elaborada com o Hermes Agent da Nous Research.

Este repositório não é afiliado ao autor do Synesis, à organização synesis-lang, à Anthropic nem à Nous Research.

## Licença

Distribuída sob licença MIT. Consulte `LICENSE`.

## Nota sobre a criação

As primeiras versões desta skill específica para o Hermes foram feitas com o
ChatGPT 5.6-sol no harness do Hermes Agent.
