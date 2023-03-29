from mixins_e_interfaces.mixins.conta import Conta
from mixins_e_interfaces.mixins.tributavel import Tributavel
class ContaPoupanca(Conta, Tributavel):
    def __init__(self, n, cli, sal):
        super().__init__(n, cli, sal)
        self._taxa_tributo = 0.005
    def valor_imposto(self):
        return self._saldo * self._taxa_tributo

    def sacar(self, valor):
        raise ValueError('Operação não permitida para conta poupança')