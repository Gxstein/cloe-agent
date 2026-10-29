# Mx Harness

**Harness local para avaliar aplicações GenAI e fluxos que usam MCP.**

O Mx executa cenários repetíveis contra um modelo e servidores MCP locais, verifica o comportamento esperado e salva evidências de cada execução. A meta é concluir um MVP demonstrável em dez dias, com escopo pequeno e dados sintéticos.

Este é um projeto independente de portfólio. Não é afiliado ao iFood e não usa dados, modelos ou serviços internos da empresa.

## Problema que o Mx resolve

Uma mudança em um prompt, modelo ou ferramenta pode melhorar uma resposta e quebrar outra. O Mx vai permitir repetir os mesmos cenários e comparar respostas, chamadas MCP, erros e latência antes de aceitar a mudança.

## Escopo do MVP

- Rodar localmente pela linha de comando.
- Carregar cenários versionáveis em JSONL.
- Usar um provedor determinístico para desenvolvimento sem chave de API.
- Conectar a servidores MCP locais por `stdio`.
- Registrar ferramentas descobertas e chamadas feitas em cada cenário.
- Avaliar expectativas explícitas e produzir relatório JSON.
- Começar com ferramentas demonstrativas somente de leitura e dados sintéticos.

O primeiro MVP não precisa de interface web, banco de dados, implantação em nuvem nem chamada a um modelo pago.

## Começar

Requisitos: Python 3.11 ou superior. Para executar o servidor MCP de exemplo, instale a dependência opcional:

```bash
python -m pip install -e ".[mcp]"
```

Executar o runner atual com o provedor determinístico:

```bash
python -m mx_harness run examples/cases.jsonl --output reports/latest.json
```

O runner inicial já carrega casos JSONL, verifica termos esperados e gera um resumo. A integração MCP e a avaliação de fluxos de agente entram nas etapas descritas em [Plano de 10 dias](docs/roadmap-10-days.md).

Para inspecionar o servidor MCP demonstrativo com o Inspector, instale também Node.js e execute:

```bash
mcp dev mcp_servers/order_support.py
```

## Diagramas

- [Arquitetura do Mx](docs/diagrams/architecture.md)
- [Fluxo de uma avaliação com MCP](docs/diagrams/evaluation-sequence.md)

## Plano de construção

O plano de dez dias divide o MVP em entregas pequenas, com um objetivo verificável por dia:

1. Definir escopo, arquitetura e contrato do cenário.
2. Fechar o schema JSONL e a validação dos casos.
3. Separar o provedor local da lógica de avaliação.
4. Criar o servidor MCP de demonstração com dados sintéticos.
5. Conectar o harness a servidores MCP locais e descobrir ferramentas.
6. Registrar chamadas, erros e limites permitidos de ferramentas.
7. Implementar avaliadores determinísticos para respostas e uso de ferramentas.
8. Gerar relatório agregado com resultados, falhas e latência.
9. Completar a CLI e dois cenários demonstrativos de ponta a ponta.
10. Revisar documentação, executar validação local e preparar a versão 0.1.

O detalhamento, os critérios de conclusão e os artefatos de cada dia estão em [docs/roadmap-10-days.md](docs/roadmap-10-days.md).

## Estrutura atual

```text
mx-harness/
├── docs/
│   ├── diagrams/
│   │   ├── architecture.md
│   │   └── evaluation-sequence.md
│   └── roadmap-10-days.md
├── examples/
├── mcp_servers/
│   └── order_support.py
├── mx_harness/
├── .gitignore
└── pyproject.toml
```

## Por que este projeto

O Mx demonstra fundamentos úteis para aplicações GenAI: avaliação repetível, integração com ferramentas, tratamento de falhas, observabilidade e limites explícitos. A implementação permanece local e pequena para que cada decisão possa ser explicada em uma entrevista técnica.

## Referências MCP

O servidor de exemplo usa o SDK Python oficial do MCP. A integração seguirá o ciclo de vida do cliente MCP e o transporte local `stdio`, conforme a documentação oficial: [Python SDK](https://github.com/modelcontextprotocol/python-sdk), [cliente MCP](https://github.com/modelcontextprotocol/python-sdk/blob/main/docs/client/index.md) e [execução de servidores](https://github.com/modelcontextprotocol/python-sdk/blob/main/docs/run/index.md).
