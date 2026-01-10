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