# Fluxos do Hermes para Synesis

## Princípio de coordenação

O agente principal conversa com o pesquisador, mantém os portões e verifica os resultados. Subagentes recebem trabalho fechado. Eles não recebem autoridade metodológica.

Subagentes do Hermes começam sem o histórico da conversa. Eles não podem usar `clarify` e, na configuração comum, não delegam para outros agentes. O campo de contexto precisa carregar tudo que afeta o subtrabalho.

## Quando delegar

Delegue quando o trabalho exige julgamento delimitado e pode ser conferido depois.

Exemplos:

- codificar um lote depois do piloto aprovado
- revisar itens contra definições operacionais já aprovadas
- procurar inconsistências entre citações, memos e códigos
- comparar versões de uma ontologia
- examinar diagnósticos extensos sem editar

Não delegue:

- entrevista do template
- criação livre de conceitos
- escolha da unidade de análise
- aprovação de definições
- resolução final de divergência interpretativa
- tarefa que precisa perguntar ao pesquisador

Para contagem, conversão ou inspeção repetitiva sem julgamento, prefira `execute_code`.

## Pacote mínimo de contexto

Todo subagente de Synesis deve receber:

1. caminho absoluto do projeto
2. arquivos permitidos para leitura e escrita
3. unidade de análise aprovada
4. pergunta de pesquisa relevante
5. texto ou caminho do template aprovado
6. conceitos permitidos com definições operacionais
7. relações permitidas com definições
8. guidelines aplicáveis
9. lote exato
10. formato da entrega
11. proibição de criar método novo
12. comando de validação

Inclua a regra:

```text
Se faltar decisão metodológica, não escolha. Registre a lacuna e devolva ao agente principal.
```

Não escreva apenas "use o template existente". Informe o caminho e peça que o subagente o leia.

## Fluxo de codificação e revisão

### Etapa 1, fechamento humano

O agente principal:

1. lê o projeto
2. confirma unidade, ontologia e guidelines
3. produz itens piloto
4. passa pelo portão A
5. define o lote autorizado

Sem essa etapa, não há delegação de codificação.

### Etapa 2, codificador

O codificador recebe um lote sem sobreposição e pode:

- extrair citações conforme a unidade
- redigir memos segundo as guidelines
- aplicar apenas conceitos aprovados
- aplicar apenas relações aprovadas
- listar trechos sem categoria adequada

O codificador não altera template ou ontologia. Propostas novas ficam em relatório separado.

### Etapa 3, revisor

O revisor recebe os mesmos critérios e os itens produzidos. Peça uma tabela com:

- identificação do item
- veredito
- problema observado
- evidência textual
- correção proposta
- tipo da correção, mecânica ou metodológica

O revisor não edita automaticamente quando a correção for metodológica.

### Etapa 4, agente principal

O agente principal:

1. lê os arquivos reais
2. confere o relatório dos dois agentes
3. executa a compilação
4. verifica contagens e diagnósticos
5. aplica correções mecânicas seguras
6. leva divergências metodológicas ao pesquisador

O relato do subagente não prova que um arquivo foi escrito ou validado.

## Paralelismo seguro

Use lote paralelo apenas quando:

- os arquivos de saída são distintos
- os trechos não se sobrepõem
- a ontologia está congelada durante o lote
- a unidade de análise está definida
- existe forma de reunir resultados sem sobrescrita

Dê um arquivo por subagente ou use diretórios de trabalho separados. O agente principal reúne os resultados depois da revisão.

Evite vários agentes escrevendo no mesmo `.syn`. O conflito pode ser sintático e interpretativo.

## Coordenação plana

A configuração padrão do Hermes favorece coordenação pelo agente principal. Use filhos do tipo leaf para codificação e revisão. Não aumente a profundidade de delegação apenas para imitar uma árvore de agentes.

Uma árvore maior aumenta custo e reduz a visibilidade de decisões. Para Synesis, a coordenação plana combina melhor com os portões humanos.

## Exemplo de tarefa para codificador

```text
Objetivo
Codificar somente as fontes lote_01 a lote_05.

Projeto
C:/pesquisa/projeto.synp

Arquivos
Leia template.synt, ontologia.syno e corpus/lote_01.md.
Grave apenas rascunhos/lote_01.syn.

Método aprovado
Unidade de análise, um turno de fala com uma afirmação completa sobre adoção.
Use apenas os conceitos listados em ontologia.syno.
Não crie novos conceitos ou relações.

Entrega
Arquivo Synesis e relatório de lacunas.
Execute synesis compile projeto-validacao.synp --stats.
Se faltar decisão, registre e pare nesse ponto.
```

O exemplo precisa ser adaptado aos caminhos e critérios reais.

## Exemplo de tarefa para revisor

```text
Revise rascunhos/lote_01.syn contra template.synt, ontologia.syno e as guidelines aprovadas.
Não altere arquivos.
Para cada problema, informe item, citação, regra violada e correção proposta.
Classifique a correção como mecânica ou metodológica.
Não invente conceitos, relações ou unidade de análise.
```

## `synesis-coder` e subagentes

O `synesis-coder` é uma ferramenta externa de codificação por IA. Ele não é um subagente do Hermes. Quando estiver instalado e aprovado pelo pesquisador, o Hermes pode executar a ferramenta e depois delegar uma revisão independente.

Fluxo recomendado:

1. confirmar custo, privacidade e envio do corpus ao provedor
2. aprovar template, ontologia, guidelines e piloto
3. executar `synesis-coder` num lote pequeno
4. compilar a saída
5. pedir revisão independente a um subagente
6. apresentar amostra e divergências ao pesquisador
7. ampliar o lote somente após aprovação

Não exponha credenciais ao chat ou ao subagente. Use o mecanismo local de configuração segura.

## Falhas e recuperação

### Subagente não recebeu contexto suficiente

Não aceite suposições produzidas. Descarte o lote ou separe os itens afetados. Refaça o pacote de contexto e execute novamente.

### Codificador e revisor discordam

Se a diferença for sintática, o agente principal pode aplicar a correção comprovada. Se for interpretativa, apresente as duas leituras ao pesquisador com a citação.

### Subagente alterou ontologia

Pare a integração. Mostre o diff. Trate cada alteração como proposta e passe pelo portão O antes de gravar no projeto principal.

### Execução foi interrompida

Delegações não são filas duráveis. Verifique quais arquivos foram realmente produzidos. Não presuma que um lote incompleto terminou.

## Auditoria do lote

Ao final, registre:

- agentes e papéis usados
- modelo ou provedor quando isso afetar reprodutibilidade
- arquivos de entrada
- arquivos de saída
- unidade de análise
- versão do template e da ontologia
- tamanho do piloto e do lote
- contagens antes e depois
- divergências e decisões humanas
- comando de compilação e código de retorno

Não grave credenciais, tokens ou conteúdo privado desnecessário.

## Critérios de conclusão

- [ ] O agente principal obteve as aprovações
- [ ] Cada subagente recebeu contexto autônomo
- [ ] Codificador e revisor tiveram papéis separados
- [ ] Nenhum agente criou método novo em silêncio
- [ ] Os arquivos reais foram lidos após a delegação
- [ ] A compilação foi executada pelo agente principal
- [ ] Divergências interpretativas voltaram ao pesquisador
- [ ] O lote tem registro de auditoria
