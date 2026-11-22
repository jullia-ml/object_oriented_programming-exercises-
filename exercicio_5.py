class CalculadoraGeometrica:
    def calcular_area(self, base, altura=None):
        if altura is None:
            lado = base
            return lado * lado
        else:
            return base * altura

calc = CalculadoraGeometrica()

print("Área do quadrado (lado=5):", calc.calcular_area(5))
print("Área do retângulo (4x6):", calc.calcular_area(4, 6))
