class Filme:
    def __init__(self, titulo, diretor, ano_lancamento):
        self.titulo = titulo
        self.diretor = diretor
        self.ano_lancamento = ano_lancamento

    def __str__(self):
        return (
            f"Filme: {self.titulo} | Diretor(a): {self.diretor} | {self.ano_lancamento}")

filme_info = Filme("Interstelar", "Christopher Nolan", 2014)
print(filme_info)
