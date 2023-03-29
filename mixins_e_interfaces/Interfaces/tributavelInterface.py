import abc


class TributavelInterface(abc.ABC):
    '''Classe que contém operações de um objeto tributável. As
    subclasses concretas devem sobrescrever o método valor_imposto.
    '''

    @abc.abstractmethod
    def valor_imposto(self):
        '''aplica taxa de imposto sobre um determinado valor do objeto'''
        pass


class SeguroDeVida:
    def __init__(self, valor, titular, apolice):
        self._valor = valor
        self._titular = titular
        self._apolice = apolice

TributavelInterface.register(ContaCorrente)
TributavelInterface.register(SeguroDeVida)
