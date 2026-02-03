from clientes import Cliente
from contas import Conta


class Banco:
    """
    Classe responsável por gerenciar clientes e contas.
    O Banco apenas orquestra as operações, não manipula saldo diretamente.
    """

    def __init__(self):
        # Lista de clientes cadastrados no banco
        self._clientes = []

    def criar_cliente(self, nome, email, cpf):
        """
        Cria um novo cliente e adiciona ao banco.
        (Não há validação de CPF duplicado nesta fase)
        """
        cliente = Cliente(nome, email, cpf)
        self._clientes.append(cliente)

    def criar_conta(self, cpf):
        """
        Cria uma nova conta para um cliente existente.
        O número da conta é baseado na quantidade de contas do cliente.
        """
        for cliente in self._clientes:
            if cliente.cpf == cpf:
                numero = len(cliente._contas) + 1
                conta = Conta(numero, cliente)
                cliente._contas.append(conta)
                return numero

        return None

    def deposito(self, valor, cpf, numero):
        """
        Realiza um depósito em uma conta específica.
        """
        for cliente in self._clientes:
            if cliente.cpf == cpf:
                conta = cliente.buscar_conta(numero)

                if conta:
                    conta.depositar(valor)
                    return 'Depósito realizado'

                return 'Conta não encontrada'

        return 'CPF não encontrado'

    def saque(self, valor, cpf, numero):
        """
        Realiza um saque em uma conta específica.
        """
        for cliente in self._clientes:
            if cliente.cpf == cpf:
                conta = cliente.buscar_conta(numero)

                if conta:
                    conta.sacar(valor)
                    return 'Saque realizado'

                return 'Conta não encontrada'

        return 'CPF não encontrado'

    def exibir_extrato(self, cpf, numero):
        """
        Retorna o extrato (histórico de transações) de uma conta.
        """
        for cliente in self._clientes:
            if cliente.cpf == cpf:
                conta = cliente.buscar_conta(numero)

                if conta:
                    return conta.extrato()

                return 'Conta não encontrada'

        return 'CPF não encontrado'
