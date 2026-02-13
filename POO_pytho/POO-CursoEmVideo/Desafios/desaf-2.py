from rich import print
from rich.panel import Panel

class Produto():
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        conteudo = f"{self.nome:^30}\n{"":-^30}\n{self.preco:.^30,.2f}"
        return Panel(conteudo,
                    title="Produto",
                    width=35)

p1 = Produto("iPhone 17 Pro Max", 17000)
print(p1.etiqueta())

p2 = Produto("Notebook Gamer Mancer", 8000)
print(p2.etiqueta())