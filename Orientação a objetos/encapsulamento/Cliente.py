
class Cliente:
    __slots__ = ['_nome', '_endereco', '_CPF', '_idade']

    def __init__(self, n, e, cpf, i):
        self._nome = n
        self._endereco = e
        self._CPF = cpf
        self._idade = i