# Decisões metodológicas

## Como conduzir a conversa

O template converte método em regras executáveis. Faça uma ou duas perguntas por vez. Use `clarify` quando houver até quatro caminhos definidos. Explique o efeito de cada opção sem impor uma preferência.

Registre cada resposta num log do projeto. Antes de escrever o `.synt`, apresente o texto integral pelo portão T.

## Bloco A, estudo

Pergunte:

1. Qual é a pergunta de pesquisa?
2. Que material será analisado?
3. Qual abordagem será usada?
4. A codificação será dedutiva, indutiva ou mista?
5. O trabalho será individual ou em equipe?
6. Qual saída será usada depois, como Excel, R, Python ou grafo?

Efeitos comuns:

| Abordagem | Configuração a discutir |
|---|---|
| Análise temática | Código central, grupos para temas, chain opcional |
| Grounded theory | Memo obrigatório, ontologia emergente, revisão por ciclos |
| Análise de conteúdo | Categorias definidas, valores fechados e maior padronização |
| Análise causal | Chain, relações definidas e memo ligado à relação |
| Análise de discurso | Campos para contexto, forma da fala e memo detalhado |
| Revisão de literatura | Metadados de fonte, unidade documental e controle de granularidade |

A tabela abre a conversa. Ela não determina a escolha.

## Bloco B, unidade de análise

Peça uma frase que permita testar se um trecho forma um item.

Exemplos:

- um turno de fala completo
- um parágrafo com uma afirmação sobre o tema
- uma ocorrência do fenômeno estudado
- um mecanismo causal sustentado por uma citação

Depois de discutir campos e ontologia, volte à unidade. Pergunte se trechos que apresentam apenas contexto, resposta ou desfecho formam itens próprios ou ficam ligados a outro item.

Se os dados não couberem na unidade aprovada, não a amplie sozinho.

## Bloco C, campos de item

Discuta cada campo.

| Campo comum | Pergunta |
|---|---|
| `quote` | A citação literal é obrigatória em todo item? |
| `memo` | Toda citação exige interpretação registrada? |
| `code` | Todo item precisa estar codificado desde a primeira rodada? |
| `chain` | O estudo representa relações ou somente categorias? |
| `context` | Informações de situação, tom ou posição precisam de campo próprio? |
| `confidence` | O pesquisador quer registrar força da interpretação? |

Para cada campo, confirme:

- nome
- tipo
- escopo
- obrigatoriedade
- descrição
- guideline
- valores permitidos, se houver

Não invente valores de ENUMERATED, ORDERED ou SCALE. Peça os rótulos, definições, ordem e intervalo.

## Bloco D, bundles

Um bundle exige que campos apareçam juntos e com contagens correspondentes. Ofereça bundle quando houver vínculo metodológico real.

Exemplo de pergunta:

```text
Cada chain deve ter um memo próprio que a justifique?
```

Se a resposta for sim, um bundle de memo e chain pode representar a decisão. Se a resposta for não, os campos devem permanecer independentes.

## Bloco E, chains

Pergunte primeiro se o estudo precisa de relações dirigidas.

Se precisar, peça ao pesquisador os nomes e definições. Exemplos para discussão:

- `CAUSA`
- `FAVORECE`
- `INIBE`
- `HABILITA`
- `MEDIA`
- `RELACIONA_SE`

Não trate os nomes como sinônimos. Cada relação precisa de uma regra de uso que permita escolher entre relações próximas.

Confirme a aridade mínima. O padrão comum é dois conceitos, mas a escolha pertence ao método.

## Bloco F, fontes

Pergunte quais características serão usadas na análise, não quais metadados seriam possíveis.

Possibilidades:

- tipo de fonte
- data de acesso
- local
- método do estudo
- veículo
- grupo de participante
- período

Um campo obrigatório de SOURCE precisa existir em todas as fontes. Mostre esse custo antes da aprovação.

## Bloco G, ontologia

Pergunte:

1. Qual estratégia de criação será usada?
2. Qual lógica organiza os grupos?
3. Qual idioma e convenção de nomes serão usados?
4. Que campos descrevem cada conceito?
5. Como novos conceitos serão propostos e aprovados?

A estratégia pode ser:

- dedutiva, com conceitos vindos do referencial
- indutiva, com conceitos propostos durante a leitura
- mista, com núcleo inicial e expansão controlada

Finalize pelo portão O descrito no `SKILL.md`.

## Bloco H, guidelines

Guidelines orientam pessoas e agentes. Peça critérios para:

- selecionar ou descartar um trecho
- delimitar começo e fim da citação
- escrever o memo
- escolher códigos
- escolher relações
- lidar com incerteza
- propor conceito novo
- separar caminhos paralelos

O Hermes pode redigir os critérios em formato consistente. O conteúdo precisa vir do pesquisador ou ser aprovado por ele.

## Bloco I, automação

Use `clarify` para escolher o nível.

- Guiado
- Colaborativo
- Automatizado com revisão

Confirme também:

- tamanho do piloto
- tamanho dos lotes
- frequência de revisão
- amostragem mínima após cada lote
- quem resolve divergências entre codificador e revisor

O árbitro final é o pesquisador.

## Portão T

Antes de gravar o template, apresente:

1. unidade de análise
2. campos de SOURCE
3. campos de ITEM
4. campos de ONTOLOGY
5. REQUIRED, OPTIONAL e bundles
6. tipo e configuração de cada campo
7. relações e aridade
8. guidelines integrais
9. texto integral do `.synt`

Peça aprovação explícita depois da apresentação. Grave apenas após a resposta.

## Mudança de template

Antes de alterar um template existente:

1. compile para obter uma linha de base
2. procure todos os usos do campo ou relação
3. explique o impacto
4. obtenha a decisão
5. apresente o texto alterado pelo portão T
6. grave e recompile
7. compare as contagens e diagnósticos

Novo campo opcional tende a exigir menos migração. Campo obrigatório, bundle, remoção ou renomeação pode exigir revisão do corpus inteiro.

## Registro de decisões

Use um arquivo como `DECISOES.md` no projeto. Para cada decisão, registre:

- data
- fase
- questão
- opções consideradas
- decisão do pesquisador
- efeito nos arquivos
- pendências

Comentários curtos nos arquivos Synesis podem apontar para o registro. Não transforme a memória global do Hermes na única cópia desse histórico.
