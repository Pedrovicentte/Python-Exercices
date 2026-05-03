from funcionario import Funcionario

class FuncionarioHorista(Funcionario):
    def __init__(self, nome, valor_hora, horas_trab):
        super().__init__(nome,sal_bruto=0, salario=0)
        self.valor_hora = valor_hora
        self.horas_trab = horas_trab
    
    def calc_sal(self):
        self.sal_bruto = self.valor_hora * self.horas_trab
        self.salario = self.sal_bruto - (self.sal_bruto * 0.075)
        super().calc_sal()
        return self.salario
