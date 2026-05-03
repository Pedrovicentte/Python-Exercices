from caminhao import Caminhao
from moto import Moto
from drone import Drone
from rich.table import Table
from rich.console import Console

def main():
    dist = 15
    entrega = Caminhao(dist)
    console = Console()
    
    viagem = [Moto(dist), Caminhao(dist), Drone(dist)]
    
    table = Table(title="Tabela de Fretes")
    
    table.add_column("Veículo", style="cyan")
    table.add_column("Distância", justify="center", style="red")
    table.add_column("Valor do Frete", style="blue")
    
    for i in viagem:
        nome_veiculo = type(i).__name__
        distancia = f"{i.distancia} Km"
        valor_frete = i.calc_frete()
        table.add_row(nome_veiculo, distancia, valor_frete)
        
    console.print(table)

if __name__ == "__main__":
    main()