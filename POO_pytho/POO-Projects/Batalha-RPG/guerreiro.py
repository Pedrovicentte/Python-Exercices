class Guerreiro():
    def __init__(self, nome):
        self.nome = nome
        self.vida = 100
        self.arma_equipada = None
        
    def equipar_arma(self, nova_arma):
        if not self.arma_equipada:
            self.arma_equipada = nova_arma
            print(f"{self.nome} pegou um(a) {nova_arma.nome} !")
        else:
            print("Você ja tem uma arma equipada!")
    
    def desequipar_arma(self):
        if self.arma_equipada:
            self.arma_equipada = None
            print(f"Arma desequipada.")
        else:
            print("Você já está de mãos vazias.")
    
    def atacar(self, alvo):
        if self.arma_equipada != None:
            alvo.vida -= self.arma_equipada.dano
            print(f"{self.nome} atacou com a {self.arma_equipada.nome} e deu {self.arma_equipada.dano} de dano!")
        else:
            alvo.vida -= 5
            print(f"{self.nome} atacou com soco e deu 5 de dano.")