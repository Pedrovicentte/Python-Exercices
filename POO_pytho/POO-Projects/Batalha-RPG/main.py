from arma import Arma
from guerreiro import Guerreiro

# Criando as armas
espada = Arma("Espada de Ferro", 25)
machado = Arma("Machado de Batalha", 40)

# Criando os guerreiros
guerreiro1 = Guerreiro("Pedro")
guerreiro2 = Guerreiro("Inimigo")

# A Batalha começa!
guerreiro1.atacar(guerreiro2) # Pedro ataca sem arma (tira 5)
print(f"Vida do Inimigo: {guerreiro2.vida}") # Deve ser 95

guerreiro1.equipar_arma(espada)
guerreiro1.atacar(guerreiro2) # Pedro ataca com a Espada (tira 25)
print(f"Vida do Inimigo: {guerreiro2.vida}") # Deve ser 70

# O Inimigo contra-ataca
guerreiro2.equipar_arma(machado)
guerreiro2.atacar(guerreiro1)
print(f"Vida do Pedro: {guerreiro1.vida}") # Deve ser 60