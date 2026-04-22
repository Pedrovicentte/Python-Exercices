from abc import ABC, abstractmethod

class BebidaQuente(ABC):
    def __init__(self):
        super().__init__()

    def preparar (self):
        print("--- Iniciando o Preparo ---")
        self.ferver_agua()
        self.misturar()
        self.servir()
        print("--- Bebida Pronta ---")
    
    def ferver_agua(self):
        print("1. Fervendo água a 100 graus Celsius.")
    
    @abstractmethod
    def misturar(self):
       pass
    
    @abstractmethod
    def servir(self):
       pass