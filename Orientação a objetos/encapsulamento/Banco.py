
class Banco:
    __slots__ = ['_num', '_nome', '_contas']
    def __init__(self, numero, nome):
        self._num = numero
        self._nome = nome
        self._contas = []