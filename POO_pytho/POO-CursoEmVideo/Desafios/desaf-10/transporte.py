from abc import ABC
from abc import abstractmethod

class Transporte(ABC):
    def __init__(self, distancia):
        self.distancia = distancia
        self.frete = None
    
    @abstractmethod
    def calc_frete(self, frete):
        return f"R$ {frete * self.distancia} reais."