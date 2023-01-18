from cliente import Cliente
from conta import Conta

cli1 = Cliente('Fulano', 'Silva', '99999999999')
c1 = Conta(1, cli1, 1000, 200)
print(dir(c1))

'''Agora tudo vem com '_Conta__saldo' porém não vem com o slado, pq ele está encapsulado '''
#c1._Conta_saldo=10000
#print(c1._Conta_saldo)
'''se tem __ é subentendido que não há deve mecher lá'''

#print(c1.limite)
print(c1._saldo)
#c1.limite=300
#print(c1.limite)