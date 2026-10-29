# Plano de 10 dias — Mx Harness

**Objetivo:** terminar um MVP local que execute cenários GenAI, conecte servidores MCP locais e produza resultados reproduzíveis. Cada dia termina com um artefato concreto e uma demonstração curta.

## Dia 1 — Escopo e arquitetura

**Foco:** decidir o que o Mx mede e manter o MVP pequeno.

- Escrever o objetivo, não objetivos e limites do MVP.
- Definir o fluxo: caso → agente/provedor → ferramentas MCP → avaliadores → relatório.
- Registrar as decisões de execução local, dados sintéticos e ausência de chaves obrigatórias.

**Entrega:** README, diagrama de arquitetura e critérios de sucesso do MVP.

**Concluído quando:** uma pessoa consegue explicar em um minuto o problema, o fluxo e o que ficou fora do escopo.

## Dia 2 — Contrato dos cenários

**Foco:** tornar os casos fáceis de criar, revisar e versionar.

- Definir campos: `id`, `input`, `expected_contains`, `expected_tools` e metadados opcionais.
- Validar campos obrigatórios, tipos, IDs repetidos e linhas JSON inválidas.
- Criar cenários sintéticos de suporte a pedidos, incluindo um caso sem necessidade de ferramenta.

**Entrega:** schema documentado e arquivo JSONL de exemplos validado.

**Concluído quando:** entradas inválidas falham com número de linha e explicação clara.

## Dia 3 — Provedor local e fronteira de modelo

**Foco:** separar o modelo do runner sem exigir uma API externa.

- Definir uma interface de provedor com resposta, duração e metadados opcionais.
- Manter um provedor determinístico para desenvolver e demonstrar offline.
- Definir como mensagens de erro e respostas incompletas chegam ao relatório.

**Entrega:** contrato de provedor e execução local reproduzível.

**Concluído quando:** o runner não depende de uma implementação específica de modelo.

## Dia 4 — Servidor MCP local de demonstração

**Foco:** construir ferramentas seguras e previsíveis para os cenários.

- Expor ferramentas MCP de leitura, como consulta de status de pedido e busca em catálogo sintético.
- Adicionar descrições e schemas claros para os argumentos.
- Usar somente dados falsos e evitar operações com efeitos colaterais.

**Entrega:** servidor MCP local executável por `stdio` e diagrama de sequência atualizado.

**Concluído quando:** um cliente MCP consegue descobrir e chamar as ferramentas de exemplo.

## Dia 5 — Cliente MCP e descoberta

**Foco:** conectar o Mx a um ou mais servidores MCP locais.

- Ler uma configuração local de servidores permitidos.
- Iniciar o processo MCP por `stdio` e encerrar corretamente ao fim da execução.
- Descobrir ferramentas, schemas e erros de conexão sem travar a avaliação inteira.

**Entrega:** cliente MCP integrado e registro da descoberta por servidor.

**Concluído quando:** os cenários identificam ferramentas disponíveis antes de executá-las.

## Dia 6 — Execução e limites das ferramentas

**Foco:** tornar chamadas de ferramenta observáveis e limitadas.

- Registrar servidor, nome da ferramenta, argumentos sanitizados, duração e resultado.
- Permitir apenas servidores e ferramentas declarados na configuração do cenário.
- Limitar tempo de execução e chamadas por cenário; representar falhas como resultados avaliáveis.

**Entrega:** trilha de chamadas MCP por caso e política de ferramentas permitidas.

**Concluído quando:** uma ferramenta não permitida é bloqueada e a razão aparece no resultado.

## Dia 7 — Avaliadores determinísticos

**Foco:** verificar comportamento sem alegar que uma métrica simples mede toda a qualidade de uma resposta.

- Implementar verificações de texto obrigatório e proibido.
- Validar respostas JSON contra um schema simples quando o caso pedir saída estruturada.
- Comparar ferramentas esperadas e observadas, incluindo chamadas ausentes ou inesperadas.

**Entrega:** avaliadores pequenos, nomeados e explicáveis, com falhas por critério.

**Concluído quando:** cada falha indica qual expectativa não foi atendida.

## Dia 8 — Relatórios e comparação

**Foco:** transformar execuções em evidência útil.

- Gerar JSON com resumo, resultados por caso, critérios, chamadas MCP e latência.
- Calcular taxa de aprovação e estatísticas básicas de duração.
- Comparar duas execuções e destacar casos que mudaram de resultado.

**Entrega:** relatório salvo localmente e comando de comparação.

**Concluído quando:** uma alteração no provedor ou cenário mostra claramente o que regrediu.

## Dia 9 — CLI e demonstração ponta a ponta

**Foco:** facilitar o uso por outra pessoa.

- Finalizar comandos `run`, `validate` e `compare`.
- Escrever dois exemplos: resposta simples e fluxo que consulta uma ferramenta MCP.
- Melhorar mensagens de erro, ajuda da CLI e instruções de instalação.

**Entrega:** demo executável do início ao fim e README de uso.

**Concluído quando:** alguém consegue instalar e repetir a demonstração seguindo apenas o README.

## Dia 10 — Qualidade e versão 0.1

**Foco:** fechar lacunas antes de apresentar o projeto.

- Revisar e executar testes unitários e de integração local.
- Validar os diagramas e os comandos documentados em um ambiente limpo.
- Revisar logs para garantir que segredos e dados sensíveis não apareçam.
- Preparar uma demonstração curta, limitações conhecidas e notas da versão 0.1.

**Entrega:** MVP local versionado, documentação final e roteiro de apresentação.

**Concluído quando:** os cenários de demonstração passam, falhas são reproduzíveis e o escopo está explicado com honestidade.

## Estado inicial do repositório

O repositório já tem um runner determinístico simples, carregamento JSONL, checagem `expected_contains`, saída JSON e um primeiro servidor MCP de leitura. Os dias 1–4 têm uma base inicial; a integração completa do cliente MCP e os critérios descritos acima ainda são trabalho futuro.

## Regras de escopo

- Sem chamadas pagas obrigatórias.
- Sem dados pessoais ou dados reais de pedidos.
- Sem ferramentas destrutivas ou com efeitos externos.
- Sem afirmar que aprovação textual equivale a qualidade semântica.
- MCP é a fronteira de ferramentas; não é o modelo nem o agente.
