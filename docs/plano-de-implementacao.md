# Plano de implementação

O plano divide a construção de um MVP em etapas curtas. A prioridade é criar uma conversa local que execute poucas ações úteis com confirmação clara, sem expandir para muitas integrações antes de validar o fluxo principal.

## Dia 1 — Definir o uso pessoal

Escolher os casos de uso prioritários, os diretórios que Cloe poderá acessar e quais serviços de e-mail ou mensagens são relevantes. Definir também quais ações ficam fora do primeiro MVP.

**Entrega:** escopo, limites de acesso e lista dos primeiros comandos em linguagem natural.

## Dia 2 — Projetar a conversa

Definir como Cloe identifica uma intenção, pergunta por dados ausentes, mostra a ação planejada e retorna resultados. Especificar uma confirmação vinculada a uma ação e a uma prévia.

**Entrega:** exemplos de conversas para criar pasta, preparar e-mail e enviar mensagem.

## Dia 3 — Criar a base local em Python

Preparar estrutura do projeto, configurações locais, logs sem conteúdo sensível e execução pela linha de comando. Guardar credenciais fora do repositório.

**Entrega:** aplicação local inicial e instruções de configuração.

## Dia 4 — Construir o chat mínimo

Criar uma interface conversacional local, manter o contexto da tarefa atual e apresentar perguntas e resultados. A interface inicial pode ser terminal se isso reduzir o escopo.

**Entrega:** conversa de ida e volta sem executar ações externas.

## Dia 5 — Implementar o registro de ferramentas

Definir um contrato comum para ferramentas: nome, descrição, parâmetros, validação, permissões e resultado. Permitir que o orquestrador escolha somente entre ferramentas registradas.

**Entrega:** ferramenta demonstrativa sem efeitos externos e fluxo de seleção validado.

## Dia 6 — Implementar ações em pastas

Adicionar criação e listagem de pastas em diretórios explicitamente permitidos. Validar caminhos, bloquear acesso fora das áreas configuradas e pedir confirmação antes de mover, sobrescrever ou remover arquivos.

**Entrega:** fluxo conversacional para criar e localizar pastas com resultado verificável.

## Dia 7 — Preparar e-mails e mensagens

Definir qual serviço ou aplicativo será integrado primeiro. Criar ferramentas que montem rascunhos e mostrem destino e conteúdo antes de qualquer envio.

**Entrega:** prévias de e-mail e mensagem; nenhuma ação é enviada sem aprovação.

## Dia 8 — Integrar envio com confirmação

Implementar uma integração escolhida, proteger credenciais, associar a confirmação ao conteúdo exato exibido e tratar falhas e respostas ambíguas do serviço.

**Entrega:** envio controlado de uma mensagem de teste após confirmação explícita.

## Dia 9 — Melhorar erros e controle

Validar pedidos ambíguos, destinatários inválidos, permissões negadas, timeouts e repetição de ações. Evitar reenviar automaticamente quando não for possível saber se o primeiro envio foi concluído.

**Entrega:** comportamento definido para falhas e casos que exigem esclarecimento.

## Dia 10 — Consolidar o MVP e a documentação

Revisar as conversas, limites de acesso e instalação local. Atualizar README, arquitetura, exemplos e limitações; preparar uma demonstração de criação de pasta e envio aprovado.

**Entrega:** MVP local demonstrável e documentação consistente com o comportamento implementado.

## Critérios do MVP

- O chat informa o que entendeu antes de executar uma ação relevante.
- A criação de pastas respeita diretórios autorizados.
- E-mail e mensagem têm prévia de destinatário e conteúdo.
- Envio externo só acontece após confirmação explícita da prévia correspondente.
- Falhas são comunicadas sem declarar sucesso indevidamente.
- Tokens, senhas e credenciais não são versionados.
