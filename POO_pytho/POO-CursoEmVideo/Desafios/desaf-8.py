from rich import print
from rich.panel import Panel

canais = [1, 2 ,3 ,4 ,5]
volume = []

class ControleRemoto():
    def __init__(self):
        self.tv_ligada = False 
        self.canal = 1
        self.volume = 1

    def ligar_tv(self):
        self.tv_ligada = False

        while True:
            if not self.tv_ligada:
                tela = "[red]A tv está desligada[/]"
            else:
                tela = f"CANAL = [white on yellow] 1 [/] 2  3  4  5 \nVOLUME = 10"
            print(Panel(tela, title="[ TV ]", width=50))

            comando = input("< CH1 >   - VOL2 +   ")
            if comando == "@":
                self.tv_ligada = not self.tv_ligada
            if comando == ">":
                self.mudar_cannal()
                
    
    def mudar_cannal(self):
        canal_atual = self.canal
        for i in range(len(canais)):
            if canal_atual == canais[i]:
                tela = f"CANAL = [white on yellow] {canais[i]} [/]\nVOLUME = 10"
                print(Panel(tela, title="[ TV ]", width=50))
                self.canal += 1
                    
canal = ControleRemoto()
canal.ligar_tv()
