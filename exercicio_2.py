class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self, base):
        return base * self.altura

    def calcular_perimetro(self, base):
        return 2*(base + self.largura)

retangulo1 = Retangulo(8, 9)
print(f"A área do Retângulo1 é: {retangulo1.calcular_area(base=7)}")
print(f"O perímetro do Retângulo1 é: {retangulo1.calcular_perimetro(base=8)}")

retangulo2 = Retangulo(4, 10)
print(f"A área do Retângulo2 é: {retangulo2.calcular_area(base=9)}")
print(f"O perímetro do Retângulo2 é: {retangulo2.calcular_perimetro(base=10)}")
