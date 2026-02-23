from rich import print

class Caneta():
    def __init__(self, cor):
        self.cor = cor
        self.tampada = True
    
    def destampar_caneta(self):
        self.tampada = False

    def escrever(self, msg):
        if self.tampada == True:
            print("A caneta está tampada!")
        elif self.cor == "azul":
            print (f"[blue]{msg}[/]")
        elif self.cor == "vermelha":
            print (f"[red]{msg}[/]")
        elif self.cor == "verde":
            print (f"[green]{msg}[/]")
        else:
            print(" :no_entry_sign: A caneta está tampada!")

    def quebrar_linha(self, qtd):
        print("\n" * qtd)

c1 = Caneta("azul")
c2 = Caneta("vermelha")
c3 = Caneta("verde")

c1.destampar_caneta()
c2.destampar_caneta()


c1.escrever("Olá tudo bem")
c1.quebrar_linha(2)
c2.escrever("Olá, Gafanhoto!")
c3.escrever("Vamos exercitar!")