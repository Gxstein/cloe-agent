# Arquitetura do Mx

```mermaid
flowchart LR
    User[Pessoa desenvolvedora] --> CLI[CLI Mx]
    CLI --> Loader[Carregador de cenários]
    Loader --> Runner[Orquestrador de avaliação]
    Runner --> Agent[Loop do agente]
    Agent <--> Provider[Provedor de modelo]
    Agent <--> Client[Cliente MCP]
    Client <--> Server[Servidor MCP local]
    Agent --> Evaluators[Avaliadores determinísticos]
    Evaluators --> Report[Relatório JSON]
    Runner --> Trace[Eventos e latências]
    Trace --> Report
    Cases[(Casos JSONL)] --> Loader
```

O loop do agente decide quando pedir uma ferramenta. O cliente MCP descobre e chama ferramentas expostas pelos servidores permitidos. O runner registra os passos e envia a resposta e os eventos observados aos avaliadores.

Na versão inicial, o agente e o cliente MCP ainda serão implementados. O servidor de exemplo já existe; o diagrama representa o estado final planejado para o MVP.
