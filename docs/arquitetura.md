# Arquitetura proposta

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

## Componentes

- **Chat:** recebe solicitações e exibe perguntas, prévias e resultados.
- **Orquestrador:** transforma cada pedido em uma ação ou sequência curta de ações.
- **Validação:** pede detalhes quando o pedido não informa caminho, destinatário ou conteúdo suficiente.
- **Política de execução:** aplica permissões e exige confirmação antes de enviar, sobrescrever ou remover conteúdo.
- **Ferramentas:** adaptadores independentes para operações locais e serviços externos autorizados.
- **Resultado:** informa sucesso, falha ou ação não executada, sem alegar que algo foi concluído antes da confirmação do serviço.

## Fluxo de envio

```mermaid
sequenceDiagram
    actor Pessoa
    participant Chat as Chat Cloe
    participant Agent as Orquestrador
    participant Tool as Ferramenta de e-mail/mensagem
    participant Service as Serviço configurado

    Pessoa->>Chat: Pede para enviar uma mensagem
    Chat->>Agent: Solicitação e contexto
    Agent->>Agent: Valida destinatário e conteúdo
    Agent->>Tool: Prepara prévia
    Tool-->>Chat: Destinatário, assunto e texto
    Chat-->>Pessoa: Solicita confirmação explícita
    Pessoa->>Chat: Confirma envio
    Chat->>Tool: Autoriza esta ação específica
    Tool->>Service: Envia a mensagem
    Service-->>Tool: Resultado do envio
    Tool-->>Chat: Confirmação ou erro
    Chat-->>Pessoa: Informa o resultado
```
