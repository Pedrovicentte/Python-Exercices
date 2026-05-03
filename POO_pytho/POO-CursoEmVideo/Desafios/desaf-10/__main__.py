from caminhao import Caminhao
from moto import Moto
from drone import Drone
from rich import print

def main():
    dist = 60
    
    entrega = Caminhao(dist)
    print(f"Frete de {type(entrega).__name__} em {dist} Km = {entrega.calc_frete()}")

if __name__ == "__main__":
    main()