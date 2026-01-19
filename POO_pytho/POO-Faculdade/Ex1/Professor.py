from Pessoa import Pessoa
from Turma import Turma


class Professor(Pessoa):
    def __init__(self):
        super().__init__()
        self.__id = None
        self.__matricula = None

    #SETTERS 

    def set_idProf (self, id):
        self.nome = id  
    
    def set_matriculaProf (self, matricula):
        self.matricula = matricula

    #GETTERS

    def get_idProf (self):
        return self.__id
    
    def get_matriculaProf (self):
        return self.__matricula
    
    #METHODS

    def ProfessorTurma(self):
        for prof in Turma.get_profTurma(self):
            print(prof.get_nome())