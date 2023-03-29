from mixins_e_interfaces.mixins.tributavel import TributavelMixIn


class SeguroDeVida(TributavelMixIn):
    def __init__(self, numero, valor, titular):
        self._numero = numero
        self._valor = valor
        self._titular = titular
        self._taxa_tributo = 0.05
        self._valor_fixo = 34

    def valor_imposto(self):
        return self._valor * self._taxa_tributo + self._valor_fixo
