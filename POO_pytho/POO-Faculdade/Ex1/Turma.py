class Turma:
    def __init__(self):
        self.__id = None
        self.__professor = None
        self.__disciplina = None
        self.__alunos = []

    #SETTERS

    def set_idTurma (self, id):
        self.__id = id

    def set_profTurma (self, professor):
        self.__professor = professor

    def set_disciplina(self, disciplina):
        self.__disciplina = disciplina
    #GETTERS

    def get_idTurma (self):
       return self.__id

    def get_profTurma(self):
        return self.__professor
    
    def get_disciplina(self):
        return self.__disciplina
    
    # ADD & REM

    def add_aluno (self, aluno):
        self.__alunos.append(aluno)
    
    def rem_aluno(self, aluno):
        self.__alunos.remove(aluno)
