class Funcionario():
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
        
    def calcular_bonus(self):
        return self.salario * 0.10
    
    def mostrar_info(self):
        return f"Nome: {self.nome} | Salário: R${self.salario:.2f} reais."