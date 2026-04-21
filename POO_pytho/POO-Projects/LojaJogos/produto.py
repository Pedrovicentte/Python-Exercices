class Produto():
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def mostrar_detalhes(self):
        return f"Produto: {self.nome} | Preço: {self.preco}"