class ContadorPassos:
    def __init__(self):
     self.passos = 0  

    def andar(self):
     self.passos += 1

    def correr(self):
     self.passos += 5

    def resetar(self):
      self.passos = 0

pessoa = ContadorPassos()
pessoa.andar()
pessoa.correr()
pessoa.correr()
print(pessoa.passos)
