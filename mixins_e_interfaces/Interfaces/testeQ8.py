from mixins_e_interfaces.mixins.contacorrente import ContaCorrente
from mixins_e_interfaces.mixins.contapoupanca import ContaPoupanca
from mixins_e_interfaces.mixins.segurodevida import SeguroDeVida
from mixins_e_interfaces.mixins.manipulador_de_tributaveis import ManipuladorDeTributaveis

cc1 = ContaCorrente(1, 'Fulano', 1000)
cc2 = ContaCorrente(2, 'Beltrano', 2000)
cp = ContaPoupanca(3, 'Ciclano', 5000)
sv = SeguroDeVida(4, 'Sara', 10000)

lista = [cc1, cc2, cp, sv, 'objeto não tributável']

manipulador = ManipuladorDeTributaveis()
total_impostos = manipulador.calcular_impostos(lista)
print(total_impostos)
