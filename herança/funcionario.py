class Funcionario:
    def __init__ (self, nome, cpf, _salario):
        self._nome = nome
        self.cpf = cpf
        self._salario = _salario

    def get_bonifica(self):
        return self._salario * 0.1