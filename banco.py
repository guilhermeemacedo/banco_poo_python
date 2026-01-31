from clientes import Cliente
from contas import Conta
class Banco:
    def __init__(self):
        self._clientes = []
        self._contas = []
    
    def criar_cliente(self, nome, email, cpf):
        cliente = Cliente(nome, email, cpf)
        self._clientes.append(cliente)

    def criar_conta(self, cpf):
        numero = len(self._contas)+1
        for cliente in self._clientes:
            if cliente.cpf == cpf:
                conta = Conta(numero, cliente)
                self._contas.append(conta)
                cliente._contas.append(conta)
    
    def mostra_extrato(self, cpf, numero_da_conta):
        cliente_encontrado = None

        for cliente in self._clientes:
            if cpf == cliente.cpf:
                cliente_encontrado = cliente
                break

        if cliente_encontrado is None:
            return 'erro, cpf nao identificado'

        for conta in cliente_encontrado._contas:
            if numero_da_conta == conta.numero:
                return conta.extrato()

        return 'erro, numero da conta nao identificado'

        
                   


                



