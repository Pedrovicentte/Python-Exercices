from funcionario import Funcionario

class FuncionarioMensalista(Funcionario):
    def __init__(self, nome, sal_bruto, salario = 0):
        super().__init__(nome, sal_bruto, salario)
        
    
    def calc_sal(self):
        self.salario = self.sal_bruto - (self.sal_bruto * 0.075)
        super().calc_sal()
        return self.salario