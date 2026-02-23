from rich import print
from rich.panel import Panel

class Gamer():
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.jogos_favoritos = []
    
    def add_fav(self, jogo):
        self.jogos_favoritos.append(jogo)

    def ficha(self):
        for i in self.jogos_favoritos: 
            ficha = f"Nome real: [bold white on blue] {self.nome} [/]\nJogos Favoritos:\n[blue]:video_game: {"\n" ":video_game: ".join(self.jogos_favoritos)}[/]"
        return Panel (ficha, 
                    title=f'Jogador <{self.nick}>',
                    width=40)
    
    
j1 = Gamer("Pedro", "Slayer_destoyer2011")
j1.add_fav("God of War")
j1.add_fav("Mario Bross")
j1.add_fav("Sex with Hitler")
print(j1.ficha())

j2 = Gamer("Maria Augusta", "bunny_grill_64")
j2.add_fav("Call of Duty")
print(j2.ficha())