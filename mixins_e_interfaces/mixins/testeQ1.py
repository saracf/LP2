from mixins_e_interfaces.mixins.contacorrente import ContaCorrente
from mixins_e_interfaces.mixins.contapoupanca import ContaPoupanca
cc = ContaCorrente(1, "João", 1000.00)
cp = ContaPoupanca(2, "Maria", 5000.00)
imposto_cc = cc.valor_imposto()
imposto_cp = cp.valor_imposto()
print(f'''O imposto da conta corrente é R$ {imposto_cc:.2f}
        O imposto da conta poupança é R$ {imposto_cp:.2f}''')