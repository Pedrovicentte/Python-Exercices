from rich import print
from rich.panel import Panel

class Churrasco():
    #Atribustos de Classe
    consumo_padrao:float = 0.400
    preco_kg:float = 82.40

    def __init__(self, titulo, quant):
        self.titulo = titulo
        self.quant = quant
    
    def calcular_qtd_carne(self) -> float:
        return self.quant * Churrasco.consumo_padrao

    def calcular_custo_total(self) -> float:
        return self.calcular_qtd_carne() * Churrasco.preco_kg
    
    def calcular_preco_individual(self) -> float:
        return self.calcular_custo_total() / self.quant
    
    def analisar(self):
        consumo = (f"Analisando o [green]{self.titulo}[/] com [blue]{self.quant} convidados...[/]\n"
                  f"Cada participante comerá {self.consumo_padrao}Kg custa R$ {self.preco_kg} reais.\n"
                  f"Recomedo [blue]comprar {self.calcular_qtd_carne():.3f} Kg[/] de carne.\n"
                  f"O custo total será de [green]R$ {self.calcular_custo_total():.2f}[/] reais.\n"
                  f"Cada pessoa pagará [yellow]R$ {self.calcular_preco_individual():.2f} [/]reais."
                )
        return Panel(consumo, 
                     title=self.titulo,
                     width=60)


c1 = Churrasco("Churalegas", 15)
print(c1.analisar())