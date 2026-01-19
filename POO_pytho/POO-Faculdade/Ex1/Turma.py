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

    def set_disciplinaTurma(self, disciplina):
        self.__disciplina = disciplina
    #GETTERS

    def get_idTurma (self):
       return self.__id

    def get_profTurma(self):
        return self.__professor
    
    def get_disciplina(self):
        return self.__disciplina
    
    def get_alunosTurma (self):
        return self.__alunos
    # ADD & REM

    def add_aluno (self, aluno):
        self.__alunos.append(aluno)
    
    def rem_aluno(self, aluno):
        self.__alunos.remove(aluno)

    #METHODS
        
    def alunosTurma(self):
        for aluno in self.__alunos:
            print(aluno.get_nome())