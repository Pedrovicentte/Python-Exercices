from personagem import Personagem
from rich import print
class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Bola de Fogo", "Magia de gelo", "Lança Elétrica"]
    
    def curar(self):
        print(f"[blue]{self.nome}[/] fez uma magia de cura e [green]recuperou {super().curar()} pontos[/] de vida. ")