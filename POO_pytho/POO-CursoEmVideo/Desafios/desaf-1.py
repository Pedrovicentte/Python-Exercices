class Funcionario():
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self):
        return f"Olá sou {self.nome} sou do setor de {self.setor} da empresa {self.cargo}"


c1 = Funcionario("Maria", "TI", "Curso em Video")
print(c1.apresentacao())

c2 = Funcionario("Pedro", "Engenheiro", "abc")
print(c2.apresentacao())