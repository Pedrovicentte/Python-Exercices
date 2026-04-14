from funcionario import Funcionario
from programador import Programador
from gerente import Gerente

# Criando os funcionários
func_comum = Funcionario("Sônia", 2000)
dev = Programador("Pedro", 4000, "Python")
chefe = Gerente("Joana", 8000, "TI")

# Testando os métodos (Todos têm o mostrar_info, mesmo sem você ter escrito nas filhas!)
print(func_comum.mostrar_info())
print(dev.mostrar_info()) 
print(chefe.mostrar_info())

# Testando as lógicas de Bônus diferentes
print("--- Bônus ---")
print(f"Bônus comum: R$ {func_comum.calcular_bonus()}") # Deve ser 200
print(f"Bônus do Dev: R$ {dev.calcular_bonus()}")       # Deve ser 400
print(f"Bônus da Chefia: R$ {chefe.calcular_bonus()}")  # Deve ser 1600 (20%)