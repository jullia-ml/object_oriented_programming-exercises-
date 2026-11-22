class AnimalZoo:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Leao(AnimalZoo):
    def __init__(self, nome, idade, tamanho_juba):
        super().__init__(nome, idade)
        self.tamanho_juba:str = tamanho_juba
    

class Elefante(AnimalZoo):
    def __init__(self, nome, idade, tamanho_presa):
        super().__init__(nome, idade)
        self.tamanho_presa:int = tamanho_presa

animal_0 = Leao("Simba", 12, "média")
animal_1 = Elefante("Dumbo", 15, 50)
print(f"{animal_0.nome} tem {animal_0.idade} anos e sua juba é {animal_0.tamanho_juba}")