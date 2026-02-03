# 🏦 Sistema Bancário em Python (POO)

Projeto de sistema bancário simples, desenvolvido em Python, com foco em
Programação Orientada a Objetos (POO), organização de código e boas práticas.

O objetivo do projeto é aprender e demonstrar conceitos, não simular um banco
real em produção.

---------------------------------------------------------------------

📌 Funcionalidades

- Criar clientes
- Criar contas bancárias
- Realizar depósitos
- Realizar saques
- Exibir extrato da conta
- Interface simples via terminal

---------------------------------------------------------------------

🧠 Arquitetura do Projeto

O sistema foi desenvolvido com responsabilidades bem definidas:

Banco
 └── Cliente
      └── Conta
           └── Transação

Banco
- Gerencia a lista de clientes
- Orquestra operações (depósito, saque, extrato)
- Não manipula saldo diretamente

Cliente
- Possui dados pessoais
- Pode ter múltiplas contas
- É identificado pelo CPF

Conta
- Controla saldo
- Valida depósitos e saques
- Mantém seu próprio histórico de transações

Transação
- Registra tipo, valor e data/hora
- Usada para compor o extrato da conta

---------------------------------------------------------------------

📂 Estrutura de Arquivos

projeto/
 ├── banco.py        -> Orquestra clientes e contas
 ├── clientes.py     -> Classe Cliente
 ├── contas.py       -> Classe Conta
 ├── transacoes.py   -> Classe Transacao
 └── main.py         -> Interface via terminal

---------------------------------------------------------------------

▶️ Como Executar

1. Certifique-se de ter Python 3.10 ou superior
2. Clone o repositório
3. Execute o arquivo principal com:

   python main.py

O menu será exibido no terminal.

---------------------------------------------------------------------

🧪 Tratamento de Erros

O sistema trata erros comuns de execução, como:
- Valores inválidos para depósito ou saque
- Saque maior que o saldo disponível
- Entrada inválida de dados numéricos

Esses erros não quebram o programa e retornam mensagens claras ao usuário.

---------------------------------------------------------------------

⚠️ Limitações Conhecidas (intencionais)

Este projeto não implementa, propositalmente:
- Validação de CPF duplicado
- Encapsulamento total da lista de contas
- Persistência em banco de dados
- Interface gráfica
- Formatação avançada de extrato

Esses pontos foram deixados fora do escopo inicial e fazem parte de
uma fase futura de refatoração.

---------------------------------------------------------------------

🔧 Próximos Passos (Refatoração Planejada)

- Implementar validação de CPF único
- Melhorar encapsulamento das entidades
- Criar método de exibição formatada do extrato
- Separar lógica de interface e regra de negócio
- Adicionar testes automatizados

---------------------------------------------------------------------

🎯 Objetivo do Projeto

Este projeto foi desenvolvido como parte do estudo de:
- Programação Orientada a Objetos em Python
- Organização de código
- Raciocínio lógico
- Estruturação de projetos para portfólio

---------------------------------------------------------------------

Apanhei bastante nesse inicio de projeto, porque foi meu primeiro contato com POO,
pretendo refatorar ele em finais de semana, e sempre usando pra estudo.

---------------------------------------------------------------------

⭐ Sugestões e feedbacks são bem-vindos.
