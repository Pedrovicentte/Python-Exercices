class Aplicativo():
    def __init__(self, nome, consumo = 0):
        self.nome = nome
        self.consumo_ram = consumo
        
    def __str__(self):
        return f"App: {self.nome} | Consumo: {self.consumo_ram}"