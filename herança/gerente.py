from funcionario import Funcionario
class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, senha, qtd):
        #Funcionario.__init__(self, nome, cpf, salario)
        super().__init__(nome, cpf, salario)
        self._senha = senha
        self.qtd = qtd

    def autentic(self, senha):
        if self._senha == senha:
            return True
        else:
            return False


    def get_bonifica(self):
        return self._salario * 0.1
        #return self._salario * 0.1 + 1000
        #return super().get_bonifica() + 1000