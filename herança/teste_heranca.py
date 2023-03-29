from herança.estagiario import Estagiario
from herança.funcionario import Funcionario
from herança.gerente import Gerente
from herança.presidente import Presidente

f1 = Funcionario('a', 12, 100)
g1 = Gerente('Sara', 11111111, 200, 1000, '2332')
p1 = Presidente('Limeira', 1234, 30000)
e1 = Estagiario()

print(f1.get_bonifica())
print(g1.get_bonifica())
print(p1.get_bonifica())

