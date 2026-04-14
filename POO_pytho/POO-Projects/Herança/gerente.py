from funcionario import Funcionario

class Gerente(Funcionario):
    def __init__(self, nome, salario, departamento):
        super().__init__(nome, salario)
        self.departamento = departamento
    
    def calcular_bonus(self):
        return self.salario * 0.20
    
    def mostrar_info(self):
        texto_pai = super().mostrar_info()
        return f"{texto_pai} | Departamento: {self.departamento}"