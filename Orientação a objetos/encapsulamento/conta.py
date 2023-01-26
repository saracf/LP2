class Conta:
    #Para definir os atributos precisamos di init
    _numero_contas = 0
    #variáel de slots para definir os objetos do tipo Conta
    __slots__ = ['_numero', '_titular', '_saldo', '_limite', '_historico', '_blocked']


    #para definir os atributos precisamos do init
    def __init__(self, n, t, s, l=100, st = False): #Variaveis locais
        self._numero = n #Variveis de objeto
        self._titular = t
        self._saldo = s #atributo provado
        self._limite = l
        self.blocked = st
        Conta._numero_contas +=1

    #Métodos de acesso

    @classmethod
    def get_numero_contas(cls):
        return Conta._numero_contas
    def close_account(self):
        if self._saldo == 0:
            self.blocked = True
            print("Conta bloqueada")
        else:
            raise ValueError("Saldo é positivo")
    def set_blocked(self, value):
        self._blocked = value

    def get_blocked(self):
        return self._blocked

    blocked = property(get_blocked, set_blocked)

    def is_active(self):
        #self.close_account != self.close_account
        if self.close_account():
            return True
    @classmethod #segunda forma
    def get_total_contas(cls):
        return Conta._total_contas

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
        if self.is_active():
            raise ValueError("Conta bloqueada")
        if self._saldo < valor:
            raise ValueError("Saldo menor que o valor solicitado")
        else:
            self._saldo = self._saldo - valor
            self._historico.transacoes.append(f'Saque de {valor}')


    def depositar(self, valor):
        self._saldo += valor
        self._historico.transacoes.append(f'Depósito de {valor}')

    #Transferência de uma conta para outra?
    def transfere(self, c_destino, valor):
        self.sacar(valor)
        c_destino.depositar(valor)
        self._historico.transacoes.append(f'Tranferência de {valor}')

    def extrato(self):
        self._historico.imprime()

    def __str__(self):
        return f'{self.__class__.__name__} {self._numero}: {self._titular} Saldo:{self._saldo}'