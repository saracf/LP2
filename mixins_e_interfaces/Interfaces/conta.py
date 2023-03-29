import abc
class Historico:
    pass
class Conta(abc.ABC):
    def __init__(self, n, cli, sal):
        self._numero = n
        self._titular = cli
        self._saldo = sal
        self._extrato = Historico()
    def atualiza(self, taxa):
        pass
    def get_saldo(self):
        return self._saldo
    @abc.abstractmethod
    def sacar(self, valor):
        pass
