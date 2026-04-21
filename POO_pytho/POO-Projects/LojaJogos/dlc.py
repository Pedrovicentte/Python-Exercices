from produto import Produto

class DLC(Produto):
    def __init__(self, nome, preco, jogo):
        super().__init__(nome, preco)
        self.jogo_base = jogo
    
    def mostrar_detalhes(self):
        return f"DLC: {self.nome} | Jogo Base: {self.jogo_base}"