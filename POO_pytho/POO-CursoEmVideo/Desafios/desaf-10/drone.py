from transporte import Transporte

class Drone(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)
        self.fator = 9.50
        
    def calc_frete(self):
        if self.distancia > 10:
            return "Raio máximo de até 10km"
        else:
           return f"R$ {self.fator * self.distancia}"