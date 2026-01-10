class Pessoa():
    def __init__(self):
        self.id = None
        self.nome = None
        self.idade = None 

    #SETTERS 
    def set_nome (self , nome):
        self.__nome = nome

    def set_id (self):
        self.__id = id

    def set_idade (self,idade):
        self.__idade = idade
    
    #GETTERS
    def get_id (self):
        return self.__id
    
    def get_nome (self):
        return self.__nome
    
    def get_idade (self):
        return self.__idade