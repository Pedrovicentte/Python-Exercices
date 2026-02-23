from rich import print
from rich.panel import Panel

class Churrasco():
    def __init__(self, titulo, quant):
        self.titulo = titulo
        self.quant = quant
    
    def analisar(self):
        quantidade_carne = 0.4 * self.quant
        custo_total = quantidade_carne * 82.40
        preco_ind = custo_total / self.quant
        consumo = (f"Analisando o [green]{self.titulo}[/] com [blue]{self.quant} convidados...[/]\n"
                  f"Cada participante comerá 0.4Kg custa R$ 82,40\n"
                  f"Recomedo [blue]comprar {quantidade_carne:.3f} Kg[/] de carne.\n"
                  f"O custo total será de [green]R$ {custo_total:.2f}[/] reais.\n"
                  f"Cada pessoa pagará [yellow]R$ {preco_ind:.2f} [/]reais."
                )
        return Panel(consumo, 
                     title=self.titulo,
                     width=60)


c1 = Churrasco("Churalegas", 3)
print(c1.analisar())