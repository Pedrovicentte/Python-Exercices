from funcionario import Funcionario

class Programador(Funcionario):
    def __init__(self,  nome, salario, linguagem):
        super().__init__(nome, salario)
        self.linguagem = linguagem
        
    def mostrar_info(self):
        texto_pai = super().mostrar_info()
        return f"{texto_pai} | Linguagem: {self.linguagem}"