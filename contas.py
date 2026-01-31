from transacoes import Transacao

class Conta:
    def __init__(self, numero, cliente):
        self._numero = numero
        self._cliente = cliente
        self._saldo = 0
        self._historico_transacoes = []
    
    def depositar(self, valor):
        if valor <= 0:
            raise ValueError('Valor inválido para deposito')

       
        self._saldo += valor
        transacao = Transacao(tipo = 'deposito', valor = valor)
        self._historico_transacoes.append(transacao)

    def sacar(self, valor):
        if valor <= 0:
            raise ValueError('Valor inválido para saque')
        
        if valor > self._saldo:
            raise ValueError('Saldo insuficiente')
        
        self._saldo -= valor 
        transacao = Transacao(tipo = 'saque', valor = valor)
        self._historico_transacoes.append(transacao)

    def extrato(self):
        return self._historico_transacoes
    

        

