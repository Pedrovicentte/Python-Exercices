class Carrinho:
  

    def __init__(self):
        self.itens = []
    
    def adicionar_item(self, produto):
        self.itens.append(produto)
        print(f"Jogo {produto.nome} ao carrinho!")
    
    def calcular_total(self):
        total = 0
        for produto in self.itens:
            total += produto.preco
        return total
    
    