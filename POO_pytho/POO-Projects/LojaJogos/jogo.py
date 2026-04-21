from produto import Produto

class Jogo(Produto):
    def __init__(self, nome, preco, genero):
        super().__init__(nome, preco)
        self.genero = genero
    
    def mostrar_detalhes(self):
        jogo_base = super().mostrar_detalhes()
        return f"{jogo_base} | Gênero: {self.genero}"