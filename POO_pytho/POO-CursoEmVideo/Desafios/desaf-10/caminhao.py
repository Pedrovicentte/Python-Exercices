from transporte import Transporte

class Caminhao(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)
        self.fator = 1.20
    
    def calc_frete(self):
        if self.distancia < 50:
            return  "Raio [yellow]Mínimo[/] de 50km"
        else:
           return super().calc_frete(self.fator)
