class ManipuladorDeTributaveis:
    def calcular_impostos(self, lista_tributaveis):
        total_impostos = 0
        for tributavel in lista_tributaveis:
            total_impostos += tributavel.valor_imposto()
        return total_impostos
