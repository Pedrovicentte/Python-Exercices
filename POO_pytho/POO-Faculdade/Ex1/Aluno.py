from Pessoa import Pessoa
from Turma import Turma
class Aluno(Pessoa):
    def __init__ (self):
        super().__init__()
        self.__id = id
        self.__matricula = None
        self.__cursos = []

    #SETTERS

    def set_alunoId(self):
        self.__id = id
    
    def set_matricula (self, matricula):
        self.__matriculas = matricula
    
    def set_cursosAluno(self, curso):
        self.__cursos = curso

    
    #GETTERS

    def get_alunoId(self):
        return self.__id
    
    def get_matricula(self):
        return self.__matricula
    
    def get_cursosAluno(self):
        return self.__cursosAluno
    
    #ADD & REM

    def add_cursos (self, curso):
        self.cursos.append(curso)
        
    def rem_cursos(self, curso):
        self.cursos.remove(curso)
