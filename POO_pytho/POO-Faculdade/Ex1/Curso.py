from Aluno import Aluno
from Turma import Turma

class Curso():
    def __init__(self):
        self.__id = None
        self.__nome = None
        self.__turmas = []
        self.__alunos = []

    #SETTERS
     
    def set_idCurso (self, id):
        self.__id = id
    
    def set_nomeCurso(self, nome):
        self.__nome = nome

    def set_turmaCurso (self, turma):
        self.__turmas = turma

    def set_alunosCurso (self, alunos):
        self.__alunos = alunos
    #GETTERS 

    def get_idCurso (self):
        return self.__id
    
    def get_nomeCurso (self):
        return self.__nome
    
    def get_turmaCurso (self):
        return self.__turmas
    
    def get_alunosCurso (self):
        return self.__alunos
    
    #ADD & REM

    def add_turma (self, turma):
        self.__turmas.append(turma)
    
    def rem_turma(self,turma):
        self.__turmas.remove(turma)
    
    def add_aluno(self, aluno):
        self.__alunos.append(aluno)

    def rem_aluno(self, aluno):
        self.__alunos.remove(aluno)

    #METHODS

    def addTurma(self, turma):
        self.__turmas.append(turma)
        for aluno in turma.get_alunosTurma():
            if aluno not in self.__alunos:
                self.__alunos.append(aluno)

    def profTurma(self):
        for turma in self.get_turmaCurso():
            print(f"Professor: {turma.get_profTurma().get_nome()}")

    def listarAlunos(self):
        for turma in self.get_turmaCurso():
            print(f"Turma: {self.__nome}")
            for aluno in turma.get_alunosTurma():
                    print(f"- {aluno.get_nome()}")

    def listarTurma(self):
        if not self.__turmas:
            print("Não há turmas neste curso")
        print(f"Turmas e alunos do curso: {self.__nome}")
        for turma in self.__turmas:
            if turma.get_alunosTurma():
                for aluno in turma.get_alunosTurma():
                    print(f"- {aluno.get_nome()}")
            else:
                print("Não há alunos nesta turma")