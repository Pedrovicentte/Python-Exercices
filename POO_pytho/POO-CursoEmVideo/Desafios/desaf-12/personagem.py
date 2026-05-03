from abc import ABC
from abc import abstractmethod
import random
from rich import print

class Personagem(ABC):
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.golpes = []
        
    def atacar(self, alvo, força):
        golpe = random.choice(self.golpes)
        print(f"[green]{self.nome}[/]({self.vida}) atacou [red]{alvo.nome}[/]({alvo.vida}) com um(a) [blue]{golpe}[/] de força {força}\n[blue]{alvo.nome}[/] recebeu [red]dano de {alvo.receber_dano(força)}[/]!")
    
    def receber_dano(self, dano):
        dano_recebido = int(random.uniform(0, dano))
        return dano_recebido
    
    @abstractmethod
    def curar(self):
        cura = int(random.uniform(0, 100))
        return cura