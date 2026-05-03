from personagem import Personagem
from rich import print

class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Pulo Giratório", "Soco"]
        
    def curar(self):
        valor_cura = super().curar()
        print(f"[blue]{self.nome}[/] enrolou uma atadura nos ferimentos e [green]recuperou {valor_cura  } pontos[/] de vida. ")
        return valor_cura