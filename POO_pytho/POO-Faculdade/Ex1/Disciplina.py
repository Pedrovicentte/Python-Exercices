from Turma import Turma

class Disciplina():
    def __init__(self):
        self.__id = None
        self.__nome = None

    #SETTERS

    def set_idDisciplina (self, id):
        self.__id = id

    def set_nomeDisciplina (self, nome):
        self.__nome = nome

    #GETTERS

    def get_idDisciplina (self):
        return self.__id

    def get_nomeDisciplina (self):
        return self.__nome
