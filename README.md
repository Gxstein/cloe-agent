# Cloe Agent

**Assistente conversacional local para organizar tarefas pessoais com ferramentas.**

Cloe Agent é um chatbot pensado para transformar pedidos escritos em ações práticas no computador. Em vez de apenas responder com instruções, Cloe poderá planejar uma tarefa, selecionar uma ferramenta permitida, executá-la e explicar o resultado na conversa.

A proposta começa com tarefas cotidianas e bem delimitadas: criar e organizar pastas, preparar e-mails, preparar mensagens e, quando houver integração configurada, enviá-los após a confirmação da pessoa usuária. Novas ações poderão ser adicionadas por ferramentas independentes.

## Como uma tarefa funciona

1. A pessoa descreve o que precisa em linguagem natural.
2. Cloe identifica a intenção e verifica se faltam informações, como destinatário ou caminho.
3. Cloe apresenta a ação planejada e os dados que serão usados.
4. A ferramenta autorizada executa a tarefa, solicitando confirmação antes de envios ou alterações sensíveis.
5. Cloe informa o resultado e eventuais erros.

Por exemplo, para um e-mail, Cloe deve mostrar destinatário, assunto e conteúdo antes de enviar. Uma instrução ambígua deve gerar uma pergunta de esclarecimento, não uma tentativa de adivinhar.

## Capacidades planejadas

### Organização local

- Criar pastas em locais configurados.
- Listar e localizar pastas dentro das áreas permitidas.
- Organizar arquivos por operações explícitas, com confirmação para ações que possam sobrescrever ou mover conteúdo.

### E-mails e mensagens

- Preparar rascunhos a partir das instruções da conversa.
- Exibir destinatários e conteúdo para revisão.
- Enviar somente depois de uma confirmação clara.
- Informar quando uma integração não estiver configurada ou quando o envio falhar.

### Ferramentas adicionais

A arquitetura deve permitir incluir novas ações sem misturar a interface de conversa com a lógica de cada integração. Calendário, lembretes e outras tarefas poderão ser avaliados depois que o fluxo inicial estiver confiável.

## Documentação adicional

- [Arquitetura e fluxo de envio](docs/arquitetura.md)
- [Plano de implementação](docs/plano-de-implementacao.md)

## Arquitetura proposta

```mermaid
flowchart LR
    User[Pessoa usuária] --> Chat[Chat local]
    Chat --> Agent[Orquestrador Cloe]
    Agent --> Clarify[Validação e esclarecimento]
    Clarify --> Policy[Permissões e confirmação]
    Policy --> Tools[Ferramentas autorizadas]
    Tools --> Files[Arquivos e pastas]
    Tools --> Email[E-mail]
    Tools --> Messages[Mensagens]
    Files --> Result[Resultado da ação]
    Email --> Result
    Messages --> Result
    Result --> Chat
```

- **Chat:** recebe pedidos e apresenta perguntas, prévias e resultados.
- **Orquestrador:** converte cada pedido em uma sequência pequena de ações.
- **Permissões e confirmação:** limita o que cada ferramenta pode acessar e exige aprovação antes de ações externas ou potencialmente destrutivas.
- **Ferramentas:** implementam operações específicas, como criar uma pasta ou enviar uma mensagem.

## Princípios de segurança e controle

- Ações externas, como enviar e-mails ou mensagens, sempre mostram uma prévia e aguardam confirmação explícita.
- Ações destrutivas ou que sobrescrevam conteúdo também exigem confirmação.
- Cada ferramenta recebe apenas o acesso necessário para sua tarefa.
- Credenciais e tokens não devem ser incluídos no repositório nem exibidos na conversa.
- A pessoa usuária pode entender qual ação será feita e interromper o fluxo antes da execução.

## Escopo inicial

O primeiro recorte deve validar a conversa e a execução de poucas tarefas úteis: criar pastas e preparar mensagens para revisão. O envio real depende de uma integração escolhida e configurada. A interface, o mecanismo conversacional e os serviços de e-mail e mensagens ainda serão definidos no planejamento técnico.

## Estado do projeto

**Em planejamento.** Este repositório registra a proposta, as decisões e os diagramas de Cloe Agent. A implementação ainda não está pronta; as capacidades descritas são objetivos do projeto.
