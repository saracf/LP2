from conta import Conta
conta1 = Conta(1, 'cliente 1', 100)
conta2 = Conta(2, 'cliente 2', 100)


#print(conta1.total_contas) #Antes de ser encapsulado
#print(f'Total de Contas: {Conta._total_contas}')
#Conta.total_contas= 4
#print(f'Total de Contas: {Conta._total_contas}') #2 também
print(conta1.get_total_contas())#Forma incorreta de acessar o método de classe
print(Conta.get_total_contas()) #Forma correta

print(dir(conta1))
print(vars(conta1))
