from bebidaQuente import BebidaQuente

class Cafe(BebidaQuente):
    def __init__(self):
        super().__init__()
    
    def misturar(self):
       print("2. Passando água pressurizada pelo pó de café moído.")
    
    def servir(self):
       print("3. Servindo em xícara pequena .")