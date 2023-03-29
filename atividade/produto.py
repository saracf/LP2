class Produto:
    def __init__(self, nome='', preco_compra=0.0, quantidade_estoque=0, preco_venda=0.0):
        self.__nome = nome
        self.__preco_compra = preco_compra
        self.__quantidade_estoque = quantidade_estoque
        self.__preco_venda = preco_venda
    @property
    def set_nome(self, nome):
        self.__nome = nome

    @property
    def preco_compra(self):
        return self.__preco_compra
    @preco_compra.setter
    def preco_compra(self, preco_compra):
        self.__preco_compra = preco_compra
    @property
    def quantidade_estoque(self):
        return self.__quantidade_estoque
    @quantidade_estoque.setter
    def quantidade_estoque(self, quantidade_estoque):
        self.__quantidade_estoque = quantidade_estoque
    @property
    def preco_venda(self):
        return self.__preco_venda
    @preco_venda.setter
    def preco_venda(self, preco_venda):
        self.__preco_venda = preco_venda

    def definir_preco_venda(self, preco_venda):
        self.__preco_venda = preco_venda

    def vender_produto(self, quantidade):
        if quantidade <= self.__quantidade_estoque:
            self.__quantidade_estoque -= quantidade
            return True
        else:
            return False

    def comprar_produto(self, quantidade):
        self.__quantidade_estoque += quantidade
