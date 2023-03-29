from mixins_e_interfaces.mixins.segurodevida import SeguroDeVida
seguro = SeguroDeVida(123, 1000, 'Fulano')
imposto = seguro.valor_imposto()
print('Imposto:', imposto)
