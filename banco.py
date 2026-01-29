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
                

