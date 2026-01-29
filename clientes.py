class Cliente:
    def __init__(self, nome, email, cpf):
        self._nome = nome 
        self._email = email
        self._cpf = cpf
        self._contas = []
        