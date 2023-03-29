from mixins_e_interfaces.mixins.contacorrente import ContaCorrente

cc = ContaCorrente(123, 'Fulano', 1000)
print('Saldo:', cc.get_saldo())
imposto = cc.valor_imposto()
print('Imposto:', imposto)
cc.sacar(imposto)
print('Saldo após o débito do imposto:', cc.get_saldo())
