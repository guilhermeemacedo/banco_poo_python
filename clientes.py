class Cliente:
    """
    Representa um cliente do banco.
    Um cliente pode possuir várias contas.
    """

    def __init__(self, nome, email, cpf):
        # Dados do cliente
        self._nome = nome
        self._email = email
        self._cpf = cpf

        # Lista de contas do cliente
        self._contas = []

    @property
    def cpf(self):
        """
        Retorna o CPF do cliente.
        """
        return self._cpf

    def buscar_conta(self, numero):
        """
        Busca uma conta pelo número.
        Retorna a conta se encontrada ou None caso contrário.
        """
        for conta in self._contas:
            if conta.numero == numero:
                return conta

        return None
