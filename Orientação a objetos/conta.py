from historico import Historico

class Conta:
    #Para definir os atributos precisamos di init
    def __init__(self, n, t, s, l=100): #Variaveis locais
        self._numero = n #Variveis de objeto
        self.titular = t
        self._saldo = s #atributo provado
        self._limite = l
        self._historico = Historico()
        self.status = st

    #Métodos de acesso
    @property
    def saldo(self):
        return self._saldo
    #Não faz sentido o set para o saldo, pois já temos o sacar e depositar


    @property
    def limite(self):
        return self._limite
    @limite.setter
    def limite(self, valor):
        self._limite = valor

    def limite(self, valor):
        return self._numero
    #Comportamentos
    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo = self.saldo - valor
            self.historico.transacoes.append(f'Saque de {valor}')
            return True

    def depositar(self, valor):
        self.saldo += valor
        self.historico.transacoes.append(f'Depósito de {valor}')

    #Como fazer uma transferência de uma conta para outra?
    def transfere(self, c_destino, valor):
        self.sacar(valor)
        c_destino.depositar(valor)
        self.historico.transacoes.append(f'Tranferência de {valor}')

    def extrato(self):
        self.historico.imprime()

    def __str__(self):
        return f'{self.__class__.__name__} {self._numero}: {self.titular} Saldo:{self.saldo}'