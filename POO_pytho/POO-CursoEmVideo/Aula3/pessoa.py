class BiscoitoCoração:
    def __init__(self ):
        # Atributos do biscoito
        self.tamanho = "Grande"
        self.forma = "Coração"
        self.massa = "Baunilha"
        self.peso = 150  # em gramas
        self.cobertura = "Chocolate"
        self.cozido = True
        self.temperatura = 55  # em graus Celsius

        # METODOS
    def confeitar(self):
        print(f"Fazendo massa de {self.massa}...")
        print(f"Escolhendo forma de tamanho {self.tamanho} para o biscoito...")
        print(f"Confeitando o bolo em forma de {self.forma}...")

    def cozinhar(self):
        self.cozido = True
        self.temperatura = 180
        print("Cozinhando o biscoito...")

    def congelar(self):
        if self.temperatura == -10:
            print("Congelando biscoito...")
        
    def cobrir(self):
        print(f"Cobrindo o biscoito com cobertura de {self.cobertura}...")

    def podeComer(self):
        if self.cozido == True:
            if self.temperatura <= 10:
                print("O biscoito está pronto para ser comido!")
                return True
            else:
                print("O biscoito ainda não pode ser comido...")
        
    def comer(self):
        if self.podeComer():
            print("Comendo biscoito..")
        else:
            print("O biscoito não pode ser comido ainda.")
                