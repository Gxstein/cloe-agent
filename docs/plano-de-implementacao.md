# Plano de implementação

O MVP será desenvolvido em etapas com entregas verificáveis. O escopo inicial privilegia operações locais limitadas e revisão explícita de qualquer ação externa.

## Etapa 1 — Conversa local

- Criar um loop de conversa local com histórico limitado à tarefa atual.
- Separar a interface, o orquestrador e os adaptadores de modelo.
- Tratar pedidos ambíguos com perguntas de esclarecimento.

**Critério de conclusão:** a pessoa consegue iniciar uma conversa, pedir ajuda e encerrar a sessão sem perder erros ou resultados.

## Etapa 2 — Ferramentas locais seguras

- Definir um contrato para ferramentas com nome, argumentos, permissões e resultado.
- Permitir criação de pastas apenas dentro de diretórios configurados.
- Validar caminhos e impedir travessia para fora da área autorizada.
- Cobrir permissões e caminhos inválidos com testes.

**Critério de conclusão:** a ferramenta cria uma pasta de teste no local permitido e recusa caminhos fora dele.

## Etapa 3 — Prévia e confirmação

- Mostrar a ação e os argumentos antes de executar operações sensíveis.
- Associar a confirmação à prévia específica que a pessoa revisou.
- Não executar quando a confirmação for ambígua ou quando os dados mudarem.

**Critério de conclusão:** ações sem confirmação explícita não produzem efeitos externos.

## Etapa 4 — Rascunhos de comunicação

- Preparar e-mails e mensagens sem enviá-los.
- Mostrar destinatário, assunto e conteúdo para revisão.
- Manter credenciais fora do repositório e dos logs.

**Critério de conclusão:** um rascunho pode ser revisado e editado sem fazer envio.

## Etapa 5 — Integrações e confiabilidade

- Escolher uma integração por vez, documentando permissões e configuração.
- Tratar falhas, timeouts e resultados incertos sem repetir envios automaticamente.
- Registrar apenas metadados operacionais que não exponham conteúdo pessoal.

**Critério de conclusão:** a integração escolhida tem testes, instruções de configuração e uma demonstração controlada.

## Critérios gerais

- Instalação e execução reproduzíveis a partir de um ambiente limpo.
- Testes para parser, permissões, ferramentas, confirmações e falhas.
- README descrevendo somente capacidades implementadas e limitações conhecidas.
- Nenhum segredo ou dado pessoal versionado.
