from mixins_e_interfaces.mixins.conta import Conta

class ContaCorrente(Conta):
    def __init__(self, n, cli, sal):
        super().__init__(n, cli, sal)
        self._taxa_tributo = 0.01

    def valor_imposto(self):
        return self._saldo * self._taxa_tributo
    def sacar(self, valor):
        return super().sacar(valor)
