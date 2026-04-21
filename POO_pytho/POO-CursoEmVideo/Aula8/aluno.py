from pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma
        
    def fazer_matricula(self):
        print("O aluno faz matricula")

    def estudar(self):
        print(f"{self.nome} está estudando {self.curso} na turma {self.turma}")