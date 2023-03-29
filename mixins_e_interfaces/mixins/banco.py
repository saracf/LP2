class Banco:
    def __init__(self, num, nome):
        self._num = num
        self._nome = nome
        self._contas = []
        self._caixa_geral = 0