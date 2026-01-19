from Pessoa import Pessoa
from Turma import Turma
class Aluno(Pessoa):
    def __init__ (self):
        super().__init__()
        self.__id = id
        self.__matricula = None
        self.__cursos = []

    #SETTERS

    def set_alunoId(self, id):
        self.__id = id
    
    def set_matricula (self, matricula):
        self.__matricula = matricula
    
    def set_cursosAluno(self, cursos):
        self.__cursos = cursos

    #GETTERS

    def get_alunoId(self):
        return self.__id
    
    def get_matricula(self):
        return self.__matricula
    
    def get_cursosAluno(self):
        return self.__cursos
    
    #ADD & REM

    def add_cursos (self, curso):
        self.cursos.append(curso)
        
    def rem_cursos(self, curso):
        self.cursos.remove(curso)
