class Caneta:
    def __init__(self, cor):
        self.cor = cor
        self.tampada = False

    def destampar(self):
        self.tampada = True

    def tampar(self):
        self.tampada = False

    def escrever(self):
        if not self.tampada:
            print(f"Escrevendo em {self.cor}")
        else:
            print(f"Erro! Não posso escrever com a caneta tampada!")

caneta = Caneta("azul")
caneta.destampar()
caneta.tampar()
caneta.escrever()