from conta import Conta
conta3 = Conta(2, 'cliente 2', 100, 1000, False)
conta3.blocked
print(conta3)
print(conta3.blocked)
conta3.sacar(100)
conta3.close_account()
print(conta3.blocked)
conta3.depositar(3)
print(conta3._saldo)