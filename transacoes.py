from datetime import datetime


class Transacao:
    """
    Representa uma transação financeira (depósito ou saque).
    """

    def __init__(self, tipo, valor):
        # Tipo da transação
        self.tipo = tipo

        # Valor da transação
        self.valor = valor

        # Data e hora da transação
        self._data_hora = datetime.now()

    def __str__(self):
        """
        Retorna a transação formatada para exibição.
        """
        return (
            f'{self._data_hora.strftime("%d/%m/%Y %H:%M")} '
            f'- {self.tipo} - R$ {self.valor:.2f}'
        )

    def __repr__(self):
        """
        Representação usada ao imprimir listas de transações.
        """
        return self.__str__()
