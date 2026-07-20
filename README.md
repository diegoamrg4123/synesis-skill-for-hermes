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
.gitattributes
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
    run_maintenance_tests.py
docs/
    PROTOCOLO_DE_MANUTENCAO.md
    PROMPT_CRON_DIARIO.md
tests/
    cenarios/
    fixtures/
    test_maintenance.py
CHANGELOG_MANUTENCAO.md
```

O `SKILL.md` contém o processo que deve estar disponível sempre. As referências são carregadas somente na fase correspondente.

Durante o desenvolvimento local, um `AGENTS.md` ignorado pelo Git pode registrar
instruções para o agente que mantém a skill. Esse arquivo não faz parte da
distribuição nem da instalação usada pelo pesquisador.

O `.gitattributes` preserva LF nos arquivos de texto. Isso evita falha falsa do
validador em clones Windows com `core.autocrlf=true`, pois a skill exige LF.

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

A forma mais previsível de instalar a skill completa, incluindo referências, é clonar o repositório dentro do diretório de skills.

```bash
git clone https://github.com/diegoamrg4123/synesis-skill-for-hermes.git "$HOME/.hermes/skills/research/synesis"
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

### Compatibilidade do compilador

Em 2026-07-20, a versão atual do Synesis era 0.9.0. O caminho básico com `--version`, `compile --help`, `init` e `compile --stats` foi executado nessa versão.

As regras empíricas detalhadas desta skill mantêm o Synesis 0.6.0 como linha de base histórica. Não use essa versão como recomendação de instalação. Use pelo menos 0.7.0, que corrigiu leitura fora da pasta do projeto, leitura sem limite de tamanho e injeção de fórmulas em CSV.

Quando a versão instalada diferir de 0.6.0, teste novamente as afirmações detalhadas antes de aplicá-las ao corpus. A execução real e a documentação da versão instalada prevalecem.

Ferramentas externas como `synesis-coder`, `synesis-graph` e o LSP são opcionais. As referências indicam quais afirmações dependem de confirmação local.

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

## Manutenção experimental

A manutenção usa somente fixtures sintéticos e cenários documentados em `tests/cenarios/`. Ela testa a infraestrutura e especifica verificações comportamentais para execução futura. Não executa pesquisa qualitativa real nem trata uma resposta de modelo como prova.

Execute localmente:

```bash
python3 -m unittest discover -s tests -p test_maintenance.py -v
python3 scripts/run_maintenance_tests.py
```

Os testes de regressão verificam as regras mecânicas da manutenção. O executor usa biblioteca padrão, roda esses testes e o validador, cria um perfil Hermes temporário, instala nele uma cópia da skill e confirma a descoberta como `synesis`, `research`, local e habilitada. Não usa credenciais nem chama modelo por API. Ele exige que o executável `hermes` esteja no `PATH`.

Os cenários dos portões T, O e A são especificações de comportamento. Uma rodada futura com Hermes configurado deve guardar briefing, saída bruta e inspeção de arquivos. Essa rodada não transforma comportamento de LLM em prova automática de decisão metodológica.

A manutenção trabalha exclusivamente na branch isolada `hermes/skill-improvement`. O protocolo está em `docs/PROTOCOLO_DE_MANUTENCAO.md`, e o prompt para cron futuro está em `docs/PROMPT_CRON_DIARIO.md`.

O prompt usa uma rotação semanal determinística. Cada dia útil cobre um dos cinco cenários. Sábado e domingo repetem a descoberta da skill, que não depende de chamada ao modelo. Relatórios sem mudança são entregues pelo cron e não criam commit.

O GitHub Actions executa os testes de regressão e `python scripts/validate_skill.py`. O executor completo depende de um binário Hermes disponível no ambiente e, por isso, a descoberta da skill permanece uma verificação local sem configuração de credenciais ou chamada de modelo no CI.

## Versionamento

Este diretório é a raiz do repositório `synesis-skill-for-hermes`. Mudanças são preparadas em branch, validadas e revisadas antes de entrar na `main`.

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
- teste básico do compilador Synesis 0.9.0
- documentação do Hermes Agent em https://hermes-agent.nousresearch.com/docs

Quando houver conflito entre texto e execução, o comportamento observado deve ser registrado e reproduzido antes de atualizar a skill.

## Créditos

Synesis foi criado por Christian M. De Britto. O projeto oficial está em https://github.com/synesis-lang/synesis e usava licença MIT na versão consultada em 2026-07-20. Confira a licença da versão instalada, pois o projeto anunciou uma mudança futura.

A skill agnóstica que serviu de base foi criada por Diego Amorim Goulart com apoio do Claude Fable 5 via Claude Code. Esta adaptação para Hermes Agent foi dirigida por Diego e elaborada com o Hermes Agent da Nous Research.

Este repositório não é afiliado ao autor do Synesis, à organização synesis-lang, à Anthropic nem à Nous Research.

## Licença

Distribuída sob licença MIT. Consulte `LICENSE`.

## Nota sobre a criação

As primeiras versões desta skill específica para o Hermes foram feitas com o
ChatGPT 5.6-sol no harness do Hermes Agent.
