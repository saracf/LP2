from funcionario import Funcionario
from autenticavel import Autenticavel
class Diretor(Funcionario, Autenticavel):
    def autentica(self):
        print('Diretor autenticou!!')