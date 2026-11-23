class Funcionario:
    def __init__(self, nome, salario_base=1.621):
        self.nome = nome 
        self.salario_base = salario_base

    def ganho_total(self):
        return self.salario_base

class Gerente(Funcionario):
    def __init__(self, nome):
        super().__init__(nome)

    def ganho_total(self):
        return (super().ganho_total() * 0.4) + self.salario_base

class Programador(Funcionario):
    def __init__(self, nome, salario_base=1.621):
        super().__init__(nome, salario_base)

gerente = Gerente("Felipe")
gerente.ganho_total()
print(f"o funcionario {gerente.nome} recebeu {gerente.ganho_total()} reais")
programmer = Programador("José")
programmer.ganho_total()
print(f"o funcionario {programmer.nome} recebeu seus {programmer.ganho_total()}")
