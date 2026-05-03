from transporte import Transporte

class Moto(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)
        self.fator = 0.50
    
    def calc_frete(self):
       return f"R$ {self.fator * self.distancia}"