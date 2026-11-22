class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco: float = preco

class CarrinhodeCompras:
    def __init__(self):
        self.carrinho = []

    def add_produto(self, produto):
        self.carrinho.append(produto)
        print(f"O {produto.nome} foi adicionado ao carrinho")

    def remover_produto(self, produto):
        self.carrinho.remove(produto)
        print(f"O {produto.nome} foi removido do carrinho")

    def calcular_valor_total(self):
        total = 0
        for produto in self.carrinho:
            total = produto.preco + total
        print(f"O valor total das compras é {total}")
            

compra1 = Produto("Pão", 8.50)
compra2 = Produto("Bolo", 13.50)
compras = CarrinhodeCompras()
compras.add_produto(compra1)
compras.add_produto(compra2)
compras.calcular_valor_total()
