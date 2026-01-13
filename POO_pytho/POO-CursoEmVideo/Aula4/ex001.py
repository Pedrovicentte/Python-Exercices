#Declaração de Classe

class Gafanhoto():
    def __init__(self): #Método Construtor
        #Atributos de Instância
        self.nome = ""
        self.idade = 20
    
    #Métodos de Instância
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")
    
#Declaração de Objetos

g1 = Gafanhoto()
g1.nome = "João"
g1.idade = 15
g1.aniversario()
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = "Maria"
g2.idade = 22
print(g2.mensagem())