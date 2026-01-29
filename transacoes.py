from datetime import datetime


class Transacao: 
    def __init__(self, tipo, valor):
        self._tipo = tipo
        self._valor = valor
        self._data_hora = datetime.now()
        
