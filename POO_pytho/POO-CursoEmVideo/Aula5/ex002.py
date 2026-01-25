#Declaração de Classe

class Gafanhoto():
    """
    Essa classe cria um gafanhoto, que é uma pessoa que tem nome e idade.
    
    Para criar uma nova pessoa, use
    variavel = Gafanhoto(nome, idade)

    """
    def __init__(self, nome = "null", idade = 0): #Método Construtor
        #Atributos de Instância
        self.nome = nome
        self.idade = idade

    #Métodos de Instância
    def aniversario(self):
        self.idade += 1

    def __str__(self):
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."
    
    def __getstate__(self):
        return f"Estado: nome = {self.nome}; idade = {self.idade}"
#Declaração de Objetos

g1 = Gafanhoto("João", 17)
g1.aniversario()
print(g1)
print(g1.__dict__)
print(g1.__getstate__())
 
g2 = Gafanhoto ("Claudio", 43)
print(g2)
print(g2.__getstate__())