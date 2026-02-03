from transacoes import Transacao


class Conta:
    """
    Representa uma conta bancária.
    A conta controla saldo e histórico de transações.
    """

    def __init__(self, numero, cliente):
        # Número identificador da conta
        self._numero = numero

        # Cliente proprietário da conta
        self._cliente = cliente

        # Saldo inicial
        self._saldo = 0

        # Histórico de transações da conta
        self._historico_transacoes = []

    @property
    def numero(self):
        """
        Retorna o número da conta.
        """
        return self._numero

    def depositar(self, valor):
        """
        Realiza um depósito na conta.
        """
        if valor <= 0:
            raise ValueError('Valor inválido para depósito')

        self._saldo += valor
        self._historico_transacoes.append(
            Transacao('deposito', valor)
        )

    def sacar(self, valor):
        """
        Realiza um saque na conta.
        """
        if valor <= 0:
            raise ValueError('Valor inválido para saque')

        if valor > self._saldo:
            raise ValueError('Saldo insuficiente')

        self._saldo -= valor
        self._historico_transacoes.append(
            Transacao('saque', valor)
        )

    def extrato(self):
        """
        Retorna o histórico de transações da conta.
        """
        return self._historico_transacoes
