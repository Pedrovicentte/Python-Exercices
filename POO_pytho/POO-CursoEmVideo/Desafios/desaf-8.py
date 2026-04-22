from abc import ABC, abstractmethod
import math

class Poligono(ABC):
    def __init__(self, qtd_lados):
        self.qtd_lados = qtd_lados
    
    @abstractmethod
    def perimetro(self):
        pass
    
    @abstractmethod
    def area(self):
        pass

class Quadrado(Poligono):
    def __init__(self, qtd_lados, lado):
        super().__init__(qtd_lados)
        self.lado = lado
        
    def area(self):
        print(f"A area do quadrado é de {4*4} cm².")
    
    def perimetro(self):
        print(f"O perimetro do quadrado é de {4 * self.lado} cm.")


class Circulo(Poligono):
    def __init__(self, qtd_lados, raio):
        super().__init__(qtd_lados)
        self.raio = raio
        
    def area(self):
        print(f"A area do circulo é de {self.qtd_lados * (self.raio ** 2)} cm².")
    
    def perimetro(self):
        print(f"O perimetro do circulo é de {2 * self.qtd_lados * self.raio:.2f} cm.")
        
q1 = Quadrado(4,5)
c1 = Circulo(3.14, 20)

print("-"*30)
q1.area()
q1.perimetro()
print("-"*30)
c1.area()
c1.perimetro()
print("-"*30)