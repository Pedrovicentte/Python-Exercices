from abc import ABC
from abc import abstractmethod
from rich.panel import Panel
from rich import print

class Funcionario(ABC):
    def __init__(self, nome,sal_bruto, salario):
        self.nome = nome 
        self.sal_bruto = sal_bruto
        self.salario = salario
        self.sal_min = 1612
        self.inss = 7.5
    
    @abstractmethod
    def calc_sal(self):
        conteudo = Panel(
            f"O salário de [blue]{self.nome}[/] [magenta]({type(self).__name__})[/] é de [green]R${self.salario:.2f}[/] e corresponde a [yellow]{self.analisar_sal():.1f} salários mínimos[/].",
            title="Análise de Salário",
            style='white',
            width= 50
        )
        print(conteudo)
        
    def analisar_sal(self):
        numero_salarios = self.salario / self.sal_min
        return numero_salarios
    