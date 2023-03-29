from mixins_e_interfaces.Interfaces.tributavelInterface import TributavelInterface


class ManipuladorDeTributaveis:
    def calcular_impostos(self, lista_tributaveis):
        total_impostos = 0
        for tributavel in lista_tributaveis:
            if isinstance(tributavel, TributavelInterface):
                total_impostos += tributavel.valor_imposto()
            else:
                print(f"{tributavel} não é um objeto tributável")
        return total_impostos
